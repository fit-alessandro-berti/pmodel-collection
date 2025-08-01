# Generated from: 6d25306f-a8a7-4e5f-b8bc-f7e2c378f65b.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed commercial building. It involves site analysis, modular system design, climate control setup, nutrient solution preparation, seed selection, automated planting, real-time environment monitoring, pest control without chemicals, energy optimization, crop growth tracking, harvest scheduling, yield analysis, waste recycling, packaging design, and distribution logistics. The process integrates sustainable technologies and data-driven decision making to maximize crop yield in limited urban spaces while minimizing environmental impact and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
site_analysis    = Transition(label='Site Analysis')
system_design    = Transition(label='System Design')
climate_setup    = Transition(label='Climate Setup')
nutrient_prep    = Transition(label='Nutrient Prep')
seed_selection   = Transition(label='Seed Selection')
automated_plant  = Transition(label='Automated Plant')
env_monitoring   = Transition(label='Env Monitoring')
pest_control     = Transition(label='Pest Control')
energy_optimize  = Transition(label='Energy Optimize')
growth_tracking  = Transition(label='Growth Tracking')
harvest_plan     = Transition(label='Harvest Plan')
yield_analyze    = Transition(label='Yield Analyze')
waste_recycle    = Transition(label='Waste Recycle')
package_design   = Transition(label='Package Design')
distribution     = Transition(label='Distribution')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis, system_design, climate_setup,
    nutrient_prep, seed_selection, automated_plant,
    env_monitoring, pest_control, energy_optimize,
    growth_tracking, harvest_plan, yield_analyze,
    waste_recycle, package_design, distribution
])

# Sequential and partial‐order dependencies
root.order.add_edge(site_analysis, system_design)
root.order.add_edge(system_design, climate_setup)

# Parallel nutrient preparation and seed selection after climate setup
root.order.add_edge(climate_setup, nutrient_prep)
root.order.add_edge(climate_setup, seed_selection)

# Both preparatory tasks precede automated planting
root.order.add_edge(nutrient_prep, automated_plant)
root.order.add_edge(seed_selection, automated_plant)

# After planting, multiple monitoring/optimization tasks run in parallel
root.order.add_edge(automated_plant, env_monitoring)
root.order.add_edge(automated_plant, pest_control)
root.order.add_edge(automated_plant, energy_optimize)
root.order.add_edge(automated_plant, growth_tracking)

# All monitoring outputs feed into the harvest planning
root.order.add_edge(env_monitoring, harvest_plan)
root.order.add_edge(pest_control, harvest_plan)
root.order.add_edge(energy_optimize, harvest_plan)
root.order.add_edge(growth_tracking, harvest_plan)

# Harvest plan leads to yield analysis
root.order.add_edge(harvest_plan, yield_analyze)

# Post‐analysis tasks can proceed in parallel
root.order.add_edge(yield_analyze, waste_recycle)
root.order.add_edge(yield_analyze, package_design)
root.order.add_edge(yield_analyze, distribution)