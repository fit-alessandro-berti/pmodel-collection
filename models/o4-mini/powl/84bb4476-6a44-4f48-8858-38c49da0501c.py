# Generated from: 84bb4476-6a44-4f48-8858-38c49da0501c.json
# Description: This process orchestrates the convergence of disparate industry insights to foster breakthrough innovations. It begins with trend spotting across multiple sectors, followed by cross-functional ideation sessions where specialists from unrelated fields collaborate. Prototypes are developed using hybrid technologies, then subjected to multi-domain feasibility and impact assessments. Stakeholder engagement spans beyond traditional partners to include community feedback and regulatory foresight. Iterative refinement incorporates lessons from pilot deployments in diverse market conditions, ensuring adaptability and scalability before final rollout. Continuous knowledge sharing and post-launch analytics close the loop, enabling sustained innovation in a complex, interconnected ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t_trend_spotting   = Transition(label='Trend Spotting')
t_idea_mining      = Transition(label='Idea Mining')
t_cross_pollinate  = Transition(label='Cross Pollinate')
t_concept_sketch   = Transition(label='Concept Sketch')
t_tech_fusion      = Transition(label='Tech Fusion')
t_proto_build      = Transition(label='Proto Build')
t_feasibility_test = Transition(label='Feasibility Test')
t_impact_review    = Transition(label='Impact Review')
t_stakeholder_sync = Transition(label='Stakeholder Sync')
t_community_input  = Transition(label='Community Input')
t_regulatory_scan  = Transition(label='Regulatory Scan')
t_pilot_deploy     = Transition(label='Pilot Deploy')
t_data_capture     = Transition(label='Data Capture')
t_iterate_design   = Transition(label='Iterate Design')
t_scale_plan       = Transition(label='Scale Plan')
t_knowledge_share  = Transition(label='Knowledge Share')
t_launch_review    = Transition(label='Launch Review')

# Define the iterative refinement loop:
#   Body A: Pilot Deploy -> Data Capture -> Iterate Design
loop_body = StrictPartialOrder(nodes=[t_pilot_deploy, t_data_capture, t_iterate_design])
loop_body.order.add_edge(t_pilot_deploy, t_data_capture)
loop_body.order.add_edge(t_data_capture, t_iterate_design)

#   Body B: Scale Plan -> Knowledge Share
scale_and_share = StrictPartialOrder(nodes=[t_scale_plan, t_knowledge_share])
scale_and_share.order.add_edge(t_scale_plan, t_knowledge_share)

# Loop operator: do A, then either exit or do B then A again
iterative_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, scale_and_share])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    t_trend_spotting,
    t_idea_mining,
    t_cross_pollinate,
    t_concept_sketch,
    t_tech_fusion,
    t_proto_build,
    t_feasibility_test,
    t_impact_review,
    t_stakeholder_sync,
    t_community_input,
    t_regulatory_scan,
    iterative_loop,
    t_launch_review
])

# 1. Trend Spotting -> (Idea Mining ∥ Cross Pollinate)
root.order.add_edge(t_trend_spotting, t_idea_mining)
root.order.add_edge(t_trend_spotting, t_cross_pollinate)
# 2. Both ideation tasks complete before Concept Sketch
root.order.add_edge(t_idea_mining, t_concept_sketch)
root.order.add_edge(t_cross_pollinate, t_concept_sketch)
# 3. Sequential prototype development
root.order.add_edge(t_concept_sketch, t_tech_fusion)
root.order.add_edge(t_tech_fusion, t_proto_build)
# 4. Sequential assessments
root.order.add_edge(t_proto_build, t_feasibility_test)
root.order.add_edge(t_feasibility_test, t_impact_review)
# 5. Concurrent stakeholder engagement starts after Impact Review
root.order.add_edge(t_impact_review, t_stakeholder_sync)
root.order.add_edge(t_impact_review, t_community_input)
root.order.add_edge(t_impact_review, t_regulatory_scan)
# 6. After all engagements, enter the iterative refinement loop
root.order.add_edge(t_stakeholder_sync, iterative_loop)
root.order.add_edge(t_community_input, iterative_loop)
root.order.add_edge(t_regulatory_scan, iterative_loop)
# 7. After exiting the loop, do final rollout (Launch Review)
root.order.add_edge(iterative_loop, t_launch_review)