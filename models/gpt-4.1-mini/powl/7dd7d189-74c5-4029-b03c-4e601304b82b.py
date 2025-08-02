# Generated from: 7dd7d189-74c5-4029-b03c-4e601304b82b.json
# Description: This process manages the sourcing, customization, and distribution of rare artisan materials used in bespoke product creation. It involves intricate coordination between local artisans, quality assurance teams, custom order management, and eco-friendly logistics providers. The process ensures traceability from raw material harvest to final delivery, incorporating sustainability checks and dynamic inventory adjustments based on artisan availability and regional demand fluctuations. It also includes a feedback loop with artisans to refine material quality and adapt supply strategies in real-time, balancing tradition with modern efficiency to meet unique customer specifications worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Material_Sourcing = Transition(label='Material Sourcing')
Supplier_Vetting = Transition(label='Supplier Vetting')
Quality_Inspect = Transition(label='Quality Inspect')
Custom_Design = Transition(label='Custom Design')
Order_Validation = Transition(label='Order Validation')
Inventory_Check = Transition(label='Inventory Check')
Artisan_Coordination = Transition(label='Artisan Coordination')
Sustainability_Audit = Transition(label='Sustainability Audit')
Packaging_Prep = Transition(label='Packaging Prep')
Logistics_Planning = Transition(label='Logistics Planning')
Shipment_Book = Transition(label='Shipment Book')
Customs_Clearance = Transition(label='Customs Clearance')
Delivery_Tracking = Transition(label='Delivery Tracking')
Customer_Feedback = Transition(label='Customer Feedback')
Demand_Forecast = Transition(label='Demand Forecast')
Stock_Replenish = Transition(label='Stock Replenish')
skip = SilentTransition()

# Partial order for sourcing and supplier vetting (sequential)
sourcing_po = StrictPartialOrder(nodes=[Material_Sourcing, Supplier_Vetting])
sourcing_po.order.add_edge(Material_Sourcing, Supplier_Vetting)

# Quality inspection comes after supplier vetting
quality_po = StrictPartialOrder(nodes=[Supplier_Vetting, Quality_Inspect])
quality_po.order.add_edge(Supplier_Vetting, Quality_Inspect)

# Custom design and order validation can be concurrent but both after quality inspect
custom_design_order_validation_po = StrictPartialOrder(
    nodes=[Quality_Inspect, Custom_Design, Order_Validation]
)
custom_design_order_validation_po.order.add_edge(Quality_Inspect, Custom_Design)
custom_design_order_validation_po.order.add_edge(Quality_Inspect, Order_Validation)

# Inventory Check and Demand Forecast can occur concurrently after Order Validation
inventory_demand_po = StrictPartialOrder(
    nodes=[Order_Validation, Inventory_Check, Demand_Forecast]
)
inventory_demand_po.order.add_edge(Order_Validation, Inventory_Check)
inventory_demand_po.order.add_edge(Order_Validation, Demand_Forecast)

# Stock Replenish after Inventory Check and Demand Forecast
stock_replenish_po = StrictPartialOrder(
    nodes=[Inventory_Check, Demand_Forecast, Stock_Replenish]
)
stock_replenish_po.order.add_edge(Inventory_Check, Stock_Replenish)
stock_replenish_po.order.add_edge(Demand_Forecast, Stock_Replenish)

# Artisan Coordination starts after Stock Replenish
artisan_coord_po = StrictPartialOrder(
    nodes=[Stock_Replenish, Artisan_Coordination]
)
artisan_coord_po.order.add_edge(Stock_Replenish, Artisan_Coordination)

# Sustainability Audit runs concurrently with Artisan Coordination
sustainability_artisan_po = StrictPartialOrder(
    nodes=[Artisan_Coordination, Sustainability_Audit]
)
# No order edges: concurrent

