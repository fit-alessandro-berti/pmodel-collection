# Generated from: e46c628d-2ddc-4ba1-8c0f-c01234136dec.json
# Description: This process involves the rapid mobilization and coordination of multiple agencies and resources to manage unforeseen emergency situations such as natural disasters, industrial accidents, or security threats. It includes initial threat assessment, resource allocation, communication synchronization, public information dissemination, and post-event analysis to improve future responsiveness. Stakeholders must work under high pressure with dynamic priorities, ensuring safety, compliance, and efficient recovery while adapting to evolving conditions on the ground. The process integrates technology, field operations, and strategic decision-making to mitigate impact effectively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ta = Transition(label='Threat Assess')
ad = Transition(label='Alert Dispatch')
rc = Transition(label='Resource Check')
ig = Transition(label='Intel Gather')
re = Transition(label='Risk Evaluate')
ps = Transition(label='Priority Set')
csu = Transition(label='Command Setup')
tm = Transition(label='Team Mobilize')
cd = Transition(label='Comm Sync')
sm = Transition(label='Safety Monitor')
sp = Transition(label='Supply Manage')
il = Transition(label='Incident Log')
pu = Transition(label='Public Update')
fd = Transition(label='Field Deploy')
rp = Transition(label='Recovery Plan')
db = Transition(label='Debrief Team')
da = Transition(label='Data Archive')

# Silent skip for optional steps
skip = SilentTransition()

# Optional Intel Gather step
xor_intel = OperatorPOWL(operator=Operator.XOR, children=[ig, skip])

# Define loop body: field operations, supply, logging, public update, monitoring
body = StrictPartialOrder(nodes=[fd, sp, il, pu, sm])
body.order.add_edge(fd, sp)
body.order.add_edge(sp, il)
body.order.add_edge(il, pu)
body.order.add_edge(pu, sm)

# Loop: Comm Sync then either exit or do body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[cd, body])

# Top‐level partial order
root = StrictPartialOrder(
    nodes=[ta, ad, rc, xor_intel, re, ps, csu, tm, loop, rp, db, da]
)

# Define the control‐flow order
root.order.add_edge(ta, ad)
root.order.add_edge(ad, rc)
root.order.add_edge(rc, xor_intel)
root.order.add_edge(xor_intel, re)
root.order.add_edge(re, ps)
root.order.add_edge(ps, csu)
root.order.add_edge(csu, tm)
root.order.add_edge(tm, loop)
root.order.add_edge(loop, rp)
root.order.add_edge(rp, db)
root.order.add_edge(db, da)