# Generated from: 958e9aea-7c34-421a-a688-ce259d3c667e.json
# Description: This process involves the sourcing, crafting, quality validation, and distribution of bespoke artisan goods. It begins with material scouting in niche markets, followed by artisan assignment based on skill compatibility. Subsequent steps include prototype creation, peer review, refinement cycles, and final approval. Once approved, goods undergo packaging with unique branding, logistics coordination for multi-modal transport, customs clearance for international shipments, and finally, delivery to exclusive retail partners. The entire process integrates feedback loops from customer insights and artisan performance metrics to ensure continual improvement and maintain the high standards expected in luxury artisan markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ms = Transition(label='Material Scout')
sm = Transition(label='Skill Match')
aa = Transition(label='Assign Artisan')
pb = Transition(label='Prototype Build')
pr = Transition(label='Peer Review')
rd = Transition(label='Refine Design')
ac = Transition(label='Approval Check')
bp = Transition(label='Brand Package')
lp = Transition(label='Logistics Plan')
tb = Transition(label='Transport Book')
cc = Transition(label='Customs Clear')
rdl = Transition(label='Retail Deliver')
cf = Transition(label='Customer Feedback')
pa = Transition(label='Performance Audit')
ci = Transition(label='Continuous Improve')

# Build the prototype‐review loop:  
#   do (Prototype Build -> Peer Review), then either exit or do Refine Design and loop again
proto_review = StrictPartialOrder(nodes=[pb, pr])
proto_review.order.add_edge(pb, pr)

loop_pr = OperatorPOWL(operator=Operator.LOOP, children=[proto_review, rd])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    ms, sm, aa,
    loop_pr,
    ac, bp, lp, tb, cc, rdl,
    cf, pa, ci
])

# Define the control-flow edges
root.order.add_edge(ms, sm)
root.order.add_edge(sm, aa)
root.order.add_edge(aa, loop_pr)
root.order.add_edge(loop_pr, ac)
root.order.add_edge(ac, bp)
root.order.add_edge(bp, lp)
root.order.add_edge(lp, tb)
root.order.add_edge(tb, cc)
root.order.add_edge(cc, rdl)

# After delivery, customer feedback and performance audit happen (in parallel)
root.order.add_edge(rdl, cf)
root.order.add_edge(rdl, pa)

# Both feedback and audit feed into continuous improvement
root.order.add_edge(cf, ci)
root.order.add_edge(pa, ci)