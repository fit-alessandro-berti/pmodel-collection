# Generated from: 4df1302a-e37b-458d-a1df-77f5910e5e40.json
# Description: This process manages the unique supply chain of handcrafted artisan goods, integrating rare raw material sourcing from remote locations, quality validation by expert artisans, adaptive production scheduling based on seasonal demand, bespoke packaging design, and direct-to-consumer personalized delivery. It includes real-time cultural trend analysis to adjust product lines, collaborative artisan feedback loops, and sustainability assessments ensuring ethical sourcing and minimal environmental impact, all coordinated through decentralized digital ledgers for transparency and trust among stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Material Sourcing')
qc = Transition(label='Quality Check')
ta = Transition(label='Trend Analysis')
df = Transition(label='Demand Forecast')
pp = Transition(label='Production Plan')
ar = Transition(label='Artisan Review')
pb = Transition(label='Prototype Build')
cf = Transition(label='Customer Feedback')
pd = Transition(label='Packaging Design')
sa = Transition(label='Sustainability Audit')
oc = Transition(label='Order Custom')
isync = Transition(label='Inventory Sync')
sp = Transition(label='Shipment Prep')
ds = Transition(label='Delivery Schedule')
lu = Transition(label='Ledger Update')

# Feedback loop: Prototype Build -> (Artisan Review -> Customer Feedback) repeating
feedback_cycle = StrictPartialOrder(nodes=[ar, cf])
feedback_cycle.order.add_edge(ar, cf)
loop = OperatorPOWL(operator=Operator.LOOP, children=[pb, feedback_cycle])

# Root partial order
root = StrictPartialOrder(
    nodes=[ms, qc, ta, df, pp, loop, pd, sa, oc, isync, sp, ds, lu]
)

# Add ordering relations
root.order.add_edge(ms, qc)
root.order.add_edge(qc, ta)
root.order.add_edge(qc, df)
root.order.add_edge(ta, pp)
root.order.add_edge(df, pp)
root.order.add_edge(pp, loop)
root.order.add_edge(loop, pd)
root.order.add_edge(loop, sa)
root.order.add_edge(pd, oc)
root.order.add_edge(sa, oc)
root.order.add_edge(oc, isync)
root.order.add_edge(isync, sp)
root.order.add_edge(isync, ds)
root.order.add_edge(isync, lu)