# Generated from: d5ebb336-3fe4-4423-9184-1dea28fc73b1.json
# Description: This process involves synchronizing customer loyalty points and rewards across multiple sales channels including in-store, online, and mobile app platforms. It handles real-time data aggregation, conflict resolution for point discrepancies, fraud detection, personalized reward adjustments, and seamless redemption validation. The process integrates customer behavior analytics with external partner programs to maximize engagement and retention. Additionally, it manages asynchronous updates, rollback procedures for transaction failures, and compliance verification with regional reward regulations, ensuring a unified loyalty experience regardless of purchase channel or device used.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
data_collection    = Transition(label='Data Collection')
point_aggregation  = Transition(label='Point Aggregation')
conflict_check     = Transition(label='Conflict Check')
fraud_scan         = Transition(label='Fraud Scan')
rollback_trigger   = Transition(label='Rollback Trigger')
async_update_rb    = Transition(label='Async Update')
reward_adjust      = Transition(label='Reward Adjust')
async_update_norm  = Transition(label='Async Update')
compliance_check   = Transition(label='Compliance Check')
redemption_verify  = Transition(label='Redemption Verify')
partner_sync       = Transition(label='Partner Sync')
behavior_analyze   = Transition(label='Behavior Analyze')
report_generate    = Transition(label='Report Generate')
notification_send  = Transition(label='Notification Send')
user_feedback      = Transition(label='User Feedback')
system_audit       = Transition(label='System Audit')

# Rollback subprocess: Trigger rollback then async update
rollback_seq = StrictPartialOrder(
    nodes=[rollback_trigger, async_update_rb]
)
rollback_seq.order.add_edge(rollback_trigger, async_update_rb)

# Loop for fraud resolution: do a fraud scan, if failed then rollback_seq and repeat
fraud_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[fraud_scan, rollback_seq]
)

# Main process partial order
root = StrictPartialOrder(
    nodes=[
        data_collection,
        point_aggregation,
        conflict_check,
        fraud_loop,
        reward_adjust,
        async_update_norm,
        compliance_check,
        redemption_verify,
        partner_sync,
        behavior_analyze,
        report_generate,
        notification_send,
        user_feedback,
        system_audit
    ]
)

# Define the control-flow dependencies
root.order.add_edge(data_collection,   point_aggregation)
root.order.add_edge(point_aggregation, conflict_check)
root.order.add_edge(conflict_check,    fraud_loop)
root.order.add_edge(fraud_loop,        reward_adjust)
root.order.add_edge(reward_adjust,     async_update_norm)
root.order.add_edge(async_update_norm, compliance_check)
root.order.add_edge(compliance_check,  redemption_verify)
root.order.add_edge(redemption_verify, partner_sync)
root.order.add_edge(redemption_verify, behavior_analyze)

# After both partner sync and behavior analysis, end activities can execute concurrently
for end_activity in [report_generate, notification_send, user_feedback, system_audit]:
    root.order.add_edge(partner_sync,      end_activity)
    root.order.add_edge(behavior_analyze,  end_activity)