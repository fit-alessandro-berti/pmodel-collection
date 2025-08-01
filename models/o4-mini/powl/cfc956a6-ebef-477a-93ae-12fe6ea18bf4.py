# Generated from: cfc956a6-ebef-477a-93ae-12fe6ea18bf4.json
# Description: This process manages a decentralized art auction platform where artists, collectors, and curators interact through blockchain technology to verify provenance, bid in real-time, and finalize sales securely. The system incorporates digital identity verification, smart contract deployment, dynamic pricing algorithms, and dispute resolution mechanisms. Participants submit digital assets, verify authenticity via cryptographic proofs, and place bids using cryptocurrency wallets. After auction closure, smart contracts automatically transfer ownership and funds, while integrating feedback loops for reputation scoring and future auction eligibility. The platform also supports fractional ownership and secondary sales, ensuring transparency and trust across global stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
artist_onboard      = Transition(label='Artist Onboard')
identity_check      = Transition(label='Identity Check')
asset_verify        = Transition(label='Asset Verify')
smart_deploy        = Transition(label='Smart Deploy')
wallet_link         = Transition(label='Wallet Link')
bid_monitor         = Transition(label='Bid Monitor')
bid_submit          = Transition(label='Bid Submit')
price_adjust        = Transition(label='Price Adjust')
auction_close       = Transition(label='Auction Close')
ownership_transfer  = Transition(label='Ownership Transfer')
fund_release        = Transition(label='Fund Release')
dispute_review      = Transition(label='Dispute Review')
reputation_update   = Transition(label='Reputation Update')
fractional_offer    = Transition(label='Fractional Offer')
secondary_sale      = Transition(label='Secondary Sale')

# Define the bidding loop: monitor -> submit -> adjust, repeated until auction close
bidding_body = StrictPartialOrder(nodes=[bid_monitor, bid_submit, price_adjust])
bidding_body.order.add_edge(bid_monitor, bid_submit)
bidding_body.order.add_edge(bid_submit, price_adjust)
bidding_loop = OperatorPOWL(operator=Operator.LOOP, children=[bidding_body, bidding_body])

# Concurrent ownership transfer and fund release after auction close
transfer_release = StrictPartialOrder(nodes=[ownership_transfer, fund_release])
# No edges => they run in parallel

# Optional dispute resolution: either do dispute_review or skip, then proceed
skip = SilentTransition()
dispute_flow = StrictPartialOrder(nodes=[dispute_review])
dispute_choice = OperatorPOWL(operator=Operator.XOR, children=[dispute_flow, skip])

# Build the root partial order of the entire process
root = StrictPartialOrder(nodes=[
    artist_onboard,
    identity_check,
    asset_verify,
    smart_deploy,
    wallet_link,
    bidding_loop,
    auction_close,
    transfer_release,
    dispute_choice,
    reputation_update,
    fractional_offer,
    secondary_sale
])

# Define the control-flow (precedence) relations
root.order.add_edge(artist_onboard, identity_check)
root.order.add_edge(identity_check, asset_verify)
root.order.add_edge(asset_verify, smart_deploy)
root.order.add_edge(smart_deploy, wallet_link)
root.order.add_edge(wallet_link, bidding_loop)
root.order.add_edge(bidding_loop, auction_close)
root.order.add_edge(auction_close, transfer_release)
root.order.add_edge(transfer_release, dispute_choice)
root.order.add_edge(dispute_choice, reputation_update)
root.order.add_edge(reputation_update, fractional_offer)
root.order.add_edge(reputation_update, secondary_sale)