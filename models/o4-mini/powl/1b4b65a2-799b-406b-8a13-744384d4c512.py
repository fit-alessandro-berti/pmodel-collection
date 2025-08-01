# Generated from: 1b4b65a2-799b-406b-8a13-744384d4c512.json
# Description: This process orchestrates the development of breakthrough innovations by integrating multiple industry perspectives, combining technological scouting, cross-sector brainstorming, rapid prototyping, and iterative validation with external ecosystem partners. It involves continuous feedback loops between R&D, market analysis, and legal compliance to ensure novel solutions meet regulatory standards and market needs. The workflow emphasizes adaptive resource allocation, risk assessment, and knowledge transfer across departments to accelerate time-to-market while maintaining quality and sustainability standards, ultimately fostering a culture of collaborative creativity within complex organizational structures.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ts = Transition(label='Tech Scouting')
ih = Transition(label='Idea Harvest')
pa = Transition(label='Partner Align')
cs = Transition(label='Concept Sketch')
rm1 = Transition(label='Resource Map')
ra1 = Transition(label='Risk Assess')
pb = Transition(label='Prototype Build')
ut = Transition(label='User Testing')
fl = Transition(label='Feedback Loop')
idg = Transition(label='Iterate Design')
ks = Transition(label='Knowledge Share')
ba = Transition(label='Budget Adjust')
rm2 = Transition(label='Resource Map')    # second instance for the iterative loop
ra2 = Transition(label='Risk Assess')     # second instance for the iterative loop
lr = Transition(label='Legal Review')
ms = Transition(label='Market Scan')
lp = Transition(label='Launch Prep')
pl = Transition(label='Post Launch')
sa = Transition(label='Sustain Audit')

# Define the core iterative cycle: always do A, then either exit or do B then A again
# A = Prototype Build -> User Testing -> Feedback Loop
A = StrictPartialOrder(nodes=[pb, ut, fl])
A.order.add_edge(pb, ut)
A.order.add_edge(ut, fl)

# B = Iterate Design -> Knowledge Share -> Budget Adjust -> Resource Map -> Risk Assess
B = StrictPartialOrder(nodes=[idg, ks, ba, rm2, ra2])
B.order.add_edge(idg, ks)
B.order.add_edge(ks, ba)
B.order.add_edge(ba, rm2)
B.order.add_edge(rm2, ra2)

# Loop node capturing the feedback-driven iterations
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    ts, ih, pa, cs, rm1, ra1,
    loop,
    lr, ms,
    lp, pl, sa
])

# Sequence before entering the loop
root.order.add_edge(ts, ih)
root.order.add_edge(ih, pa)
root.order.add_edge(pa, cs)
root.order.add_edge(cs, rm1)
root.order.add_edge(rm1, ra1)
root.order.add_edge(ra1, loop)

# After loop: legal and market compliance in parallel, both must complete before launch prep
root.order.add_edge(loop, lr)
root.order.add_edge(loop, ms)
root.order.add_edge(lr, lp)
root.order.add_edge(ms, lp)

# Final launch and post‐launch activities
root.order.add_edge(lp, pl)
root.order.add_edge(pl, sa)