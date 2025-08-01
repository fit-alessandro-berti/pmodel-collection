# Generated from: 66215a1e-251b-4cfb-9729-2dbe2443b1c5.json
# Description: This process outlines the end-to-end supply chain for artisan cheese production, starting from sourcing rare milk varieties from select farms, through specialized fermentation and aging techniques in unique microclimates, to customized packaging and niche market distribution. It involves seasonal ingredient adjustments, quality audits at multiple stages, collaboration with local artisans for flavor profiling, and direct-to-consumer subscription management. Unexpected factors such as weather impacts on milk quality and regulatory checks for raw milk cheeses are integrated to ensure compliance and product excellence throughout the chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Culture = Transition(label='Starter Culture')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Pressing_Cheese = Transition(label='Pressing Cheese')
Aging_Control = Transition(label='Aging Control')
Flavor_Profiling = Transition(label='Flavor Profiling')
Microclimate_Check = Transition(label='Microclimate Check')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Regulatory_Audit = Transition(label='Regulatory Audit')
Order_Processing = Transition(label='Order Processing')
Subscription_Setup = Transition(label='Subscription Setup')
Delivery_Scheduling = Transition(label='Delivery Scheduling')
Customer_Feedback = Transition(label='Customer Feedback')

skip = SilentTransition()  # for optional or silent behaviors

# Quality audits happen at multiple stages. Model as XOR choice: audit or skip
Quality_Audit_1 = OperatorPOWL(operator=Operator.XOR, children=[Regulatory_Audit, skip])
Quality_Audit_2 = OperatorPOWL(operator=Operator.XOR, children=[Quality_Testing, skip])

# Seasonal ingredient adjustments and unexpected factors might cause loops (e.g., re-sourcing, re-checking)
# Model a loop for sourcing and quality audit retry due to weather/regulatory:
Sourcing_Loop = OperatorPOWL(operator=Operator.LOOP,
                             children=[Milk_Sourcing,
                                       OperatorPOWL(operator=Operator.XOR, children=[Quality_Audit_1, skip])])

# Early fermentation steps in sequence with checks
Fermentation_PO = StrictPartialOrder(nodes=[Starter_Culture, Milk_Pasteurize, Curd_Cutting])
Fermentation_PO.order.add_edge(Starter_Culture, Milk_Pasteurize)
Fermentation_PO.order.add_edge(Milk_Pasteurize, Curd_Cutting)

# Followed by whey draining and pressing in sequence
Pressing_PO = StrictPartialOrder(nodes=[Whey_Draining, Pressing_Cheese])
Pressing_PO.order.add_edge(Whey_Draining, Pressing_Cheese)

# Aging involves microclimate checks and aging control, partial order: microclimate check concurrent or before aging control
Aging_PO = StrictPartialOrder(nodes=[Microclimate_Check, Aging_Control])
Aging_PO.order.add_edge(Microclimate_Check, Aging_Control)

# Flavor profiling collaborates with artisans, happens after aging
Flavor_PO = StrictPartialOrder(nodes=[Flavor_Profiling])
# No ordering needed, standalone

# Packaging design and label printing in sequence
Packaging_PO = StrictPartialOrder(nodes=[Packaging_Design, Label_Printing])
Packaging_PO.order.add_edge(Packaging_Design, Label_Printing)

# Order processing, subscription setup and delivery scheduling partially ordered (parallel)
Order_PO = StrictPartialOrder(nodes=[Order_Processing, Subscription_Setup, Delivery_Scheduling])
# No further edges: parallel activities

# Customer feedback last
# Model final partial order connecting the flow to customer feedback
# After delivery scheduling and subscription set up finish, feedback happens
Delivery_Feedback_PO = StrictPartialOrder(nodes=[Delivery_Scheduling, Subscription_Setup, Customer_Feedback])
Delivery_Feedback_PO.order.add_edge(Delivery_Scheduling, Customer_Feedback)
Delivery_Feedback_PO.order.add_edge(Subscription_Setup, Customer_Feedback)

# Assemble all major stages in partial order
# Order: Sourcing loop -> Quality audit 2 (testing) optional -> fermentation -> pressing -> aging -> flavor profiling -> packaging -> orders -> delivery feedback

# Quality audit 2 optional after sourcing loop
After_Sourcing_PO = OperatorPOWL(operator=Operator.XOR, children=[Quality_Testing, skip])

# Complete process partial order nodes
nodes = [Sourcing_Loop, After_Sourcing_PO, Fermentation_PO, Pressing_PO,
         Aging_PO, Flavor_PO, Packaging_PO, Order_PO, Delivery_Feedback_PO]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(Sourcing_Loop, After_Sourcing_PO)
root.order.add_edge(After_Sourcing_PO, Fermentation_PO)
root.order.add_edge(Fermentation_PO, Pressing_PO)
root.order.add_edge(Pressing_PO, Aging_PO)
root.order.add_edge(Aging_PO, Flavor_PO)
root.order.add_edge(Flavor_PO, Packaging_PO)
root.order.add_edge(Packaging_PO, Order_PO)
root.order.add_edge(Order_PO, Delivery_Feedback_PO)