# Generated from: 9103e96d-4d03-4c25-9a67-47708fc233bf.json
# Description: This process involves the intricate creation of bespoke artisanal perfumes, combining rare natural ingredients sourced globally with advanced blending techniques. It starts with raw material selection, followed by scent profiling, experimental formulation, and iterative refinement. Quality assessments are performed through sensory evaluation panels and chemical analysis to ensure complexity and harmony. Packaging design integrates sustainable materials while reflecting the brand identity. Finally, limited batch production is coordinated with exclusive distribution channels targeting niche luxury markets, ensuring each perfume embodies uniqueness and craftsmanship in every bottle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Material Sourcing')
sp = Transition(label='Scent Profiling')
fd = Transition(label='Formula Drafting')
bt = Transition(label='Blend Testing')
sens = Transition(label='Sensory Panel')
chem = Transition(label='Chemical Analysis')
rl = Transition(label='Refinement Loop')
sc = Transition(label='Stability Check')
pd = Transition(label='Packaging Design')
la = Transition(label='Label Approval')
bm = Transition(label='Batch Mixing')
qa = Transition(label='Quality Audit')
le = Transition(label='Limited Edition')
ds = Transition(label='Distribution Setup')
ml = Transition(label='Market Launch')
cf = Transition(label='Customer Feedback')

# Define the loop body A: initial drafting and testing
A = StrictPartialOrder(nodes=[fd, bt])
A.order.add_edge(fd, bt)

# Define the loop body B: assessments and refinement
B = StrictPartialOrder(nodes=[sens, chem, rl])
B.order.add_edge(sens, chem)
B.order.add_edge(chem, rl)

# LOOP operator for iterative refinement
loop_refine = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[ms, sp, loop_refine, sc, pd, la, bm, qa, le, ds, ml, cf]
)

# Define the global control‐flow
root.order.add_edge(ms, sp)
root.order.add_edge(sp, loop_refine)
root.order.add_edge(loop_refine, sc)
root.order.add_edge(sc, pd)
root.order.add_edge(pd, la)
root.order.add_edge(la, bm)
root.order.add_edge(bm, qa)
root.order.add_edge(qa, le)
root.order.add_edge(le, ds)
root.order.add_edge(ds, ml)
root.order.add_edge(ml, cf)