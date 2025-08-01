# Generated from: d4e50be6-b1ef-4673-9711-8f3843d9441e.json
# Description: This process outlines the complex steps involved in identifying, evaluating, and monetizing intellectual property assets through licensing, partnerships, or sales. It begins with patent scouting to discover viable patents, followed by technical and legal due diligence. Market analysis identifies potential licensees or buyers, and valuation models estimate patent worth. Negotiations and contract drafting establish terms, while portfolio management tracks ongoing performance. Post-deal compliance ensures adherence to agreements, and continuous innovation monitoring detects new opportunities or risks, making this a multifaceted business process combining legal, technical, and commercial expertise.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
patent_scouting    = Transition(label='Patent Scouting')
technical_review   = Transition(label='Technical Review')
legal_audit        = Transition(label='Legal Audit')
market_analysis    = Transition(label='Market Analysis')
valuation_modeling = Transition(label='Valuation Modeling')
risk_assessment    = Transition(label='Risk Assessment')
license_targeting  = Transition(label='License Targeting')
buyer_outreach     = Transition(label='Buyer Outreach')
negotiation_phase  = Transition(label='Negotiation Phase')
contract_drafting  = Transition(label='Contract Drafting')
approval_process   = Transition(label='Approval Process')
portfolio_tracking = Transition(label='Portfolio Tracking')
revenue_monitoring = Transition(label='Revenue Monitoring')
compliance_check   = Transition(label='Compliance Check')
innovation_scan    = Transition(label='Innovation Scan')
renewal_management = Transition(label='Renewal Management')

# Exclusive choice between licensing vs. sales
deal_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[license_targeting, buyer_outreach]
)

# Loop for ongoing portfolio management and monitoring
loop_body_A = StrictPartialOrder(
    nodes=[portfolio_tracking, revenue_monitoring, compliance_check, innovation_scan, renewal_management]
)
loop_body_B = StrictPartialOrder(
    nodes=[portfolio_tracking, revenue_monitoring, compliance_check, innovation_scan, renewal_management]
)
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[loop_body_A, loop_body_B]
)

# Build the top-level partial order
root = StrictPartialOrder(
    nodes=[
        patent_scouting,
        technical_review,
        legal_audit,
        market_analysis,
        valuation_modeling,
        risk_assessment,
        deal_choice,
        negotiation_phase,
        contract_drafting,
        approval_process,
        monitoring_loop
    ]
)

# Define the control-flow (partial order) edges
root.order.add_edge(patent_scouting, technical_review)
root.order.add_edge(patent_scouting, legal_audit)
root.order.add_edge(technical_review, market_analysis)
root.order.add_edge(legal_audit, market_analysis)
root.order.add_edge(market_analysis, valuation_modeling)
root.order.add_edge(market_analysis, risk_assessment)
root.order.add_edge(valuation_modeling, deal_choice)
root.order.add_edge(risk_assessment, deal_choice)
root.order.add_edge(deal_choice, negotiation_phase)
root.order.add_edge(negotiation_phase, contract_drafting)
root.order.add_edge(contract_drafting, approval_process)
root.order.add_edge(approval_process, monitoring_loop)