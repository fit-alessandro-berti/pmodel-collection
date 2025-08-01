# Generated from: 482b2c2a-4757-4dc3-952c-fdbaf5038804.json
# Description: This process governs the complex compliance workflow for cryptocurrency exchanges to ensure adherence to international regulations and internal policies. It involves verifying user identities, monitoring transactions for suspicious activity, conducting risk assessments, coordinating with legal teams for regulatory updates, and managing reporting obligations to financial authorities. The workflow also integrates blockchain analysis tools to track token provenance and flags irregular patterns for manual review. Continuous updates to compliance frameworks and employee training ensure the process adapts to evolving legal landscapes while maintaining efficient customer onboarding and transaction processing within secure parameters.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
identity_check    = Transition(label='Identity Check')
risk_assessment   = Transition(label='Risk Assessment')
transaction_scan  = Transition(label='Transaction Scan')
flag_review       = Transition(label='Flag Review')
legal_update      = Transition(label='Legal Update')
policy_revision   = Transition(label='Policy Revision')
user_onboarding   = Transition(label='User Onboarding')
token_tracking    = Transition(label='Token Tracking')
manual_audit      = Transition(label='Manual Audit')
report_generation = Transition(label='Report Generation')
training_session  = Transition(label='Training Session')
compliance_meeting= Transition(label='Compliance Meeting')
data_encryption   = Transition(label='Data Encryption')
alert_dispatch    = Transition(label='Alert Dispatch')
feedback_loop     = Transition(label='Feedback Loop')
system_update     = Transition(label='System Update')

# Part 1: Initial onboarding (strict sequence)
onboard_po = StrictPartialOrder(nodes=[user_onboarding, identity_check, data_encryption])
onboard_po.order.add_edge(user_onboarding, identity_check)
onboard_po.order.add_edge(identity_check, data_encryption)

# Part 2: Continuous transaction-monitoring loop
# 2a: Scanning phase A
scan_phase = StrictPartialOrder(nodes=[transaction_scan, risk_assessment, token_tracking])
scan_phase.order.add_edge(transaction_scan, risk_assessment)
scan_phase.order.add_edge(risk_assessment, token_tracking)

# 2b: Suspicious‐handling phase B
suspicious_phase = StrictPartialOrder(nodes=[
    flag_review,
    alert_dispatch,
    manual_audit,
    report_generation,
    compliance_meeting,
    training_session,
    feedback_loop,
    legal_update,
    policy_revision,
    system_update
])
suspicious_phase.order.add_edge(flag_review, manual_audit)
suspicious_phase.order.add_edge(flag_review, alert_dispatch)
suspicious_phase.order.add_edge(manual_audit, report_generation)
suspicious_phase.order.add_edge(report_generation, compliance_meeting)
suspicious_phase.order.add_edge(report_generation, training_session)
suspicious_phase.order.add_edge(compliance_meeting, feedback_loop)
suspicious_phase.order.add_edge(training_session, feedback_loop)
suspicious_phase.order.add_edge(feedback_loop, legal_update)
suspicious_phase.order.add_edge(legal_update, policy_revision)
suspicious_phase.order.add_edge(policy_revision, system_update)

# Build the LOOP operator: do scan_phase, then either exit or do suspicious_phase and repeat
main_loop = OperatorPOWL(operator=Operator.LOOP, children=[scan_phase, suspicious_phase])

# Root model: onboarding followed by the perpetual monitoring loop
root = StrictPartialOrder(nodes=[onboard_po, main_loop])
root.order.add_edge(onboard_po, main_loop)