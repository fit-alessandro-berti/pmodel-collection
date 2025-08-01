# Generated from: bf8151aa-0b34-4ef6-91f1-ba6617479c7e.json
# Description: This process governs the entire operational cycle of an urban vertical farm that integrates hydroponic and aeroponic systems within a multi-story building. It begins with seed selection optimized for limited space and light conditions, followed by germination monitoring using AI sensors. Nutrient mixing and delivery are dynamically adjusted based on real-time plant health data. Concurrently, microclimate controls regulate humidity, temperature, and CO2 levels floor-by-floor. Pollination is artificially induced via robotic drones, while pest detection employs machine vision and targeted biocontrol agents. Harvesting is scheduled by growth stage prediction models, ensuring peak freshness. Post-harvest, produce undergoes automated cleaning, packaging, and quality sorting before distribution. Waste biomass is recycled onsite into compost or bioenergy. Throughout the cycle, data analytics optimize energy usage and yield forecasts, supporting continuous improvements in urban agriculture sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all transitions
seed_select       = Transition(label='Seed Select')
germinate_monitor = Transition(label='Germinate Monitor')
nutrient_mix      = Transition(label='Nutrient Mix')
nutrient_deliver  = Transition(label='Nutrient Deliver')
climate_control   = Transition(label='Climate Control')
co2_adjust        = Transition(label='CO2 Adjust')
humidity_regulate = Transition(label='Humidity Regulate')
temperature_set   = Transition(label='Temperature Set')
pollination_drone = Transition(label='Pollination Drone')
pest_detect       = Transition(label='Pest Detect')
biocontrol_apply  = Transition(label='Biocontrol Apply')
growth_predict    = Transition(label='Growth Predict')
harvest_schedule  = Transition(label='Harvest Schedule')
produce_clean     = Transition(label='Produce Clean')
package_sort      = Transition(label='Package Sort')
waste_recycle     = Transition(label='Waste Recycle')
data_analyze      = Transition(label='Data Analyze')
energy_optimize   = Transition(label='Energy Optimize')

# Micro-climate control as a small partial order (concurrent CO2/Humidity/Temp after Climate Control)
microclimate = StrictPartialOrder(nodes=[
    climate_control,
    co2_adjust,
    humidity_regulate,
    temperature_set
])
microclimate.order.add_edge(climate_control, co2_adjust)
microclimate.order.add_edge(climate_control, humidity_regulate)
microclimate.order.add_edge(climate_control, temperature_set)

# Build the top‐level process partial order
root = StrictPartialOrder(nodes=[
    seed_select,
    germinate_monitor,
    nutrient_mix,
    nutrient_deliver,
    microclimate,
    pollination_drone,
    pest_detect,
    biocontrol_apply,
    growth_predict,
    harvest_schedule,
    produce_clean,
    package_sort,
    waste_recycle,
    data_analyze,
    energy_optimize
])
# Main sequential flow
root.order.add_edge(seed_select, germinate_monitor)
root.order.add_edge(germinate_monitor, nutrient_mix)
root.order.add_edge(nutrient_mix, nutrient_deliver)
root.order.add_edge(nutrient_deliver, microclimate)
root.order.add_edge(microclimate, pollination_drone)
root.order.add_edge(pollination_drone, pest_detect)
root.order.add_edge(pest_detect, biocontrol_apply)
root.order.add_edge(biocontrol_apply, growth_predict)
root.order.add_edge(growth_predict, harvest_schedule)
root.order.add_edge(harvest_schedule, produce_clean)
root.order.add_edge(produce_clean, package_sort)
root.order.add_edge(package_sort, waste_recycle)

# Data analytics & energy optimization run throughout (concurrent branch)
root.order.add_edge(seed_select, data_analyze)
root.order.add_edge(data_analyze, energy_optimize)