# Generated from: 89ca2343-6e87-4ae5-81b7-2550f4788833.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a constrained city environment. It begins with site analysis and zoning compliance, followed by modular structure design and custom hydroponic system integration. Concurrently, environmental sensors are calibrated to optimize plant growth cycles. Specialized nutrient solutions are formulated and tested for different crop types, while energy-efficient LED lighting schedules are programmed. Worker safety protocols are developed alongside automation routines for seeding, irrigation, and harvesting. Finally, a digital inventory system is implemented to track crop yields and supply chain logistics, ensuring sustainability and profitability in a complex urban agriculture setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
site_analysis = Transition(label='Site Analysis')
zoning_check = Transition(label='Zoning Check')

structure_design = Transition(label='Structure Design')
hydroponic_setup = Transition(label='Hydroponic Setup')

sensor_calibration = Transition(label='Sensor Calibration')

nutrient_testing = Transition(label='Nutrient Testing')
lighting_program = Transition(label='Lighting Program')

safety_protocol = Transition(label='Safety Protocol')

automation_script = Transition(label='Automation Script')
seeding_cycle = Transition(label='Seeding Cycle')
irrigation_plan = Transition(label='Irrigation Plan')
harvest_routine = Transition(label='Harvest Routine')

inventory_setup = Transition(label='Inventory Setup')
yield_tracking = Transition(label='Yield Tracking')
supply_logistics = Transition(label='Supply Logistics')

# Partial order for initial two sequential activities
po1 = StrictPartialOrder(nodes=[site_analysis, zoning_check])
po1.order.add_edge(site_analysis, zoning_check)

# Partial order for modular structure design and hydroponic setup sequential
po2 = StrictPartialOrder(nodes=[structure_design, hydroponic_setup])
po2.order.add_edge(structure_design, hydroponic_setup)

# Partial order for nutrient testing and lighting program concurrent
po3 = StrictPartialOrder(nodes=[nutrient_testing, lighting_program])
# no edges, concurrent

# Partial order for automation sub-process: automation script then seeding, irrigation, harvest sequentially
po4 = StrictPartialOrder(nodes=[automation_script, seeding_cycle, irrigation_plan, harvest_routine])
po4.order.add_edge(automation_script, seeding_cycle)
po4.order.add_edge(seeding_cycle, irrigation_plan)
po4.order.add_edge(irrigation_plan, harvest_routine)

# Partial order for inventory related activities sequentially
po5 = StrictPartialOrder(nodes=[inventory_setup, yield_tracking, supply_logistics])
po5.order.add_edge(inventory_setup, yield_tracking)
po5.order.add_edge(yield_tracking, supply_logistics)

# Partial order for safety protocol alone
# single node - can be combined later

# STRUCTURE:
# 1) Site Analysis --> Zoning Check --> Structure/Hydroponic (po2)
# 2) Concurrently with 1. sensor_calibration
# 3) nutrient_testing and lighting_program concurrent with above
# 4) safety_protocol concurrent with above
# 5) automation subprocess po4 concurrent with above
# 6) finally inventory subprocess po5 after all above complete

# Combine structure_design and hydroponic_setup after zoning_check
po_123 = StrictPartialOrder(
    nodes=[po1, po2, sensor_calibration, po3, safety_protocol, po4]
)
# edges inside po1 and po2 are internal, so we add ordering btw these partial orders:
po_123.order.add_edge(po1, po2)          # zoning_check before structure_design
po_123.order.add_edge(po1, sensor_calibration)
po_123.order.add_edge(po1, po3)
po_123.order.add_edge(po1, safety_protocol)
po_123.order.add_edge(po1, po4)

po_123.order.add_edge(po2, sensor_calibration)
po_123.order.add_edge(po2, po3)
po_123.order.add_edge(po2, safety_protocol)
po_123.order.add_edge(po2, po4)

# sensor_calibration, po3, safety_protocol, and po4 are concurrent (no edges among them)

# Finally inventory subprocess after all above
root = StrictPartialOrder(
    nodes=[po_123, po5]
)
root.order.add_edge(po_123, po5)