# Packaging Prep and Logistics Planning after Sustainability Audit and Artisan Coordination (both must finish)
packaging_logistics_po = StrictPartialOrder(
    nodes=[Artisan_Coordination, Sustainability_Audit, Packaging_Prep, Logistics_Planning]
)
packaging_logistics_po.order.add_edge(Artisan_Coordination, Packaging_Prep)
packaging_logistics_po.order.add_edge(Sustainability_Audit, Packaging_Prep)
packaging_logistics_po.order.add_edge(Artisan_Coordination, Logistics_Planning)
packaging_logistics_po.order.add_edge(Sustainability_Audit, Logistics_Planning)

# Shipment Book after Packaging Prep and Logistics Planning (both must finish)
shipment_booking_po = StrictPartialOrder(
    nodes=[Packaging_Prep, Logistics_Planning, Shipment_Book]
)
shipment_booking_po.order.add_edge(Packaging_Prep, Shipment_Book)
shipment_booking_po.order.add_edge(Logistics_Planning, Shipment_Book)

# Customs Clearance after Shipment Book
customs_po = StrictPartialOrder(
    nodes=[Shipment_Book, Customs_Clearance]
)
customs_po.order.add_edge(Shipment_Book, Customs_Clearance)

# Delivery Tracking after Customs Clearance
delivery_po = StrictPartialOrder(
    nodes=[Customs_Clearance, Delivery_Tracking]
)
delivery_po.order.add_edge(Customs_Clearance, Delivery_Tracking)

# Customer Feedback after Delivery Tracking
feedback_po = StrictPartialOrder(
    nodes=[Delivery_Tracking, Customer_Feedback]
)
feedback_po.order.add_edge(Delivery_Tracking, Customer_Feedback)

# Loop: Feedback triggers Artisan Coordination again, to refine quality & adapt supply (loop with feedback and artisan coordination)
# Loop node: body = Artisan Coordination + Sustainability Audit (concurrent), loop condition/step = Customer Feedback

loop_body = StrictPartialOrder(
    nodes=[Artisan_Coordination, Sustainability_Audit]
)
# They run concurrently; no edges needed.

# Loop node: first child = body (Artisan Coordination + Sustainability audit),
# second child = Customer Feedback (loop back condition)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, Customer_Feedback])

# Assemble all parts into one big partial order
# Group phases with po nodes:
# PHASE 1: Sourcing and vetting and quality inspect -> sourcing_po + quality_po (note quality depends on vetting)
phase1 = StrictPartialOrder(
    nodes=[sourcing_po, quality_po]
)
phase1.order.add_edge(sourcing_po, quality_po)

# Because sourcing_po includes Material_Sourcing -> Supplier_Vetting, quality_po includes Supplier_Vetting -> Quality_Inspect 
# supplier vetting is shared node, but here we compose as nodes of po, so kept as partial orders:

# Similarly for phase2: Custom Design and Order Validation
phase2 = custom_design_order_validation_po

# Phase3: Inventory, demand and stock
phase3 = StrictPartialOrder(
    nodes=[inventory_demand_po, stock_replenish_po]
)
phase3.order.add_edge(inventory_demand_po, stock_replenish_po)

# Phase4: Loop with artisan coordination, sustainability audit and feedback loop
phase4 = feedback_loop

# Phase5: Packaging, logistics, shipment, customs, delivery, feedback (feedback part included in loop)
phase5_nodes = [
    packaging_logistics_po,
    shipment_booking_po,
    customs_po,
    delivery_po,
]
phase5 = StrictPartialOrder(nodes=phase5_nodes)
phase5.order.add_edge(packaging_logistics_po, shipment_booking_po)
phase5.order.add_edge(shipment_booking_po, customs_po)
phase5.order.add_edge(customs_po, delivery_po)
# feedback is in loop already

# Compose all phases partially ordered:
# phase1 --> phase2 --> phase3 --> phase4 --> phase5
root = StrictPartialOrder(nodes=[phase1, phase2, phase3, phase4, phase5])
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, phase5)