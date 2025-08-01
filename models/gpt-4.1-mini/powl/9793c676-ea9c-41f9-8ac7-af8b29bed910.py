# Generated from: 9793c676-ea9c-41f9-8ac7-af8b29bed910.json
# Description: This process details the intricate supply chain of artisan coffee, starting from rare coffee bean sourcing in remote microclimates, followed by meticulous quality sampling and fermentation monitoring. The beans undergo custom roasting based on regional flavor profiles, then are packaged using eco-friendly materials. The distribution includes direct-to-café logistics with real-time freshness tracking. Additionally, customer feedback is integrated into future harvest selections to maintain superior taste consistency. The process also involves seasonal collaboration with local farmers for sustainable farming education and crop diversification, ensuring long-term ecosystem health and premium product quality.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Bean_Sourcing = Transition(label='Bean Sourcing')
Quality_Sampling = Transition(label='Quality Sampling')
Fermentation_Check = Transition(label='Fermentation Check')
Custom_Roasting = Transition(label='Custom Roasting')
Flavor_Profiling = Transition(label='Flavor Profiling')
Eco_Packaging = Transition(label='Eco Packaging')
Freshness_Track = Transition(label='Freshness Track')
Direct_Shipping = Transition(label='Direct Shipping')
Café_Delivery = Transition(label='Café Delivery')
Customer_Survey = Transition(label='Customer Survey')
Data_Analysis = Transition(label='Data Analysis')
Harvest_Planning = Transition(label='Harvest Planning')
Farmer_Training = Transition(label='Farmer Training')
Crop_Diversify = Transition(label='Crop Diversify')
Sustainability_Audit = Transition(label='Sustainability Audit')
Feedback_Loop = Transition(label='Feedback Loop')

# Process structure interpretation:

# 1) Bean Sourcing --> Quality Sampling --> Fermentation Check
supply_chain_PO = StrictPartialOrder(nodes=[Bean_Sourcing, Quality_Sampling, Fermentation_Check])
supply_chain_PO.order.add_edge(Bean_Sourcing, Quality_Sampling)
supply_chain_PO.order.add_edge(Quality_Sampling, Fermentation_Check)

# 2) Custom Roasting and Flavor Profiling are sequential after Fermentation Check
roast_profile_PO = StrictPartialOrder(nodes=[Custom_Roasting, Flavor_Profiling])
roast_profile_PO.order.add_edge(Custom_Roasting, Flavor_Profiling)

# 3) Eco Packaging follows flavor profiling
# 4) Distribution: Freshness Track --> Direct Shipping --> Café Delivery
distribution_PO = StrictPartialOrder(nodes=[Freshness_Track, Direct_Shipping, Café_Delivery])
distribution_PO.order.add_edge(Freshness_Track, Direct_Shipping)
distribution_PO.order.add_edge(Direct_Shipping, Café_Delivery)

# 5) Customer Survey --> Data Analysis --> Harvest Planning
# Harvest Planning leads into Feedback Loop
feedback_PO = StrictPartialOrder(nodes=[Customer_Survey, Data_Analysis, Harvest_Planning, Feedback_Loop])
feedback_PO.order.add_edge(Customer_Survey, Data_Analysis)
feedback_PO.order.add_edge(Data_Analysis, Harvest_Planning)
feedback_PO.order.add_edge(Harvest_Planning, Feedback_Loop)

# 6) Seasonal collaboration with local farmers:
# Farmer Training --> Crop Diversify --> Sustainability Audit (these 3 sequential)
farmers_PO = StrictPartialOrder(nodes=[Farmer_Training, Crop_Diversify, Sustainability_Audit])
farmers_PO.order.add_edge(Farmer_Training, Crop_Diversify)
farmers_PO.order.add_edge(Crop_Diversify, Sustainability_Audit)

# Feedback loop influences Harvest Planning and probably Bean Sourcing (for future harvests),
# but to keep partial order simple, we connect Feedback_Loop back conceptually out of PO

# Compose the entire process partial order:
# Sequence:
# supply_chain_PO --> roast_profile_PO --> Eco Packaging --> distribution_PO
# In parallel: feedback_PO and farmers_PO occur alongside or after distribution_PO
# We'll use partial order with edges to respect these relations.

# First, create node for Eco Packaging (as it's single and in-between)
# We'll create an intermediate PO for the middle steps

middle_PO = StrictPartialOrder(nodes=[supply_chain_PO, roast_profile_PO, Eco_Packaging])
middle_PO.order.add_edge(supply_chain_PO, roast_profile_PO)
middle_PO.order.add_edge(roast_profile_PO, Eco_Packaging)

# Then distribution after Eco Packaging
middle_dist_PO = StrictPartialOrder(nodes=[middle_PO, distribution_PO])
middle_dist_PO.order.add_edge(middle_PO, distribution_PO)

# Feedback loop and farmers_PO are separate branches starting after distribution_PO
root = StrictPartialOrder(
    nodes=[middle_dist_PO, feedback_PO, farmers_PO]
)
root.order.add_edge(middle_dist_PO, feedback_PO)
root.order.add_edge(middle_dist_PO, farmers_PO)