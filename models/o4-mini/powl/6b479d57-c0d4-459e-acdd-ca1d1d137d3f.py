# Generated from: 6b479d57-c0d4-459e-acdd-ca1d1d137d3f.json
# Description: This process involves dynamically adjusting supply chain operations in response to real-time market fluctuations, supplier disruptions, and customer demand shifts. It integrates predictive analytics, autonomous procurement, and collaborative logistics to minimize delays and costs while maximizing responsiveness. The process requires continuous monitoring, rapid decision-making, and cross-functional coordination between procurement, production, and distribution teams to maintain optimal inventory levels and service quality under uncertain conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# define activities
df = Transition(label='Demand Forecast')
sa = Transition(label='Supplier Audit')
ra = Transition(label='Risk Assess')
inv = Transition(label='Inventory Sync')
op = Transition(label='Order Prioritize')
pa = Transition(label='Procure Auto')
qc = Transition(label='Quality Check')
lp = Transition(label='Logistics Plan')
ro = Transition(label='Route Optimize')
st = Transition(label='Shipment Track')
ea = Transition(label='Exception Alert')
sr = Transition(label='Stock Rebalance')
cn = Transition(label='Customer Notify')
fc = Transition(label='Feedback Capture')
pr = Transition(label='Performance Review')
asg = Transition(label='Adjust Strategy')

# exception handling subprocess
ex = StrictPartialOrder(nodes=[ea, sr])
ex.order.add_edge(ea, sr)

# normal feedback subprocess
fb = StrictPartialOrder(nodes=[cn, fc])
fb.order.add_edge(cn, fc)

# choice between exception handling and normal feedback
xor = OperatorPOWL(operator=Operator.XOR, children=[ex, fb])

# core workflow A: from forecasting through shipment then choice
A = StrictPartialOrder(nodes=[df, sa, ra, inv, op, pa, qc, lp, ro, st, xor])
seq_A = [df, sa, ra, inv, op, pa, qc, lp, ro, st, xor]
for i in range(len(seq_A) - 1):
    A.order.add_edge(seq_A[i], seq_A[i + 1])

# adjustment subprocess B: review and strategy adjustment
B = StrictPartialOrder(nodes=[pr, asg])
B.order.add_edge(pr, asg)

# loop: continuous execution of A with optional B before repeating
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])