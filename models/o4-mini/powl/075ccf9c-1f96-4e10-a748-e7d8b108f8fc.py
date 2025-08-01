# Generated from: 075ccf9c-1f96-4e10-a748-e7d8b108f8fc.json
# Description: This process governs the acquisition of rare cultural artifacts through a multi-phase approach involving detailed provenance verification, ethical compliance checks, multi-jurisdictional legal clearance, and bespoke logistics planning. It starts with artifact identification and initial owner negotiation, followed by expert authentication and condition assessment. Concurrently, an ethical review committee evaluates the artifact's acquisition impact. Once cleared, legal teams coordinate cross-border permits and export licenses. The process culminates in tailored packaging, insured transport arrangements, and final delivery confirmation to ensure artifact integrity and adherence to all regulatory frameworks, protecting both cultural heritage and organizational interests throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
identify = Transition(label='Identify Artifact')
owner_contact = Transition(label='Owner Contact')
initial_negotiation = Transition(label='Initial Negotiation')
provenance_check = Transition(label='Provenance Check')
expert_review = Transition(label='Expert Review')
condition_report = Transition(label='Condition Report')
ethical_review = Transition(label='Ethical Review')
legal_clearance = Transition(label='Legal Clearance')
permit_acquisition = Transition(label='Permit Acquisition')
export_license = Transition(label='Export License')
customs_filing = Transition(label='Customs Filing')
packaging_plan = Transition(label='Packaging Plan')
insurance_setup = Transition(label='Insurance Setup')
transport_booking = Transition(label='Transport Booking')
delivery_confirm = Transition(label='Delivery Confirm')
post_arrival_audit = Transition(label='Post-Arrival Audit')

# Build the partial order
root = StrictPartialOrder(nodes=[
    identify,
    owner_contact,
    initial_negotiation,
    provenance_check,
    expert_review,
    condition_report,
    ethical_review,
    legal_clearance,
    permit_acquisition,
    export_license,
    customs_filing,
    packaging_plan,
    insurance_setup,
    transport_booking,
    delivery_confirm,
    post_arrival_audit
])

# Sequence: Identify -> Owner Contact -> Initial Negotiation
root.order.add_edge(identify, owner_contact)
root.order.add_edge(owner_contact, initial_negotiation)

# After negotiation: start provenance & ethical review
root.order.add_edge(initial_negotiation, provenance_check)
root.order.add_edge(initial_negotiation, ethical_review)

# Provenance then expert review then condition report
root.order.add_edge(provenance_check, expert_review)
root.order.add_edge(expert_review, condition_report)

# Both condition report and ethical review must finish before legal clearance
root.order.add_edge(condition_report, legal_clearance)
root.order.add_edge(ethical_review, legal_clearance)

# After legal clearance: parallel permit, export license, customs filing
root.order.add_edge(legal_clearance, permit_acquisition)
root.order.add_edge(legal_clearance, export_license)
root.order.add_edge(legal_clearance, customs_filing)

# Packaging plan waits for all three legal subtasks
root.order.add_edge(permit_acquisition, packaging_plan)
root.order.add_edge(export_license, packaging_plan)
root.order.add_edge(customs_filing, packaging_plan)

# Final logistics sequence
root.order.add_edge(packaging_plan, insurance_setup)
root.order.add_edge(insurance_setup, transport_booking)
root.order.add_edge(transport_booking, delivery_confirm)
root.order.add_edge(delivery_confirm, post_arrival_audit)