# Generated from: 21cc30fb-196b-44a3-be66-fcbaa8c293c3.json
# Description: This process orchestrates the identification, evaluation, and integration of breakthrough innovations sourced from diverse industries into a company's existing product or service lines. It involves systematic scouting of emerging technologies, cross-disciplinary ideation workshops, feasibility assessments combining technical and market insights, pilot prototyping with rapid iteration, stakeholder alignment across departments, regulatory compliance checks adapted for unconventional applications, and finally scaled deployment with continuous feedback loops. The process emphasizes agility, knowledge transfer, and risk management to harness unconventional ideas while ensuring alignment with strategic goals and operational capabilities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ts = Transition(label='Tech Scouting')
ih = Transition(label='Idea Harvest')
cw = Transition(label='Concept Workshop')
fc = Transition(label='Feasibility Check')
ms = Transition(label='Market Scan')
rr = Transition(label='Risk Review')
ss = Transition(label='Stakeholder Sync')
ca = Transition(label='Compliance Audit')
kt = Transition(label='Knowledge Transfer')
pb = Transition(label='Prototype Build')
its = Transition(label='Iteration Sprint')
fl = Transition(label='Feedback Loop')
pl = Transition(label='Pilot Launch')
sp = Transition(label='Scale Planning')
lr = Transition(label='Launch Review')
pj = Transition(label='Post Launch')

# Define the iteration loop: sprint, then optionally feedback and sprint again
loop_iter = OperatorPOWL(operator=Operator.LOOP, children=[its, fl])

# Assemble the partial order
root = StrictPartialOrder(
    nodes=[
        ts, ih, cw,
        fc, ms,
        rr,
        ss, ca, kt,
        pb,
        loop_iter,
        pl, sp, lr, pj
    ]
)

# Sequential and parallel dependencies
root.order.add_edge(ts, ih)
root.order.add_edge(ih, cw)

# After concept workshop, do feasibility and market scan in parallel
root.order.add_edge(cw, fc)
root.order.add_edge(cw, ms)

# Both assessments must complete before risk review
root.order.add_edge(fc, rr)
root.order.add_edge(ms, rr)

# After risk review, stakeholder sync, compliance audit, and knowledge transfer run in parallel
root.order.add_edge(rr, ss)
root.order.add_edge(rr, ca)
root.order.add_edge(rr, kt)

# All three must finish before prototype build
root.order.add_edge(ss, pb)
root.order.add_edge(ca, pb)
root.order.add_edge(kt, pb)

# Prototype build leads into the iteration loop
root.order.add_edge(pb, loop_iter)

# After iteration loop, proceed to pilot launch and final rollout steps
root.order.add_edge(loop_iter, pl)
root.order.add_edge(pl, sp)
root.order.add_edge(sp, lr)
root.order.add_edge(lr, pj)