# Generated from: 486e1a30-a03b-4d03-a179-eb46555978a0.json
# Description: This process involves launching a new product specifically tailored for emerging markets where infrastructure, consumer behavior, and regulatory environments differ significantly from developed regions. It starts with localized market research and cultural adaptation, followed by modular product design to accommodate varying supply chain constraints. Parallel activities include securing local partnerships, navigating complex import regulations, and performing risk assessments on geopolitical factors. Marketing strategies are co-created with regional influencers and pilot campaigns are run in select urban and rural areas. Continuous feedback loops ensure iterative product refinement. The process culminates in scalable distribution network setup, compliance audits, and cross-border payment integration, ensuring a sustainable entry and growth within these dynamic markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
mr = Transition(label='Market Research')
cs = Transition(label='Cultural Study')
sa = Transition(label='Supply Analysis')
da = Transition(label='Design Adaptation')
ps = Transition(label='Partner Sourcing')
rc = Transition(label='Regulatory Check')
rr = Transition(label='Risk Review')
isf = Transition(label='Influencer Setup')
pl = Transition(label='Pilot Launch')
fb = Transition(label='Feedback Loop')
pt = Transition(label='Product Tuning')
dm = Transition(label='Distribution Map')
ca = Transition(label='Compliance Audit')
pset = Transition(label='Payment Setup')
gp = Transition(label='Growth Planning')

# Parallel block: Partner Sourcing, Regulatory Check, Risk Review
parallel1 = StrictPartialOrder(nodes=[ps, rc, rr])

# Loop for continuous feedback and product tuning
loop = OperatorPOWL(operator=Operator.LOOP, children=[fb, pt])

# Parallel block: Distribution Map, Compliance Audit, Payment Setup
parallel2 = StrictPartialOrder(nodes=[dm, ca, pset])

# Assemble the root partial order
root = StrictPartialOrder(
    nodes=[mr, cs, sa, da, parallel1, isf, pl, loop, parallel2, gp]
)

# Define the control-flow ordering
root.order.add_edge(mr, cs)
root.order.add_edge(cs, sa)
root.order.add_edge(sa, da)

root.order.add_edge(da, parallel1)
root.order.add_edge(parallel1, isf)

root.order.add_edge(isf, pl)
root.order.add_edge(pl, loop)

root.order.add_edge(loop, parallel2)
root.order.add_edge(parallel2, gp)