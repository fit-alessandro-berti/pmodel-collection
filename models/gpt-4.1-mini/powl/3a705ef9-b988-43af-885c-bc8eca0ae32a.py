# Generated from: 3a705ef9-b988-43af-885c-bc8eca0ae32a.json
# Description: This process manages a dynamic art auction where artworks are continuously evaluated by AI algorithms for authenticity and market trends while bidders participate both physically and virtually. The system integrates real-time sentiment analysis from social media, adjusts bidding increments based on demand elasticity, and automatically reallocates auction lots to optimize final sale prices. Post-auction, the system arranges provenance verification, coordinates logistics with specialized art handlers, and triggers personalized marketing campaigns for unsold pieces. This atypical auction process blends technology-driven valuation, multi-channel engagement, and adaptive inventory management to maximize revenue and collector satisfaction in a fluctuating art market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
AuthCheck = Transition(label='Auth Check')
TrendScan = Transition(label='Trend Scan')
SentimentMap = Transition(label='Sentiment Map')
BidAdjust = Transition(label='Bid Adjust')
LotReassign = Transition(label='Lot Reassign')
VirtualJoin = Transition(label='Virtual Join')
PriceUpdate = Transition(label='Price Update')
DemandGauge = Transition(label='Demand Gauge')
ProvenanceVerify = Transition(label='Provenance Verify')
HandlerAssign = Transition(label='Handler Assign')
MarketingPush = Transition(label='Marketing Push')
UnsoldReview = Transition(label='Unsold Review')
BuyerNotify = Transition(label='Buyer Notify')
PaymentClear = Transition(label='Payment Clear')
ShipmentPlan = Transition(label='Shipment Plan')
FeedbackCollect = Transition(label='Feedback Collect')

# Pre-auction parallel processes:
# - AI evaluation activities run in partial order with some concurrency:
#   Auth Check -> Trend Scan -> Sentiment Map run sequentially (evaluation pipeline)
eval_pipeline = StrictPartialOrder(nodes=[AuthCheck, TrendScan, SentimentMap])
eval_pipeline.order.add_edge(AuthCheck, TrendScan)
eval_pipeline.order.add_edge(TrendScan, SentimentMap)

# - Parallel to that, bidders can join both virtually and physically (represented by Virtual Join)
# We combine VirtualJoin with a partial order expressing concurrency with evaluation pipeline
pre_auction = StrictPartialOrder(nodes=[eval_pipeline, VirtualJoin])
# No edges: concurrent with the evaluation pipeline

# Auction process:
# The core loop: continuously adjust bids based on demand and market trends:
# loop body = (BidAdjust + DemandGauge + LotReassign + PriceUpdate) in partial order,
# assume BidAdjust -> DemandGauge -> LotReassign -> PriceUpdate
auction_body = StrictPartialOrder(
    nodes=[BidAdjust, DemandGauge, LotReassign, PriceUpdate])
auction_body.order.add_edge(BidAdjust, DemandGauge)
auction_body.order.add_edge(DemandGauge, LotReassign)
auction_body.order.add_edge(LotReassign, PriceUpdate)

# Loop structure: run auction_body repeatedly, exit to post-auction
auction_loop = OperatorPOWL(operator=Operator.LOOP, children=[auction_body, SilentTransition()])

# Post-auction processes:
# - ProvenanceVerify, HandlerAssign, MarketingPush, UnsoldReview in partial order with some dependencies:
#   ProvenanceVerify -> HandlerAssign
#   UnsoldReview -> MarketingPush (Unsold pieces marketing)
post_auction = StrictPartialOrder(
    nodes=[ProvenanceVerify, HandlerAssign, MarketingPush, UnsoldReview, BuyerNotify, PaymentClear, ShipmentPlan, FeedbackCollect])
post_auction.order.add_edge(ProvenanceVerify, HandlerAssign)
post_auction.order.add_edge(UnsoldReview, MarketingPush)

# Notification and payment/shipment after auction:
# BuyerNotify -> PaymentClear -> ShipmentPlan -> FeedbackCollect
post_auction.order.add_edge(BuyerNotify, PaymentClear)
post_auction.order.add_edge(PaymentClear, ShipmentPlan)
post_auction.order.add_edge(ShipmentPlan, FeedbackCollect)

# Merge notifications and provenance/logistics branches by concurrency

# Now model the overall process:

# After pre-auction (evaluation and VirtualJoin), auction loop starts, then post auction

root = StrictPartialOrder(
    nodes=[pre_auction, auction_loop, post_auction]
)
# Control flow order:
root.order.add_edge(pre_auction, auction_loop)
root.order.add_edge(auction_loop, post_auction)