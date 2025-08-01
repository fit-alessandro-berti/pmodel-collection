# Generated from: 7f94bf10-9334-463e-b495-ab492a8e095a.json
# Description: This process manages the entire lifecycle of an urban vertical farm, integrating advanced hydroponics, automated environmental controls, and real-time data analytics to optimize crop yield within confined city spaces. It begins with site analysis and design customization, proceeds through seed selection and nutrient calibration, followed by growth monitoring using AI-driven sensors. The process includes pest management via biological controls, energy consumption optimization, and waste recycling. Harvesting is synchronized with distribution logistics to ensure freshness, and feedback loops from consumer data help refine subsequent cycles, making the system adaptive and sustainable in complex urban ecosystems.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_analysis = Transition(label='Site Analysis')
design_layout = Transition(label='Design Layout')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
system_setup = Transition(label='System Setup')
planting_seeds = Transition(label='Planting Seeds')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
climate_adjust = Transition(label='Climate Adjust')
water_recycling = Transition(label='Water Recycling')
energy_audit = Transition(label='Energy Audit')
harvest_plan = Transition(label='Harvest Plan')
quality_check = Transition(label='Quality Check')
pack_produce = Transition(label='Pack Produce')
distribute_goods = Transition(label='Distribute Goods')
data_feedback = Transition(label='Data Feedback')

# Phase 1: Site analysis and design customization (sequential)
phase1 = StrictPartialOrder(nodes=[site_analysis, design_layout])
phase1.order.add_edge(site_analysis, design_layout)

# Phase 2: Seed selection and nutrient calibration (sequential)
phase2 = StrictPartialOrder(nodes=[seed_selection, nutrient_mix])
phase2.order.add_edge(seed_selection, nutrient_mix)

# Phase 3: System setup, then planting seeds (sequential)
phase3 = StrictPartialOrder(nodes=[system_setup, planting_seeds])
phase3.order.add_edge(system_setup, planting_seeds)

# Phase 4: Growth monitoring, pest control, climate adjustment, water recycling, energy audit
# These activities can run concurrently but growth_monitor precedes pest_control (since sensors detect pests),
# and pest_control and climate_adjust can run concurrently, water_recycling and energy_audit concurrently as well.
# But monitor is prerequisite for pest_control, climate_adjust, water_recycling, energy_audit.

growth_subnodes = [
    growth_monitor,
    pest_control,
    climate_adjust,
    water_recycling,
    energy_audit
]
phase4 = StrictPartialOrder(nodes=growth_subnodes)
phase4.order.add_edge(growth_monitor, pest_control)
phase4.order.add_edge(growth_monitor, climate_adjust)
phase4.order.add_edge(growth_monitor, water_recycling)
phase4.order.add_edge(growth_monitor, energy_audit)

# Phase 5: Harvest planning, quality check, pack produce (sequential)
phase5 = StrictPartialOrder(nodes=[harvest_plan, quality_check, pack_produce])
phase5.order.add_edge(harvest_plan, quality_check)
phase5.order.add_edge(quality_check, pack_produce)

# Phase 6: Distribute goods
phase6 = StrictPartialOrder(nodes=[distribute_goods])

# Phase 7: Data feedback loop to refine future cycles: loop of data_feedback leading to site_analysis
# Model the loop: After distributing goods, data_feedback happens and then loop back to site_analysis and onward.
# Use LOOP: body = site_analysis ... distribute_goods, redo = data_feedback

# Combine all phases (except loop) sequentially for the main cycle

main_cycle_nodes = [phase1, phase2, phase3, phase4, phase5, phase6]
main_cycle = StrictPartialOrder(nodes=main_cycle_nodes)
# Establish order between phases
main_cycle.order.add_edge(phase1, phase2)
main_cycle.order.add_edge(phase2, phase3)
main_cycle.order.add_edge(phase3, phase4)
main_cycle.order.add_edge(phase4, phase5)
main_cycle.order.add_edge(phase5, phase6)

# Loop structure: LOOP(body=main_cycle, redo=data_feedback)
# According to the semantics * (A,B): execute A, then choose to exit or execute B then A again
root = OperatorPOWL(operator=Operator.LOOP, children=[main_cycle, data_feedback])