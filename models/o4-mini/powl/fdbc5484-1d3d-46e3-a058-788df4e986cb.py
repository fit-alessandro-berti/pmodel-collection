# Generated from: fdbc5484-1d3d-46e3-a058-788df4e986cb.json
# Description: This process involves the systematic valuation, negotiation, transfer, and legal safeguarding of intellectual assets between multiple corporate entities and individual creators. It begins with asset identification followed by detailed appraisal and risk assessment. Next, parties engage in multi-round negotiations facilitated by automated workflows and AI-driven market analysis. Upon agreement, contracts are drafted and digitally signed, incorporating dynamic royalty structures and usage restrictions. Post-transfer, continuous monitoring ensures compliance, and periodic audits verify asset integrity and usage rights. The process concludes with strategic adjustments based on market feedback and evolving intellectual property laws to maximize long-term value and minimize disputes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
asset_id        = Transition(label='Asset ID')
value_assess    = Transition(label='Value Assess')
risk_scan       = Transition(label='Risk Scan')

market_review   = Transition(label='Market Review')
initial_offer   = Transition(label='Initial Offer')
counter_offer   = Transition(label='Counter Offer')
negotiation     = Transition(label='Negotiation')

contract_draft  = Transition(label='Contract Draft')
legal_review    = Transition(label='Legal Review')
digital_sign    = Transition(label='Digital Sign')
royalty_setup   = Transition(label='Royalty Setup')
transfer_record = Transition(label='Transfer Record')

compliance_check = Transition(label='Compliance Check')
audit_schedule   = Transition(label='Audit Schedule')

market_feedback = Transition(label='Market Feedback')
strategy_update = Transition(label='Strategy Update')

# Build the negotiation sub-process as a strict partial order
neg_seq = StrictPartialOrder(nodes=[
    market_review,
    initial_offer,
    counter_offer,
    negotiation
])
neg_seq.order.add_edge(market_review, initial_offer)
neg_seq.order.add_edge(initial_offer, counter_offer)
neg_seq.order.add_edge(counter_offer, negotiation)

# Loop for multi-round negotiations:
#   execute neg_seq, then choose to exit or re-enter neg_seq
skip = SilentTransition()
negotiation_loop = OperatorPOWL(operator=Operator.LOOP, children=[neg_seq, skip])

# Build the top-level process
root = StrictPartialOrder(nodes=[
    asset_id, value_assess, risk_scan,
    negotiation_loop,
    contract_draft, legal_review, digital_sign, royalty_setup, transfer_record,
    compliance_check, audit_schedule,
    market_feedback, strategy_update
])

# Define the control-flow (partial order) edges
root.order.add_edge(asset_id,        value_assess)
root.order.add_edge(value_assess,    risk_scan)
root.order.add_edge(risk_scan,       negotiation_loop)

root.order.add_edge(negotiation_loop, contract_draft)
root.order.add_edge(contract_draft,   legal_review)
root.order.add_edge(legal_review,     digital_sign)
root.order.add_edge(digital_sign,     royalty_setup)
root.order.add_edge(royalty_setup,    transfer_record)

root.order.add_edge(transfer_record, compliance_check)
root.order.add_edge(transfer_record, audit_schedule)

root.order.add_edge(compliance_check, market_feedback)
root.order.add_edge(audit_schedule,   market_feedback)

root.order.add_edge(market_feedback, strategy_update)