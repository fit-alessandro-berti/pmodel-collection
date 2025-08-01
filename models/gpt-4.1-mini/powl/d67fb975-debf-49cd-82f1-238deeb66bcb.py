# Generated from: d67fb975-debf-49cd-82f1-238deeb66bcb.json
# Description: This process outlines the adaptive urban farming cycle designed to optimize crop yield in limited city spaces by integrating environmental data, community feedback, and resource availability. It begins with site analysis, followed by soil enhancement and precision planting. Sensor arrays continuously monitor microclimate and soil conditions, allowing dynamic irrigation and nutrient delivery adjustments. Community workshops gather experiential insights which feed into iterative crop selection and pest management strategies. Harvesting is coordinated with local distribution networks to minimize waste. Post-harvest, composting converts organic waste into soil amendments, completing the sustainability loop. Throughout, data analytics refine practices seasonally to adapt to urban environmental fluctuations and community needs, ensuring resilient and productive green spaces within dense urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Analyze = Transition(label='Site Analyze')
Soil_Enhance = Transition(label='Soil Enhance')
Seed_Select = Transition(label='Seed Select')
Plant_Precise = Transition(label='Plant Precise')
Sensor_Deploy = Transition(label='Sensor Deploy')
Climate_Monitor = Transition(label='Climate Monitor')
Irrigate_Adjust = Transition(label='Irrigate Adjust')
Nutrient_Feed = Transition(label='Nutrient Feed')
Pest_Control = Transition(label='Pest Control')
Community_Engage = Transition(label='Community Engage')
Feedback_Collect = Transition(label='Feedback Collect')
Yield_Harvest = Transition(label='Yield Harvest')
Waste_Sort = Transition(label='Waste Sort')
Compost_Create = Transition(label='Compost Create')
Data_Analyze = Transition(label='Data Analyze')
Network_Distribute = Transition(label='Network Distribute')

# Sensor continuous monitoring subprocess (Sensor_Deploy then Climate_Monitor runs concurrently with Irrigate_Adjust and Nutrient_Feed)
sensor_monitoring_PO = StrictPartialOrder(
    nodes=[Sensor_Deploy, Climate_Monitor, Irrigate_Adjust, Nutrient_Feed]
)
sensor_monitoring_PO.order.add_edge(Sensor_Deploy, Climate_Monitor)
sensor_monitoring_PO.order.add_edge(Sensor_Deploy, Irrigate_Adjust)
sensor_monitoring_PO.order.add_edge(Sensor_Deploy, Nutrient_Feed)
# Climate Monitor, Irrigate Adjust, Nutrient Feed run concurrently after Sensor Deploy

# Community feedback subprocess (Community_Engage then Feedback_Collect)
community_feedback_PO = StrictPartialOrder(
    nodes=[Community_Engage, Feedback_Collect]
)
community_feedback_PO.order.add_edge(Community_Engage, Feedback_Collect)

# Crop selection and pest management loop:
# Loop with:
# A = Seed_Select then Plant_Precise
# B = Pest_Control then community feedback (Feedback Collect used as input)
A_crops = StrictPartialOrder(
    nodes=[Seed_Select, Plant_Precise]
)
A_crops.order.add_edge(Seed_Select, Plant_Precise)

# B body of the loop: Pest_Control then community feedback PO (Community_Engage & Feedback_Collect)
# Represent feedback as community_feedback_PO
B_loop = StrictPartialOrder(nodes=[Pest_Control, community_feedback_PO])
B_loop.order.add_edge(Pest_Control, community_feedback_PO)

crop_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[A_crops, B_loop])

# Harvest and distribution subprocess (Yield_Harvest then parallel Waste_Sort and Network_Distribute)
harvest_PO = StrictPartialOrder(
    nodes=[Yield_Harvest, Waste_Sort, Network_Distribute]
)
harvest_PO.order.add_edge(Yield_Harvest, Waste_Sort)
harvest_PO.order.add_edge(Yield_Harvest, Network_Distribute)
# Waste_Sort and Network_Distribute run concurrently after Yield_Harvest

# Composting follows Waste Sort
compost_PO = StrictPartialOrder(
    nodes=[Waste_Sort, Compost_Create]
)
compost_PO.order.add_edge(Waste_Sort, Compost_Create)

# Data Analyze after harvest and compost
post_harvest_PO = StrictPartialOrder(
    nodes=[harvest_PO, compost_PO, Data_Analyze]
)
# Harvest_PO and Compost_PO are partial orders, treat them as nodes in this POWL
post_harvest_PO.order.add_edge(harvest_PO, Data_Analyze)
post_harvest_PO.order.add_edge(compost_PO, Data_Analyze)

# Overall flow:
# Site Analyze --> Soil Enhance --> crop_selection_loop with planting and feedback
# Then Sensor monitoring runs concurrently with Data Analyze (seasonal refinement)
# But Data Analyze should be after crop management and composting (done above)
# So sensor monitoring can be before or during crop growth, but we can put it after Soil Enhance and before crop loop for modeling

# Define the top-level PO with ordering:
# Site Analyze --> Soil Enhance --> Sensor monitoring and crop_selection_loop concur
# After crop_selection_loop completes, do harvest_PO, compost_PO, and Data Analyze

top_PO_nodes = [Site_Analyze, Soil_Enhance, sensor_monitoring_PO, crop_selection_loop, post_harvest_PO]
root = StrictPartialOrder(nodes=top_PO_nodes)
root.order.add_edge(Site_Analyze, Soil_Enhance)
root.order.add_edge(Soil_Enhance, sensor_monitoring_PO)
root.order.add_edge(Soil_Enhance, crop_selection_loop)
root.order.add_edge(sensor_monitoring_PO, post_harvest_PO)
root.order.add_edge(crop_selection_loop, post_harvest_PO)