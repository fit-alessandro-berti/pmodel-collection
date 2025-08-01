# Generated from: aa251f3d-392c-4376-881a-324ecde6a71e.json
# Description: This process outlines the highly specialized assembly of custom drones tailored for diverse industrial applications such as agriculture, surveillance, and delivery. It begins with design specification collection from clients followed by component sourcing that includes rare materials and specialized electronics. Subsequent activities involve precision machining, micro-soldering of circuit boards, and advanced sensor calibration under controlled environments. Quality assurance includes real-time flight simulation and adaptive software integration specific to each drone model. Final steps cover packaging with anti-static materials and customized documentation before shipping. This atypical process requires interdisciplinary coordination between engineering, procurement, and software teams to ensure every drone meets exacting client demands and regulatory standards, emphasizing flexibility and innovation in manufacturing.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all labeled transitions
SpecCollection      = Transition(label='Spec Collection')
ComponentSourcing   = Transition(label='Component Sourcing')
MaterialInspection  = Transition(label='Material Inspection')
CircuitAssembly     = Transition(label='Circuit Assembly')
SensorCalibration   = Transition(label='Sensor Calibration')
FirmwareUpload      = Transition(label='Firmware Upload')
FlightSimulation    = Transition(label='Flight Simulation')
StructuralTesting   = Transition(label='Structural Testing')
ThermalImaging      = Transition(label='Thermal Imaging')
BatteryConditioning = Transition(label='Battery Conditioning')
SoftwareIntegration = Transition(label='Software Integration')
AntiStaticPack      = Transition(label='Anti-Static Pack')
DocumentationPrep   = Transition(label='Documentation Prep')
ClientApproval      = Transition(label='Client Approval')
ShippingDispatch    = Transition(label='Shipping Dispatch')

# Build the partial order
root = StrictPartialOrder(nodes=[
    SpecCollection,
    ComponentSourcing,
    MaterialInspection,
    CircuitAssembly,
    SensorCalibration,
    FirmwareUpload,
    FlightSimulation,
    StructuralTesting,
    ThermalImaging,
    BatteryConditioning,
    SoftwareIntegration,
    AntiStaticPack,
    DocumentationPrep,
    ClientApproval,
    ShippingDispatch
])

# Linear assembly flow
root.order.add_edge(SpecCollection, ComponentSourcing)
root.order.add_edge(ComponentSourcing, MaterialInspection)
root.order.add_edge(MaterialInspection, CircuitAssembly)
root.order.add_edge(CircuitAssembly, SensorCalibration)
root.order.add_edge(SensorCalibration, FirmwareUpload)

# After firmware upload, QA tasks run in parallel
for qa in [FlightSimulation, StructuralTesting, ThermalImaging, BatteryConditioning, SoftwareIntegration]:
    root.order.add_edge(FirmwareUpload, qa)

# Packaging and documentation after all QA
for qa in [FlightSimulation, StructuralTesting, ThermalImaging, BatteryConditioning, SoftwareIntegration]:
    root.order.add_edge(qa, AntiStaticPack)
    root.order.add_edge(qa, DocumentationPrep)

# Client approval and shipping
root.order.add_edge(AntiStaticPack, ClientApproval)
root.order.add_edge(DocumentationPrep, ClientApproval)
root.order.add_edge(ClientApproval, ShippingDispatch)