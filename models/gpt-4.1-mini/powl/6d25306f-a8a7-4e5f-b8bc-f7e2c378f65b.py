# Generated from: 6d25306f-a8a7-4e5f-b8bc-f7e2c378f65b.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed commercial building. It involves site analysis, modular system design, climate control setup, nutrient solution preparation, seed selection, automated planting, real-time environment monitoring, pest control without chemicals, energy optimization, crop growth tracking, harvest scheduling, yield analysis, waste recycling, packaging design, and distribution logistics. The process integrates sustainable technologies and data-driven decision making to maximize crop yield in limited urban spaces while minimizing environmental impact and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all activities as Transitions:
site_analysis = Transition(label='Site Analysis')
system_design = Transition(label='System Design')
climate_setup = Transition(label='Climate Setup')
nutrient_prep = Transition(label='Nutrient Prep')
seed_selection = Transition(label='Seed Selection')
automated_plant = Transition(label='Automated Plant')
env_monitoring = Transition(label='Env Monitoring')
pest_control = Transition(label='Pest Control')
energy_optimize = Transition(label='Energy Optimize')
growth_tracking = Transition(label='Growth Tracking')
harvest_plan = Transition(label='Harvest Plan')
yield_analyze = Transition(label='Yield Analyze')
waste_recycle = Transition(label='Waste Recycle')
package_design = Transition(label='Package Design')
distribution = Transition(label='Distribution')

# Build partial order according to typical logical sequence:

# Initial phase: Site Analysis --> System Design --> Climate Setup & Nutrient Prep concur
# Then Seed Selection before Automated Plant
# After planting, concurrent monitoring & pest control & energy optimization
# Followed by Growth Tracking --> Harvest Plan --> Yield Analyze
# Then Waste Recycle & Package Design concur before final Distribution

root = StrictPartialOrder(
    nodes=[
        site_analysis, system_design, climate_setup, nutrient_prep,
        seed_selection, automated_plant,
        env_monitoring, pest_control, energy_optimize,
        growth_tracking, harvest_plan, yield_analyze,
        waste_recycle, package_design, distribution
    ]
)

order = root.order
# Sequential starting chain
order.add_edge(site_analysis, system_design)
order.add_edge(system_design, climate_setup)
order.add_edge(system_design, nutrient_prep)
# Climate Setup and Nutrient Prep run concurrently (no order edge between them)

# Both must finish before Seed Selection
order.add_edge(climate_setup, seed_selection)
order.add_edge(nutrient_prep, seed_selection)

order.add_edge(seed_selection, automated_plant)

# After planting start concurrent monitoring, pest control, energy optimize
order.add_edge(automated_plant, env_monitoring)
order.add_edge(automated_plant, pest_control)
order.add_edge(automated_plant, energy_optimize)

# These three run concurrently (no further order between them)

# Then Growth Tracking after at least monitoring and pest control finish
order.add_edge(env_monitoring, growth_tracking)
order.add_edge(pest_control, growth_tracking)
order.add_edge(energy_optimize, growth_tracking)  # assume also needed

order.add_edge(growth_tracking, harvest_plan)
order.add_edge(harvest_plan, yield_analyze)

# Waste Recycle and Package Design concurrent after Yield Analyze
order.add_edge(yield_analyze, waste_recycle)
order.add_edge(yield_analyze, package_design)

# Both must finish before Distribution
order.add_edge(waste_recycle, distribution)
order.add_edge(package_design, distribution)