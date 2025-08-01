# Generated from: e4ef1b80-4e70-40f7-a5af-10d7a1c9bf4e.json
# Description: This process enables companies from disparate industries to collaboratively generate and implement breakthrough innovations by leveraging diverse expertise, iterative knowledge exchange, and synchronized development phases. It begins with opportunity scouting across sectors, followed by rapid ideation workshops that blend unique perspectives. Subsequent feasibility testing incorporates shared resources and joint prototyping. The cycle continues with cross-validation through pilot deployments in varied markets, collecting multi-dimensional feedback. Adaptation and scaling efforts require coordinated regulatory navigation and resource allocation among partners. The process concludes with collective intellectual property management and market launch strategies that maximize cross-industry synergies while maintaining agility and confidentiality throughout the collaboration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
os = Transition(label='Opportunity Scan')
iw = Transition(label='Idea Workshop')
# Two separate nodes for Concept Merge: one for loop entry, one within the cycle body
cm_entry = Transition(label='Concept Merge')
cm_loop = Transition(label='Concept Merge')
ra = Transition(label='Resource Align')
pb = Transition(label='Prototype Build')
ft = Transition(label='Feasibility Test')
pl = Transition(label='Pilot Launch')
fg = Transition(label='Feedback Gather')
da = Transition(label='Design Adapt')
cc = Transition(label='Compliance Check')
sp = Transition(label='Scaling Plan')
pr = Transition(label='Partner Review')
ip = Transition(label='IP Management')
ms = Transition(label='Market Sync')
es = Transition(label='Exit Strategy')

# Build the cycle body: Concept Merge (loop) → Resource Align → Prototype Build → Feasibility Test
# → Pilot Launch → Feedback Gather → Design Adapt → Compliance Check → Scaling Plan → Partner Review
cycle_body = StrictPartialOrder(nodes=[cm_loop, ra, pb, ft, pl, fg, da, cc, sp, pr])
cycle_body.order.add_edge(cm_loop, ra)
cycle_body.order.add_edge(ra, pb)
cycle_body.order.add_edge(pb, ft)
cycle_body.order.add_edge(ft, pl)
cycle_body.order.add_edge(pl, fg)
cycle_body.order.add_edge(fg, da)
cycle_body.order.add_edge(da, cc)
cycle_body.order.add_edge(cc, sp)
cycle_body.order.add_edge(sp, pr)

# Wrap the iterative innovation cycle in a LOOP:
#   first execute cm_entry, then repeatedly either exit or do (cycle_body then cm_entry) again
innovation_cycle = OperatorPOWL(operator=Operator.LOOP, children=[cm_entry, cycle_body])

# Top‐level partial order:
# Opportunity Scan → Idea Workshop → innovation_cycle → IP Management → Market Sync → Exit Strategy
root = StrictPartialOrder(nodes=[os, iw, innovation_cycle, ip, ms, es])
root.order.add_edge(os, iw)
root.order.add_edge(iw, innovation_cycle)
root.order.add_edge(innovation_cycle, ip)
root.order.add_edge(ip, ms)
root.order.add_edge(ms, es)