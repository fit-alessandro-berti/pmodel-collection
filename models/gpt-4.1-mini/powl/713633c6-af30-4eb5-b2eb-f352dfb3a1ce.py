# Generated from: 713633c6-af30-4eb5-b2eb-f352dfb3a1ce.json
# Description: This process involves leasing customized drones to corporate clients for specific operational needs such as agricultural monitoring, infrastructure inspection, or event coverage. It includes client consultation to define requirements, drone customization with specialized sensors, regulatory compliance checks, fleet scheduling, pilot training, live mission support, data collection and analysis, maintenance scheduling, and feedback integration for continuous product improvement. The process ensures tailored drone solutions are delivered efficiently while managing complex logistics and regulatory environments to maximize client satisfaction and operational safety.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Client_Consult = Transition(label='Client Consult')
Needs_Assess = Transition(label='Needs Assess')
Drone_Design = Transition(label='Drone Design')
Sensor_Install = Transition(label='Sensor Install')
Compliance_Check = Transition(label='Compliance Check')
Fleet_Assign = Transition(label='Fleet Assign')
Pilot_Train = Transition(label='Pilot Train')
Mission_Plan = Transition(label='Mission Plan')
Live_Support = Transition(label='Live Support')
Data_Capture = Transition(label='Data Capture')
Data_Analyze = Transition(label='Data Analyze')
Maintenance_Set = Transition(label='Maintenance Set')
Feedback_Collect = Transition(label='Feedback Collect')
Update_Fleet = Transition(label='Update Fleet')
Billing_Process = Transition(label='Billing Process')
Contract_Close = Transition(label='Contract Close')

# Construct a POWL partial order reflecting the process logic:
# Logical approximation of dependencies from description:
# - Client Consult then Needs Assess
# - Needs Assess then parallel Drone Design + Compliance Check (since checking regs might run in parallel with design)
# - Drone Design then Sensor Install
# - After Sensor Install and Compliance Check, Fleet Assign
# - Fleet Assign then Pilot Train
# - Then Mission Plan
# - Then Live Support
# - Then Data Capture
# - Then Data Analyze
# - Then Maintenance Set and Feedback Collect (can run in parallel)
# - Feedback Collect leads to Update Fleet
# - Then Billing Process
# - Then Contract Close

nodes = [
    Client_Consult,
    Needs_Assess,
    Drone_Design,
    Sensor_Install,
    Compliance_Check,
    Fleet_Assign,
    Pilot_Train,
    Mission_Plan,
    Live_Support,
    Data_Capture,
    Data_Analyze,
    Maintenance_Set,
    Feedback_Collect,
    Update_Fleet,
    Billing_Process,
    Contract_Close
]

root = StrictPartialOrder(nodes=nodes)

# Ordering edges:

# Client Consult -> Needs Assess
root.order.add_edge(Client_Consult, Needs_Assess)

# Needs Assess -> Drone Design
root.order.add_edge(Needs_Assess, Drone_Design)
# Needs Assess -> Compliance Check (can do in parallel)
root.order.add_edge(Needs_Assess, Compliance_Check)

# Drone Design -> Sensor Install
root.order.add_edge(Drone_Design, Sensor_Install)

# Both Sensor Install and Compliance Check must complete before Fleet Assign
root.order.add_edge(Sensor_Install, Fleet_Assign)
root.order.add_edge(Compliance_Check, Fleet_Assign)

# Fleet Assign -> Pilot Train
root.order.add_edge(Fleet_Assign, Pilot_Train)

# Pilot Train -> Mission Plan
root.order.add_edge(Pilot_Train, Mission_Plan)

# Mission Plan -> Live Support
root.order.add_edge(Mission_Plan, Live_Support)

# Live Support -> Data Capture
root.order.add_edge(Live_Support, Data_Capture)

# Data Capture -> Data Analyze
root.order.add_edge(Data_Capture, Data_Analyze)

# Data Analyze -> Maintenance Set and Feedback Collect (parallel)
root.order.add_edge(Data_Analyze, Maintenance_Set)
root.order.add_edge(Data_Analyze, Feedback_Collect)

# Feedback Collect -> Update Fleet
root.order.add_edge(Feedback_Collect, Update_Fleet)

# Update Fleet and Maintenance Set must complete before Billing Process
root.order.add_edge(Update_Fleet, Billing_Process)
root.order.add_edge(Maintenance_Set, Billing_Process)

# Billing Process -> Contract Close
root.order.add_edge(Billing_Process, Contract_Close)