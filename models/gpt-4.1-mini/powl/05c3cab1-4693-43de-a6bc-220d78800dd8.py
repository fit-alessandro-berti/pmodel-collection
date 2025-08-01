# Generated from: 05c3cab1-4693-43de-a6bc-220d78800dd8.json
# Description: This process governs a dynamic art auction platform where artworks are not only bid on traditionally but also undergo adaptive revaluation based on real-time sentiment analysis from social media, expert reviews, and collector interest. The process integrates AI-driven appraisal updates and selective artist feedback loops, allowing bidders to adjust their offers as the perceived value of the artwork evolves during the auction. Additionally, it incorporates provenance verification and fractional ownership settlement, enabling multiple parties to co-invest in pieces with transparent ownership records. This atypical auction model blends technology, market psychology, and collaborative financing to create a fluid, multi-dimensional marketplace experience.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
initiate_auction = Transition(label='Initiate Auction')
upload_artwork = Transition(label='Upload Artwork')
verify_provenance = Transition(label='Verify Provenance')
analyze_sentiment = Transition(label='Analyze Sentiment')
update_appraisal = Transition(label='Update Appraisal')
notify_experts = Transition(label='Notify Experts')
collect_feedback = Transition(label='Collect Feedback')
broadcast_auction = Transition(label='Broadcast Auction')
monitor_bids = Transition(label='Monitor Bids')
recalculate_value = Transition(label='Recalculate Value')
notify_bidders = Transition(label='Notify Bidders')
adjust_offers = Transition(label='Adjust Offers')
confirm_ownership = Transition(label='Confirm Ownership')
process_payments = Transition(label='Process Payments')
issue_certificates = Transition(label='Issue Certificates')
enable_fractional = Transition(label='Enable Fractional')
close_auction = Transition(label='Close Auction')

skip = SilentTransition()

# Feedback loop for artist feedback and appraisal update:
# LOOP( [Notify Experts + Collect Feedback], [Update Appraisal] )
# Construct this loop as * (A, B):
# A = choice of collecting feedback or skip (simulating optional artist feedback)
# B = update appraisal + choice: continue loop or exit

# Notify Experts -> Collect Feedback as partial order
notify_and_collect = StrictPartialOrder(nodes=[notify_experts, collect_feedback])
notify_and_collect.order.add_edge(notify_experts, collect_feedback)

# In the loop construct, "A" is notify_and_collect,
# "B" is update_appraisal before looping again
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[notify_and_collect, update_appraisal])

# Sentiment analysis and appraisal update partial order:
# Analyze Sentiment --> (feedback_loop) --> Notify Bidders
sentiment_and_feedback = StrictPartialOrder(nodes=[analyze_sentiment, feedback_loop, notify_bidders])
sentiment_and_feedback.order.add_edge(analyze_sentiment, feedback_loop)
sentiment_and_feedback.order.add_edge(feedback_loop, notify_bidders)

# Adjustable offers loop: bidders monitor bids, recalculate value, notify bidders, adjust offers repeatedly until auction closes
# This can be a loop on [Monitor Bids, Recalculate Value, Notify Bidders, Adjust Offers]
# To fit * (A,B), let's split as:
# A: monitor -> recalc -> notify -> adjust (partial order)
# B: silent skip (to keep the loop simple, no extra activity)
adjust_offers_seq = StrictPartialOrder(nodes=[monitor_bids, recalculate_value, notify_bidders, adjust_offers])
adjust_offers_seq.order.add_edge(monitor_bids, recalculate_value)
adjust_offers_seq.order.add_edge(recalculate_value, notify_bidders)
adjust_offers_seq.order.add_edge(notify_bidders, adjust_offers)

adjust_offers_loop = OperatorPOWL(operator=Operator.LOOP, children=[adjust_offers_seq, skip])

# Provenance verification and fractional ownership partial order:
# Verify Provenance --> Confirm Ownership --> Enable Fractional --> Process Payments --> Issue Certificates
provenance_flow = StrictPartialOrder(nodes=[
    verify_provenance, confirm_ownership, enable_fractional, process_payments, issue_certificates])
