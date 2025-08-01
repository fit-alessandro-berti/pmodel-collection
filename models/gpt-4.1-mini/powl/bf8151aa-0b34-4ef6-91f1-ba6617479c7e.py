# Generated from: bf8151aa-0b34-4ef6-91f1-ba6617479c7e.json
# Description: This process governs the entire operational cycle of an urban vertical farm that integrates hydroponic and aeroponic systems within a multi-story building. It begins with seed selection optimized for limited space and light conditions, followed by germination monitoring using AI sensors. Nutrient mixing and delivery are dynamically adjusted based on real-time plant health data. Concurrently, microclimate controls regulate humidity, temperature, and CO2 levels floor-by-floor. Pollination is artificially induced via robotic drones, while pest detection employs machine vision and targeted biocontrol agents. Harvesting is scheduled by growth stage prediction models, ensuring peak freshness. Post-harvest, produce undergoes automated cleaning, packaging, and quality sorting before distribution. Waste biomass is recycled onsite into compost or bioenergy. Throughout the cycle, data analytics optimize energy usage and yield forecasts, supporting continuous improvements in urban agriculture sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
Seed_Select = Transition(label='Seed Select')
Germinate_Monitor = Transition(label='Germinate Monitor')

Nutrient_Mix = Transition(label='Nutrient Mix')
Nutrient_Deliver = Transition(label='Nutrient Deliver')

Climate_Control = Transition(label='Climate Control')
CO2_Adjust = Transition(label='CO2 Adjust')
Humidity_Regulate = Transition(label='Humidity Regulate')
Temperature_Set = Transition(label='Temperature Set')

Pollination_Drone = Transition(label='Pollination Drone')

Pest_Detect = Transition(label='Pest Detect')
Biocontrol_Apply = Transition(label='Biocontrol Apply')

Growth_Predict = Transition(label='Growth Predict')
Harvest_Schedule = Transition(label='Harvest Schedule')

Produce_Clean = Transition(label='Produce Clean')
Package_Sort = Transition(label='Package Sort')

Waste_Recycle = Transition(label='Waste Recycle')

Data_Analyze = Transition(label='Data Analyze')
Energy_Optimize = Transition(label='Energy Optimize')

# Partial order for nutrient delivery (Nutrient Mix -> Nutrient Deliver)
nutrient_PO = StrictPartialOrder(nodes=[Nutrient_Mix, Nutrient_Deliver])
nutrient_PO.order.add_edge(Nutrient_Mix, Nutrient_Deliver)

# Partial order for climate controls (CO2 Adjust, Humidity Regulate, Temperature Set) in parallel before Climate Control
# The text says "microclimate controls regulate humidity, temperature, and CO2 ... floor-by-floor" concurrently: assume these 3 concurrent and then must finish before Climate_Control
climate_controls_concurrent = StrictPartialOrder(
    nodes=[CO2_Adjust, Humidity_Regulate, Temperature_Set]
)
# Then these precede Climate_Control
climate_PO = StrictPartialOrder(
    nodes=[climate_controls_concurrent, Climate_Control]
)
climate_PO.order.add_edge(climate_controls_concurrent, Climate_Control)

# Partial order for pest detection and biocontrol apply (Pest Detect -> Biocontrol Apply)
pest_PO = StrictPartialOrder(nodes=[Pest_Detect, Biocontrol_Apply])
pest_PO.order.add_edge(Pest_Detect, Biocontrol_Apply)

# Partial order for produce cleaning and packaging (Produce Clean -> Package Sort)
produce_PO = StrictPartialOrder(nodes=[Produce_Clean, Package_Sort])
produce_PO.order.add_edge(Produce_Clean, Package_Sort)

# Partial order for data analytics and energy optimization in parallel
data_energy_PO = StrictPartialOrder(nodes=[Data_Analyze, Energy_Optimize])

# Now build main partial order

# Define nodes of the main PO:

# Sequential start: Seed Select -> Germinate Monitor
start_PO = StrictPartialOrder(nodes=[Seed_Select, Germinate_Monitor])
start_PO.order.add_edge(Seed_Select, Germinate_Monitor)

# After Germinate Monitor, Nutrient Mix and climate controls happen concurrently:
# Nutrient partial order, climate partial order and Pollination and pest partial orders, growth prediction and harvest scheduling, produce handling, waste recycle and data analytics run later
# Pollination Drone and Nutrient/deliver and climate controls + pest detection run concurrently after Germinate Monitor

# Concurrent nodes after Germinate Monitor:
concurrent_after_germinate = [nutrient_PO, climate_PO, Pollination_Drone, pest_PO]

# After these concurrent activities are done, proceed to growth prediction and harvest schedule (Growth Predict -> Harvest Schedule)
growth_PO = StrictPartialOrder(nodes=[Growth_Predict, Harvest_Schedule])
growth_PO.order.add_edge(Growth_Predict, Harvest_Schedule)

# After harvesting, produce clean/sort then waste recycle
produce_and_waste_PO = StrictPartialOrder(nodes=[produce_PO, Waste_Recycle])
# produce_PO and Waste_Recycle concurrent (no order between them)

# Finally data analysis and energy optimize run concurrent, assumed at the end
final_PO = data_energy_PO

# Build upper level PO with nodes:
# start_PO -> concurrent_after_germinate -> growth_PO -> produce_and_waste_PO -> final_PO
# But start_PO and others are themselves StrictPartialOrder or Transition objects

nodes = [
    start_PO,
    StrictPartialOrder(nodes=concurrent_after_germinate),
    growth_PO,
    produce_and_waste_PO,
    final_PO
]

root = StrictPartialOrder(nodes=nodes)

root.order.add_edge(start_PO, nodes[1])  # start_PO -> concurrent_after_germinate
root.order.add_edge(nodes[1], growth_PO)  # concurrent_after_germinate -> growth_PO
root.order.add_edge(growth_PO, produce_and_waste_PO)  # growth_PO -> produce_and_waste_PO
root.order.add_edge(produce_and_waste_PO, final_PO)  # produce_and_waste_PO -> final_PO