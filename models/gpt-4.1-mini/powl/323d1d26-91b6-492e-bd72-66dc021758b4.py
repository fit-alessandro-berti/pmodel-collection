# Generated from: 323d1d26-91b6-492e-bd72-66dc021758b4.json
# Description: This process facilitates the continuous generation and integration of innovative concepts sourced from disparate industries to create breakthrough solutions. It begins with environmental scanning and trend mapping to identify emerging technologies and market shifts. Following this, a multidisciplinary ideation workshop is conducted to merge insights from unrelated sectors, fostering novel perspectives. Prototypes are rapidly developed and tested in controlled environments, with feedback loops involving external experts to refine concepts. Parallel regulatory and risk assessments ensure compliance and viability, while strategic partnerships are negotiated to leverage complementary capabilities. The process includes iterative knowledge transfer sessions and scalability planning to prepare innovations for market launch, followed by post-implementation reviews to capture lessons learned and inform subsequent cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Trend_Scan = Transition(label='Trend Scan')
Tech_Mapping = Transition(label='Tech Mapping')
Idea_Merge = Transition(label='Idea Merge')
Workshop_Host = Transition(label='Workshop Host')
Prototype_Build = Transition(label='Prototype Build')
Test_Run = Transition(label='Test Run')
Expert_Review = Transition(label='Expert Review')
Risk_Assess = Transition(label='Risk Assess')
Regulatory_Check = Transition(label='Regulatory Check')
Partner_Align = Transition(label='Partner Align')
Knowledge_Share = Transition(label='Knowledge Share')
Scale_Plan = Transition(label='Scale Plan')
Market_Prep = Transition(label='Market Prep')
Launch_Execute = Transition(label='Launch Execute')
Post_Review = Transition(label='Post Review')
Feedback_Loop = Transition(label='Feedback Loop')
Iterate_Cycle = Transition(label='Iterate Cycle')

# Build subgraphs according to the process description

# Initial scanning part: Trend Scan then Tech Mapping
scan_PO = StrictPartialOrder(nodes=[Trend_Scan, Tech_Mapping])
scan_PO.order.add_edge(Trend_Scan, Tech_Mapping)

# Multidisciplinary ideation workshop: Idea Merge then Workshop Host
ideation_PO = StrictPartialOrder(nodes=[Idea_Merge, Workshop_Host])
ideation_PO.order.add_edge(Idea_Merge, Workshop_Host)

# Prototype build and test with feedback loop and expert review
# Test Run and Expert Review happen after Prototype Build
prototype_PO = StrictPartialOrder(nodes=[Prototype_Build, Test_Run, Expert_Review, Feedback_Loop])
prototype_PO.order.add_edge(Prototype_Build, Test_Run)
prototype_PO.order.add_edge(Test_Run, Expert_Review)
prototype_PO.order.add_edge(Expert_Review, Feedback_Loop)

# Regulatory and risk assessments in parallel
regulatory_PO = StrictPartialOrder(nodes=[Regulatory_Check, Risk_Assess])  # parallel, no edges

# Strategic partnerships negotiation after assessments (we create partial order where Partner Align depends on both checks)
partner_PO = StrictPartialOrder(nodes=[Regulatory_Check, Risk_Assess, Partner_Align])
partner_PO.order.add_edge(Regulatory_Check, Partner_Align)
partner_PO.order.add_edge(Risk_Assess, Partner_Align)

# Knowledge transfer and scalability planning sequential
knowledge_PO = StrictPartialOrder(nodes=[Knowledge_Share, Scale_Plan])
knowledge_PO.order.add_edge(Knowledge_Share, Scale_Plan)

# Market preparation and launch execution sequential
market_PO = StrictPartialOrder(nodes=[Market_Prep, Launch_Execute])
market_PO.order.add_edge(Market_Prep, Launch_Execute)

# Post implementation review after launch
post_PO = Post_Review  # single activity

# Loop with iterative knowledge transfer and cycle iteration
loop_body = StrictPartialOrder(nodes=[Feedback_Loop, Iterate_Cycle])
loop_body.order.add_edge(Feedback_Loop, Iterate_Cycle)

# Loop: execute loop_body, then choose exit or loop again the prototype build/testing/refinement part
# Loop children: body (Knowledge Share, Scale Plan, Feedback Loop, Iterate Cycle are linked here logically)
# But Feedback Loop and Iterate Cycle are the "loop" body, while Prototype PO is "do" part to be repeated
# However, description: feedback loops involving experts refine concepts, iterative knowledge transfer sessions and scalability planning to prepare ...
# We'll model the loop as: 
# A = prototype_PO (build, test, expert review, feedback loop)
# B = knowledge_PO + loop_body (knowledge share, scale plan, feedback loop and iterate cycle)
# But feedback loop is also in prototype_PO, to avoid confusion, we model loop on:
# A = StrictPartialOrder(prototype build→test→expert review→feedback loop)
# B = StrictPartialOrder(knowledge share→scale plan→Feedback Loop, Iterate Cycle)
# We should treat the loop on (A, B)

# Define loop on prototype_PO and knowledge+feedback iteration
knowledge_feedback_PO = StrictPartialOrder(nodes=[Knowledge_Share, Scale_Plan, Feedback_Loop, Iterate_Cycle])
knowledge_feedback_PO.order.add_edge(Knowledge_Share, Scale_Plan)
knowledge_feedback_PO.order.add_edge(Scale_Plan, Feedback_Loop)
knowledge_feedback_PO.order.add_edge(Feedback_Loop, Iterate_Cycle)

# Loop operator with children: A (prototype_PO), B (knowledge_feedback_PO)
loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype_PO, knowledge_feedback_PO])

# The main process order:

# 1) [Trend Scan -> Tech Mapping] then
# 2) [Idea Merge -> Workshop Host] then
# 3) loop (prototype & test → knowledge transfer & feedback loops)
# 4) regulatory and risk assessments in parallel: Regulatory_Check || Risk_Assess
# 5) partner align depends on both assessments
# 6) Market prep → Launch execute
# 7) Post review
# Merge all:

# Step 4 and 5 combined:
reg_and_partner_PO = partner_PO  # edges: Regulatory_Check -> Partner_Align, Risk_Assess -> Partner_Align

# Parallel regulatory & risk is embedded by joint PO with edges to Partner_Align
# So reg_and_partner_PO is ok.

# Final composition:

nodes_main = [
    scan_PO,
    ideation_PO,
    loop,
    reg_and_partner_PO,
    market_PO,
    Post_Review
]

root = StrictPartialOrder(nodes=nodes_main)

# Add edges for sequential logic between big steps:
root.order.add_edge(scan_PO, ideation_PO)
root.order.add_edge(ideation_PO, loop)
root.order.add_edge(loop, reg_and_partner_PO)
root.order.add_edge(reg_and_partner_PO, market_PO)
root.order.add_edge(market_PO, Post_Review)