# Generated from: 075ccf9c-1f96-4e10-a748-e7d8b108f8fc.json
# Description: This process governs the acquisition of rare cultural artifacts through a multi-phase approach involving detailed provenance verification, ethical compliance checks, multi-jurisdictional legal clearance, and bespoke logistics planning. It starts with artifact identification and initial owner negotiation, followed by expert authentication and condition assessment. Concurrently, an ethical review committee evaluates the artifact's acquisition impact. Once cleared, legal teams coordinate cross-border permits and export licenses. The process culminates in tailored packaging, insured transport arrangements, and final delivery confirmation to ensure artifact integrity and adherence to all regulatory frameworks, protecting both cultural heritage and organizational interests throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Identify_Artifact = Transition(label='Identify Artifact')
Owner_Contact = Transition(label='Owner Contact')

Provenance_Check = Transition(label='Provenance Check')
Initial_Negotiation = Transition(label='Initial Negotiation')

Expert_Review = Transition(label='Expert Review')
Condition_Report = Transition(label='Condition Report')

Ethical_Review = Transition(label='Ethical Review')

Legal_Clearance = Transition(label='Legal Clearance')
Permit_Acquisition = Transition(label='Permit Acquisition')
Export_License = Transition(label='Export License')
Customs_Filing = Transition(label='Customs Filing')

Packaging_Plan = Transition(label='Packaging Plan')
Insurance_Setup = Transition(label='Insurance Setup')
Transport_Booking = Transition(label='Transport Booking')

Delivery_Confirm = Transition(label='Delivery Confirm')

Post_Arrival_Audit = Transition(label='Post-Arrival Audit')

# Phase 1: Identification and initial negotiation
# Assume Identify Artifact --> Owner Contact and Initial Negotiation follows Owner Contact
phase1 = StrictPartialOrder(nodes=[Identify_Artifact, Owner_Contact, Initial_Negotiation])
phase1.order.add_edge(Identify_Artifact, Owner_Contact)
phase1.order.add_edge(Owner_Contact, Initial_Negotiation)

# Phase 2: Provenance check after initial negotiation
# After Initial Negotiation, do Provenance Check
phase2 = StrictPartialOrder(nodes=[Initial_Negotiation, Provenance_Check])
phase2.order.add_edge(Initial_Negotiation, Provenance_Check)

# Phase 3: Expert authentication and condition assessment sequentially after Provenance Check
phase3 = StrictPartialOrder(nodes=[Provenance_Check, Expert_Review, Condition_Report])
phase3.order.add_edge(Provenance_Check, Expert_Review)
phase3.order.add_edge(Expert_Review, Condition_Report)

# Phase 4: Ethical Review runs concurrently with phase3 (Expert Review + Condition Report)
ethical_review_node = Ethical_Review  # single node

# Combine phase3 and Ethical Review in parallel (partial order with no edges between them)
phase3_ethics = StrictPartialOrder(
    nodes=[Expert_Review, Condition_Report, ethical_review_node]
)
phase3_ethics.order.add_edge(Expert_Review, Condition_Report)
# Ethical_Review concurrent: no edges to/from Ethical_Review here

# Phase 5: Legal clearance sequence after both phase3 and Ethical Review
# Legal_Clearance after both Condition_Report and Ethical_Review
legal_sequence = StrictPartialOrder(
    nodes=[Legal_Clearance, Permit_Acquisition, Export_License, Customs_Filing]
)
legal_sequence.order.add_edge(Legal_Clearance, Permit_Acquisition)
legal_sequence.order.add_edge(Permit_Acquisition, Export_License)
legal_sequence.order.add_edge(Export_License, Customs_Filing)

# Legal_Clearance depends on Condition_Report and Ethical_Review completion 
# We'll integrate all prior phases with edges accordingly

# Phase 6: Logistics planning and transport after customs filing
logistics = StrictPartialOrder(
    nodes=[Packaging_Plan, Insurance_Setup, Transport_Booking]
)
# No specified order between packaging, insurance, transport - assume concurrent
# So edges empty to keep concurrency

# Phase 7: Delivery Confirm after logistics
# Phase 8: Post Arrival Audit after Delivery Confirm

post_delivery = StrictPartialOrder(
    nodes=[Delivery_Confirm, Post_Arrival_Audit]
)
post_delivery.order.add_edge(Delivery_Confirm, Post_Arrival_Audit)

# Now combine all phases into final root partial order with correct dependencies

# Collect all nodes
all_nodes = [
    phase1,
    phase2,
    phase3_ethics,
    legal_sequence,
    logistics,
    post_delivery,
]

root = StrictPartialOrder(nodes=all_nodes)

# Add order edges between phases

# phase1 --> phase2: Initial_Negotiation is in both
root.order.add_edge(phase1, phase2)  # This adds edges from phase1 nodes to phase2 nodes

# phase2 --> phase3_ethics: Provenance_Check is in phase2, Expert_Review and Ethical_Review in phase3_ethics
root.order.add_edge(phase2, phase3_ethics)

# phase3_ethics --> legal_sequence: Legal_Clearance depends on Condition_Report and Ethical_Review completion
root.order.add_edge(phase3_ethics, legal_sequence)

# legal_sequence --> logistics: Customs_Filing completed before packaging etc
root.order.add_edge(legal_sequence, logistics)

# logistics --> post_delivery: all logistics before Delivery Confirm
root.order.add_edge(logistics, post_delivery)