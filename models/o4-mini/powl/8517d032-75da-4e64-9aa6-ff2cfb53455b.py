# Generated from: 8517d032-75da-4e64-9aa6-ff2cfb53455b.json
# Description: This process outlines the end-to-end workflow for managing custom art commissions in a boutique studio. It begins with client inquiry and concept ideation, followed by detailed proposal drafting and contract agreement. Once approved, the artist performs research and preliminary sketches before proceeding to the main artwork creation. Throughout the process, feedback loops ensure alignment with client expectations. After final approval, high-resolution digitalization and packaging preparation occur, concluding with delivery and post-sale support including archival and client follow-up for future commissions or referrals. This atypical workflow balances creative flexibility with structured project management to ensure both artistic integrity and client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
CI = Transition(label='Client Inquiry')
CIdeation = Transition(label='Concept Ideation')
PDraft = Transition(label='Proposal Draft')
CAgree = Transition(label='Contract Agree')
AResearch = Transition(label='Artist Research')
SketchReview = Transition(label='Sketch Review')
MaterialSourcing = Transition(label='Material Sourcing')
BasePainting = Transition(label='Base Painting')
DetailingPhase = Transition(label='Detailing Phase')
ClientFeedback = Transition(label='Client Feedback')
RevisionCycle = Transition(label='Revision Cycle')
FinalApproval = Transition(label='Final Approval')
DigitalCapture = Transition(label='Digital Capture')
PackagingPrep = Transition(label='Packaging Prep')
DeliverySetup = Transition(label='Delivery Setup')
PostSupport = Transition(label='Post Support')
ArchivalStore = Transition(label='Archival Store')
ClientFollowup = Transition(label='Client Followup')

# Define the body of the feedback loop: research → sketch → materials → base → detail
A = StrictPartialOrder(nodes=[
    AResearch, SketchReview, MaterialSourcing, BasePainting, DetailingPhase
])
A.order.add_edge(AResearch, SketchReview)
A.order.add_edge(SketchReview, MaterialSourcing)
A.order.add_edge(MaterialSourcing, BasePainting)
A.order.add_edge(BasePainting, DetailingPhase)

# Define the redo part of the loop: client feedback → revision
B = StrictPartialOrder(nodes=[ClientFeedback, RevisionCycle])
B.order.add_edge(ClientFeedback, RevisionCycle)

# Loop: do A, then either exit or do B and repeat A
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Build the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    CI, CIdeation, PDraft, CAgree, loop,
    FinalApproval, DigitalCapture, PackagingPrep, DeliverySetup,
    PostSupport, ArchivalStore, ClientFollowup
])
root.order.add_edge(CI, CIdeation)
root.order.add_edge(CIdeation, PDraft)
root.order.add_edge(PDraft, CAgree)
root.order.add_edge(CAgree, loop)
root.order.add_edge(loop, FinalApproval)
root.order.add_edge(FinalApproval, DigitalCapture)
root.order.add_edge(DigitalCapture, PackagingPrep)
root.order.add_edge(PackagingPrep, DeliverySetup)
root.order.add_edge(DeliverySetup, PostSupport)
root.order.add_edge(PostSupport, ArchivalStore)
root.order.add_edge(PostSupport, ClientFollowup)