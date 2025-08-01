# Generated from: d4e50be6-b1ef-4673-9711-8f3843d9441e.json
# Description: This process outlines the complex steps involved in identifying, evaluating, and monetizing intellectual property assets through licensing, partnerships, or sales. It begins with patent scouting to discover viable patents, followed by technical and legal due diligence. Market analysis identifies potential licensees or buyers, and valuation models estimate patent worth. Negotiations and contract drafting establish terms, while portfolio management tracks ongoing performance. Post-deal compliance ensures adherence to agreements, and continuous innovation monitoring detects new opportunities or risks, making this a multifaceted business process combining legal, technical, and commercial expertise.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Patent_Scouting = Transition(label='Patent Scouting')
Technical_Review = Transition(label='Technical Review')
Legal_Audit = Transition(label='Legal Audit')
Market_Analysis = Transition(label='Market Analysis')
Valuation_Modeling = Transition(label='Valuation Modeling')
Risk_Assessment = Transition(label='Risk Assessment')
License_Targeting = Transition(label='License Targeting')
Buyer_Outreach = Transition(label='Buyer Outreach')
Negotiation_Phase = Transition(label='Negotiation Phase')
Contract_Drafting = Transition(label='Contract Drafting')
Approval_Process = Transition(label='Approval Process')
Portfolio_Tracking = Transition(label='Portfolio Tracking')
Revenue_Monitoring = Transition(label='Revenue Monitoring')
Compliance_Check = Transition(label='Compliance Check')
Innovation_Scan = Transition(label='Innovation Scan')
Renewal_Management = Transition(label='Renewal Management')

# Create partial orders for some parallel steps and partial orders for sequential steps

# Patent scouting followed by both technical and legal reviews in parallel
scouting_and_reviews = StrictPartialOrder(
    nodes=[Patent_Scouting, Technical_Review, Legal_Audit]
)
scouting_and_reviews.order.add_edge(Patent_Scouting, Technical_Review)
scouting_and_reviews.order.add_edge(Patent_Scouting, Legal_Audit)

# Market analysis follows reviews
market_and_valuation = StrictPartialOrder(
    nodes=[Market_Analysis, Valuation_Modeling, Risk_Assessment]
)
market_and_valuation.order.add_edge(Market_Analysis, Valuation_Modeling)
market_and_valuation.order.add_edge(Market_Analysis, Risk_Assessment)

# License Targeting and Buyer Outreach are an exclusive choice: either license-targeting path or buyer outreach path
license_path = StrictPartialOrder(
    nodes=[License_Targeting]
)
buyer_path = StrictPartialOrder(
    nodes=[Buyer_Outreach]
)
license_or_buyer = OperatorPOWL(operator=Operator.XOR, children=[license_path, buyer_path])

# Negotiation and Contract Drafting sequentially
negotiation_and_contract = StrictPartialOrder(
    nodes=[Negotiation_Phase, Contract_Drafting]
)
negotiation_and_contract.order.add_edge(Negotiation_Phase, Contract_Drafting)

# Approval Process after contract drafting
approval_step = Approval_Process

# Portfolio Tracking and Revenue Monitoring in parallel after approval
portfolio_and_revenue = StrictPartialOrder(
    nodes=[Portfolio_Tracking, Revenue_Monitoring]
)
# No order edges between these two, so they are concurrent

# Compliance Check after portfolio and revenue monitoring
# So for dependency, Compliance_Check depends on both Portfolio_Tracking and Revenue_Monitoring
# We'll create a partial order that has those 3 nodes
post_monitoring = StrictPartialOrder(
    nodes=[Portfolio_Tracking, Revenue_Monitoring, Compliance_Check]
)
post_monitoring.order.add_edge(Portfolio_Tracking, Compliance_Check)
post_monitoring.order.add_edge(Revenue_Monitoring, Compliance_Check)

# Innovation Scan and Renewal Management are ongoing monitoring, modeled as a loop:
# Loop body: Innovation Scan followed by Renewal Management
# Loop condition: after Innovation Scan and Renewal Management, choose to exit or continue the loop.
innovation_scan = Innovation_Scan
renewal_management = Renewal_Management
innov_renewal_seq = StrictPartialOrder(
    nodes=[innovation_scan, renewal_management]
)
innov_renewal_seq.order.add_edge(innovation_scan, renewal_management)

innovation_loop = OperatorPOWL(operator=Operator.LOOP, children=[innov_renewal_seq, SilentTransition()])

# Now combine all parts into a big partial order

# First combine scouting_and_reviews and market_and_valuation sequentially
scout_to_market = StrictPartialOrder(
    nodes=[scouting_and_reviews, market_and_valuation]
)
scout_to_market.order.add_edge(scouting_and_reviews, market_and_valuation)

# Combine license_or_buyer after market_and_valuation
market_to_license_buyer = StrictPartialOrder(
    nodes=[scout_to_market, license_or_buyer]
)
market_to_license_buyer.order.add_edge(scout_to_market, license_or_buyer)

# Combine negotiation_and_contract after license_or_buyer
license_to_negotiation = StrictPartialOrder(
    nodes=[market_to_license_buyer, negotiation_and_contract]
)
license_to_negotiation.order.add_edge(market_to_license_buyer, negotiation_and_contract)

# Approval after negotiation_and_contract
negotiation_to_approval = StrictPartialOrder(
    nodes=[license_to_negotiation, approval_step]
)
negotiation_to_approval.order.add_edge(license_to_negotiation, approval_step)

# portfolio_and_revenue after approval
approval_to_port_rev = StrictPartialOrder(
    nodes=[negotiation_to_approval, portfolio_and_revenue]
)
approval_to_port_rev.order.add_edge(negotiation_to_approval, portfolio_and_revenue)

# Compliance Check after portfolio_and_revenue (using post_monitoring)
port_rev_to_compliance = StrictPartialOrder(
    nodes=[approval_to_port_rev, Compliance_Check]
)
# But Compliance_Check is already included in post_monitoring. We want to keep post_monitoring as portfolio, revenue, compliance (already linked).
# To keep consistency, replace portfolio_and_revenue + Compliance_Check with post_monitoring, then attach post_monitoring after approval.
approval_to_post_monitoring = StrictPartialOrder(
    nodes=[negotiation_to_approval, post_monitoring]
)
approval_to_post_monitoring.order.add_edge(negotiation_to_approval, post_monitoring)

# Finally attach innovation_loop after compliance check (end of post_monitoring)
final_order = StrictPartialOrder(
    nodes=[approval_to_post_monitoring, innovation_loop]
)
final_order.order.add_edge(approval_to_post_monitoring, innovation_loop)

# root is the overall model
root = final_order