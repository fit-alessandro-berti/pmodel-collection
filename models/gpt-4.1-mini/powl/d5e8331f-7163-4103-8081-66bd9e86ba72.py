# Generated from: d5e8331f-7163-4103-8081-66bd9e86ba72.json
# Description: This process involves managing and optimizing the production cycle within a multi-level urban vertical farm. It includes site preparation, seed selection, nutrient management, environmental monitoring, automated pest control, and energy optimization. The cycle ensures sustainable crop yield while minimizing waste and resource consumption by integrating IoT sensors, AI-driven analytics, and robotic harvesting. Post-harvest activities include quality grading, packaging, cold storage, and direct distribution to local markets or restaurants. Continuous data feedback loops enable adaptive adjustments to improve efficiency and crop resilience throughout seasonal variations in an urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
site_prep = Transition(label='Site Prep')
seed_select = Transition(label='Seed Select')
nutrient_mix = Transition(label='Nutrient Mix')
planting_rows = Transition(label='Planting Rows')

env_monitor = Transition(label='Env Monitor')
water_adjust = Transition(label='Water Adjust')
pest_control = Transition(label='Pest Control')
growth_check = Transition(label='Growth Check')
light_calibrate = Transition(label='Light Calibrate')
energy_manage = Transition(label='Energy Manage')

harvest_crop = Transition(label='Harvest Crop')

quality_sort = Transition(label='Quality Sort')
pack_goods = Transition(label='Pack Goods')
cold_store = Transition(label='Cold Store')

market_ship = Transition(label='Market Ship')

data_analyze = Transition(label='Data Analyze')

# Loop body: environmental and growth monitoring and adjustment
# Loop over env_monitor, water_adjust, pest_control, growth_check, light_calibrate, energy_manage
# Cycle: after these adjustments, do data analysis that feeds back running these steps again or exit loop

# Loop children: 
# A = data_analyze (activity done after adjustments)
# B = partial order of the adjustments

# Build the partial order of the adjustments (B)
adjustments_nodes = [env_monitor, water_adjust, pest_control, growth_check, light_calibrate, energy_manage]
adjustments_po = StrictPartialOrder(nodes=adjustments_nodes)
# They can be concurrent (no order between them)

loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, adjustments_po])

# Production phase linear sequence
production_seq_nodes = [
    site_prep,
    seed_select,
    nutrient_mix,
    planting_rows,
    loop,
    harvest_crop
]

production_po = StrictPartialOrder(nodes=production_seq_nodes)
for i in range(len(production_seq_nodes) - 1):
    production_po.order.add_edge(production_seq_nodes[i], production_seq_nodes[i + 1])

# Post-harvest partial order: quality_sort -> pack_goods -> cold_store -> choice(market_ship,X(tau))
# Market shipment is a final choice between two alternatives: direct shipment or skip (silent)
tau = SilentTransition()
choice_ship = OperatorPOWL(operator=Operator.XOR, children=[market_ship, tau])

post_harvest_nodes = [quality_sort, pack_goods, cold_store, choice_ship]
post_harvest_po = StrictPartialOrder(nodes=post_harvest_nodes)
post_harvest_po.order.add_edge(quality_sort, pack_goods)
post_harvest_po.order.add_edge(pack_goods, cold_store)
post_harvest_po.order.add_edge(cold_store, choice_ship)

# The entire process: production_po --> post_harvest_po
root = StrictPartialOrder(nodes=[production_po, post_harvest_po])
root.order.add_edge(production_po, post_harvest_po)