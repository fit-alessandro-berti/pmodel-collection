# Generated from: 300d484b-ee57-4490-8696-22a91c4ff690.json
# Description: This process manages the end-to-end lifecycle of a custom drone fleet tailored for complex environmental monitoring missions. It begins with client consultation to define specific requirements, followed by modular drone design and prototype assembly. The process continues with iterative flight testing, data integration setup, and regulatory compliance validation. After deployment planning and operator training, the fleet undergoes continuous performance monitoring and adaptive maintenance scheduling. Data collected from missions is analyzed for insights, triggering firmware updates and hardware recalibrations. Post-mission reports are generated to refine future deployments and optimize operational efficiency, ensuring sustainable and scalable drone fleet management tailored to unique environmental challenges.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions with exact labels
ClientConsult = Transition(label='Client Consult')
RequirementGather = Transition(label='Requirement Gather')
ModularDesign = Transition(label='Modular Design')
PrototypeBuild = Transition(label='Prototype Build')
FlightTesting = Transition(label='Flight Testing')
DataSetup = Transition(label='Data Setup')
ComplianceCheck = Transition(label='Compliance Check')
DeploymentPlan = Transition(label='Deployment Plan')
OperatorTrain = Transition(label='Operator Train')
PerformanceMonitor = Transition(label='Performance Monitor')
MaintenanceSchedule = Transition(label='Maintenance Schedule')
DataAnalysis = Transition(label='Data Analysis')
FirmwareUpdate = Transition(label='Firmware Update')
HardwareCalibrate = Transition(label='Hardware Calibrate')
ReportGenerate = Transition(label='Report Generate')

# Define the loop for continuous performance monitoring and adaptive maintenance scheduling:
# Loop body: PerformanceMonitor then MaintenanceSchedule
loopBody = StrictPartialOrder(nodes=[PerformanceMonitor, MaintenanceSchedule])
loopBody.order.add_edge(PerformanceMonitor, MaintenanceSchedule)
monitor_maint_loop = OperatorPOWL(operator=Operator.LOOP, children=[loopBody, PerformanceMonitor])

# After DataAnalysis, firmware update and hardware calibrate are triggered in parallel (no ordering)
firmware_and_hardware = StrictPartialOrder(nodes=[FirmwareUpdate, HardwareCalibrate])

# Construct the main partial order with the given dependencies:
# ClientConsult -> RequirementGather -> ModularDesign -> PrototypeBuild -> FlightTesting ->
# DataSetup -> ComplianceCheck -> DeploymentPlan -> OperatorTrain -> (loop) -> DataAnalysis -> firmware/hardware -> ReportGenerate

root = StrictPartialOrder(nodes=[
    ClientConsult,
    RequirementGather,
    ModularDesign,
    PrototypeBuild,
    FlightTesting,
    DataSetup,
    ComplianceCheck,
    DeploymentPlan,
    OperatorTrain,
    monitor_maint_loop,
    DataAnalysis,
    firmware_and_hardware,
    ReportGenerate,
])

root.order.add_edge(ClientConsult, RequirementGather)
root.order.add_edge(RequirementGather, ModularDesign)
root.order.add_edge(ModularDesign, PrototypeBuild)
root.order.add_edge(PrototypeBuild, FlightTesting)
root.order.add_edge(FlightTesting, DataSetup)
root.order.add_edge(DataSetup, ComplianceCheck)
root.order.add_edge(ComplianceCheck, DeploymentPlan)
root.order.add_edge(DeploymentPlan, OperatorTrain)
root.order.add_edge(OperatorTrain, monitor_maint_loop)
root.order.add_edge(monitor_maint_loop, DataAnalysis)
root.order.add_edge(DataAnalysis, firmware_and_hardware)
root.order.add_edge(firmware_and_hardware, ReportGenerate)