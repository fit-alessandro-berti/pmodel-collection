# Generated from: 0e1dcf81-4436-4d67-aaea-0fd6d1f1ea77.json
# Description: This process manages the intricate repatriation of corporate artifacts loaned to international museums and exhibitions. It involves verifying artifact authenticity, navigating customs regulations, coordinating multi-party logistics, securing insurance coverage, and ensuring proper cultural sensitivity. The process requires cross-border legal compliance, stakeholder communication, condition reporting, restoration scheduling, and final reintegration into corporate archives or displays, often under strict confidentiality agreements and tight timelines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artifact_verify   = Transition(label='Artifact Verify')
loan_assessment  = Transition(label='Loan Assessment')
legal_review     = Transition(label='Legal Review')
cultural_review  = Transition(label='Cultural Review')
confidentiality  = Transition(label='Confidentiality Sign')
customs_filing   = Transition(label='Customs Filing')
insurance_setup  = Transition(label='Insurance Setup')
transport_booking= Transition(label='Transport Booking')
shipping_monitor = Transition(label='Shipping Monitor')
stakeholder_notify = Transition(label='Stakeholder Notify')
security_audit   = Transition(label='Security Audit')
arrival_inspect  = Transition(label='Arrival Inspect')
condition_report = Transition(label='Condition Report')
restoration_plan = Transition(label='Restoration Plan')
archive_update   = Transition(label='Archive Update')

# Loop for repeated restoration until condition is acceptable
restoration_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[condition_report, restoration_plan]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    artifact_verify,
    loan_assessment,
    legal_review,
    cultural_review,
    confidentiality,
    customs_filing,
    insurance_setup,
    transport_booking,
    shipping_monitor,
    stakeholder_notify,
    security_audit,
    arrival_inspect,
    restoration_loop,
    archive_update
])

# Sequence: Verify -> Assess -> {Legal, Cultural} -> Confidentiality
root.order.add_edge(artifact_verify, loan_assessment)
root.order.add_edge(loan_assessment, legal_review)
root.order.add_edge(loan_assessment, cultural_review)
root.order.add_edge(legal_review, confidentiality)
root.order.add_edge(cultural_review, confidentiality)

# After confidentiality: Customs & Insurance in parallel -> Booking
root.order.add_edge(confidentiality, customs_filing)
root.order.add_edge(confidentiality, insurance_setup)
root.order.add_edge(customs_filing, transport_booking)
root.order.add_edge(insurance_setup, transport_booking)

# Booking -> Shipping monitor + Notifications/Audit in parallel
root.order.add_edge(transport_booking, shipping_monitor)
root.order.add_edge(transport_booking, stakeholder_notify)
root.order.add_edge(transport_booking, security_audit)

# Shipping monitor -> Arrival inspect -> possible restoration loop -> Final archive update
root.order.add_edge(shipping_monitor, arrival_inspect)
root.order.add_edge(arrival_inspect, restoration_loop)
root.order.add_edge(restoration_loop, archive_update)