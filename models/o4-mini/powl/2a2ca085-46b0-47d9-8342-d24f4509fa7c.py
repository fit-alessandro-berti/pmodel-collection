# Generated from: 2a2ca085-46b0-47d9-8342-d24f4509fa7c.json
# Description: This process involves the intricate verification and authentication of rare antique assets for auction houses. It includes provenance research, material analysis, stylistic evaluation, condition reporting, and legal compliance checks. Each step requires collaboration between historians, scientists, legal experts, and auctioneers to ensure the asset's authenticity and market value before final cataloging and sale approval. Unexpected findings may trigger re-evaluation or legal hold, adding complexity to the workflow and requiring meticulous documentation and chain-of-custody management throughout the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ai = Transition(label='Asset Intake')
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
sc = Transition(label='Scientific Test')
st = Transition(label='Stylistic Review')
cr = Transition(label='Condition Report')
lr = Transition(label='Legal Review')
ep = Transition(label='Expert Panel')
ma = Transition(label='Market Analysis')
ce = Transition(label='Catalog Entry')
fa = Transition(label='Final Approval')
au = Transition(label='Auction Setup')
fd = Transition(label='Forgery Detection')
re = Transition(label='Re-Evaluation')
hn = Transition(label='Hold Notification')
cc = Transition(label='Chain Custody')

# A silent transition to represent "no rework/no hold"
skip = SilentTransition()

# Forgery‐triggered path: Forgery Detection -> Hold Notification
forgery_sub = StrictPartialOrder(nodes=[fd, hn])
forgery_sub.order.add_edge(fd, hn)

# Choice after Provenance Check: either proceed or go through forgery path
xor_after_pc = OperatorPOWL(operator=Operator.XOR, children=[skip, forgery_sub])

# Choice after Scientific Test: either proceed or do a Re‐Evaluation
xor_after_sc = OperatorPOWL(operator=Operator.XOR, children=[skip, re])

# Root partial order with all nodes (Chain Custody runs fully concurrent)
root = StrictPartialOrder(nodes=[
    ai, pc, xor_after_pc,
    ms, sc, xor_after_sc,
    st, cr, lr,
    ep, ma, ce,
    fa, au,
    cc
])

# Define the main sequence edges
root.order.add_edge(ai, pc)
root.order.add_edge(pc, xor_after_pc)
root.order.add_edge(xor_after_pc, ms)
root.order.add_edge(ms, sc)
root.order.add_edge(sc, xor_after_sc)
root.order.add_edge(xor_after_sc, st)
root.order.add_edge(st, cr)
root.order.add_edge(cr, lr)
root.order.add_edge(lr, ep)
root.order.add_edge(ep, ma)
root.order.add_edge(ma, ce)
root.order.add_edge(ce, fa)
root.order.add_edge(fa, au)