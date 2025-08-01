# Generated from: 5952d56a-0979-4c41-a5b3-4ef6e4a7417f.json
# Description: This process outlines the end-to-end production of custom drones tailored for specialized industrial applications. It begins with client consultation to gather detailed requirements, followed by design customization using advanced CAD tools. The production phase involves precision component fabrication, including 3D printing of unique parts and selective material treatments. Assembly is conducted in a controlled environment to ensure optimal integration of electronics and mechanical systems. Quality assurance includes rigorous flight testing and software calibration. Finally, the process concludes with packaging, client training, and post-delivery support to ensure operational success and client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
cb  = Transition(label='Client Brief')
dd  = Transition(label='Design Draft')
ms  = Transition(label='Material Sourcing')
pf  = Transition(label='Part Fabrication')
tp  = Transition(label='3D Printing')
st  = Transition(label='Surface Treat')
ct  = Transition(label='Component Test')
sa  = Transition(label='System Assembly')
fl  = Transition(label='Firmware Load')
cs  = Transition(label='Calibration Setup')
ft  = Transition(label='Flight Testing')
qr  = Transition(label='Quality Review')
pp  = Transition(label='Packaging Prep')
ds  = Transition(label='Delivery Setup')
ctr = Transition(label='Client Training')
sl  = Transition(label='Support Launch')

# Build the partial order
root = StrictPartialOrder(nodes=[cb, dd, ms, pf, tp, st, ct, sa, fl, cs, ft, qr, pp, ds, ctr, sl])

# Define ordering constraints
root.order.add_edge(cb, dd)
root.order.add_edge(dd, ms)
root.order.add_edge(ms, pf)
root.order.add_edge(ms, tp)
root.order.add_edge(pf, st)
root.order.add_edge(tp, st)
root.order.add_edge(st, ct)
root.order.add_edge(ct, sa)
root.order.add_edge(sa, fl)
root.order.add_edge(fl, cs)
root.order.add_edge(cs, ft)
root.order.add_edge(ft, qr)
root.order.add_edge(qr, pp)
root.order.add_edge(pp, ds)
root.order.add_edge(ds, ctr)
root.order.add_edge(ctr, sl)