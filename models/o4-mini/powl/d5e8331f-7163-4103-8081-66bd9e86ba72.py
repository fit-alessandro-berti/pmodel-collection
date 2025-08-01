# Generated from: d5e8331f-7163-4103-8081-66bd9e86ba72.json
# Description: This process involves managing and optimizing the production cycle within a multi-level urban vertical farm. It includes site preparation, seed selection, nutrient management, environmental monitoring, automated pest control, and energy optimization. The cycle ensures sustainable crop yield while minimizing waste and resource consumption by integrating IoT sensors, AI-driven analytics, and robotic harvesting. Post-harvest activities include quality grading, packaging, cold storage, and direct distribution to local markets or restaurants. Continuous data feedback loops enable adaptive adjustments to improve efficiency and crop resilience throughout seasonal variations in an urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_prep      = Transition(label='Site Prep')
seed_select    = Transition(label='Seed Select')
nutrient_mix   = Transition(label='Nutrient Mix')
planting_rows  = Transition(label='Planting Rows')
env_monitor    = Transition(label='Env Monitor')
water_adjust   = Transition(label='Water Adjust')
pest_control   = Transition(label='Pest Control')
growth_check   = Transition(label='Growth Check')
light_calibrate= Transition(label='Light Calibrate')
energy_manage  = Transition(label='Energy Manage')
harvest_crop   = Transition(label='Harvest Crop')
quality_sort   = Transition(label='Quality Sort')
pack_goods     = Transition(label='Pack Goods')
cold_store     = Transition(label='Cold Store')
market_ship    = Transition(label='Market Ship')
data_analyze   = Transition(label='Data Analyze')

# Build the full production + post-harvest sequence as a strict partial order
po_cycle = StrictPartialOrder(nodes=[
    site_prep, seed_select, nutrient_mix, planting_rows,
    env_monitor, water_adjust, pest_control, growth_check,
    light_calibrate, energy_manage,
    harvest_crop, quality_sort, pack_goods, cold_store, market_ship
])
# Site prep → seed selection → nutrient mix → planting
po_cycle.order.add_edge(site_prep, seed_select)
po_cycle.order.add_edge(seed_select, nutrient_mix)
po_cycle.order.add_edge(nutrient_mix, planting_rows)
# Planting → environmental monitoring → water adjust → pest control → growth check → light calibrate → energy manage
po_cycle.order.add_edge(planting_rows, env_monitor)
po_cycle.order.add_edge(env_monitor, water_adjust)
po_cycle.order.add_edge(water_adjust, pest_control)
po_cycle.order.add_edge(pest_control, growth_check)
po_cycle.order.add_edge(growth_check, light_calibrate)
po_cycle.order.add_edge(light_calibrate, energy_manage)
# Energy manage → harvest → quality sort → packaging → cold storage → shipping
po_cycle.order.add_edge(energy_manage, harvest_crop)
po_cycle.order.add_edge(harvest_crop, quality_sort)
po_cycle.order.add_edge(quality_sort, pack_goods)
po_cycle.order.add_edge(pack_goods, cold_store)
po_cycle.order.add_edge(cold_store, market_ship)

# Wrap the cycle in a loop: after each full cycle optionally do data analysis, then repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[po_cycle, data_analyze]
)