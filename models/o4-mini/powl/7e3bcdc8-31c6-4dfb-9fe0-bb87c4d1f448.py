# Generated from: 7e3bcdc8-31c6-4dfb-9fe0-bb87c4d1f448.json
# Description: This process manages a decentralized auction platform where digital artists tokenize their artwork as NFTs and sell them using multiple cryptocurrencies. It involves verifying artist credentials, minting NFTs, setting reserve prices, enabling crypto-wallet bidding, conducting real-time bid validation on blockchain, handling automated escrow for payment security, resolving disputes via smart contracts, and finalizing ownership transfers. Additionally, the process includes dynamic fee calculations based on transaction volume, cross-platform promotion, and post-sale royalty tracking to ensure artists receive ongoing compensation for secondary sales, all while maintaining transparency and compliance with regional crypto regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic transitions
artist_verify     = Transition(label='Artist Verify')
compliance_check  = Transition(label='Compliance Check')
nft_mint          = Transition(label='NFT Mint')
price_set         = Transition(label='Price Set')
wallet_link       = Transition(label='Wallet Link')
bid_submit        = Transition(label='Bid Submit')
bid_validate      = Transition(label='Bid Validate')
escrow_lock       = Transition(label='Escrow Lock')
dispute_review    = Transition(label='Dispute Review')
ownership_transfer= Transition(label='Ownership Transfer')
fee_calculate     = Transition(label='Fee Calculate')
promote_auction   = Transition(label='Promote Auction')
royalty_track     = Transition(label='Royalty Track')
sale_finalize     = Transition(label='Sale Finalize')
report_generate   = Transition(label='Report Generate')

# Silent transition for exits
skip = SilentTransition()

# Build the looping bid workflow: submit -> validate -> lock, repeated until auction ends
bid_body = StrictPartialOrder(nodes=[bid_submit, bid_validate, escrow_lock])
bid_body.order.add_edge(bid_submit, bid_validate)
bid_body.order.add_edge(bid_validate, escrow_lock)
bid_loop = OperatorPOWL(operator=Operator.LOOP, children=[bid_body, skip])

# Build the dispute check: either review or skip
dispute_choice = OperatorPOWL(operator=Operator.XOR, children=[dispute_review, skip])

# Assemble the overall workflow as a partial order
root = StrictPartialOrder(nodes=[
    artist_verify, compliance_check, nft_mint, price_set, wallet_link,
    promote_auction, bid_loop, sale_finalize, dispute_choice,
    ownership_transfer, fee_calculate, royalty_track, report_generate
])

# Define the main sequential flow
root.order.add_edge(artist_verify,    compliance_check)
root.order.add_edge(compliance_check, nft_mint)
root.order.add_edge(nft_mint,         price_set)
root.order.add_edge(price_set,        wallet_link)

# After linking wallet, auction promotion can run in parallel with bidding loop
root.order.add_edge(wallet_link,      promote_auction)
root.order.add_edge(wallet_link,      bid_loop)

# Once bidding ends, finalize the sale
root.order.add_edge(bid_loop,         sale_finalize)

# After finalizing, optionally review disputes
root.order.add_edge(sale_finalize,    dispute_choice)

# Proceed with ownership transfer and post‐sale activities
root.order.add_edge(dispute_choice,   ownership_transfer)
root.order.add_edge(ownership_transfer, fee_calculate)
root.order.add_edge(fee_calculate,    royalty_track)
root.order.add_edge(royalty_track,    report_generate)