provenance_flow.order.add_edge(verify_provenance, confirm_ownership)
provenance_flow.order.add_edge(confirm_ownership, enable_fractional)
provenance_flow.order.add_edge(enable_fractional, process_payments)
provenance_flow.order.add_edge(process_payments, issue_certificates)

# Initial auction setup partial order:
# Initiate Auction --> Upload Artwork --> Verify Provenance
initial_setup = StrictPartialOrder(nodes=[initiate_auction, upload_artwork, verify_provenance])
initial_setup.order.add_edge(initiate_auction, upload_artwork)
initial_setup.order.add_edge(upload_artwork, verify_provenance)

# Broadcast Auction can only start after Upload Artwork (artwork info ready)
# Broadcast Auction and provenance flow can run concurrently after verify provenance
# Let's create a partial order for broadcast and provenance flow, both depending on verify_provenance

broadcast_and_provenance = StrictPartialOrder(nodes=[broadcast_auction, provenance_flow])
broadcast_and_provenance.order.add_edge(broadcast_auction, provenance_flow)  # actually this would force broadcast before provenance, but both can be concurrent after verify provenance,
# so do not add edge broadcast -> provenance_flow. Instead create a PO with both nodes and add edges from verify provenance to both.

# Instead, create a root partial order with:
# initial_setup nodes + broadcast_auction + provenance_flow + sentiment_and_feedback + feedback_loop + adjust_offers_loop + close_auction
# Add edges accordingly:
# upload_artwork --> broadcast_auction (broadcast can start after artwork upload)
# verify_provenance --> provenance_flow (already includes verify provenance inside, so skip adding edge)
# broadcast_auction & provenance_flow run concurrently after upload_artwork + verify_provenance
# broadcast_auction --> sentiment_and_feedback --> adjust_offers_loop --> close_auction

# We have verify_provenance inside provenance_flow, so to only reference "provenance_flow" as node, it should not contain verify_provenance 
# So separate verify_provenance from provenance_flow:

# Let's redefine:
# initial_setup is Initiate Auction --> Upload Artwork --> Verify Provenance
# provenance_flow_wihout_verify = Confirm Ownership --> Enable Fractional --> Process Payments --> Issue Certificates
provenance_subflow = StrictPartialOrder(nodes=[
    confirm_ownership, enable_fractional, process_payments, issue_certificates])
provenance_subflow.order.add_edge(confirm_ownership, enable_fractional)
provenance_subflow.order.add_edge(enable_fractional, process_payments)
provenance_subflow.order.add_edge(process_payments, issue_certificates)

# Now the full flow:
# After Verify Provenance completes, provenance_subflow starts
# Broadcast Auction can start after Upload Artwork (parallel to verify_provenance)
# Sentiment and feedback depend on broadcast_auction
# Adjust offers loop depends on sentiment and feedback
# Close Auction depends on adjust offers loop and provenance_subflow

root = StrictPartialOrder(nodes=[
    # initial_setup nodes
    initiate_auction, upload_artwork, verify_provenance,
    # other parts
    broadcast_auction,
    provenance_subflow,
    sentiment_and_feedback,
    adjust_offers_loop,
    close_auction,
    feedback_loop  # feedback_loop is used inside sentiment_and_feedback but also as explicit node
])

# Order edges

# initial setup order
root.order.add_edge(initiate_auction, upload_artwork)
root.order.add_edge(upload_artwork, verify_provenance)

# broadcast_auction after upload_artwork
root.order.add_edge(upload_artwork, broadcast_auction)

# provenance_subflow after verify_provenance
root.order.add_edge(verify_provenance, provenance_subflow)

# sentiment_and_feedback after broadcast_auction
root.order.add_edge(broadcast_auction, sentiment_and_feedback)

# adjust_offers_loop after sentiment_and_feedback
root.order.add_edge(sentiment_and_feedback, adjust_offers_loop)

# close_auction after adjust_offers_loop and provenance_subflow
root.order.add_edge(adjust_offers_loop, close_auction)
root.order.add_edge(provenance_subflow, close_auction)