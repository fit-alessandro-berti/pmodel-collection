# Generated from: 1a7c9004-7fa7-47c6-8648-79992abf5bea.json
# Description: This process details the intricate steps involved in sourcing, producing, and distributing artisan cheese with a focus on maintaining quality and authenticity. It begins with selecting rare milk sources, followed by specialized fermentation and aging stages. Quality control includes sensory evaluation and microbial testing to ensure safety and flavor consistency. Packaging is done in eco-friendly materials, with customized labeling reflecting the cheese’s origin. Distribution channels are unique, targeting niche gourmet retailers and direct-to-consumer subscriptions. Throughout the process, traceability and sustainability reporting are integral to meet regulatory and consumer demands, making this supply chain highly specialized and complex.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sourcing = Transition(label='Milk Sourcing')
fermentation_start = Transition(label='Fermentation Start')
curd_cutting = Transition(label='Curd Cutting')
whey_removal = Transition(label='Whey Removal')
molding_cheese = Transition(label='Molding Cheese')
salting_process = Transition(label='Salting Process')
aging_control = Transition(label='Aging Control')
quality_testing = Transition(label='Quality Testing')
sensory_review = Transition(label='Sensory Review')
microbial_check = Transition(label='Microbial Check')
eco_packaging = Transition(label='Eco Packaging')
label_printing = Transition(label='Label Printing')
order_processing = Transition(label='Order Processing')
niche_shipping = Transition(label='Niche Shipping')
sustainability_audit = Transition(label='Sustainability Audit')

# Silent transition to represent the alternative distribution channel (direct-to-consumer)
skip = SilentTransition()

# XOR choice between niche shipping and the alternative (silent) channel
distribution = OperatorPOWL(
    operator=Operator.XOR,
    children=[niche_shipping, skip]
)

# Main workflow partial order
main = StrictPartialOrder(nodes=[
    milk_sourcing,
    fermentation_start,
    curd_cutting,
    whey_removal,
    molding_cheese,
    salting_process,
    aging_control,
    quality_testing,
    sensory_review,
    microbial_check,
    eco_packaging,
    label_printing,
    order_processing,
    distribution
])

# Add ordering constraints for the core cheese production process
main.order.add_edge(milk_sourcing, fermentation_start)
main.order.add_edge(fermentation_start, curd_cutting)
main.order.add_edge(curd_cutting, whey_removal)
main.order.add_edge(whey_removal, molding_cheese)
main.order.add_edge(molding_cheese, salting_process)
main.order.add_edge(salting_process, aging_control)

# Quality testing before the two parallel checks
main.order.add_edge(aging_control, quality_testing)
main.order.add_edge(quality_testing, sensory_review)
main.order.add_edge(quality_testing, microbial_check)

# Both checks must finish before packaging
main.order.add_edge(sensory_review, eco_packaging)
main.order.add_edge(microbial_check, eco_packaging)

# Packaging and labeling
main.order.add_edge(eco_packaging, label_printing)

# Order processing and distribution choice
main.order.add_edge(label_printing, order_processing)
main.order.add_edge(order_processing, distribution)

# Root partial order with sustainability audit in parallel
root = StrictPartialOrder(nodes=[main, sustainability_audit])
# No edges between 'main' and 'sustainability_audit' => they are concurrent