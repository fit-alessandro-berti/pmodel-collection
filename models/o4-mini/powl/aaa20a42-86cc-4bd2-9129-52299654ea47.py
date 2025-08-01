# Generated from: aaa20a42-86cc-4bd2-9129-52299654ea47.json
# Description: This process manages the leasing and operational coordination of a remote drone fleet used for agricultural monitoring and environmental data collection. It includes client onboarding, drone assignment, flight scheduling, data acquisition, real-time monitoring, maintenance coordination, compliance checks, data processing, anomaly reporting, billing, and feedback collection. The process ensures seamless integration between remote operators, clients, and maintenance teams to optimize drone usage and data quality while adhering to regulatory standards and minimizing downtime.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for the core activities
client_onboard    = Transition(label='Client Onboard')
fleet_assign      = Transition(label='Fleet Assign')
flight_schedule   = Transition(label='Flight Schedule')
preflight_check   = Transition(label='Preflight Check')
launch_drone      = Transition(label='Launch Drone')
flight_monitor    = Transition(label='Flight Monitor')
data_capture      = Transition(label='Data Capture')
data_upload       = Transition(label='Data Upload')
anomaly_detect    = Transition(label='Anomaly Detect')
maintenance_alert = Transition(label='Maintenance Alert')
compliance_audit  = Transition(label='Compliance Audit')
data_process      = Transition(label='Data Process')
report_generate   = Transition(label='Report Generate')
client_billing    = Transition(label='Client Billing')
feedback_review   = Transition(label='Feedback Review')

# A silent transition used to signal loop exit
skip = SilentTransition()

# Loop for anomaly handling: do an anomaly detect, then either exit or perform maintenance and repeat
anomaly_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[anomaly_detect, maintenance_alert]
)

# A single flight sequence: schedule -> preflight -> launch -> monitor -> capture -> upload -> anomaly handling
flight_sequence = StrictPartialOrder(nodes=[
    flight_schedule,
    preflight_check,
    launch_drone,
    flight_monitor,
    data_capture,
    data_upload,
    anomaly_loop
])
flight_sequence.order.add_edge(flight_schedule,   preflight_check)
flight_sequence.order.add_edge(preflight_check,   launch_drone)
flight_sequence.order.add_edge(launch_drone,      flight_monitor)
flight_sequence.order.add_edge(flight_monitor,    data_capture)
flight_sequence.order.add_edge(data_capture,      data_upload)
flight_sequence.order.add_edge(data_upload,       anomaly_loop)

# Wrap the flight sequence in a loop so multiple flights can occur
flight_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[flight_sequence, skip]
)

# After all flights, perform compliance audit, then data processing, then report generation
compliance_sequence = StrictPartialOrder(nodes=[
    compliance_audit,
    data_process,
    report_generate
])
compliance_sequence.order.add_edge(compliance_audit, data_process)
compliance_sequence.order.add_edge(data_process,     report_generate)

# Finally billing and feedback (which can proceed in parallel after reporting)
root = StrictPartialOrder(nodes=[
    client_onboard,
    fleet_assign,
    flight_loop,
    compliance_sequence,
    client_billing,
    feedback_review
])
root.order.add_edge(client_onboard,   fleet_assign)
root.order.add_edge(fleet_assign,     flight_loop)
root.order.add_edge(flight_loop,      compliance_sequence)
root.order.add_edge(compliance_sequence, client_billing)
root.order.add_edge(compliance_sequence, feedback_review)