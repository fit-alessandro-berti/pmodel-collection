# Generated from: bf7c676c-39e6-4872-a6dd-ffdfffec2301.json
# Description: This process outlines the comprehensive cycle of urban vertical farming operations within a constrained city environment. It includes site preparation, modular system assembly, seedling nurturing, automated nutrient delivery, environmental monitoring, pest management using integrated biocontrols, crop growth tracking through AI analytics, harvest scheduling, post-harvest quality assessment, packaging with biodegradable materials, distribution logistics coordination, waste repurposing into bioenergy, market demand forecasting, continuous system upgrades, and community engagement for educational outreach. Each step integrates advanced technology with sustainable practices to optimize yield while minimizing ecological footprint in an urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_prep = Transition(label='Site Prep')
module_setup = Transition(label='Module Setup')
seedling_care = Transition(label='Seedling Care')
nutrient_flow = Transition(label='Nutrient Flow')
env_monitoring = Transition(label='Env Monitoring')
pest_control = Transition(label='Pest Control')
growth_tracking = Transition(label='Growth Tracking')
harvest_plan = Transition(label='Harvest Plan')
quality_check = Transition(label='Quality Check')
eco_packaging = Transition(label='Eco Packaging')
logistics_coord = Transition(label='Logistics Coord')
waste_recycle = Transition(label='Waste Recycle')
demand_forecast = Transition(label='Demand Forecast')
system_upgrade = Transition(label='System Upgrade')
community_meet = Transition(label='Community Meet')

# Build strict partial order following the described urban vertical farming workflow,
# assuming mostly sequential flow with some possible concurrency for monitoring/tracking and planning-related tasks

root = StrictPartialOrder(nodes=[
    site_prep,
    module_setup,
    seedling_care,
    nutrient_flow,
    env_monitoring,
    pest_control,
    growth_tracking,
    harvest_plan,
    quality_check,
    eco_packaging,
    logistics_coord,
    waste_recycle,
    demand_forecast,
    system_upgrade,
    community_meet,
])

# Define sequential order for main flow:
root.order.add_edge(site_prep, module_setup)
root.order.add_edge(module_setup, seedling_care)
root.order.add_edge(seedling_care, nutrient_flow)

# Pest control and environmental monitoring are part of ongoing care - parallel with nutrient flow
# But nutrient_flow should happen before pest_control, growth_tracking
root.order.add_edge(nutrient_flow, env_monitoring)
root.order.add_edge(nutrient_flow, pest_control)
root.order.add_edge(nutrient_flow, growth_tracking)

# Growth tracking depends on pest control and env monitoring (tracking after monitoring + pest control)
root.order.add_edge(pest_control, growth_tracking)
root.order.add_edge(env_monitoring, growth_tracking)

root.order.add_edge(growth_tracking, harvest_plan)

root.order.add_edge(harvest_plan, quality_check)
root.order.add_edge(quality_check, eco_packaging)
root.order.add_edge(eco_packaging, logistics_coord)

# Waste recycling happens after logistics (waste from packaging + shipping)
root.order.add_edge(logistics_coord, waste_recycle)

# Demand forecast and system upgrade happen later but can be after waste recycle or concurrent with community meeting
root.order.add_edge(waste_recycle, demand_forecast)
root.order.add_edge(demand_forecast, system_upgrade)

# Community meet can happen concurrently with system upgrade
# No ordering edges to allow concurrency with system upgrade and demand forecast
root.order.add_edge(waste_recycle, community_meet)

# root now models the described comprehensive vertical farming cycle with proper partial order
