# Generated from: f52e4627-6d8c-48e3-ba70-28d6e33882c4.json
# Description: This process involves sourcing rare, single-origin coffee beans directly from small-scale farmers across remote regions. It includes detailed farm assessments, quality verification through cupping sessions, and sustainability audits. The process requires negotiation of fair-trade contracts, coordination of logistics for fragile shipments, and continuous relationship management to ensure consistent supply and ethical practices. Additionally, it integrates seasonal forecasting and adaptive procurement strategies to account for climate variability affecting harvests, all while maintaining brand exclusivity and traceability from farm to cup.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Farm_Visit = Transition(label='Farm Visit')
Quality_Cupping = Transition(label='Quality Cupping')
Sustainability_Audit = Transition(label='Sustainability Audit')
Contract_Draft = Transition(label='Contract Draft')
Price_Negotiate = Transition(label='Price Negotiate')
Sample_Testing = Transition(label='Sample Testing')
Shipment_Plan = Transition(label='Shipment Plan')
Customs_Clear = Transition(label='Customs Clear')
Inventory_Update = Transition(label='Inventory Update')
Supplier_Review = Transition(label='Supplier Review')
Risk_Assess = Transition(label='Risk Assess')
Forecast_Adjust = Transition(label='Forecast Adjust')
Payment_Process = Transition(label='Payment Process')
Relationship_Call = Transition(label='Relationship Call')
Traceability_Log = Transition(label='Traceability Log')
Market_Research = Transition(label='Market Research')
Compliance_Check = Transition(label='Compliance Check')

# Partial Order 1: sourcing and quality assessment
so_q = StrictPartialOrder(nodes=[Farm_Visit, Quality_Cupping, Sustainability_Audit])
so_q.order.add_edge(Farm_Visit, Quality_Cupping)
so_q.order.add_edge(Farm_Visit, Sustainability_Audit)

# Partial Order 2: contract negotiation (draft then negotiate)
contract = StrictPartialOrder(nodes=[Contract_Draft, Price_Negotiate])
contract.order.add_edge(Contract_Draft, Price_Negotiate)

# Partial Order 3: sample testing before shipment plan
sample_ship = StrictPartialOrder(nodes=[Sample_Testing, Shipment_Plan])
sample_ship.order.add_edge(Sample_Testing, Shipment_Plan)

# Partial Order 4: customs clearance -> inventory update
customs_inv = StrictPartialOrder(nodes=[Customs_Clear, Inventory_Update])
customs_inv.order.add_edge(Customs_Clear, Inventory_Update)

# Partial Order 5: supplier review and risk assess concurrent
sup_risk = StrictPartialOrder(nodes=[Supplier_Review, Risk_Assess])
# no order => concurrent

# Partial Order 6: forecast adjust before market research
forecast_market = StrictPartialOrder(nodes=[Forecast_Adjust, Market_Research])
forecast_market.order.add_edge(Forecast_Adjust, Market_Research)

# Partial Order 7: payment process and relationship call concurrent
pay_rel = StrictPartialOrder(nodes=[Payment_Process, Relationship_Call])
# no order => concurrent

# Partial Order 8: traceability and compliance concurrent
trace_comp = StrictPartialOrder(nodes=[Traceability_Log, Compliance_Check])
# no order => concurrent

# Combine partial orders into one big partial order

# We'll create a root strict partial order with all nodes from all sub modules
all_nodes = [
    so_q, contract, sample_ship, customs_inv,
    sup_risk, forecast_market, pay_rel, trace_comp
]

root = StrictPartialOrder(nodes=all_nodes)

# Define the order among the subprocesses to reflect logical flow:

# From sourcing and quality assessment to contract negotiation
root.order.add_edge(so_q, contract)

# contract negotiation before sample testing and shipment plan
root.order.add_edge(contract, sample_ship)

# sample testing & shipment plan before customs clear & inventory update
root.order.add_edge(sample_ship, customs_inv)

# customs clear & inventory update before supplier review & risk assess
root.order.add_edge(customs_inv, sup_risk)

# supplier review & risk assess before forecast adjust & market research
root.order.add_edge(sup_risk, forecast_market)

# forecast adjust & market research before payment & relationship call
root.order.add_edge(forecast_market, pay_rel)

# payment & relationship call before traceability & compliance
root.order.add_edge(pay_rel, trace_comp)