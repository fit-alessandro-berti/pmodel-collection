# Generated from: 50df8b41-67a4-48ae-87d1-ab7710836e0c.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farming system designed to maximize crop yield in limited city spaces. It begins with seed selection tailored to urban climates and continues through nutrient blending, automated planting, and environmental monitoring using IoT sensors. The system integrates waste recycling from organic matter to produce bio-fertilizers, while AI-driven growth analysis optimizes lighting and hydration schedules. Pest control employs biological agents instead of chemicals to maintain eco-friendliness. Harvesting is coordinated with real-time market data to adjust crop variety dynamically. Post-harvest, produce is processed in modular packaging units to preserve freshness before distribution. The process also incorporates energy management to minimize carbon footprint, with periodic maintenance cycles ensuring system resilience and sustainability in a fluctuating urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Select = Transition(label='Seed Select')
Nutrient_Blend = Transition(label='Nutrient Blend')
Auto_Plant = Transition(label='Auto Plant')
Enviro_Monitor = Transition(label='Enviro Monitor')
Waste_Recycle = Transition(label='Waste Recycle')
Bio_Fertilize = Transition(label='Bio Fertilize')
Growth_Analyze = Transition(label='Growth Analyze')
Light_Adjust = Transition(label='Light Adjust')
Water_Schedule = Transition(label='Water Schedule')
Pest_Control = Transition(label='Pest Control')
Market_Sync = Transition(label='Market Sync')
Crop_Harvest = Transition(label='Crop Harvest')
Pack_Produce = Transition(label='Pack Produce')
Energy_Manage = Transition(label='Energy Manage')
System_Maintain = Transition(label='System Maintain')
Data_Record = Transition(label='Data Record')
Yield_Forecast = Transition(label='Yield Forecast')

# Define loop for maintenance cycle:
# * (System_Maintain, Data_Record)
# maintenance cycle: execute maintenance, then choose to exit or do data record then maintenance again
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[System_Maintain, Data_Record])

# Define partial order of initial core workflow before maintenance and final forecasting

# Partial order nodes are:
# Seed_Select --> Nutrient_Blend --> Auto_Plant --> Enviro_Monitor

# After Enviro_Monitor:
# Two branches concurrently:
# 1) Waste_Recycle --> Bio_Fertilize (waste recycling branch)
# 2) Growth_Analyze --> (Light_Adjust and Water_Schedule concurently) --> Pest_Control
# Then all converge before Market_Sync

# Define Light_Adjust and Water_Schedule as concurrent (no order)

# After Pest_Control and Waste branch Bio_Fertilize complete, join before Market_Sync

# After Market_Sync --> Crop_Harvest --> Pack_Produce

# Energy_Manage can run concurrently anytime after Enviro_Monitor before harvesting

po_nodes = [
    Seed_Select,
    Nutrient_Blend,
    Auto_Plant,
    Enviro_Monitor,
    Waste_Recycle,
    Bio_Fertilize,
    Growth_Analyze,
    Light_Adjust,
    Water_Schedule,
    Pest_Control,
    Market_Sync,
    Crop_Harvest,
    Pack_Produce,
    Energy_Manage,
    maintenance_loop,
    Yield_Forecast
]

root = StrictPartialOrder(nodes=po_nodes)

# Define order edges

# Initial linear sequence
root.order.add_edge(Seed_Select, Nutrient_Blend)
root.order.add_edge(Nutrient_Blend, Auto_Plant)
root.order.add_edge(Auto_Plant, Enviro_Monitor)

# Waste recycle branch: Waste_Recycle --> Bio_Fertilize
root.order.add_edge(Enviro_Monitor, Waste_Recycle)
root.order.add_edge(Waste_Recycle, Bio_Fertilize)

# Growth analyze branch: Growth_Analyze --> Pest_Control
# Light_Adjust and Water_Schedule concurrent after Growth_Analyze, both before Pest_Control
root.order.add_edge(Enviro_Monitor, Growth_Analyze)
root.order.add_edge(Growth_Analyze, Light_Adjust)
root.order.add_edge(Growth_Analyze, Water_Schedule)
root.order.add_edge(Light_Adjust, Pest_Control)
root.order.add_edge(Water_Schedule, Pest_Control)

# Pest_Control after both Light_Adjust and Water_Schedule done
# Waste branch Bio_Fertilize and Pest_Control must both complete before Market_Sync
root.order.add_edge(Bio_Fertilize, Market_Sync)
root.order.add_edge(Pest_Control, Market_Sync)

# Market_Sync --> Crop_Harvest --> Pack_Produce --> Yield_Forecast
root.order.add_edge(Market_Sync, Crop_Harvest)
root.order.add_edge(Crop_Harvest, Pack_Produce)
root.order.add_edge(Pack_Produce, Yield_Forecast)

# Energy_Manage concurrent with branches after Enviro_Monitor,
# so Energy_Manage happens after Enviro_Monitor, before Crop_Harvest
root.order.add_edge(Enviro_Monitor, Energy_Manage)

# Energy_Manage and Market_Sync can run in any order, so no edge between them
# But Energy_Manage must be done before Crop_Harvest to affect harvesting

root.order.add_edge(Energy_Manage, Crop_Harvest)

# Maintenance loop can happen anytime after Enviro_Monitor but before Yield_Forecast.
# To allow flexibility, connect Enviro_Monitor --> maintenance_loop --> Yield_Forecast

root.order.add_edge(Enviro_Monitor, maintenance_loop)
root.order.add_edge(maintenance_loop, Yield_Forecast)