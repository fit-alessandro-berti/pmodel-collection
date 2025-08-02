# Generated from: 7d461b6d-28ee-480b-aa75-192b3fc7598d.json
# Description: This process orchestrates the collection, evaluation, and implementation of innovative ideas sourced from a global community. It begins with idea solicitation through multiple channels, followed by automated filtering and peer review to prioritize high-potential concepts. Selected ideas undergo prototyping and iterative feedback loops involving both internal experts and the crowd. Concurrently, legal assessments ensure intellectual property compliance, while resource allocation optimizes development costs. After refinement, successful prototypes are transitioned to pilot programs with continuous performance monitoring. Finally, viable innovations are scaled for full market deployment, supported by targeted marketing and post-launch evaluation to capture learnings and inform future cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Idea_Capture = Transition(label='Idea Capture')

# Filtering and review (Automated filtering and peer review)
Filter_Review = Transition(label='Filter Review')
Peer_Voting = Transition(label='Peer Voting')
Concept_Ranking = Transition(label='Concept Ranking')

# Prototype build and iterative feedback loop
Prototype_Build = Transition(label='Prototype Build')
Expert_Feedback = Transition(label='Expert Feedback')

# SilentTransition for loop exit
skip = SilentTransition()

# Loop for iterative feedback: execute Prototype_Build then either exit or do Expert_Feedback then Prototype_Build again 
# (* (Prototype_Build, Expert_Feedback))
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[Prototype_Build, Expert_Feedback])

# Legal and resource assessments running concurrently with prototyping and feedback loop
Legal_Check = Transition(label='Legal Check')
Resource_Assign = Transition(label='Resource Assign')

# After iteration and concurrent checks, move to pilot launch and monitoring
Pilot_Launch = Transition(label='Pilot Launch')
Performance_Monitor = Transition(label='Performance Monitor')

# Market test and scale plan following pilot
Market_Test = Transition(label='Market Test')
Scale_Plan = Transition(label='Scale Plan')

# Marketing preparation and post-launch evaluation running concurrently
Marketing_Prep = Transition(label='Marketing Prep')
Post_Launch = Transition(label='Post Launch')
Data_Analyze = Transition(label='Data Analyze')

# Post_launch evaluation includes data analyze after post launch
postlaunch_porder = StrictPartialOrder(nodes=[Post_Launch, Data_Analyze])
postlaunch_porder.order.add_edge(Post_Launch, Data_Analyze)

# Marketing prep and post_launch evaluation run concurrently
marketing_post_porder = StrictPartialOrder(nodes=[Marketing_Prep, postlaunch_porder])

# Pilot launch precedes performance monitor
pilot_porder = StrictPartialOrder(nodes=[Pilot_Launch, Performance_Monitor])
pilot_porder.order.add_edge(Pilot_Launch, Performance_Monitor)

# Market test precedes scale plan
market_scale_porder = StrictPartialOrder(nodes=[Market_Test, Scale_Plan])
market_scale_porder.order.add_edge(Market_Test, Scale_Plan)

# Concurrent block of pilot process and market/scale process and marketing/postlaunch
post_proto_conc = StrictPartialOrder(nodes=[pilot_porder, market_scale_porder, marketing_post_porder])

# Concept ranking comes after peer voting
peer_review_porder = StrictPartialOrder(nodes=[Filter_Review, Peer_Voting, Concept_Ranking])
peer_review_porder.order.add_edge(Filter_Review, Peer_Voting)
peer_review_porder.order.add_edge(Peer_Voting, Concept_Ranking)

# After idea capture the peer review block
first_phase_porder = StrictPartialOrder(nodes=[Idea_Capture, peer_review_porder])
first_phase_porder.order.add_edge(Idea_Capture, peer_review_porder)

# Concurrently with loop_feedback run legal check and resource assign
concurrent_after_ranking = StrictPartialOrder(nodes=[loop_feedback, Legal_Check, Resource_Assign])
# no order edges here: concurrency

# Build the whole prototype phase order, ranking then concurrent (loop + legal + resource)
proto_phase = StrictPartialOrder(nodes=[Concept_Ranking, concurrent_after_ranking])
proto_phase.order.add_edge(Concept_Ranking, concurrent_after_ranking)

# After prototype phase complete, next is final concurrent phase of pilot, market, marketing/postlaunch
final_phase = post_proto_conc

# Root PO: ordering the phases
root = StrictPartialOrder(nodes=[first_phase_porder, proto_phase, final_phase])
root.order.add_edge(first_phase_porder, proto_phase)
root.order.add_edge(proto_phase, final_phase)