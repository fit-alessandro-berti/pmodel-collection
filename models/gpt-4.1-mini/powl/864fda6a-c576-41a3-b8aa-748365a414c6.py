# Generated from: 864fda6a-c576-41a3-b8aa-748365a414c6.json
# Description: This process encompasses the intricate journey of producing and distributing artisanal cheese, starting from selecting rare milk sources, through precise fermentation and aging techniques, to packaging with bespoke materials, and finally coordinating niche market deliveries. It involves quality validation at multiple points, managing small batch variations, syncing with seasonal farm outputs, and engaging specialized transport to maintain product integrity. The process also integrates customer feedback loops for continuous refinement and limited edition releases, ensuring the cheese retains its unique character and exclusivity throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Culture = Transition(label='Starter Culture')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding_Press = Transition(label='Molding Press')
Salting_Dry = Transition(label='Salting Dry')
Fermentation = Transition(label='Fermentation')
Aging_Control = Transition(label='Aging Control')
Quality_Check = Transition(label='Quality Check')
Packaging_Design = Transition(label='Packaging Design')
Custom_Wrapping = Transition(label='Custom Wrapping')
Inventory_Sync = Transition(label='Inventory Sync')
Order_Processing = Transition(label='Order Processing')
Special_Shipping = Transition(label='Special Shipping')
Customer_Feedback = Transition(label='Customer Feedback')
Batch_Analysis = Transition(label='Batch Analysis')
Limited_Release = Transition(label='Limited Release')

skip = SilentTransition()

# Batch Analysis is a loop with Milk Sourcing (small batch variations and syncing with farm outputs)
batch_loop = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Sourcing, Batch_Analysis])

# Cheese production partial order (after Milk Sourcing and Batch Analysis):
# Starter Culture -> Milk Pasteurize -> Coagulation -> Curd Cutting -> Whey Draining -> Molding Press -> Salting Dry -> Fermentation -> Aging Control
production_nodes = [
    Starter_Culture, Milk_Pasteurize, Coagulation, Curd_Cutting,
    Whey_Draining, Molding_Press, Salting_Dry, Fermentation, Aging_Control
]
production = StrictPartialOrder(nodes=production_nodes)
production.order.add_edge(Starter_Culture, Milk_Pasteurize)
production.order.add_edge(Milk_Pasteurize, Coagulation)
production.order.add_edge(Coagulation, Curd_Cutting)
production.order.add_edge(Curd_Cutting, Whey_Draining)
production.order.add_edge(Whey_Draining, Molding_Press)
production.order.add_edge(Molding_Press, Salting_Dry)
production.order.add_edge(Salting_Dry, Fermentation)
production.order.add_edge(Fermentation, Aging_Control)

# Quality Testing before and Quality Check after production steps:
quality_before = StrictPartialOrder(nodes=[Quality_Testing])
quality_after = StrictPartialOrder(nodes=[Quality_Check])

# Packaging partial order: Packaging Design -> Custom Wrapping -> Inventory Sync
packaging = StrictPartialOrder(nodes=[Packaging_Design, Custom_Wrapping, Inventory_Sync])
packaging.order.add_edge(Packaging_Design, Custom_Wrapping)
packaging.order.add_edge(Custom_Wrapping, Inventory_Sync)

# Ordering and delivery: Order Processing -> Special Shipping
order_delivery = StrictPartialOrder(nodes=[Order_Processing, Special_Shipping])
order_delivery.order.add_edge(Order_Processing, Special_Shipping)

# Customer Feedback loop connected to production for continuous refinement
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Customer_Feedback, production])

# Limited Release choice: either normal process flow or perform Limited Release (exclusive choice)
release_choice = OperatorPOWL(operator=Operator.XOR, children=[order_delivery, Limited_Release])

# Assemble main workflow partial order
# Edges:
# batch_loop --> Quality_Testing --> production --> Quality_Check --> packaging --> release_choice
# Also connect feedback_loop after aging control to allow continuous refinement
root = StrictPartialOrder(nodes=[
    batch_loop, Quality_Testing, production, Quality_Check, packaging, release_choice, feedback_loop
])

root.order.add_edge(batch_loop, Quality_Testing)
root.order.add_edge(Quality_Testing, production)
root.order.add_edge(production, Quality_Check)
root.order.add_edge(Quality_Check, packaging)
root.order.add_edge(packaging, release_choice)

# Connect feedback_loop to production start to represent feedback-driven refinement
# feedback_loop depends on Aging Control finishing, so connect Aging_Control -> feedback_loop
root.order.add_edge(production, feedback_loop)

# For correctness, also allow the feedback loop to re-enter production (loop operator inside feedback_loop covers that)

# Finished root definition