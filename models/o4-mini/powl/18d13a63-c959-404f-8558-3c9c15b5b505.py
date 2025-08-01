# Generated from: 18d13a63-c959-404f-8558-3c9c15b5b505.json
# Description: This process involves the intricate creation of bespoke artisanal perfumes combining traditional craftsmanship with modern sensory analysis. Starting with raw material sourcing, the process includes botanical extraction, scent profiling, and iterative blending cycles guided by expert perfumers. Each batch undergoes stability testing and sensory panel reviews before final bottling and packaging. The process also integrates sustainable practices by recycling waste and optimizing ingredient usage, ensuring both quality and environmental responsibility throughout the development stages. Customer feedback loops further refine future formulations, making it a continuous innovation cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ms    = Transition(label='Material Sourcing')
be    = Transition(label='Botanical Extraction')
sp    = Transition(label='Scent Profiling')
ib    = Transition(label='Initial Blending')
sa    = Transition(label='Sensory Analysis')
st    = Transition(label='Stability Testing')
pr    = Transition(label='Panel Review')
pd    = Transition(label='Packaging Design')
qc    = Transition(label='Quality Control')
fb    = Transition(label='Final Bottling')
cf    = Transition(label='Customer Feedback')
wr    = Transition(label='Waste Recycling')
saud  = Transition(label='Sustainability Audit')
br    = Transition(label='Batch Refinement')
fu    = Transition(label='Formula Update')

# Main forward sequence A
A = StrictPartialOrder(nodes=[ms, be, sp, ib, sa, st, pr, pd, qc, fb, cf])
A.order.add_edge(ms, be)
A.order.add_edge(be, sp)
A.order.add_edge(sp, ib)
A.order.add_edge(ib, sa)
A.order.add_edge(ib, st)
A.order.add_edge(sa, pr)
A.order.add_edge(st, pr)
A.order.add_edge(pr, pd)
A.order.add_edge(pd, qc)
A.order.add_edge(qc, fb)
A.order.add_edge(fb, cf)

# Improvement & sustainability block B
B = StrictPartialOrder(nodes=[wr, saud, br, fu])
B.order.add_edge(wr, br)
B.order.add_edge(saud, br)
B.order.add_edge(br, fu)

# Loop: execute A, then either exit or do B then A again, iterating the innovation cycle
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])