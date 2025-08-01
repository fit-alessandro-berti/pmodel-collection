# Generated from: 50df8b41-67a4-48ae-87d1-ab7710836e0c.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farming system designed to maximize crop yield in limited city spaces. It begins with seed selection tailored to urban climates and continues through nutrient blending, automated planting, and environmental monitoring using IoT sensors. The system integrates waste recycling from organic matter to produce bio-fertilizers, while AI-driven growth analysis optimizes lighting and hydration schedules. Pest control employs biological agents instead of chemicals to maintain eco-friendliness. Harvesting is coordinated with real-time market data to adjust crop variety dynamically. Post-harvest, produce is processed in modular packaging units to preserve freshness before distribution. The process also incorporates energy management to minimize carbon footprint, with periodic maintenance cycles ensuring system resilience and sustainability in a fluctuating urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_select     = Transition(label='Seed Select')
nutrient_blend  = Transition(label='Nutrient Blend')
auto_plant      = Transition(label='Auto Plant')
enviro_monitor  = Transition(label='Enviro Monitor')
waste_recycle   = Transition(label='Waste Recycle')
bio_fertilize   = Transition(label='Bio Fertilize')
growth_analyze  = Transition(label='Growth Analyze')
light_adjust    = Transition(label='Light Adjust')
water_schedule  = Transition(label='Water Schedule')
pest_control    = Transition(label='Pest Control')
market_sync     = Transition(label='Market Sync')
crop_harvest    = Transition(label='Crop Harvest')
pack_produce    = Transition(label='Pack Produce')
energy_manage   = Transition(label='Energy Manage')
system_maintain = Transition(label='System Maintain')
data_record     = Transition(label='Data Record')
yield_forecast  = Transition(label='Yield Forecast')

# Define the periodic maintenance loop: execute System Maintain, then either exit or do Data Record + repeat
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[system_maintain, data_record]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    seed_select,
    nutrient_blend,
    auto_plant,
    enviro_monitor,
    waste_recycle,
    bio_fertilize,
    growth_analyze,
    light_adjust,
    water_schedule,
    pest_control,
    market_sync,
    crop_harvest,
    pack_produce,
    energy_manage,
    maintenance_loop,
    yield_forecast
])

# Define the control‐flow dependencies (partial order edges)
o = root.order
o.add_edge(seed_select,    nutrient_blend)
o.add_edge(nutrient_blend, auto_plant)
o.add_edge(auto_plant,     enviro_monitor)
o.add_edge(enviro_monitor, waste_recycle)
o.add_edge(waste_recycle,  bio_fertilize)
o.add_edge(bio_fertilize,  growth_analyze)
# After growth analysis, adjust light and water concurrently
o.add_edge(growth_analyze, light_adjust)
o.add_edge(growth_analyze, water_schedule)
# Both adjustments must complete before pest control
o.add_edge(light_adjust,   pest_control)
o.add_edge(water_schedule, pest_control)
o.add_edge(pest_control,   market_sync)
o.add_edge(market_sync,    crop_harvest)
o.add_edge(crop_harvest,   pack_produce)
o.add_edge(pack_produce,   energy_manage)
# Energy management precedes the maintenance loop, which then leads to final yield forecast
o.add_edge(energy_manage,   maintenance_loop)
o.add_edge(maintenance_loop, yield_forecast)