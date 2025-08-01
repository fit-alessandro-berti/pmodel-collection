# Generated from: dcc3cfe5-b295-4ee6-b6d9-964565539021.json
# Description: This process involves leveraging a global network of independent couriers and local hubs to dynamically optimize package delivery routes in real-time. It integrates AI-driven demand forecasting with crowdsourced labor allocation, allowing rapid adaptation to fluctuating delivery volumes and traffic conditions. The system continuously collects performance data, validates courier credentials, and manages incentives through a decentralized blockchain ledger. It includes risk assessment for package security, automated dispute resolution, and real-time customer notifications. The process culminates with delivery confirmation and feedback incorporation to improve future operations and enhance overall service reliability and efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
df = Transition(label='Demand Forecast')
cm = Transition(label='Courier Match')
cc = Transition(label='Credential Check')
rd = Transition(label='Route Design')
ts = Transition(label='Traffic Scan')
la = Transition(label='Load Assign')
da = Transition(label='Dispatch Alert')
rt = Transition(label='Real-time Track')
pl = Transition(label='Performance Log')
lu = Transition(label='Ledger Update')
hs = Transition(label='Hub Sync')
ps = Transition(label='Package Secure')
ii = Transition(label='Incentive Issue')
dr = Transition(label='Dispute Review')
cn = Transition(label='Customer Notify')
fc = Transition(label='Feedback Collect')

# Silent transitions for loop exit and optional dispute
skip_loop = SilentTransition()
skip_dispute = SilentTransition()

# Define the body of the continuous operational loop:
#   Route Design -> Traffic Scan -> Load Assign -> Dispatch Alert -> Real-time Track
#   and from Dispatch Alert concurrently to Performance Log, Ledger Update, Hub Sync
loop_body = StrictPartialOrder(nodes=[rd, ts, la, da, rt, pl, lu, hs])
loop_body.order.add_edge(rd, ts)
loop_body.order.add_edge(ts, la)
loop_body.order.add_edge(la, da)
loop_body.order.add_edge(da, rt)
# concurrent logging, ledger update, hub sync after dispatch
loop_body.order.add_edge(da, pl)
loop_body.order.add_edge(da, lu)
loop_body.order.add_edge(da, hs)

# LOOP operator: repeat the operational loop until exit
operational_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, skip_loop])

# XOR for optional dispute resolution
dispute_xor = OperatorPOWL(operator=Operator.XOR, children=[skip_dispute, dr])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    df, cm, cc,                # forecasting and courier pre-check
    operational_loop,          # dynamic routing & tracking loop
    ps,                        # secure package / risk assessment
    dispute_xor,               # optional dispute resolution
    ii, cn, fc                 # incentive issue -> customer notify -> feedback
])

# Define the control-flow edges
root.order.add_edge(df, cm)
root.order.add_edge(cm, cc)
root.order.add_edge(cc, operational_loop)
root.order.add_edge(operational_loop, ps)
root.order.add_edge(ps, dispute_xor)
root.order.add_edge(dispute_xor, ii)
root.order.add_edge(ii, cn)
root.order.add_edge(cn, fc)