# Generated from: 9619ef2d-9311-44d7-9b59-a61e1ae1633e.json
# Description: This process outlines the steps involved in conducting a cryptocurrency-based art auction where digital and physical artworks are tokenized and auctioned using blockchain technology. It includes artist verification, artwork digitization, smart contract creation, bidder registration via crypto wallets, live bidding with real-time crypto payments, and post-auction token transfer. The process also handles dispute resolution through decentralized arbitration and ensures provenance tracking on the blockchain. Finally, it integrates with external shipment providers for delivering physical artworks and manages royalty payouts automatically to artists through smart contracts, ensuring transparency and security throughout the auction lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities explicitly
Artist_Verify = Transition(label='Artist Verify')
Artwork_Tokenize = Transition(label='Artwork Tokenize')
Smart_Contract = Transition(label='Smart Contract')
Bidder_Register = Transition(label='Bidder Register')
Wallet_Link = Transition(label='Wallet Link')
Reserve_Set = Transition(label='Reserve Set')
Auction_Launch = Transition(label='Auction Launch')
Live_Bidding = Transition(label='Live Bidding')
Payment_Confirm = Transition(label='Payment Confirm')
Bid_Increment = Transition(label='Bid Increment')
Dispute_Review = Transition(label='Dispute Review')
Arbitration_Call = Transition(label='Arbitration Call')
Token_Transfer = Transition(label='Token Transfer')
Royalty_Process = Transition(label='Royalty Process')
Shipment_Arrange = Transition(label='Shipment Arrange')
Provenance_Track = Transition(label='Provenance Track')

# 1. Preparation phase: Artist verification, artwork digitization, smart contract creation
prep_PO = StrictPartialOrder(nodes=[Artist_Verify, Artwork_Tokenize, Smart_Contract])
prep_PO.order.add_edge(Artist_Verify, Artwork_Tokenize)
prep_PO.order.add_edge(Artwork_Tokenize, Smart_Contract)

# 2. Bidder registration with wallet linking
registration_PO = StrictPartialOrder(nodes=[Bidder_Register, Wallet_Link])
registration_PO.order.add_edge(Bidder_Register, Wallet_Link)

# 3. Reserve setting and auction launch, after registration
reserve_auction_PO = StrictPartialOrder(nodes=[Reserve_Set, Auction_Launch])
reserve_auction_PO.order.add_edge(Reserve_Set, Auction_Launch)

# 4. Live bidding phase - loop with bidding increment and payment confirmation possible multiple times

# Bid increment and payment confirm can happen concurrently with live bidding activities but 
# we assume payment confirm depends on bid increments, and bid increments depend on live bidding initiated

# Model the live bidding loop:
# Loop structure:
# A = Live_Bidding + options for Bid Increment and Payment Confirm before next iteration or exit
# We can model the loop body as a partial order where Bid Increment-->Payment Confirm

bid_loop_body_PO = StrictPartialOrder(nodes=[Bid_Increment, Payment_Confirm])
bid_loop_body_PO.order.add_edge(Bid_Increment, Payment_Confirm)

# Compose the loop body as PO of Live_Bidding and bid_loop_body_PO nodes concurrent
loop_body_nodes = [Live_Bidding, bid_loop_body_PO]
# We need to create a PO over these:
loop_body_PO = StrictPartialOrder(nodes=loop_body_nodes)
# No order edges: Live_Bidding concurrent with bid_loop_body_PO (Bid Increment -> Payment Confirm)
# This allows Live_Bidding and the bid increments+payment to proceed interleaved partially ordered

# Loop: execute loop_body_PO, then choose exit or repeat
bidding_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body_PO, SilentTransition()]) 
# As per definition, LOOP(A,B): execute A, then choose to exit or execute B then A again
# Here B is silent transition (tau) to allow exit (no extra behavior after first run)

# 5. After loop, possible dispute resolution or directly token transfer
# Dispute resolution: choice between dispute resolution or skip
dispute_PO = StrictPartialOrder(nodes=[Dispute_Review, Arbitration_Call])
dispute_PO.order.add_edge(Dispute_Review, Arbitration_Call)

dispute_xor = OperatorPOWL(operator=Operator.XOR, children=[dispute_PO, SilentTransition()])

# 6. Token transfer depends on dispute resolution outcome
# Token Transfer --> Royalty Process
token_royalty_PO = StrictPartialOrder(nodes=[Token_Transfer, Royalty_Process])
token_royalty_PO.order.add_edge(Token_Transfer, Royalty_Process)

# 7. Shipment arrange and provenance track concurrent after royalties
shipment_provenance_PO = StrictPartialOrder(nodes=[Shipment_Arrange, Provenance_Track])
# No order edges => concurrent

# Compose the post-bidding process PO:
post_bidding_PO = StrictPartialOrder(
    nodes=[dispute_xor, token_royalty_PO, shipment_provenance_PO]
)
# Ordering:
# dispute_xor before token_royalty_PO (token transfer after dispute)
post_bidding_PO.order.add_edge(dispute_xor, token_royalty_PO)
# token_royalty_PO before shipment_provenance_PO
post_bidding_PO.order.add_edge(token_royalty_PO, shipment_provenance_PO)

# 8. Combine all major phases in partial order
root_nodes = [prep_PO, registration_PO, reserve_auction_PO, bidding_loop, post_bidding_PO]

root = StrictPartialOrder(nodes=root_nodes)

# Set orders among main phases:
# Preparation before registration
root.order.add_edge(prep_PO, registration_PO)
# registration before reserve & auction launch
root.order.add_edge(registration_PO, reserve_auction_PO)
# reserve & auction launch before bidding loop
root.order.add_edge(reserve_auction_PO, bidding_loop)
# bidding loop before post bidding
root.order.add_edge(bidding_loop, post_bidding_PO)