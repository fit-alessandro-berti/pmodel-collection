# Generated from: 4ae7afa7-448f-4df0-b213-90f0545af4c5.json
# Description: This process orchestrates a continuous cycle of innovation by leveraging a global crowd of contributors. It begins with idea submission through an open platform, followed by community voting to prioritize concepts. Selected ideas undergo collaborative refinement via virtual workshops, integrating diverse expertise. Prototypes are then developed using decentralized resources and tested in multiple real-world environments. Feedback loops from testers and stakeholders drive iterative improvements. The process concludes with scalable implementation and knowledge sharing across the community, fostering sustained innovation and collective ownership while managing intellectual property transparently.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
IdeaSubmit = Transition(label='Idea Submit')
CommunityVote = Transition(label='Community Vote')
ConceptRefine = Transition(label='Concept Refine')
WorkshopHost = Transition(label='Workshop Host')
ExpertReview = Transition(label='Expert Review')
ResourceAllocate = Transition(label='Resource Allocate')
PrototypeBuild = Transition(label='Prototype Build')
FieldTest = Transition(label='Field Test')
FeedbackCollect = Transition(label='Feedback Collect')
IterateDesign = Transition(label='Iterate Design')
IPRegister = Transition(label='IP Register')
ScaleDeploy = Transition(label='Scale Deploy')
ImpactAssess = Transition(label='Impact Assess')
KnowledgeShare = Transition(label='Knowledge Share')
CommunityReward = Transition(label='Community Reward')
DataArchive = Transition(label='Data Archive')

# Loop body: the iterative innovation cycle after idea submission and voting
# Define the refinement partial order of Concept Refine and WorkshopHost & ExpertReview in parallel
# WorkshopHost precedes ExpertReview (expert review follows workshop)
refine_order = StrictPartialOrder(nodes=[ConceptRefine, WorkshopHost, ExpertReview])
refine_order.order.add_edge(WorkshopHost, ExpertReview)
# ConceptRefine is concurrent with (WorkshopHost->ExpertReview), i.e. no order to/from ConceptRefine

# Prototype development partial order: ResourceAllocate --> PrototypeBuild --> FieldTest
prototype_order = StrictPartialOrder(nodes=[ResourceAllocate, PrototypeBuild, FieldTest])
prototype_order.order.add_edge(ResourceAllocate, PrototypeBuild)
prototype_order.order.add_edge(PrototypeBuild, FieldTest)

# Feedback and iteration partial order: FeedbackCollect --> IterateDesign
feedback_order = StrictPartialOrder(nodes=[FeedbackCollect, IterateDesign])
feedback_order.order.add_edge(FeedbackCollect, IterateDesign)

# Combine refinement, prototype and feedback partial orders in parallel within the loop body
# The order is:
# refine_order --> prototype_order --> feedback_order
# but prototype depends on refinement, and feedback depends on testing (field test), so connect edges accordingly
# So link ConceptRefine or ExpertReview to ResourceAllocate? It makes sense that prototype starts after ConceptRefine and ExpertReview.
# For simplicity, add edges from ExpertReview to ResourceAllocate to enforce prototype build starts after refinement
# And link FieldTest to FeedbackCollect to start feedback after testing

# Combine all nodes for loop body
loop_body_nodes = [refine_order, prototype_order, feedback_order]

# Create a partial order linking the nested POWL nodes accordingly
loop_body = StrictPartialOrder(nodes=loop_body_nodes)
loop_body.order.add_edge(refine_order, prototype_order)
loop_body.order.add_edge(prototype_order, feedback_order)

# Also add edge from ExpertReview (inside refine_order) to ResourceAllocate
# However, edges are between nodes of loop_body, not of refine_order.
# Thus, within refine_order and prototype_order, internal order established; at this level, we order the subprocesses.
# So only link overall refine_order to prototype_order and prototype_order to feedback_order

# Iterative loop: after feedback, iterate design then loop again
# Loop: A= loop_body, B= iterate design phase: IterateDesign then loop_body again
# Actually the "iterate design" is part of feedback_order already, but the description says feedback loop drives iterative improvements,
# so the iterate design and re-execute loop_body.

# We'll consider Loop with A= loop_body, and B = IterateDesign
# But IterateDesign is already in feedback_order.
# To make it clearer, split IterateDesign out as B of loop operator.

# Remove IterateDesign from feedback_order nodes
feedback_order = StrictPartialOrder(nodes=[FeedbackCollect])
# Reassign loop_body nodes accordingly
loop_body_nodes = [refine_order, prototype_order, feedback_order]
loop_body = StrictPartialOrder(nodes=loop_body_nodes)
loop_body.order.add_edge(refine_order, prototype_order)
loop_body.order.add_edge(prototype_order, feedback_order)

# B is IterateDesign alone
B = IterateDesign

# Construct loop: execute loop_body, then choose to exit (silent) or execute B then loop_body again
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, B])

# After loop finishes (exits), continue with IP Register, Scale Deploy, Impact Assess, Knowledge Share, Community Reward, Data Archive
# Some of these are probably sequential:
# IP Register --> Scale Deploy --> Impact Assess
# Impact Assess leads to Knowledge Share, Community Reward, Data Archive in parallel (no order)
post_loop_nodes = [
    IPRegister, 
    ScaleDeploy, 
    ImpactAssess, 
    KnowledgeShare,
    CommunityReward,
    DataArchive
]

post_loop = StrictPartialOrder(nodes=post_loop_nodes)
post_loop.order.add_edge(IPRegister, ScaleDeploy)
post_loop.order.add_edge(ScaleDeploy, ImpactAssess)

# ImpactAssess precedes the last three nodes
post_loop.order.add_edge(ImpactAssess, KnowledgeShare)
post_loop.order.add_edge(ImpactAssess, CommunityReward)
post_loop.order.add_edge(ImpactAssess, DataArchive)

# The overall starting sequence: Idea Submit --> Community Vote --> loop --> post loop
root_nodes = [IdeaSubmit, CommunityVote, loop, post_loop]

root = StrictPartialOrder(nodes=root_nodes)
root.order.add_edge(IdeaSubmit, CommunityVote)
root.order.add_edge(CommunityVote, loop)
root.order.add_edge(loop, post_loop)