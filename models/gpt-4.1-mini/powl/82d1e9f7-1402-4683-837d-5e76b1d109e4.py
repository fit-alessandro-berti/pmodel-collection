# Generated from: 82d1e9f7-1402-4683-837d-5e76b1d109e4.json
# Description: This process facilitates the structured collaboration between multiple industries to co-create innovative solutions by leveraging diverse expertise. It begins with idea scouting across sectors, followed by joint feasibility studies and resource pooling. Iterative prototyping occurs with continuous feedback loops, incorporating legal and regulatory assessments. The process emphasizes knowledge transfer through workshops and shared digital platforms, culminating in a pilot deployment and market impact analysis. Post-launch, lessons learned sessions ensure refinement and scalability potential, fostering long-term strategic partnerships and continuous innovation cycles beyond traditional industry boundaries.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
idea_scouting = Transition(label='Idea Scouting')
partner_vetting = Transition(label='Partner Vetting')
feasibility_check = Transition(label='Feasibility Check')
resource_pooling = Transition(label='Resource Pooling')
concept_design = Transition(label='Concept Design')
risk_review = Transition(label='Risk Review')
prototype_build = Transition(label='Prototype Build')
user_testing = Transition(label='User Testing')
legal_review = Transition(label='Legal Review')
workshop_hosting = Transition(label='Workshop Hosting')
data_sharing = Transition(label='Data Sharing')
pilot_launch = Transition(label='Pilot Launch')
impact_study = Transition(label='Impact Study')
feedback_loop = Transition(label='Feedback Loop')
lessons_learned = Transition(label='Lessons Learned')
scaling_plan = Transition(label='Scaling Plan')

skip = SilentTransition()

# Model the Feedback Loop after prototyping with continuous feedback and legal review
# Loop: execute prototype_build, then feedback_loop and legal_review concurrently, then either exit or repeat
feedback_and_legal_po = StrictPartialOrder(nodes=[feedback_loop, legal_review])
# no order edges between feedback_loop and legal_review -> concurrent

loop_prototype = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        prototype_build,
        feedback_and_legal_po
    ]
)

# Knowledge transfer activities (workshops and data sharing) concurrent after loop
knowledge_transfer_po = StrictPartialOrder(nodes=[workshop_hosting, data_sharing])

# Pilot launch followed by impact study in order
pilot_impact_po = StrictPartialOrder(nodes=[pilot_launch, impact_study])
pilot_impact_po.order.add_edge(pilot_launch, impact_study)

# Lessons learned then scaling plan in order
lessons_scaling_po = StrictPartialOrder(nodes=[lessons_learned, scaling_plan])
lessons_scaling_po.order.add_edge(lessons_learned, scaling_plan)

# Post launch refinement phases in strict order:
# pilot_impact_po --> lessons_scaling_po
post_launch_po = StrictPartialOrder(nodes=[pilot_impact_po, lessons_scaling_po])
post_launch_po.order.add_edge(pilot_impact_po, lessons_scaling_po)

# Early phases: Idea scouting -> partner vetting -> feasibility check and resource pooling concurrently
early_feasibility_po = StrictPartialOrder(nodes=[feasibility_check, resource_pooling])
# no order edges between feasibility_check and resource_pooling - concurrent

early_phase_po = StrictPartialOrder(nodes=[idea_scouting, partner_vetting, early_feasibility_po])
early_phase_po.order.add_edge(idea_scouting, partner_vetting)
early_phase_po.order.add_edge(partner_vetting, early_feasibility_po)

# Concept design and risk review concurrent after feasibility/resource pooling
concept_risk_po = StrictPartialOrder(nodes=[concept_design, risk_review])
# no edges => concurrent

early_middle_po = StrictPartialOrder(
    nodes=[early_phase_po, concept_risk_po]
)
early_middle_po.order.add_edge(early_phase_po, concept_risk_po)

# User testing after loop prototype (which contains prototyping + feedback/ legal reviews)
user_testing_follow = StrictPartialOrder(
    nodes=[loop_prototype, user_testing]
)
user_testing_follow.order.add_edge(loop_prototype, user_testing)

# Knowledge transfer after user testing
knowledge_after_testing_po = StrictPartialOrder(
    nodes=[user_testing_follow, knowledge_transfer_po]
)
knowledge_after_testing_po.order.add_edge(user_testing_follow, knowledge_transfer_po)

# Pilot launch sequence after knowledge transfer
full_after_knowledge_po = StrictPartialOrder(
    nodes=[knowledge_after_testing_po, post_launch_po]
)
full_after_knowledge_po.order.add_edge(knowledge_after_testing_po, post_launch_po)

# Combine all main parts into the root PO:
# early_middle_po --> full_after_knowledge_po
root = StrictPartialOrder(
    nodes=[early_middle_po, full_after_knowledge_po]
)
root.order.add_edge(early_middle_po, full_after_knowledge_po)