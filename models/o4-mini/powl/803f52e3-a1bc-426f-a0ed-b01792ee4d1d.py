# Generated from: 803f52e3-a1bc-426f-a0ed-b01792ee4d1d.json
# Description: This process describes the comprehensive operational cycle of an urban vertical farm integrating IoT sensors, AI-driven crop monitoring, and automated nutrient delivery. It begins with environmental calibration and seed selection, followed by germination, growth monitoring, and adaptive lighting control. Concurrently, water recycling and pest detection systems operate to maintain optimal conditions. Harvesting is coordinated with supply chain logistics for immediate distribution to local markets. Post-harvest, waste composting and data analysis optimize future cycles, ensuring sustainability and efficient resource use within constrained urban spaces. The process intricately balances technology, biology, and logistics to maximize yield and minimize environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
env_setup      = Transition(label='Env Setup')
seed_select    = Transition(label='Seed Select')
seed_plant     = Transition(label='Seed Plant')
germinate      = Transition(label='Germinate')
monitor_growth = Transition(label='Monitor Growth')
adjust_light   = Transition(label='Adjust Light')
nutrient_feed  = Transition(label='Nutrient Feed')
water_recycle  = Transition(label='Water Recycle')
pest_scan      = Transition(label='Pest Scan')
harvest_crop   = Transition(label='Harvest Crop')
pack_produce   = Transition(label='Pack Produce')
dispatch_goods = Transition(label='Dispatch Goods')
waste_compost  = Transition(label='Waste Compost')
data_analyze   = Transition(label='Data Analyze')
cycle_review   = Transition(label='Cycle Review')

# Build the partial order
root = StrictPartialOrder(nodes=[
    env_setup, seed_select, seed_plant, germinate,
    monitor_growth, adjust_light, nutrient_feed,
    water_recycle, pest_scan,
    harvest_crop, pack_produce, dispatch_goods,
    waste_compost, data_analyze, cycle_review
])

# Sequence: setup → select → plant → germinate
root.order.add_edge(env_setup,   seed_select)
root.order.add_edge(seed_select, seed_plant)
root.order.add_edge(seed_plant,  germinate)

# After germination: start monitoring, water recycling, pest scanning
root.order.add_edge(germinate,      monitor_growth)
root.order.add_edge(germinate,      water_recycle)
root.order.add_edge(germinate,      pest_scan)

# Monitoring leads to adjusting light and nutrient feed
root.order.add_edge(monitor_growth, adjust_light)
root.order.add_edge(monitor_growth, nutrient_feed)

# Harvest waits for all maintenance branches to complete
root.order.add_edge(adjust_light,  harvest_crop)
root.order.add_edge(nutrient_feed, harvest_crop)
root.order.add_edge(water_recycle, harvest_crop)
root.order.add_edge(pest_scan,     harvest_crop)

# Then packing and dispatch
root.order.add_edge(harvest_crop,   pack_produce)
root.order.add_edge(pack_produce,   dispatch_goods)

# Post‐harvest: waste composting and data analysis in parallel
root.order.add_edge(dispatch_goods, waste_compost)
root.order.add_edge(dispatch_goods, data_analyze)

# Final review after both post‐harvest tasks
root.order.add_edge(waste_compost,  cycle_review)
root.order.add_edge(data_analyze,   cycle_review)