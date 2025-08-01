# Generated from: 3b3c6bb3-cbcd-4037-a67e-f122041aa734.json
# Description: This process governs the secure and confidential exchange of proprietary artifacts between multinational corporations involved in joint ventures. It includes authentication, artifact classification, risk assessment, encryption, transfer approval, and compliance verification. The process ensures traceability and audit readiness, balancing intellectual property protection with collaboration efficiency. Each artifact undergoes integrity checks and metadata tagging before and after transit, involving multiple stakeholders such as legal, IT security, and project management. Post-transfer, reconciliation and feedback collection optimize future exchanges and mitigate potential disputes, making the process essential for maintaining trust and operational continuity in complex business ecosystems.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions (activities)
Verify_Identity = Transition(label='Verify Identity')
Classify_Artifact = Transition(label='Classify Artifact')
Assess_Risk = Transition(label='Assess Risk')
Encrypt_Data = Transition(label='Encrypt Data')

Request_Approval = Transition(label='Request Approval')

Validate_Compliance = Transition(label='Validate Compliance')
Package_Artifact = Transition(label='Package Artifact')

Initiate_Transfer = Transition(label='Initiate Transfer')
Monitor_Transit = Transition(label='Monitor Transit')

Integrity_Check = Transition(label='Integrity Check')
Metadata_Tag = Transition(label='Metadata Tag')

Notify_Recipients = Transition(label='Notify Recipients')

Reconcile_Records = Transition(label='Reconcile Records')
Collect_Feedback = Transition(label='Collect Feedback')
Archive_Logs = Transition(label='Archive Logs')

# Pre-transfer quality assurance (integrity + metadata tagging)
pre_transfer_qc = StrictPartialOrder(nodes=[Integrity_Check, Metadata_Tag])
pre_transfer_qc.order.add_edge(Integrity_Check, Metadata_Tag)

# Post-transfer quality assurance (integrity + metadata tagging)
post_transfer_qc = StrictPartialOrder(nodes=[Integrity_Check, Metadata_Tag])
post_transfer_qc.order.add_edge(Integrity_Check, Metadata_Tag)

# After Monitor Transit completes, do post-transfer integrity check and tagging in sequence
post_transfer_qc_after_monitor = StrictPartialOrder(nodes=[Monitor_Transit, post_transfer_qc])
post_transfer_qc_after_monitor.order.add_edge(Monitor_Transit, post_transfer_qc)

# After compliance and packaging, initiate transfer
compliance_and_packaging = StrictPartialOrder(nodes=[Validate_Compliance, Package_Artifact])
# Let's assume no explicit order between Validate_Compliance and Package_Artifact, so concurrent.

# After classification and risk assessment, encrypt data
classify_risk_encrypt = StrictPartialOrder(nodes=[Classify_Artifact, Assess_Risk, Encrypt_Data])
classify_risk_encrypt.order.add_edge(Classify_Artifact, Encrypt_Data)
classify_risk_encrypt.order.add_edge(Assess_Risk, Encrypt_Data)
# The Classify and Assess_Risk are concurrent, both must complete before Encrypt_Data

# Request approval is after encryption
encrypt_plus_approval = StrictPartialOrder(nodes=[classify_risk_encrypt, Request_Approval])
encrypt_plus_approval.order.add_edge(classify_risk_encrypt, Request_Approval)

# After approval, validate compliance and package artifact done concurrently
approval_plus_comp_pack = StrictPartialOrder(nodes=[Request_Approval, compliance_and_packaging])
approval_plus_comp_pack.order.add_edge(Request_Approval, compliance_and_packaging)

# Pre-transfer part combining all before initiating transfer
pre_transfer = StrictPartialOrder(nodes=[Verify_Identity, encrypt_plus_approval, approval_plus_comp_pack, pre_transfer_qc])
pre_transfer.order.add_edge(Verify_Identity, encrypt_plus_approval)
pre_transfer.order.add_edge(encrypt_plus_approval, approval_plus_comp_pack)
pre_transfer.order.add_edge(approval_plus_comp_pack, pre_transfer_qc)

# Initiate Transfer after pre-transfer quality control
initiate_and_monitor = StrictPartialOrder(nodes=[Initiate_Transfer, Monitor_Transit])
initiate_and_monitor.order.add_edge(Initiate_Transfer, Monitor_Transit)

# Notify recipients happens after post_transfer_qc
notify_after_post_qc = StrictPartialOrder(nodes=[post_transfer_qc, Notify_Recipients])
notify_after_post_qc.order.add_edge(post_transfer_qc, Notify_Recipients)

# Post-transfer process: reconcile records, collect feedback, archive logs
# Assume reconcile first, then feedback and archive concurrent
reconcile_then_feedback_archive = StrictPartialOrder(nodes=[Reconcile_Records, Collect_Feedback, Archive_Logs])
reconcile_then_feedback_archive.order.add_edge(Reconcile_Records, Collect_Feedback)
reconcile_then_feedback_archive.order.add_edge(Reconcile_Records, Archive_Logs)

# Full post-transfer sequence
post_transfer = StrictPartialOrder(nodes=[post_transfer_qc_after_monitor, notify_after_post_qc, reconcile_then_feedback_archive])
post_transfer.order.add_edge(post_transfer_qc_after_monitor, notify_after_post_qc)
post_transfer.order.add_edge(notify_after_post_qc, reconcile_then_feedback_archive)

# Combine all main parts sequentially:
# pre_transfer -> initiate_and_monitor -> post_transfer
root = StrictPartialOrder(
    nodes=[pre_transfer, initiate_and_monitor, post_transfer]
)
root.order.add_edge(pre_transfer, initiate_and_monitor)
root.order.add_edge(initiate_and_monitor, post_transfer)