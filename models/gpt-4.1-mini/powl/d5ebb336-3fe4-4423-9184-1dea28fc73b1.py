# Generated from: d5ebb336-3fe4-4423-9184-1dea28fc73b1.json
# Description: This process involves synchronizing customer loyalty points and rewards across multiple sales channels including in-store, online, and mobile app platforms. It handles real-time data aggregation, conflict resolution for point discrepancies, fraud detection, personalized reward adjustments, and seamless redemption validation. The process integrates customer behavior analytics with external partner programs to maximize engagement and retention. Additionally, it manages asynchronous updates, rollback procedures for transaction failures, and compliance verification with regional reward regulations, ensuring a unified loyalty experience regardless of purchase channel or device used.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Data_Collection = Transition(label='Data Collection')
Point_Aggregation = Transition(label='Point Aggregation')
Conflict_Check = Transition(label='Conflict Check')
Fraud_Scan = Transition(label='Fraud Scan')
Reward_Adjust = Transition(label='Reward Adjust')
Redemption_Verify = Transition(label='Redemption Verify')
Partner_Sync = Transition(label='Partner Sync')
Behavior_Analyze = Transition(label='Behavior Analyze')
Async_Update = Transition(label='Async Update')
Rollback_Trigger = Transition(label='Rollback Trigger')
Compliance_Check = Transition(label='Compliance Check')
Notification_Send = Transition(label='Notification Send')
User_Feedback = Transition(label='User Feedback')
Report_Generate = Transition(label='Report Generate')
System_Audit = Transition(label='System Audit')

# Partial order for initial data processing (Data Collection -> Point Aggregation)
initial_proc = StrictPartialOrder(nodes=[Data_Collection, Point_Aggregation])
initial_proc.order.add_edge(Data_Collection, Point_Aggregation)

# Conflict resolution and scanning in parallel (Conflict Check || Fraud Scan)
conflict_fraud = StrictPartialOrder(nodes=[Conflict_Check, Fraud_Scan])

# Join conflict_fraud results before reward adjustment
conflict_to_reward = StrictPartialOrder(
    nodes=[conflict_fraud, Reward_Adjust]
)
conflict_to_reward.order.add_edge(conflict_fraud, Reward_Adjust)

# Redemption verification after reward adjustment
reward_to_redemption = StrictPartialOrder(
    nodes=[Reward_Adjust, Redemption_Verify]
)
reward_to_redemption.order.add_edge(Reward_Adjust, Redemption_Verify)

# Partner sync and behavior analyze concurrent after redemption verification
partner_behavior = StrictPartialOrder(
    nodes=[Partner_Sync, Behavior_Analyze]
)

# Both depend on redemption verify
partner_behavior_init = StrictPartialOrder(
    nodes=[reward_to_redemption, partner_behavior]
)
partner_behavior_init.order.add_edge(reward_to_redemption, partner_behavior)

# Async updates can run concurrently any time after partner sync and behavior analyze
async_update = Async_Update  # single node

# Compliance check after async update
async_to_compliance = StrictPartialOrder(
    nodes=[async_update, Compliance_Check]
)
async_to_compliance.order.add_edge(async_update, Compliance_Check)

# Rollback trigger choice loop:
# After compliance check, either exit or rollback trigger then re-run Compliance check
rollback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Compliance_Check,
        Rollback_Trigger
    ]
)

# Notifications and user feedback after compliance check (outside loop)
notify_feedback = StrictPartialOrder(
    nodes=[Notification_Send, User_Feedback]
)

# Both depend on compliance check (loop exit)
notify_feedback_init = StrictPartialOrder(
    nodes=[rollback_loop, notify_feedback]
)
notify_feedback_init.order.add_edge(rollback_loop, notify_feedback)

# Report generation and system audit after notifications and feedback
final_proc = StrictPartialOrder(
    nodes=[notify_feedback_init, Report_Generate, System_Audit]
)
final_proc.order.add_edge(notify_feedback_init, Report_Generate)
final_proc.order.add_edge(Report_Generate, System_Audit)

# Compose full model
# Compose initial_proc -> conflict_to_reward -> reward_to_redemption -> partner_behavior_init ->
# async_to_compliance -> rollback_loop -> notify_feedback_init -> final_proc chain with partial order edges

root = StrictPartialOrder(
    nodes=[
        initial_proc,
        conflict_to_reward,
        reward_to_redemption,
        partner_behavior_init,
        async_to_compliance,
        rollback_loop,
        notify_feedback_init,
        final_proc,
    ]
)

root.order.add_edge(initial_proc, conflict_to_reward)
root.order.add_edge(conflict_to_reward, reward_to_redemption)
root.order.add_edge(reward_to_redemption, partner_behavior_init)
root.order.add_edge(partner_behavior_init, async_to_compliance)
root.order.add_edge(async_to_compliance, rollback_loop)
root.order.add_edge(rollback_loop, notify_feedback_init)
root.order.add_edge(notify_feedback_init, final_proc)