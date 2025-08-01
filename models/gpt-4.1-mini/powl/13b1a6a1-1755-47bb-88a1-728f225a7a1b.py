# Generated from: 13b1a6a1-1755-47bb-88a1-728f225a7a1b.json
# Description: This process outlines the intricate steps involved in the assembly and configuration of customized drones tailored for specialized industrial applications. It begins with component sourcing based on client specifications, followed by precision frame construction and modular subsystem integration. Each drone undergoes advanced firmware installation, sensor calibration, and environmental resilience testing. The process also involves iterative flight simulations and real-world trial deployments to ensure compliance with safety and performance standards. Post-deployment, the system captures operational data for continuous improvement and client feedback integration, culminating in bespoke maintenance scheduling and upgrade path planning to extend drone lifecycle and optimize mission effectiveness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities as transitions
ComponentSourcing = Transition(label='Component Sourcing')
FrameBuild = Transition(label='Frame Build')
SubsystemFit = Transition(label='Subsystem Fit')
FirmwareLoad = Transition(label='Firmware Load')
SensorCalibrate = Transition(label='Sensor Calibrate')
EnvTest = Transition(label='Env Test')
FlightSimulate = Transition(label='Flight Simulate')
TrialDeploy = Transition(label='Trial Deploy')
DataCapture = Transition(label='Data Capture')
ClientReview = Transition(label='Client Review')
FeedbackIntegrate = Transition(label='Feedback Integrate')
MaintenancePlan = Transition(label='Maintenance Plan')
UpgradeDesign = Transition(label='Upgrade Design')
ComplianceCheck = Transition(label='Compliance Check')
FinalApproval = Transition(label='Final Approval')

# Loop for iterative flight simulation and trial deployment: 
# *(Flight Simulate, Trial Deploy)
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[FlightSimulate, TrialDeploy])

# Feedback integration after client review (sequential)
feedback_seq = StrictPartialOrder(nodes=[ClientReview, FeedbackIntegrate])
feedback_seq.order.add_edge(ClientReview, FeedbackIntegrate)

# Maintenance and upgrade planning happen sequentially after feedback integration
maint_upgrade_seq = StrictPartialOrder(nodes=[MaintenancePlan, UpgradeDesign])
maint_upgrade_seq.order.add_edge(MaintenancePlan, UpgradeDesign)

# Compliance check and final approval sequential after upgrade design
comp_approval_seq = StrictPartialOrder(nodes=[ComplianceCheck, FinalApproval])
comp_approval_seq.order.add_edge(ComplianceCheck, FinalApproval)

# Assemble the final partial order:
# Main sequence:
# Component Sourcing --> Frame Build --> Subsystem Fit --> Firmware Load --> Sensor Calibrate --> Env Test
# --> flight_loop (iterative Flight Simulate & Trial Deploy)
# --> Data Capture --> feedback_seq (Client Review -> Feedback Integrate)
# --> maint_upgrade_seq (Maintenance Plan -> Upgrade Design)
# --> comp_approval_seq (Compliance Check -> Final Approval)

nodes = [
    ComponentSourcing,
    FrameBuild,
    SubsystemFit,
    FirmwareLoad,
    SensorCalibrate,
    EnvTest,
    flight_loop,
    DataCapture,
    feedback_seq,
    maint_upgrade_seq,
    comp_approval_seq,
]

root = StrictPartialOrder(nodes=nodes)

root.order.add_edge(ComponentSourcing, FrameBuild)
root.order.add_edge(FrameBuild, SubsystemFit)
root.order.add_edge(SubsystemFit, FirmwareLoad)
root.order.add_edge(FirmwareLoad, SensorCalibrate)
root.order.add_edge(SensorCalibrate, EnvTest)
root.order.add_edge(EnvTest, flight_loop)
root.order.add_edge(flight_loop, DataCapture)
root.order.add_edge(DataCapture, feedback_seq)
root.order.add_edge(feedback_seq, maint_upgrade_seq)
root.order.add_edge(maint_upgrade_seq, comp_approval_seq)