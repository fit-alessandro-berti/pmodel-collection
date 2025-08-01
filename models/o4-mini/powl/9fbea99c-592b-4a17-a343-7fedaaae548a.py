# Generated from: 9fbea99c-592b-4a17-a343-7fedaaae548a.json
# Description: This process involves rapidly restoring disrupted supply chains following unexpected global crises such as natural disasters, geopolitical conflicts, or pandemics. It requires cross-functional coordination to assess damage, identify alternate suppliers, reroute logistics, and ensure compliance with emergency regulations. Continuous risk monitoring and stakeholder communication are crucial to adapt strategies as conditions evolve. The process also incorporates contingency financing, technology deployment for real-time tracking, and post-crisis analysis to strengthen future resilience, making it a complex and dynamic recovery operation atypical in routine supply management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
da = Transition(label='Damage Assess')
rm = Transition(label='Risk Monitor')
sv = Transition(label='Supplier Vet')
asrc = Transition(label='Alternate Source')
cc = Transition(label='Compliance Check')
lr = Transition(label='Logistics Reroute')
ef = Transition(label='Emergency Finance')
ss = Transition(label='Stakeholder Sync')
td = Transition(label='Tech Deploy')
ia = Transition(label='Inventory Audit')
ts = Transition(label='Transport Secure')
ce = Transition(label='Customs Expedite')
df = Transition(label='Demand Forecast')
cp = Transition(label='Communication Plan')
pr = Transition(label='Post-Crisis Review')

# Loop for continuous risk monitoring and stakeholder communication
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[rm, ss])

# Build the partial order
root = StrictPartialOrder(nodes=[da, risk_loop, sv, asrc, cc, lr, ef, td, ia, ts, ce, df, cp, pr])

# After Damage Assess, start all recovery tasks and the monitoring loop in parallel
for nxt in [risk_loop, sv, asrc, cc, lr, ef, td, ia, ts, ce, df, cp]:
    root.order.add_edge(da, nxt)

# All tasks (including the monitoring loop) must complete before Post-Crisis Review
for prev in [risk_loop, sv, asrc, cc, lr, ef, td, ia, ts, ce, df, cp]:
    root.order.add_edge(prev, pr)