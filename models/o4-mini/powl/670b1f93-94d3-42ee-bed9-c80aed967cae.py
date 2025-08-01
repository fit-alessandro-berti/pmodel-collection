# Generated from: 670b1f93-94d3-42ee-bed9-c80aed967cae.json
# Description: This process orchestrates the systematic fusion of ideas from disparate industries to generate breakthrough products. It begins with trend spotting across unrelated sectors, followed by interdisciplinary brainstorming sessions. Concepts are prototyped using agile sprints, then undergo cross-functional peer reviews to identify unforeseen synergies. After iterative refinements, pilot launches are conducted in niche markets to collect diverse user feedback. The insights gained inform strategic pivots and scaling decisions. Throughout, knowledge management ensures lessons learned are archived for future cycles, fostering continuous evolution and competitive advantage in rapidly shifting markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the core activities
ts = Transition(label="Trend Spotting")
im = Transition(label="Idea Mining")
bs = Transition(label="Brainstorming")
cs = Transition(label="Concept Sketch")
pb = Transition(label="Prototype Build")
sr = Transition(label="Sprint Review")
pf = Transition(label="Peer Feedback")
id_ = Transition(label="Iterate Design")
pl = Transition(label="Pilot Launch")
us = Transition(label="User Survey")
da = Transition(label="Data Analysis")
mp = Transition(label="Market Pivot")
sp = Transition(label="Scale Planning")
ka = Transition(label="Knowledge Archive")

# Define the cycle‐review activity (loop body)
cr = Transition(label="Cycle Review")

# Build the partial order for one iteration of the process (the "body" of the loop)
body = StrictPartialOrder(
    nodes=[ts, im, bs, cs, pb, sr, pf, id_, pl, us, da, mp, sp, ka]
)
# Add direct‐sequence edges
edges = [
    (ts, im), (im, bs), (bs, cs), (cs, pb), (pb, sr),
    (sr, pf), (pf, id_), (id_, pl), (pl, us), (us, da),
    (da, mp), (mp, sp), (sp, ka)
]
for src, tgt in edges:
    body.order.add_edge(src, tgt)

# Create a LOOP: do one body; then either exit or do cycle‐review then body again, etc.
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, cr])

# The loop is the root of the POWL model
root = loop