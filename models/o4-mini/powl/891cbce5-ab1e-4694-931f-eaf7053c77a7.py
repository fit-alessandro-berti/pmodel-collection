# Generated from: 891cbce5-ab1e-4694-931f-eaf7053c77a7.json
# Description: This process outlines the intricate steps involved in sourcing, crafting, and delivering bespoke artisan goods. It begins with raw material scouting in remote regions, followed by quality validation using non-standardized criteria. Artisans receive personalized design briefs, enabling handcrafting with adaptive techniques. Finished items undergo multi-stage authenticity and durability testing, including community feedback loops. Packaging is customized per client preferences using eco-friendly materials. The logistics phase integrates unconventional transport methods like local courier networks and barter exchanges. Finally, a post-delivery artisan-client interaction ensures satisfaction and future collaboration, fostering a sustainable and culturally rich business ecosystem that defies mainstream mass production models.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Material Scout')
qc = Transition(label='Quality Check')
db = Transition(label='Design Brief')
aa = Transition(label='Artisan Assign')
cp = Transition(label='Crafting Phase')
mr = Transition(label='Midway Review')
at = Transition(label='Authenticity Test')
dc = Transition(label='Durability Check')
cf = Transition(label='Community Feedback')
pd = Transition(label='Package Design')
ep = Transition(label='Eco Packaging')
lc = Transition(label='Local Courier')
be = Transition(label='Barter Exchange')
delc = Transition(label='Delivery Confirm')
cfu = Transition(label='Client Followup')
sa = Transition(label='Sustainability Audit')

# Build the testing + feedback loop: run tests (A), then optionally do feedback (B) and repeat
test_seq = StrictPartialOrder(nodes=[at, dc])
test_seq.order.add_edge(at, dc)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_seq, cf])

# Build logistics choice
logistics = OperatorPOWL(operator=Operator.XOR, children=[lc, be])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    ms, qc, db, aa, cp, mr,
    feedback_loop,
    pd, ep,
    logistics,
    delc, cfu, sa
])
root.order.add_edge(ms, qc)
root.order.add_edge(qc, db)
root.order.add_edge(db, aa)
root.order.add_edge(aa, cp)
root.order.add_edge(cp, mr)
root.order.add_edge(mr, feedback_loop)
root.order.add_edge(feedback_loop, pd)
root.order.add_edge(pd, ep)
root.order.add_edge(ep, logistics)
root.order.add_edge(logistics, delc)
root.order.add_edge(delc, cfu)
root.order.add_edge(cfu, sa)