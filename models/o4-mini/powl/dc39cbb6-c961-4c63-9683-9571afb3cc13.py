# Generated from: dc39cbb6-c961-4c63-9683-9571afb3cc13.json
# Description: This process outlines the workflow for managing custom art commissions from initial client inquiry through to final delivery and post-sale support. It begins with client consultation to understand project requirements, followed by concept development and iterative feedback cycles. After client approval, the artist proceeds with detailed creation, periodic progress updates, and quality assurance reviews. Once the artwork is complete, it undergoes final adjustments before invoicing and shipping. Post-delivery includes client satisfaction confirmation and optional framing or digital licensing arrangements. The process ensures clear communication, creative alignment, and efficient resource allocation to meet unique artistic demands in a timely manner.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Basic activities
clientInquiry   = Transition(label='Client Inquiry')
requirementGather = Transition(label='Requirement Gather')
conceptSketch   = Transition(label='Concept Sketch')
clientFeedback  = Transition(label='Client Feedback')
revisionCycle   = Transition(label='Revision Cycle')
finalApproval   = Transition(label='Final Approval')
artCreation     = Transition(label='Art Creation')
progressUpdate  = Transition(label='Progress Update')
qualityCheck    = Transition(label='Quality Check')
finalAdjust     = Transition(label='Final Adjust')
invoiceIssue    = Transition(label='Invoice Issue')
shipmentPrep    = Transition(label='Shipment Prep')
deliveryConfirm = Transition(label='Delivery Confirm')
postSupport     = Transition(label='Post Support')
licenseSetup    = Transition(label='License Setup')
frameArrange    = Transition(label='Frame Arrange')

# Silent transition for optional skip
skip = SilentTransition()

# Loop for iterative feedback & revisions: CF -> (exit or RC -> CF)*
loopConcept = OperatorPOWL(
    operator=Operator.LOOP,
    children=[clientFeedback, revisionCycle]
)

# Optional post-delivery arrangement: choose one or skip
xorPost = OperatorPOWL(
    operator=Operator.XOR,
    children=[licenseSetup, frameArrange, skip]
)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    clientInquiry,
    requirementGather,
    conceptSketch,
    loopConcept,
    finalApproval,
    artCreation,
    progressUpdate,
    qualityCheck,
    finalAdjust,
    invoiceIssue,
    shipmentPrep,
    deliveryConfirm,
    postSupport,
    xorPost
])

# Define the control‐flow (partial order) edges
root.order.add_edge(clientInquiry,   requirementGather)
root.order.add_edge(requirementGather, conceptSketch)
root.order.add_edge(conceptSketch,   loopConcept)
root.order.add_edge(loopConcept,     finalApproval)
root.order.add_edge(finalApproval,   artCreation)
root.order.add_edge(artCreation,     progressUpdate)
root.order.add_edge(artCreation,     qualityCheck)
root.order.add_edge(qualityCheck,    finalAdjust)
root.order.add_edge(artCreation,     finalAdjust)
root.order.add_edge(finalAdjust,     invoiceIssue)
root.order.add_edge(invoiceIssue,    shipmentPrep)
root.order.add_edge(shipmentPrep,    deliveryConfirm)
root.order.add_edge(deliveryConfirm, postSupport)
root.order.add_edge(postSupport,     xorPost)