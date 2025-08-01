# Generated from: 453bf409-65d9-4ecf-9816-da1c29353948.json
# Description: This process involves the end-to-end assembly and testing of custom-made drones tailored to unique client specifications. It begins with detailed requirement analysis, followed by component sourcing from multiple specialized suppliers. Each drone frame is assembled manually to ensure precision. Firmware is then developed and uploaded to the flight controller. The drone undergoes multi-stage calibration, including sensor alignment and motor balancing. After initial bench testing, a simulated flight test is conducted in a controlled environment. Post-testing, data analytics are applied to evaluate performance metrics. If the drone passes quality standards, it is packaged with personalized documentation and shipped using a custom logistics solution. Throughout, frequent client updates and iterative feedback integration ensure the final product meets exact expectations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
RequirementReview    = Transition(label='Requirement Review')
SupplierSelection    = Transition(label='Supplier Selection')
ComponentSourcing    = Transition(label='Component Sourcing')
FrameAssembly        = Transition(label='Frame Assembly')
FirmwareUpload       = Transition(label='Firmware Upload')
SensorCalibration    = Transition(label='Sensor Calibration')
MotorBalancing       = Transition(label='Motor Balancing')
BenchTesting         = Transition(label='Bench Testing')
FlightSimulation     = Transition(label='Flight Simulation')
DataAnalysis         = Transition(label='Data Analysis')
QualityAudit         = Transition(label='Quality Audit')
DocumentationPrep    = Transition(label='Documentation Prep')
CustomPackaging      = Transition(label='Custom Packaging')
LogisticsPlanning    = Transition(label='Logistics Planning')
ShipmentDispatch     = Transition(label='Shipment Dispatch')
ClientFeedback       = Transition(label='Client Feedback')

# Calibration can happen in parallel (no ordering between sensor and motor)
calibration = StrictPartialOrder(nodes=[SensorCalibration, MotorBalancing])

# Main assembly‐and‐test workflow (strict sequential ordering)
main_process = StrictPartialOrder(nodes=[
    RequirementReview,
    SupplierSelection,
    ComponentSourcing,
    FrameAssembly,
    FirmwareUpload,
    calibration,
    BenchTesting,
    FlightSimulation,
    DataAnalysis,
    QualityAudit,
    DocumentationPrep,
    CustomPackaging,
    LogisticsPlanning,
    ShipmentDispatch
])
main_process.order.add_edge(RequirementReview,    SupplierSelection)
main_process.order.add_edge(SupplierSelection,    ComponentSourcing)
main_process.order.add_edge(ComponentSourcing,    FrameAssembly)
main_process.order.add_edge(FrameAssembly,        FirmwareUpload)
main_process.order.add_edge(FirmwareUpload,       calibration)
main_process.order.add_edge(calibration,          BenchTesting)
main_process.order.add_edge(BenchTesting,         FlightSimulation)
main_process.order.add_edge(FlightSimulation,     DataAnalysis)
main_process.order.add_edge(DataAnalysis,         QualityAudit)
main_process.order.add_edge(QualityAudit,         DocumentationPrep)
main_process.order.add_edge(DocumentationPrep,    CustomPackaging)
main_process.order.add_edge(CustomPackaging,      LogisticsPlanning)
main_process.order.add_edge(LogisticsPlanning,    ShipmentDispatch)

# Wrap in a feedback loop: execute main_process, then optionally perform client feedback and repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[main_process, ClientFeedback])