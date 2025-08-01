# Generated from: 0d047628-73c1-46ca-b60e-1588ea5bb56d.json
# Description: This process outlines the comprehensive operations involved in managing an urban vertical farming system that integrates hydroponics, automated climate control, and AI-driven crop monitoring. It includes seed selection, nutrient mixing, planting, growth tracking, pest detection, harvesting, quality assessment, packaging, and distribution logistics. The process ensures sustainable production by optimizing resource usage and minimizing waste, while adapting dynamically to environmental changes and market demands through continuous data analysis and feedback loops.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_sort      = Transition(label='Seed Sorting')
nutrient_prep  = Transition(label='Nutrient Prep')
planting       = Transition(label='Planting Beds')

climate        = Transition(label='Climate Adjust')
water          = Transition(label='Water Circulate')
light          = Transition(label='Light Tuning')
growth         = Transition(label='Growth Monitor')
pest           = Transition(label='Pest Scanning')
disease_alert  = Transition(label='Disease Alert')
skip           = SilentTransition()

data_analyze   = Transition(label='Data Analyze')

harvest        = Transition(label='Harvest Crop')
quality_check  = Transition(label='Quality Check')
pack_produce   = Transition(label='Pack Produce')
store_inventory= Transition(label='Store Inventory')
order_process  = Transition(label='Order Process')
dispatch_goods = Transition(label='Dispatch Goods')
waste_manage   = Transition(label='Waste Manage')

# Initial staging: Seed Sorting -> Nutrient Prep -> Planting Beds
initial_stage = StrictPartialOrder(nodes=[seed_sort, nutrient_prep, planting])
initial_stage.order.add_edge(seed_sort, nutrient_prep)
initial_stage.order.add_edge(nutrient_prep, planting)

# Monitoring sub-process: Climate Adjust -> Water Circulate -> Light Tuning -> Growth Monitor -> Pest Scanning -> XOR(Disease Alert, τ)
xor_disease = OperatorPOWL(operator=Operator.XOR, children=[disease_alert, skip])
monitoring_phase = StrictPartialOrder(nodes=[climate, water, light, growth, pest, xor_disease])
monitoring_phase.order.add_edge(climate, water)
monitoring_phase.order.add_edge(water, light)
monitoring_phase.order.add_edge(light, growth)
monitoring_phase.order.add_edge(growth, pest)
monitoring_phase.order.add_edge(pest, xor_disease)

# Loop: monitoring_phase then either exit or Data Analyze then repeat monitoring_phase
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_phase, data_analyze])

# Final staging: Harvest -> Quality Check -> Pack -> Store -> Order -> Dispatch -> Waste Manage
final_stage = StrictPartialOrder(nodes=[harvest, quality_check, pack_produce, store_inventory, order_process, dispatch_goods, waste_manage])
final_stage.order.add_edge(harvest, quality_check)
final_stage.order.add_edge(quality_check, pack_produce)
final_stage.order.add_edge(pack_produce, store_inventory)
final_stage.order.add_edge(store_inventory, order_process)
final_stage.order.add_edge(order_process, dispatch_goods)
final_stage.order.add_edge(dispatch_goods, waste_manage)

# Combine into the root process
root = StrictPartialOrder(nodes=[initial_stage, loop, final_stage])
root.order.add_edge(initial_stage, loop)
root.order.add_edge(loop, final_stage)