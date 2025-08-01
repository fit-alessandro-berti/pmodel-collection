# Generated from: ee5d716a-43b3-45ac-825b-3132be50aa60.json
# Description: This process governs the operation of a dynamic art auction platform where artists, collectors, and curators interact in real-time. It involves verifying artwork authenticity through blockchain and AI analysis, dynamically adjusting reserve prices based on market trends, enabling fractional ownership bids, and managing post-auction royalty distributions. The platform ensures transparent provenance tracking, live bidding with adaptive increments, dispute resolution via decentralized arbitration, and integrates social media promotion to drive engagement. Finally, it settles payments through multi-currency crypto gateways and coordinates logistics for artwork delivery with insured shipping providers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
verify = Transition(label='Verify Artwork')
analyze = Transition(label='Analyze Provenance')
set_reserve = Transition(label='Set Reserve')
activate = Transition(label='Activate Auction')
validate = Transition(label='Validate Bidders')
enable_frac = Transition(label='Enable Fractional')
monitor = Transition(label='Monitor Bids')
adjust = Transition(label='Adjust Pricing')
promote = Transition(label='Promote Auction')
resolve = Transition(label='Resolve Disputes')
distribute = Transition(label='Distribute Royalties')
process_pay = Transition(label='Process Payments')
confirm = Transition(label='Confirm Ownership')
arrange = Transition(label='Arrange Shipping')
track = Transition(label='Track Delivery')
report = Transition(label='Report Analytics')

# Silent transitions for optional behavior
skip_frac = SilentTransition()
skip_dispute = SilentTransition()

# Optional fractional ownership before bidding
xor_frac = OperatorPOWL(operator=Operator.XOR, children=[enable_frac, skip_frac])

# Continuous bidding loop with adaptive pricing
auction_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor, adjust])

# Optional dispute resolution after auction loop
xor_dispute = OperatorPOWL(operator=Operator.XOR, children=[resolve, skip_dispute])

# Build the partial order
root = StrictPartialOrder(nodes=[
    verify, analyze, set_reserve, activate, validate,
    xor_frac, auction_loop, promote, xor_dispute,
    distribute, process_pay, confirm, arrange, track, report,
    skip_frac, skip_dispute
])

# Define control-flow order
root.order.add_edge(verify, analyze)
root.order.add_edge(analyze, set_reserve)
root.order.add_edge(set_reserve, activate)
root.order.add_edge(activate, validate)
root.order.add_edge(validate, xor_frac)

# From fractional choice to auction and promotion
root.order.add_edge(xor_frac, auction_loop)
root.order.add_edge(xor_frac, promote)

# Auction loop feeds into optional dispute resolution
root.order.add_edge(auction_loop, xor_dispute)

# After dispute resolution and auction loop, distribute royalties
root.order.add_edge(xor_dispute, distribute)
root.order.add_edge(auction_loop, distribute)

# Downstream linear flow
root.order.add_edge(distribute, process_pay)
root.order.add_edge(process_pay, confirm)
root.order.add_edge(confirm, arrange)
root.order.add_edge(arrange, track)
root.order.add_edge(track, report)