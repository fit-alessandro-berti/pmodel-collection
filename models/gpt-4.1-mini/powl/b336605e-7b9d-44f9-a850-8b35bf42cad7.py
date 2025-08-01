# Generated from: b336605e-7b9d-44f9-a850-8b35bf42cad7.json
# Description: This process manages the licensing of digital artifacts that are dynamically created and modified based on user interactions and environmental conditions. It involves capturing artifact metadata, verifying usage rights in real-time, negotiating adaptive license terms with multiple stakeholders, executing smart contracts, monitoring ongoing compliance through automated audits, and dynamically updating license conditions as artifacts evolve. The process ensures secure distribution, handles dispute resolution via decentralized arbitration, and integrates with external content management systems to synchronize license statuses. It also involves periodic reporting to licensors and licensees, enabling transparent usage tracking and payment settlements based on actual consumption patterns. This atypical licensing workflow combines legal, technical, and operational activities to support continuously changing digital assets in a robust, scalable, and compliant manner.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Capture_Metadata = Transition(label='Capture Metadata')
Verify_Rights = Transition(label='Verify Rights')
Negotiate_Terms = Transition(label='Negotiate Terms')
Execute_Contract = Transition(label='Execute Contract')
Monitor_Usage = Transition(label='Monitor Usage')
Audit_Compliance = Transition(label='Audit Compliance')
Update_License = Transition(label='Update License')
Distribute_Artifact = Transition(label='Distribute Artifact')
Resolve_Disputes = Transition(label='Resolve Disputes')
Sync_Systems = Transition(label='Sync Systems')
Generate_Reports = Transition(label='Generate Reports')
Process_Payments = Transition(label='Process Payments')
Track_Consumption = Transition(label='Track Consumption')
Notify_Stakeholders = Transition(label='Notify Stakeholders')
Archive_Records = Transition(label='Archive Records')
Review_Feedback = Transition(label='Review Feedback')
Adjust_Pricing = Transition(label='Adjust Pricing')

# The workflow as understood:
# 1) Capture Metadata
# 2) Verify Rights in real-time
# 3) Negotiate Terms with stakeholders
# 4) Execute Contract (smart contract)
# 5) Monitor Usage + Audit Compliance (can be concurrent)
# 6) Update License dynamically (loop with monitoring and audits)
# 7) Distribute Artifact securely
# 8) Resolve Disputes via decentralized arbitration
# 9) Sync with external content management systems
# 10) Reporting and payments & tracking consumption
# 11) Notifications and archival, feedback, pricing adjustments (continuous improvements/iterations)

# Create loop for step 6: Monitor+Audit -> Update License (loop)
monitor_audit = StrictPartialOrder(nodes=[Monitor_Usage, Audit_Compliance])
monitor_audit.order.add_edge(Monitor_Usage, Audit_Compliance)  # Audit after monitoring

# Loop: execute Update License after monitor_audit, then repeat monitoring+audit or exit loop
loop_update = OperatorPOWL(operator=Operator.LOOP, children=[Update_License, monitor_audit])

# Concurrent activities after contract execution: Distribute, Resolve Disputes, Sync Systems
concurrent_dist_resolve_sync = StrictPartialOrder(nodes=[Distribute_Artifact, Resolve_Disputes, Sync_Systems])

# Another concurrency block for reporting activities after distribution and sync:
reporting = StrictPartialOrder(
    nodes=[Generate_Reports, Process_Payments, Track_Consumption, Notify_Stakeholders, Archive_Records, Review_Feedback, Adjust_Pricing]
)

# Add some partial orders among reporting nodes to reflect logical flows:
# Track consumption before Process Payments
reporting.order.add_edge(Track_Consumption, Process_Payments)
# Generate reports before Notify Stakeholders
reporting.order.add_edge(Generate_Reports, Notify_Stakeholders)
# Notify Stakeholders before Review Feedback
reporting.order.add_edge(Notify_Stakeholders, Review_Feedback)
# Review Feedback before Adjust Pricing and Archive Records
reporting.order.add_edge(Review_Feedback, Adjust_Pricing)
reporting.order.add_edge(Review_Feedback, Archive_Records)

# Main sequential partial order from start to end
root = StrictPartialOrder(nodes=[
    Capture_Metadata,
    Verify_Rights,
    Negotiate_Terms,
    Execute_Contract,
    monitor_audit,
    loop_update,
    concurrent_dist_resolve_sync,
    reporting
])

# Add edges reflecting sequential ordering:
root.order.add_edge(Capture_Metadata, Verify_Rights)
root.order.add_edge(Verify_Rights, Negotiate_Terms)
root.order.add_edge(Negotiate_Terms, Execute_Contract)
root.order.add_edge(Execute_Contract, monitor_audit)
root.order.add_edge(monitor_audit, loop_update)
root.order.add_edge(loop_update, concurrent_dist_resolve_sync)
root.order.add_edge(concurrent_dist_resolve_sync, reporting)