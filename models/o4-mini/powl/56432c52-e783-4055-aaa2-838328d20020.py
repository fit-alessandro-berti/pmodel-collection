# Generated from: 56432c52-e783-4055-aaa2-838328d20020.json
# Description: This process involves sourcing rare milk varieties from remote farms, conducting quality certification through microbiological testing, and aging cheese in controlled cave environments. Packaging requires custom humidity-controlled containers before coordinating multi-modal transport logistics including refrigerated sea freight. Customs clearance demands specialized documentation due to dairy export restrictions. The final step includes retailer training on product handling and shelf-life optimization to ensure premium quality upon delivery.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
batch_blending = Transition(label='Batch Blending')
culture_inoculation = Transition(label='Culture Inoculation')
cave_aging = Transition(label='Cave Aging')
packaging_prep = Transition(label='Packaging Prep')
humidity_control = Transition(label='Humidity Control')
container_sealing = Transition(label='Container Sealing')
logistics_planning = Transition(label='Logistics Planning')
freight_booking = Transition(label='Freight Booking')
documentation = Transition(label='Documentation')
customs_filing = Transition(label='Customs Filing')
retailer_training = Transition(label='Retailer Training')
shelf_life_audit = Transition(label='Shelf-Life Audit')
customer_feedback = Transition(label='Customer Feedback')
skip = SilentTransition()

# Optional feedback at the end
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    batch_blending,
    culture_inoculation,
    cave_aging,
    packaging_prep,
    humidity_control,
    container_sealing,
    logistics_planning,
    freight_booking,
    documentation,
    customs_filing,
    retailer_training,
    shelf_life_audit,
    xor_feedback
])

# Define the control-flow ordering
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, batch_blending)
root.order.add_edge(batch_blending, culture_inoculation)
root.order.add_edge(culture_inoculation, cave_aging)
root.order.add_edge(cave_aging, packaging_prep)
root.order.add_edge(packaging_prep, humidity_control)
root.order.add_edge(humidity_control, container_sealing)
root.order.add_edge(container_sealing, logistics_planning)
root.order.add_edge(logistics_planning, freight_booking)
root.order.add_edge(freight_booking, documentation)
root.order.add_edge(documentation, customs_filing)
root.order.add_edge(customs_filing, retailer_training)
root.order.add_edge(retailer_training, shelf_life_audit)
root.order.add_edge(shelf_life_audit, xor_feedback)