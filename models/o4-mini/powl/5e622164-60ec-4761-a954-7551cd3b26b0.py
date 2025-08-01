# Generated from: 5e622164-60ec-4761-a954-7551cd3b26b0.json
# Description: This process outlines the intricate coordination required in an artisan supply chain, where handcrafted goods are sourced, produced, and distributed with a focus on sustainability and cultural heritage. It involves raw material scouting in remote areas, quality validation by experts, adaptive production scheduling based on artisan availability, and bespoke packaging design. The process also integrates community feedback loops, dynamic pricing adjustments influenced by market trends, and specialized logistics management to ensure fragile items reach niche markets globally while maintaining ethical standards and minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Material Scout')
st = Transition(label='Sample Test')
am = Transition(label='Artisan Match')
sp = Transition(label='Schedule Plan')
ts = Transition(label='Tool Setup')
cp = Transition(label='Craft Produce')
qc = Transition(label='Quality Check')
fc = Transition(label='Feedback Collect')
mr = Transition(label='Market Review')
pa = Transition(label='Price Adjust')
pd = Transition(label='Package Design')
el = Transition(label='Eco Labeling')
oc = Transition(label='Order Confirm')
lp = Transition(label='Logistics Plan')
ship = Transition(label='Shipment Track')
ia = Transition(label='Inventory Audit')
ce = Transition(label='Community Engage')

# Initial scouting and validation sequence
initial_seq = StrictPartialOrder(nodes=[ms, st, am])
initial_seq.order.add_edge(ms, st)
initial_seq.order.add_edge(st, am)

# Production and quality loop: plan, setup, produce, check, then optionally collect feedback and repeat
prod_seq = StrictPartialOrder(nodes=[sp, ts, cp, qc])
prod_seq.order.add_edge(sp, ts)
prod_seq.order.add_edge(ts, cp)
prod_seq.order.add_edge(cp, qc)
prod_loop = OperatorPOWL(operator=Operator.LOOP, children=[prod_seq, fc])

# Dynamic pricing loop based on market review
price_seq = StrictPartialOrder(nodes=[mr, pa])
price_seq.order.add_edge(mr, pa)
price_loop = OperatorPOWL(operator=Operator.LOOP, children=[price_seq, SilentTransition()])

# Packaging and labeling sequence
pack_seq = StrictPartialOrder(nodes=[pd, el])
pack_seq.order.add_edge(pd, el)

# Order confirmation and shipment sequence
order_flow = StrictPartialOrder(nodes=[oc, lp, ship])
order_flow.order.add_edge(oc, lp)
order_flow.order.add_edge(lp, ship)

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[initial_seq, prod_loop, price_loop, pack_seq, order_flow, ia, ce])
root.order.add_edge(initial_seq, prod_loop)
root.order.add_edge(prod_loop, pack_seq)
root.order.add_edge(pack_seq, order_flow)
root.order.add_edge(price_loop, order_flow)
root.order.add_edge(order_flow, ia)
root.order.add_edge(order_flow, ce)