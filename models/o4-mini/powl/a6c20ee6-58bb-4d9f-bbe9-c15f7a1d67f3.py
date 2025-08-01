# Generated from: a6c20ee6-58bb-4d9f-bbe9-c15f7a1d67f3.json
# Description: This process involves the thorough authentication and provenance verification of rare historical artifacts intended for museum acquisition or private collection. It includes multi-disciplinary expert evaluations, scientific testing like radiocarbon dating and spectrography, cross-referencing archival records, and secure chain-of-custody documentation. Additionally, it incorporates risk assessment related to forgery, legal ownership verification, and final certification issuance. The process requires coordination between curators, forensic scientists, historians, legal advisors, and logistics teams to ensure authenticity and compliance with international cultural heritage laws.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
initial_review      = Transition(label='Initial Review')
provenance_check    = Transition(label='Provenance Check')
record_crossref     = Transition(label='Record Crossref')
expert_consult      = Transition(label='Expert Consult')
scientific_test_lbl = Transition(label='Scientific Test')
radiocarbon_date    = Transition(label='Radiocarbon Date')
spectrograph_scan   = Transition(label='Spectrograph Scan')
forgery_assessment  = Transition(label='Forgery Assessment')
legal_verify        = Transition(label='Legal Verify')
custody_chain       = Transition(label='Custody Chain')
risk_evaluate       = Transition(label='Risk Evaluate')
condition_report    = Transition(label='Condition Report')
final_approval      = Transition(label='Final Approval')
certification       = Transition(label='Certification')
secure_transport    = Transition(label='Secure Transport')
archive_update      = Transition(label='Archive Update')

# Build the "Scientific Test" partial order (Radiocarbon & Spectrograph in parallel)
scientific_test = StrictPartialOrder(
    nodes=[scientific_test_lbl, radiocarbon_date, spectrograph_scan]
)
scientific_test.order.add_edge(scientific_test_lbl, radiocarbon_date)
scientific_test.order.add_edge(scientific_test_lbl, spectrograph_scan)

# Loop: after initial tests, perform risk evaluation; if fails, re-run scientific tests
risk_test_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[risk_evaluate, scientific_test]
)

# Root model: sequence all main steps
root = StrictPartialOrder(nodes=[
    initial_review,
    provenance_check,
    record_crossref,
    expert_consult,
    scientific_test,
    risk_test_loop,
    forgery_assessment,
    legal_verify,
    custody_chain,
    condition_report,
    final_approval,
    certification,
    secure_transport,
    archive_update
])

# Define the (partial) order between them
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(provenance_check, record_crossref)
root.order.add_edge(record_crossref, expert_consult)
root.order.add_edge(expert_consult, scientific_test)
root.order.add_edge(scientific_test, risk_test_loop)
root.order.add_edge(risk_test_loop, forgery_assessment)
root.order.add_edge(forgery_assessment, legal_verify)
root.order.add_edge(legal_verify, custody_chain)
root.order.add_edge(custody_chain, condition_report)
root.order.add_edge(condition_report, final_approval)
root.order.add_edge(final_approval, certification)
root.order.add_edge(certification, secure_transport)
root.order.add_edge(secure_transport, archive_update)