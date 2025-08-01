# Generated from: 35e87503-c00c-4607-9dea-5df68b84e108.json
# Description: This process outlines the end-to-end workflow for commissioning bespoke artwork tailored to individual client preferences. It begins with initial client inquiry and concept briefing, proceeds through iterative design proposals and client feedback sessions, incorporates material sourcing and artist scheduling, and culminates in final production, quality assurance, packaging, and delivery. Throughout, the process involves coordination between multiple stakeholders including clients, artists, suppliers, and logistics, ensuring custom specifications are met while managing timelines and budgets efficiently. Post-delivery follow-ups and archival documentation close the cycle, enabling repeat business and portfolio enhancement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ClientInquiry = Transition(label='Client Inquiry')
ConceptBrief = Transition(label='Concept Brief')
DesignDraft = Transition(label='Design Draft')
FeedbackReview = Transition(label='Feedback Review')
MaterialSourcing = Transition(label='Material Sourcing')
ArtistScheduling = Transition(label='Artist Scheduling')
PrototypeCreation = Transition(label='Prototype Creation')
QualityCheck = Transition(label='Quality Check')
ClientApproval = Transition(label='Client Approval')
FinalProduction = Transition(label='Final Production')
PackagingPrep = Transition(label='Packaging Prep')
ShippingArrange = Transition(label='Shipping Arrange')
DeliveryConfirm = Transition(label='Delivery Confirm')
PostFollowup = Transition(label='Post Followup')
ArchiveRecords = Transition(label='Archive Records')

# Loop for iterative design proposals and client feedback:
# Loop body: (DesignDraft then FeedbackReview)
design_loop_body = StrictPartialOrder(nodes=[DesignDraft, FeedbackReview])
design_loop_body.order.add_edge(DesignDraft, FeedbackReview)

# Loop with exit after FeedbackReview
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[DesignDraft, FeedbackReview])

# Actually, the LOOP operator in pm4py has children [first, loopBody],
# where the semantics is: first → (loopBody → first)* → exit
# We want the loop:
# first: DesignDraft (start of iteration),
# loopBody: FeedbackReview (after design draft),
# so it loops: DesignDraft → FeedbackReview → (loop again or exit)
# Thus children=[DesignDraft, FeedbackReview]

design_loop = OperatorPOWL(operator=Operator.LOOP, children=[DesignDraft, FeedbackReview])

# Partial order for the main workflow sequence
# Start: ClientInquiry → ConceptBrief → design_loop → MaterialSourcing & ArtistScheduling (concurrent) → PrototypeCreation →
# QualityCheck → ClientApproval → FinalProduction → PackagingPrep → ShippingArrange → DeliveryConfirm →
# PostFollowup → ArchiveRecords

# Create concurrent node for MaterialSourcing and ArtistScheduling
mat_art = StrictPartialOrder(nodes=[MaterialSourcing, ArtistScheduling])

# Define the main sequence partial order
nodes = [
    ClientInquiry,
    ConceptBrief,
    design_loop,
    mat_art,
    PrototypeCreation,
    QualityCheck,
    ClientApproval,
    FinalProduction,
    PackagingPrep,
    ShippingArrange,
    DeliveryConfirm,
    PostFollowup,
    ArchiveRecords,
]

root = StrictPartialOrder(nodes=nodes)

root.order.add_edge(ClientInquiry, ConceptBrief)
root.order.add_edge(ConceptBrief, design_loop)
root.order.add_edge(design_loop, mat_art)
root.order.add_edge(mat_art, PrototypeCreation)
root.order.add_edge(PrototypeCreation, QualityCheck)
root.order.add_edge(QualityCheck, ClientApproval)
root.order.add_edge(ClientApproval, FinalProduction)
root.order.add_edge(FinalProduction, PackagingPrep)
root.order.add_edge(PackagingPrep, ShippingArrange)
root.order.add_edge(ShippingArrange, DeliveryConfirm)
root.order.add_edge(DeliveryConfirm, PostFollowup)
root.order.add_edge(PostFollowup, ArchiveRecords)