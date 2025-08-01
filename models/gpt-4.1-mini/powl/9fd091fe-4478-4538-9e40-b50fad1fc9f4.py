# Generated from: 9fd091fe-4478-4538-9e40-b50fad1fc9f4.json
# Description: This process involves the intricate assembly and customization of drones tailored for specialized industrial applications. Starting with component verification, it includes firmware integration, dynamic calibration, and environmental adaptability testing. The workflow demands rigorous quality assurance and compliance checks, followed by client-specific software loading and remote diagnostics setup. Final steps cover packaging with augmented reality manuals and logistics coordination for secure delivery. The process ensures drones meet unique operational demands while maintaining safety and performance standards in diverse environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
ComponentCheck = Transition(label='Component Check')
FrameAssembly = Transition(label='Frame Assembly')
MotorMount = Transition(label='Motor Mount')
SensorSetup = Transition(label='Sensor Setup')
WiringHarness = Transition(label='Wiring Harness')
FirmwareLoad = Transition(label='Firmware Load')
CalibrationRun = Transition(label='Calibration Run')
FlightTest = Transition(label='Flight Test')
EnvAdaptation = Transition(label='Env Adaptation')
QAInspection = Transition(label='QA Inspection')
ComplianceVerify = Transition(label='Compliance Verify')
SoftwareInstall = Transition(label='Software Install')
DiagnosticsSetup = Transition(label='Diagnostics Setup')
PackagingAR = Transition(label='Packaging AR')
LogisticsPlan = Transition(label='Logistics Plan')
CustomerHandoff = Transition(label='Customer Handoff')

# Partial order for assembly: FrameAssembly, MotorMount, SensorSetup, WiringHarness are concurrent after ComponentCheck
assembly = StrictPartialOrder(nodes=[FrameAssembly, MotorMount, SensorSetup, WiringHarness])
# No order edges among assembly tasks since they appear concurrent

# After assembly, FirmwareLoad
# After FirmwareLoad, CalibrationRun and FlightTest in sequence
calibration_and_test = StrictPartialOrder(nodes=[CalibrationRun, FlightTest])
calibration_and_test.order.add_edge(CalibrationRun, FlightTest)

# After FlightTest, EnvAdaptation
env_adaptation = EnvAdaptation

# Quality assurance sequence: QAInspection then ComplianceVerify
qa_compliance = StrictPartialOrder(nodes=[QAInspection, ComplianceVerify])
qa_compliance.order.add_edge(QAInspection, ComplianceVerify)

# SoftwareInstall and DiagnosticsSetup concurrent after QA+Compliance
software_diagnostics = StrictPartialOrder(nodes=[SoftwareInstall, DiagnosticsSetup])

# Packaging with AR then Logistics planning, then Customer handoff in sequence
packaging_logistics = StrictPartialOrder(nodes=[PackagingAR, LogisticsPlan, CustomerHandoff])
packaging_logistics.order.add_edge(PackagingAR, LogisticsPlan)
packaging_logistics.order.add_edge(LogisticsPlan, CustomerHandoff)

# Compose the full PO:
# ComponentCheck --> assembly (the 4 tasks) --> FirmwareLoad --> calibration_and_test --> EnvAdaptation -->
# qa_compliance --> software_diagnostics --> packaging_logistics

nodes = [
    ComponentCheck,
    assembly,
    FirmwareLoad,
    calibration_and_test,
    EnvAdaptation,
    qa_compliance,
    software_diagnostics,
    packaging_logistics
]

root = StrictPartialOrder(nodes=nodes)

# Add the edges representing control flow
root.order.add_edge(ComponentCheck, assembly)
root.order.add_edge(assembly, FirmwareLoad)
root.order.add_edge(FirmwareLoad, calibration_and_test)
root.order.add_edge(calibration_and_test, EnvAdaptation)
root.order.add_edge(EnvAdaptation, qa_compliance)
root.order.add_edge(qa_compliance, software_diagnostics)
root.order.add_edge(software_diagnostics, packaging_logistics)