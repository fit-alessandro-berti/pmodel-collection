# Generated from: 4a3c0b9f-e093-4195-96c5-9f5937c0f645.json
# Description: This process involves the complex verification and authentication of ancient artifacts crossing international borders. It includes multi-disciplinary collaboration between historians, customs officials, forensic analysts, and legal experts to ensure provenance accuracy, compliance with cultural heritage laws, and secure transportation. The procedure requires detailed historical research, chemical composition analysis, photographic documentation, legal clearance, and diplomatic coordination to prevent illicit trafficking and preserve cultural integrity. Each step is critical to validate authenticity, legality, and safe delivery to museums or private collectors while respecting international treaties and ethical standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
artifact_logging    = Transition(label='Artifact Logging')
historical_review   = Transition(label='Historical Review')
customs_check       = Transition(label='Customs Check')
chemical_scan       = Transition(label='Chemical Scan')
provenance_match    = Transition(label='Provenance Match')
photo_capture       = Transition(label='Photo Capture')
legal_review        = Transition(label='Legal Review')
diplomatic_notify   = Transition(label='Diplomatic Notify')
security_clear      = Transition(label='Security Clear')
transport_arrange   = Transition(label='Transport Arrange')
condition_report    = Transition(label='Condition Report')
data_archiving      = Transition(label='Data Archiving')
stakeholder_update  = Transition(label='Stakeholder Update')
final_approval      = Transition(label='Final Approval')
delivery_confirm    = Transition(label='Delivery Confirm')

# Build a single partial‐order model that captures concurrency and dependencies
root = StrictPartialOrder(nodes=[
    artifact_logging, historical_review, customs_check,
    chemical_scan, provenance_match, photo_capture,
    legal_review, diplomatic_notify, security_clear,
    transport_arrange, condition_report, data_archiving,
    stakeholder_update, final_approval, delivery_confirm
])

# Add precedence relations
root.order.add_edge(artifact_logging, historical_review)
root.order.add_edge(artifact_logging, customs_check)

# After historical review, run scans and photo in parallel
root.order.add_edge(historical_review, chemical_scan)
root.order.add_edge(historical_review, photo_capture)

# Provenance match depends on chemical scan
root.order.add_edge(chemical_scan, provenance_match)

# Legal review and diplomatic notify wait for both customs check & provenance match
root.order.add_edge(customs_check, legal_review)
root.order.add_edge(provenance_match, legal_review)
root.order.add_edge(customs_check, diplomatic_notify)
root.order.add_edge(provenance_match, diplomatic_notify)

# After legal & diplomatic check, prepare secure transport
root.order.add_edge(legal_review, security_clear)
root.order.add_edge(diplomatic_notify, security_clear)
root.order.add_edge(legal_review, transport_arrange)
root.order.add_edge(diplomatic_notify, transport_arrange)

# Condition report once security & transport arranged
root.order.add_edge(security_clear, condition_report)
root.order.add_edge(transport_arrange, condition_report)

# Archiving and stakeholder update in parallel
root.order.add_edge(condition_report, data_archiving)
root.order.add_edge(condition_report, stakeholder_update)

# Final approval after archiving & update, then delivery confirmation
root.order.add_edge(data_archiving, final_approval)
root.order.add_edge(stakeholder_update, final_approval)
root.order.add_edge(final_approval, delivery_confirm)