# Generated from: f9565973-0ee1-4535-978e-c2c682527568.json
# Description: This process involves the detailed validation and documentation of an artifact's origin, ownership, and authenticity through multiple verification stages including material analysis, historical registry checks, provenance interviews, and secure digital ledger entries. Each step ensures comprehensive traceability and legal compliance, often requiring interdisciplinary collaboration between historians, scientists, legal experts, and technology specialists to certify rare or culturally significant objects before sale or exhibition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
artifact_intake     = Transition(label='Artifact Intake')
initial_survey      = Transition(label='Initial Survey')
material_test       = Transition(label='Material Test')
historical_check    = Transition(label='Historical Check')
registry_search     = Transition(label='Registry Search')
owner_interview     = Transition(label='Owner Interview')
condition_report    = Transition(label='Condition Report')
forgery_scan        = Transition(label='Forgery Scan')
digital_tagging     = Transition(label='Digital Tagging')
ledger_entry        = Transition(label='Ledger Entry')
expert_review       = Transition(label='Expert Review')
legal_verify        = Transition(label='Legal Verify')
provenance_draft    = Transition(label='Provenance Draft')
client_approval     = Transition(label='Client Approval')
final_certificate   = Transition(label='Final Certificate')
archive_storage     = Transition(label='Archive Storage')

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    initial_survey,
    material_test,
    historical_check,
    registry_search,
    owner_interview,
    condition_report,
    forgery_scan,
    digital_tagging,
    ledger_entry,
    expert_review,
    legal_verify,
    provenance_draft,
    client_approval,
    final_certificate,
    archive_storage
])

# Sequential flow
root.order.add_edge(artifact_intake, initial_survey)

# Parallel verification steps
for step in [material_test, historical_check, registry_search, owner_interview]:
    root.order.add_edge(initial_survey, step)
    root.order.add_edge(step, condition_report)

# Continue the main sequence
root.order.add_edge(condition_report, forgery_scan)
root.order.add_edge(forgery_scan, digital_tagging)
root.order.add_edge(digital_tagging, ledger_entry)
root.order.add_edge(ledger_entry, expert_review)
root.order.add_edge(expert_review, legal_verify)
root.order.add_edge(legal_verify, provenance_draft)
root.order.add_edge(provenance_draft, client_approval)
root.order.add_edge(client_approval, final_certificate)
root.order.add_edge(final_certificate, archive_storage)