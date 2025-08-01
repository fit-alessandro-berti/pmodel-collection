# Generated from: 07fc5d86-4882-4448-a8f8-31a1179e6a55.json
# Description: This process manages a supply chain that dynamically adapts to real-time market fluctuations, supplier disruptions, and customer demand variability. It incorporates predictive analytics, multi-tier supplier coordination, and automated contingency planning. The workflow includes continuous data ingestion from IoT devices, AI-driven risk assessment, and decentralized decision-making to optimize inventory levels and logistics routes. This atypical approach reduces lead times and enhances resilience by blending human oversight with autonomous adjustments, ensuring seamless operations despite external uncertainties and internal constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
di   = Transition(label='Data Ingestion')
risk = Transition(label='Risk Analysis')
df   = Transition(label='Demand Forecast')
ss   = Transition(label='Supplier Sync')
ia   = Transition(label='Inventory Audit')
cp   = Transition(label='Contingency Plan')
op   = Transition(label='Order Prioritize')
ro   = Transition(label='Route Optimize')
cc   = Transition(label='Capacity Check')
qr   = Transition(label='Quality Review')
st   = Transition(label='Shipment Track')
da   = Transition(label='Disruption Alert')
cu   = Transition(label='Contract Update')
res  = Transition(label='Resource Allocate')
fl   = Transition(label='Feedback Loop')
pr   = Transition(label='Performance Review')

# Silent transition for optional / skip behavior
skip = SilentTransition()

# Loop: after each risk analysis you can either exit or do a contingency plan and repeat
loop_risk = OperatorPOWL(operator=Operator.LOOP, children=[risk, cp])

# Loop for continuous feedback/improvement
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[fl, skip])

# Optional performance review at the end
xor_perf = OperatorPOWL(operator=Operator.XOR, children=[pr, skip])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    di,
    loop_risk,
    df,
    ss,
    ia,
    op,
    ro,
    cc,
    qr,
    st,
    da,
    cu,
    res,
    loop_feedback,
    xor_perf
])

# Define the ordering (-->)
root.order.add_edge(di, loop_risk)
root.order.add_edge(di, df)

root.order.add_edge(loop_risk, ss)
root.order.add_edge(loop_risk, ia)
root.order.add_edge(df, ss)
root.order.add_edge(df, ia)

root.order.add_edge(ss, op)
root.order.add_edge(ia, op)
root.order.add_edge(ss, ro)
root.order.add_edge(ia, ro)

root.order.add_edge(op, cc)
root.order.add_edge(ro, cc)
root.order.add_edge(op, qr)
root.order.add_edge(ro, qr)

root.order.add_edge(cc, st)
root.order.add_edge(qr, st)

# Disruption can trigger a new risk/contingency loop
root.order.add_edge(st, da)
root.order.add_edge(da, loop_risk)

# After either normal shipment or a disruption, update contracts
root.order.add_edge(st, cu)
root.order.add_edge(da, cu)

# Allocate resources, then engage in feedback loop
root.order.add_edge(cu, res)
root.order.add_edge(res, loop_feedback)

# Finally, perform an optional performance review
root.order.add_edge(loop_feedback, xor_perf)