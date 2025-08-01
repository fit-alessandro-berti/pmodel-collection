# Generated from: b2f8042b-9ed1-4376-9f37-8518d05aef9f.json
# Description: This process involves sourcing small-batch artisan cheeses from regional farms, ensuring quality through sensory evaluation and microbial testing, then coordinating cold-chain logistics to specialty retailers. It includes seasonal inventory adjustments based on production cycles, managing compliance with local food regulations, and fostering relationships with cheesemakers for exclusive varieties. Marketing focuses on storytelling and provenance, while feedback loops from retailers guide product selection and promotional strategies to maximize shelf-life and customer satisfaction in niche markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
fs = Transition(label='Farm Sourcing')
qc = Transition(label='Quality Check')
mt = Transition(label='Microbial Test')
sp = Transition(label='Sample Panel')
ir = Transition(label='Inventory Audit')
of = Transition(label='Order Forecast')
sr = Transition(label='Stock Rotation')
cs = Transition(label='Cold Storage')
lp = Transition(label='Logistics Plan')
rr = Transition(label='Regulation Review')
so = Transition(label='Supplier Meeting')
mc = Transition(label='Marketing Campaign')
st = Transition(label='Sales Training')
ro = Transition(label='Retail Outreach')
sa = Transition(label='Sales Analysis')
fg = Transition(label='Feedback Gather')
cust = Transition(label='Customer Support')

# Seasonal inventory adjustment loop: Audit -> Forecast, then loop with Stock Rotation
inv_seq = StrictPartialOrder(nodes=[ir, of])
inv_seq.order.add_edge(ir, of)
inv_cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[inv_seq, sr])

# Marketing & promotions sequence
marketing_seq = StrictPartialOrder(nodes=[mc, st, ro, sa])
marketing_seq.order.add_edge(mc, st)
marketing_seq.order.add_edge(st, ro)
marketing_seq.order.add_edge(ro, sa)

# Feedback loop around marketing/promotions
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[marketing_seq, fg])

# Top‐level partial order
root = StrictPartialOrder(
    nodes=[
        fs, qc, mt, sp,
        rr, so,
        inv_cycle_loop,
        cs, lp,
        feedback_loop,
        cust
    ]
)

# Define control‐flow edges
root.order.add_edge(fs, qc)
root.order.add_edge(qc, mt)
root.order.add_edge(qc, sp)
root.order.add_edge(mt, rr)
root.order.add_edge(sp, rr)
root.order.add_edge(rr, so)
root.order.add_edge(so, inv_cycle_loop)
root.order.add_edge(inv_cycle_loop, cs)
root.order.add_edge(cs, lp)
root.order.add_edge(lp, feedback_loop)
root.order.add_edge(feedback_loop, cust)