# Generated from: 185da74d-cc66-4541-b682-8140b3e1d4a7.json
# Description: This process manages the sourcing, creation, and distribution of handcrafted artisanal goods from remote rural communities to urban boutique retailers. It involves identifying unique raw materials, coordinating with local artisans, ensuring quality control through multi-stage inspections, handling complex logistics in regions with limited infrastructure, and maintaining traceability for ethical certification. Additionally, the process integrates real-time feedback loops from customers to adapt designs and production methods, while balancing sustainability goals and fair trade principles with market demand fluctuations and seasonal variations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
Material_Sourcing = Transition(label='Material Sourcing')
Artisan_Selection = Transition(label='Artisan Selection')
Design_Review = Transition(label='Design Review')
Prototype_Build = Transition(label='Prototype Build')
Quality_Inspect = Transition(label='Quality Inspect')
Batch_Scheduling = Transition(label='Batch Scheduling')
Logistics_Plan = Transition(label='Logistics Plan')
Customs_Clearance = Transition(label='Customs Clearance')
Inventory_Check = Transition(label='Inventory Check')
Packaging_Setup = Transition(label='Packaging Setup')
Market_Analysis = Transition(label='Market Analysis')
Order_Processing = Transition(label='Order Processing')
Feedback_Gather = Transition(label='Feedback Gather')
Sustainability_Audit = Transition(label='Sustainability Audit')
Payment_Reconcile = Transition(label='Payment Reconcile')
Demand_Forecast = Transition(label='Demand Forecast')
Shipment_Track = Transition(label='Shipment Track')

# 1) Initial sourcing and artisan selection partial order
sourcing_po = StrictPartialOrder(nodes=[
    Material_Sourcing,
    Artisan_Selection
])
sourcing_po.order.add_edge(Material_Sourcing, Artisan_Selection)

# 2) Design and build prototype partial order
prototype_po = StrictPartialOrder(nodes=[
    Design_Review,
    Prototype_Build
])
prototype_po.order.add_edge(Design_Review, Prototype_Build)

# 3) Quality inspection loop:
# Loop body: Batch Scheduling and Quality Inspect
batch_schedule = Batch_Scheduling
quality_inspect = Quality_Inspect

# quality loop: execute Batch Scheduling then Quality Inspect, then decide to repeat or exit
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, batch_schedule])

# However, the LOOP in pm4py means (* (do body, do body)), typically:
# LOOP(A,B): execute A first, then choose exit or do B then A again.
# Our quality loop wants Batch Scheduling then Quality Inspect repeatedly.
# So we set loop = *(Batch_Scheduling, Quality_Inspect)
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[Batch_Scheduling, Quality_Inspect])

# 4) Logistics partial order:
logistics_po = StrictPartialOrder(nodes=[
    Logistics_Plan,
    Customs_Clearance,
    Inventory_Check,
    Packaging_Setup
])
logistics_po.order.add_edge(Logistics_Plan, Customs_Clearance)
logistics_po.order.add_edge(Customs_Clearance, Inventory_Check)
logistics_po.order.add_edge(Inventory_Check, Packaging_Setup)

# 5) Market and order management partial order:
market_order_po = StrictPartialOrder(nodes=[
    Market_Analysis,
    Demand_Forecast,
    Order_Processing,
    Payment_Reconcile
])
market_order_po.order.add_edge(Market_Analysis, Demand_Forecast)
market_order_po.order.add_edge(Demand_Forecast, Order_Processing)
market_order_po.order.add_edge(Order_Processing, Payment_Reconcile)

# 6) Feedback loop with sustainability audit

# The feedback loop can be represented as a loop:
# Loop body: Feedback Gather and Sustainability Audit
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Gather, Sustainability_Audit])

# 7) Shipment tracking after packaging and payment completed:
shipping_po = StrictPartialOrder(nodes=[
    Shipment_Track,
])
# Shipment_Track comes after Packaging Setup and Payment Reconcile, so connect edges later

