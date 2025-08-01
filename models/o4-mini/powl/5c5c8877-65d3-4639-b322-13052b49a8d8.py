# Generated from: 5c5c8877-65d3-4639-b322-13052b49a8d8.json
# Description: This process outlines an adaptive urban farming cycle designed to optimize crop yield within constrained city environments. It involves initial soil analysis and microclimate assessment to tailor cultivation strategies, followed by nutrient cycling using organic waste sourced locally. Continuous monitoring of plant health is integrated with IoT sensor data to dynamically adjust watering and light exposure. The process further includes pest bio-control using native species, community engagement for shared resources, and iterative yield forecasting to plan harvest and distribution. Finally, waste biomass is repurposed for energy generation, closing the loop in a sustainable urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
soil_analysis    = Transition(label='Soil Analysis')
climate_assess   = Transition(label='Climate Assess')
waste_sourcing   = Transition(label='Waste Sourcing')
nutrient_cycling = Transition(label='Nutrient Cycling')
seed_selection   = Transition(label='Seed Selection')
planting_setup   = Transition(label='Planting Setup')
sensor_deploy    = Transition(label='Sensor Deploy')
health_monitor   = Transition(label='Health Monitor')
water_adjust     = Transition(label='Water Adjust')
light_control    = Transition(label='Light Control')
pest_biocontrol  = Transition(label='Pest BioControl')
community_engage = Transition(label='Community Engage')
yield_forecast   = Transition(label='Yield Forecast')
harvest_plan     = Transition(label='Harvest Plan')
biomass_energy   = Transition(label='Biomass Energy')

# Build the loop sub‐process: monitor health, then optionally adjust water & light, repeat
adjustments = StrictPartialOrder(nodes=[water_adjust, light_control])
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[health_monitor, adjustments])

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    soil_analysis,
    climate_assess,
    waste_sourcing,
    nutrient_cycling,
    seed_selection,
    planting_setup,
    sensor_deploy,
    monitor_loop,
    pest_biocontrol,
    community_engage,
    yield_forecast,
    harvest_plan,
    biomass_energy
])

# Define the control‐flow dependencies
root.order.add_edge(soil_analysis,    waste_sourcing)
root.order.add_edge(climate_assess,   waste_sourcing)
root.order.add_edge(waste_sourcing,   nutrient_cycling)
root.order.add_edge(nutrient_cycling, seed_selection)
root.order.add_edge(seed_selection,   planting_setup)
root.order.add_edge(planting_setup,   sensor_deploy)
root.order.add_edge(sensor_deploy,    monitor_loop)
root.order.add_edge(monitor_loop,     pest_biocontrol)
root.order.add_edge(pest_biocontrol,  community_engage)
root.order.add_edge(community_engage, yield_forecast)
root.order.add_edge(yield_forecast,   harvest_plan)
root.order.add_edge(harvest_plan,     biomass_energy)