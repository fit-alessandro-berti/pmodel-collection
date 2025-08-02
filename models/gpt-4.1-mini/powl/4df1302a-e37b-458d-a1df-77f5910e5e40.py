# Generated from: 4df1302a-e37b-458d-a1df-77f5910e5e40.json
# Description: This process manages the unique supply chain of handcrafted artisan goods, integrating rare raw material sourcing from remote locations, quality validation by expert artisans, adaptive production scheduling based on seasonal demand, bespoke packaging design, and direct-to-consumer personalized delivery. It includes real-time cultural trend analysis to adjust product lines, collaborative artisan feedback loops, and sustainability assessments ensuring ethical sourcing and minimal environmental impact, all coordinated through decentralized digital ledgers for transparency and trust among stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
isyn = Transition(label='Inventory Sync')
sp = Transition(label='Shipment Prep')
ds = Transition(label='Delivery Schedule')
lu = Transition(label='Ledger Update')

# Collaborative artisan feedback loop modeled as a loop:
# Loop node executes (Customer Feedback) and (Artisan Review) repeatedly until exit.
feedback = OperatorPOWL(operator=Operator.LOOP, children=[cf, ar])

# The main partial order reflecting the sequence and partial concurrency:
# Material Sourcing -> Quality Check -> (Trend Analysis and Demand Forecast in parallel)
# Both Trend Analysis and Demand Forecast precede Production Plan
# Production Plan -> Prototype Build -> Sustainability Audit
# Prototype Build also precedes Packaging Design
# Sustainability Audit precedes Packaging Design, which precedes Order Custom
# Order Custom -> Inventory Sync -> Shipment Prep -> Delivery Schedule -> Ledger Update
# The Feedback loop is integrated after Production Plan and before Packaging Design, 
# so Production Plan --> feedback --> Packaging Design

# Construct the partial order nodes list
nodes = [
    ms, qc,
    # Trend Analysis and Demand Forecast are concurrent
    ta, df,
    pp,
    pb,
    sa,
    feedback,
    pd,
    oc, isyn, sp, ds, lu
]

root = StrictPartialOrder(nodes=nodes)

# Add control-flow edges:
root.order.add_edge(ms, qc)

# qc precedes ta and df concurrently
root.order.add_edge(qc, ta)
root.order.add_edge(qc, df)

# Both ta and df precede pp
root.order.add_edge(ta, pp)
root.order.add_edge(df, pp)

# pp precedes pb and feedback loop
root.order.add_edge(pp, pb)
root.order.add_edge(pp, feedback)

# pb precedes sa and pd (pd also after feedback)
root.order.add_edge(pb, sa)

root.order.add_edge(pb, pd)

# feedback precedes pd
root.order.add_edge(feedback, pd)

# sa precedes pd
root.order.add_edge(sa, pd)

# pd precedes oc
root.order.add_edge(pd, oc)

root.order.add_edge(oc, isyn)
root.order.add_edge(isyn, sp)
root.order.add_edge(sp, ds)
root.order.add_edge(ds, lu)