# Generated from: 3b861877-18bf-423c-90ab-8739ebdee861.json
# Description: This process involves locating, authenticating, and repatriating corporate artifacts lost or stolen during historical mergers and acquisitions. It begins with artifact identification using archival research, followed by stakeholder interviews to verify provenance. Legal consultations ensure compliance with international ownership laws. Next, covert negotiations with current holders are conducted to facilitate return agreements. Logistics planning addresses secure transport and customs clearance. Finally, artifacts are restored, cataloged, and integrated into corporate heritage exhibits to preserve brand legacy and employee engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions
archival_scan   = Transition(label='Archival Scan')
artifact_id     = Transition(label='Artifact ID')
stakeholder_meet = Transition(label='Stakeholder Meet')
provenance_check = Transition(label='Provenance Check')
legal_review    = Transition(label='Legal Review')
ownership_audit = Transition(label='Ownership Audit')
negotiation_prep = Transition(label='Negotiation Prep')
stakeholder_contact = Transition(label='Stakeholder Contact')
agreement_draft = Transition(label='Agreement Draft')
transport_plan  = Transition(label='Transport Plan')
customs_clear   = Transition(label='Customs Clear')
artifact_restore = Transition(label='Artifact Restore')
catalog_entry   = Transition(label='Catalog Entry')
exhibit_setup   = Transition(label='Exhibit Setup')
legacy_report   = Transition(label='Legacy Report')

# Create the root partial order with all activities
root = StrictPartialOrder(nodes=[
    archival_scan, artifact_id,
    stakeholder_meet, provenance_check,
    legal_review, ownership_audit,
    negotiation_prep, stakeholder_contact, agreement_draft,
    transport_plan, customs_clear,
    artifact_restore, catalog_entry, exhibit_setup,
    legacy_report
])

# Define the sequence of the process
root.order.add_edge(archival_scan, artifact_id)
root.order.add_edge(artifact_id, stakeholder_meet)
root.order.add_edge(stakeholder_meet, provenance_check)
root.order.add_edge(provenance_check, legal_review)
root.order.add_edge(legal_review, ownership_audit)
root.order.add_edge(ownership_audit, negotiation_prep)
root.order.add_edge(negotiation_prep, stakeholder_contact)
root.order.add_edge(stakeholder_contact, agreement_draft)
root.order.add_edge(agreement_draft, transport_plan)
root.order.add_edge(transport_plan, customs_clear)
root.order.add_edge(customs_clear, artifact_restore)
root.order.add_edge(artifact_restore, catalog_entry)
root.order.add_edge(catalog_entry, exhibit_setup)
root.order.add_edge(exhibit_setup, legacy_report)