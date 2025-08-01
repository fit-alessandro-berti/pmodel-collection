# Generated from: 6c45ed73-c3f5-4fee-99d3-d7f55c90c8b4.json
# Description: This process outlines a cross-industry innovation cycle where ideas from unrelated sectors are systematically extracted, evaluated, and adapted to create novel solutions. The cycle begins with trend scouting across diverse markets, followed by interdisciplinary workshops to generate hybrid concepts. Concepts are then prototyped using agile sprints and validated through multi-sector pilot programs. Feedback loops integrate stakeholder insights from contrasting industries, ensuring robust iteration. Intellectual property strategies are tailored to protect innovations spanning multiple regulatory environments. Finally, strategic partnerships are formed to scale the innovation globally, leveraging complementary distribution channels and joint marketing campaigns. This atypical process fosters breakthrough innovation by embracing complexity and diversity beyond traditional single-sector approaches.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ts = Transition(label='Trend Scouting')
ih = Transition(label='Idea Harvest')
cw = Transition(label='Cross-Workshops')
cf = Transition(label='Concept Fusion')
rp = Transition(label='Rapid Prototyping')
pt = Transition(label='Pilot Testing')
sr = Transition(label='Stakeholder Review')
fb = Transition(label='Feedback Loop')
ip = Transition(label='IP Strategy')
rs = Transition(label='Regulatory Scan')
pb = Transition(label='Partnership Build')
ma = Transition(label='Market Alignment')
sp = Transition(label='Scaling Plan')
jm = Transition(label='Joint Marketing')
ia = Transition(label='Innovation Audit')

# Build the feedback‐driven iteration as a LOOP: 
# bodyA = Concept Fusion -> Rapid Prototyping -> Pilot Testing -> Stakeholder Review
# bodyB = Feedback Loop
bodyA = StrictPartialOrder(nodes=[cf, rp, pt, sr])
bodyA.order.add_edge(cf, rp)
bodyA.order.add_edge(rp, pt)
bodyA.order.add_edge(pt, sr)

bodyB = StrictPartialOrder(nodes=[fb])

loop = OperatorPOWL(operator=Operator.LOOP, children=[bodyA, bodyB])

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[ts, ih, cw, loop, ip, rs, pb, ma, sp, jm, ia])
root.order.add_edge(ts, ih)
root.order.add_edge(ih, cw)
root.order.add_edge(cw, loop)
root.order.add_edge(loop, ip)
root.order.add_edge(ip, rs)
root.order.add_edge(rs, pb)
root.order.add_edge(pb, ma)
root.order.add_edge(ma, sp)
root.order.add_edge(sp, jm)
root.order.add_edge(jm, ia)