# Generated from: b841d47f-8306-4b51-ab7b-957b6143a25f.json
# Description: This process involves the intricate creation of bespoke artisanal perfumes by blending rare natural essences through a series of highly specialized steps. Starting with ingredient sourcing from remote locations, the process continues through extraction, scent profiling, and iterative blending, incorporating sensory evaluations and stability testing. Packaging is customized for each batch with handcrafted bottles and personalized labels, followed by targeted marketing to niche luxury clients. The entire workflow requires coordination between botanists, chemists, and artisans to ensure each fragrance is unique, consistent, and meets high-quality standards before distribution to exclusive retail partners or direct clients.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
tSource = Transition(label="Scent Sourcing")
tExtr = Transition(label="Essence Extract")
tProf = Transition(label="Profile Scents")

tBlend = Transition(label="Blend Trial")
tSens = Transition(label="Sensory Test")
tStab = Transition(label="Stability Check")
tAdjust = Transition(label="Batch Adjust")

tBottle = Transition(label="Bottle Craft")
tLabel = Transition(label="Label Design")
tPack = Transition(label="Package Assemble")

tQA = Transition(label="Quality Audit")

tConsult = Transition(label="Client Consult")
tMarketing = Transition(label="Marketing Prep")

tOrder = Transition(label="Order Manage")
tShip = Transition(label="Ship Product")
tFeedback = Transition(label="Feedback Review")

# Build the redo‐loop body: sensory test → stability check → batch adjust
redo = StrictPartialOrder(nodes=[tSens, tStab, tAdjust])
redo.order.add_edge(tSens, tStab)
redo.order.add_edge(tStab, tAdjust)

# Loop: Blend Trial, then either exit or do (sensory→stability→adjust) and Blend Trial again
loop = OperatorPOWL(operator=Operator.LOOP, children=[tBlend, redo])

# Exclusive choice of distribution channels after quality audit
xorDist = OperatorPOWL(operator=Operator.XOR, children=[tConsult, tMarketing])

# Assemble the full partial order
root = StrictPartialOrder(
    nodes=[
        tSource,
        tExtr,
        tProf,
        loop,
        tBottle,
        tLabel,
        tPack,
        tQA,
        xorDist,
        tOrder,
        tShip,
        tFeedback,
    ]
)
root.order.add_edge(tSource, tExtr)
root.order.add_edge(tExtr, tProf)
root.order.add_edge(tProf, loop)

root.order.add_edge(loop, tBottle)
root.order.add_edge(tBottle, tLabel)
root.order.add_edge(tLabel, tPack)
root.order.add_edge(tPack, tQA)

root.order.add_edge(tQA, xorDist)
root.order.add_edge(xorDist, tOrder)

root.order.add_edge(tOrder, tShip)
root.order.add_edge(tShip, tFeedback)