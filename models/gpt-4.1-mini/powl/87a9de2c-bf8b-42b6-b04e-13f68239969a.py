# Generated from: 87a9de2c-bf8b-42b6-b04e-13f68239969a.json
# Description: This process outlines the complex and non-traditional workflow of patent monetization within a technology company. It involves identifying valuable intellectual property, conducting market research to find potential licensees, performing legal assessments on patent enforceability, negotiating licensing terms, and managing royalty collections. Additionally, it includes monitoring infringement through automated systems, initiating enforcement actions when necessary, and continuously optimizing the patent portfolio based on evolving market trends and technological advancements. The workflow requires cross-functional collaboration between legal, R&D, finance, and business development teams to maximize revenue from intangible assets while mitigating risks associated with patent disputes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
IP_Identification = Transition(label='IP Identification')
Market_Scan = Transition(label='Market Scan')
Legal_Review = Transition(label='Legal Review')
Valuation_Estimate = Transition(label='Valuation Estimate')
License_Outreach = Transition(label='License Outreach')
Negotiation_Phase = Transition(label='Negotiation Phase')
Contract_Draft = Transition(label='Contract Draft')
Royalty_Setup = Transition(label='Royalty Setup')
Infringement_Scan = Transition(label='Infringement Scan')
Enforcement_Action = Transition(label='Enforcement Action')
Portfolio_Audit = Transition(label='Portfolio Audit')
Trend_Analysis = Transition(label='Trend Analysis')
Risk_Assessment = Transition(label='Risk Assessment')
Revenue_Tracking = Transition(label='Revenue Tracking')
Renewal_Management = Transition(label='Renewal Management')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Compliance_Check = Transition(label='Compliance Check')

# Monitoring infringement -> enforcement loop: LOOP(Infringement_Scan, Enforcement_Action)
infringement_loop = OperatorPOWL(operator=Operator.LOOP, children=[Infringement_Scan, Enforcement_Action])

# Continuous portfolio optimization = partial order of Portfolio_Audit -> Trend_Analysis -> Risk_Assessment
portfolio_analysis = StrictPartialOrder(nodes=[Portfolio_Audit, Trend_Analysis, Risk_Assessment])
portfolio_analysis.order.add_edge(Portfolio_Audit, Trend_Analysis)
portfolio_analysis.order.add_edge(Trend_Analysis, Risk_Assessment)

# Revenue tracking related activities sequence:
revenue_sequence = StrictPartialOrder(
    nodes=[Revenue_Tracking, Renewal_Management, Stakeholder_Sync, Compliance_Check])
revenue_sequence.order.add_edge(Revenue_Tracking, Renewal_Management)
revenue_sequence.order.add_edge(Renewal_Management, Stakeholder_Sync)
revenue_sequence.order.add_edge(Stakeholder_Sync, Compliance_Check)

# Licensing sequence: Valuation_Estimate -> License_Outreach -> Negotiation_Phase -> Contract_Draft -> Royalty_Setup
licensing_sequence = StrictPartialOrder(
    nodes=[Valuation_Estimate, License_Outreach, Negotiation_Phase, Contract_Draft, Royalty_Setup])
licensing_sequence.order.add_edge(Valuation_Estimate, License_Outreach)
licensing_sequence.order.add_edge(License_Outreach, Negotiation_Phase)
licensing_sequence.order.add_edge(Negotiation_Phase, Contract_Draft)
licensing_sequence.order.add_edge(Contract_Draft, Royalty_Setup)

# Market research and legal review are parallel before valuation:
market_legal = StrictPartialOrder(nodes=[Market_Scan, Legal_Review])
# no order edges -> concurrent

# After both market scan and legal review complete, valuation estimate starts:
# This means Market_Scan and Legal_Review must precede Valuation_Estimate
market_legal_valuation = StrictPartialOrder(
    nodes=[market_legal, Valuation_Estimate])
market_legal_valuation.order.add_edge(market_legal, Valuation_Estimate)

# Partial order combining market/legal parallel, then valuation, then licensing
pre_licensing = StrictPartialOrder(
    nodes=[Market_Scan, Legal_Review, Valuation_Estimate])
pre_licensing.order.add_edge(Market_Scan, Valuation_Estimate)
pre_licensing.order.add_edge(Legal_Review, Valuation_Estimate)

# Combine pre_licensing and licensing_sequence in sequence
market_to_license = StrictPartialOrder(
    nodes=[pre_licensing, licensing_sequence])
market_to_license.order.add_edge(pre_licensing, licensing_sequence)

# IP Identification to start, then market/legal and beyond
start_to_market = StrictPartialOrder(
    nodes=[IP_Identification, market_to_license])
start_to_market.order.add_edge(IP_Identification, market_to_license)

# Combine all top-level parts:
# start_to_market -> infringement_loop (monitoring)
# start_to_market -> portfolio_analysis (optimization)
# start_to_market -> revenue_sequence (tracking and management)

root = StrictPartialOrder(
    nodes=[start_to_market, infringement_loop, portfolio_analysis, revenue_sequence])
root.order.add_edge(start_to_market, infringement_loop)
root.order.add_edge(start_to_market, portfolio_analysis)
root.order.add_edge(start_to_market, revenue_sequence)