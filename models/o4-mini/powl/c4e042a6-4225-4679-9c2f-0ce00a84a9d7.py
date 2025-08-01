# Generated from: c4e042a6-4225-4679-9c2f-0ce00a84a9d7.json
# Description: This process outlines the intricate supply chain management for a bespoke artisan goods company specializing in handcrafted musical instruments. It involves sourcing rare organic materials from remote regions, verifying artisan credentials, coordinating small batch production, managing custom design approvals, and synchronizing global shipping with strict quality inspections. The process integrates real-time artisan feedback loops, adaptive inventory adjustments, and niche marketing strategies to ensure exclusivity while maintaining transparency and sustainability throughout the supply chain lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ms = Transition(label='Material Sourcing')
sa = Transition(label='Supplier Audit')
cv = Transition(label='Credential Verify')
dc = Transition(label='Design Concept')
aa = Transition(label='Artisan Assign')
pb = Transition(label='Prototype Build')
qr = Transition(label='Quality Review')
fl = Transition(label='Feedback Loop')
bs = Transition(label='Batch Scheduling')
ia = Transition(label='Inventory Adjust')
ps = Transition(label='Production Sync')
ca = Transition(label='Custom Approvals')
cc = Transition(label='Compliance Check')
sp = Transition(label='Shipping Plan')
mt = Transition(label='Market Target')
ce = Transition(label='Customer Engage')
of = Transition(label='Order Fulfill')
sust = Transition(label='Sustainability')

# 1) Initial linear sequence: Material Sourcing -> Supplier Audit -> Credential Verify -> Design Concept -> Artisan Assign
PO_init = StrictPartialOrder(nodes=[ms, sa, cv, dc, aa])
PO_init.order.add_edge(ms, sa)
PO_init.order.add_edge(sa, cv)
PO_init.order.add_edge(cv, dc)
PO_init.order.add_edge(dc, aa)

# 2) Prototype/Review loop with artisan feedback
A1 = StrictPartialOrder(nodes=[pb, qr])
A1.order.add_edge(pb, qr)
cycle = OperatorPOWL(operator=Operator.LOOP, children=[A1, fl])

# 3) Production planning: Batch Scheduling & Inventory Adjust in parallel, then Production Sync
PO2 = StrictPartialOrder(nodes=[bs, ia, ps])
PO2.order.add_edge(bs, ps)
PO2.order.add_edge(ia, ps)

# 4) Custom Approvals followed by Compliance Check
PO3 = StrictPartialOrder(nodes=[ca, cc])
PO3.order.add_edge(ca, cc)

# 5) Shipping & marketing activities in parallel, then Order Fulfill
PO4 = StrictPartialOrder(nodes=[sp, mt, ce, of])
PO4.order.add_edge(sp, of)
PO4.order.add_edge(mt, of)
PO4.order.add_edge(ce, of)

# 6) Root combining all phases in sequence, ending with Sustainability
root = StrictPartialOrder(nodes=[PO_init, cycle, PO2, PO3, PO4, sust])
root.order.add_edge(PO_init, cycle)
root.order.add_edge(cycle, PO2)
root.order.add_edge(PO2, PO3)
root.order.add_edge(PO3, PO4)
root.order.add_edge(PO4, sust)