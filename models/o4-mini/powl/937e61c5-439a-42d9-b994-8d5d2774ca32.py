# Generated from: 937e61c5-439a-42d9-b994-8d5d2774ca32.json
# Description: This process involves integrating ideas from unrelated industries to create groundbreaking products or services. It starts with trend scouting in multiple sectors, followed by cross-functional brainstorming sessions that challenge conventional boundaries. Prototypes are rapidly developed using agile sprints, incorporating feedback from diverse user groups. Parallel market simulations assess potential impact and feasibility. Intellectual property strategies are crafted concurrently to safeguard novel concepts. The process concludes with a phased rollout plan that leverages partnerships across industries to maximize reach and adoption while continuously gathering data for iterative improvements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ts  = Transition(label='Trend Scouting')
cb  = Transition(label='Cross Brainstorm')
ic  = Transition(label='Idea Capture')
cf  = Transition(label='Concept Filter')
rp  = Transition(label='Rapid Prototype')
uf  = Transition(label='User Feedback')
ms  = Transition(label='Market Simulate')
fc  = Transition(label='Feasibility Check')
ip  = Transition(label='IP Strategy')
pa  = Transition(label='Partner Align')
pl  = Transition(label='Pilot Launch')
dm  = Transition(label='Data Monitor')
idg = Transition(label='Iterate Design')
sp  = Transition(label='Scale Plan')
ab  = Transition(label='Adoption Boost')

# Loop for continuous improvement: monitor data then optionally iterate design
improve_loop = OperatorPOWL(operator=Operator.LOOP, children=[dm, idg])

# Build the partial order
root = StrictPartialOrder(nodes=[ts, cb, ic, cf, rp, uf,
                                 ms, fc, ip,
                                 pa, pl, improve_loop,
                                 sp, ab])

# Define the control-flow dependencies
root.order.add_edge(ts,  cb)            # trend scouting -> brainstorming
root.order.add_edge(cb,  ic)            # brainstorming -> idea capture
root.order.add_edge(ic,  cf)            # idea capture -> concept filter
root.order.add_edge(cf,  rp)            # filter -> prototype
root.order.add_edge(rp,  uf)            # prototype -> user feedback

# After feedback, run market simulation, feasibility check, and IP strategy in parallel
root.order.add_edge(uf,  ms)
root.order.add_edge(uf,  fc)
root.order.add_edge(uf,  ip)

# Synchronize before partner alignment
root.order.add_edge(ms, pa)
root.order.add_edge(fc, pa)
root.order.add_edge(ip, pa)

# Launch and then improvement loop
root.order.add_edge(pa, pl)
root.order.add_edge(pl, improve_loop)

# After loop exit, scale and boost adoption
root.order.add_edge(improve_loop, sp)
root.order.add_edge(sp, ab)