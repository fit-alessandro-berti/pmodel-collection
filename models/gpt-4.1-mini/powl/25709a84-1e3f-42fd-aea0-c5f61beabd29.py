# Generated from: 25709a84-1e3f-42fd-aea0-c5f61beabd29.json
# Description: This process outlines the workflow for managing bespoke art commissions from initial client inquiry through to final delivery and post-sale support. It includes client consultation, concept development, iterative feedback cycles, material sourcing, creation phases, quality assurance, and coordinating logistics with specialized packaging and shipping. Additionally, it covers the management of intellectual property rights, final invoicing, and securing client testimonials to support future commissions. The process ensures transparency, client satisfaction, and efficient turnaround times for unique, high-value art pieces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

ClientInquiry = Transition(label='Client Inquiry')
InitialBrief = Transition(label='Initial Brief')
ConceptDraft = Transition(label='Concept Draft')

# Feedback Loop: iterative cycle between ConceptDraft and FeedbackLoop
# Model as a loop: A=ConceptDraft, B=FeedbackLoop (Feedback Loop activity is included as a Transition)
FeedbackLoop = Transition(label='Feedback Loop')
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[ConceptDraft, FeedbackLoop])

MaterialSourcing = Transition(label='Material Sourcing')
WorkScheduling = Transition(label='Work Scheduling')

PrototypeReview = Transition(label='Prototype Review')

# Art Creation and Detailing Phase are concurrent (partial order without edges between them)
ArtCreation = Transition(label='Art Creation')
DetailingPhase = Transition(label='Detailing Phase')

QualityCheck = Transition(label='Quality Check')

PackagingPrep = Transition(label='Packaging Prep')
ShippingSetup = Transition(label='Shipping Setup')

IPAgreement = Transition(label='IP Agreement')

FinalInvoice = Transition(label='Final Invoice')

ClientFollowup = Transition(label='Client Followup')
TestimonialRequest = Transition(label='Testimonial Request')

# Build partial orders stepwise:
# From ClientInquiry --> InitialBrief --> loop_feedback (ConceptDraft + FeedbackLoop)
# Then MaterialSourcing and WorkScheduling after feedback loop
# PrototypeReview after MaterialSourcing and WorkScheduling
# ArtCreation and DetailingPhase after PrototypeReview (concurrent)
# QualityCheck after both ArtCreation and DetailingPhase
# PackagingPrep and ShippingSetup (concurrent) after QualityCheck
# IPAagreement after PackagingPrep and ShippingSetup (concurrent)
# FinalInvoice after IP Agreement
# ClientFollowup after FinalInvoice
# TestimonialRequest after ClientFollowup

root = StrictPartialOrder(
    nodes=[
        ClientInquiry, InitialBrief, loop_feedback,
        MaterialSourcing, WorkScheduling,
        PrototypeReview,
        ArtCreation, DetailingPhase,
        QualityCheck,
        PackagingPrep, ShippingSetup,
        IPAgreement,
        FinalInvoice,
        ClientFollowup,
        TestimonialRequest
    ]
)

# Define order edges according to description
root.order.add_edge(ClientInquiry, InitialBrief)
root.order.add_edge(InitialBrief, loop_feedback)

root.order.add_edge(loop_feedback, MaterialSourcing)
root.order.add_edge(loop_feedback, WorkScheduling)

root.order.add_edge(MaterialSourcing, PrototypeReview)
root.order.add_edge(WorkScheduling, PrototypeReview)

root.order.add_edge(PrototypeReview, ArtCreation)
root.order.add_edge(PrototypeReview, DetailingPhase)

root.order.add_edge(ArtCreation, QualityCheck)
root.order.add_edge(DetailingPhase, QualityCheck)

root.order.add_edge(QualityCheck, PackagingPrep)
root.order.add_edge(QualityCheck, ShippingSetup)

root.order.add_edge(PackagingPrep, IPAgreement)
root.order.add_edge(ShippingSetup, IPAgreement)

root.order.add_edge(IPAgreement, FinalInvoice)
root.order.add_edge(FinalInvoice, ClientFollowup)
root.order.add_edge(ClientFollowup, TestimonialRequest)