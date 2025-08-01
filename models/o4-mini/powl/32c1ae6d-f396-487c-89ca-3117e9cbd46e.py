# Generated from: 32c1ae6d-f396-487c-89ca-3117e9cbd46e.json
# Description: This process outlines the comprehensive management cycle of an urban vertical farm that integrates IoT monitoring, automated nutrient delivery, and sustainable energy usage. It begins with environmental sensing to assess light, humidity, and temperature, followed by adaptive lighting adjustments. Water recycling and nutrient mixing are precisely controlled to optimize plant growth. Pollination is facilitated through robotic drones, while growth progress is tracked via computer vision systems. Harvest scheduling aligns with demand forecasting, and post-harvest processing includes packaging and quality assurance. Waste materials are composted onsite, and energy consumption is continuously optimized through smart grid integration, ensuring minimal environmental impact and maximum yield in a constrained urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# define transitions
env       = Transition(label='Env Sensing')
light     = Transition(label='Light Adjust')
hum       = Transition(label='Humidity Check')
temp      = Transition(label='Temp Control')
nut       = Transition(label='Nutrient Mix')
water     = Transition(label='Water Recycle')
drone     = Transition(label='Drone Pollinate')
scan      = Transition(label='Growth Scan')
pest      = Transition(label='Pest Detect')
harvest   = Transition(label='Harvest Plan')
demand    = Transition(label='Demand Forecast')
quality   = Transition(label='Quality Check')
pack      = Transition(label='Pack Produce')
waste     = Transition(label='Waste Compost')
energy    = Transition(label='Energy Optimize')
archive   = Transition(label='Data Archive')

# build partial order
root = StrictPartialOrder(nodes=[
    env, light, hum, temp,
    nut, water,
    drone, scan, pest,
    harvest, demand, quality, pack,
    waste, energy, archive
])

# sensing to environment controls
root.order.add_edge(env, light)
root.order.add_edge(env, hum)
root.order.add_edge(env, temp)

# environment controls to nutrient and water
for ctrl in (light, hum, temp):
    root.order.add_edge(ctrl, nut)
    root.order.add_edge(ctrl, water)

# nutrient and water to plant care activities
for src in (nut, water):
    root.order.add_edge(src, drone)
    root.order.add_edge(src, scan)
    root.order.add_edge(src, pest)

# plant care to harvest planning
for src in (drone, scan, pest):
    root.order.add_edge(src, harvest)

# harvest planning sequence
root.order.add_edge(harvest, demand)
root.order.add_edge(demand, quality)
root.order.add_edge(quality, pack)

# post-harvest and utilities
root.order.add_edge(pack, waste)
root.order.add_edge(pack, energy)

# final archive after composting and energy optimization
root.order.add_edge(waste, archive)
root.order.add_edge(energy, archive)