# Generated from: 5c5c8877-65d3-4639-b322-13052b49a8d8.json
# Description: This process outlines an adaptive urban farming cycle designed to optimize crop yield within constrained city environments. It involves initial soil analysis and microclimate assessment to tailor cultivation strategies, followed by nutrient cycling using organic waste sourced locally. Continuous monitoring of plant health is integrated with IoT sensor data to dynamically adjust watering and light exposure. The process further includes pest bio-control using native species, community engagement for shared resources, and iterative yield forecasting to plan harvest and distribution. Finally, waste biomass is repurposed for energy generation, closing the loop in a sustainable urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Soil_Analysis = Transition(label='Soil Analysis')
Climate_Assess = Transition(label='Climate Assess')

Waste_Sourcing = Transition(label='Waste Sourcing')
Nutrient_Cycling = Transition(label='Nutrient Cycling')

Seed_Selection = Transition(label='Seed Selection')
Planting_Setup = Transition(label='Planting Setup')

Sensor_Deploy = Transition(label='Sensor Deploy')
Health_Monitor = Transition(label='Health Monitor')

Water_Adjust = Transition(label='Water Adjust')
Light_Control = Transition(label='Light Control')

Pest_BioControl = Transition(label='Pest BioControl')
Community_Engage = Transition(label='Community Engage')

Yield_Forecast = Transition(label='Yield Forecast')
Harvest_Plan = Transition(label='Harvest Plan')

Biomass_Energy = Transition(label='Biomass Energy')

# Partial order for initial soil and climate assessment in parallel
initial_assessment = StrictPartialOrder(nodes=[Soil_Analysis, Climate_Assess])
# no ordering edges -> concurrent activities

# Nutrient cycling after waste sourcing
nutrient_proc = StrictPartialOrder(nodes=[Waste_Sourcing, Nutrient_Cycling])
nutrient_proc.order.add_edge(Waste_Sourcing, Nutrient_Cycling)

# Seed selection and planting setup in sequence
planting_setup_proc = StrictPartialOrder(nodes=[Seed_Selection, Planting_Setup])
planting_setup_proc.order.add_edge(Seed_Selection, Planting_Setup)

# Sensor deploy before health monitor
monitoring_proc = StrictPartialOrder(nodes=[Sensor_Deploy, Health_Monitor])
monitoring_proc.order.add_edge(Sensor_Deploy, Health_Monitor)

# Water adjust and light control in parallel after monitoring
watering_light = StrictPartialOrder(nodes=[Water_Adjust, Light_Control])
# no order edges, concurrent adjustment activities

# Combine monitoring and adjustments in partial order:
monitoring_and_adjust = StrictPartialOrder(
    nodes=[monitoring_proc, watering_light]
)
monitoring_and_adjust.order.add_edge(monitoring_proc, watering_light)

# Pest bio control and community engage can be concurrent
community_proc = StrictPartialOrder(nodes=[Pest_BioControl, Community_Engage])
# no order edges

# Yield forecast and harvest plan in sequence
forecast_harvest = StrictPartialOrder(nodes=[Yield_Forecast, Harvest_Plan])
forecast_harvest.order.add_edge(Yield_Forecast, Harvest_Plan)

# Build loop for yield forecasting and harvest planning (iterative)
forecast_harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[forecast_harvest, monitoring_and_adjust])
# interpretation: run forecast_harvest, then either exit or do monitoring_and_adjust then forecast_harvest again

# Final process partial order
root = StrictPartialOrder(
    nodes=[
        initial_assessment,
        nutrient_proc,
        planting_setup_proc,
        forecast_harvest_loop,
        community_proc,
        Biomass_Energy,
    ]
)

# Add control flow edges according to the description/order:

# 1. initial assessment precedes nutrient cycling and planting setup
root.order.add_edge(initial_assessment, nutrient_proc)
root.order.add_edge(initial_assessment, planting_setup_proc)

# 2. nutrient cycling and planting setup precede loop (forecast/harvest + monitoring/adjust)
root.order.add_edge(nutrient_proc, forecast_harvest_loop)
root.order.add_edge(planting_setup_proc, forecast_harvest_loop)

# 3. community engagement and pest biocontrol proceed independently but precede biomass energy
root.order.add_edge(community_proc, Biomass_Energy)

# 4. forecast_harvest_loop precedes biomass energy (closing loop)
root.order.add_edge(forecast_harvest_loop, Biomass_Energy)

# 5. pest bio control in community_proc — no ordering needed between pest bio control and community engage, both precede biomass energy (already added)

# This models:
# - Initial soil and climate checks parallel
# - Waste sourcing -> nutrient cycling
# - Seed selection -> planting setup
# - Sensor deploy -> health monitor -> (water adjust || light control) in parallel
# - Loop of yield forecasting & harvest planning with monitoring/adjustments
# - Pest bio control & community engage in parallel
# - All feeding into biomass energy final step
