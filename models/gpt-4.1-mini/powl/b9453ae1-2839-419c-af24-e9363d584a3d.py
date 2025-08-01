# Generated from: b9453ae1-2839-419c-af24-e9363d584a3d.json
# Description: This process governs the intricate supply chain for handcrafted artisan goods, integrating raw material sourcing from remote villages, quality certification by cultural experts, bespoke packaging design, and direct-to-consumer logistics. It involves multiple stakeholders including local artisans, certification bodies, eco-friendly transport providers, and niche market distributors, ensuring authenticity, sustainability, and cultural preservation while adapting dynamically to fluctuating demand and seasonal availability of materials.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Material_Sourcing = Transition(label='Material Sourcing')
Artisan_Vetting = Transition(label='Artisan Vetting')
Quality_Audit = Transition(label='Quality Audit')
Cultural_Certify = Transition(label='Cultural Certify')
Design_Packaging = Transition(label='Design Packaging')
Order_Processing = Transition(label='Order Processing')
Inventory_Sync = Transition(label='Inventory Sync')
Custom_Labeling = Transition(label='Custom Labeling')
Eco_Transport = Transition(label='Eco Transport')
Demand_Forecast = Transition(label='Demand Forecast')
Market_Analysis = Transition(label='Market Analysis')
Consumer_Feedback = Transition(label='Consumer Feedback')
Restock_Planning = Transition(label='Restock Planning')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Compliance_Check = Transition(label='Compliance Check')
Payment_Settlement = Transition(label='Payment Settlement')
Return_Handling = Transition(label='Return Handling')

# Modeling the logic described:

# 1) Raw material sourcing involves Material Sourcing from villages,
# followed by Artisan Vetting, Quality Audit and Cultural Certify in sequence.
sourcing_po = StrictPartialOrder(nodes=[Material_Sourcing, Artisan_Vetting, Quality_Audit, Cultural_Certify])
sourcing_po.order.add_edge(Material_Sourcing, Artisan_Vetting)
sourcing_po.order.add_edge(Artisan_Vetting, Quality_Audit)
sourcing_po.order.add_edge(Quality_Audit, Cultural_Certify)

# 2) Packaging: Design Packaging precedes Custom Labeling, 
# which follows the quality certification.
packaging_po = StrictPartialOrder(nodes=[Design_Packaging, Custom_Labeling])
packaging_po.order.add_edge(Design_Packaging, Custom_Labeling)

# 3) Logistics & order part: Order Processing, Inventory Sync, Eco Transport, Payment Settlement, Return Handling.
# Inventory Sync and Eco Transport can be done concurrently after Order Processing.
logistics_po = StrictPartialOrder(nodes=[Order_Processing, Inventory_Sync, Eco_Transport, Payment_Settlement, Return_Handling])
logistics_po.order.add_edge(Order_Processing, Inventory_Sync)
logistics_po.order.add_edge(Order_Processing, Eco_Transport)
logistics_po.order.add_edge(Inventory_Sync, Payment_Settlement)
logistics_po.order.add_edge(Eco_Transport, Payment_Settlement)
logistics_po.order.add_edge(Payment_Settlement, Return_Handling)

# 4) Demand & Market analysis and feedback loop:
# Demand Forecast and Market Analysis are concurrent activities,
# after which Consumer Feedback is gathered.
demand_po = StrictPartialOrder(nodes=[Demand_Forecast, Market_Analysis, Consumer_Feedback])
# Demand Forecast and Market Analysis concurrent, no order edges between them
demand_po.order.add_edge(Demand_Forecast, Consumer_Feedback)
demand_po.order.add_edge(Market_Analysis, Consumer_Feedback)

# Feedback influences Restock Planning.
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Restock_Planning, Consumer_Feedback])

# 5) Governance and compliance done concurrently with supply chain:
# Stakeholder Meet and Compliance Check concurrent, Compliance Check precedes Payment Settlement.
governance_po = StrictPartialOrder(nodes=[Stakeholder_Meet, Compliance_Check])
# Compliance_Check before Payment_Settlement (link to logistics_po)
# Add link in the final po

# Now combine all main parts:

# First combine sourcing and packaging sequentially:
sp_po = StrictPartialOrder(nodes=[sourcing_po, packaging_po])
sp_po.order.add_edge(sourcing_po, packaging_po)

# Combine demand analysis and feedback loop sequentially:
demand_feedback_po = StrictPartialOrder(nodes=[demand_po, feedback_loop])
demand_feedback_po.order.add_edge(demand_po, feedback_loop)

# Combine governance and logistics partially ordered (concurrent)
gov_log_po = StrictPartialOrder(nodes=[governance_po, logistics_po])
# Add edge Compliance_Check --> Payment_Settlement across nodes inside gov_log_po
# logistics_po and governance_po are nodes here, so to enforce Compliance_Check --> Payment_Settlement:
# We will add edges between nodes inside these pos. Instead, to keep proper structure
# we put Compliance_Check and Payment_Settlement in the same PO and add edge directly.
# So split governance_po nodes and logistics_po nodes and combine all:

combined_nodes = [
    sourcing_po,
    packaging_po,
    demand_po,
    feedback_loop,
    Stakeholder_Meet,
    Compliance_Check,
    Order_Processing,
    Inventory_Sync,
    Eco_Transport,
    Payment_Settlement,
    Return_Handling
]

root = StrictPartialOrder(nodes=combined_nodes)

# Order edges:

# sourcing_po --> packaging_po
root.order.add_edge(sourcing_po, packaging_po)

# packaging_po --> Order_Processing (packaging precedes order processing)
root.order.add_edge(packaging_po, Order_Processing)

# Order_Processing precedes Inventory_Sync and Eco_Transport
root.order.add_edge(Order_Processing, Inventory_Sync)
root.order.add_edge(Order_Processing, Eco_Transport)

# Inventory_Sync and Eco_Transport precede Payment_Settlement
root.order.add_edge(Inventory_Sync, Payment_Settlement)
root.order.add_edge(Eco_Transport, Payment_Settlement)

# Payment Settlement precedes Return Handling
root.order.add_edge(Payment_Settlement, Return_Handling)

# Stakeholder Meet and Compliance Check concurrent (no edge)

# Compliance Check precedes Payment Settlement
root.order.add_edge(Compliance_Check, Payment_Settlement)

# Demand_Forecast and Market_Analysis inside demand_po connected to Consumer Feedback already
# demand_po --> feedback_loop
root.order.add_edge(demand_po, feedback_loop)

# Restock_Planning inside feedback_loop, so no direct edge needed here

# For clarity, also add sourcing_po and demand_po concurrent so no edges between them.

# Final root is the complete process POWL model