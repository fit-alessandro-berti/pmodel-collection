# Generated from: 89ca2343-6e87-4ae5-81b7-2550f4788833.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a constrained city environment. It begins with site analysis and zoning compliance, followed by modular structure design and custom hydroponic system integration. Concurrently, environmental sensors are calibrated to optimize plant growth cycles. Specialized nutrient solutions are formulated and tested for different crop types, while energy-efficient LED lighting schedules are programmed. Worker safety protocols are developed alongside automation routines for seeding, irrigation, and harvesting. Finally, a digital inventory system is implemented to track crop yields and supply chain logistics, ensuring sustainability and profitability in a complex urban agriculture setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define activities
site_analysis    = Transition(label='Site Analysis')
zoning_check     = Transition(label='Zoning Check')
structure_design = Transition(label='Structure Design')
hydroponic_setup = Transition(label='Hydroponic Setup')
sensor_cal       = Transition(label='Sensor Calibration')
nutrient_test    = Transition(label='Nutrient Testing')
lighting_prog    = Transition(label='Lighting Program')
safety_protocol  = Transition(label='Safety Protocol')
automation_script= Transition(label='Automation Script')
seeding_cycle    = Transition(label='Seeding Cycle')
irrigation_plan  = Transition(label='Irrigation Plan')
harvest_routine  = Transition(label='Harvest Routine')
inventory_setup  = Transition(label='Inventory Setup')
yield_tracking   = Transition(label='Yield Tracking')
supply_logistics = Transition(label='Supply Logistics')

# Phase 1: Site Analysis -> Zoning Check
seq1 = StrictPartialOrder(nodes=[site_analysis, zoning_check])
seq1.order.add_edge(site_analysis, zoning_check)

# Phase 2: Structure Design -> Hydroponic Setup
seq2 = StrictPartialOrder(nodes=[structure_design, hydroponic_setup])
seq2.order.add_edge(structure_design, hydroponic_setup)

# Phase 3: concurrent Sensor Calibration, Nutrient Testing, Lighting Program
phase3 = StrictPartialOrder(nodes=[sensor_cal, nutrient_test, lighting_prog])
# no edges => fully concurrent

# Phase 4: Safety Protocol concurrent with automation sequence
automation_seq = StrictPartialOrder(
    nodes=[automation_script, seeding_cycle, irrigation_plan, harvest_routine]
)
automation_seq.order.add_edge(automation_script, seeding_cycle)
automation_seq.order.add_edge(seeding_cycle, irrigation_plan)
automation_seq.order.add_edge(irrigation_plan, harvest_routine)

safety_automation = StrictPartialOrder(nodes=[safety_protocol, automation_seq])
# no edge between safety_protocol and automation_seq => concurrent

# Phase 5: Inventory Setup -> (Yield Tracking & Supply Logistics) concurrently
inventory_phase = StrictPartialOrder(
    nodes=[inventory_setup, yield_tracking, supply_logistics]
)
inventory_phase.order.add_edge(inventory_setup, yield_tracking)
inventory_phase.order.add_edge(inventory_setup, supply_logistics)

# Root process: phases in sequence
root = StrictPartialOrder(
    nodes=[seq1, seq2, phase3, safety_automation, inventory_phase]
)
root.order.add_edge(seq1, seq2)
root.order.add_edge(seq2, phase3)
root.order.add_edge(phase3, safety_automation)
root.order.add_edge(safety_automation, inventory_phase)