# Generated from: fe4e062d-1644-4a6d-bea0-a3f0c98d9403.json
# Description: This process involves the intricate creation of custom artisan perfumes tailored to individual client preferences. Starting from scent profiling, raw ingredient sourcing, and quality assessment, it moves through experimental blending, maturation cycles, and sensory evaluation by expert panels. The process incorporates iterative refinement and stability testing to ensure product consistency. Packaging design and limited edition batch coordination add exclusivity, while compliance checks and market feedback loops optimize the final offering. This atypical process merges creativity, chemistry, and customer collaboration to deliver unique fragrance experiences.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity nodes (separate instances for repeated activities in loops)
cp = Transition(label='Client Profiling')
isrc = Transition(label='Ingredient Sourcing')
qc = Transition(label='Quality Check')
be1 = Transition(label='Blend Experiment')

mc = Transition(label='Maturation Cycle')
sp = Transition(label='Sensory Panel')
refine = Transition(label='Refinement Loop')
be2 = Transition(label='Blend Experiment')  # for the loop body

st = Transition(label='Stability Test')

pd = Transition(label='Packaging Design')
bc = Transition(label='Batch Coordination')

ca = Transition(label='Compliance Audit')

ms = Transition(label='Market Survey')
fr = Transition(label='Feedback Review')

of = Transition(label='Order Finalize')
dp = Transition(label='Distribution Plan')
iu = Transition(label='Inventory Update')

# Loop for iterative blending refinement: body = BE2 -> MC -> SP, redo = Refinement Loop
blend_refine_body = StrictPartialOrder(nodes=[be2, mc, sp])
blend_refine_body.order.add_edge(be2, mc)
blend_refine_body.order.add_edge(mc, sp)
loop_refine = OperatorPOWL(operator=Operator.LOOP, children=[blend_refine_body, refine])

# Loop for market feedback: body = MS -> FR, redo = FR
market_body = StrictPartialOrder(nodes=[ms, fr])
market_body.order.add_edge(ms, fr)
loop_market = OperatorPOWL(operator=Operator.LOOP, children=[market_body, fr])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    cp, isrc, qc, be1,
    loop_refine,    # iterative blending/refinement
    st,
    pd, bc,         # concurrent exclusivity steps
    ca,
    loop_market,    # market feedback loop
    of, dp, iu
])

# Initial sequencing: CP -> IS -> QC -> BE1 -> loop_refine -> ST
root.order.add_edge(cp, isrc)
root.order.add_edge(isrc, qc)
root.order.add_edge(qc, be1)
root.order.add_edge(be1, loop_refine)
root.order.add_edge(loop_refine, st)

# After stability test, packaging design and batch coordination in parallel
root.order.add_edge(st, pd)
root.order.add_edge(st, bc)

# After both PD and BC, compliance audit
root.order.add_edge(pd, ca)
root.order.add_edge(bc, ca)

# After compliance audit, market feedback loop, then finalization steps
root.order.add_edge(ca, loop_market)
root.order.add_edge(loop_market, of)
root.order.add_edge(of, dp)
root.order.add_edge(dp, iu)