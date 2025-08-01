# Generated from: 8517d032-75da-4e64-9aa6-ff2cfb53455b.json
# Description: This process outlines the end-to-end workflow for managing custom art commissions in a boutique studio. It begins with client inquiry and concept ideation, followed by detailed proposal drafting and contract agreement. Once approved, the artist performs research and preliminary sketches before proceeding to the main artwork creation. Throughout the process, feedback loops ensure alignment with client expectations. After final approval, high-resolution digitalization and packaging preparation occur, concluding with delivery and post-sale support including archival and client follow-up for future commissions or referrals. This atypical workflow balances creative flexibility with structured project management to ensure both artistic integrity and client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
client_inquiry = Transition(label='Client Inquiry')
concept_ideation = Transition(label='Concept Ideation')
proposal_draft = Transition(label='Proposal Draft')
contract_agree = Transition(label='Contract Agree')
artist_research = Transition(label='Artist Research')
sketch_review = Transition(label='Sketch Review')
material_sourcing = Transition(label='Material Sourcing')
base_painting = Transition(label='Base Painting')
detailing_phase = Transition(label='Detailing Phase')
client_feedback = Transition(label='Client Feedback')
revision_cycle = Transition(label='Revision Cycle')
final_approval = Transition(label='Final Approval')
digital_capture = Transition(label='Digital Capture')
packaging_prep = Transition(label='Packaging Prep')
delivery_setup = Transition(label='Delivery Setup')
post_support = Transition(label='Post Support')
archival_store = Transition(label='Archival Store')
client_followup = Transition(label='Client Followup')

# Define loops and feedback

# Feedback loop from Client Feedback to Revision Cycle to Material Sourcing and onward again
# Revision cycle leads back to Material Sourcing, Base Painting, Detailing Phase, Client Feedback
# We'll model the creative phases and feedback as a loop:
# loop_body = StrictPartialOrder of Material Sourcing --> Base Painting --> Detailing Phase --> Client Feedback
po_creative_cycle = StrictPartialOrder(nodes=[material_sourcing, base_painting, detailing_phase, client_feedback])
po_creative_cycle.order.add_edge(material_sourcing, base_painting)
po_creative_cycle.order.add_edge(base_painting, detailing_phase)
po_creative_cycle.order.add_edge(detailing_phase, client_feedback)

# The loop is: do po_creative_cycle, then choice between exit or do revision_cycle then again po_creative_cycle
revision_loop = OperatorPOWL(operator=Operator.LOOP, children=[po_creative_cycle, revision_cycle])

# After final approval, sequence of Digital Capture -> Packaging Prep -> Delivery Setup -> Post Support
po_finish = StrictPartialOrder(nodes=[digital_capture, packaging_prep, delivery_setup, post_support])
po_finish.order.add_edge(digital_capture, packaging_prep)
po_finish.order.add_edge(packaging_prep, delivery_setup)
po_finish.order.add_edge(delivery_setup, post_support)

# Post Support leads to Archival Store and Client Followup concurrently
po_post = StrictPartialOrder(nodes=[archival_store, client_followup])
# no order edges -> concurrent

# Compose post_support with po_post to maintain order: Post Support --> (Archival Store and Client Followup concurrent)
po_finish_plus_post = StrictPartialOrder(nodes=[post_support, archival_store, client_followup])
po_finish_plus_post.order.add_edge(post_support, archival_store)
po_finish_plus_post.order.add_edge(post_support, client_followup)

# Sequence to connect everything from start to end:

# Initial chain: Client Inquiry -> Concept Ideation -> Proposal Draft -> Contract Agree
po_start = StrictPartialOrder(nodes=[client_inquiry, concept_ideation, proposal_draft, contract_agree])
po_start.order.add_edge(client_inquiry, concept_ideation)
po_start.order.add_edge(concept_ideation, proposal_draft)
po_start.order.add_edge(proposal_draft, contract_agree)

# After contract agree, sequence: Artist Research -> Sketch Review -> revision_loop
po_mid = StrictPartialOrder(nodes=[artist_research, sketch_review, revision_loop])
po_mid.order.add_edge(artist_research, sketch_review)
po_mid.order.add_edge(sketch_review, revision_loop)

# After loop and client feedback finalization, go to Final Approval
# Final Approval comes after revision_loop finishes
po_post_loop = StrictPartialOrder(nodes=[revision_loop, final_approval])
po_post_loop.order.add_edge(revision_loop, final_approval)

# Connect final approval to po_finish_plus_post
po_end = StrictPartialOrder(nodes=[final_approval, digital_capture, packaging_prep, delivery_setup, post_support, archival_store, client_followup])
po_end.order.add_edge(final_approval, digital_capture)
po_end.order.add_edge(digital_capture, packaging_prep)
po_end.order.add_edge(packaging_prep, delivery_setup)
po_end.order.add_edge(delivery_setup, post_support)
po_end.order.add_edge(post_support, archival_store)
po_end.order.add_edge(post_support, client_followup)

# Now combine all into root StrictPartialOrder for overall process:
# nodes: all atomic and operator nodes
nodes = [
    client_inquiry, concept_ideation, proposal_draft, contract_agree,
    artist_research, sketch_review, revision_loop,
    final_approval,
    digital_capture, packaging_prep, delivery_setup, post_support,
    archival_store, client_followup
]

root = StrictPartialOrder(nodes=nodes)

# Add order edges to root:

# Start chain
root.order.add_edge(client_inquiry, concept_ideation)
root.order.add_edge(concept_ideation, proposal_draft)
root.order.add_edge(proposal_draft, contract_agree)

# Post contract agree chain
root.order.add_edge(contract_agree, artist_research)
root.order.add_edge(artist_research, sketch_review)
root.order.add_edge(sketch_review, revision_loop)

# After loop to final approval
root.order.add_edge(revision_loop, final_approval)

# Finish sequence
root.order.add_edge(final_approval, digital_capture)
root.order.add_edge(digital_capture, packaging_prep)
root.order.add_edge(packaging_prep, delivery_setup)
root.order.add_edge(delivery_setup, post_support)

# Post support splits to archival and followup concurrently
root.order.add_edge(post_support, archival_store)
root.order.add_edge(post_support, client_followup)