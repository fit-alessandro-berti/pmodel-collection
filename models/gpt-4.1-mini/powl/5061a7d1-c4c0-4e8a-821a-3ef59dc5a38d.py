# Generated from: 5061a7d1-c4c0-4e8a-821a-3ef59dc5a38d.json
# Description: This complex business process involves designing and launching a tailored drone delivery solution for specialized clients. It begins with client needs analysis, followed by regulatory compliance checks and custom drone configuration. The process includes route optimization, payload testing, and integration with client logistics systems. Continuous monitoring and adaptive feedback loops ensure delivery efficiency and safety. Post-deployment support and iterative upgrades maintain operational excellence and client satisfaction over time, making the process both innovative and highly specialized.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
Client_Brief = Transition(label='Client Brief')
Needs_Analysis = Transition(label='Needs Analysis')
Regulatory_Check = Transition(label='Regulatory Check')
Drone_Design = Transition(label='Drone Design')
Component_Sourcing = Transition(label='Component Sourcing')
Assembly_Test = Transition(label='Assembly Test')
Payload_Setup = Transition(label='Payload Setup')
Route_Mapping = Transition(label='Route Mapping')
Flight_Simulation = Transition(label='Flight Simulation')
Logistics_Sync = Transition(label='Logistics Sync')
Safety_Audit = Transition(label='Safety Audit')
Pilot_Training = Transition(label='Pilot Training')
Deployment_Launch = Transition(label='Deployment Launch')
Performance_Review = Transition(label='Performance Review')
Feedback_Loop = Transition(label='Feedback Loop')
Maintenance_Plan = Transition(label='Maintenance Plan')
Upgrade_Cycle = Transition(label='Upgrade Cycle')

# Define Feedback Loop as a LOOP
# Loop body: Performance Review
# Loop condition: Feedback Loop + Maintenance Plan + Upgrade Cycle, in sequence
# Construct loop B = PO(Feedback Loop -> Maintenance Plan -> Upgrade Cycle)
loop_body = Performance_Review
loop_condition_nodes = [Feedback_Loop, Maintenance_Plan, Upgrade_Cycle]
loop_condition = StrictPartialOrder(nodes=loop_condition_nodes)
loop_condition.order.add_edge(Feedback_Loop, Maintenance_Plan)
loop_condition.order.add_edge(Maintenance_Plan, Upgrade_Cycle)

Feedback_Loop_Loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_condition])

# Define the main process PO nodes
# Partial ordering given by logical sequence and concurrency:
# Client Brief --> Needs Analysis --> Regulatory Check --> Drone Design
# After Drone Design, Component Sourcing and Assembly Test are concurrent (can happen in parallel)
# After both Component Sourcing and Assembly Test complete, Payload Setup
# Then Route Mapping --> Flight Simulation (sequence)
# Flight Simulation --> Logistics Sync --> Safety Audit --> Pilot Training (sequence)
# Pilot Training --> Deployment Launch
# Deployment Launch --> Feedback Loop Loop (continuous feedback)
# Then Post deployment support: Maintenance Plan and Upgrade Cycle are handled inside the loop,
# but also after the loop is finished, process ends.

# Build partial order nodes list
nodes_main = [
    Client_Brief, Needs_Analysis, Regulatory_Check, Drone_Design,
    Component_Sourcing, Assembly_Test,
    Payload_Setup,
    Route_Mapping, Flight_Simulation,
    Logistics_Sync, Safety_Audit,
    Pilot_Training,
    Deployment_Launch,
    Feedback_Loop_Loop
]

root = StrictPartialOrder(nodes=nodes_main)

# Add edges for main sequence
root.order.add_edge(Client_Brief, Needs_Analysis)
root.order.add_edge(Needs_Analysis, Regulatory_Check)
root.order.add_edge(Regulatory_Check, Drone_Design)

# Drone Design precedes both Component Sourcing and Assembly Test (these two concurrent, no order between them)
root.order.add_edge(Drone_Design, Component_Sourcing)
root.order.add_edge(Drone_Design, Assembly_Test)

# Both Component Sourcing and Assembly Test precede Payload Setup
root.order.add_edge(Component_Sourcing, Payload_Setup)
root.order.add_edge(Assembly_Test, Payload_Setup)

# Payload Setup --> Route Mapping --> Flight Simulation
root.order.add_edge(Payload_Setup, Route_Mapping)
root.order.add_edge(Route_Mapping, Flight_Simulation)

# Flight Simulation --> Logistics Sync --> Safety Audit --> Pilot Training
root.order.add_edge(Flight_Simulation, Logistics_Sync)
root.order.add_edge(Logistics_Sync, Safety_Audit)
root.order.add_edge(Safety_Audit, Pilot_Training)

# Pilot Training --> Deployment Launch
root.order.add_edge(Pilot_Training, Deployment_Launch)

# Deployment Launch --> Feedback Loop Loop
root.order.add_edge(Deployment_Launch, Feedback_Loop_Loop)