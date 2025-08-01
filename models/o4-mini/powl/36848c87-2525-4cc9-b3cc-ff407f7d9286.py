# Generated from: 36848c87-2525-4cc9-b3cc-ff407f7d9286.json
# Description: This process outlines the intricate journey of sourcing, processing, and distributing small-batch artisanal coffee beans from remote farms to specialty cafes worldwide. It involves unique steps such as local farmer engagement, micro-lot selection, hand-processing, quality cupping, eco-friendly packaging, and bespoke logistics coordination. The process emphasizes sustainability, traceability, and maintaining bean integrity throughout transportation and roasting. Each activity ensures the preservation of flavor profiles and ethical practices, resulting in a premium coffee experience for discerning consumers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities as POWL transitions
fo   = Transition(label='Farm Outreach')
bs   = Transition(label='Bean Selection')
hp   = Transition(label='Hand Picking')
isrt = Transition(label='Initial Sorting')
wp   = Transition(label='Wet Processing')
sd   = Transition(label='Sun Drying')
qc   = Transition(label='Quality Cupping')
mg   = Transition(label='Micro-lot Grading')
ep   = Transition(label='Eco Packaging')
cl   = Transition(label='Custom Labeling')
isyn = Transition(label='Inventory Sync')
sr   = Transition(label='Specialty Roasting')
ls   = Transition(label='Logistics Setup')
cd   = Transition(label='Cafe Delivery')
cf   = Transition(label='Customer Feedback')

# Build the partial order
root = StrictPartialOrder(nodes=[
    fo, bs, hp, isrt, wp, sd, qc, mg, ep, cl, isyn, sr, ls, cd, cf
])

# Sequential sourcing and processing
root.order.add_edge(fo,   bs)
root.order.add_edge(bs,   hp)
root.order.add_edge(hp,   isrt)
root.order.add_edge(isrt, wp)
root.order.add_edge(wp,   sd)
# Quality check
root.order.add_edge(sd,   qc)
root.order.add_edge(qc,   mg)
# Packaging and inventory
root.order.add_edge(mg,   ep)
root.order.add_edge(ep,   cl)
root.order.add_edge(cl,   isyn)
# Roasting and logistics can proceed in parallel after inventory sync
root.order.add_edge(isyn, sr)
root.order.add_edge(isyn, ls)
# Both roasting and logistics must complete before delivery
root.order.add_edge(sr,   cd)
root.order.add_edge(ls,   cd)
# Final feedback
root.order.add_edge(cd,   cf)