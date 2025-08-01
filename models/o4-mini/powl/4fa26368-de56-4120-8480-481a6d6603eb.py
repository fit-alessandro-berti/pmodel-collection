# Generated from: 4fa26368-de56-4120-8480-481a6d6603eb.json
# Description: This process involves the intricate steps required to produce, certify, package, and export artisanal cheese from a local farm to international gourmet markets. It begins with careful milk selection and fermentation, followed by quality inspections and aging under controlled conditions. After maturation, the cheese undergoes sensory evaluation and microbiological testing to comply with export regulations. Packaging is done using eco-friendly materials, accompanied by detailed labeling that meets destination country standards. Logistics coordination ensures timely shipment while maintaining cold chain integrity. Finally, customs clearance and distributor onboarding complete the process, enabling the cheese to reach connoisseurs worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
ms  = Transition(label='Milk Selection')
fs  = Transition(label='Fermentation Start')
qc  = Transition(label='Quality Check')
ca  = Transition(label='Cheese Aging')
st  = Transition(label='Sensory Test')
mt  = Transition(label='Microbial Test')
cp  = Transition(label='Certification Prep')
ep  = Transition(label='Eco Packaging')
ld  = Transition(label='Label Design')
la  = Transition(label='Label Approval')
cs  = Transition(label='Cold Storage')
lp  = Transition(label='Logistics Plan')
cf  = Transition(label='Customs Filing')
ds  = Transition(label='Distributor Setup')
sd  = Transition(label='Shipment Dispatch')

# Build partial order
root = StrictPartialOrder(nodes=[ms, fs, qc, ca, st, mt, cp, ep, ld, la, cs, lp, cf, ds, sd])

# Linear flow up to aging
root.order.add_edge(ms, fs)
root.order.add_edge(fs, qc)
root.order.add_edge(qc, ca)

# Parallel tests after aging
root.order.add_edge(ca, st)
root.order.add_edge(ca, mt)

# Both tests must complete before certification prep
root.order.add_edge(st, cp)
root.order.add_edge(mt, cp)

# Certification prep forks into packaging and labeling
root.order.add_edge(cp, ep)
root.order.add_edge(cp, ld)

# Labeling sequence
root.order.add_edge(ld, la)

# Packaging and labeling converge into cold storage
root.order.add_edge(ep, cs)
root.order.add_edge(la, cs)

# Cold storage then logistics planning
root.order.add_edge(cs, lp)

# Logistics planning forks into customs filing and distributor setup
root.order.add_edge(lp, cf)
root.order.add_edge(lp, ds)

# Both must complete before final dispatch
root.order.add_edge(cf, sd)
root.order.add_edge(ds, sd)