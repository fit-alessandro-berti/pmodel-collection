# Generated from: 7681640e-8dd6-4a87-ac5c-4c1c87d12954.json
# Description: This process outlines the end-to-end setup and deployment of a bespoke drone fleet designed for specialized industrial inspection tasks. It begins with requirement analysis and proceeds through custom hardware sourcing, firmware adaptation, and environmental simulation testing. After pilot training and regulatory compliance validation, the process includes dynamic route programming, real-time telemetry integration, and emergency protocol implementation. Finally, the process ensures continuous performance monitoring and adaptive maintenance scheduling to optimize operational longevity and safety in challenging environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Requirement_Analysis = Transition(label='Requirement Analysis')
Hardware_Sourcing = Transition(label='Hardware Sourcing')
Firmware_Adaptation = Transition(label='Firmware Adaptation')
Simulated_Testing = Transition(label='Simulated Testing')
Pilot_Training = Transition(label='Pilot Training')
Compliance_Check = Transition(label='Compliance Check')
Route_Programming = Transition(label='Route Programming')
Telemetry_Setup = Transition(label='Telemetry Setup')
Emergency_Setup = Transition(label='Emergency Setup')
Performance_Audit = Transition(label='Performance Audit')
Maintenance_Plan = Transition(label='Maintenance Plan')
Data_Integration = Transition(label='Data Integration')
Risk_Assessment = Transition(label='Risk Assessment')
Field_Deployment = Transition(label='Field Deployment')
Feedback_Loop = Transition(label='Feedback Loop')

# The process:
# 1. Requirement Analysis 
# 2. Hardware Sourcing
# 3. Firmware Adaptation
# 4. Simulated Testing
# 5. Pilot Training and Compliance Check in parallel (concurrent)
# 6. Route Programming, Telemetry Setup, Emergency Setup in parallel (concurrent)
# 7. Data Integration and Risk Assessment in parallel (concurrent)
# 8. Then Field Deployment
# 9. Then a loop: Feedback Loop -> Performance Audit -> Maintenance Plan -> (back to Feedback Loop or exit)

# Step 5 concurrency
step_5_PO = StrictPartialOrder(nodes=[Pilot_Training, Compliance_Check])

# Step 6 concurrency
step_6_PO = StrictPartialOrder(nodes=[Route_Programming, Telemetry_Setup, Emergency_Setup])

# Step 7 concurrency
step_7_PO = StrictPartialOrder(nodes=[Data_Integration, Risk_Assessment])

# Loop structure at the end
# Loop body = Feedback Loop -> Performance Audit -> Maintenance Plan
loop_body_PO = StrictPartialOrder(nodes=[Feedback_Loop, Performance_Audit, Maintenance_Plan])
loop_body_PO.order.add_edge(Feedback_Loop, Performance_Audit)
loop_body_PO.order.add_edge(Performance_Audit, Maintenance_Plan)

# LOOP operator: execute Feedback Loop sequence, then choose to exit or loop again
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body_PO, SilentTransition()])

# Build the full partial order for the main sequence before the loop:
# Nodes = all main activities + the three concurrent sets + the loop at the end
nodes = [
    Requirement_Analysis,
    Hardware_Sourcing,
    Firmware_Adaptation,
    Simulated_Testing,
    step_5_PO,
    step_6_PO,
    step_7_PO,
    Data_Integration,  # Need to remove duplicate in nodes: Data_Integration and Risk_Assessment are in step_7_PO, so no need here
    Field_Deployment,
    loop
]

# Remove Data_Integration from nodes list above because it is included in step_7_PO
nodes.remove(Data_Integration)

root = StrictPartialOrder(nodes=nodes)

# Add order edges for the main sequence
root.order.add_edge(Requirement_Analysis, Hardware_Sourcing)
root.order.add_edge(Hardware_Sourcing, Firmware_Adaptation)
root.order.add_edge(Firmware_Adaptation, Simulated_Testing)
root.order.add_edge(Simulated_Testing, step_5_PO)
root.order.add_edge(step_5_PO, step_6_PO)
root.order.add_edge(step_6_PO, step_7_PO)
root.order.add_edge(step_7_PO, Field_Deployment)
root.order.add_edge(Field_Deployment, loop)