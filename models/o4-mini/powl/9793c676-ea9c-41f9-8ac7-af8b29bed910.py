# Generated from: 9793c676-ea9c-41f9-8ac7-af8b29bed910.json
# Description: This process details the intricate supply chain of artisan coffee, starting from rare coffee bean sourcing in remote microclimates, followed by meticulous quality sampling and fermentation monitoring. The beans undergo custom roasting based on regional flavor profiles, then are packaged using eco-friendly materials. The distribution includes direct-to-café logistics with real-time freshness tracking. Additionally, customer feedback is integrated into future harvest selections to maintain superior taste consistency. The process also involves seasonal collaboration with local farmers for sustainable farming education and crop diversification, ensuring long-term ecosystem health and premium product quality.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.powl.obj import SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
bean_sourcing     = Transition(label='Bean Sourcing')
quality_sampling  = Transition(label='Quality Sampling')
fermentation_check= Transition(label='Fermentation Check')
custom_roasting   = Transition(label='Custom Roasting')
flavor_profiling  = Transition(label='Flavor Profiling')
eco_packaging     = Transition(label='Eco Packaging')
direct_shipping   = Transition(label='Direct Shipping')
freshness_track   = Transition(label='Freshness Track')
cafe_delivery     = Transition(label='Café Delivery')
customer_survey   = Transition(label='Customer Survey')
data_analysis     = Transition(label='Data Analysis')
harvest_planning  = Transition(label='Harvest Planning')
feedback_loop     = Transition(label='Feedback Loop')
farmer_training   = Transition(label='Farmer Training')
crop_diversify    = Transition(label='Crop Diversify')
sustainability_audit = Transition(label='Sustainability Audit')

# Build the seasonal collaboration loop:
#   A = parallel Farmer Training and Crop Diversify
#   B = Sustainability Audit
seasonal_body = StrictPartialOrder(nodes=[farmer_training, crop_diversify])
seasonal_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[seasonal_body, sustainability_audit]
)

# Build the main partial‐order workflow
root = StrictPartialOrder(nodes=[
    bean_sourcing,
    quality_sampling,
    fermentation_check,
    custom_roasting,
    flavor_profiling,
    eco_packaging,
    direct_shipping,
    freshness_track,
    cafe_delivery,
    customer_survey,
    data_analysis,
    harvest_planning,
    feedback_loop,
    seasonal_loop
])

# 1. Bean sourcing → Quality sampling → Fermentation check → Custom roasting → Flavor profiling → Eco packaging
root.order.add_edge(bean_sourcing,      quality_sampling)
root.order.add_edge(quality_sampling,   fermentation_check)
root.order.add_edge(fermentation_check, custom_roasting)
root.order.add_edge(custom_roasting,    flavor_profiling)
root.order.add_edge(flavor_profiling,   eco_packaging)

# 2. After eco packaging, shipping and freshness tracking run in parallel
root.order.add_edge(eco_packaging,  direct_shipping)
root.order.add_edge(eco_packaging,  freshness_track)

# 3. Both shipping and tracking must complete before café delivery
root.order.add_edge(direct_shipping, cafe_delivery)
root.order.add_edge(freshness_track, cafe_delivery)

# 4. After delivery: customer survey → data analysis → harvest planning → feedback loop
root.order.add_edge(cafe_delivery,   customer_survey)
root.order.add_edge(customer_survey, data_analysis)
root.order.add_edge(data_analysis,   harvest_planning)
root.order.add_edge(harvest_planning, feedback_loop)

# 5. After feedback loop, start the seasonal farmer collaboration loop
root.order.add_edge(feedback_loop, seasonal_loop)