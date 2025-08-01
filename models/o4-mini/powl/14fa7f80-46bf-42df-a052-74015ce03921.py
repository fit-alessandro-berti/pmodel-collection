# Generated from: 14fa7f80-46bf-42df-a052-74015ce03921.json
# Description: This process outlines the complete operational cycle of an urban vertical farm specializing in sustainable crop production. It includes seed selection based on climate data, nutrient solution preparation, automated planting using robotic arms, continuous environmental monitoring, pest detection using AI imaging, dynamic lighting adjustment to optimize photosynthesis, pollination via controlled bee habitats, precision harvesting, post-harvest quality scanning, packaging with biodegradable materials, real-time inventory tracking, direct-to-consumer distribution, waste composting, energy consumption optimization, and data-driven yield forecasting. Each step integrates advanced technology and sustainability principles to maximize efficiency and minimize environmental impact within a confined urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

activities = [
    'Seed Select', 'Nutrient Prep', 'Auto Plant', 'Env Monitor', 'Pest Detect',
    'Light Adjust', 'Pollination', 'Precision Harvest', 'Quality Scan',
    'Eco Package', 'Inventory Track', 'Consumer Ship', 'Waste Compost',
    'Energy Optimize', 'Yield Forecast'
]

# create a Transition object for each activity
nodes = [Transition(label=act) for act in activities]

# build a strict partial order where each step follows the previous one
root = StrictPartialOrder(nodes=nodes)
for i in range(len(nodes) - 1):
    root.order.add_edge(nodes[i], nodes[i + 1])