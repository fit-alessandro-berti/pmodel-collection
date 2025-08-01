# Generated from: ebff34d5-e38a-4e94-8130-f6820132347f.json
# Description: This process details the unique supply chain of artisanal cheese production, starting from milk sourcing at micro-dairies, through specialized fermentation and aging techniques, to boutique packaging and direct delivery to niche markets. It involves quality checks at multiple stages, seasonal adjustments based on milk composition, and collaboration with local farmers and artisans to maintain traditional methods while ensuring compliance with food safety standards. The process culminates in personalized customer engagement and feedback integration to refine future batches and expand product varieties sustainably.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Culture = Transition(label='Starter Culture')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salting_Stage = Transition(label='Salting Stage')
Fermentation = Transition(label='Fermentation')
Aging_Control = Transition(label='Aging Control')
Flavor_Tasting = Transition(label='Flavor Tasting')
Packaging_Artisanal = Transition(label='Packaging Artisanal')
Label_Printing = Transition(label='Label Printing')
Order_Processing = Transition(label='Order Processing')
Direct_Delivery = Transition(label='Direct Delivery')
Customer_Feedback = Transition(label='Customer Feedback')

skip = SilentTransition()

# Seasonal adjustments based on milk composition -> modeled as a loop with Starter Culture and Milk Pasteurize repeated
seasonal_adjustments_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Milk_Pasteurize, Starter_Culture]  # Milk Pasteurize first, then optionally repeat Starter Culture then Milk Pasteurize
)

# Collaboration with local farmers and artisans, simultaneous with Quality Testing is partial order (concurrent)
collab = StrictPartialOrder(nodes=[Quality_Testing, seasonal_adjustments_loop])
# No order edges between Quality Testing and seasonal adjustment loop to allow concurrency

# Core cheese making partial order
core_cheese = StrictPartialOrder(nodes=[
    Curd_Cutting, Whey_Draining, Pressing_Cheese,
    Salting_Stage, Fermentation, Aging_Control, Flavor_Tasting
])

# Define order edges for core cheese production steps
core_cheese.order.add_edge(Curd_Cutting, Whey_Draining)
core_cheese.order.add_edge(Whey_Draining, Pressing_Cheese)
core_cheese.order.add_edge(Pressing_Cheese, Salting_Stage)
core_cheese.order.add_edge(Salting_Stage, Fermentation)
core_cheese.order.add_edge(Fermentation, Aging_Control)
core_cheese.order.add_edge(Aging_Control, Flavor_Tasting)

# Packaging phase partial order
packaging = StrictPartialOrder(nodes=[Packaging_Artisanal, Label_Printing])
# Packaging and label printing could be concurrent
# But typically label printing after packaging or vice versa?
# Let's assume Label Printing after Packaging
packaging.order.add_edge(Packaging_Artisanal, Label_Printing)

# Final delivery partial order
delivery = StrictPartialOrder(nodes=[Order_Processing, Direct_Delivery])
delivery.order.add_edge(Order_Processing, Direct_Delivery)

# Final feedback activity after delivery
final_phase = StrictPartialOrder(nodes=[delivery, Customer_Feedback])
final_phase.order.add_edge(delivery, Customer_Feedback)

# Build the overall partial order with all main phases

root = StrictPartialOrder(
    nodes=[
        Milk_Sourcing,
        collab,
        core_cheese,
        packaging,
        final_phase
    ]
)

# Define control flow edges reflecting the process flow:
# Milk Sourcing -> collab (Quality Testing and Seasonal Adjustment loop)
root.order.add_edge(Milk_Sourcing, collab)

# collab -> core cheese making
root.order.add_edge(collab, core_cheese)

# core cheese -> packaging
root.order.add_edge(core_cheese, packaging)

# packaging -> delivery and feedback
root.order.add_edge(packaging, final_phase)