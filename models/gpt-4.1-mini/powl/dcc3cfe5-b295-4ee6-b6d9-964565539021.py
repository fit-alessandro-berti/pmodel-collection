# Generated from: dcc3cfe5-b295-4ee6-b6d9-964565539021.json
# Description: This process involves leveraging a global network of independent couriers and local hubs to dynamically optimize package delivery routes in real-time. It integrates AI-driven demand forecasting with crowdsourced labor allocation, allowing rapid adaptation to fluctuating delivery volumes and traffic conditions. The system continuously collects performance data, validates courier credentials, and manages incentives through a decentralized blockchain ledger. It includes risk assessment for package security, automated dispute resolution, and real-time customer notifications. The process culminates with delivery confirmation and feedback incorporation to improve future operations and enhance overall service reliability and efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities as Transitions
Demand_Forecast = Transition(label='Demand Forecast')
Courier_Match = Transition(label='Courier Match')
Credential_Check = Transition(label='Credential Check')
Route_Design = Transition(label='Route Design')
Load_Assign = Transition(label='Load Assign')
Traffic_Scan = Transition(label='Traffic Scan')
Package_Secure = Transition(label='Package Secure')
Dispatch_Alert = Transition(label='Dispatch Alert')
Real_time_Track = Transition(label='Real-time Track')
Incentive_Issue = Transition(label='Incentive Issue')
Dispute_Review = Transition(label='Dispute Review')
Customer_Notify = Transition(label='Customer Notify')
Feedback_Collect = Transition(label='Feedback Collect')
Performance_Log = Transition(label='Performance Log')
Ledger_Update = Transition(label='Ledger Update')
Hub_Sync = Transition(label='Hub Sync')

# The process loosely follows this pattern:

# 1) Demand Forecast feeds Courier Match
# 2) Courier Match must have Credential Check before Route Design
# 3) Route Design -> Load Assign -> Traffic Scan can run concurrently with Package Secure
# 4) Dispatch Alert follows those preparations
# 5) Real-time Track and Incentive Issue run concurrently, and Incentive Issue updates Ledger
# 6) Dispute Review and Customer Notify are alternative branches after Dispatch Alert
# 7) Feedback Collect and Performance Log run concurrently at the end
# 8) Hub Sync updates concurrently with Ledger Update in the background throughout

# Build sub partial orders and choices reflecting this:

# Step 1 and 2 sequence
step1_2 = StrictPartialOrder(nodes=[Demand_Forecast, Courier_Match, Credential_Check, Route_Design])
step1_2.order.add_edge(Demand_Forecast, Courier_Match)
step1_2.order.add_edge(Courier_Match, Credential_Check)
step1_2.order.add_edge(Credential_Check, Route_Design)

# Step 3: after Route Design comes Load Assign; Traffic Scan and Package Secure are concurrent but both depend on Load Assign
# Actually Traffic Scan and Package Secure both depend on Load Assign, but are concurrent to each other
step3 = StrictPartialOrder(nodes=[Load_Assign, Traffic_Scan, Package_Secure])
step3.order.add_edge(Load_Assign, Traffic_Scan)
step3.order.add_edge(Load_Assign, Package_Secure)

# Step 4: Dispatch Alert after step3 finishes
step4 = Dispatch_Alert

# Step 5: Real-time Track and Incentive Issue concurrent; Incentive Issue leads to Ledger Update
step5_conc = StrictPartialOrder(nodes=[Real_time_Track, Incentive_Issue, Ledger_Update])
step5_conc.order.add_edge(Incentive_Issue, Ledger_Update)

# Step 6: Dispute Review XOR Customer Notify after Dispatch Alert
step6_choice = OperatorPOWL(operator=Operator.XOR, children=[Dispute_Review, Customer_Notify])

# Step 7: Feedback Collect and Performance Log concurrent after step6_choice
step7 = StrictPartialOrder(nodes=[Feedback_Collect, Performance_Log])

# Step 8: Hub Sync runs concurrently with Ledger Update always (concurrently in background, model by putting Hub Sync and Ledger_Update in same PO with no order between them)
# Since Ledger_Update appears in step5_conc and step8, we integrate Hub_Sync there without ordering between them.
# For clarity and to avoid duplication of Ledger_Update node, include Hub_Sync in step5_conc nodes, no extra edges.
step5_with_hub = StrictPartialOrder(nodes=[Real_time_Track, Incentive_Issue, Ledger_Update, Hub_Sync])
step5_with_hub.order.add_edge(Incentive_Issue, Ledger_Update)

# Compose all steps in a partial order reflecting the overall ordering:

root = StrictPartialOrder(
    nodes=[
        step1_2,
        step3,
        step4,
        step5_with_hub,
        step6_choice,
        step7
    ]
)

root.order.add_edge(step1_2, step3)          # After demand forecast etc, do step3
root.order.add_edge(step3, step4)            # After preparations, dispatch alert
root.order.add_edge(step4, step5_with_hub)   # After dispatch, monitor + incentives + ledger + hub sync
root.order.add_edge(step5_with_hub, step6_choice)  # Then Dispute review or Customer notify
root.order.add_edge(step6_choice, step7)     # Finally feedback collect & performance log