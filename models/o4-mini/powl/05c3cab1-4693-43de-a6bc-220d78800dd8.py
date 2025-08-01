# Generated from: 05c3cab1-4693-43de-a6bc-220d78800dd8.json
# Description: This process governs a dynamic art auction platform where artworks are not only bid on traditionally but also undergo adaptive revaluation based on real-time sentiment analysis from social media, expert reviews, and collector interest. The process integrates AI-driven appraisal updates and selective artist feedback loops, allowing bidders to adjust their offers as the perceived value of the artwork evolves during the auction. Additionally, it incorporates provenance verification and fractional ownership settlement, enabling multiple parties to co-invest in pieces with transparent ownership records. This atypical auction model blends technology, market psychology, and collaborative financing to create a fluid, multi-dimensional marketplace experience.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
t_initiate      = Transition(label='Initiate Auction')
t_upload        = Transition(label='Upload Artwork')
t_verify        = Transition(label='Verify Provenance')
t_broadcast     = Transition(label='Broadcast Auction')
t_monitor       = Transition(label='Monitor Bids')
t_analyze       = Transition(label='Analyze Sentiment')
t_notify_exp    = Transition(label='Notify Experts')
t_collect       = Transition(label='Collect Feedback')
t_update        = Transition(label='Update Appraisal')
t_recalc        = Transition(label='Recalculate Value')
t_notify_bid    = Transition(label='Notify Bidders')
t_adjust        = Transition(label='Adjust Offers')
t_confirm       = Transition(label='Confirm Ownership')
t_pay           = Transition(label='Process Payments')
t_issue         = Transition(label='Issue Certificates')
t_fraction      = Transition(label='Enable Fractional')
t_close         = Transition(label='Close Auction')

# Silent transition for loop exit
skip = SilentTransition()

# Define the appraisal‐adjustment cycle (to be repeated in a loop)
appraisal_cycle = StrictPartialOrder(nodes=[
    t_analyze, t_notify_exp, t_collect, t_update,
    t_recalc, t_notify_bid, t_adjust
])
appraisal_cycle.order.add_edge(t_analyze,    t_notify_exp)
appraisal_cycle.order.add_edge(t_analyze,    t_collect)
appraisal_cycle.order.add_edge(t_notify_exp, t_update)
appraisal_cycle.order.add_edge(t_collect,    t_update)
appraisal_cycle.order.add_edge(t_update,     t_recalc)
appraisal_cycle.order.add_edge(t_recalc,     t_notify_bid)
appraisal_cycle.order.add_edge(t_notify_bid, t_adjust)

# Loop wrapper: repeat the appraisal_cycle until a silent exit occurs
loop = OperatorPOWL(operator=Operator.LOOP, children=[appraisal_cycle, skip])

# Define the settlement phase after the auction closes
settlement = StrictPartialOrder(nodes=[
    t_confirm, t_pay, t_issue, t_fraction
])
settlement.order.add_edge(t_confirm, t_pay)
settlement.order.add_edge(t_pay,     t_issue)
settlement.order.add_edge(t_issue,   t_fraction)

# Root partial order combining all phases
root = StrictPartialOrder(nodes=[
    t_initiate, t_upload, t_verify,
    t_broadcast, t_monitor, loop,
    settlement, t_close
])
root.order.add_edge(t_initiate,  t_upload)
root.order.add_edge(t_upload,    t_verify)
root.order.add_edge(t_verify,    t_broadcast)
root.order.add_edge(t_verify,    t_monitor)
root.order.add_edge(t_verify,    loop)
root.order.add_edge(loop,        settlement)
root.order.add_edge(settlement,  t_close)