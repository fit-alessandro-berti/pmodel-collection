# Generated from: d6f37c8c-bf1c-469e-a369-66cdbd7f150f.json
# Description: This process involves the bespoke design and assembly of high-performance drones tailored for specialized industrial applications. Starting from client consultation to understand unique requirements, the workflow includes component sourcing, firmware customization, precision assembly, multi-stage testing, and regulatory compliance verification. The integration of AI modules and advanced sensors is followed by environmental stress testing and final quality assurance before packaging and logistics coordination to ensure timely delivery. This atypical process demands cross-functional collaboration among designers, engineers, and logistics specialists to meet strict performance and safety standards in an evolving market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ClientBrief = Transition(label='Client Brief')
DesignDraft = Transition(label='Design Draft')
ComponentOrder = Transition(label='Component Order')
FirmwareBuild = Transition(label='Firmware Build')
PCBAssembly = Transition(label='PCB Assembly')
SensorInstall = Transition(label='Sensor Install')
MotorMount = Transition(label='Motor Mount')
BatteryTest = Transition(label='Battery Test')
AIModule = Transition(label='AI Module')
SystemIntegrate = Transition(label='System Integrate')
FlightSimulate = Transition(label='Flight Simulate')
StressTest = Transition(label='Stress Test')
ComplianceCheck = Transition(label='Compliance Check')
QualityAudit = Transition(label='Quality Audit')
PackageDrone = Transition(label='Package Drone')
DeliveryPlan = Transition(label='Delivery Plan')

# Partial order for component assembly activities (concurrent)
assembly_PO = StrictPartialOrder(nodes=[PCBAssembly, SensorInstall, MotorMount])
# No order edges between them -> concurrent

# After assembly, Battery Test must happen
assembly_chain = StrictPartialOrder(
    nodes=[assembly_PO, BatteryTest]
)
assembly_chain.order.add_edge(assembly_PO, BatteryTest)

# Firmware Build is independent but must complete before System Integrate
firmware_sys_PO = StrictPartialOrder(nodes=[FirmwareBuild, SystemIntegrate])
firmware_sys_PO.order.add_edge(FirmwareBuild, SystemIntegrate)

# AI Module integrations and Flight Simulate after System Integrate
ai_flight_PO = StrictPartialOrder(nodes=[AIModule, FlightSimulate])
# After AIModule must be integrated and then Flight Simulate
ai_flight_chain = StrictPartialOrder(
    nodes=[AIModule, FlightSimulate]
)
ai_flight_chain.order.add_edge(AIModule, FlightSimulate)

# System Integrate precedes AI Module
sys_ai_chain = StrictPartialOrder(
    nodes=[SystemIntegrate, ai_flight_chain]
)
sys_ai_chain.order.add_edge(SystemIntegrate, ai_flight_chain)

# Testing after flight simulate
testing_PO = StrictPartialOrder(
    nodes=[FlightSimulate, StressTest, ComplianceCheck, QualityAudit]
)
testing_PO.order.add_edge(FlightSimulate, StressTest)
testing_PO.order.add_edge(StressTest, ComplianceCheck)
testing_PO.order.add_edge(ComplianceCheck, QualityAudit)

# Packaging and delivery after quality audit
pack_del_PO = StrictPartialOrder(
    nodes=[PackageDrone, DeliveryPlan]
)
pack_del_PO.order.add_edge(PackageDrone, DeliveryPlan)

# Design Draft after Client Brief
design_PO = StrictPartialOrder(nodes=[ClientBrief, DesignDraft])
design_PO.order.add_edge(ClientBrief, DesignDraft)

# Component Order can be done after Design Draft
component_order_PO = StrictPartialOrder(nodes=[DesignDraft, ComponentOrder])
component_order_PO.order.add_edge(DesignDraft, ComponentOrder)

# Component Order precedes assembly and firmware build
comp_assembly_fw_PO = StrictPartialOrder(nodes=[ComponentOrder, assembly_chain, firmware_sys_PO])
comp_assembly_fw_PO.order.add_edge(ComponentOrder, assembly_chain)
comp_assembly_fw_PO.order.add_edge(ComponentOrder, firmware_sys_PO)

# Combine all before testing: assembly and firmware+integration followed by testing
before_testing_PO = StrictPartialOrder(
    nodes=[comp_assembly_fw_PO, sys_ai_chain]
)
before_testing_PO.order.add_edge(comp_assembly_fw_PO, sys_ai_chain)

# Final root combining all parts sequentially:
root = StrictPartialOrder(
    nodes=[design_PO, component_order_PO, before_testing_PO, testing_PO, pack_del_PO]
)
# Enforce overall order

# Client Brief -> Design Draft already in design_PO
# Design Draft -> Component Order already in component_order_PO
root.order.add_edge(design_PO, component_order_PO)
root.order.add_edge(component_order_PO, before_testing_PO)
root.order.add_edge(before_testing_PO, testing_PO)
root.order.add_edge(testing_PO, pack_del_PO)