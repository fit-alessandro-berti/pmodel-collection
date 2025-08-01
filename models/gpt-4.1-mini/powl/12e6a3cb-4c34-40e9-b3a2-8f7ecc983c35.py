# Generated from: 12e6a3cb-4c34-40e9-b3a2-8f7ecc983c35.json
# Description: This process outlines the steps involved in managing a bespoke art commission from initial client inquiry to final delivery. It includes client briefing, style exploration, iterative feedback loops, material sourcing, prototype creation, approval stages, and final packaging. The workflow ensures close collaboration between the artist and client to meet unique artistic requirements while maintaining quality and timelines, integrating digital and physical checkpoints along the way.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Client_Inquiry = Transition(label='Client Inquiry')
Brief_Gathering = Transition(label='Brief Gathering')
Style_Research = Transition(label='Style Research')
Concept_Sketch = Transition(label='Concept Sketch')
Initial_Proposal = Transition(label='Initial Proposal')
Client_Feedback = Transition(label='Client Feedback')
Revised_Draft = Transition(label='Revised Draft')
Material_Sourcing = Transition(label='Material Sourcing')
Prototype_Build = Transition(label='Prototype Build')
Internal_Review = Transition(label='Internal Review')
Client_Approval = Transition(label='Client Approval')
Final_Artwork = Transition(label='Final Artwork')
Quality_Check = Transition(label='Quality Check')
Packaging_Prep = Transition(label='Packaging Prep')
Shipment_Dispatch = Transition(label='Shipment Dispatch')
Post_Delivery = Transition(label='Post Delivery')
Feedback_Collection = Transition(label='Feedback Collection')

# Loop for iterative feedback and revisions:
# Loop body is the choice between exiting or repeating the loop.
# Loop structure: *(A, B) means perform A then either exit or do B then A again.
# Here:
#   A = Client_Feedback
#   B = Revised_Draft

feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Client_Feedback, Revised_Draft])

# Partial order before the loop:
# Client Inquiry --> Brief Gathering --> Style Research --> Concept Sketch --> Initial Proposal
# After Initial Proposal, enters feedback loop
pre_loop = StrictPartialOrder(nodes=[
    Client_Inquiry, Brief_Gathering, Style_Research, Concept_Sketch, Initial_Proposal
])
pre_loop.order.add_edge(Client_Inquiry, Brief_Gathering)
pre_loop.order.add_edge(Brief_Gathering, Style_Research)
pre_loop.order.add_edge(Style_Research, Concept_Sketch)
pre_loop.order.add_edge(Concept_Sketch, Initial_Proposal)

# Partial order after feedback loop:
# Material Sourcing --> Prototype Build --> Internal Review --> Client Approval
post_feedback = StrictPartialOrder(nodes=[
    Material_Sourcing, Prototype_Build, Internal_Review, Client_Approval
])
post_feedback.order.add_edge(Material_Sourcing, Prototype_Build)
post_feedback.order.add_edge(Prototype_Build, Internal_Review)
post_feedback.order.add_edge(Internal_Review, Client_Approval)

# Partial order after approval:
# Final Artwork --> Quality Check --> Packaging Prep --> Shipment Dispatch
approval_to_ship = StrictPartialOrder(nodes=[
    Final_Artwork, Quality_Check, Packaging_Prep, Shipment_Dispatch
])
approval_to_ship.order.add_edge(Final_Artwork, Quality_Check)
approval_to_ship.order.add_edge(Quality_Check, Packaging_Prep)
approval_to_ship.order.add_edge(Packaging_Prep, Shipment_Dispatch)

# Partial order for post-delivery:
# Post Delivery --> Feedback Collection
post_delivery = StrictPartialOrder(nodes=[Post_Delivery, Feedback_Collection])
post_delivery.order.add_edge(Post_Delivery, Feedback_Collection)

# Compose the main workflow partial order
# The sequence is:
# pre_loop --> feedback_loop --> post_feedback --> approval_to_ship --> post_delivery

root = StrictPartialOrder(nodes=[
    pre_loop,
    feedback_loop,
    post_feedback,
    approval_to_ship,
    post_delivery
])

root.order.add_edge(pre_loop, feedback_loop)
root.order.add_edge(feedback_loop, post_feedback)
root.order.add_edge(post_feedback, approval_to_ship)
root.order.add_edge(approval_to_ship, post_delivery)