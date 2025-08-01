# Generated from: b692e74c-a887-4025-91a2-f3266ebcb373.json
# Description: This process outlines the comprehensive cycle of urban vertical farming operations, integrating advanced hydroponic systems with AI-driven environmental controls and community engagement initiatives. It begins with seed selection based on local climate data, followed by nutrient solution preparation and precise planting schedules. Throughout growth, AI monitors plant health and adjusts light, humidity, and nutrient delivery to optimize yield. Periodic pest detection employs bio-control agents to maintain organic standards. Harvesting is synchronized with demand forecasts to minimize waste. Post-harvest, produce undergoes quality grading and packaging using sustainable materials. The cycle concludes with data analytics to refine future crops and community workshops to promote urban agriculture awareness, creating a resilient, eco-friendly food production loop within city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the basic activities
seed_select   = Transition(label="Seed Select")
nutrient_mix  = Transition(label="Nutrient Mix")
plant_setup   = Transition(label="Plant Setup")
ai_monitor    = Transition(label="AI Monitor")
env_adjust    = Transition(label="Env Adjust")
pest_detect   = Transition(label="Pest Detect")
bio_control   = Transition(label="Bio Control")
growth_audit  = Transition(label="Growth Audit")
demand_sync   = Transition(label="Demand Sync")
harvest_plan  = Transition(label="Harvest Plan")
quality_check = Transition(label="Quality Check")
eco_package   = Transition(label="Eco Package")
data_review   = Transition(label="Data Review")
crop_forecast = Transition(label="Crop Forecast")
community_train = Transition(label="Community Train")
waste_manage  = Transition(label="Waste Manage")

# Build a strict partial order capturing the (largely sequential) workflow
root = StrictPartialOrder(nodes=[
    seed_select, nutrient_mix, plant_setup,
    ai_monitor, env_adjust, pest_detect, bio_control, growth_audit,
    demand_sync, harvest_plan, quality_check, eco_package,
    data_review, crop_forecast, community_train, waste_manage
])

# Define the main control‐flow edges
root.order.add_edge(seed_select,   nutrient_mix)
root.order.add_edge(nutrient_mix,  plant_setup)
root.order.add_edge(plant_setup,   ai_monitor)
root.order.add_edge(ai_monitor,    env_adjust)
root.order.add_edge(env_adjust,    pest_detect)
root.order.add_edge(pest_detect,   bio_control)
root.order.add_edge(bio_control,   growth_audit)
root.order.add_edge(growth_audit,  demand_sync)
root.order.add_edge(demand_sync,   harvest_plan)
root.order.add_edge(harvest_plan,  quality_check)
root.order.add_edge(quality_check, eco_package)
root.order.add_edge(eco_package,   data_review)
root.order.add_edge(data_review,   crop_forecast)
root.order.add_edge(crop_forecast, community_train)
root.order.add_edge(community_train, waste_manage)