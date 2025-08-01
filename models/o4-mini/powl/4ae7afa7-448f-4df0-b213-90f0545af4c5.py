# Generated from: 4ae7afa7-448f-4df0-b213-90f0545af4c5.json
# Description: This process orchestrates a continuous cycle of innovation by leveraging a global crowd of contributors. It begins with idea submission through an open platform, followed by community voting to prioritize concepts. Selected ideas undergo collaborative refinement via virtual workshops, integrating diverse expertise. Prototypes are then developed using decentralized resources and tested in multiple real-world environments. Feedback loops from testers and stakeholders drive iterative improvements. The process concludes with scalable implementation and knowledge sharing across the community, fostering sustained innovation and collective ownership while managing intellectual property transparently.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# -- Define atomic activities as transitions --
idea_submit      = Transition(label='Idea Submit')
community_vote   = Transition(label='Community Vote')
concept_refine   = Transition(label='Concept Refine')
workshop_host    = Transition(label='Workshop Host')
expert_review    = Transition(label='Expert Review')
resource_allocate= Transition(label='Resource Allocate')
prototype_build  = Transition(label='Prototype Build')
field_test       = Transition(label='Field Test')
feedback_collect = Transition(label='Feedback Collect')
iterate_design   = Transition(label='Iterate Design')
ip_register      = Transition(label='IP Register')
scale_deploy     = Transition(label='Scale Deploy')
impact_assess    = Transition(label='Impact Assess')
knowledge_share  = Transition(label='Knowledge Share')
community_reward = Transition(label='Community Reward')
data_archive     = Transition(label='Data Archive')

# -- Silent transition for choices/exits --
skip = SilentTransition()

# -- 1) Concept refinement: Concept Refine -> (Workshop Host & Expert Review in parallel) --
refine_po = StrictPartialOrder(nodes=[concept_refine, workshop_host, expert_review])
refine_po.order.add_edge(concept_refine, workshop_host)
refine_po.order.add_edge(concept_refine, expert_review)

# -- XOR choice: either refine or drop the idea --
refine_choice = OperatorPOWL(operator=Operator.XOR, children=[refine_po, skip])

# -- 2) Prototype/Test/Feedback loop: RA -> Build -> Test -> Collect -->
proto_body = StrictPartialOrder(nodes=[resource_allocate, prototype_build, field_test, feedback_collect])
proto_body.order.add_edge(resource_allocate, prototype_build)
proto_body.order.add_edge(prototype_build, field_test)
proto_body.order.add_edge(field_test, feedback_collect)

# Loop: do proto_body, then optionally iterate_design, then proto_body again, ...
proto_loop = OperatorPOWL(operator=Operator.LOOP, children=[proto_body, iterate_design])

# -- 3) Post‐loop implementation & sharing --
post_nodes = [
    ip_register,
    scale_deploy,
    impact_assess,
    knowledge_share,
    community_reward,
    data_archive
]
post_po = StrictPartialOrder(nodes=post_nodes)
post_po.order.add_edge(ip_register, scale_deploy)
# after scale_deploy, do impact, share, reward in parallel
post_po.order.add_edge(scale_deploy, impact_assess)
post_po.order.add_edge(scale_deploy, knowledge_share)
post_po.order.add_edge(scale_deploy, community_reward)
# finally archive once all three are done
post_po.order.add_edge(impact_assess, data_archive)
post_po.order.add_edge(knowledge_share, data_archive)
post_po.order.add_edge(community_reward, data_archive)

# -- 4) Assemble the full workflow in a single partial order --
root = StrictPartialOrder(nodes=[
    idea_submit,
    community_vote,
    refine_choice,
    proto_loop,
    ip_register,
    scale_deploy,
    impact_assess,
    knowledge_share,
    community_reward,
    data_archive
])

# define the ordering between phases
root.order.add_edge(idea_submit, community_vote)
root.order.add_edge(community_vote, refine_choice)
root.order.add_edge(refine_choice, proto_loop)
root.order.add_edge(proto_loop, ip_register)
# (the edges inside post_po handle ip_register -> ... -> data_archive)