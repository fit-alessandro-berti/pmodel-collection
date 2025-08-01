# Generated from: 9a74f651-680a-4b21-8d27-7ee2d4e104be.json
# Description: This process outlines the intricate steps involved in producing and distributing artisanal cheese from small-scale farms to boutique retailers. It begins with selective milk sourcing, followed by controlled fermentation, aging under precise environmental conditions, quality inspections, and customized packaging. The chain further includes dynamic inventory adjustments based on seasonal demand, specialized cold-chain logistics, and direct marketing efforts to niche customer segments. Each stage requires meticulous coordination between farmers, master cheesemakers, logistics partners, and sales teams to maintain product integrity and brand authenticity while navigating regulatory compliance and fluctuating raw material availability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Starter_Culture = Transition(label='Starter Culture')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Aging_Control = Transition(label='Aging Control')
Flavor_Monitoring = Transition(label='Flavor Monitoring')
Quality_Testing = Transition(label='Quality Testing')
Quality_Inspect = Transition(label='Quality Inspect')
Custom_Packaging = Transition(label='Custom Packaging')
Inventory_Update = Transition(label='Inventory Update')
Cold_Transport = Transition(label='Cold Transport')
Retail_Delivery = Transition(label='Retail Delivery')
Customer_Feedback = Transition(label='Customer Feedback')

# Define sub-processes as partial orders or operators

# Milk processing sub-process partial order:
# Milk Sourcing -> Milk Pasteurize -> Starter Culture -> Curd Formation -> Whey Separation -> Pressing Cheese
milk_proc_nodes = [
    Milk_Sourcing,
    Milk_Pasteurize,
    Starter_Culture,
    Curd_Formation,
    Whey_Separation,
    Pressing_Cheese,
]
milk_proc = StrictPartialOrder(nodes=milk_proc_nodes)
milk_proc.order.add_edge(Milk_Sourcing, Milk_Pasteurize)
milk_proc.order.add_edge(Milk_Pasteurize, Starter_Culture)
milk_proc.order.add_edge(Starter_Culture, Curd_Formation)
milk_proc.order.add_edge(Curd_Formation, Whey_Separation)
milk_proc.order.add_edge(Whey_Separation, Pressing_Cheese)

# Aging sub-process involves Aging Control and Flavor Monitoring in parallel
aging = StrictPartialOrder(nodes=[Aging_Control, Flavor_Monitoring])
# No edges - concurrent

# Quality sub-process:
# Quality Testing and Quality Inspect happen sequentially after aging
quality = StrictPartialOrder(nodes=[Quality_Testing, Quality_Inspect])
quality.order.add_edge(Quality_Testing, Quality_Inspect)

# Packaging
packaging = Custom_Packaging

# Inventory Update depends on Custom Packaging
inventory_and_packaging = StrictPartialOrder(nodes=[packaging, Inventory_Update])
inventory_and_packaging.order.add_edge(packaging, Inventory_Update)

# Logistics and delivery partial order:
logistics_nodes = [Cold_Transport, Retail_Delivery]
logistics = StrictPartialOrder(nodes=logistics_nodes)
logistics.order.add_edge(Cold_Transport, Retail_Delivery)

# Customer Feedback happens after Retail Delivery
feedback_po = StrictPartialOrder(nodes=[Retail_Delivery, Customer_Feedback])
feedback_po.order.add_edge(Retail_Delivery, Customer_Feedback)

# Combine aging, quality, inventory+packaging, logistics, feedback into a partial order
# Ordering: Aging -> Quality -> Packaging+Inventory -> Logistics -> Feedback
# Represent packaging and inventory as one PO, logistics as another, feedback as after logistics.

# Combine quality and packaging+inventory for order quality -> packaging+inventory
qual_pack_nodes = [quality, inventory_and_packaging]
qual_pack = StrictPartialOrder(nodes=qual_pack_nodes)
qual_pack.order.add_edge(quality, inventory_and_packaging)

# Combine logistics and feedback for logistics -> feedback
logistics_feedback_nodes = [logistics, feedback_po]
logistics_feedback = StrictPartialOrder(nodes=logistics_feedback_nodes)
logistics_feedback.order.add_edge(logistics, feedback_po)

# Combine aging, qual_pack, logistics_feedback in order:
# aging -> qual_pack -> logistics_feedback
middle_level = StrictPartialOrder(nodes=[aging, qual_pack, logistics_feedback])
middle_level.order.add_edge(aging, qual_pack)
middle_level.order.add_edge(qual_pack, logistics_feedback)

# Top-level: milk_proc -> middle_level
root = StrictPartialOrder(nodes=[milk_proc, middle_level])
root.order.add_edge(milk_proc, middle_level)