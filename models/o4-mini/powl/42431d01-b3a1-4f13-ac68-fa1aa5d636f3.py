# Generated from: 42431d01-b3a1-4f13-ac68-fa1aa5d636f3.json
# Description: This process involves systematically integrating breakthrough ideas from unrelated industries into a company’s product development framework. It begins with scanning diverse sectors for emerging trends, followed by ideation sessions where cross-disciplinary teams reinterpret these insights. The process includes rapid prototyping, iterative feedback loops with external experts, and scenario testing under variable market conditions. Risk assessments and intellectual property evaluations are conducted before finalizing scalable solutions. The process concludes with strategic launch planning, knowledge transfer workshops, and continuous monitoring of innovation impact across business units to ensure sustainable competitive advantage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ts = Transition(label='Trend Scan')
ih = Transition(label='Idea Harvest')
cts = Transition(label='Cross-Team Sync')
cs = Transition(label='Concept Sketch')
pb = Transition(label='Prototype Build')
er = Transition(label='Expert Review')
fl = Transition(label='Feedback Loop')
st = Transition(label='Scenario Test')
ra = Transition(label='Risk Assess')
ipr = Transition(label='IP Review')
sd = Transition(label='Scale Design')
lp = Transition(label='Launch Plan')
ks = Transition(label='Knowledge Share')
mm = Transition(label='Market Monitor')
ia = Transition(label='Impact Audit')

# Silent transition for loop exits
skip = SilentTransition()

# Loop for iterative prototyping & review: (build → review) with feedback repetitions
build_review = StrictPartialOrder(nodes=[pb, er])
build_review.order.add_edge(pb, er)
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[build_review, fl])

# Loop for continuous monitoring & impact audit
monitor_audit = StrictPartialOrder(nodes=[mm, ia])
monitor_audit.order.add_edge(mm, ia)
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[monitor_audit, skip])

# Assemble the main partial order
root = StrictPartialOrder(
    nodes=[ts, ih, cts, cs, loop1, st, ra, ipr, sd, lp, ks, loop2]
)

# Define the overall sequence
root.order.add_edge(ts, ih)
root.order.add_edge(ih, cts)
root.order.add_edge(cts, cs)
root.order.add_edge(cs, loop1)
root.order.add_edge(loop1, st)
root.order.add_edge(st, ra)
root.order.add_edge(ra, ipr)
root.order.add_edge(ipr, sd)
root.order.add_edge(sd, lp)
root.order.add_edge(lp, ks)
root.order.add_edge(ks, loop2)