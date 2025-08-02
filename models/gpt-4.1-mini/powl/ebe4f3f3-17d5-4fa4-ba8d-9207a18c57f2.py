# Generated from: ebe4f3f3-17d5-4fa4-ba8d-9207a18c57f2.json
# Description: This process describes the end-to-end supply chain management of artisan cheese production, involving unique sourcing of raw milk from local farms, quality assessment of milk, traditional cheese crafting techniques, aging control, custom packaging, and distribution to specialized retailers. The process integrates seasonal variations in milk supply, artisan scheduling, compliance with food safety standards, and direct communication with boutique shops for demand forecasting to ensure freshness and authenticity. It also includes customer feedback loops for continuous product refinement and limited edition release planning to maintain exclusivity and market differentiation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Farm_Audit = Transition(label='Farm Audit')
Milk_Testing = Transition(label='Milk Testing')
Batch_Forming = Transition(label='Batch Forming')
Curd_Cutting = Transition(label='Curd Cutting')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Process = Transition(label='Salting Process')
Aging_Control = Transition(label='Aging Control')
Quality_Check = Transition(label='Quality Check')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Inventory_Update = Transition(label='Inventory Update')
Order_Receiving = Transition(label='Order Receiving')
Retail_Coordination = Transition(label='Retail Coordination')
Shipping_Prep = Transition(label='Shipping Prep')
Customer_Feedback = Transition(label='Customer Feedback')
Demand_Forecast = Transition(label='Demand Forecast')
Limited_Release = Transition(label='Limited Release')

# Loop for customer feedback and product refinement cycle:
# Customer_Feedback then Demand_Forecast, then back to some earlier step (we model it as a loop)
# The loop body is:
#   B = sequence: Customer_Feedback -> Demand_Forecast
#   A = just after Aging and Packaging, before shipment, to resume normal flow
# We'll embed this loop around Shipping Prep or after Quality_Check.

# Another loop or choice could be the limited edition release planning, which is parallel/concurrent with normal packaging and distribution

# Construct partial order for the main supply chain process

# Define the core supply chain sequence nodes independently to then add edges between them
# We will create partial orders for some parts to model concurrency and partial orders

# Activities related to sourcing and quality assessment with seasonal variations and audits:

# A partial order for milk sourcing, farm audit and milk testing where farm audit and milk testing happen after milk sourcing,
# farm audit and milk testing can be concurrent (after milk sourcing)
Sourcing_PO = StrictPartialOrder(nodes=[Milk_Sourcing, Farm_Audit, Milk_Testing])
Sourcing_PO.order.add_edge(Milk_Sourcing, Farm_Audit)
Sourcing_PO.order.add_edge(Milk_Sourcing, Milk_Testing)

# Batch forming and cheese crafting sequence:
# Batch_Forming -> Curd_Cutting -> Molding_Cheese -> Salting_Process -> Aging_Control -> Quality_Check
Crafting_PO = StrictPartialOrder(nodes=[Batch_Forming, Curd_Cutting, Molding_Cheese, Salting_Process, Aging_Control, Quality_Check])
Crafting_PO.order.add_edge(Batch_Forming, Curd_Cutting)
Crafting_PO.order.add_edge(Curd_Cutting, Molding_Cheese)
Crafting_PO.order.add_edge(Molding_Cheese, Salting_Process)
Crafting_PO.order.add_edge(Salting_Process, Aging_Control)
Crafting_PO.order.add_edge(Aging_Control, Quality_Check)

# Packaging subtree:
Packaging_PO = StrictPartialOrder(nodes=[Packaging_Design, Label_Printing, Inventory_Update])
Packaging_PO.order.add_edge(Packaging_Design, Label_Printing)
Packaging_PO.order.add_edge(Label_Printing, Inventory_Update)

# Order receiving and retail coordination and shipping:
Order_PO = StrictPartialOrder(nodes=[Order_Receiving, Retail_Coordination, Shipping_Prep])
Order_PO.order.add_edge(Order_Receiving, Retail_Coordination)
Order_PO.order.add_edge(Retail_Coordination, Shipping_Prep)

# Concurrency of packaging and order processing/shipping (Packaging_PO and Order_PO concurrent)
Packaging_And_Order = StrictPartialOrder(nodes=[Packaging_PO, Order_PO])
Packaging_And_Order.order.add_edge(Packaging_PO, Order_PO)  # Actually should be concurrent - no edge, remove this line

# Demand forecasting and limited release planning (both related to market and exclusivity) concurrency:

Demand_Forecast_and_Release_PO = StrictPartialOrder(nodes=[Demand_Forecast, Limited_Release])
# no edges - concurrent

# Loop for customer feedback and demand forecast refinement:

# Loop: execute Customer_Feedback (A), then choice: exit or Demand_Forecast (B) then repeat loop
# According to definition: LOOP (A,B):
#   Execute A, then either exit or execute B then A again...

Customer_Feedback_Loop = OperatorPOWL(operator=Operator.LOOP,
                                      children=[Customer_Feedback, Demand_Forecast])

# Now compose the entire process:

# Overall flow:
# Sourcing_PO -> Crafting_PO -> (Packaging_PO || Order_PO) -> Customer_Feedback_Loop || Limited_Release

# Where Packaging_PO and Order_PO concurrent
Packaging_and_Order_PO = StrictPartialOrder(nodes=[Packaging_PO, Order_PO])
# no edges between Packaging_PO and Order_PO -> concurrency

# Now create a top-level PO:

root = StrictPartialOrder(
    nodes=[Sourcing_PO, Crafting_PO, Packaging_and_Order_PO, Customer_Feedback_Loop, Limited_Release]
)
# Add control flow edges:
root.order.add_edge(Sourcing_PO, Crafting_PO)
root.order.add_edge(Crafting_PO, Packaging_and_Order_PO)
root.order.add_edge(Packaging_and_Order_PO, Customer_Feedback_Loop)
# Customer_Feedback_Loop and Limited_Release concurrent (no edge)

# Resulting model:
# Sourcing_PO -> Crafting_PO -> Packaging_and_Order_PO -> Customer_Feedback_Loop
# Limited_Release concurrent with Customer_Feedback_Loop and Packaging_and_Order_PO

# No edges between Limited_Release and others to keep concurrency

# This models supply chain process with quality loops, concurrency, and limited release planning

