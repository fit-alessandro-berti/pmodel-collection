# Generated from: f0c57729-9608-427e-940c-019931fda78e.json
# Description: This process manages the end-to-end workflow of commissioning custom artwork from initial client inquiry to final delivery. It includes client consultation, concept drafting, iterative feedback cycles, contract negotiation with unique terms, artist assignment based on style matching, material sourcing with ethical considerations, progress tracking with milestone reviews, quality assurance involving third-party evaluation, legal copyright transfer, packaging design for fragile items, and post-delivery support including care instructions and follow-up surveys. This atypical process ensures both artist creativity and client satisfaction through structured yet flexible collaboration while addressing logistics, legalities, and customer experience comprehensively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Inquiry_Intake = Transition(label='Inquiry Intake')
Consultation_Call = Transition(label='Consultation Call')
Concept_Draft = Transition(label='Concept Draft')

# Feedback Loop is iterative: after Feedback Loop, repeat Concept Draft or exit
Feedback_Loop = Transition(label='Feedback Loop')

Contract_Setup = Transition(label='Contract Setup')
Artist_Match = Transition(label='Artist Match')

Material_Sourcing = Transition(label='Material Sourcing')
Ethics_Review = Transition(label='Ethics Review')

Progress_Check = Transition(label='Progress Check')
Milestone_Approve = Transition(label='Milestone Approve')

Quality_Audit = Transition(label='Quality Audit')
Copyright_Transfer = Transition(label='Copyright Transfer')

Packaging_Plan = Transition(label='Packaging Plan')
Shipping_Arrange = Transition(label='Shipping Arrange')

# Post Delivery involves Post Delivery and Client Survey, which can be sequential
Post_Delivery = Transition(label='Post Delivery')
Client_Survey = Transition(label='Client Survey')

# Create loop for concept draft and feedback loop: 
# LOOP(body=A (Concept Draft), condition=B (Feedback Loop))
# * (Concept Draft, Feedback Loop)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Concept_Draft, Feedback_Loop])

# Material sourcing with ethics review: partial order, Ethics Review after Material Sourcing
material_ethics = StrictPartialOrder(nodes=[Material_Sourcing, Ethics_Review])
material_ethics.order.add_edge(Material_Sourcing, Ethics_Review)

# Progress check and milestone approve, sequential
progress_milestone = StrictPartialOrder(nodes=[Progress_Check, Milestone_Approve])
progress_milestone.order.add_edge(Progress_Check, Milestone_Approve)

# Post delivery and client survey sequential
post_delivery_chain = StrictPartialOrder(nodes=[Post_Delivery, Client_Survey])
post_delivery_chain.order.add_edge(Post_Delivery, Client_Survey)

# Top-level partial order to represent the process flow:
# Inquiry Intake --> Consultation Call --> (feedback loop)
# After finishing feedback loop successfully --> Contract Setup --> Artist Match --> Material/Ethics --> Progress/Milestone --> Quality Audit --> Copyright 
# --> Packaging --> Shipping --> Post delivery

nodes = [
    Inquiry_Intake,
    Consultation_Call,
    feedback_loop,
    Contract_Setup,
    Artist_Match,
    material_ethics,
    progress_milestone,
    Quality_Audit,
    Copyright_Transfer,
    Packaging_Plan,
    Shipping_Arrange,
    post_delivery_chain,
]

root = StrictPartialOrder(nodes=nodes)

root.order.add_edge(Inquiry_Intake, Consultation_Call)
root.order.add_edge(Consultation_Call, feedback_loop)
root.order.add_edge(feedback_loop, Contract_Setup)
root.order.add_edge(Contract_Setup, Artist_Match)
root.order.add_edge(Artist_Match, material_ethics)
root.order.add_edge(material_ethics, progress_milestone)
root.order.add_edge(progress_milestone, Quality_Audit)
root.order.add_edge(Quality_Audit, Copyright_Transfer)
root.order.add_edge(Copyright_Transfer, Packaging_Plan)
root.order.add_edge(Packaging_Plan, Shipping_Arrange)
root.order.add_edge(Shipping_Arrange, post_delivery_chain)