# --- Compose main process partial order ---

# Combine initial sourcing, prototype building, quality loop in partial order:
# Prototype phase depends on Artisan Selection
phase1 = StrictPartialOrder(nodes=[sourcing_po, prototype_po])
# Partial orders inside StrictPartialOrder nodes, so edges must be between these nodes, but these are StrictPartialOrders
# pm4py POWL allows nodes as other POWL objects.

# Add edges:
phase1.order.add_edge(sourcing_po, prototype_po)  # Artisan Selection -> Design Review (through ordering phases)

# Combine phase1 with quality_loop
phase2 = StrictPartialOrder(nodes=[phase1, quality_loop])
phase2.order.add_edge(phase1, quality_loop)

# Combine phase2 with logistics_po
phase3 = StrictPartialOrder(nodes=[phase2, logistics_po])
phase3.order.add_edge(phase2, logistics_po)

# Combine phase3 with market_order_po
phase4 = StrictPartialOrder(nodes=[phase3, market_order_po])
phase4.order.add_edge(phase3, market_order_po)

# Combine phase4 with feedback_loop
phase5 = StrictPartialOrder(nodes=[phase4, feedback_loop])
phase5.order.add_edge(phase4, feedback_loop)

# Combine phase5 with shipment tracking
root = StrictPartialOrder(nodes=[phase5, shipping_po])
root.order.add_edge(phase5, shipping_po)

# Add ordering inside partial orders that cross between inner nodes for clarity:

# Expand phase1 internal edges between transitions:
# Artisan Selection must precede Design Review; it was sourced by ordering sourcing_po --> prototype_po, but transitions inside do not connect.
# Instead, add edges between transitions for clarity (combine all in one PO or keep hierarchically):

# In pm4py POWL, for cross-nodes edges, nodes must be at the same level, so better to flatten.

# Let's flatten everything at top-level for clearer partial order:

all_nodes = [
    Material_Sourcing, Artisan_Selection,
    Design_Review, Prototype_Build,
    quality_loop,
    Logistics_Plan, Customs_Clearance, Inventory_Check, Packaging_Setup,
    Market_Analysis, Demand_Forecast, Order_Processing, Payment_Reconcile,
    feedback_loop,
    Shipment_Track
]

root = StrictPartialOrder(nodes=all_nodes)

# Add edges for sourcing and artisan selection
root.order.add_edge(Material_Sourcing, Artisan_Selection)
# Artisan selection precedes design review
root.order.add_edge(Artisan_Selection, Design_Review)
# Design review precedes prototype build
root.order.add_edge(Design_Review, Prototype_Build)
# Prototype build precedes quality loop
root.order.add_edge(Prototype_Build, quality_loop)
# Quality loop precedes logistics plan
root.order.add_edge(quality_loop, Logistics_Plan)

# Logistics plan order chain
root.order.add_edge(Logistics_Plan, Customs_Clearance)
root.order.add_edge(Customs_Clearance, Inventory_Check)
root.order.add_edge(Inventory_Check, Packaging_Setup)

# Packaging setup precedes market analysis and order processing (since order processing depends on market conditions)
root.order.add_edge(Packaging_Setup, Market_Analysis)

# Market analysis order chain
root.order.add_edge(Market_Analysis, Demand_Forecast)
root.order.add_edge(Demand_Forecast, Order_Processing)
root.order.add_edge(Order_Processing, Payment_Reconcile)

# Payment reconcile precedes feedback loop and shipment track
root.order.add_edge(Payment_Reconcile, feedback_loop)
root.order.add_edge(Payment_Reconcile, Shipment_Track)

# Feedback loop can happen concurrently with shipment track once payment is done, no order edge between them

# This models the process with key sequential and partially ordered dependencies,
# quality inspections loop, feedback loop, and concurrency where possible.