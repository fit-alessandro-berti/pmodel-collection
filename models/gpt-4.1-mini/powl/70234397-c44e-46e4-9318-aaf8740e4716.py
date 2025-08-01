# Generated from: 70234397-c44e-46e4-9318-aaf8740e4716.json
# Description: This process outlines the intricate steps involved in commissioning custom artwork from initial client inquiry to final delivery and feedback collection. It begins with client briefing and concept approval, followed by iterative design adjustments, material sourcing, and multi-phase quality inspections. The workflow incorporates unconventional activities such as legal rights negotiation and digital archiving of the artwork. Additionally, it includes coordination with logistics for special packaging and international shipping, ensuring the artwork remains secure and pristine. The process concludes with client onboarding for future collaborations and post-delivery support, emphasizing personalized communication and relationship management to foster long-term partnerships between the artist and client.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities:
Client_Inquiry = Transition(label='Client Inquiry')
Brief_Review = Transition(label='Brief Review')
Concept_Draft = Transition(label='Concept Draft')
Approval_Check = Transition(label='Approval Check')
Design_Adjust = Transition(label='Design Adjust')
Material_Source = Transition(label='Material Source')
Rights_Negotiate = Transition(label='Rights Negotiate')
Prototype_Build = Transition(label='Prototype Build')
Quality_Inspect = Transition(label='Quality Inspect')
Packaging_Prep = Transition(label='Packaging Prep')
Logistics_Plan = Transition(label='Logistics Plan')
Shipment_Track = Transition(label='Shipment Track')
Delivery_Confirm = Transition(label='Delivery Confirm')
Client_Feedback = Transition(label='Client Feedback')
Archive_Digital = Transition(label='Archive Digital')
Support_Setup = Transition(label='Support Setup')
Future_Onboard = Transition(label='Future Onboard')

# Loop for iterative design adjustments:
# LOOP (A=Design_Adjust, B=Approval_Check)
# Actually, design adjustments and approval likely interact iteratively:
# We can model loop as: first Approval_Check, then either exit or Design_Adjust then Approval_Check again
# But from description: "iterative design adjustments" happen between Design_Adjust and Approval_Check
# So loop = * (Approval_Check, Design_Adjust)

design_loop = OperatorPOWL(operator=Operator.LOOP, children=[Approval_Check, Design_Adjust])

# Quality inspections are multi-phase, so possibly concurrent or sequential phases between Prototype_Build and Quality_Inspect

# Construct the partial order between all activities:

# First phase:
# Client Inquiry --> Brief Review --> Concept Draft --> design_loop

# Rights negotiation and material sourcing can happen in parallel after concept approved
# after design_loop finishes (i.e., concept approved), Rights_Negotiate and Material_Source concurrent

# Prototype build after material sourcing and rights negotiated
# Quality inspection after prototype build

# Packaging prep and logistics plan after quality inspection
# Shipment track after logistics plan

# Delivery confirm after shipment track

# Client feedback and archive digital after delivery confirm, concurrent

# Support setup and future onboarding after client feedback, partly concurrent

# Build nodes list:
nodes = [
    Client_Inquiry,
    Brief_Review,
    Concept_Draft,
    design_loop,
    Rights_Negotiate,
    Material_Source,
    Prototype_Build,
    Quality_Inspect,
    Packaging_Prep,
    Logistics_Plan,
    Shipment_Track,
    Delivery_Confirm,
    Client_Feedback,
    Archive_Digital,
    Support_Setup,
    Future_Onboard,
]

root = StrictPartialOrder(nodes=nodes)

# Add edges for sequence and dependencies:

# Client Inquiry --> Brief Review --> Concept Draft --> design_loop
root.order.add_edge(Client_Inquiry, Brief_Review)
root.order.add_edge(Brief_Review, Concept_Draft)
root.order.add_edge(Concept_Draft, design_loop)

# design_loop completed means concept approved, then Rights_Negotiate and Material_Source concurrently
root.order.add_edge(design_loop, Rights_Negotiate)
root.order.add_edge(design_loop, Material_Source)

# Both Rights_Negotiate and Material_Source must complete before Prototype_Build
root.order.add_edge(Rights_Negotiate, Prototype_Build)
root.order.add_edge(Material_Source, Prototype_Build)

# Prototype_Build --> Quality Inspect
root.order.add_edge(Prototype_Build, Quality_Inspect)

# Quality Inspect --> Packaging Prep --> Logistics Plan --> Shipment Track --> Delivery Confirm
root.order.add_edge(Quality_Inspect, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Shipment_Track)
root.order.add_edge(Shipment_Track, Delivery_Confirm)

# Delivery Confirm --> Client Feedback & Archive Digital (concurrent)
root.order.add_edge(Delivery_Confirm, Client_Feedback)
root.order.add_edge(Delivery_Confirm, Archive_Digital)

# Client Feedback --> Support Setup and Future Onboard (concurrent)
root.order.add_edge(Client_Feedback, Support_Setup)
root.order.add_edge(Client_Feedback, Future_Onboard)

# Model completed
