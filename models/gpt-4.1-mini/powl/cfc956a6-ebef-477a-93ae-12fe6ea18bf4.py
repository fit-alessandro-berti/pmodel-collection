# Generated from: cfc956a6-ebef-477a-93ae-12fe6ea18bf4.json
# Description: This process manages a decentralized art auction platform where artists, collectors, and curators interact through blockchain technology to verify provenance, bid in real-time, and finalize sales securely. The system incorporates digital identity verification, smart contract deployment, dynamic pricing algorithms, and dispute resolution mechanisms. Participants submit digital assets, verify authenticity via cryptographic proofs, and place bids using cryptocurrency wallets. After auction closure, smart contracts automatically transfer ownership and funds, while integrating feedback loops for reputation scoring and future auction eligibility. The platform also supports fractional ownership and secondary sales, ensuring transparency and trust across global stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Artist_Onboard = Transition(label='Artist Onboard')
Asset_Verify = Transition(label='Asset Verify')
Identity_Check = Transition(label='Identity Check')
Smart_Deploy = Transition(label='Smart Deploy')
Bid_Monitor = Transition(label='Bid Monitor')
Price_Adjust = Transition(label='Price Adjust')
Wallet_Link = Transition(label='Wallet Link')
Bid_Submit = Transition(label='Bid Submit')
Auction_Close = Transition(label='Auction Close')
Ownership_Transfer = Transition(label='Ownership Transfer')
Fund_Release = Transition(label='Fund Release')
Dispute_Review = Transition(label='Dispute Review')
Reputation_Update = Transition(label='Reputation Update')
Fractional_Offer = Transition(label='Fractional Offer')
Secondary_Sale = Transition(label='Secondary Sale')

# Loop: Price_Adjust and Bid_Monitor interact in a loop (dynamic pricing + monitoring bids)
price_bid_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Bid_Monitor, Price_Adjust]
)

# Partial order for digital identity verification and asset verification, feeding into smart contract deployment:
identity_asset_po = StrictPartialOrder(
    nodes=[Artist_Onboard, Identity_Check, Asset_Verify]
)
identity_asset_po.order.add_edge(Artist_Onboard, Identity_Check)
identity_asset_po.order.add_edge(Identity_Check, Asset_Verify)

# Wallet linking and bid submission happen concurrently with ongoing bid monitoring and price adjusting loop:
wallet_bid_po = StrictPartialOrder(
    nodes=[Wallet_Link, Bid_Submit, price_bid_loop]
)
# Wallet link and bid submit concurrency, price_bid_loop concurrent to them (no edges)

# Auction Close follows bid submission and bid monitoring loop completion
auction_close_po = StrictPartialOrder(
    nodes=[wallet_bid_po, Auction_Close]
)
auction_close_po.order.add_edge(wallet_bid_po, Auction_Close)

# After auction close, smart contract deploy, ownership transfer, fund release happen sequentially
settlement_po = StrictPartialOrder(
    nodes=[Smart_Deploy, Ownership_Transfer, Fund_Release]
)
settlement_po.order.add_edge(Smart_Deploy, Ownership_Transfer)
settlement_po.order.add_edge(Ownership_Transfer, Fund_Release)

# Dispute review and reputation update happen after settlement concurrently with fractional offer and secondary sale (secondary sales domain)
post_auction_po = StrictPartialOrder(
    nodes=[Dispute_Review, Reputation_Update, Fractional_Offer, Secondary_Sale]
)
# Dispute Review -> Reputation Update
post_auction_po.order.add_edge(Dispute_Review, Reputation_Update)
# Fractional_Offer and Secondary_Sale concurrent, and after Reputation_Update
post_auction_po.order.add_edge(Reputation_Update, Fractional_Offer)
post_auction_po.order.add_edge(Reputation_Update, Secondary_Sale)

# Compose whole process partial order including all main phases

root = StrictPartialOrder(
    nodes=[identity_asset_po, auction_close_po, settlement_po, post_auction_po]
)
# Connect identity_asset_po to auction_close_po (auction actions after onboarding + verification)
root.order.add_edge(identity_asset_po, auction_close_po)
# Auction close to settlement sequence
root.order.add_edge(auction_close_po, settlement_po)
# Settlement to post auction activities
root.order.add_edge(settlement_po, post_auction_po)