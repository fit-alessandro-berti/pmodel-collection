# Generated from: bdea8788-5b9e-4795-9f65-aaeda45f2282.json
# Description: This process coordinates rapid disaster response by leveraging a global network of volunteers, local authorities, and AI-driven resource allocation. It begins with hazard detection and public alerting, followed by volunteer mobilization through geotagged task assignments. Data from on-site volunteers is continuously aggregated and analyzed for situational awareness. Concurrently, supply chains are dynamically managed to deliver essential goods, while remote experts provide real-time guidance via digital platforms. The process integrates feedback loops to adapt resource allocation and volunteer deployment, ensuring efficient coverage despite unpredictable conditions and communication challenges. Post-event, the system facilitates impact assessment and lessons learned compilation for future preparedness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
hd = Transition(label='Hazard Detect')
ia = Transition(label='Issue Alert')
mv = Transition(label='Mobilize Volunteers')
at = Transition(label='Assign Tasks')
cd = Transition(label='Collect Data')
ar = Transition(label='Analyze Reports')
us = Transition(label='Update Status')
mp = Transition(label='Monitor Progress')
ad = Transition(label='Adjust Deployment')
alloc_supplies = Transition(label='Allocate Supplies')
coord_transport = Transition(label='Coordinate Transport')
pg = Transition(label='Provide Guidance')
mf = Transition(label='Manage Feedback')
cdt = Transition(label='Conduct Debrief')
cl = Transition(label='Compile Lessons')

# Feedback loop on monitoring and adjustment
loop = OperatorPOWL(operator=Operator.LOOP, children=[mp, ad])

# Data‐analysis branch: Collect Data -> Analyze Reports -> Update Status -> loop(Monitor, Adjust)
data_branch = StrictPartialOrder(nodes=[cd, ar, us, loop])
data_branch.order.add_edge(cd, ar)
data_branch.order.add_edge(ar, us)
data_branch.order.add_edge(us, loop)

# Supply‐chain branch: Allocate Supplies -> Coordinate Transport
supply_branch = StrictPartialOrder(nodes=[alloc_supplies, coord_transport])
supply_branch.order.add_edge(alloc_supplies, coord_transport)

# Build the root process with partial order and concurrent branches
root = StrictPartialOrder(nodes=[
    hd, ia, mv, at,
    data_branch,
    supply_branch,
    pg,
    mf,
    cdt, cl
])
o = root.order
# Initial sequence
o.add_edge(hd, ia)
o.add_edge(ia, mv)
o.add_edge(mv, at)
# Fork into three concurrent branches
o.add_edge(at, data_branch)
o.add_edge(at, supply_branch)
o.add_edge(at, pg)
# Join branches into feedback management
o.add_edge(data_branch, mf)
o.add_edge(supply_branch, mf)
o.add_edge(pg, mf)
# Final sequence: debrief and lessons
o.add_edge(mf, cdt)
o.add_edge(cdt, cl)