# Generated from: 9bc95ec9-6b0a-4b56-b653-3878499008ee.json
# Description: This process describes the end-to-end supply chain for artisan cheese production and distribution, focusing on unique quality control, seasonal sourcing, and small-batch logistics. It begins with selecting rare milk breeds and continues through handcrafted cheese making, aging in controlled environments, specialized packaging, and niche market delivery. The process involves coordination between farmers, cheesemakers, quality inspectors, packaging specialists, and boutique retailers, ensuring each batch maintains distinct flavor profiles while adapting to fluctuating demand and regulatory compliance. Traceability and sustainability are emphasized throughout, requiring detailed record keeping and adaptive transport scheduling to preserve product integrity and freshness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Breed_Select = Transition(label='Breed Select')
Milk_Collect = Transition(label='Milk Collect')
Quality_Test = Transition(label='Quality Test')
Curd_Form = Transition(label='Curd Form')
Press_Cheese = Transition(label='Press Cheese')
Salt_Cure = Transition(label='Salt Cure')
Age_Control = Transition(label='Age Control')
Flavor_Add = Transition(label='Flavor Add')
Rind_Treat = Transition(label='Rind Treat')
Batch_Label = Transition(label='Batch Label')
Package_Seal = Transition(label='Package Seal')
Storage_Track = Transition(label='Storage Track')
Order_Process = Transition(label='Order Process')
Route_Plan = Transition(label='Route Plan')
Delivery_Confirm = Transition(label='Delivery Confirm')
Customer_Feedback = Transition(label='Customer Feedback')

# Partial order for Cheese Production sequence with some concurrency:
# After Breed Select and Milk Collect, Quality Test is done.
# Then Curd Form, Press Cheese, Salt Cure sequentially.
# Aging steps (Age Control, Flavor Add, Rind Treat) are done in partial order:
# Flavor_Add and Rind_Treat can be concurrent after Age_Control is completed.

# Define aging partial order nodes and edges
aging_nodes = [Age_Control, Flavor_Add, Rind_Treat]
aging_po = StrictPartialOrder(nodes=aging_nodes)
aging_po.order.add_edge(Age_Control, Flavor_Add)
aging_po.order.add_edge(Age_Control, Rind_Treat)
# Flavor_Add and Rind_Treat have no order - concurrent

# Packaging and labeling sequence
packaging_nodes = [Batch_Label, Package_Seal, Storage_Track]
packaging_po = StrictPartialOrder(nodes=packaging_nodes)
packaging_po.order.add_edge(Batch_Label, Package_Seal)
packaging_po.order.add_edge(Package_Seal, Storage_Track)

# Delivery sequence - order process, route planning, delivery confirm
delivery_nodes = [Order_Process, Route_Plan, Delivery_Confirm]
delivery_po = StrictPartialOrder(nodes=delivery_nodes)
delivery_po.order.add_edge(Order_Process, Route_Plan)
delivery_po.order.add_edge(Route_Plan, Delivery_Confirm)

# Root nodes including Customer Feedback which comes last
root_nodes = [
    Breed_Select,
    Milk_Collect,
    Quality_Test,
    Curd_Form,
    Press_Cheese,
    Salt_Cure,
    aging_po,
    packaging_po,
    delivery_po,
    Customer_Feedback
]

root = StrictPartialOrder(nodes=root_nodes)

# Define all ordering edges to represent the process dependencies

# Breed Select and Milk Collect start concurrently but both precede Quality Test
root.order.add_edge(Breed_Select, Quality_Test)
root.order.add_edge(Milk_Collect, Quality_Test)

# Quality Test precedes Curd Form
root.order.add_edge(Quality_Test, Curd_Form)

# Curd Form -> Press Cheese -> Salt Cure sequentially
root.order.add_edge(Curd_Form, Press_Cheese)
root.order.add_edge(Press_Cheese, Salt_Cure)

# Salt Cure precedes Aging partial order
root.order.add_edge(Salt_Cure, aging_po)

# Aging partial order precedes Packaging partial order
root.order.add_edge(aging_po, packaging_po)

# Packaging partial order precedes Delivery partial order
root.order.add_edge(packaging_po, delivery_po)

# Delivery partial order precedes Customer Feedback
root.order.add_edge(delivery_po, Customer_Feedback)