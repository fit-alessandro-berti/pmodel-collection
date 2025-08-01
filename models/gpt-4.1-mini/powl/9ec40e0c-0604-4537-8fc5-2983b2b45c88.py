# Generated from: 9ec40e0c-0604-4537-8fc5-2983b2b45c88.json
# Description: This process outlines the intricate lifecycle of producing artisanal cheese, starting from sourcing rare local milk, through precise fermentation and aging stages, to quality evaluation and bespoke packaging. Each step requires specialized craftsmanship and environmental monitoring to ensure distinctive flavor profiles. The process incorporates traditional methods alongside modern quality controls, involving seasonal adjustments and customer feedback loops to maintain authenticity and excellence across batches, culminating in distribution to niche markets and exclusive retailers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Culture = Transition(label='Starter Culture')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Cutting_Curd = Transition(label='Cutting Curd')
Whey_Drain = Transition(label='Whey Drain')
Molding_Cheese = Transition(label='Molding Cheese')
Pressing_Blocks = Transition(label='Pressing Blocks')
Salting_Surface = Transition(label='Salting Surface')
Aging_Control = Transition(label='Aging Control')
Flavor_Sampling = Transition(label='Flavor Sampling')
Rind_Treatment = Transition(label='Rind Treatment')
Packaging_Design = Transition(label='Packaging Design')
Market_Distribution = Transition(label='Market Distribution')
Customer_Feedback = Transition(label='Customer Feedback')

# Model the initial sourcing and testing partial order with starter culture prep:
# Milk Sourcing --> Quality Testing --> Starter Culture
po_initial = StrictPartialOrder(
    nodes=[Milk_Sourcing, Quality_Testing, Starter_Culture]
)
po_initial.order.add_edge(Milk_Sourcing, Quality_Testing)
po_initial.order.add_edge(Quality_Testing, Starter_Culture)

# Pasteurize milk after starter culture:
po_pasteurize = StrictPartialOrder(
    nodes=[po_initial, Milk_Pasteurize]
)
po_pasteurize.order.add_edge(po_initial, Milk_Pasteurize)

# Cheese making steps partial order:
# Curd Formation --> Cutting Curd --> Whey Drain --> Molding Cheese --> Pressing Blocks --> Salting Surface
po_cheesemaking = StrictPartialOrder(
    nodes=[
        Curd_Formation,
        Cutting_Curd,
        Whey_Drain,
        Molding_Cheese,
        Pressing_Blocks,
        Salting_Surface
    ]
)
po_cheesemaking.order.add_edge(Curd_Formation, Cutting_Curd)
po_cheesemaking.order.add_edge(Cutting_Curd, Whey_Drain)
po_cheesemaking.order.add_edge(Whey_Drain, Molding_Cheese)
po_cheesemaking.order.add_edge(Molding_Cheese, Pressing_Blocks)
po_cheesemaking.order.add_edge(Pressing_Blocks, Salting_Surface)

# Aging and quality partial order with seasonal feedback loop:
# Aging Control --> Flavor Sampling --> Rind Treatment --> (loop back through customer feedback)
# Loop structure: (Flavor Sampling, Customer Feedback)
loop_feedback = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Flavor_Sampling,
        Customer_Feedback
    ]
)

po_aging_quality = StrictPartialOrder(
    nodes=[Aging_Control, Rind_Treatment, loop_feedback]
)
po_aging_quality.order.add_edge(Aging_Control, loop_feedback)
po_aging_quality.order.add_edge(loop_feedback, Rind_Treatment)

# Packaging and distribution partial order:
po_packaging_distribution = StrictPartialOrder(
    nodes=[Packaging_Design, Market_Distribution]
)
po_packaging_distribution.order.add_edge(Packaging_Design, Market_Distribution)

# Combine the process chain with partial orders and their intrinsic orderings

root = StrictPartialOrder(
    nodes=[
        po_pasteurize,
        po_cheesemaking,
        po_aging_quality,
        po_packaging_distribution
    ]
)

# Define high-level order:
# Milk pasteurize precedes cheese making (milk needed)
root.order.add_edge(po_pasteurize, po_cheesemaking)
# Cheese making precedes aging and quality control
root.order.add_edge(po_cheesemaking, po_aging_quality)
# Aging and quality control precedes packaging and distribution
root.order.add_edge(po_aging_quality, po_packaging_distribution)