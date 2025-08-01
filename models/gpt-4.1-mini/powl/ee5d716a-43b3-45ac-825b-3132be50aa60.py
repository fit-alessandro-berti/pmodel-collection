# Generated from: ee5d716a-43b3-45ac-825b-3132be50aa60.json
# Description: This process governs the operation of a dynamic art auction platform where artists, collectors, and curators interact in real-time. It involves verifying artwork authenticity through blockchain and AI analysis, dynamically adjusting reserve prices based on market trends, enabling fractional ownership bids, and managing post-auction royalty distributions. The platform ensures transparent provenance tracking, live bidding with adaptive increments, dispute resolution via decentralized arbitration, and integrates social media promotion to drive engagement. Finally, it settles payments through multi-currency crypto gateways and coordinates logistics for artwork delivery with insured shipping providers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Verify_Artwork = Transition(label='Verify Artwork')
Analyze_Provenance = Transition(label='Analyze Provenance')
Set_Reserve = Transition(label='Set Reserve')
Activate_Auction = Transition(label='Activate Auction')
Monitor_Bids = Transition(label='Monitor Bids')
Adjust_Pricing = Transition(label='Adjust Pricing')
Enable_Fractional = Transition(label='Enable Fractional')
Validate_Bidders = Transition(label='Validate Bidders')
Resolve_Disputes = Transition(label='Resolve Disputes')
Distribute_Royalties = Transition(label='Distribute Royalties')
Promote_Auction = Transition(label='Promote Auction')
Process_Payments = Transition(label='Process Payments')
Confirm_Ownership = Transition(label='Confirm Ownership')
Arrange_Shipping = Transition(label='Arrange Shipping')
Track_Delivery = Transition(label='Track Delivery')
Report_Analytics = Transition(label='Report Analytics')

# Modeling the process logically according to the description
#
# Phase 1: Verify Artwork and Analyze Provenance (can be concurrent)
verify_and_analyze = StrictPartialOrder(nodes=[Verify_Artwork, Analyze_Provenance])

# Phase 2: Set Reserve and Activate Auction (Set Reserve before Activate Auction)
reserve_and_activate = StrictPartialOrder(nodes=[Set_Reserve, Activate_Auction])
reserve_and_activate.order.add_edge(Set_Reserve, Activate_Auction)

# Phase 3: Monitor Bids, Adjust Pricing, Enable Fractional, Validate Bidders
# These can run in parallel once auction activated
monitor_bids = Monitor_Bids
adjust_pricing = Adjust_Pricing
enable_fractional = Enable_Fractional
validate_bidders = Validate_Bidders
# Activities concurrent, partial order with no order edges
bidding_activities = StrictPartialOrder(
    nodes=[monitor_bids, adjust_pricing, enable_fractional, validate_bidders]
)

# Phase 4: Loop representing live bidding with adaptive increments and dispute resolution
# Loop behavior: 
#   A = Monitor Bids + Adjust Pricing + Enable Fractional + Validate Bidders in parallel (concurrent)
#   B = Resolve Disputes (after A, before next A)
# Loop = *(A, B) means do A then choose exit or do B then A again

# A is bidding_activities (concurrent bidding activities)
A = bidding_activities
B = Resolve_Disputes

loop_bidding = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Phase 5: After auction ends:
# Distribution of royalties, payment processing, confirm ownership
post_auction_seq = StrictPartialOrder(
    nodes=[Distribute_Royalties, Process_Payments, Confirm_Ownership]
)
post_auction_seq.order.add_edge(Distribute_Royalties, Process_Payments)
post_auction_seq.order.add_edge(Process_Payments, Confirm_Ownership)

# Phase 6: Arrange Shipping and Track Delivery in sequence
shipping_seq = StrictPartialOrder(nodes=[Arrange_Shipping, Track_Delivery])
shipping_seq.order.add_edge(Arrange_Shipping, Track_Delivery)

# Phase 7: Promote Auction and Report Analytics are concurrent with other main phases:
# For maximal concurrency, put Promote_Auction and Report_Analytics concurrent with auction phases
promotion_and_reporting = StrictPartialOrder(nodes=[Promote_Auction, Report_Analytics])

# Now, assemble the main POWL model reflecting order

# 1) first verify_and_analyze
# 2) then reserve_and_activate (depends on verify_and_analyze)
# 3) then loop_bidding (depends on activate_auction, so depends on reserve_and_activate)
# 4) then post_auction_seq (depends on loop ending)
# 5) then shipping_seq (depends on confirm ownership)
# 6) promotion_and_reporting concurrent with bidding and post-auction (so connect it after reserve_and_activate)

root_nodes = [
    verify_and_analyze,
    reserve_and_activate,
    loop_bidding,
    post_auction_seq,
    shipping_seq,
    promotion_and_reporting,
]

root = StrictPartialOrder(nodes=root_nodes)

# Add order edges for dependencies
root.order.add_edge(verify_and_analyze, reserve_and_activate)
root.order.add_edge(reserve_and_activate, loop_bidding)
root.order.add_edge(loop_bidding, post_auction_seq)
root.order.add_edge(post_auction_seq, shipping_seq)
root.order.add_edge(reserve_and_activate, promotion_and_reporting)
