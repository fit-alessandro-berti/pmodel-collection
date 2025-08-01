# Generated from: 965a7e58-5b85-4701-b829-47d75eb60bfe.json
# Description: This process outlines the complex and atypical supply chain involved in producing and distributing artisanal cheeses. It begins with selecting rare milk sources, followed by unique fermentation techniques that require constant environmental adjustments. Quality assessment includes sensory tests alongside lab analysis to ensure flavor profiles meet niche market demands. Packaging is customized per region with biodegradable materials. Distribution involves coordination between local farmers, specialty retailers, and international gourmet markets, incorporating cold chain logistics and real-time tracking. Customer feedback loops influence future batch variations, creating a dynamic production cycle balancing tradition and innovation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
ms = Transition(label='Milk Sourcing')
mt = Transition(label='Milk Testing')
sc = Transition(label='Starter Culture')
mp = Transition(label='Milk Pasteurize')
cf = Transition(label='Curd Formation')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Drain')
mi = Transition(label='Mold Inoculate')
ac = Transition(label='Aging Control')
ft = Transition(label='Flavor Tasting')
la = Transition(label='Lab Analysis')
pd = Transition(label='Packaging Design')
ep = Transition(label='Eco Packaging')
cs = Transition(label='Cold Storage')
lp = Transition(label='Logistics Plan')
rc = Transition(label='Retail Coordination')
fr = Transition(label='Feedback Review')

# Packaging & distribution sequence
pkg_seq = StrictPartialOrder(nodes=[pd, ep, cs, lp, rc])
pkg_seq.order.add_edge(pd, ep)
pkg_seq.order.add_edge(ep, cs)
pkg_seq.order.add_edge(cs, lp)
pkg_seq.order.add_edge(lp, rc)

# Loop: after packaging/distribution, do feedback, then optionally repeat
pack_loop = OperatorPOWL(operator=Operator.LOOP, children=[pkg_seq, fr])

# Root model: from milk sourcing through quality check, then packaging loop
root = StrictPartialOrder(
    nodes=[ms, mt, sc, mp, cf, cc, wd, mi, ac, ft, la, pack_loop]
)
root.order.add_edge(ms, mt)
root.order.add_edge(mt, sc)
root.order.add_edge(sc, mp)
root.order.add_edge(mp, cf)
root.order.add_edge(cf, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mi)
root.order.add_edge(mi, ac)
root.order.add_edge(ac, ft)
root.order.add_edge(ac, la)
root.order.add_edge(ft, pack_loop)
root.order.add_edge(la, pack_loop)