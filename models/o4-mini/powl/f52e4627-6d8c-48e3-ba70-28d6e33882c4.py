# Generated from: f52e4627-6d8c-48e3-ba70-28d6e33882c4.json
# Description: This process involves sourcing rare, single-origin coffee beans directly from small-scale farmers across remote regions. It includes detailed farm assessments, quality verification through cupping sessions, and sustainability audits. The process requires negotiation of fair-trade contracts, coordination of logistics for fragile shipments, and continuous relationship management to ensure consistent supply and ethical practices. Additionally, it integrates seasonal forecasting and adaptive procurement strategies to account for climate variability affecting harvests, all while maintaining brand exclusivity and traceability from farm to cup.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# define activities
farm_visit        = Transition(label='Farm Visit')
quality_cupping   = Transition(label='Quality Cupping')
sample_testing    = Transition(label='Sample Testing')
sustain_audit     = Transition(label='Sustainability Audit')
risk_assess       = Transition(label='Risk Assess')
contract_draft    = Transition(label='Contract Draft')
price_negotiate   = Transition(label='Price Negotiate')
shipment_plan     = Transition(label='Shipment Plan')
customs_clear     = Transition(label='Customs Clear')
inventory_update  = Transition(label='Inventory Update')
payment_process   = Transition(label='Payment Process')
traceability_log  = Transition(label='Traceability Log')
compliance_check  = Transition(label='Compliance Check')
market_research   = Transition(label='Market Research')
forecast_adjust   = Transition(label='Forecast Adjust')
supplier_review   = Transition(label='Supplier Review')
relationship_call = Transition(label='Relationship Call')

# define loops
forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_research, forecast_adjust])
relationship_loop = OperatorPOWL(operator=Operator.LOOP, children=[supplier_review, relationship_call])

# assemble into a single partial order
nodes = [
    farm_visit, quality_cupping, sample_testing,
    sustain_audit, risk_assess, contract_draft,
    price_negotiate, shipment_plan, customs_clear,
    inventory_update, payment_process, traceability_log,
    compliance_check, forecast_loop, relationship_loop
]
root = StrictPartialOrder(nodes=nodes)

# main sequence
root.order.add_edge(farm_visit, quality_cupping)
root.order.add_edge(quality_cupping, sample_testing)
root.order.add_edge(farm_visit, sustain_audit)
root.order.add_edge(sustain_audit, risk_assess)

# converge to contract
root.order.add_edge(sample_testing, contract_draft)
root.order.add_edge(risk_assess, contract_draft)

# contract negotiation and logistics
root.order.add_edge(contract_draft, price_negotiate)
root.order.add_edge(price_negotiate, shipment_plan)
root.order.add_edge(shipment_plan, customs_clear)
root.order.add_edge(customs_clear, inventory_update)
root.order.add_edge(inventory_update, payment_process)

# traceability and compliance after inventory
root.order.add_edge(inventory_update, traceability_log)
root.order.add_edge(inventory_update, compliance_check)

# integrate forecasting before contracting
root.order.add_edge(forecast_loop, contract_draft)

# start relationship management after payment
root.order.add_edge(payment_process, relationship_loop)