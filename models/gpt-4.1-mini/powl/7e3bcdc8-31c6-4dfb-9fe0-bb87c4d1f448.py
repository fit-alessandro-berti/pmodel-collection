# Generated from: 7e3bcdc8-31c6-4dfb-9fe0-bb87c4d1f448.json
# Description: This process manages a decentralized auction platform where digital artists tokenize their artwork as NFTs and sell them using multiple cryptocurrencies. It involves verifying artist credentials, minting NFTs, setting reserve prices, enabling crypto-wallet bidding, conducting real-time bid validation on blockchain, handling automated escrow for payment security, resolving disputes via smart contracts, and finalizing ownership transfers. Additionally, the process includes dynamic fee calculations based on transaction volume, cross-platform promotion, and post-sale royalty tracking to ensure artists receive ongoing compensation for secondary sales, all while maintaining transparency and compliance with regional crypto regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artist_verify = Transition(label='Artist Verify')
nft_mint = Transition(label='NFT Mint')
price_set = Transition(label='Price Set')
wallet_link = Transition(label='Wallet Link')
bid_submit = Transition(label='Bid Submit')
bid_validate = Transition(label='Bid Validate')
escrow_lock = Transition(label='Escrow Lock')
dispute_review = Transition(label='Dispute Review')
ownership_transfer = Transition(label='Ownership Transfer')
fee_calculate = Transition(label='Fee Calculate')
promote_auction = Transition(label='Promote Auction')
royalty_track = Transition(label='Royalty Track')
compliance_check = Transition(label='Compliance Check')
sale_finalize = Transition(label='Sale Finalize')
report_generate = Transition(label='Report Generate')

# Define partial orders respecting the main flow

# Initial verification and preparation
prep = StrictPartialOrder(nodes=[artist_verify, nft_mint, price_set, wallet_link, compliance_check])
prep.order.add_edge(artist_verify, nft_mint)
prep.order.add_edge(nft_mint, price_set)
prep.order.add_edge(price_set, wallet_link)
prep.order.add_edge(wallet_link, compliance_check)

# Bidding and validation
bidding = StrictPartialOrder(nodes=[bid_submit, bid_validate])
bidding.order.add_edge(bid_submit, bid_validate)

# Escrow locking after bids validated
escrow = escrow_lock

# Dispute handling is optional and concurrent with escrow resolution before ownership transfer
dispute_choice = OperatorPOWL(operator=Operator.XOR, children=[dispute_review, SilentTransition()])

# Ownership transfer after escrow and disputing (if any)
ownership_phase = StrictPartialOrder(nodes=[escrow, dispute_choice, ownership_transfer])
ownership_phase.order.add_edge(escrow, dispute_choice)
ownership_phase.order.add_edge(dispute_choice, ownership_transfer)

# Fee calculation is dynamic and may loop with sales/refunds (model loop between fee calculation and promote auction)
fee_promotion_loop = OperatorPOWL(operator=Operator.LOOP, children=[fee_calculate, promote_auction])

# Post-sale activities: royalty tracking, sale finalizing, report generation
post_sale = StrictPartialOrder(nodes=[royalty_track, sale_finalize, report_generate])
post_sale.order.add_edge(royalty_track, sale_finalize)
post_sale.order.add_edge(sale_finalize, report_generate)

# Compose all main phases into single partial order:
all_nodes = [prep, bidding, ownership_phase, fee_promotion_loop, post_sale]

root = StrictPartialOrder(nodes=all_nodes)

# Order the phases respecting logical sequence
root.order.add_edge(prep, bidding)
root.order.add_edge(bidding, ownership_phase)
root.order.add_edge(ownership_phase, fee_promotion_loop)
root.order.add_edge(fee_promotion_loop, post_sale)