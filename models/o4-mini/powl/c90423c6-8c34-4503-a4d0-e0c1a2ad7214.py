# Generated from: c90423c6-8c34-4503-a4d0-e0c1a2ad7214.json
# Description: This process describes the complex journey of sourcing, roasting, packaging, and distributing artisan coffee beans from remote farms to specialty cafes. It includes unique steps such as micro-lot selection, sensory profiling, fermentation control, and direct trade negotiations. The process also involves sustainability audits, custom blend creation, and dynamic pricing models based on seasonal crop yields and market demand fluctuations, ensuring premium quality and traceability throughout the supply chain. Additionally, it incorporates digital inventory synchronization and barista training programs to maintain brand consistency and customer satisfaction across multiple geographic regions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# define activities
fs    = Transition(label='Farm Selection')
tn    = Transition(label='Trade Negotiation')
st    = Transition(label='Sample Testing')
ms    = Transition(label='Micro-Lot Sorting')
fc    = Transition(label='Fermentation Control')
sp    = Transition(label='Sensory Profiling')
rc    = Transition(label='Roast Calibration')
bc    = Transition(label='Blend Creation')
pd    = Transition(label='Packaging Design')
qi    = Transition(label='Quality Inspection')
sa    = Transition(label='Sustainability Audit')
isync = Transition(label='Inventory Sync')
lp    = Transition(label='Logistics Planning')
ct    = Transition(label='Cafe Training')
dp    = Transition(label='Dynamic Pricing')
cf    = Transition(label='Customer Feedback')
tl    = Transition(label='Traceability Logging')

# build partial order
root = StrictPartialOrder(nodes=[
    fs, tn, st, ms, fc, sp, rc, bc, pd, qi, sa,
    isync, lp, ct, dp, cf, tl
])

# farm selection and trade negotiation happen in parallel, then sample testing
root.order.add_edge(fs, st)
root.order.add_edge(tn, st)

# core processing chain
root.order.add_edge(st, ms)
root.order.add_edge(ms, fc)
root.order.add_edge(fc, sp)
root.order.add_edge(sp, rc)
root.order.add_edge(rc, bc)
root.order.add_edge(bc, pd)

# packaging followed by quality inspection and sustainability audit in parallel
root.order.add_edge(pd, qi)
root.order.add_edge(pd, sa)

# after both inspection and audit, synchronize inventory
root.order.add_edge(qi, isync)
root.order.add_edge(sa, isync)

# plan logistics and update dynamic pricing in parallel
root.order.add_edge(isync, lp)
root.order.add_edge(isync, dp)

# then train baristas
root.order.add_edge(lp, ct)
root.order.add_edge(dp, ct)

# collect feedback and log traceability, feedback precedes logging
root.order.add_edge(ct, cf)
root.order.add_edge(ct, tl)
root.order.add_edge(cf, tl)