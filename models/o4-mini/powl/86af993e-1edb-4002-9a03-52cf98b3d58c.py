# Generated from: 86af993e-1edb-4002-9a03-52cf98b3d58c.json
# Description: This process facilitates the integration of emerging technologies from disparate industries into a unified innovation pipeline. It begins with trend scanning across sectors, followed by cross-functional ideation sessions to identify transferable solutions. After initial concept validation, the process moves into prototype adaptation, where technology is customized for new applications. Concurrently, regulatory and compliance checks are conducted to ensure feasibility. The next phase involves pilot deployments in controlled environments, capturing performance data and user feedback. Iterative refinement cycles address technical and operational challenges, supported by cross-industry mentorship programs. Finally, scalable rollout strategies are developed, incorporating market entry tactics and continuous improvement plans, creating a sustainable innovation ecosystem that leverages unconventional synergies for competitive advantage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ts = Transition(label='Trend Scan')
im = Transition(label='Idea Merge')
cv = Transition(label='Concept Vetting')
pa = Transition(label='Prototype Adapt')
cc = Transition(label='Compliance Check')
pd = Transition(label='Pilot Deploy')
dc = Transition(label='Data Capture')
uf = Transition(label='User Feedback')
idesign = Transition(label='Iterate Design')
ra = Transition(label='Risk Assess')
ma = Transition(label='Mentor Align')
ms = Transition(label='Market Study')
sd = Transition(label='Strategy Draft')
sp = Transition(label='Scale Plan')
ls = Transition(label='Launch Sync')
pr = Transition(label='Performance Review')

# Build the refinement-loop: first Iterate Design → Risk Assess, then optionally Mentor Align, and repeat
refine_body = StrictPartialOrder(nodes=[idesign, ra])
refine_body.order.add_edge(idesign, ra)
loop_refine = OperatorPOWL(operator=Operator.LOOP, children=[refine_body, ma])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    ts, im, cv,
    pa, cc,
    pd, dc, uf,
    loop_refine,
    ms, sd, sp, ls, pr
])

# Define the control‐flow edges
root.order.add_edge(ts, im)
root.order.add_edge(im, cv)

# After concept vetting, prototype adaptation and compliance checks run in parallel
root.order.add_edge(cv, pa)
root.order.add_edge(cv, cc)

# Both must complete before pilot deployment
root.order.add_edge(pa, pd)
root.order.add_edge(cc, pd)

# Pilot deployment feeds into data capture and user feedback (in parallel)
root.order.add_edge(pd, dc)
root.order.add_edge(pd, uf)

# Both data capture and user feedback trigger the refinement loop
root.order.add_edge(dc, loop_refine)
root.order.add_edge(uf, loop_refine)

# After all refinements finish, move to scalable rollout planning
root.order.add_edge(loop_refine, ms)
root.order.add_edge(ms, sd)
root.order.add_edge(sd, sp)
root.order.add_edge(sp, ls)
root.order.add_edge(ls, pr)