# Generated from: 07fc5d86-4882-4448-a8f8-31a1179e6a55.json
# Description: This process manages a supply chain that dynamically adapts to real-time market fluctuations, supplier disruptions, and customer demand variability. It incorporates predictive analytics, multi-tier supplier coordination, and automated contingency planning. The workflow includes continuous data ingestion from IoT devices, AI-driven risk assessment, and decentralized decision-making to optimize inventory levels and logistics routes. This atypical approach reduces lead times and enhances resilience by blending human oversight with autonomous adjustments, ensuring seamless operations despite external uncertainties and internal constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Data_Ingestion = Transition(label='Data Ingestion')
Risk_Analysis = Transition(label='Risk Analysis')
Demand_Forecast = Transition(label='Demand Forecast')
Supplier_Sync = Transition(label='Supplier Sync')
Inventory_Audit = Transition(label='Inventory Audit')
Contingency_Plan = Transition(label='Contingency Plan')
Order_Prioritize = Transition(label='Order Prioritize')
Route_Optimize = Transition(label='Route Optimize')
Capacity_Check = Transition(label='Capacity Check')
Quality_Review = Transition(label='Quality Review')
Shipment_Track = Transition(label='Shipment Track')
Disruption_Alert = Transition(label='Disruption Alert')
Contract_Update = Transition(label='Contract Update')
Resource_Allocate = Transition(label='Resource Allocate')
Feedback_Loop = Transition(label='Feedback Loop')
Performance_Review = Transition(label='Performance Review')

# Model a loop where continuous Data Ingestion is followed by Risk Analysis,
# then conditional Demand Forecast or Disruption Alert, then multi-tier coordination:
# Supplier Sync and Inventory Audit concurrent,
# then Contingency Plan,
# then order and routing optimization,
# capacity and quality checks concurrent,
# shipment tracking, contract updates, resource allocation,
# finally a feedback and performance review loop.

# Choice after Risk Analysis: either Demand Forecast or Disruption Alert (market or supplier issues)
demand_or_disruption = OperatorPOWL(operator=Operator.XOR, children=[Demand_Forecast, Disruption_Alert])

# Supplier Sync and Inventory Audit concurrent partial order (no edges)
supplier_inventory = StrictPartialOrder(nodes=[Supplier_Sync, Inventory_Audit])

# Capacity Check and Quality Review concurrent partial order (no edges)
capacity_quality = StrictPartialOrder(nodes=[Capacity_Check, Quality_Review])

# Build a partial order from Demand/Disruption -> supplier_inventory -> contingency plan
po_mid = StrictPartialOrder(nodes=[demand_or_disruption, supplier_inventory, Contingency_Plan])
po_mid.order.add_edge(demand_or_disruption, supplier_inventory)
po_mid.order.add_edge(supplier_inventory, Contingency_Plan)

# Partial order for order_prioritize -> route_optimize -> capacity_quality
po_order_route = StrictPartialOrder(nodes=[Order_Prioritize, Route_Optimize, capacity_quality])
po_order_route.order.add_edge(Order_Prioritize, Route_Optimize)
po_order_route.order.add_edge(Route_Optimize, capacity_quality)

# Partial order from contingency plan -> order_route -> shipment tracking etc
po_late = StrictPartialOrder(
    nodes=[Contingency_Plan, po_order_route, Shipment_Track, Contract_Update, Resource_Allocate]
)
po_late.order.add_edge(Contingency_Plan, po_order_route)
po_late.order.add_edge(po_order_route, Shipment_Track)
po_late.order.add_edge(Shipment_Track, Contract_Update)
po_late.order.add_edge(Contract_Update, Resource_Allocate)

# Feedback loop after resource allocate to Feedback Loop and Performance Review
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Resource_Allocate, StrictPartialOrder(
    nodes=[Feedback_Loop, Performance_Review]
)])

# Combine late phase (up to resource allocate) with feedback loop
po_with_feedback = StrictPartialOrder(nodes=[po_late, feedback_loop])
po_with_feedback.order.add_edge(po_late, feedback_loop)

# Full partial order: Data Ingestion -> Risk Analysis -> po_mid -> po_with_feedback
root = StrictPartialOrder(
    nodes=[Data_Ingestion, Risk_Analysis, po_mid, po_with_feedback]
)
root.order.add_edge(Data_Ingestion, Risk_Analysis)
root.order.add_edge(Risk_Analysis, po_mid)
root.order.add_edge(po_mid, po_with_feedback)