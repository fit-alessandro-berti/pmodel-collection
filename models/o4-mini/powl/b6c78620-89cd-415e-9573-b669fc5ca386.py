# Generated from: b6c78620-89cd-415e-9573-b669fc5ca386.json
# Description: This process outlines the comprehensive steps involved in authenticating rare cultural artifacts for a global auction house. It involves multidisciplinary expert evaluations, advanced scientific testing, provenance verification, legal compliance checks, and secure documentation handling. Each artifact undergoes intricate imaging, material analysis, historical cross-referencing, and ethical sourcing validation to ensure authenticity and legal ownership. The process culminates in certified approval and archival before public auction listing, ensuring transparency and trust for buyers and sellers worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
artifact_intake    = Transition(label='Artifact Intake')
prelim_scan        = Transition(label='Preliminary Scan')
material_test      = Transition(label='Material Test')
historical_check   = Transition(label='Historical Check')
provenance_review  = Transition(label='Provenance Review')
ethics_audit       = Transition(label='Ethics Audit')
imaging_capture    = Transition(label='Imaging Capture')
expert_panel       = Transition(label='Expert Panel')
legal_verify       = Transition(label='Legal Verify')
data_encryption    = Transition(label='Data Encryption')
report_draft       = Transition(label='Report Draft')
final_review       = Transition(label='Final Review')
certification      = Transition(label='Certification')
archival_store     = Transition(label='Archival Store')
auction_setup      = Transition(label='Auction Setup')
client_notify      = Transition(label='Client Notify')

# Build the partial‐order workflow
root = StrictPartialOrder(
    nodes=[
        artifact_intake, prelim_scan,
        material_test, historical_check, provenance_review, ethics_audit, imaging_capture,
        expert_panel, legal_verify, data_encryption, report_draft, final_review,
        certification, archival_store, auction_setup, client_notify
    ]
)

# 1) Artifact Intake -> Preliminary Scan
root.order.add_edge(artifact_intake, prelim_scan)

# 2) After Preliminary Scan, five analyses in parallel
for step in [material_test, historical_check, provenance_review, ethics_audit, imaging_capture]:
    root.order.add_edge(prelim_scan, step)

# 3) Synchronize all analyses at Expert Panel
for step in [material_test, historical_check, provenance_review, ethics_audit, imaging_capture]:
    root.order.add_edge(step, expert_panel)

# 4) Linear completion path
root.order.add_edge(expert_panel, legal_verify)
root.order.add_edge(legal_verify, data_encryption)
root.order.add_edge(data_encryption, report_draft)
root.order.add_edge(report_draft, final_review)
root.order.add_edge(final_review, certification)
root.order.add_edge(certification, archival_store)
root.order.add_edge(archival_store, auction_setup)
root.order.add_edge(auction_setup, client_notify)