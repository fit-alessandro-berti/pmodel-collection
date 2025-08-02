# Generated from: 56ed66fe-30dc-4240-be74-d778222e633d.json
# Description: This process involves leveraging a global community to generate, refine, and implement innovative ideas for a company’s product line. It starts with launching a challenge, collecting submissions, and then curating entries through multiple review stages including peer voting and expert evaluation. Selected ideas undergo prototyping, iterative feedback loops with contributors, and final validation before integration into the product roadmap. The process requires coordination across multiple teams, continuous engagement with external contributors, and adaptive resource allocation based on idea potential and community response. It ensures a dynamic flow of creativity while maintaining quality and strategic alignment with business goals.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Launch_Challenge = Transition(label='Launch Challenge')
Collect_Ideas = Transition(label='Collect Ideas')
Community_Voting = Transition(label='Community Voting')
Expert_Review = Transition(label='Expert Review')
Select_Winners = Transition(label='Select Winners')
Prototype_Build = Transition(label='Prototype Build')
Feedback_Loop = Transition(label='Feedback Loop')
Revise_Prototype = Transition(label='Revise Prototype')
Final_Validation = Transition(label='Final Validation')
Resource_Align = Transition(label='Resource Align')
Contributor_Engage = Transition(label='Contributor Engage')
Roadmap_Update = Transition(label='Roadmap Update')
Legal_Check = Transition(label='Legal Check')
IP_Filing = Transition(label='IP Filing')
Scale_Production = Transition(label='Scale Production')
Market_Test = Transition(label='Market Test')

# Silent transition for choice exit or loop exit
skip = SilentTransition()

# Feedback loops modeled as a LOOP operator: 
# Execute feedback loop (Feedback_Loop) then either exit or do Revise Prototype and then iterate the loop again.
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Revise_Prototype])

# Prototyping phase involves Prototype Build followed by the feedback loop
# So partial order: Prototype Build --> loop_feedback
proto_po = StrictPartialOrder(nodes=[Prototype_Build, loop_feedback])
proto_po.order.add_edge(Prototype_Build, loop_feedback)

# Coordinated resource align and contributor engage can be concurrent during prototyping and feedback loops
# So model resource align and contributor engage as concurrent with proto_po (non-blocking)
# We'll model this by creating a strict partial order of these two + proto_po nodes 
# but resource align and contributor engage have to start after select winners.

# After Select Winners, before prototyping:
# Resource Align and Contributor Engage run concurrently and in parallel with prototyping
# So first Select Winners, then all these 3 nodes (Resource Align, Contributor Engage, and proto_po) concurrent

# Create the parallel nodes after select winners
post_selection_nodes = [Resource_Align, Contributor_Engage, proto_po]

post_selection_po = StrictPartialOrder(nodes=post_selection_nodes)  # no order edges -> all concurrent

# Initial part: Launch Challenge --> Collect Ideas --> Community Voting --> Expert Review --> Select Winners
initial_po = StrictPartialOrder(nodes=[Launch_Challenge, Collect_Ideas, Community_Voting, Expert_Review, Select_Winners])
initial_po.order.add_edge(Launch_Challenge, Collect_Ideas)
initial_po.order.add_edge(Collect_Ideas, Community_Voting)
initial_po.order.add_edge(Community_Voting, Expert_Review)
initial_po.order.add_edge(Expert_Review, Select_Winners)

# After prototyping and resource engagement, final validation + legal check + ip filing done sequentially
final_checks_po = StrictPartialOrder(nodes=[Final_Validation, Legal_Check, IP_Filing])
final_checks_po.order.add_edge(Final_Validation, Legal_Check)
final_checks_po.order.add_edge(Legal_Check, IP_Filing)

# Production scaling and market test run concurrently but after final_checks_po
scale_and_test_po = StrictPartialOrder(nodes=[Scale_Production, Market_Test])

# After final checks update roadmap and then scale and test
# Roadmap update after final validation but logically should be after resource/contribution phases and final checks
# We will put Roadmap_Update after final_checks_po but before scale_and_test_po.

# Build order for the end:
# final_checks_po --> Roadmap_Update --> scale_and_test_po
end_po = StrictPartialOrder(nodes=[final_checks_po, Roadmap_Update, scale_and_test_po])
end_po.order.add_edge(final_checks_po, Roadmap_Update)
end_po.order.add_edge(Roadmap_Update, scale_and_test_po)

# Now combine all major parts into one top-level partial order:
# initial_po --> post_selection_po --> end_po
root = StrictPartialOrder(nodes=[initial_po, post_selection_po, end_po])
root.order.add_edge(initial_po, post_selection_po)
root.order.add_edge(post_selection_po, end_po)