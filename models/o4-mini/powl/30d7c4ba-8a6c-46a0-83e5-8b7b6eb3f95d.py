# Generated from: 30d7c4ba-8a6c-46a0-83e5-8b7b6eb3f95d.json
# Description: This process details the comprehensive cycle of managing an urban vertical farm that integrates IoT sensors, AI-driven analytics, and automated hydroponic systems to optimize crop yield year-round. Starting from environmental setup and seed selection, the process includes nutrient mixing, growth monitoring, pest detection via drones, adaptive lighting control, and harvesting automation. Post-harvest activities encompass quality sorting, packaging using biodegradable materials, and distribution logistics tailored for city-based delivery. The process also incorporates sustainability checks, energy consumption audits, and community engagement initiatives to ensure ecological balance and social impact within the urban farming ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
sensors    = Transition(label='Setup Sensors')
seeds      = Transition(label='Select Seeds')
mix        = Transition(label='Mix Nutrients')
plant      = Transition(label='Plant Crops')
monitor    = Transition(label='Monitor Growth')
detect     = Transition(label='Detect Pests')
lighting   = Transition(label='Adjust Lighting')
climate    = Transition(label='Control Climate')
water      = Transition(label='Automate Watering')
harvest    = Transition(label='Harvest Crops')
sort_q     = Transition(label='Sort Quality')
pack       = Transition(label='Package Goods')
delivery   = Transition(label='Plan Delivery')
audit      = Transition(label='Audit Energy')
engage     = Transition(label='Engage Community')
recycle    = Transition(label='Recycle Waste')

# Build one cycle of the vertical farm process as a partial order
cycle = StrictPartialOrder(nodes=[
    sensors, seeds, mix, plant,
    monitor, detect, lighting, climate, water,
    harvest, sort_q, pack, delivery, audit, engage, recycle
])

# Sequential setup and planting
cycle.order.add_edge(sensors, seeds)
cycle.order.add_edge(seeds, mix)
cycle.order.add_edge(mix, plant)

# Concurrent monitoring & control after planting
for activity in [monitor, detect, lighting, climate, water]:
    cycle.order.add_edge(plant, activity)
    cycle.order.add_edge(activity, harvest)

# Post-harvest sequence
cycle.order.add_edge(harvest, sort_q)
cycle.order.add_edge(sort_q, pack)
cycle.order.add_edge(pack, delivery)
cycle.order.add_edge(delivery, audit)
cycle.order.add_edge(audit, engage)
cycle.order.add_edge(engage, recycle)

# Wrap the whole cycle in a LOOP to allow repeated yearly cycles
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, cycle])

# Final POWL model
root = loop