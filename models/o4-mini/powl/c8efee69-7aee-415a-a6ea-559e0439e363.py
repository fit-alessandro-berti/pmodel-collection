# Generated from: c8efee69-7aee-415a-a6ea-559e0439e363.json
# Description: This process manages the complete lifecycle of producing and distributing artisan cheese from small-scale farms to niche gourmet retailers. It includes raw milk sourcing, quality testing, artisan fermentation, aging control, packaging customization, and cold-chain logistics. The workflow ensures traceability, compliance with regional food safety laws, and adaptive inventory management based on seasonal production variations. Additionally, it integrates direct consumer feedback loops through digital platforms to adjust future batches and marketing strategies, while coordinating limited batch releases and specialty event planning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
ms  = Transition(label='Milk Sourcing')
qt  = Transition(label='Quality Testing')
sp  = Transition(label='Starter Prep')
cc  = Transition(label='Curd Cutting')
mc  = Transition(label='Molding Cheese')
salt= Transition(label='Salting Process')
ac  = Transition(label='Aging Control')
hc  = Transition(label='Humidity Check')
pd  = Transition(label='Packaging Design')
lp  = Transition(label='Label Printing')
ia  = Transition(label='Inventory Audit')
op  = Transition(label='Order Processing')
plan= Transition(label='Logistics Planning')
cs  = Transition(label='Cold Storage')
rd  = Transition(label='Retail Delivery')
ec  = Transition(label='Event Coordination')
cf  = Transition(label='Consumer Feedback')
ba  = Transition(label='Batch Adjustment')

# Core production + distribution partial order (one batch)
A = StrictPartialOrder(nodes=[
    ms, qt, sp, cc, mc, salt, ac, hc,
    pd, lp, ia, op, plan, cs, rd, ec
])
A.order.add_edge(ms,  qt)
A.order.add_edge(qt,  sp)
A.order.add_edge(sp,  cc)
A.order.add_edge(cc,  mc)
A.order.add_edge(mc,  salt)
A.order.add_edge(salt,ac)
A.order.add_edge(ac,  hc)
A.order.add_edge(hc,  pd)
A.order.add_edge(pd,  lp)
A.order.add_edge(lp,  ia)
A.order.add_edge(ia,  op)
A.order.add_edge(op,  plan)
# after planning, cold‐chain (then retail) and event coordination happen in parallel
A.order.add_edge(plan, cs)
A.order.add_edge(cs,   rd)
A.order.add_edge(plan, ec)

# Feedback loop partial order
B = StrictPartialOrder(nodes=[cf, ba])
B.order.add_edge(cf, ba)

# Loop: produce one batch (A), then either exit or take feedback path B and repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])