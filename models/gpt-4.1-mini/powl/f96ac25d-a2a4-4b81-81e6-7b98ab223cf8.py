# Generated from: f96ac25d-a2a4-4b81-81e6-7b98ab223cf8.json
# Description: This process governs the lifecycle of a custom art commission from initial client inquiry to final delivery and post-sale support. It begins with client briefing and concept ideation, followed by iterative design reviews and adjustments. The artist then proceeds with material sourcing and prototype creation, coordinating with external vendors for specialty supplies. Quality assurance involves both technical and aesthetic evaluations, ensuring the artwork meets client expectations and industry standards. After final approval, packaging and logistics are arranged with eco-friendly considerations. Post-delivery, the process includes client feedback collection, documentation for portfolio updates, and scheduling of potential future commissions or maintenance services. Throughout, communication and contract management maintain transparency and protect intellectual property rights, ensuring a seamless experience for both artist and client.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Client_Brief = Transition(label='Client Brief')
Concept_Sketch = Transition(label='Concept Sketch')

Design_Review = Transition(label='Design Review')
# Loop body: adjustments after design review, modeled as Design_Review -> (Choice: adjust or exit)
# We'll model loop: A=Design_Review, B= Adjustment cycle.
# Adjustment cycle is a partial order of no activities, just represented by Design_Review again (for re-review).
# Since adjustment is iterative, we model loop between Design_Review and an empty silent transition to exit
# but adjustments are unnamed, so let's assume the loop goes as:
# LOOP(Design_Review, SilentTransition)
adjustment_cycle = SilentTransition()
design_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[Design_Review, adjustment_cycle])

Material_Sourcing = Transition(label='Material Sourcing')
Prototype_Build = Transition(label='Prototype Build')
Vendor_Coordination = Transition(label='Vendor Coordination')

Quality_Check = Transition(label='Quality Check')
Client_Approval = Transition(label='Client Approval')

Packaging_Prep = Transition(label='Packaging Prep')
Shipping_Arrange = Transition(label='Shipping Arrange')

Feedback_Collect = Transition(label='Feedback Collect')
Portfolio_Update = Transition(label='Portfolio Update')
Future_Schedule = Transition(label='Future Schedule')
Maintenance_Plan = Transition(label='Maintenance Plan')

Contract_Sign = Transition(label='Contract Sign')
IP_Management = Transition(label='IP Management')

# Model the control flow:

# 1) Client Brief -> Concept Sketch
# 2) Concept Sketch -> Design Review Loop (iterative design reviews and adjustments)
# 3) After Design Review loop finishes, proceed to Material Sourcing and Prototype Build and Vendor Coordination (some can be concurrent)

# After prototyping phase: Quality Check -> Client Approval
# Then Packaging Prep -> Shipping Arrange
# Then Post-delivery: Feedback Collect -> Portfolio Update -> Choice( Future Schedule, Maintenance Plan)

# Contract Sign and IP Management maintain transparency throughout -> the description suggests concurrency

# Define post delivery sequence:
post_delivery_seq = StrictPartialOrder(nodes=[Feedback_Collect, Portfolio_Update])
post_delivery_seq.order.add_edge(Feedback_Collect, Portfolio_Update)

# Choice between Future Schedule and Maintenance Plan after portfolio update
post_choice = OperatorPOWL(operator=Operator.XOR, children=[Future_Schedule, Maintenance_Plan])

# Combine post delivery sequence and choice in PO
post_delivery = StrictPartialOrder(nodes=[post_delivery_seq, post_choice])
post_delivery.order.add_edge(post_delivery_seq, post_choice)

# Sourcing and Prototype stage partial order (Material Sourcing, Prototype Build, Vendor Coordination).
# Assume Material Sourcing before Prototype Build and Vendor Coordination can be concurrent with Prototype Build
sourcing_proto = StrictPartialOrder(
    nodes=[Material_Sourcing, Prototype_Build, Vendor_Coordination]
)
sourcing_proto.order.add_edge(Material_Sourcing, Prototype_Build)

# Vendor Coordination can start after or concurrent with Material Sourcing? Let's assume it starts after Material Sourcing.
sourcing_proto.order.add_edge(Material_Sourcing, Vendor_Coordination)

# Quality Check after all three
quality_phase = StrictPartialOrder(
    nodes=[sourcing_proto, Quality_Check]
)
quality_phase.order.add_edge(sourcing_proto, Quality_Check)

# Client Approval after Quality Check
approval_phase = StrictPartialOrder(
    nodes=[quality_phase, Client_Approval]
)
approval_phase.order.add_edge(quality_phase, Client_Approval)

# Packaging Prep and Shipping Arrange sequence
pack_ship_seq = StrictPartialOrder(
    nodes=[Packaging_Prep, Shipping_Arrange]
)
pack_ship_seq.order.add_edge(Packaging_Prep, Shipping_Arrange)

# Contract Sign and IP Management concurrent with everything, so separate node set, then combined at top level (concurrent)

# Now top level partial order:

# order:
# Client_Brief --> Concept_Sketch
# Concept_Sketch --> Design_Review Loop
# Design_Review Loop --> sourcing_proto (Material_Sourcing etc)
# sourcing_proto --> Quality_Check ... cascades to Approval, Packaging, Shipping, Post delivery

top_level = StrictPartialOrder(
    nodes=[
        Client_Brief,
        Concept_Sketch,
        design_review_loop,
        approval_phase,  # includes sourcing, quality, approval nested
        pack_ship_seq,
        post_delivery,
        Contract_Sign,
        IP_Management
    ]
)

# Add partial order edges based on above logic:
top_level.order.add_edge(Client_Brief, Concept_Sketch)
top_level.order.add_edge(Concept_Sketch, design_review_loop)

# design_review_loop --> approval_phase (approval_phase includes sourcing, quality, client approval)
top_level.order.add_edge(design_review_loop, approval_phase)

# approval_phase --> packing/shipping
top_level.order.add_edge(approval_phase, pack_ship_seq)

# pack_ship_seq --> post_delivery
top_level.order.add_edge(pack_ship_seq, post_delivery)

# Contract_Sign and IP_Management concurrent with entire process: no edges needed for concurrency

root = top_level