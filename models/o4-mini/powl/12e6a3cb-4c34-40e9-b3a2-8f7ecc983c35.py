# Generated from: 12e6a3cb-4c34-40e9-b3a2-8f7ecc983c35.json
# Description: This process outlines the steps involved in managing a bespoke art commission from initial client inquiry to final delivery. It includes client briefing, style exploration, iterative feedback loops, material sourcing, prototype creation, approval stages, and final packaging. The workflow ensures close collaboration between the artist and client to meet unique artistic requirements while maintaining quality and timelines, integrating digital and physical checkpoints along the way.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
clientInquiry   = Transition(label="Client Inquiry")
briefGathering  = Transition(label="Brief Gathering")
styleResearch   = Transition(label="Style Research")
conceptSketch   = Transition(label="Concept Sketch")
initialProposal = Transition(label="Initial Proposal")
clientFeedback  = Transition(label="Client Feedback")
revisedDraft    = Transition(label="Revised Draft")
materialSourcing = Transition(label="Material Sourcing")
prototypeBuild   = Transition(label="Prototype Build")
internalReview   = Transition(label="Internal Review")
clientApproval   = Transition(label="Client Approval")
finalArtwork     = Transition(label="Final Artwork")
qualityCheck     = Transition(label="Quality Check")
packagingPrep    = Transition(label="Packaging Prep")
shipmentDispatch = Transition(label="Shipment Dispatch")
postDelivery     = Transition(label="Post Delivery")
feedbackCollection = Transition(label="Feedback Collection")

# Build the loop for the iterative feedback on the proposal
# A: Style Research -> Concept Sketch -> Initial Proposal
A = StrictPartialOrder(nodes=[styleResearch, conceptSketch, initialProposal])
A.order.add_edge(styleResearch, conceptSketch)
A.order.add_edge(conceptSketch, initialProposal)

# B: Client Feedback -> Revised Draft
B = StrictPartialOrder(nodes=[clientFeedback, revisedDraft])
B.order.add_edge(clientFeedback, revisedDraft)

proposalLoop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Build the overall workflow as a partial order
root = StrictPartialOrder(nodes=[
    clientInquiry,
    briefGathering,
    proposalLoop,
    materialSourcing,
    prototypeBuild,
    internalReview,
    clientApproval,
    finalArtwork,
    qualityCheck,
    packagingPrep,
    shipmentDispatch,
    postDelivery,
    feedbackCollection
])

# Define the control-flow edges
root.order.add_edge(clientInquiry, briefGathering)
root.order.add_edge(briefGathering, proposalLoop)
root.order.add_edge(proposalLoop, materialSourcing)
root.order.add_edge(materialSourcing, prototypeBuild)
root.order.add_edge(prototypeBuild, internalReview)
root.order.add_edge(internalReview, clientApproval)
root.order.add_edge(clientApproval, finalArtwork)
root.order.add_edge(finalArtwork, qualityCheck)
root.order.add_edge(qualityCheck, packagingPrep)
root.order.add_edge(packagingPrep, shipmentDispatch)
root.order.add_edge(shipmentDispatch, postDelivery)
root.order.add_edge(postDelivery, feedbackCollection)