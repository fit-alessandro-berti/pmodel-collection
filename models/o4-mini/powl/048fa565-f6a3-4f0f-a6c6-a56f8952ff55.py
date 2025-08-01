# Generated from: 048fa565-f6a3-4f0f-a6c6-a56f8952ff55.json
# Description: This process integrates diverse industry insights to fuel novel product development through iterative collaboration between R&D, marketing, and external partners. It involves continuous environmental scanning, trend synthesis, concept incubation, rapid prototyping, multi-stakeholder feedback loops, and adaptive commercialization strategies. The cycle emphasizes agility, knowledge transfer, and risk mitigation by leveraging cross-sector data analytics and co-creation workshops, ultimately accelerating innovation beyond traditional boundaries and creating sustainable competitive advantages in dynamic markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
TS = Transition(label='Trend Scan')
IG = Transition(label='Insight Gather')
IF = Transition(label='Idea Filter')
CM = Transition(label='Concept Map')

PA = Transition(label='Partner Align')
RAlloc = Transition(label='Resource Allocate')
PB = Transition(label='Prototype Build')
FL = Transition(label='Feedback Loop')
DA = Transition(label='Data Analyze')
SP = Transition(label='Strategy Pivot')
RAssess = Transition(label='Risk Assess')
MT = Transition(label='Market Test')
LP = Transition(label='Launch Plan')
IR = Transition(label='Impact Review')
KS = Transition(label='Knowledge Share')

# Phase A: environmental scanning & concept incubation
A = StrictPartialOrder(nodes=[TS, IG, IF, CM])
A.order.add_edge(TS, IG)
A.order.add_edge(IG, IF)
A.order.add_edge(IF, CM)

# Phase B: partner alignment, prototyping, feedback, commercialization
B = StrictPartialOrder(nodes=[
    PA, RAlloc, PB, FL, DA, SP, RAssess, MT, LP, IR, KS
])
# partner alignment and resource allocation in parallel, both precede prototype build
B.order.add_edge(PA, PB)
B.order.add_edge(RAlloc, PB)
# then sequential flow through the rest
B.order.add_edge(PB, FL)
B.order.add_edge(FL, DA)
B.order.add_edge(DA, SP)
B.order.add_edge(SP, RAssess)
B.order.add_edge(RAssess, MT)
B.order.add_edge(MT, LP)
B.order.add_edge(LP, IR)
B.order.add_edge(IR, KS)

# Wrap into an iterative loop: do A, then either exit or do B then A again
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])