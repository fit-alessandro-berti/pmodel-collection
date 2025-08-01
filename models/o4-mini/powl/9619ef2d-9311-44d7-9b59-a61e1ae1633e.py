# Generated from: 9619ef2d-9311-44d7-9b59-a61e1ae1633e.json
# Description: This process outlines the steps involved in conducting a cryptocurrency-based art auction where digital and physical artworks are tokenized and auctioned using blockchain technology. It includes artist verification, artwork digitization, smart contract creation, bidder registration via crypto wallets, live bidding with real-time crypto payments, and post-auction token transfer. The process also handles dispute resolution through decentralized arbitration and ensures provenance tracking on the blockchain. Finally, it integrates with external shipment providers for delivering physical artworks and manages royalty payouts automatically to artists through smart contracts, ensuring transparency and security throughout the auction lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
t_verify        = Transition(label='Artist Verify')
t_tokenize      = Transition(label='Artwork Tokenize')
t_contract      = Transition(label='Smart Contract')
t_reserve       = Transition(label='Reserve Set')
t_launch        = Transition(label='Auction Launch')
t_reg           = Transition(label='Bidder Register')
t_link          = Transition(label='Wallet Link')
t_live          = Transition(label='Live Bidding')
t_increment     = Transition(label='Bid Increment')
t_payment       = Transition(label='Payment Confirm')
t_dispute       = Transition(label='Dispute Review')
t_arbitrate     = Transition(label='Arbitration Call')
t_transfer      = Transition(label='Token Transfer')
t_royalty       = Transition(label='Royalty Process')
t_provenance    = Transition(label='Provenance Track')
t_shipment      = Transition(label='Shipment Arrange')

# Silent transition for loop exit / choice skip
skip = SilentTransition()

# 1) Build the live‐bidding loop body: Bid Increment -> Payment Confirm
bidding_body = StrictPartialOrder(nodes=[t_increment, t_payment])
bidding_body.order.add_edge(t_increment, t_payment)
# LOOP(children=[A, B]) executes A, then either exits or executes B then A again.
bidding_loop = OperatorPOWL(operator=Operator.LOOP, children=[bidding_body, skip])

# 2) Build the dispute‐resolution choice: either go through dispute sequence or skip
dispute_seq = StrictPartialOrder(nodes=[t_dispute, t_arbitrate])
dispute_seq.order.add_edge(t_dispute, t_arbitrate)
dispute_choice = OperatorPOWL(operator=Operator.XOR, children=[dispute_seq, skip])

# 3) Assemble the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        t_verify,
        t_tokenize,
        t_contract,
        t_reserve,
        t_launch,
        t_reg,
        t_link,
        t_live,
        bidding_loop,
        dispute_choice,
        t_transfer,
        t_royalty,
        t_provenance,
        t_shipment
    ]
)

# 4) Declare the control‐flow dependencies
root.order.add_edge(t_verify,    t_tokenize)
root.order.add_edge(t_tokenize,  t_contract)
root.order.add_edge(t_contract,  t_reserve)
root.order.add_edge(t_reserve,   t_launch)
root.order.add_edge(t_launch,    t_reg)
root.order.add_edge(t_reg,       t_link)
root.order.add_edge(t_link,      t_live)
root.order.add_edge(t_live,      bidding_loop)
root.order.add_edge(bidding_loop, dispute_choice)
root.order.add_edge(dispute_choice, t_transfer)
root.order.add_edge(t_transfer,  t_royalty)
root.order.add_edge(t_royalty,   t_provenance)
root.order.add_edge(t_provenance, t_shipment)