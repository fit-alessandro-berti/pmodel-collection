# Generated from: b9c06257-822e-4505-8c1e-f0c5f5c7adb0.json
# Description: This process outlines the steps required to design, assemble, and deploy a custom drone fleet tailored for environmental monitoring in remote areas. It involves initial requirement gathering, prototype design, component sourcing from multiple vendors, iterative testing under varied environmental conditions, software integration for autonomous operations, regulatory compliance checks, pilot training, and final deployment. Continuous feedback loops ensure adaptability and performance improvements, while data collection protocols are established to support long-term ecological studies and reporting obligations to environmental agencies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
RequirementGather = Transition(label='Requirement Gather')
ConceptDesign = Transition(label='Concept Design')
VendorSelect = Transition(label='Vendor Select')
ComponentOrder = Transition(label='Component Order')
PrototypeBuild = Transition(label='Prototype Build')
FieldTesting = Transition(label='Field Testing')
SoftwareInstall = Transition(label='Software Install')
AutonomySetup = Transition(label='Autonomy Setup')
ComplianceCheck = Transition(label='Compliance Check')
PilotTrain = Transition(label='Pilot Train')
DataProtocol = Transition(label='Data Protocol')
FleetAssemble = Transition(label='Fleet Assemble')
DeploymentPlan = Transition(label='Deployment Plan')
PerformanceReview = Transition(label='Performance Review')
FeedbackLoop = Transition(label='Feedback Loop')
ReportGenerate = Transition(label='Report Generate')
MaintenanceSchedule = Transition(label='Maintenance Schedule')

# Model iterative testing with continuous feedback loop:
# Loop node: execute FieldTesting, then choose to exit or perform FeedbackLoop and then FieldTesting again
test_loop = OperatorPOWL(operator=Operator.LOOP, children=[FieldTesting, FeedbackLoop])

# Partial order representing the main flow
nodes = [
    RequirementGather,
    ConceptDesign,
    VendorSelect,
    ComponentOrder,
    PrototypeBuild,
    test_loop,
    SoftwareInstall,
    AutonomySetup,
    ComplianceCheck,
    PilotTrain,
    DataProtocol,
    FleetAssemble,
    DeploymentPlan,
    PerformanceReview,
    ReportGenerate,
    MaintenanceSchedule
]

root = StrictPartialOrder(nodes=nodes)

# Define order edges based on described dependencies:

# Initial sequence
root.order.add_edge(RequirementGather, ConceptDesign)
root.order.add_edge(ConceptDesign, VendorSelect)
root.order.add_edge(VendorSelect, ComponentOrder)
root.order.add_edge(ComponentOrder, PrototypeBuild)

# Prototype build followed by iterative testing loop
root.order.add_edge(PrototypeBuild, test_loop)

# After testing loop finishes, continue with software and autonomy setup
root.order.add_edge(test_loop, SoftwareInstall)
root.order.add_edge(SoftwareInstall, AutonomySetup)

# Autonomy setup to regulatory compliance check
root.order.add_edge(AutonomySetup, ComplianceCheck)

# Compliance check then pilot training
root.order.add_edge(ComplianceCheck, PilotTrain)

# Pilot training and Data Protocol can be concurrent, both before Fleet Assemble
root.order.add_edge(PilotTrain, FleetAssemble)
root.order.add_edge(DataProtocol, FleetAssemble)

# Data Protocol can start after PilotTrain or in parallel, no direct order to start it; but should start after ComplianceCheck for realistic scenario
root.order.add_edge(ComplianceCheck, DataProtocol)

# Fleet Assemble before Deployment Plan
root.order.add_edge(FleetAssemble, DeploymentPlan)

# Deployment Plan before Performance Review
root.order.add_edge(DeploymentPlan, PerformanceReview)

# Performance Review before Report Generate
root.order.add_edge(PerformanceReview, ReportGenerate)

# Maintenance Schedule after Report Generate
root.order.add_edge(ReportGenerate, MaintenanceSchedule)