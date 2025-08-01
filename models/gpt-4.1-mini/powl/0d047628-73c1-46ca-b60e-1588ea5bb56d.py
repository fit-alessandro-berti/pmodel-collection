# Generated from: 0d047628-73c1-46ca-b60e-1588ea5bb56d.json
# Description: This process outlines the comprehensive operations involved in managing an urban vertical farming system that integrates hydroponics, automated climate control, and AI-driven crop monitoring. It includes seed selection, nutrient mixing, planting, growth tracking, pest detection, harvesting, quality assessment, packaging, and distribution logistics. The process ensures sustainable production by optimizing resource usage and minimizing waste, while adapting dynamically to environmental changes and market demands through continuous data analysis and feedback loops.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
seed_sorting = Transition(label='Seed Sorting')
nutrient_prep = Transition(label='Nutrient Prep')
planting_beds = Transition(label='Planting Beds')
climate_adjust = Transition(label='Climate Adjust')
water_circulate = Transition(label='Water Circulate')
growth_monitor = Transition(label='Growth Monitor')
pest_scanning = Transition(label='Pest Scanning')
disease_alert = Transition(label='Disease Alert')
light_tuning = Transition(label='Light Tuning')
harvest_crop = Transition(label='Harvest Crop')
quality_check = Transition(label='Quality Check')
pack_produce = Transition(label='Pack Produce')
store_inventory = Transition(label='Store Inventory')
order_process = Transition(label='Order Process')
dispatch_goods = Transition(label='Dispatch Goods')
waste_manage = Transition(label='Waste Manage')
data_analyze = Transition(label='Data Analyze')

# Model disease alert reaction as a choice:
# after Pest Scanning, either Disease Alert occurs or not (silent)
silent = SilentTransition()
disease_choice = OperatorPOWL(operator=Operator.XOR, children=[disease_alert, silent])

# Data analyze feedback loop:
# After Data Analyze, either exit or go to Climate Adjust + Light Tuning (environment adjustments) then Data Analyze again
env_adjust = StrictPartialOrder(nodes=[climate_adjust, light_tuning])
env_adjust.order.add_edge(climate_adjust, light_tuning)

loop_body = StrictPartialOrder(nodes=[env_adjust, water_circulate, growth_monitor, pest_scanning, disease_choice, harvest_crop, quality_check, pack_produce, store_inventory, order_process, dispatch_goods, waste_manage])
# Add order dependencies inside loop_body
loop_body.order.add_edge(env_adjust, water_circulate)
loop_body.order.add_edge(water_circulate, growth_monitor)
loop_body.order.add_edge(growth_monitor, pest_scanning)
loop_body.order.add_edge(pest_scanning, disease_choice)
loop_body.order.add_edge(disease_choice, harvest_crop)
loop_body.order.add_edge(harvest_crop, quality_check)
loop_body.order.add_edge(quality_check, pack_produce)
loop_body.order.add_edge(pack_produce, store_inventory)
loop_body.order.add_edge(store_inventory, order_process)
loop_body.order.add_edge(order_process, dispatch_goods)
loop_body.order.add_edge(dispatch_goods, waste_manage)

# Loop: Data Analyze first, then a loop of the above, repeated until exit
# LOOP(A, B): execute A, then choose to exit or execute B then A again, repeated
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, loop_body])

# Initial sequence: Seed Sorting --> Nutrient Prep --> Planting Beds --> loop
initial_seq = StrictPartialOrder(nodes=[seed_sorting, nutrient_prep, planting_beds, loop])
initial_seq.order.add_edge(seed_sorting, nutrient_prep)
initial_seq.order.add_edge(nutrient_prep, planting_beds)
initial_seq.order.add_edge(planting_beds, loop)

root = initial_seq