# Generated from: a21ca7a4-5172-4185-b454-25a8cbf3b696.json
# Description: This process outlines the detailed and non-linear supply chain involved in sourcing, producing, aging, packaging, and distributing artisan cheeses. It includes unique steps like microbial culture selection, seasonal milk sourcing, manual curd cutting, controlled humidity aging, quality flavor profiling, and niche market delivery coordination. Each activity ensures high product quality and traceability while balancing artisan techniques with scalable logistics, addressing challenges such as variable milk quality, fluctuating demand, and maintaining traditional craftsmanship alongside modern food safety standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Selection = Transition(label='Culture Selection')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding_Press = Transition(label='Molding Press')
Salt_Brining = Transition(label='Salt Brining')
Humidity_Aging = Transition(label='Humidity Aging')
Flavor_Profiling = Transition(label='Flavor Profiling')
Quality_Testing = Transition(label='Quality Testing')
Packaging_Prep = Transition(label='Packaging Prep')
Label_Design = Transition(label='Label Design')
Niche_Marketing = Transition(label='Niche Marketing')
Order_Processing = Transition(label='Order Processing')
Cold_Storage = Transition(label='Cold Storage')
Delivery_Routing = Transition(label='Delivery Routing')
Customer_Feedback = Transition(label='Customer Feedback')
Inventory_Audit = Transition(label='Inventory Audit')

# Model the core production partial order:
# Milk sourcing and culture selection are parallel start activities
# Followed by sequential cheese making steps: curd cutting -> whey draining -> molding press -> salt brining
# Then humidity aging, flavor profiling, quality testing (some parallelism possible)
# Followed by packaging prep and label design in parallel
# Then niche marketing and order processing parallel
# Followed by cold storage -> delivery routing
# Customer feedback and inventory audit run after delivery routing, possibly in parallel

# Partial order nodes for initial parallel sourcing and selection
initial_nodes = [Milk_Sourcing, Culture_Selection]
# Cheese making chain
cheese_chain = [Curd_Cutting, Whey_Draining, Molding_Press, Salt_Brining]
# Post-cheese aging and profiling
aging_and_profiling = [Humidity_Aging, Flavor_Profiling, Quality_Testing]
# Packaging nodes parallel
packaging_nodes = [Packaging_Prep, Label_Design]
# Marketing and order processing parallel
marketing_order = [Niche_Marketing, Order_Processing]
# Cold storage and delivery sequence
storage_and_delivery = [Cold_Storage, Delivery_Routing]
# Final parallel feedback and audit
feedback_and_audit = [Customer_Feedback, Inventory_Audit]

# Create partial orders for each grouped sequence where it is strictly sequential

# Cheese making strict chain PO
cheese_PO = StrictPartialOrder(nodes=cheese_chain)
for i in range(len(cheese_chain)-1):
    cheese_PO.order.add_edge(cheese_chain[i], cheese_chain[i+1])

# Aging and profiling partial order
# Humidity aging must happen before flavor profiling and quality testing
aging_PO = StrictPartialOrder(nodes=aging_and_profiling)
aging_PO.order.add_edge(Humidity_Aging, Flavor_Profiling)
aging_PO.order.add_edge(Humidity_Aging, Quality_Testing)
# Flavor profiling and Quality testing are concurrent after Humidity Aging (no edge between them)

# Packaging prep and label design are parallel, no sequential order

packaging_PO = StrictPartialOrder(nodes=packaging_nodes)  # no edges

# Marketing and order processing parallel

marketing_PO = StrictPartialOrder(nodes=marketing_order)  # no edges

# Storage and delivery sequence

storage_PO = StrictPartialOrder(nodes=storage_and_delivery)
storage_PO.order.add_edge(Cold_Storage, Delivery_Routing)

# Customer feedback and inventory audit in parallel

final_PO = StrictPartialOrder(nodes=feedback_and_audit)  # no edges

# Create initial sourcing and selection parallel PO

initial_PO = StrictPartialOrder(nodes=initial_nodes)  # parallel start, no edges

# Now build the overall PO by connecting these sub-models with ordering dependencies

# Combine initial_PO, cheese_PO, aging_PO, packaging_PO, marketing_PO, storage_PO, final_PO

# All nodes:
nodes = [
    initial_PO,
    cheese_PO,
    aging_PO,
    packaging_PO,
    marketing_PO,
    storage_PO,
    final_PO
]

root = StrictPartialOrder(nodes=nodes)

# Order edges:

# initial_PO before cheese_PO
root.order.add_edge(initial_PO, cheese_PO)
# cheese_PO before aging_PO
root.order.add_edge(cheese_PO, aging_PO)
# aging_PO before packaging_PO
root.order.add_edge(aging_PO, packaging_PO)
# packaging_PO before marketing_PO
root.order.add_edge(packaging_PO, marketing_PO)
# marketing_PO before storage_PO
root.order.add_edge(marketing_PO, storage_PO)
# storage_PO before final_PO
root.order.add_edge(storage_PO, final_PO)