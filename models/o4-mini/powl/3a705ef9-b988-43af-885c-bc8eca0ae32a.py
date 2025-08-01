# Generated from: 3a705ef9-b988-43af-885c-bc8eca0ae32a.json
# Description: This process manages a dynamic art auction where artworks are continuously evaluated by AI algorithms for authenticity and market trends while bidders participate both physically and virtually. The system integrates real-time sentiment analysis from social media, adjusts bidding increments based on demand elasticity, and automatically reallocates auction lots to optimize final sale prices. Post-auction, the system arranges provenance verification, coordinates logistics with specialized art handlers, and triggers personalized marketing campaigns for unsold pieces. This atypical auction process blends technology-driven valuation, multi-channel engagement, and adaptive inventory management to maximize revenue and collector satisfaction in a fluctuating art market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
auth_check       = Transition(label='Auth Check')
trend_scan       = Transition(label='Trend Scan')
sentiment_map    = Transition(label='Sentiment Map')
demand_gauge     = Transition(label='Demand Gauge')
bid_adjust       = Transition(label='Bid Adjust')
price_update     = Transition(label='Price Update')
lot_reassign     = Transition(label='Lot Reassign')
virtual_join     = Transition(label='Virtual Join')
provenance_verify= Transition(label='Provenance Verify')
handler_assign   = Transition(label='Handler Assign')
unsold_review    = Transition(label='Unsold Review')
marketing_push   = Transition(label='Marketing Push')
buyer_notify     = Transition(label='Buyer Notify')
payment_clear    = Transition(label='Payment Clear')
shipment_plan    = Transition(label='Shipment Plan')
feedback_collect = Transition(label='Feedback Collect')

# 1) One auction‐round evaluation: concurrent checks + demand→bid→price sequence
eval_round = StrictPartialOrder(nodes=[
    auth_check,
    trend_scan,
    sentiment_map,
    demand_gauge,
    bid_adjust,
    price_update
])
# demand gauge must precede bid adjust, which must precede price update
eval_round.order.add_edge(demand_gauge, bid_adjust)
eval_round.order.add_edge(bid_adjust, price_update)

# 2) Loop: perform one evaluation round, then optionally reassign lots and repeat
loop_round = OperatorPOWL(
    operator=Operator.LOOP,
    children=[eval_round, lot_reassign]
)

# 3) Post‐auction “sold” flow
sold_flow = StrictPartialOrder(nodes=[
    buyer_notify,
    payment_clear,
    shipment_plan
])
sold_flow.order.add_edge(buyer_notify, payment_clear)
sold_flow.order.add_edge(payment_clear, shipment_plan)

# 4) Post‐auction “unsold” flow
unsold_flow = StrictPartialOrder(nodes=[
    unsold_review,
    marketing_push
])
unsold_flow.order.add_edge(unsold_review, marketing_push)

# 5) Choice between sold vs. unsold post‐auction branches
post_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[sold_flow, unsold_flow]
)

# 6) Assemble the root POWL: join → loop rounds → provenance & handler → choice → feedback
root = StrictPartialOrder(nodes=[
    virtual_join,
    loop_round,
    provenance_verify,
    handler_assign,
    post_choice,
    feedback_collect
])
root.order.add_edge(virtual_join,    loop_round)
root.order.add_edge(loop_round,      provenance_verify)
root.order.add_edge(loop_round,      handler_assign)
root.order.add_edge(provenance_verify, post_choice)
root.order.add_edge(handler_assign,    post_choice)
root.order.add_edge(post_choice,       feedback_collect)