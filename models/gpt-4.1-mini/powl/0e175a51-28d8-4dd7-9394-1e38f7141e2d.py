# Generated from: 0e175a51-28d8-4dd7-9394-1e38f7141e2d.json
# Description: This process outlines the end-to-end supply chain management for a specialty artisan coffee company that sources unique coffee beans from remote farms, manages bespoke roasting profiles, and delivers personalized subscription packages to niche market customers. It includes activities such as farmer collaboration, quality cupping, custom roasting, packaging innovation, logistics coordination, and customer feedback integration to ensure a highly tailored coffee experience that balances sustainability, quality, and exclusivity across multiple global regions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Farm_Selection = Transition(label='Farm Selection')
Bean_Harvest = Transition(label='Bean Harvest')
Initial_Sorting = Transition(label='Initial Sorting')
Quality_Cupping = Transition(label='Quality Cupping')
Farmer_Feedback = Transition(label='Farmer Feedback')
Roast_Profiling = Transition(label='Roast Profiling')
Batch_Roasting = Transition(label='Batch Roasting')
Flavor_Testing = Transition(label='Flavor Testing')
Custom_Packaging = Transition(label='Custom Packaging')
Subscription_Setup = Transition(label='Subscription Setup')
Order_Processing = Transition(label='Order Processing')
Logistics_Planning = Transition(label='Logistics Planning')
Shipment_Tracking = Transition(label='Shipment Tracking')
Customer_Support = Transition(label='Customer Support')
Feedback_Analysis = Transition(label='Feedback Analysis')
Inventory_Audit = Transition(label='Inventory Audit')

# Construct partial orders for production chain

# Coffee sourcing and quality assessment (linear flow)
sourcing_qc = StrictPartialOrder(nodes=[Farm_Selection, Bean_Harvest, Initial_Sorting, Quality_Cupping, Farmer_Feedback])
sourcing_qc.order.add_edge(Farm_Selection, Bean_Harvest)
sourcing_qc.order.add_edge(Bean_Harvest, Initial_Sorting)
sourcing_qc.order.add_edge(Initial_Sorting, Quality_Cupping)
sourcing_qc.order.add_edge(Qualer_Cupping := Quality_Cupping, Farmer_Feedback)

# Roasting loop: Roast Profiling and Batch Roasting iterated until flavor testing succeeds
# Model loop: execute Roast Profiling, then Batch Roasting; after Batch Roasting choose to exit or repeat
roasting_loop = OperatorPOWL(operator=Operator.LOOP, children=[Roast_Profiling, Batch_Roasting])

# Flavor testing happens after the roasting loop
post_roast = StrictPartialOrder(nodes=[roasting_loop, Flavor_Testing])
post_roast.order.add_edge(roasting_loop, Flavor_Testing)

# Packaging and subscription setup run in partial order (can be concurrent)
packaging_subscription = StrictPartialOrder(nodes=[Custom_Packaging, Subscription_Setup])

# Order processing follows subscription setup
order_and_logistics = StrictPartialOrder(nodes=[Subscription_Setup, Order_Processing, Logistics_Planning, Shipment_Tracking])
order_and_logistics.order.add_edge(Subscription_Setup, Order_Processing)
order_and_logistics.order.add_edge(Order_Processing, Logistics_Planning)
order_and_logistics.order.add_edge(Logistics_Planning, Shipment_Tracking)

# Customer feedback processing parallel with Inventory audit
feedback_inventory_po = StrictPartialOrder(nodes=[Customer_Support, Feedback_Analysis, Inventory_Audit])
feedback_inventory_po.order.add_edge(Customer_Support, Feedback_Analysis)

# Merge the whole flow as partial order: 
# sourcing_qc --> post_roast --> packaging_subscription & order_and_logistics --> feedback_inventory_po

# We create a partial order including all these major blocks:
root = StrictPartialOrder(
    nodes=[sourcing_qc, post_roast, packaging_subscription, order_and_logistics, feedback_inventory_po]
)

# Add order edges according to the process description
root.order.add_edge(sourcing_qc, post_roast)
root.order.add_edge(post_roast, packaging_subscription)
root.order.add_edge(post_roast, order_and_logistics)
root.order.add_edge(packaging_subscription, feedback_inventory_po)
root.order.add_edge(order_and_logistics, feedback_inventory_po)