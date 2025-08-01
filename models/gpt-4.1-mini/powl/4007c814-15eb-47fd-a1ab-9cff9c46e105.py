# Generated from: 4007c814-15eb-47fd-a1ab-9cff9c46e105.json
# Description: This process outlines the unique and intricate supply chain for producing artisanal cheese, involving rare milk sourcing, traditional fermentation, customized aging, and niche market distribution. It includes quality inspections at multiple stages, environmental condition monitoring, and collaboration with local farmers. The process ensures the preservation of heritage techniques while integrating modern traceability and customer feedback loops to maintain product authenticity and high quality. Seasonal variations and small batch production add complexity, requiring adaptive scheduling and logistics coordination to meet demand without compromising artisanal standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Check1 = Transition(label='Quality Check')     # After Milk Sourcing
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Culture_Prepare = Transition(label='Culture Prepare')
Milk_Inoculate = Transition(label='Milk Inoculate')
Coagulate_Milk = Transition(label='Coagulate Milk')
Curd_Cut = Transition(label='Curd Cut')
Whey_Drain = Transition(label='Whey Drain')
Mold_Fill = Transition(label='Mold Fill')
Press_Cheese = Transition(label='Press Cheese')
Salt_Rub = Transition(label='Salt Rub')

Quality_Check2 = Transition(label='Quality Check')     # After pressing & salt rub

Aging_Monitor = Transition(label='Aging Monitor')
Humidity_Control = Transition(label='Humidity Control')

Flavor_Test = Transition(label='Flavor Test')

Packaging = Transition(label='Packaging')

Inventory_Update = Transition(label='Inventory Update')
Order_Fulfill = Transition(label='Order Fulfill')

Customer_Feedback = Transition(label='Customer Feedback')

# We use Quality_Check twice, these are two distinct occurrences to model checkpoints
# Environmental condition monitoring done by Aging Monitor and Humidity Control,
# which can be done concurrently and repeatedly during aging phase.

# Build the initial supply and preparation partial order
prep_nodes = [
    Milk_Sourcing,
    Quality_Check1,
    Milk_Pasteurize,
    Culture_Prepare,
    Milk_Inoculate,
    Coagulate_Milk,
    Curd_Cut,
    Whey_Drain,
    Mold_Fill,
    Press_Cheese,
    Salt_Rub,
    Quality_Check2,
]
prep_po = StrictPartialOrder(nodes=prep_nodes)
# Ordering
prep_po.order.add_edge(Milk_Sourcing, Quality_Check1)
prep_po.order.add_edge(Quality_Check1, Milk_Pasteurize)
prep_po.order.add_edge(Milk_Pasteurize, Culture_Prepare)
prep_po.order.add_edge(Culture_Prepare, Milk_Inoculate)
prep_po.order.add_edge(Milk_Inoculate, Coagulate_Milk)
prep_po.order.add_edge(Coagulate_Milk, Curd_Cut)
prep_po.order.add_edge(Curd_Cut, Whey_Drain)
prep_po.order.add_edge(Whey_Drain, Mold_Fill)
prep_po.order.add_edge(Mold_Fill, Press_Cheese)
prep_po.order.add_edge(Press_Cheese, Salt_Rub)
prep_po.order.add_edge(Salt_Rub, Quality_Check2)

# Aging phase: Aging Monitor and Humidity Control done concurrently and repeatedly
# Model as a LOOP:
# A = (Aging Monitor and Humidity Control in parallel)
# B = Flavor Test (quality check in aging loop)

# Build aging concurrent nodes
aging_nodes = [Aging_Monitor, Humidity_Control]
aging_po = StrictPartialOrder(nodes=aging_nodes)
# No order edges so they are concurrent

aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        aging_po,       # A: monitoring in partial order (concurrent)
        Flavor_Test     # B: test flavor before next cycle
    ]
)

# Packaging after aging loop
# so ordering: aging_loop --> Packaging
aging_pack_po = StrictPartialOrder(nodes=[aging_loop, Packaging])
aging_pack_po.order.add_edge(aging_loop, Packaging)

# Final distribution partial order
final_nodes = [Inventory_Update, Order_Fulfill, Customer_Feedback]
final_po = StrictPartialOrder(nodes=final_nodes)
final_po.order.add_edge(Inventory_Update, Order_Fulfill)
final_po.order.add_edge(Order_Fulfill, Customer_Feedback)

# Connect phases in partial order 
# prep_po --> aging_pack_po --> final_po

root = StrictPartialOrder(nodes=[prep_po, aging_pack_po, final_po])
root.order.add_edge(prep_po, aging_pack_po)
root.order.add_edge(aging_pack_po, final_po)