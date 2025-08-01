# Generated from: a21ca7a4-5172-4185-b454-25a8cbf3b696.json
# Description: This process outlines the detailed and non-linear supply chain involved in sourcing, producing, aging, packaging, and distributing artisan cheeses. It includes unique steps like microbial culture selection, seasonal milk sourcing, manual curd cutting, controlled humidity aging, quality flavor profiling, and niche market delivery coordination. Each activity ensures high product quality and traceability while balancing artisan techniques with scalable logistics, addressing challenges such as variable milk quality, fluctuating demand, and maintaining traditional craftsmanship alongside modern food safety standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as POWL transitions
Milk_Sourcing      = Transition(label='Milk Sourcing')
Culture_Selection  = Transition(label='Culture Selection')
Curd_Cutting       = Transition(label='Curd Cutting')
Whey_Draining      = Transition(label='Whey Draining')
Molding_Press      = Transition(label='Molding Press')
Salt_Brining       = Transition(label='Salt Brining')
Humidity_Aging     = Transition(label='Humidity Aging')
Flavor_Profiling   = Transition(label='Flavor Profiling')
Quality_Testing    = Transition(label='Quality Testing')
Packaging_Prep     = Transition(label='Packaging Prep')
Label_Design       = Transition(label='Label Design')
Niche_Marketing    = Transition(label='Niche Marketing')
Order_Processing   = Transition(label='Order Processing')
Cold_Storage       = Transition(label='Cold Storage')
Delivery_Routing   = Transition(label='Delivery Routing')
Customer_Feedback  = Transition(label='Customer Feedback')
Inventory_Audit    = Transition(label='Inventory Audit')

# Define the main batch process as a partial order
batch = StrictPartialOrder(nodes=[
    Milk_Sourcing, Culture_Selection, Curd_Cutting, Whey_Draining,
    Molding_Press, Salt_Brining, Humidity_Aging, Flavor_Profiling,
    Quality_Testing, Packaging_Prep, Label_Design,
    Niche_Marketing, Order_Processing,
    Cold_Storage, Delivery_Routing, Customer_Feedback
])

# Sequential dependencies
batch.order.add_edge(Milk_Sourcing,     Culture_Selection)
batch.order.add_edge(Culture_Selection, Curd_Cutting)
batch.order.add_edge(Curd_Cutting,      Whey_Draining)
batch.order.add_edge(Whey_Draining,     Molding_Press)
batch.order.add_edge(Molding_Press,     Salt_Brining)
batch.order.add_edge(Salt_Brining,      Humidity_Aging)
batch.order.add_edge(Humidity_Aging,    Flavor_Profiling)
batch.order.add_edge(Flavor_Profiling,  Quality_Testing)
batch.order.add_edge(Quality_Testing,   Packaging_Prep)
batch.order.add_edge(Packaging_Prep,    Label_Design)

# After labeling, marketing and order processing can run in parallel
batch.order.add_edge(Label_Design,      Niche_Marketing)
batch.order.add_edge(Label_Design,      Order_Processing)

# Both marketing and order processing must complete before cold storage
batch.order.add_edge(Niche_Marketing,   Cold_Storage)
batch.order.add_edge(Order_Processing,  Cold_Storage)

# Final delivery sequence
batch.order.add_edge(Cold_Storage,      Delivery_Routing)
batch.order.add_edge(Delivery_Routing,  Customer_Feedback)

# Build a loop: after completing a batch, perform inventory audit,
# then optionally repeat the batch for the next cycle
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[batch, Inventory_Audit]
)