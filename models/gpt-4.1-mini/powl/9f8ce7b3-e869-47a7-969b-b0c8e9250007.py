# Generated from: 9f8ce7b3-e869-47a7-969b-b0c8e9250007.json
# Description: This process outlines the intricate steps involved in assembling custom drones tailored to unique client specifications. Starting from component sourcing, it includes specialized firmware integration, dynamic propeller calibration, environmental resistance testing under varying conditions, and adaptive AI training for autonomous flight behaviors. Quality assurance involves iterative stress simulations and real-time telemetry analysis to ensure reliability. Finally, packaging integrates modular upgrade options, and the delivery schedule adapts based on client feedback and seasonal demand fluctuations, ensuring a highly personalized and responsive manufacturing workflow.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
ComponentSourcing = Transition(label='Component Sourcing')
FrameAssembly = Transition(label='Frame Assembly')
FirmwareUpload = Transition(label='Firmware Upload')
PropellerMount = Transition(label='Propeller Mount')
BalanceCheck = Transition(label='Balance Check')
SensorInstall = Transition(label='Sensor Install')
BatteryFit = Transition(label='Battery Fit')
WiringRoute = Transition(label='Wiring Route')
AITraining = Transition(label='AI Training')
StressTesting = Transition(label='Stress Testing')
TelemetrySync = Transition(label='Telemetry Sync')
ResistanceTest = Transition(label='Resistance Test')
FlightTrial = Transition(label='Flight Trial')
PackagingPrep = Transition(label='Packaging Prep')
UpgradeConfig = Transition(label='Upgrade Config')
ClientFeedback = Transition(label='Client Feedback')
DeliveryPlan = Transition(label='Delivery Plan')

# Assemble frame after component sourcing
assembly = StrictPartialOrder(nodes=[FrameAssembly, FirmwareUpload, PropellerMount, BalanceCheck, SensorInstall, BatteryFit, WiringRoute])
assembly.order.add_edge(FrameAssembly, FirmwareUpload)
assembly.order.add_edge(FirmwareUpload, PropellerMount)
assembly.order.add_edge(PropellerMount, BalanceCheck)
assembly.order.add_edge(BalanceCheck, SensorInstall)
assembly.order.add_edge(SensorInstall, BatteryFit)
assembly.order.add_edge(BatteryFit, WiringRoute)

# Resistance Test followed by Flight Trial (environmental resistance testing and flight trial)
testing = StrictPartialOrder(nodes=[ResistanceTest, FlightTrial])
testing.order.add_edge(ResistanceTest, FlightTrial)

# Quality assurance loop:
# iterative stress simulations and telemetry analysis
# Loop with body = StressTesting -> TelemetrySync, loop back on telemetry to stress for iterations then exit
qa_loop_body = StrictPartialOrder(nodes=[StressTesting, TelemetrySync])
qa_loop_body.order.add_edge(StressTesting, TelemetrySync)
quality_assurance = OperatorPOWL(operator=Operator.LOOP, children=[StressTesting, TelemetrySync])

# Packaging with upgrade config concurrent (modular upgrade options integrated)
packaging = StrictPartialOrder(nodes=[PackagingPrep, UpgradeConfig])
# no order edge means concurrent packaging prep and upgrade config

# Delivery plan depends on client feedback and seasonal demand (seasonal demand not modeled explicitly,
# so use client feedback influencing delivery plan)
delivery = StrictPartialOrder(nodes=[ClientFeedback, DeliveryPlan])
delivery.order.add_edge(ClientFeedback, DeliveryPlan)

# Build the entire workflow partial order

# First: Component Sourcing then Assembly
po1 = StrictPartialOrder(nodes=[ComponentSourcing, assembly])
po1.order.add_edge(ComponentSourcing, assembly)

# Then FirmwareUpload etc is part of assembly, so assembly is single composite node here

# After assembly, FirmwareUpload done, then continue with AI Training and Resistance Test and Testing
post_assembly = StrictPartialOrder(nodes=[AITraining, testing, quality_assurance])
# AITraining, Testing and Quality Assurance can be concurrent, but QA depends on Testing (testing before QA)
post_assembly.order.add_edge(testing, quality_assurance)

# Now deliver the sequence:
# ComponentSourcing --> Assembly --> (concurrent AITraining, Testing->QA) --> Packaging --> Delivery

# Packaging happens after QA and AI Training
packaging_and_delivery = StrictPartialOrder(nodes=[packaging, delivery])
# Packaging before delivery
packaging_and_delivery.order.add_edge(packaging, delivery)

# Combine all together in order: po1 -> post_assembly -> packaging_and_delivery
root = StrictPartialOrder(nodes=[po1, post_assembly, packaging_and_delivery])
root.order.add_edge(po1, post_assembly)
root.order.add_edge(post_assembly, packaging_and_delivery)