# Generated from: 3b51a585-ec0d-4f22-b41a-cb5bc7184003.json
# Description: This process describes a complex, iterative cycle where a company integrates emerging technologies from unrelated industries to create novel products. It begins with trend scouting across diverse sectors, followed by cross-disciplinary ideation sessions. Prototypes are rapidly developed using minimal viable concepts, then tested in simulated environments reflecting multiple market conditions. Feedback loops incorporate insights from external experts, regulatory bodies, and potential end-users. Parallel risk assessments and resource reallocations ensure adaptability. The cycle culminates in a phased pilot launch, with continuous data-driven refinement before full-scale commercialization. This atypical approach demands agility, broad expertise, and extensive collaboration beyond conventional boundaries, enabling breakthrough innovations that disrupt traditional markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ts = Transition(label='Trend Scouting')
ifuse = Transition(label='Idea Fusion')
rp = Transition(label='Rapid Prototyping')
st = Transition(label='Simulated Testing')
ms = Transition(label='Market Simulation')
er = Transition(label='Expert Review')
rc = Transition(label='Regulatory Check')
uf = Transition(label='User Feedback')
ra = Transition(label='Risk Analysis')
rs = Transition(label='Resource Shift')
cr = Transition(label='Concept Refinement')
pl = Transition(label='Pilot Launch')
dm = Transition(label='Data Monitoring')
iu = Transition(label='Iterative Update')
ct = Transition(label='Cross Training')
ss = Transition(label='Stakeholder Sync')

# Define the "A" part: one full run of the innovation cycle
A = StrictPartialOrder(nodes=[
    ts, ifuse, rp,
    st, ms,
    er, rc, uf, ra, rs,
    cr, pl, dm
])
# Linear progression up to simulation
A.order.add_edge(ts, ifuse)
A.order.add_edge(ifuse, rp)
# After prototyping, run both testing and market simulation in sequence
A.order.add_edge(rp, st)
A.order.add_edge(st, ms)
# After simulation, kick off all feedback and risk activities in parallel
for prev in [ms]:
    for nxt in [er, rc, uf, ra, rs]:
        A.order.add_edge(prev, nxt)
# After all feedback/risk complete, do concept refinement
for prev in [er, rc, uf, ra, rs]:
    A.order.add_edge(prev, cr)
# Then pilot launch and data monitoring
A.order.add_edge(cr, pl)
A.order.add_edge(pl, dm)

# Define the "B" part: the iterative update & cross‐functional collaboration
B = StrictPartialOrder(nodes=[iu, ct, ss])
B.order.add_edge(iu, ct)
B.order.add_edge(ct, ss)

# Wrap them into a loop: do A, then optionally do B and A again, etc., until exit
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])