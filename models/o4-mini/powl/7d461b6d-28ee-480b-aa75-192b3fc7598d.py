# Generated from: 7d461b6d-28ee-480b-aa75-192b3fc7598d.json
# Description: This process orchestrates the collection, evaluation, and implementation of innovative ideas sourced from a global community. It begins with idea solicitation through multiple channels, followed by automated filtering and peer review to prioritize high-potential concepts. Selected ideas undergo prototyping and iterative feedback loops involving both internal experts and the crowd. Concurrently, legal assessments ensure intellectual property compliance, while resource allocation optimizes development costs. After refinement, successful prototypes are transitioned to pilot programs with continuous performance monitoring. Finally, viable innovations are scaled for full market deployment, supported by targeted marketing and post-launch evaluation to capture learnings and inform future cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ic = Transition(label='Idea Capture')
fr = Transition(label='Filter Review')
pv = Transition(label='Peer Voting')
cr = Transition(label='Concept Ranking')
pb = Transition(label='Prototype Build')
ef = Transition(label='Expert Feedback')
lc = Transition(label='Legal Check')
ra = Transition(label='Resource Assign')
pl = Transition(label='Pilot Launch')
pm = Transition(label='Performance Monitor')
mt = Transition(label='Market Test')
sp = Transition(label='Scale Plan')
mp = Transition(label='Marketing Prep')
po = Transition(label='Post Launch')
da = Transition(label='Data Analyze')

# Loop for prototyping and feedback
proto_loop = OperatorPOWL(operator=Operator.LOOP, children=[pb, ef])

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    ic, fr, pv, cr,
    proto_loop, lc, ra,
    pl, pm, mt, sp, mp, po, da
])

# Define the sequencing and concurrency
root.order.add_edge(ic,  fr)
root.order.add_edge(fr,  pv)
root.order.add_edge(pv,  cr)

# After ranking, start prototyping‐loop, legal check, and resource assign in parallel
root.order.add_edge(cr, proto_loop)
root.order.add_edge(cr, lc)
root.order.add_edge(cr, ra)

# All three must finish before pilot launch
root.order.add_edge(proto_loop, pl)
root.order.add_edge(lc,         pl)
root.order.add_edge(ra,         pl)

# Continue sequential execution
root.order.add_edge(pl, pm)
root.order.add_edge(pm, mt)
root.order.add_edge(mt, sp)
root.order.add_edge(sp, mp)
root.order.add_edge(mp, po)
root.order.add_edge(po, da)