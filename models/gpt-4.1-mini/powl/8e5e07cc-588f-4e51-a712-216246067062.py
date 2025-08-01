# Generated from: 8e5e07cc-588f-4e51-a712-216246067062.json
# Description: This process outlines the steps involved in managing a custom art commission from initial client inquiry through final delivery and post-sale support. It begins with gathering detailed client requirements and concept approval, followed by iterative design drafts and revisions. After client confirmation, the artist proceeds with production using specialized materials and techniques. Quality checks ensure adherence to client specifications before packaging. The process concludes with shipment logistics and a feedback collection phase to maintain client satisfaction and improve future commissions. This atypical process incorporates creative, logistical, and customer service tasks in a cohesive workflow.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Client_Inquiry = Transition(label='Client Inquiry')
Requirement_Gather = Transition(label='Requirement Gather')
Concept_Sketch = Transition(label='Concept Sketch')
Client_Review = Transition(label='Client Review')
Design_Revise = Transition(label='Design Revise')
Material_Select = Transition(label='Material Select')
Production_Start = Transition(label='Production Start')
Midway_Check = Transition(label='Midway Check')
Quality_Review = Transition(label='Quality Review')
Final_Approval = Transition(label='Final Approval')
Packaging_Prep = Transition(label='Packaging Prep')
Shipment_Arrange = Transition(label='Shipment Arrange')
Delivery_Confirm = Transition(label='Delivery Confirm')
Feedback_Collect = Transition(label='Feedback Collect')
Aftercare_Support = Transition(label='Aftercare Support')

# Model the loop between Client_Review and Design_Revise, repeated until client confirms
# LOOP(A, B): A then choose exit or B then A again
# Here: A = Client_Review, B = Design_Revise
# So: Client_Review, then either exit (client approves) or revise design then client review again
review_revise_loop = OperatorPOWL(operator=Operator.LOOP, children=[Client_Review, Design_Revise])

# Model the partial order:
# Start: Client Inquiry -> Requirement Gather -> Concept Sketch -> (review_revise_loop)
# After exiting loop (i.e. final client approval), continue production steps:
# Material Select -> Production Start -> Midway Check -> Quality Review -> Final Approval -> Packaging Prep
# Packaging Prep -> Shipment Arrange -> Delivery Confirm -> Feedback Collect -> Aftercare Support

# Build the partially ordered workflow
nodes = [
    Client_Inquiry,
    Requirement_Gather,
    Concept_Sketch,
    review_revise_loop,
    Material_Select,
    Production_Start,
    Midway_Check,
    Quality_Review,
    Final_Approval,
    Packaging_Prep,
    Shipment_Arrange,
    Delivery_Confirm,
    Feedback_Collect,
    Aftercare_Support
]

root = StrictPartialOrder(nodes=nodes)

# Define control flow dependencies
root.order.add_edge(Client_Inquiry, Requirement_Gather)
root.order.add_edge(Requirement_Gather, Concept_Sketch)
root.order.add_edge(Concept_Sketch, review_revise_loop)

# The loop node represents Client_Review and Design_Revise with internal looping. After acceptance, continue:
root.order.add_edge(review_revise_loop, Material_Select)

root.order.add_edge(Material_Select, Production_Start)
root.order.add_edge(Production_Start, Midway_Check)
root.order.add_edge(Midway_Check, Quality_Review)
root.order.add_edge(Quality_Review, Final_Approval)
root.order.add_edge(Final_Approval, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Shipment_Arrange)
root.order.add_edge(Shipment_Arrange, Delivery_Confirm)
root.order.add_edge(Delivery_Confirm, Feedback_Collect)
root.order.add_edge(Feedback_Collect, Aftercare_Support)