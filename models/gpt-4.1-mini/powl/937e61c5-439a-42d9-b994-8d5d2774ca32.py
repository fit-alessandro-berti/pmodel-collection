# Generated from: 937e61c5-439a-42d9-b994-8d5d2774ca32.json
# Description: This process involves integrating ideas from unrelated industries to create groundbreaking products or services. It starts with trend scouting in multiple sectors, followed by cross-functional brainstorming sessions that challenge conventional boundaries. Prototypes are rapidly developed using agile sprints, incorporating feedback from diverse user groups. Parallel market simulations assess potential impact and feasibility. Intellectual property strategies are crafted concurrently to safeguard novel concepts. The process concludes with a phased rollout plan that leverages partnerships across industries to maximize reach and adoption while continuously gathering data for iterative improvements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
trend_scouting = Transition(label='Trend Scouting')
idea_capture = Transition(label='Idea Capture')
cross_brainstorm = Transition(label='Cross Brainstorm')
concept_filter = Transition(label='Concept Filter')
rapid_prototype = Transition(label='Rapid Prototype')
user_feedback = Transition(label='User Feedback')
market_simulate = Transition(label='Market Simulate')
feasibility_check = Transition(label='Feasibility Check')
ip_strategy = Transition(label='IP Strategy')
partner_align = Transition(label='Partner Align')
pilot_launch = Transition(label='Pilot Launch')
data_monitor = Transition(label='Data Monitor')
iterate_design = Transition(label='Iterate Design')
scale_plan = Transition(label='Scale Plan')
adoption_boost = Transition(label='Adoption Boost')

# Loop: after Feedback and iterations 
# We model iteration as a loop over (Iterate Design) and (Rapid Prototype + User Feedback)
# The loop body B is Iterate Design,
# The loop "A" part before loop is Rapid Prototype + User Feedback,
# Because the description: prototypes developed, feedback incorporated, then done or iterate

# Build partial order for loop body "A": rapid prototype -> user feedback
prototype_feedback = StrictPartialOrder(nodes=[rapid_prototype, user_feedback])
prototype_feedback.order.add_edge(rapid_prototype, user_feedback)

# Loop node: execute prototype_feedback, then choose exit or execute iterate_design then prototype_feedback again
loop_body = OperatorPOWL(operator=Operator.LOOP, children=[prototype_feedback, iterate_design])

# Parallel assessments: market simulate + feasibility check (feasibility depends on market simulate)
market_feasibility = StrictPartialOrder(nodes=[market_simulate, feasibility_check])
market_feasibility.order.add_edge(market_simulate, feasibility_check)

# IP strategy runs concurrently with market_feasibility
concurrent_assessments = StrictPartialOrder(nodes=[market_feasibility, ip_strategy])
# No edges between market_feasibility and ip_strategy for concurrency

# After cross brainstorm and concept filter, proceed to loop over prototyping/iteration and parallel assessments
post_brainstorm = StrictPartialOrder(nodes=[loop_body, concurrent_assessments])
# No order edges: both can start concurrently after concept filter

# Rollout plan: partner align -> pilot launch -> data monitor -> scale plan -> adoption boost
rollout = StrictPartialOrder(nodes=[partner_align, pilot_launch, data_monitor, scale_plan, adoption_boost])
rollout.order.add_edge(partner_align, pilot_launch)
rollout.order.add_edge(pilot_launch, data_monitor)
rollout.order.add_edge(data_monitor, scale_plan)
rollout.order.add_edge(scale_plan, adoption_boost)

# Full linear sequence at start: trend scouting -> idea capture -> cross brainstorm -> concept filter
start_sequence = StrictPartialOrder(nodes=[trend_scouting, idea_capture, cross_brainstorm, concept_filter])
start_sequence.order.add_edge(trend_scouting, idea_capture)
start_sequence.order.add_edge(idea_capture, cross_brainstorm)
start_sequence.order.add_edge(cross_brainstorm, concept_filter)

# Between concept filter and post_brainstorm (loop_body + concurrent assessments)
# concept_filter -> loop_body & concurrent_assessments (both start together)
# So edges: concept_filter -> loop_body, concept_filter -> concurrent_assessments

# Finally, post_brainstorm -> rollout -> iterate_design is not direct: iterate_design is inside loop
# rollout starts after post_brainstorm (i.e., after prototyping/ assessments are done)
# So we add edges:
# for post_brainstorm nodes, the ending nodes are loop_body and concurrent_assessments
# Add edges from both loop_body and concurrent_assessments to partner_align

root_nodes = [
    start_sequence,
    post_brainstorm,
    rollout
]

root = StrictPartialOrder(nodes=root_nodes)

# Add edges for synchronization between start_sequence and post_brainstorm
root.order.add_edge(start_sequence, post_brainstorm)  # concept_filter -> loop_body and concurrent assessments (inside post_brainstorm)

# Add edges from post_brainstorm to rollout
root.order.add_edge(post_brainstorm, rollout)