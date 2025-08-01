# Generated from: cdccf476-9ee9-4e31-8175-559567c6dcb1.json
# Description: This process details the complex supply chain of artisan cheese production, starting from sourcing rare milk varieties from remote farms, followed by precise curdling and aging in controlled environments. It involves quality validation through microbial testing, packaging with environmentally sustainable materials, managing inventory under strict temperature controls, coordinating logistics with specialized carriers, and finally ensuring traceability through blockchain records. The process also includes customer feedback loops to adjust future batches and compliance audits to meet international food safety standards, emphasizing both tradition and innovation in food craftsmanship.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
ms = Transition(label='Milk Sourcing')
cf = Transition(label='Curd Formation')
mt = Transition(label='Microbial Test')
wr = Transition(label='Whey Removal')
pc = Transition(label='Pressing Cheese')
sa = Transition(label='Salt Application')
ac = Transition(label='Aging Control')
qc = Transition(label='Quality Check')
ep = Transition(label='Eco Packaging')
il = Transition(label='Inventory Log')
tm = Transition(label='Temp Monitoring')
cb = Transition(label='Carrier Booking')
tr = Transition(label='Trace Recording')
fr = Transition(label='Feedback Review')
ca = Transition(label='Compliance Audit')
ba = Transition(label='Batch Adjustment')

# Core supply‐chain sequence
core = StrictPartialOrder(nodes=[ms, cf, wr, pc, sa, ac, mt, qc, ep, il, tm, cb, tr, ca])
core.order.add_edge(ms, cf)
core.order.add_edge(cf, wr)
core.order.add_edge(wr, pc)
core.order.add_edge(pc, sa)
core.order.add_edge(sa, ac)
core.order.add_edge(ac, mt)
core.order.add_edge(mt, qc)
core.order.add_edge(qc, ep)
core.order.add_edge(ep, il)
core.order.add_edge(ep, tm)
core.order.add_edge(il, cb)
core.order.add_edge(tm, cb)
core.order.add_edge(cb, tr)
core.order.add_edge(tr, ca)

# Feedback + batch‐adjustment loop body
fb = StrictPartialOrder(nodes=[fr, ba])
fb.order.add_edge(fr, ba)

# Loop: run core once, then either exit or do feedback+adjust and rerun core, etc.
root = OperatorPOWL(operator=Operator.LOOP, children=[core, fb])