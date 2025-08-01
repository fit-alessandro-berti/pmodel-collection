# Generated from: 64a2e559-1075-46f5-86ac-c6995dfdd260.json
# Description: This process outlines the complex operational cycle of an urban vertical farm specializing in multi-crop production within a controlled environment. It involves initial seed sourcing and genetic selection, followed by nutrient solution optimization and automated planting. Continuous monitoring of microclimate variables and pest detection uses IoT sensors and AI-driven analytics. Crop growth is managed through adaptive lighting and irrigation schedules, integrating real-time data feedback. Harvesting is precisely timed using maturity indicators, and post-harvest handling includes automated sorting, quality inspection, and packaging. Waste biomass is recycled onsite through bio-digestion, generating energy and fertilizers. The process concludes with distribution logistics optimized for urban delivery routes, incorporating demand forecasting and sustainability metrics to minimize carbon footprint and maximize yield efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
seed_selection    = Transition(label='Seed Selection')
genetic_testing  = Transition(label='Genetic Testing')
nutrient_mix     = Transition(label='Nutrient Mix')
automated_plant  = Transition(label='Automated Plant')
micro_scan       = Transition(label='Microclimate Scan')
pest_detect      = Transition(label='Pest Detect')
light_control    = Transition(label='Light Control')
irrigation_set   = Transition(label='Irrigation Set')
growth_monitor   = Transition(label='Growth Monitor')
maturity_check   = Transition(label='Maturity Check')
auto_harvest     = Transition(label='Automated Harvest')
quality_inspect  = Transition(label='Quality Inspect')
sort_packaging   = Transition(label='Sort Packaging')
waste_recycling  = Transition(label='Waste Recycling')
energy_recovery  = Transition(label='Energy Recovery')
demand_forecast  = Transition(label='Demand Forecast')
delivery_plan    = Transition(label='Delivery Plan')

# Phase 1: initial seed & genetic work
# Phase 2: planting
# Phase 3: concurrent microclimate scan & pest detection
micro_pest_phase = StrictPartialOrder(nodes=[micro_scan, pest_detect])
# they run concurrently => no ordering edges

# Phase 4: adaptive growth loop (monitor -> [light + irrigation] -> monitor -> ...)
light_irrigation = StrictPartialOrder(nodes=[light_control, irrigation_set])
light_irrigation.order.add_edge(light_control, irrigation_set)
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, light_irrigation]
)

# Phase 5: harvest & post‐harvest handling
# Phase 6: waste recycling
# Phase 7: distribution planning
root = StrictPartialOrder(nodes=[
    seed_selection,
    genetic_testing,
    nutrient_mix,
    automated_plant,
    micro_pest_phase,
    growth_loop,
    maturity_check,
    auto_harvest,
    quality_inspect,
    sort_packaging,
    waste_recycling,
    energy_recovery,
    demand_forecast,
    delivery_plan
])

# Add the global partial‐order dependencies
root.order.add_edge(seed_selection,   genetic_testing)
root.order.add_edge(genetic_testing,  nutrient_mix)
root.order.add_edge(nutrient_mix,     automated_plant)

# After planting, start microclimate & pest detection
root.order.add_edge(automated_plant,  micro_pest_phase)

# Once sensing starts, go into the adaptive growth loop
root.order.add_edge(micro_pest_phase, growth_loop)

# After loop, proceed to maturity check and harvesting
root.order.add_edge(growth_loop,      maturity_check)
root.order.add_edge(maturity_check,   auto_harvest)
root.order.add_edge(auto_harvest,     quality_inspect)
root.order.add_edge(quality_inspect,  sort_packaging)

# Post‐harvest splits into recycling and distribution prep
root.order.add_edge(sort_packaging,   waste_recycling)
root.order.add_edge(sort_packaging,   demand_forecast)

# Waste recycling → energy recovery
root.order.add_edge(waste_recycling,  energy_recovery)

# Demand forecasting → delivery planning
root.order.add_edge(demand_forecast,  delivery_plan)