# Generated from: 43d71985-3c41-41b1-8cda-9680ac9d5899.json
# Description: This process outlines the creation of a bespoke artisanal perfume, starting from raw material sourcing to the final personalized packaging. It involves selecting rare botanical extracts, formulating unique scent blends through iterative testing, aging the mixture to enhance aroma complexity, and conducting sensory evaluations with expert panels. The process also integrates sustainable harvesting methods, custom bottle design, and client feedback incorporation to ensure a distinct and high-quality product tailored to individual preferences. Documentation and quality assurance steps are embedded to maintain consistency and traceability throughout production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Material Sourcing')
sh = Transition(label='Sustainable Harvest')
ed = Transition(label='Extract Distill')
bt = Transition(label='Blend Testing')
sa = Transition(label='Scent Aging')
sp = Transition(label='Sensory Panel')
fr1 = Transition(label='Feedback Review')  # feedback within blend‐testing loop
fa = Transition(label='Formula Adjust')
bd = Transition(label='Bottle Design')
pp = Transition(label='Packaging Print')
bl = Transition(label='Batch Labeling')
cs = Transition(label='Client Sampling')
fr2 = Transition(label='Feedback Review')  # feedback after client sampling
qa = Transition(label='Quality Audit')
ic = Transition(label='Inventory Check')
od = Transition(label='Order Dispatch')

# 1) Build the loop for iterative blend testing:
#    Body A_seq: Blend Testing -> Scent Aging -> Sensory Panel -> Feedback Review
A_seq = StrictPartialOrder(nodes=[bt, sa, sp, fr1])
A_seq.order.add_edge(bt, sa)
A_seq.order.add_edge(sa, sp)
A_seq.order.add_edge(sp, fr1)

#    Redo B_seq: Formula Adjust
B_seq = StrictPartialOrder(nodes=[fa])

#    LOOP operator: perform A_seq, then either exit or do B_seq then A_seq again
blend_loop = OperatorPOWL(operator=Operator.LOOP, children=[A_seq, B_seq])

# 2) Build the packaging partial order:
#    Bottle Design and Packaging Print in parallel, both must precede Batch Labeling
pack = StrictPartialOrder(nodes=[bd, pp, bl])
pack.order.add_edge(bd, bl)
pack.order.add_edge(pp, bl)

# 3) Build the top‐level process partial order
root = StrictPartialOrder(
    nodes=[ms, sh, ed, blend_loop, pack, cs, fr2, qa, ic, od]
)

# Concurrency: Material Sourcing and Sustainable Harvest can happen in parallel,
# both must finish before Extract Distill
root.order.add_edge(ms, ed)
root.order.add_edge(sh, ed)

# After distillation, do the blending/testing loop
root.order.add_edge(ed, blend_loop)

# Once the scent formula is finalized, move to packaging steps
root.order.add_edge(blend_loop, pack)

# After labeling, perform client sampling and subsequent feedback review
root.order.add_edge(pack, cs)
root.order.add_edge(cs, fr2)

# Finally do quality audit, inventory check, and dispatch
root.order.add_edge(fr2, qa)
root.order.add_edge(qa, ic)
root.order.add_edge(ic, od)