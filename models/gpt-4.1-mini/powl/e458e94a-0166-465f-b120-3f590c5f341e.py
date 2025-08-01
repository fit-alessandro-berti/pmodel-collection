# Generated from: e458e94a-0166-465f-b120-3f590c5f341e.json
# Description: This process manages the end-to-end workflow for commissioning custom artwork from initial client inquiry through final delivery and post-sale support. It includes client onboarding, concept development, iterative feedback loops, contract negotiation, milestone payments, artwork creation, quality assurance, framing coordination, shipping logistics, and customer satisfaction follow-up. The process ensures tailored communication between artist and client while maintaining clear documentation and legal compliance throughout. It also incorporates contingency planning for creative revisions and unexpected delays, ensuring a seamless experience from idea inception to completed commissioned piece delivery.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Inquiry_Review = Transition(label='Inquiry Review')
Client_Onboard = Transition(label='Client Onboard')
Concept_Draft = Transition(label='Concept Draft')
Feedback_Cycle = Transition(label='Feedback Cycle')
Contract_Setup = Transition(label='Contract Setup')
Payment_Schedule = Transition(label='Payment Schedule')
Material_Sourcing = Transition(label='Material Sourcing')
Artwork_Create = Transition(label='Artwork Create')
Quality_Check = Transition(label='Quality Check')
Frame_Selection = Transition(label='Frame Selection')
Packaging_Prep = Transition(label='Packaging Prep')
Shipment_Arrange = Transition(label='Shipment Arrange')
Delivery_Confirm = Transition(label='Delivery Confirm')
Post_Sale_Support = Transition(label='Post-Sale Support')
Revision_Manage = Transition(label='Revision Manage')
Delay_Mitigate = Transition(label='Delay Mitigate')

skip = SilentTransition()

# Loop for feedback and revisions/delays:
# Execute Feedback Cycle, then choose to exit or do Revision Manage or Delay Mitigate then repeat Feedback Cycle
revision_or_delay = OperatorPOWL(operator=Operator.XOR, children=[Revision_Manage, Delay_Mitigate, skip])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Cycle, revision_or_delay])

# Partial order for initial onboarding and contract/payment
initial_seq = StrictPartialOrder(nodes=[
    Inquiry_Review,
    Client_Onboard,
    Concept_Draft,
    feedback_loop,
    Contract_Setup,
    Payment_Schedule
])
initial_seq.order.add_edge(Inquiry_Review, Client_Onboard)
initial_seq.order.add_edge(Client_Onboard, Concept_Draft)
initial_seq.order.add_edge(Concept_Draft, feedback_loop)
initial_seq.order.add_edge(feedback_loop, Contract_Setup)
initial_seq.order.add_edge(Contract_Setup, Payment_Schedule)

# Parallel activities for material sourcing and artwork creation after payment schedule
material_and_artwork = StrictPartialOrder(nodes=[Material_Sourcing, Artwork_Create])
# No ordering, so concurrent

# Quality check after artwork create
quality_phase = StrictPartialOrder(nodes=[Artwork_Create, Quality_Check])
quality_phase.order.add_edge(Artwork_Create, Quality_Check)

# After quality check, sequential framing, packaging, shipment, delivery confirm
finalization = StrictPartialOrder(nodes=[
    Frame_Selection,
    Packaging_Prep,
    Shipment_Arrange,
    Delivery_Confirm
])
finalization.order.add_edge(Frame_Selection, Packaging_Prep)
finalization.order.add_edge(Packaging_Prep, Shipment_Arrange)
finalization.order.add_edge(Shipment_Arrange, Delivery_Confirm)

# Post sale support after delivery confirm
post_sale = Post_Sale_Support

# Compose entire partial order
# Combine initial_seq --> material_and_artwork and quality_phase
# material_and_artwork and quality_phase share Artwork_Create, so merge carefully:
# We'll combine all in one PO:
nodes_all = [
    Inquiry_Review,
    Client_Onboard,
    Concept_Draft,
    feedback_loop,
    Contract_Setup,
    Payment_Schedule,
    Material_Sourcing,
    Artwork_Create,
    Quality_Check,
    Frame_Selection,
    Packaging_Prep,
    Shipment_Arrange,
    Delivery_Confirm,
    post_sale
]

root = StrictPartialOrder(nodes=nodes_all)

# initial sequence edges
root.order.add_edge(Inquiry_Review, Client_Onboard)
root.order.add_edge(Client_Onboard, Concept_Draft)
root.order.add_edge(Concept_Draft, feedback_loop)
root.order.add_edge(feedback_loop, Contract_Setup)
root.order.add_edge(Contract_Setup, Payment_Schedule)

# Payment Schedule precedes Material Sourcing & Artwork Create (concurrent)
root.order.add_edge(Payment_Schedule, Material_Sourcing)
root.order.add_edge(Payment_Schedule, Artwork_Create)

# Artwork Create precedes Quality Check
root.order.add_edge(Artwork_Create, Quality_Check)

# Quality Check precedes Frame Selection
root.order.add_edge(Quality_Check, Frame_Selection)

# Frame Selection to Packaging Prep
root.order.add_edge(Frame_Selection, Packaging_Prep)

# Packaging Prep to Shipment Arrange
root.order.add_edge(Packaging_Prep, Shipment_Arrange)

# Shipment Arrange to Delivery Confirm
root.order.add_edge(Shipment_Arrange, Delivery_Confirm)

# Delivery Confirm to Post-Sale Support
root.order.add_edge(Delivery_Confirm, post_sale)

# Add feedback loop and revision/delay loop nodes in nodes_all for completion
# Actually feedback_loop is an OperatorPOWL node - must be included
# Already included as feedback_loop in initial sequence edges
# feedback_loop node is represented by the OperatorPOWL

# Replace feedback_loop node in root nodes with that OperatorPOWL correctly
# First remove old feedback_loop label from root.nodes and add the OperatorPOWL
# But since we've included it as a Transition earlier? Let's remove that and add proper OperatorPOWL node.

# Rebuild nodes_all to include feedback_loop instead of Feedback_Cycle
# Actually Feedback_Cycle is one node, feedback_loop is the OperatorPOWL with Feedback_Cycle and revision_or_delay inside it.

nodes_all = [
    Inquiry_Review,
    Client_Onboard,
    Concept_Draft,
    feedback_loop,
    Contract_Setup,
    Payment_Schedule,
    Material_Sourcing,
    Artwork_Create,
    Quality_Check,
    Frame_Selection,
    Packaging_Prep,
    Shipment_Arrange,
    Delivery_Confirm,
    post_sale
]

root = StrictPartialOrder(nodes=nodes_all)

root.order.add_edge(Inquiry_Review, Client_Onboard)
root.order.add_edge(Client_Onboard, Concept_Draft)
root.order.add_edge(Concept_Draft, feedback_loop)
root.order.add_edge(feedback_loop, Contract_Setup)
root.order.add_edge(Contract_Setup, Payment_Schedule)

root.order.add_edge(Payment_Schedule, Material_Sourcing)
root.order.add_edge(Payment_Schedule, Artwork_Create)

root.order.add_edge(Artwork_Create, Quality_Check)
root.order.add_edge(Quality_Check, Frame_Selection)
root.order.add_edge(Frame_Selection, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Shipment_Arrange)
root.order.add_edge(Shipment_Arrange, Delivery_Confirm)
root.order.add_edge(Delivery_Confirm, post_sale)