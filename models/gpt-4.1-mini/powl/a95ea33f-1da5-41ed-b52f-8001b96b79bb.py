# Generated from: a95ea33f-1da5-41ed-b52f-8001b96b79bb.json
# Description: This process outlines the intricate supply chain management of a niche artisan goods company specializing in handcrafted luxury items. It involves sourcing rare raw materials from remote locations, coordinating with local craftspeople, ensuring quality through multi-stage inspections, managing bespoke orders, and integrating sustainable packaging solutions. The process demands close collaboration between procurement, production, design, and logistics teams to maintain authenticity, meet custom client specifications, and adhere to strict environmental standards while optimizing delivery timelines and cost efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# activities
Material_Sourcing = Transition(label='Material Sourcing')
Supplier_Vetting = Transition(label='Supplier Vetting')
Sample_Testing = Transition(label='Sample Testing')

Order_Customization = Transition(label='Order Customization')
Craft_Allocation = Transition(label='Craft Allocation')
Production_Tracking = Transition(label='Production Tracking')

Quality_Audit = Transition(label='Quality Audit')
Sustainability_Check = Transition(label='Sustainability Check')

Packaging_Design = Transition(label='Packaging Design')
Inventory_Sync = Transition(label='Inventory Sync')
Logistics_Planning = Transition(label='Logistics Planning')

Client_Approval = Transition(label='Client Approval')
Shipment_Prep = Transition(label='Shipment Prep')
Delivery_Monitoring = Transition(label='Delivery Monitoring')

Feedback_Collection = Transition(label='Feedback Collection')
Reorder_Forecast = Transition(label='Reorder Forecast')

# Define the sourcing and vetting partial order
sourcing_po = StrictPartialOrder(nodes=[Material_Sourcing, Supplier_Vetting, Sample_Testing])
sourcing_po.order.add_edge(Material_Sourcing, Supplier_Vetting)
sourcing_po.order.add_edge(Supplier_Vetting, Sample_Testing)

# Production preparation partial order: order customization → craft allocation → production tracking
production_prep_po = StrictPartialOrder(
    nodes=[Order_Customization, Craft_Allocation, Production_Tracking]
)
production_prep_po.order.add_edge(Order_Customization, Craft_Allocation)
production_prep_po.order.add_edge(Craft_Allocation, Production_Tracking)

# Quality and sustainability checks in parallel but must both complete before packaging
quality_po = StrictPartialOrder(nodes=[Quality_Audit, Sustainability_Check])
# No order between Quality_Audit and Sustainability_Check = concurrent

# Packaging and logistics partial order
packaging_logistics_po = StrictPartialOrder(
    nodes=[Packaging_Design, Inventory_Sync, Logistics_Planning]
)
# Packaging_Design before Inventory_Sync and Logistics_Planning, those two concurrent
packaging_logistics_po.order.add_edge(Packaging_Design, Inventory_Sync)
packaging_logistics_po.order.add_edge(Packaging_Design, Logistics_Planning)

# Shipping and client interaction partial order
client_shipping_po = StrictPartialOrder(
    nodes=[Client_Approval, Shipment_Prep, Delivery_Monitoring]
)
client_shipping_po.order.add_edge(Client_Approval, Shipment_Prep)
client_shipping_po.order.add_edge(Shipment_Prep, Delivery_Monitoring)

# Feedback and reorder: happens after delivery monitoring
feedback_reorder_po = StrictPartialOrder(nodes=[Feedback_Collection, Reorder_Forecast])
# Both occur after Delivery Monitoring, so model as a partial order with incoming edge
# We'll connect Delivery_Monitoring --> Feedback_Collection and Delivery_Monitoring --> Reorder_Forecast
feedback_reorder_po.order.add_edge(Feedback_Collection, Reorder_Forecast)  # feedback then reorder

# Top level partial order integration

# Step 1: sourcing_po
# Step 2: production_prep_po
# Step 3: quality_po and sustainability in parallel (we have both in one partial order)
# Step 4: packaging_logistics_po
# Step 5: client_shipping_po
# Step 6: feedback_reorder_po

# Combine sourcing and production prep sequentially
sp_po = StrictPartialOrder(
    nodes=[sourcing_po, production_prep_po]
)
sp_po.order.add_edge(sourcing_po, production_prep_po)

# Combine step3 (quality checks) as a node
# We can represent quality_po as node on top level
# Then sp_po → quality_po
spq_po = StrictPartialOrder(
    nodes=[sp_po, quality_po]
)
spq_po.order.add_edge(sp_po, quality_po)

# After quality and sustainability checks, packaging and logistics
spqp_po = StrictPartialOrder(
    nodes=[spq_po, packaging_logistics_po]
)
spqp_po.order.add_edge(spq_po, packaging_logistics_po)

# Then client shipping
spqpc_po = StrictPartialOrder(
    nodes=[spqp_po, client_shipping_po]
)
spqpc_po.order.add_edge(spqp_po, client_shipping_po)

# Finally feedback and reorder after delivery monitoring
# We add an edge from client_shipping_po nodes Delivery_Monitoring to feedback_reorder_po nodes Feedback_Collection

root = StrictPartialOrder(
    nodes=[spqpc_po, feedback_reorder_po]
)
root.order.add_edge(spqpc_po, feedback_reorder_po)

# Add dependencies between Delivery_Monitoring and Feedback_Collection, Reorder_Forecast
# We cannot add edges directly between sub partial orders nodes,
# but the model structure implies the partial order.

# The above constructs a hierarchical partial order with concurrency and sequencing matching the description.