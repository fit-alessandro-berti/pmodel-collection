# Generated from: 2910b74d-5ab6-49d2-b6de-d4599d7ec6a7.json
# Description: This process outlines the intricate steps involved in producing and distributing artisanal cheese from small-scale farms to gourmet retailers. It includes sourcing rare milk varieties, controlled fermentation, manual curdling, delicate aging in microclimates, quality testing, custom packaging, and niche marketing. The process demands precise coordination between farmers, cheesemakers, quality inspectors, and logistics teams to maintain the unique flavor profiles and artisanal qualities. Additionally, it involves seasonal adjustments, compliance with food safety regulations, and direct consumer feedback loops to refine product offerings and maintain exclusivity in a competitive gourmet market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Starter_Culture = Transition(label='Starter Culture')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Cutting_Curd = Transition(label='Cutting Curd')
Whey_Drain = Transition(label='Whey Drain')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Stage = Transition(label='Salting Stage')
Aging_Control = Transition(label='Aging Control')
Humidity_Check = Transition(label='Humidity Check')
Flavor_Sampling = Transition(label='Flavor Sampling')
Quality_Testing = Transition(label='Quality Testing')
Packaging_Prep = Transition(label='Packaging Prep')
Label_Printing = Transition(label='Label Printing')
Order_Fulfill = Transition(label='Order Fulfill')
Retail_Delivery = Transition(label='Retail Delivery')
Customer_Feedback = Transition(label='Customer Feedback')

skip = SilentTransition()

# Loop for seasonal adjustment and feedback refinement:
# LOOP( 
#   Aging_Control -> Humidity_Check -> Flavor_Sampling -> Quality_Testing,
#   Customer_Feedback
# )
aging_loop_body = StrictPartialOrder(
    nodes=[Aging_Control, Humidity_Check, Flavor_Sampling, Quality_Testing],
)
aging_loop_body.order.add_edge(Aging_Control, Humidity_Check)
aging_loop_body.order.add_edge(Humidity_Check, Flavor_Sampling)
aging_loop_body.order.add_edge(Flavor_Sampling, Quality_Testing)

aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_loop_body, Customer_Feedback])

# Packaging and Delivery partial order: Packaging_Prep then Label_Printing then Order_Fulfill then Retail_Delivery
packaging_po = StrictPartialOrder(
    nodes=[Packaging_Prep, Label_Printing, Order_Fulfill, Retail_Delivery]
)
packaging_po.order.add_edge(Packaging_Prep, Label_Printing)
packaging_po.order.add_edge(Label_Printing, Order_Fulfill)
packaging_po.order.add_edge(Order_Fulfill, Retail_Delivery)

# Core cheese production sequence before aging and testing
production_po = StrictPartialOrder(
    nodes=[
        Milk_Sourcing,
        Starter_Culture,
        Milk_Pasteurize,
        Curd_Formation,
        Cutting_Curd,
        Whey_Drain,
        Molding_Cheese,
        Salting_Stage,
    ]
)
production_po.order.add_edge(Milk_Sourcing, Starter_Culture)
production_po.order.add_edge(Starter_Culture, Milk_Pasteurize)
production_po.order.add_edge(Milk_Pasteurize, Curd_Formation)
production_po.order.add_edge(Curd_Formation, Cutting_Curd)
production_po.order.add_edge(Cutting_Curd, Whey_Drain)
production_po.order.add_edge(Whey_Drain, Molding_Cheese)
production_po.order.add_edge(Molding_Cheese, Salting_Stage)

# Combine production and aging/testing loop: Salting_Stage before aging_loop entry point (Aging_Control is first in loop body)
root_po = StrictPartialOrder(
    nodes=[production_po, aging_loop, packaging_po]
)
# Order edges from production to aging loop (the loop's first node is aging_loop_body)
# We connect Salting_Stage --> aging_loop_body (which is the first child in loop)
root_po.order.add_edge(production_po, aging_loop)  # connect production node to loop operator
root_po.order.add_edge(aging_loop, packaging_po)   # after loop, packaging and delivery

# Because StrictPartialOrder expects nodes as direct nodes, not nested structures,
# we need to flatten production_po nodes, aging_loop, packaging_po as nodes,
# and use edges among these nodes.

# So let's create a root PO with these three nodes (production_po, aging_loop, packaging_po)
# and add edges accordingly to reflect the sequence:
# production_po --> aging_loop --> packaging_po

root = StrictPartialOrder(nodes=[production_po, aging_loop, packaging_po])
root.order.add_edge(production_po, aging_loop)
root.order.add_edge(aging_loop, packaging_po)