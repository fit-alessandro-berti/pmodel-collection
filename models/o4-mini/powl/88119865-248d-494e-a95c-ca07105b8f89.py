# Generated from: 88119865-248d-494e-a95c-ca07105b8f89.json
# Description: This process governs the authentication of rare historical artifacts before acquisition by museums or private collectors. It involves multidisciplinary verification steps including provenance validation, scientific material analysis, expert consultation, and legal compliance checks. Initial artifact intake triggers documentation and condition assessment, followed by imaging and spectroscopy tests. Concurrently, provenance research is conducted through archival records and ownership history. Expert panels review findings to confirm authenticity, while legal teams ensure clear title and export permissions. Any conflicting data initiates re-examination or rejection. Final approval leads to cataloging and secure storage, completing the authentication cycle with comprehensive reporting for stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all labeled transitions
artifact_intake   = Transition(label="Artifact Intake")
condition_check   = Transition(label="Condition Check")
imaging_scan      = Transition(label="Imaging Scan")
spectroscopy_test = Transition(label="Spectroscopy Test")
provenance_research = Transition(label="Provenance Research")
archival_review   = Transition(label="Archival Review")
ownership_verify  = Transition(label="Ownership Verify")
expert_panel      = Transition(label="Expert Panel")
data_reconcile    = Transition(label="Data Reconcile")
conflict_resolve  = Transition(label="Conflict Resolve")
legal_review      = Transition(label="Legal Review")
export_check      = Transition(label="Export Check")
final_approval    = Transition(label="Final Approval")
catalog_entry     = Transition(label="Catalog Entry")
secure_storage    = Transition(label="Secure Storage")

# Testing sub‐process: Imaging Scan and Spectroscopy Test in parallel
testing_po = StrictPartialOrder(nodes=[imaging_scan, spectroscopy_test])
# Research sub‐process: Provenance Research → {Archival Review, Ownership Verify} in parallel
research_po = StrictPartialOrder(nodes=[provenance_research, archival_review, ownership_verify])
research_po.order.add_edge(provenance_research, archival_review)
research_po.order.add_edge(provenance_research, ownership_verify)

# Validation sub‐process: Expert Panel in parallel with (Legal Review → Export Check)
validation_po = StrictPartialOrder(nodes=[expert_panel, legal_review, export_check])
validation_po.order.add_edge(legal_review, export_check)

# Reconciliation sub‐process: Data Reconcile → Conflict Resolve
reconcile_po = StrictPartialOrder(nodes=[data_reconcile, conflict_resolve])
reconcile_po.order.add_edge(data_reconcile, conflict_resolve)

# Loop: do validation_po, then optionally do reconcile_po and repeat validation
validation_loop = OperatorPOWL(operator=Operator.LOOP, children=[validation_po, reconcile_po])

# Assemble the full partial order
root = StrictPartialOrder(
    nodes=[
        artifact_intake,
        condition_check,
        testing_po,
        research_po,
        validation_loop,
        final_approval,
        catalog_entry,
        secure_storage
    ]
)

# Define the control‐flow edges
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, testing_po)
root.order.add_edge(condition_check, research_po)
root.order.add_edge(testing_po, validation_loop)
root.order.add_edge(research_po, validation_loop)
root.order.add_edge(validation_loop, final_approval)
root.order.add_edge(final_approval, catalog_entry)
root.order.add_edge(catalog_entry, secure_storage)