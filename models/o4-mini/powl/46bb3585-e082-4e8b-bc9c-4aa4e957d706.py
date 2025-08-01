# Generated from: 46bb3585-e082-4e8b-bc9c-4aa4e957d706.json
# Description: This process involves the complex coordination of sourcing rare milk varieties, managing fermentation under strict environmental controls, aging cheeses to develop unique flavors, and ensuring traceability throughout the supply chain. It integrates artisanal craftsmanship with modern quality assurance, logistics planning for fragile goods, and niche market distribution strategies. Each step requires specialized knowledge, regulatory compliance, and rigorous testing to maintain product integrity and customer trust while adapting to seasonal variations in milk quality and production capacity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing    = Transition(label='Milk Sourcing')
quality_testing  = Transition(label='Quality Testing')
milk_pasteurize  = Transition(label='Milk Pasteurize')
culture_addition = Transition(label='Culture Addition')
curd_cutting     = Transition(label='Curd Cutting')
whey_draining    = Transition(label='Whey Draining')
pressing_curd    = Transition(label='Pressing Curd')
salting_cheese   = Transition(label='Salting Cheese')
aging_control    = Transition(label='Aging Control')
flavor_sampling  = Transition(label='Flavor Sampling')
packaging_prep   = Transition(label='Packaging Prep')
cold_storage     = Transition(label='Cold Storage')
traceability_log = Transition(label='Traceability Log')
order_processing = Transition(label='Order Processing')
niche_shipping   = Transition(label='Niche Shipping')
customer_feedback= Transition(label='Customer Feedback')

# Loop for the aging and sampling cycle
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, flavor_sampling])

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, milk_pasteurize, culture_addition,
    curd_cutting, whey_draining, pressing_curd, salting_cheese,
    aging_loop, packaging_prep, cold_storage, traceability_log,
    order_processing, niche_shipping, customer_feedback
])

# Define the sequence of the main process
root.order.add_edge(milk_sourcing,  quality_testing)
root.order.add_edge(quality_testing,  milk_pasteurize)
root.order.add_edge(milk_pasteurize,  culture_addition)
root.order.add_edge(culture_addition, curd_cutting)
root.order.add_edge(curd_cutting,    whey_draining)
root.order.add_edge(whey_draining,   pressing_curd)
root.order.add_edge(pressing_curd,   salting_cheese)
root.order.add_edge(salting_cheese,  aging_loop)
root.order.add_edge(aging_loop,      packaging_prep)

# Packaging leads to two concurrent tasks: cold storage and traceability
root.order.add_edge(packaging_prep,  cold_storage)
root.order.add_edge(packaging_prep,  traceability_log)

# Both storage and logging must complete before order processing
root.order.add_edge(cold_storage,     order_processing)
root.order.add_edge(traceability_log, order_processing)

# Final distribution and feedback
root.order.add_edge(order_processing, niche_shipping)
root.order.add_edge(niche_shipping,   customer_feedback)