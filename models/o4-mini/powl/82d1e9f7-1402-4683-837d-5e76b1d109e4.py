# Generated from: 82d1e9f7-1402-4683-837d-5e76b1d109e4.json
# Description: This process facilitates the structured collaboration between multiple industries to co-create innovative solutions by leveraging diverse expertise. It begins with idea scouting across sectors, followed by joint feasibility studies and resource pooling. Iterative prototyping occurs with continuous feedback loops, incorporating legal and regulatory assessments. The process emphasizes knowledge transfer through workshops and shared digital platforms, culminating in a pilot deployment and market impact analysis. Post-launch, lessons learned sessions ensure refinement and scalability potential, fostering long-term strategic partnerships and continuous innovation cycles beyond traditional industry boundaries.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
idea_scout     = Transition(label='Idea Scouting')
partner_vet    = Transition(label='Partner Vetting')
feas_check     = Transition(label='Feasibility Check')
resource_pool  = Transition(label='Resource Pooling')
concept_design = Transition(label='Concept Design')
risk_review    = Transition(label='Risk Review')
prototype_build= Transition(label='Prototype Build')
user_test      = Transition(label='User Testing')
legal_rev      = Transition(label='Legal Review')
workshop       = Transition(label='Workshop Hosting')
data_share     = Transition(label='Data Sharing')
pilot_launch   = Transition(label='Pilot Launch')
impact_study   = Transition(label='Impact Study')
feedback_loop  = Transition(label='Feedback Loop')
lessons_learned= Transition(label='Lessons Learned')
scaling_plan   = Transition(label='Scaling Plan')

# Build the prototyping + legal/feedback loop
loop_body = StrictPartialOrder(nodes=[user_test, feedback_loop, legal_rev])
loop_body.order.add_edge(user_test, feedback_loop)
loop_body.order.add_edge(feedback_loop, legal_rev)

prot_loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, loop_body])

# Knowledge‐transfer happens concurrently (workshop & data sharing)
knowledge_transfer = StrictPartialOrder(nodes=[workshop, data_share])
# no edges → they can occur in parallel

# Assemble the full workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    idea_scout,
    partner_vet,
    feas_check,
    resource_pool,
    concept_design,
    risk_review,
    prot_loop,
    knowledge_transfer,
    pilot_launch,
    impact_study,
    lessons_learned,
    scaling_plan
])

# Sequence constraints
root.order.add_edge(idea_scout, partner_vet)
root.order.add_edge(partner_vet, feas_check)
root.order.add_edge(feas_check, resource_pool)
root.order.add_edge(resource_pool, concept_design)
root.order.add_edge(concept_design, risk_review)
root.order.add_edge(risk_review, prot_loop)
root.order.add_edge(prot_loop, knowledge_transfer)
root.order.add_edge(knowledge_transfer, pilot_launch)
root.order.add_edge(pilot_launch, impact_study)
root.order.add_edge(impact_study, lessons_learned)
root.order.add_edge(lessons_learned, scaling_plan)