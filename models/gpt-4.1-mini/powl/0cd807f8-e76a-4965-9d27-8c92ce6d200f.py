# Generated from: 0cd807f8-e76a-4965-9d27-8c92ce6d200f.json
# Description: This process involves the bespoke assembly of drones tailored to specific client requirements, integrating unique hardware and software components. It starts with requirement analysis, followed by parts sourcing from specialized vendors, custom frame fabrication, and component integration. Quality testing includes flight simulation and endurance trials. Final steps feature software calibration, safety certification, and packaging for delivery. The process requires coordination among design, engineering, procurement, and quality assurance teams to ensure each drone meets precise operational standards while maintaining adaptability for future upgrades and modifications.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
RequirementSync = Transition(label='Requirement Sync')
VendorAudit = Transition(label='Vendor Audit')
PartSourcing = Transition(label='Part Sourcing')
FrameDesign = Transition(label='Frame Design')
MaterialCut = Transition(label='Material Cut')
ComponentFit = Transition(label='Component Fit')
WiringSetup = Transition(label='Wiring Setup')
FirmwareLoad = Transition(label='Firmware Load')
InitialTesting = Transition(label='Initial Testing')
FlightSim = Transition(label='Flight Sim')
BatteryInstall = Transition(label='Battery Install')
EnduranceTest = Transition(label='Endurance Test')
SafetyCert = Transition(label='Safety Cert')
SoftwareTune = Transition(label='Software Tune')
FinalPack = Transition(label='Final Pack')

# Build partial order structure for fabrication & integration:
# FrameDesign -> MaterialCut
fabrication = StrictPartialOrder(nodes=[FrameDesign, MaterialCut])
fabrication.order.add_edge(FrameDesign, MaterialCut)

# Integration partial order (concurrent parts):
# ComponentFit -> WiringSetup -> FirmwareLoad
integration = StrictPartialOrder(nodes=[ComponentFit, WiringSetup, FirmwareLoad])
integration.order.add_edge(ComponentFit, WiringSetup)
integration.order.add_edge(WiringSetup, FirmwareLoad)

# Quality Testing partial order:
# FlightSim and BatteryInstall can be concurrent after InitialTesting
testing = StrictPartialOrder(nodes=[InitialTesting, FlightSim, BatteryInstall, EnduranceTest])
testing.order.add_edge(InitialTesting, FlightSim)
testing.order.add_edge(InitialTesting, BatteryInstall)
# EnduranceTest after FlightSim and BatteryInstall
testing.order.add_edge(FlightSim, EnduranceTest)
testing.order.add_edge(BatteryInstall, EnduranceTest)

# Assemble design and engineering steps partial order:
design_engineering = StrictPartialOrder(
    nodes=[RequirementSync, VendorAudit, PartSourcing, fabrication, integration, InitialTesting]
)
# Requirement Sync -> Vendor Audit -> Part Sourcing
design_engineering.order.add_edge(RequirementSync, VendorAudit)
design_engineering.order.add_edge(VendorAudit, PartSourcing)
# Part Sourcing -> fabrication (FrameDesign->MaterialCut)
design_engineering.order.add_edge(PartSourcing, fabrication)
# fabrication -> integration
design_engineering.order.add_edge(fabrication, integration)
# integration -> InitialTesting
design_engineering.order.add_edge(integration, InitialTesting)

# Quality assurance steps after endurance test: Safety Cert
quality_assurance = StrictPartialOrder(nodes=[testing, SafetyCert])
testing_end = EnduranceTest
quality_assurance.order.add_edge(testing, SafetyCert)

# Software calibration after Safety Certification
software_calibration = StrictPartialOrder(nodes=[SafetyCert, SoftwareTune])
software_calibration.order.add_edge(SafetyCert, SoftwareTune)

# Final packaging after software tuning
final_delivery = StrictPartialOrder(nodes=[SoftwareTune, FinalPack])
final_delivery.order.add_edge(SoftwareTune, FinalPack)

# Compose overall process partial order
root = StrictPartialOrder(
    nodes=[design_engineering, quality_assurance, software_calibration, final_delivery]
)
root.order.add_edge(design_engineering, quality_assurance)
root.order.add_edge(quality_assurance, software_calibration)
root.order.add_edge(software_calibration, final_delivery)