# Generated from: 791123cb-a90b-43f3-ac30-ce2414b1db9a.json
# Description: This process manages the synchronization and optimization of customer loyalty rewards across multiple retail channels including in-store, online, and mobile app platforms. It involves complex data validation, real-time transaction tracking, personalized reward adjustments, fraud detection, and dynamic points allocation based on customer behavior analytics. The process also integrates third-party marketing campaigns and seasonal promotions, ensuring consistent and accurate reward redemption experiences. Additionally, it includes feedback loops for continuous algorithm tuning and compliance checks with privacy regulations to protect customer data while maximizing engagement and retention.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
data_import      = Transition(label='Data Import')
transaction_match= Transition(label='Transaction Match')
fraud_check      = Transition(label='Fraud Check')
points_adjust    = Transition(label='Points Adjust')
promo_sync       = Transition(label='Promo Sync')
campaign_merge   = Transition(label='Campaign Merge')
behavior_scan    = Transition(label='Behavior Scan')
reward_calc      = Transition(label='Reward Calc')
redemption_track = Transition(label='Redemption Track')
customer_notify  = Transition(label='Customer Notify')
report_generate  = Transition(label='Report Generate')
feedback_log     = Transition(label='Feedback Log')
algorithm_tune   = Transition(label='Algorithm Tune')
privacy_audit    = Transition(label='Privacy Audit')
compliance_verify= Transition(label='Compliance Verify')
channel_update   = Transition(label='Channel Update')

# Build a partial order for the compliance sub‐process
comp_checks = StrictPartialOrder(nodes=[privacy_audit, compliance_verify])
comp_checks.order.add_edge(privacy_audit, compliance_verify)

# Loop for continuous algorithm tuning and compliance checks
tuning_loop = OperatorPOWL(operator=Operator.LOOP, children=[algorithm_tune, comp_checks])

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[
    data_import, transaction_match, fraud_check, points_adjust,
    promo_sync, campaign_merge, channel_update, behavior_scan,
    reward_calc, redemption_track, customer_notify,
    report_generate, feedback_log, tuning_loop
])

# Define control‐flow dependencies
root.order.add_edge(data_import,       transaction_match)
root.order.add_edge(transaction_match, fraud_check)
root.order.add_edge(fraud_check,       points_adjust)

root.order.add_edge(points_adjust,     promo_sync)
root.order.add_edge(points_adjust,     campaign_merge)
root.order.add_edge(points_adjust,     channel_update)

root.order.add_edge(promo_sync,        behavior_scan)
root.order.add_edge(campaign_merge,    behavior_scan)

root.order.add_edge(behavior_scan,     reward_calc)
root.order.add_edge(channel_update,    reward_calc)

root.order.add_edge(reward_calc,       redemption_track)
root.order.add_edge(redemption_track,  customer_notify)

root.order.add_edge(customer_notify,   report_generate)
root.order.add_edge(customer_notify,   feedback_log)

root.order.add_edge(report_generate,   tuning_loop)
root.order.add_edge(feedback_log,      tuning_loop)