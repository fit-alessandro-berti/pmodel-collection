# Generated from: 46bb3585-e082-4e8b-bc9c-4aa4e957d706.json
# Description: This process involves the complex coordination of sourcing rare milk varieties, managing fermentation under strict environmental controls, aging cheeses to develop unique flavors, and ensuring traceability throughout the supply chain. It integrates artisanal craftsmanship with modern quality assurance, logistics planning for fragile goods, and niche market distribution strategies. Each step requires specialized knowledge, regulatory compliance, and rigorous testing to maintain product integrity and customer trust while adapting to seasonal variations in milk quality and production capacity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Culture_Addition = Transition(label='Culture Addition')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Pressing_Curd = Transition(label='Pressing Curd')
Salting_Cheese = Transition(label='Salting Cheese')
Aging_Control = Transition(label='Aging Control')
Flavor_Sampling = Transition(label='Flavor Sampling')
Packaging_Prep = Transition(label='Packaging Prep')
Traceability_Log = Transition(label='Traceability Log')
Cold_Storage = Transition(label='Cold Storage')
Order_Processing = Transition(label='Order Processing')
Niche_Shipping = Transition(label='Niche Shipping')
Customer_Feedback = Transition(label='Customer Feedback')

# Model phases:

# Phase 1: Milk sourcing and quality
po_phase1 = StrictPartialOrder(
    nodes=[Milk_Sourcing, Quality_Testing, Traceability_Log]
)
po_phase1.order.add_edge(Milk_Sourcing, Quality_Testing)
po_phase1.order.add_edge(Quality_Testing, Traceability_Log)

# Phase 2: Milk treatment and fermentation preparation
po_phase2 = StrictPartialOrder(
    nodes=[Milk_Pasteurize, Culture_Addition]
)
po_phase2.order.add_edge(Milk_Pasteurize, Culture_Addition)

# Phase 3: Cheese formation steps (Curd Cutting, Whey Draining, Pressing Curd, Salting Cheese)
po_cheese_formation = StrictPartialOrder(
    nodes=[Curd_Cutting, Whey_Draining, Pressing_Curd, Salting_Cheese]
)
po_cheese_formation.order.add_edge(Curd_Cutting, Whey_Draining)
po_cheese_formation.order.add_edge(Whey_Draining, Pressing_Curd)
po_cheese_formation.order.add_edge(Pressing_Curd, Salting_Cheese)

# Phase 4: Aging and flavor sampling (Flavor Sampling concurrent with Aging Control)
po_aging = StrictPartialOrder(
    nodes=[Aging_Control, Flavor_Sampling]
)
# these are concurrent (no order edges)

# Phase 5: Packaging prep and cold storage (concurrent)
po_packaging_storage = StrictPartialOrder(
    nodes=[Packaging_Prep, Cold_Storage]
)
# concurrent (no order edges)

# Phase 6: Order processing and niche shipping sequential
po_distribution = StrictPartialOrder(
    nodes=[Order_Processing, Niche_Shipping]
)
po_distribution.order.add_edge(Order_Processing, Niche_Shipping)

# Customer feedback after shipping
po_feedback = StrictPartialOrder(
    nodes=[Customer_Feedback]
)

# Assemble main partial order of phases with order edges:
# Phase 1 --> Phase 2 --> Phase 3 --> Phase 4 --> Phase 5 --> Phase 6 --> Feedback

root_nodes = [
    po_phase1,
    po_phase2,
    po_cheese_formation,
    po_aging,
    po_packaging_storage,
    po_distribution,
    po_feedback
]

root = StrictPartialOrder(nodes=root_nodes)

# Add order between phases
root.order.add_edge(po_phase1, po_phase2)
root.order.add_edge(po_phase2, po_cheese_formation)
root.order.add_edge(po_cheese_formation, po_aging)
root.order.add_edge(po_aging, po_packaging_storage)
root.order.add_edge(po_packaging_storage, po_distribution)
root.order.add_edge(po_distribution, po_feedback)