# Generated from: 048fa565-f6a3-4f0f-a6c6-a56f8952ff55.json
# Description: This process integrates diverse industry insights to fuel novel product development through iterative collaboration between R&D, marketing, and external partners. It involves continuous environmental scanning, trend synthesis, concept incubation, rapid prototyping, multi-stakeholder feedback loops, and adaptive commercialization strategies. The cycle emphasizes agility, knowledge transfer, and risk mitigation by leveraging cross-sector data analytics and co-creation workshops, ultimately accelerating innovation beyond traditional boundaries and creating sustainable competitive advantages in dynamic markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Trend_Scan = Transition(label='Trend Scan')
Insight_Gather = Transition(label='Insight Gather')
Idea_Filter = Transition(label='Idea Filter')
Concept_Map = Transition(label='Concept Map')
Partner_Align = Transition(label='Partner Align')
Prototype_Build = Transition(label='Prototype Build')
Feedback_Loop = Transition(label='Feedback Loop')
Risk_Assess = Transition(label='Risk Assess')
Market_Test = Transition(label='Market Test')
Data_Analyze = Transition(label='Data Analyze')
Strategy_Pivot = Transition(label='Strategy Pivot')
Resource_Allocate = Transition(label='Resource Allocate')
Knowledge_Share = Transition(label='Knowledge Share')
Launch_Plan = Transition(label='Launch Plan')
Impact_Review = Transition(label='Impact Review')

# Define the iterative feedback loop:
# Within the cycle we have "Prototype Build" then "Feedback Loop" then "Risk Assess" then loop back to "Prototype Build"
# The cycle includes agile decision points "Strategy Pivot" or "Market Test"
# And knowledge/resource sharing before launch

# Loop body: after Prototype_Build, do Feedback_Loop and Risk_Assess
# Then XOR choice between Strategy_Pivot (pivot and continue loop) or Market_Test (exit loop cycle)
loop_body = StrictPartialOrder(nodes=[Feedback_Loop, Risk_Assess, Strategy_Pivot, Market_Test])

# Partial order edges inside loop_body
loop_body.order.add_edge(Feedback_Loop, Risk_Assess)
loop_body.order.add_edge(Risk_Assess, Strategy_Pivot)
loop_body.order.add_edge(Risk_Assess, Market_Test)

# LOOP operator: (Prototype_Build, loop_body)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Prototype_Build, loop_body])

# Pre-loop partial order for initial innovation steps:
# Trend_Scan -> Insight_Gather -> Idea_Filter -> Concept_Map -> Partner_Align -> loop (prototype & feedback)
pre_loop = StrictPartialOrder(nodes=[Trend_Scan, Insight_Gather, Idea_Filter, Concept_Map, Partner_Align, loop])

pre_loop.order.add_edge(Trend_Scan, Insight_Gather)
pre_loop.order.add_edge(Insight_Gather, Idea_Filter)
pre_loop.order.add_edge(Idea_Filter, Concept_Map)
pre_loop.order.add_edge(Concept_Map, Partner_Align)
pre_loop.order.add_edge(Partner_Align, loop)

# Post-loop partial order after exiting loop:
# After loop exit (via Market_Test), proceed: Resource_Allocate -> Data_Analyze -> Knowledge_Share -> Launch_Plan -> Impact_Review

post_loop = StrictPartialOrder(nodes=[Resource_Allocate, Data_Analyze, Knowledge_Share, Launch_Plan, Impact_Review])

post_loop.order.add_edge(Resource_Allocate, Data_Analyze)
post_loop.order.add_edge(Data_Analyze, Knowledge_Share)
post_loop.order.add_edge(Knowledge_Share, Launch_Plan)
post_loop.order.add_edge(Launch_Plan, Impact_Review)

# Combine pre_loop and post_loop with edge from loop to Resource_Allocate
root = StrictPartialOrder(nodes=[pre_loop, post_loop])

root.order.add_edge(pre_loop, post_loop)