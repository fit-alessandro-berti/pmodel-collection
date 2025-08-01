# Generated from: 87a9de2c-bf8b-42b6-b04e-13f68239969a.json
# Description: This process outlines the complex and non-traditional workflow of patent monetization within a technology company. It involves identifying valuable intellectual property, conducting market research to find potential licensees, performing legal assessments on patent enforceability, negotiating licensing terms, and managing royalty collections. Additionally, it includes monitoring infringement through automated systems, initiating enforcement actions when necessary, and continuously optimizing the patent portfolio based on evolving market trends and technological advancements. The workflow requires cross-functional collaboration between legal, R&D, finance, and business development teams to maximize revenue from intangible assets while mitigating risks associated with patent disputes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ip_ident            = Transition(label='IP Identification')
market_scan         = Transition(label='Market Scan')
legal_review        = Transition(label='Legal Review')
valuation_est       = Transition(label='Valuation Estimate')
license_out         = Transition(label='License Outreach')
negotiation         = Transition(label='Negotiation Phase')
contract_draft      = Transition(label='Contract Draft')
royalty_setup       = Transition(label='Royalty Setup')
infringement_scan   = Transition(label='Infringement Scan')
enforcement_action  = Transition(label='Enforcement Action')
portfolio_audit     = Transition(label='Portfolio Audit')
trend_analysis      = Transition(label='Trend Analysis')
risk_assessment     = Transition(label='Risk Assessment')
revenue_tracking    = Transition(label='Revenue Tracking')
renewal_management  = Transition(label='Renewal Management')
stakeholder_sync    = Transition(label='Stakeholder Sync')
compliance_check    = Transition(label='Compliance Check')

# Silent skip for optional enforcement
skip = SilentTransition()

# Enforcement choice: either take enforcement action or skip
enforcement_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[enforcement_action, skip]
)

# Monitoring infringement: scan then optional enforcement
monitor = StrictPartialOrder(nodes=[infringement_scan, enforcement_choice])
monitor.order.add_edge(infringement_scan, enforcement_choice)

# Optimization loop: trend analysis, then a branch of portfolio audit sequence
opt_b = StrictPartialOrder(
    nodes=[portfolio_audit, risk_assessment, stakeholder_sync, compliance_check]
)
opt_b.order.add_edge(portfolio_audit, risk_assessment)
opt_b.order.add_edge(risk_assessment, stakeholder_sync)
opt_b.order.add_edge(stakeholder_sync, compliance_check)

optimization_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[trend_analysis, opt_b]
)

# Revenue & renewal sequence
revenue_seq = StrictPartialOrder(nodes=[revenue_tracking, renewal_management])
revenue_seq.order.add_edge(revenue_tracking, renewal_management)

# Root partial order: main patent monetization flow, then concurrently monitoring, revenue, optimization
root = StrictPartialOrder(
    nodes=[
        ip_ident, market_scan, legal_review, valuation_est,
        license_out, negotiation, contract_draft, royalty_setup,
        revenue_seq, monitor, optimization_loop
    ]
)

# Sequential edges for the core licensing flow
root.order.add_edge(ip_ident, market_scan)
root.order.add_edge(market_scan, legal_review)
root.order.add_edge(legal_review, valuation_est)
root.order.add_edge(valuation_est, license_out)
root.order.add_edge(license_out, negotiation)
root.order.add_edge(negotiation, contract_draft)
root.order.add_edge(contract_draft, royalty_setup)

# Forking into concurrent branches after royalty setup
root.order.add_edge(royalty_setup, revenue_seq)
root.order.add_edge(royalty_setup, monitor)
root.order.add_edge(royalty_setup, optimization_loop)