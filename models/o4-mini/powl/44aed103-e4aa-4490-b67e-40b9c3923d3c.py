# Generated from: 44aed103-e4aa-4490-b67e-40b9c3923d3c.json
# Description: This process governs the authentication and provenance verification of rare historical artifacts submitted to a specialized auction house. It involves interdisciplinary collaboration among historians, scientists, and legal experts to validate the artifact's origin, material composition, and ownership history. The workflow includes initial intake, condition assessment, multi-level scientific testing (such as radiocarbon dating and spectroscopy), provenance research through archival databases, conflict artifact screening, expert panel review, legal clearance for export, and final certification issuance. The process ensures the integrity of the auction and prevents illicit trade, requiring meticulous documentation and secure data management throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# define all activities as transitions
artifact_intake     = Transition(label="Artifact Intake")
condition_check     = Transition(label="Condition Check")
initial_screening   = Transition(label="Initial Screening")
scientific_tests    = Transition(label="Scientific Tests")
radiocarbon_date    = Transition(label="Radiocarbon Date")
spectroscopy_test   = Transition(label="Spectroscopy Test")
provenance_search   = Transition(label="Provenance Search")
archival_review     = Transition(label="Archival Review")
conflict_check      = Transition(label="Conflict Check")
expert_panel        = Transition(label="Expert Panel")
legal_clearance     = Transition(label="Legal Clearance")
export_approval     = Transition(label="Export Approval")
certification       = Transition(label="Certification")
documentation       = Transition(label="Documentation")
data_archiving      = Transition(label="Data Archiving")
client_notification = Transition(label="Client Notification")

# build the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake, condition_check, initial_screening,
    scientific_tests, radiocarbon_date, spectroscopy_test,
    provenance_search, archival_review, conflict_check,
    expert_panel, legal_clearance, export_approval,
    certification, documentation, data_archiving,
    client_notification
])

# linear intake and assessment
root.order.add_edge(artifact_intake,   condition_check)
root.order.add_edge(condition_check,   initial_screening)

# branch into scientific tests
root.order.add_edge(initial_screening, scientific_tests)
root.order.add_edge(scientific_tests,  radiocarbon_date)
root.order.add_edge(scientific_tests,  spectroscopy_test)
# synchronize tests before provenance research
root.order.add_edge(radiocarbon_date,  provenance_search)
root.order.add_edge(spectroscopy_test, provenance_search)

# provenance research sequence
root.order.add_edge(provenance_search, archival_review)
root.order.add_edge(archival_review,   conflict_check)

# expert review and legal steps
root.order.add_edge(conflict_check,    expert_panel)
root.order.add_edge(expert_panel,      legal_clearance)
root.order.add_edge(legal_clearance,   export_approval)
root.order.add_edge(export_approval,   certification)

# final concurrent steps after certification
root.order.add_edge(certification,     documentation)
root.order.add_edge(certification,     data_archiving)
root.order.add_edge(certification,     client_notification)