# Generated from: 3b3c6bb3-cbcd-4037-a67e-f122041aa734.json
# Description: This process governs the secure and confidential exchange of proprietary artifacts between multinational corporations involved in joint ventures. It includes authentication, artifact classification, risk assessment, encryption, transfer approval, and compliance verification. The process ensures traceability and audit readiness, balancing intellectual property protection with collaboration efficiency. Each artifact undergoes integrity checks and metadata tagging before and after transit, involving multiple stakeholders such as legal, IT security, and project management. Post-transfer, reconciliation and feedback collection optimize future exchanges and mitigate potential disputes, making the process essential for maintaining trust and operational continuity in complex business ecosystems.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
verify_identity    = Transition(label="Verify Identity")
classify_artifact  = Transition(label="Classify Artifact")
assess_risk        = Transition(label="Assess Risk")
encrypt_data       = Transition(label="Encrypt Data")
request_approval   = Transition(label="Request Approval")
validate_compliance= Transition(label="Validate Compliance")
package_artifact   = Transition(label="Package Artifact")
initiate_transfer  = Transition(label="Initiate Transfer")
monitor_transit    = Transition(label="Monitor Transit")
integrity_check    = Transition(label="Integrity Check")
metadata_tag       = Transition(label="Metadata Tag")
notify_recipients  = Transition(label="Notify Recipients")
reconcile_records  = Transition(label="Reconcile Records")
collect_feedback   = Transition(label="Collect Feedback")
archive_logs       = Transition(label="Archive Logs")

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    verify_identity,
    classify_artifact,
    assess_risk,
    encrypt_data,
    request_approval,
    validate_compliance,
    package_artifact,
    initiate_transfer,
    monitor_transit,
    integrity_check,
    metadata_tag,
    notify_recipients,
    reconcile_records,
    collect_feedback,
    archive_logs
])

# Control‐flow dependencies
root.order.add_edge(verify_identity,     classify_artifact)
root.order.add_edge(classify_artifact,   assess_risk)
root.order.add_edge(assess_risk,         encrypt_data)
root.order.add_edge(encrypt_data,        request_approval)
root.order.add_edge(request_approval,    validate_compliance)
root.order.add_edge(validate_compliance, package_artifact)
root.order.add_edge(package_artifact,    initiate_transfer)
root.order.add_edge(initiate_transfer,   monitor_transit)

# After transit, perform integrity check and metadata tagging concurrently
root.order.add_edge(monitor_transit,     integrity_check)
root.order.add_edge(monitor_transit,     metadata_tag)
# Notify recipients once both integrity check and tagging are done
root.order.add_edge(integrity_check,     notify_recipients)
root.order.add_edge(metadata_tag,        notify_recipients)

# Post‐transfer steps
root.order.add_edge(notify_recipients,   reconcile_records)
root.order.add_edge(reconcile_records,   collect_feedback)
root.order.add_edge(collect_feedback,    archive_logs)