# Generated from: c214f20c-26dd-4489-846b-508b44b5ecfa.json
# Description: This process outlines the integration of urban vertical farming systems into existing city infrastructure. It involves site analysis, modular farm design, environmental impact assessment, community engagement, regulatory approval, resource logistics, automated planting, crop monitoring, pest control, data analytics, harvest scheduling, waste recycling, energy optimization, distribution planning, and continuous system refinement to ensure sustainable food production within dense urban environments while minimizing ecological footprint and maximizing yield efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
sa = Transition(label='Site Analysis')
dm = Transition(label='Design Modules')
ia = Transition(label='Impact Assess')
ec = Transition(label='Engage Community')
oa = Transition(label='Obtain Approval')
lp = Transition(label='Logistics Plan')
ap = Transition(label='Automated Plant')
cm = Transition(label='Crop Monitor')
pc = Transition(label='Pest Control')
da = Transition(label='Data Analytics')
sh = Transition(label='Schedule Harvest')
rw = Transition(label='Recycle Waste')
oe = Transition(label='Optimize Energy')
pd = Transition(label='Plan Distribution')
rs = Transition(label='Refine System')

# Build the loop body: monitoring, control, analytics, scheduling, recycling, optimization, distribution, refinement
body = StrictPartialOrder(nodes=[cm, pc, da, sh, rw, oe, pd, rs])
body.order.add_edge(cm, da)
body.order.add_edge(pc, da)
body.order.add_edge(da, sh)
body.order.add_edge(sh, rw)
body.order.add_edge(rw, pd)
body.order.add_edge(pd, oe)
body.order.add_edge(oe, rs)

# Define the LOOP: do Automated Plant, then zero or more iterations of the body + Automated Plant
loop_cycle = OperatorPOWL(operator=Operator.LOOP, children=[ap, body])

# Top‐level partial order: sequential setup then the production loop
root = StrictPartialOrder(nodes=[sa, dm, ia, ec, oa, lp, loop_cycle])
root.order.add_edge(sa, dm)
root.order.add_edge(dm, ia)
root.order.add_edge(ia, ec)
root.order.add_edge(ec, oa)
root.order.add_edge(oa, lp)
root.order.add_edge(lp, loop_cycle)