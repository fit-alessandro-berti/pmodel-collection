# Generated from: af2ad303-7f6a-4093-8dcd-fff50c8d6bbf.json
# Description: This process orchestrates the synchronization of customer loyalty data across multiple sales channels including in-store, online, mobile app, and third-party partners. It involves real-time data validation, conflict resolution for overlapping rewards, dynamic points recalculation based on channel-specific promotions, and secure data exchange protocols. Additionally, it incorporates anomaly detection to flag suspicious activity, automated customer notifications about point updates or expirations, and a feedback loop to update marketing strategies based on loyalty trends. The process ensures consistency and accuracy of loyalty benefits while enhancing customer engagement and preventing fraud across diverse platforms.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
DataIngest = Transition(label='Data Ingest')
ValidateEntries = Transition(label='Validate Entries')
ConflictCheck = Transition(label='Conflict Check')
PointsRecalc = Transition(label='Points Recalc')
PromoApply = Transition(label='Promo Apply')
FraudScan = Transition(label='Fraud Scan')
NotifyUser = Transition(label='Notify User')
SyncPartners = Transition(label='Sync Partners')
UpdateLedger = Transition(label='Update Ledger')
TrendAnalyze = Transition(label='Trend Analyze')
FeedbackLoop = Transition(label='Feedback Loop')
AdjustRules = Transition(label='Adjust Rules')
ArchiveLogs = Transition(label='Archive Logs')
ReportGenerate = Transition(label='Report Generate')
AuditTrail = Transition(label='Audit Trail')

skip = SilentTransition()

# Model the inner loop for FeedbackLoop and AdjustRules
# Loop: execute FeedbackLoop, then choose to exit or execute AdjustRules then FeedbackLoop again
feedback_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackLoop, AdjustRules])

# Compose a sequence for trend analysis then loop over feedback-adjust
trend_feedback_part = StrictPartialOrder(nodes=[TrendAnalyze, feedback_adjust_loop])
trend_feedback_part.order.add_edge(TrendAnalyze, feedback_adjust_loop)

# Points recalculation and promo apply are concurrent after conflict check
points_promo = StrictPartialOrder(nodes=[PointsRecalc, PromoApply])  # concurrent (no order)

# NotifyUser and SyncPartners are concurrent activities after fraud scan
notify_sync = StrictPartialOrder(nodes=[NotifyUser, SyncPartners])  # concurrent (no order)

# Data validation part: ValidateEntries -> ConflictCheck
validation_part = StrictPartialOrder(nodes=[ValidateEntries, ConflictCheck])
validation_part.order.add_edge(ValidateEntries, ConflictCheck)

# The core data processing partial order:
# DataIngest -> ValidateEntries -> ConflictCheck -> (PointsRecalc || PromoApply) -> FraudScan -> (NotifyUser || SyncPartners) -> UpdateLedger
process_seq = StrictPartialOrder(
    nodes=[
        DataIngest,
        validation_part,
        points_promo,
        FraudScan,
        notify_sync,
        UpdateLedger
    ]
)

# Define internal edges for embedded StrictPartialOrders within
# We treat validation_part, points_promo, notify_sync as nodes within process_seq.
# So edges from process_seq from one node to the next:

# Add edges between the main nodes inside process_seq:
process_seq.order.add_edge(DataIngest, validation_part)
process_seq.order.add_edge(validation_part, points_promo)
process_seq.order.add_edge(points_promo, FraudScan)
process_seq.order.add_edge(FraudScan, notify_sync)
process_seq.order.add_edge(notify_sync, UpdateLedger)

# Final part after ledger update: ArchiveLogs, ReportGenerate and AuditTrail concurrent with trend_feedback_part
# So these four nodes are concurrent:
final_concurrent = StrictPartialOrder(
    nodes=[ArchiveLogs, ReportGenerate, AuditTrail, trend_feedback_part]
)

# The root process orders UpdateLedger --> final_concurrent
root = StrictPartialOrder(
    nodes=[process_seq, final_concurrent]
)
root.order.add_edge(process_seq, final_concurrent)