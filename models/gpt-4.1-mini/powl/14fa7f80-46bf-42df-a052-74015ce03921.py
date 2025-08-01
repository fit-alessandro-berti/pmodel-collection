# Generated from: 14fa7f80-46bf-42df-a052-74015ce03921.json
# Description: This process outlines the complete operational cycle of an urban vertical farm specializing in sustainable crop production. It includes seed selection based on climate data, nutrient solution preparation, automated planting using robotic arms, continuous environmental monitoring, pest detection using AI imaging, dynamic lighting adjustment to optimize photosynthesis, pollination via controlled bee habitats, precision harvesting, post-harvest quality scanning, packaging with biodegradable materials, real-time inventory tracking, direct-to-consumer distribution, waste composting, energy consumption optimization, and data-driven yield forecasting. Each step integrates advanced technology and sustainability principles to maximize efficiency and minimize environmental impact within a confined urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition, OperatorPOWL
from pm4py.objects.process_tree.obj import Operator

Seed_Select = Transition(label='Seed Select')
Nutrient_Prep = Transition(label='Nutrient Prep')
Auto_Plant = Transition(label='Auto Plant')
Env_Monitor = Transition(label='Env Monitor')
Pest_Detect = Transition(label='Pest Detect')
Light_Adjust = Transition(label='Light Adjust')
Pollination = Transition(label='Pollination')
Precision_Harvest = Transition(label='Precision Harvest')
Quality_Scan = Transition(label='Quality Scan')
Eco_Package = Transition(label='Eco Package')
Inventory_Track = Transition(label='Inventory Track')
Consumer_Ship = Transition(label='Consumer Ship')
Waste_Compost = Transition(label='Waste Compost')
Energy_Optimize = Transition(label='Energy Optimize')
Yield_Forecast = Transition(label='Yield Forecast')

root = StrictPartialOrder(
    nodes=[
        Seed_Select,
        Nutrient_Prep,
        Auto_Plant,
        Env_Monitor,
        Pest_Detect,
        Light_Adjust,
        Pollination,
        Precision_Harvest,
        Quality_Scan,
        Eco_Package,
        Inventory_Track,
        Consumer_Ship,
        Waste_Compost,
        Energy_Optimize,
        Yield_Forecast
    ]
)

# Define order according to the operational cycle flow (serial order of main activities, some concurrency possible):

root.order.add_edge(Seed_Select, Nutrient_Prep)
root.order.add_edge(Nutrient_Prep, Auto_Plant)

# The following monitoring and detection activities occur concurrently after planting:

# Env Monitor, Pest Detect, Light Adjust, Pollination run concurrently after Auto Plant
root.order.add_edge(Auto_Plant, Env_Monitor)
root.order.add_edge(Auto_Plant, Pest_Detect)
root.order.add_edge(Auto_Plant, Light_Adjust)
root.order.add_edge(Auto_Plant, Pollination)

# Precision Harvest follows these; they all must complete before harvest can start, so order edges from all to Precision Harvest
root.order.add_edge(Env_Monitor, Precision_Harvest)
root.order.add_edge(Pest_Detect, Precision_Harvest)
root.order.add_edge(Light_Adjust, Precision_Harvest)
root.order.add_edge(Pollination, Precision_Harvest)

root.order.add_edge(Precision_Harvest, Quality_Scan)
root.order.add_edge(Quality_Scan, Eco_Package)
root.order.add_edge(Eco_Package, Inventory_Track)
root.order.add_edge(Inventory_Track, Consumer_Ship)

# Waste Compost and Energy Optimize run concurrently with distribution, so after Consumer Ship
root.order.add_edge(Consumer_Ship, Waste_Compost)
root.order.add_edge(Consumer_Ship, Energy_Optimize)

# Yield Forecast occurs after Waste Compost and Energy Optimize (data-driven forecasting aggregates all info)
root.order.add_edge(Waste_Compost, Yield_Forecast)
root.order.add_edge(Energy_Optimize, Yield_Forecast)