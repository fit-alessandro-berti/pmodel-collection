# Generated from: 482b2c2a-4757-4dc3-952c-fdbaf5038804.json
# Description: This process governs the complex compliance workflow for cryptocurrency exchanges to ensure adherence to international regulations and internal policies. It involves verifying user identities, monitoring transactions for suspicious activity, conducting risk assessments, coordinating with legal teams for regulatory updates, and managing reporting obligations to financial authorities. The workflow also integrates blockchain analysis tools to track token provenance and flags irregular patterns for manual review. Continuous updates to compliance frameworks and employee training ensure the process adapts to evolving legal landscapes while maintaining efficient customer onboarding and transaction processing within secure parameters.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for the activities
Identity_Check = Transition(label='Identity Check')
Risk_Assessment = Transition(label='Risk Assessment')
Transaction_Scan = Transition(label='Transaction Scan')
Flag_Review = Transition(label='Flag Review')
Legal_Update = Transition(label='Legal Update')
Policy_Revision = Transition(label='Policy Revision')
User_Onboarding = Transition(label='User Onboarding')
Token_Tracking = Transition(label='Token Tracking')
Manual_Audit = Transition(label='Manual Audit')
Report_Generation = Transition(label='Report Generation')
Training_Session = Transition(label='Training Session')
Compliance_Meeting = Transition(label='Compliance Meeting')
Data_Encryption = Transition(label='Data Encryption')
Alert_Dispatch = Transition(label='Alert Dispatch')
Feedback_Loop = Transition(label='Feedback Loop')
System_Update = Transition(label='System Update')

# Build partial orders and control-flow structures reflecting process logic:

# 1. User Onboarding requires Identity Check -> Risk Assessment -> Transaction Scan
onboarding_sequence = StrictPartialOrder(nodes=[Identity_Check, Risk_Assessment, Transaction_Scan, User_Onboarding])
onboarding_sequence.order.add_edge(Identity_Check, Risk_Assessment)
onboarding_sequence.order.add_edge(Risk_Assessment, Transaction_Scan)
onboarding_sequence.order.add_edge(Transaction_Scan, User_Onboarding)

# 2. Token Tracking (blockchain analysis) runs concurrent with onboarding but before Flag Review and Manual Audit
token_and_flag = StrictPartialOrder(nodes=[Token_Tracking, Flag_Review, Manual_Audit])
token_and_flag.order.add_edge(Token_Tracking, Flag_Review)
token_and_flag.order.add_edge(Flag_Review, Manual_Audit)

# 3. Manual Audit is triggered by Flag Review - sequential

# 4. Risk Assessment and Transaction Scan are prerequisite for Flag Review (so connect onboarding_sequence end to Flag Review start)
# Actually, we linked Transaction Scan->User Onboarding, so we link User Onboarding -> Flag Review for the suspicious flags path
# But the Token Tracking runs in parallel to User Onboarding and leads to Flag Review

# So we merge Token Tracking and onboarding partial order concurrent with edges:
# User Onboarding and Token Tracking are concurrent after Transaction Scan? Actually Token Tracking analyses tokens along with onboarding.

# We'll build a strict partial order with nodes = onboarding_sequence + token_and_flag (excluding duplicates)

concurrent_onboarding_token = StrictPartialOrder(
    nodes=[Identity_Check, Risk_Assessment, Transaction_Scan, User_Onboarding, Token_Tracking, Flag_Review, Manual_Audit]
)
concurrent_onboarding_token.order.add_edge(Identity_Check, Risk_Assessment)
concurrent_onboarding_token.order.add_edge(Risk_Assessment, Transaction_Scan)
concurrent_onboarding_token.order.add_edge(Transaction_Scan, User_Onboarding)
concurrent_onboarding_token.order.add_edge(Token_Tracking, Flag_Review)
concurrent_onboarding_token.order.add_edge(Flag_Review, Manual_Audit)

# Add concurrency: User_Onboarding and Token_Tracking can run in parallel after Transaction_Scan,
# so no order between User_Onboarding and Token_Tracking
# Flag_Review after both User_Onboarding and Token_Tracking? We only have Token_Tracking->Flag_Review,
# To reflect dependency also from User_Onboarding, add User_Onboarding->Flag_Review
concurrent_onboarding_token.order.add_edge(User_Onboarding, Flag_Review)

# 5. Reporting branch: Report Generation depends on Manual Audit and Compliance Meeting
report_branch = StrictPartialOrder(nodes=[Manual_Audit, Compliance_Meeting, Report_Generation])
report_branch.order.add_edge(Manual_Audit, Report_Generation)
report_branch.order.add_edge(Compliance_Meeting, Report_Generation)

# 6. Training and Policy: loops for updating policies with Legal Update, Policy Revision, Training Session, System Update
# Represented as a loop to indicate continuous improvement with feedback

# Loop body:
policy_update_seq = StrictPartialOrder(
    nodes=[Legal_Update, Policy_Revision, Training_Session, System_Update]
)
policy_update_seq.order.add_edge(Legal_Update, Policy_Revision)
policy_update_seq.order.add_edge(Policy_Revision, Training_Session)
policy_update_seq.order.add_edge(Training_Session, System_Update)

# Feedback loop to Legal_Update:
# loop = LOOP(body=policy_update_seq, redo=Feedback_Loop)
feedback = Transition(label='Feedback Loop')
loop_policy = OperatorPOWL(operator=Operator.LOOP, children=[policy_update_seq, feedback])

# 7. Data Encryption and Alert Dispatch occur after Report Generation and Manual Audit, perhaps in parallel
security_and_alert = StrictPartialOrder(nodes=[Data_Encryption, Alert_Dispatch])
# No order -> concurrent

# 8. Connect report_branch and security_and_alert partial orders
# Report_Generation -> Data_Encryption and Alert_Dispatch
report_and_security = StrictPartialOrder(
    nodes=[Manual_Audit, Compliance_Meeting, Report_Generation, Data_Encryption, Alert_Dispatch]
)
report_and_security.order.add_edge(Manual_Audit, Report_Generation)
report_and_security.order.add_edge(Compliance_Meeting, Report_Generation)
report_and_security.order.add_edge(Report_Generation, Data_Encryption)
report_and_security.order.add_edge(Report_Generation, Alert_Dispatch)

# 9. Finally root partial order combining all major parts:
# concurrent_onboarding_token (initial activities)
# report_and_security (reporting and security)
# loop_policy (policy updates)
root = StrictPartialOrder(
    nodes=[concurrent_onboarding_token, report_and_security, loop_policy]
)
# Ordering: concurrent_onboarding_token directs to report_and_security (i.e. process flow)
root.order.add_edge(concurrent_onboarding_token, report_and_security)
# loop_policy is independent, runs concurrently (continuous process)
