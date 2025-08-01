# Generated from: 4b15225e-0546-4b73-bd75-d6c6125380d4.json
# Description: This process describes a dynamic approach to supply chain management that integrates real-time data analytics, machine learning predictions, and decentralized decision-making across multiple stakeholders. It begins with continuous demand sensing to capture evolving customer preferences, followed by adaptive inventory adjustments that respond to market volatility. Supplier collaboration involves synchronized updates and risk assessments to mitigate disruptions. The process incorporates automated transport routing with contingency planning for delays, alongside quality compliance checks using IoT-enabled sensors. Financial reconciliation is performed through blockchain verification to ensure transparency and reduce fraud. Finally, performance feedback loops utilize AI-driven insights to refine forecasting models and operational strategies, enabling a resilient and responsive supply chain ecosystem that adapts proactively to unexpected changes and optimizes resource allocation efficiently.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Demand_Sensing = Transition(label='Demand Sensing')
Data_Collection = Transition(label='Data Collection')

Risk_Assess = Transition(label='Risk Assess')
Supplier_Sync = Transition(label='Supplier Sync')

Inventory_Adjust = Transition(label='Inventory Adjust')
Order_Validation = Transition(label='Order Validation')

Route_Planning = Transition(label='Route Planning')
Transport_Monitor = Transition(label='Transport Monitor')
Disruption_Alert = Transition(label='Disruption Alert')

Quality_Check = Transition(label='Quality Check')
Compliance_Audit = Transition(label='Compliance Audit')

Blockchain_Verify = Transition(label='Blockchain Verify')
Payment_Authorize = Transition(label='Payment Authorize')

Feedback_Analyze = Transition(label='Feedback Analyze')
Forecast_Update = Transition(label='Forecast Update')
Strategy_Revise = Transition(label='Strategy Revise')
Resource_Allocate = Transition(label='Resource Allocate')

skip = SilentTransition()

# 1) Continuous demand sensing (Demand_Sensing + Data_Collection)
demand_sensing_po = StrictPartialOrder(nodes=[Demand_Sensing, Data_Collection])
demand_sensing_po.order.add_edge(Demand_Sensing, Data_Collection)

# 2) Adaptive inventory adjustment and order validation
inv_adj_po = StrictPartialOrder(nodes=[Inventory_Adjust, Order_Validation])
inv_adj_po.order.add_edge(Inventory_Adjust, Order_Validation)

# 3) Supplier collaboration with synchronized updates and risk assessments
supplier_collab_po = StrictPartialOrder(nodes=[Supplier_Sync, Risk_Assess])
supplier_collab_po.order.add_edge(Supplier_Sync, Risk_Assess)

# 4) Automated transport routing with contingency planning for delays
# Loop: Execute Route Planning, then choose exit or do (Disruption Alert) followed by Route Planning again
transport_loop = OperatorPOWL(operator=Operator.LOOP, children=[Route_Planning, Disruption_Alert])

# Transport monitor runs concurrently with the loop (monitor in parallel with routing)
transport_po = StrictPartialOrder(nodes=[transport_loop, Transport_Monitor])
# no order edge between them (concurrent)

# 5) Quality compliance checks
quality_po = StrictPartialOrder(nodes=[Quality_Check, Compliance_Audit])
quality_po.order.add_edge(Quality_Check, Compliance_Audit)

# 6) Financial reconciliation through blockchain verification and payment authorization
finance_po = StrictPartialOrder(nodes=[Blockchain_Verify, Payment_Authorize])
finance_po.order.add_edge(Blockchain_Verify, Payment_Authorize)

# 7) Performance feedback loops with AI-driven insights:
# This is a loop: Feedback Analyze followed by choice(XOR) between exit (skip) or Forecast Update and Strategy Revise, then Feedback Analyze again
forecast_strategy_po = StrictPartialOrder(nodes=[Forecast_Update, Strategy_Revise])
forecast_strategy_po.order.add_edge(Forecast_Update, Strategy_Revise)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Analyze, OperatorPOWL(operator=Operator.XOR, children=[forecast_strategy_po, skip])])

# 8) Resource Allocate happens after feedback loop completes
# Assemble final process as partial order
root = StrictPartialOrder(nodes=[
    demand_sensing_po, 
    inv_adj_po, 
    supplier_collab_po,
    transport_po,
    quality_po,
    finance_po,
    feedback_loop,
    Resource_Allocate
])

# Define the order:
# demand_sensing_po -> inv_adj_po, supplier_collab_po
root.order.add_edge(demand_sensing_po, inv_adj_po)
root.order.add_edge(demand_sensing_po, supplier_collab_po)

# Both inv_adj_po and supplier_collab_po lead to transport_po
root.order.add_edge(inv_adj_po, transport_po)
root.order.add_edge(supplier_collab_po, transport_po)

# transport_po leads to quality_po
root.order.add_edge(transport_po, quality_po)

# quality_po leads to finance_po
root.order.add_edge(quality_po, finance_po)

# finance_po leads to feedback_loop
root.order.add_edge(finance_po, feedback_loop)

# feedback_loop leads to Resource_Allocate
root.order.add_edge(feedback_loop, Resource_Allocate)