# Generated from: 0618ba6c-cd5e-4205-9b89-fd41ef27e339.json
# Description: This process outlines a dynamic and iterative approach to entering new international markets where traditional linear strategies are insufficient. It combines real-time market sensing, rapid prototyping of localized offerings, continuous stakeholder feedback loops, regulatory navigation, and adaptive resource allocation to optimize market fit and minimize entry risks. The process involves cross-functional collaboration between marketing, legal, product development, and local partners, ensuring responsiveness to emerging challenges and opportunities. It requires constant data-driven adjustments to the go-to-market plan based on evolving customer preferences, competitor moves, and regulatory changes, ultimately enabling faster and more sustainable market penetration in volatile environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ms   = Transition(label='Market Scan')
rm   = Transition(label='Regulatory Map')
ss   = Transition(label='Stakeholder Sync')
ra   = Transition(label='Risk Assess')
lp   = Transition(label='Local Partner')
pb   = Transition(label='Prototype Build')
tl   = Transition(label='Test Launch')
cp   = Transition(label='Customer Poll')
dr   = Transition(label='Data Review')
fl   = Transition(label='Feedback Loop')
pa   = Transition(label='Plan Adjust')
rs   = Transition(label='Resource Shift')
cc   = Transition(label='Compliance Check')
cw   = Transition(label='Competitor Watch')
fr   = Transition(label='Final Rollout')
pl   = Transition(label='Post Launch')

# Build the iterative loop:
#   A = prototype → test launch → customer poll → data review
A = StrictPartialOrder(nodes=[pb, tl, cp, dr])
A.order.add_edge(pb, tl)
A.order.add_edge(tl, cp)
A.order.add_edge(cp, dr)

#   B = feedback loop → plan adjust → compliance check → resource shift
B = StrictPartialOrder(nodes=[fl, pa, cc, rs])
B.order.add_edge(fl, pa)
B.order.add_edge(pa, cc)
B.order.add_edge(cc, rs)

loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Assemble the full process in a single partial order
root = StrictPartialOrder(
    nodes=[ms, rm, cw, ss, lp, ra, loop, fr, pl]
)

# Initial sensing & mapping run in parallel, then stakeholder & partner sync
for init in [ms, rm, cw]:
    root.order.add_edge(init, ss)
    root.order.add_edge(init, lp)

# After sync, perform risk assessment, then enter the iterative loop
root.order.add_edge(ss, ra)
root.order.add_edge(lp, ra)
root.order.add_edge(ra, loop)

# Upon loop exit, do the final rollout and post‐launch review
root.order.add_edge(loop, fr)
root.order.add_edge(fr, pl)