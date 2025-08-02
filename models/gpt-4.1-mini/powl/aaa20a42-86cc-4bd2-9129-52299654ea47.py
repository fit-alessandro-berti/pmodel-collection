# Generated from: aaa20a42-86cc-4bd2-9129-52299654ea47.json
# Description: This process manages the leasing and operational coordination of a remote drone fleet used for agricultural monitoring and environmental data collection. It includes client onboarding, drone assignment, flight scheduling, data acquisition, real-time monitoring, maintenance coordination, compliance checks, data processing, anomaly reporting, billing, and feedback collection. The process ensures seamless integration between remote operators, clients, and maintenance teams to optimize drone usage and data quality while adhering to regulatory standards and minimizing downtime.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
Client_Onboard = Transition(label='Client Onboard')
Fleet_Assign = Transition(label='Fleet Assign')
Flight_Schedule = Transition(label='Flight Schedule')
Preflight_Check = Transition(label='Preflight Check')
Launch_Drone = Transition(label='Launch Drone')
Flight_Monitor = Transition(label='Flight Monitor')
Data_Capture = Transition(label='Data Capture')
Data_Upload = Transition(label='Data Upload')
Anomaly_Detect = Transition(label='Anomaly Detect')
Maintenance_Alert = Transition(label='Maintenance Alert')
Compliance_Audit = Transition(label='Compliance Audit')
Data_Process = Transition(label='Data Process')
Report_Generate = Transition(label='Report Generate')
Client_Billing = Transition(label='Client Billing')
Feedback_Review = Transition(label='Feedback Review')

# Model the loop of flight operations
# loop body:
# A = Flight operations from Preflight_Check to Data_Upload in strict order (including monitoring concurrent with flight)
# B = parallel activities for anomaly detection, maintenance alert, and compliance audit before next loop iteration or exit
# Loop: execute flight ops, then either exit or execute anomaly/maintenance/compliance followed by flight ops again

# Flight monitoring can run in parallel with data capture and upload (partial order)
flight_ops_nodes = [
    Preflight_Check,
    Launch_Drone,
    Flight_Monitor,
    Data_Capture,
    Data_Upload
]
flight_ops_order = StrictPartialOrder(nodes=flight_ops_nodes)
flight_ops_order.order.add_edge(Preflight_Check, Launch_Drone)
flight_ops_order.order.add_edge(Launch_Drone, Flight_Monitor)
# Flight_Monitor runs concurrent with Data_Capture and Data_Upload
flight_ops_order.order.add_edge(Data_Capture, Data_Upload)

# Assume Flight_Monitor and Data_Capture+Data_Upload start after Launch_Drone, but Flight_Monitor concurrent with Data Capture/Upload:
# This is represented by no edges between Flight_Monitor and Data_Capture+Data_Upload (concurrent),
# but both start after Launch_Drone, so add edges from Launch_Drone to Flight_Monitor and Data_Capture
flight_ops_order.order.add_edge(Launch_Drone, Data_Capture)
flight_ops_order.order.add_edge(Launch_Drone, Flight_Monitor)

# After flight ops, anomaly detection, maintenance alert, compliance audit as parallel (PO no order among them)
post_flight_nodes = [Anomaly_Detect, Maintenance_Alert, Compliance_Audit]
post_flight_order = StrictPartialOrder(nodes=post_flight_nodes)  # empty order -> concurrent

# Create PO for post flight activities
post_flight_PO = post_flight_order

# After post flight activities, loop back to Preflight_Check or exit
# Loop with body = flight_ops_order, condition body = post_flight_PO (to repeat flight ops) in LOOP operator
loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_ops_order, post_flight_PO])

# After the loop ends, process remaining activities:
# Data_Process -> Report_Generate -> Client_Billing -> Feedback_Review (strict order)
post_loop_nodes = [
    Data_Process,
    Report_Generate,
    Client_Billing,
    Feedback_Review
]
post_loop_order = StrictPartialOrder(nodes=post_loop_nodes)
post_loop_order.order.add_edge(Data_Process, Report_Generate)
post_loop_order.order.add_edge(Report_Generate, Client_Billing)
post_loop_order.order.add_edge(Client_Billing, Feedback_Review)

# Before the loop, order the initial steps:
# Client Onboard -> Fleet Assign -> Flight Schedule -> loop
initial_nodes = [Client_Onboard, Fleet_Assign, Flight_Schedule]
initial_order = StrictPartialOrder(nodes=initial_nodes)
initial_order.order.add_edge(Client_Onboard, Fleet_Assign)
initial_order.order.add_edge(Fleet_Assign, Flight_Schedule)

# Build top-level partial order with:
# initial_order nodes + loop + post_loop_order nodes
root_nodes = initial_nodes + [loop] + post_loop_nodes
root = StrictPartialOrder(nodes=root_nodes)

# Add edges for initial order
root.order.add_edge(Client_Onboard, Fleet_Assign)
root.order.add_edge(Fleet_Assign, Flight_Schedule)
# Flight_Schedule --> loop
root.order.add_edge(Flight_Schedule, loop)
# loop --> Data_Process (start of post processing)
root.order.add_edge(loop, Data_Process)
# Add edges for post loop order
root.order.add_edge(Data_Process, Report_Generate)
root.order.add_edge(Report_Generate, Client_Billing)
root.order.add_edge(Client_Billing, Feedback_Review)