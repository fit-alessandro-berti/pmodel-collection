# Generated from: 864fda6a-c576-41a3-b8aa-748365a414c6.json
# Description: This process encompasses the intricate journey of producing and distributing artisanal cheese, starting from selecting rare milk sources, through precise fermentation and aging techniques, to packaging with bespoke materials, and finally coordinating niche market deliveries. It involves quality validation at multiple points, managing small batch variations, syncing with seasonal farm outputs, and engaging specialized transport to maintain product integrity. The process also integrates customer feedback loops for continuous refinement and limited edition releases, ensuring the cheese retains its unique character and exclusivity throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms   = Transition(label='Milk Sourcing')
qt   = Transition(label='Quality Testing')
mp   = Transition(label='Milk Pasteurize')
sc   = Transition(label='Starter Culture')
co   = Transition(label='Coagulation')
cc   = Transition(label='Curd Cutting')
wd   = Transition(label='Whey Draining')
mpr  = Transition(label='Molding Press')
sd   = Transition(label='Salting Dry')
fer  = Transition(label='Fermentation')
ac   = Transition(label='Aging Control')
qc   = Transition(label='Quality Check')
pd   = Transition(label='Packaging Design')
cw   = Transition(label='Custom Wrapping')
isyn = Transition(label='Inventory Sync')
op   = Transition(label='Order Processing')
ss   = Transition(label='Special Shipping')
cf   = Transition(label='Customer Feedback')
ba   = Transition(label='Batch Analysis')
lr   = Transition(label='Limited Release')

# Build the main packaging‐and‐shipping subprocess A
A = StrictPartialOrder(nodes=[pd, cw, isyn, op, ss])
A.order.add_edge(pd, cw)
A.order.add_edge(cw, isyn)
A.order.add_edge(isyn, op)
A.order.add_edge(op, ss)

# Build the feedback & limited‐release subprocess B
B = StrictPartialOrder(nodes=[cf, ba, lr])
B.order.add_edge(cf, ba)
B.order.add_edge(ba, lr)

# Loop: do A once, then either exit or do B and A again, etc.
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Compose the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    ms, qt, mp, sc, co, cc, wd, mpr, sd,
    fer, ac, qc,
    loop
])
# Sequential dependencies for cheese production
root.order.add_edge(ms, qt)
root.order.add_edge(qt, mp)
root.order.add_edge(mp, sc)
root.order.add_edge(sc, co)
root.order.add_edge(co, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mpr)
root.order.add_edge(mpr, sd)
root.order.add_edge(sd, fer)
root.order.add_edge(fer, ac)
root.order.add_edge(ac, qc)
# After quality check, move into the packaging‐shipping + feedback loop
root.order.add_edge(qc, loop)