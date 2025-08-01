# Generated from: 70234397-c44e-46e4-9318-aaf8740e4716.json
# Description: This process outlines the intricate steps involved in commissioning custom artwork from initial client inquiry to final delivery and feedback collection. It begins with client briefing and concept approval, followed by iterative design adjustments, material sourcing, and multi-phase quality inspections. The workflow incorporates unconventional activities such as legal rights negotiation and digital archiving of the artwork. Additionally, it includes coordination with logistics for special packaging and international shipping, ensuring the artwork remains secure and pristine. The process concludes with client onboarding for future collaborations and post-delivery support, emphasizing personalized communication and relationship management to foster long-term partnerships between the artist and client.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
client_inquiry    = Transition(label='Client Inquiry')
brief_review      = Transition(label='Brief Review')
concept_draft     = Transition(label='Concept Draft')
approval_check    = Transition(label='Approval Check')
design_adjust     = Transition(label='Design Adjust')
material_source   = Transition(label='Material Source')
rights_negotiate  = Transition(label='Rights Negotiate')
prototype_build   = Transition(label='Prototype Build')
quality_inspect   = Transition(label='Quality Inspect')
packaging_prep    = Transition(label='Packaging Prep')
logistics_plan    = Transition(label='Logistics Plan')
shipment_track    = Transition(label='Shipment Track')
delivery_confirm  = Transition(label='Delivery Confirm')
client_feedback   = Transition(label='Client Feedback')
archive_digital   = Transition(label='Archive Digital')
support_setup     = Transition(label='Support Setup')
future_onboard    = Transition(label='Future Onboard')

# Loop for iterative design: Concept Draft -> Approval Check, if not approved do Design Adjust then repeat
concept_seq = StrictPartialOrder(nodes=[concept_draft, approval_check])
concept_seq.order.add_edge(concept_draft, approval_check)
concept_loop = OperatorPOWL(operator=Operator.LOOP, children=[concept_seq, design_adjust])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    client_inquiry, brief_review, concept_loop,
    material_source, rights_negotiate, prototype_build,
    quality_inspect, archive_digital,
    packaging_prep, logistics_plan, shipment_track,
    delivery_confirm, client_feedback, support_setup, future_onboard
])

# Define the control-flow edges
root.order.add_edge(client_inquiry, brief_review)
root.order.add_edge(brief_review, concept_loop)
root.order.add_edge(concept_loop, material_source)
root.order.add_edge(material_source, rights_negotiate)
root.order.add_edge(rights_negotiate, prototype_build)
# After building prototype, archiving and quality inspection can proceed in parallel
root.order.add_edge(prototype_build, quality_inspect)
root.order.add_edge(prototype_build, archive_digital)
# Continue with packaging and shipping
root.order.add_edge(quality_inspect, packaging_prep)
root.order.add_edge(packaging_prep, logistics_plan)
root.order.add_edge(logistics_plan, shipment_track)
root.order.add_edge(shipment_track, delivery_confirm)
# Post-delivery: feedback, support setup, and future onboarding in parallel
root.order.add_edge(delivery_confirm, client_feedback)
root.order.add_edge(delivery_confirm, support_setup)
root.order.add_edge(delivery_confirm, future_onboard)