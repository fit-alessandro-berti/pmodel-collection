# Generated from: 70624408-facb-430b-a4eb-811971596dbd.json
# Description: This process involves locating, authenticating, and reclaiming lost or stolen corporate artifacts that hold significant historical or strategic value. It combines legal research, field investigation, negotiation with private collectors, and coordination with law enforcement agencies. The process demands careful documentation, risk assessment, and strategic communication to ensure successful recovery while preserving corporate reputation and avoiding legal pitfalls. Multiple stakeholders including legal, security, PR, and executive teams collaborate to track provenance, validate ownership, and secure transfer agreements in compliance with international laws. The final phase includes artifact restoration and integration into corporate heritage or museum collections, followed by public relations campaigns to highlight the recovery success.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
init_request        = Transition(label='Initiate Request')
legal_review        = Transition(label='Legal Review')
historical_audit    = Transition(label='Historical Audit')
stakeholder_map     = Transition(label='Stakeholder Map')
risk_assessment     = Transition(label='Risk Assessment')
provenance_check    = Transition(label='Provenance Check')
field_investigation = Transition(label='Field Investigation')
collector_contact   = Transition(label='Collector Contact')
negotiation_phase   = Transition(label='Negotiation Phase')
law_enforcement     = Transition(label='Law Enforcement')
ownership_validation= Transition(label='Ownership Validation')
transfer_agreement  = Transition(label='Transfer Agreement')
artifact_transport  = Transition(label='Artifact Transport')
restoration_work    = Transition(label='Restoration Work')
pr_campaign         = Transition(label='PR Campaign')
final_reporting     = Transition(label='Final Reporting')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    init_request,
    legal_review,
    historical_audit,
    stakeholder_map,
    risk_assessment,
    provenance_check,
    field_investigation,
    collector_contact,
    negotiation_phase,
    law_enforcement,
    ownership_validation,
    transfer_agreement,
    artifact_transport,
    restoration_work,
    pr_campaign,
    final_reporting
])

# Initiation leads to parallel due‐diligence activities
root.order.add_edge(init_request, legal_review)
root.order.add_edge(init_request, historical_audit)
root.order.add_edge(init_request, stakeholder_map)
root.order.add_edge(init_request, risk_assessment)

# After due‐diligence, perform provenance check
root.order.add_edge(legal_review, provenance_check)
root.order.add_edge(historical_audit, provenance_check)
root.order.add_edge(stakeholder_map, provenance_check)
root.order.add_edge(risk_assessment, provenance_check)

# Once provenance is checked, launch field work and contact/coordination
root.order.add_edge(provenance_check, field_investigation)
root.order.add_edge(provenance_check, collector_contact)
root.order.add_edge(provenance_check, law_enforcement)

# Negotiation follows collector contact
root.order.add_edge(collector_contact, negotiation_phase)

# Ownership validation depends on legal review and provenance check
root.order.add_edge(legal_review, ownership_validation)
root.order.add_edge(provenance_check, ownership_validation)

# Transfer agreement awaits negotiation, law enforcement, and ownership validation
root.order.add_edge(negotiation_phase, transfer_agreement)
root.order.add_edge(law_enforcement, transfer_agreement)
root.order.add_edge(ownership_validation, transfer_agreement)

# Final sequence: transport → restoration → PR → reporting
root.order.add_edge(transfer_agreement, artifact_transport)
root.order.add_edge(artifact_transport, restoration_work)
root.order.add_edge(restoration_work, pr_campaign)
root.order.add_edge(pr_campaign, final_reporting)