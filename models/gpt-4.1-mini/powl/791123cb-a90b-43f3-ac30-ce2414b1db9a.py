# Generated from: 791123cb-a90b-43f3-ac30-ce2414b1db9a.json
# Description: This process manages the synchronization and optimization of customer loyalty rewards across multiple retail channels including in-store, online, and mobile app platforms. It involves complex data validation, real-time transaction tracking, personalized reward adjustments, fraud detection, and dynamic points allocation based on customer behavior analytics. The process also integrates third-party marketing campaigns and seasonal promotions, ensuring consistent and accurate reward redemption experiences. Additionally, it includes feedback loops for continuous algorithm tuning and compliance checks with privacy regulations to protect customer data while maximizing engagement and retention.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
DataImport = Transition(label='Data Import')
TransactionMatch = Transition(label='Transaction Match')
FraudCheck = Transition(label='Fraud Check')
PointsAdjust = Transition(label='Points Adjust')
PromoSync = Transition(label='Promo Sync')
CampaignMerge = Transition(label='Campaign Merge')
BehaviorScan = Transition(label='Behavior Scan')
RewardCalc = Transition(label='Reward Calc')
PrivacyAudit = Transition(label='Privacy Audit')
ComplianceVerify = Transition(label='Compliance Verify')
CustomerNotify = Transition(label='Customer Notify')
FeedbackLog = Transition(label='Feedback Log')
AlgorithmTune = Transition(label='Algorithm Tune')
ChannelUpdate = Transition(label='Channel Update')
RedemptionTrack = Transition(label='Redemption Track')
ReportGenerate = Transition(label='Report Generate')

# Define feedback loop: FeedbackLog and AlgorithmTune in a LOOP
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackLog, AlgorithmTune])

# Compliance check partial order: PrivacyAudit --> ComplianceVerify
compliance_check = StrictPartialOrder(
    nodes=[PrivacyAudit, ComplianceVerify]
)
compliance_check.order.add_edge(PrivacyAudit, ComplianceVerify)

# Fraud detection and points adjustment partial order:
fraud_and_adjust = StrictPartialOrder(
    nodes=[FraudCheck, PointsAdjust]
)
fraud_and_adjust.order.add_edge(FraudCheck, PointsAdjust)

# Marketing and promo sync partial order: PromoSync --> CampaignMerge
promo_campaign = StrictPartialOrder(
    nodes=[PromoSync, CampaignMerge]
)
promo_campaign.order.add_edge(PromoSync, CampaignMerge)

# Behavior analytics and reward calc parallel to above but ordered behavior scan --> reward calc
behavior_reward = StrictPartialOrder(
    nodes=[BehaviorScan, RewardCalc]
)
behavior_reward.order.add_edge(BehaviorScan, RewardCalc)

# Redemption tracking and report generation partial order: RedemptionTrack --> ReportGenerate
redemption_report = StrictPartialOrder(
    nodes=[RedemptionTrack, ReportGenerate]
)
redemption_report.order.add_edge(RedemptionTrack, ReportGenerate)

# Channel update and customer notify partial order: ChannelUpdate --> CustomerNotify
channel_notify = StrictPartialOrder(
    nodes=[ChannelUpdate, CustomerNotify]
)
channel_notify.order.add_edge(ChannelUpdate, CustomerNotify)

# Initial data validation and transaction match partial order: DataImport --> TransactionMatch
initial_validation = StrictPartialOrder(
    nodes=[DataImport, TransactionMatch]
)
initial_validation.order.add_edge(DataImport, TransactionMatch)

# Build a strict partial order to sequence the main phases
# Phase 1: initial_validation
# Phase 2: fraud_and_adjust, promo_campaign, behavior_reward can run in parallel (no mutual order)
# Phase 3: compliance_check
# Phase 4: redemption_report and channel_notify can run in parallel 
# Phase 5: customer notify already in channel_notify, so treated
# Phase 6: feedback loop after compliance_check and redemption_report and channel_notify

# Combine fraud_and_adjust, promo_campaign, behavior_reward together as parallel nodes
phase2_nodes = [fraud_and_adjust, promo_campaign, behavior_reward]

# Combine redemption_report and channel_notify as parallel nodes
phase4_nodes = [redemption_report, channel_notify]

# Create root StrictPartialOrder with nodes for all phases and feedback loop
root = StrictPartialOrder(
    nodes=[
        initial_validation,
        fraud_and_adjust,
        promo_campaign,
        behavior_reward,
        compliance_check,
        redemption_report,
        channel_notify,
        feedback_loop
    ]
)

# Add order edges for phases:
# initial_validation --> fraud_and_adjust
root.order.add_edge(initial_validation, fraud_and_adjust)
# initial_validation --> promo_campaign
root.order.add_edge(initial_validation, promo_campaign)
# initial_validation --> behavior_reward
root.order.add_edge(initial_validation, behavior_reward)

# fraud_and_adjust --> compliance_check
root.order.add_edge(fraud_and_adjust, compliance_check)
# promo_campaign --> compliance_check
root.order.add_edge(promo_campaign, compliance_check)
# behavior_reward --> compliance_check
root.order.add_edge(behavior_reward, compliance_check)

# compliance_check --> redemption_report
root.order.add_edge(compliance_check, redemption_report)
# compliance_check --> channel_notify
root.order.add_edge(compliance_check, channel_notify)

# redemption_report --> feedback_loop
root.order.add_edge(redemption_report, feedback_loop)
# channel_notify --> feedback_loop
root.order.add_edge(channel_notify, feedback_loop)