# Generated from: c4171bc6-df59-4b81-bb6b-498a97ae24bb.json
# Description: This process outlines the complex steps involved in producing and delivering artisanal cheese from local farms to niche gourmet retailers. It starts with milk sourcing from specialized livestock, followed by quality testing, traditional curdling, and aging under controlled environments. The process includes periodic sensory evaluations, packaging with sustainable materials, coordinating cold-chain logistics, and managing limited batch releases. Additionally, it involves tracking provenance for authenticity, handling customer feedback for continuous improvement, and adapting production schedules based on seasonal milk variations and demand forecasting to maintain product excellence and exclusivity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities as transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
press_cheese = Transition(label='Press Cheese')
salt_application = Transition(label='Salt Application')
controlled_aging = Transition(label='Controlled Aging')
sensory_check = Transition(label='Sensory Check')
batch_packaging = Transition(label='Batch Packaging')
label_printing = Transition(label='Label Printing')
cold_storage = Transition(label='Cold Storage')
logistics_plan = Transition(label='Logistics Plan')
retail_delivery = Transition(label='Retail Delivery')
feedback_review = Transition(label='Feedback Review')
demand_forecast = Transition(label='Demand Forecast')
provenance_track = Transition(label='Provenance Track')

# Loop for adapting production schedules based on seasonal milk variations and demand forecasting
# This loop models: execute demand_forecast, then choose to exit or execute milk_sourcing then again demand_forecast
adapt_production_loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, milk_sourcing])

# Partial order for production steps after milk sourcing (excluding milk sourcing because it's in the loop)
# Milk Pasteurize -> Curd Formation -> Whey Separation -> Press Cheese -> Salt Application -> Controlled Aging
# Controlled Aging -> Sensory Check (periodic, can happen multiple times, but we will treat as after aging)
production_flow = StrictPartialOrder(nodes=[
    milk_pasteurize, curd_formation, whey_separation, press_cheese, 
    salt_application, controlled_aging, sensory_check
])
production_flow.order.add_edge(milk_pasteurize, curd_formation)
production_flow.order.add_edge(curd_formation, whey_separation)
production_flow.order.add_edge(whey_separation, press_cheese)
production_flow.order.add_edge(press_cheese, salt_application)
production_flow.order.add_edge(salt_application, controlled_aging)
production_flow.order.add_edge(controlled_aging, sensory_check)

# Packaging partial order: batch_packaging -> label_printing
packaging = StrictPartialOrder(nodes=[batch_packaging, label_printing])
packaging.order.add_edge(batch_packaging, label_printing)

# Logistics partial order: cold_storage -> logistics_plan -> retail_delivery
logistics = StrictPartialOrder(nodes=[cold_storage, logistics_plan, retail_delivery])
logistics.order.add_edge(cold_storage, logistics_plan)
logistics.order.add_edge(logistics_plan, retail_delivery)

# Partial order for provenance tracking and feedback review (can run concurrently after retail delivery)
post_delivery = StrictPartialOrder(nodes=[provenance_track, feedback_review])
# No order edges - they can happen concurrently

# Compose packaging, logistics, post_delivery all concurrent
pack_log_post = StrictPartialOrder(nodes=[packaging, logistics, post_delivery])

# Define the big partial order connecting all together:
# Adapt production loop precedes (quality_testing and production_flow and then packaging/logistics/post_delivery)
# quality_testing after milk sourcing (inside loop), production_flow after quality_testing
# packaging/logistics/post_delivery after sensory_check

root = StrictPartialOrder(
    nodes=[adapt_production_loop, quality_testing, production_flow, packaging, logistics, post_delivery]
)

# Add order edges accordingly
root.order.add_edge(adapt_production_loop, quality_testing)
root.order.add_edge(quality_testing, production_flow)
root.order.add_edge(production_flow, packaging)
root.order.add_edge(production_flow, logistics)
root.order.add_edge(production_flow, post_delivery)

# Because packaging, logistics and post_delivery are independent concurrent branches started after production_flow,
# no edges among packaging, logistics, post_delivery in root (they are partial orders themselves)

# Note: 'packaging', 'logistics', and 'post_delivery' are StrictPartialOrder objects with their own nodes
# This composition assumes that these can be nodes inside root (nested POWL nodes).
