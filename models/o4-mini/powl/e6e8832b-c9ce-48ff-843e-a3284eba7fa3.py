# Generated from: e6e8832b-c9ce-48ff-843e-a3284eba7fa3.json
# Description: This process outlines the steps for liquidating physical and digital assets located in multiple international jurisdictions without direct physical access. It involves remote valuation, compliance verification with local laws, digital auction setup, secure transfer of ownership, and final financial reconciliation. Given the complexity of cross-border regulations, fluctuating asset values, and cybersecurity risks, each activity must ensure transparency, legality, and efficient communication between remote teams, legal advisors, and buyers to maximize asset recovery while minimizing exposure to fraud and legal penalties.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
asset_listing      = Transition(label='Asset Listing')
valuation_check    = Transition(label='Valuation Check')
compliance_scan    = Transition(label='Compliance Scan')
legal_review       = Transition(label='Legal Review')
remote_audit       = Transition(label='Remote Audit')
auction_setup      = Transition(label='Auction Setup')
bid_monitoring     = Transition(label='Bid Monitoring')
fraud_detection    = Transition(label='Fraud Detection')
ownership_transfer = Transition(label='Ownership Transfer')
payment_clearing   = Transition(label='Payment Clearing')
tax_calculation    = Transition(label='Tax Calculation')
fund_allocation    = Transition(label='Fund Allocation')
dispute_handling   = Transition(label='Dispute Handling')
report_generation  = Transition(label='Report Generation')
stakeholder_update = Transition(label='Stakeholder Update')

# Silent transition for optional dispute handling
skip = SilentTransition()

# Loop: perform bid monitoring, then optionally fraud detection, and repeat
bid_loop = OperatorPOWL(operator=Operator.LOOP, children=[bid_monitoring, fraud_detection])

# Exclusive choice: either handle a dispute or skip
xor_dispute = OperatorPOWL(operator=Operator.XOR, children=[dispute_handling, skip])

# Build the partial order
nodes = [
    asset_listing,
    valuation_check,
    compliance_scan,
    legal_review,
    remote_audit,
    auction_setup,
    bid_loop,
    xor_dispute,
    ownership_transfer,
    payment_clearing,
    tax_calculation,
    fund_allocation,
    report_generation,
    stakeholder_update
]
root = StrictPartialOrder(nodes=nodes)

# Initial parallel tasks after listing
root.order.add_edge(asset_listing, valuation_check)
root.order.add_edge(asset_listing, compliance_scan)
root.order.add_edge(asset_listing, legal_review)
root.order.add_edge(asset_listing, remote_audit)

# All four must complete before auction setup
root.order.add_edge(valuation_check, auction_setup)
root.order.add_edge(compliance_scan, auction_setup)
root.order.add_edge(legal_review, auction_setup)
root.order.add_edge(remote_audit, auction_setup)

# Auction setup before bidding loop
root.order.add_edge(auction_setup, bid_loop)

# After bidding loop optionally handle dispute
root.order.add_edge(bid_loop, xor_dispute)

# Then proceed to ownership transfer and financial steps
root.order.add_edge(xor_dispute, ownership_transfer)
root.order.add_edge(ownership_transfer, payment_clearing)
root.order.add_edge(payment_clearing, tax_calculation)
root.order.add_edge(tax_calculation, fund_allocation)
root.order.add_edge(fund_allocation, report_generation)

# Final stakeholder update after report generation
root.order.add_edge(report_generation, stakeholder_update)