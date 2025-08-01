# Generated from: ebff34d5-e38a-4e94-8130-f6820132347f.json
# Description: This process details the unique supply chain of artisanal cheese production, starting from milk sourcing at micro-dairies, through specialized fermentation and aging techniques, to boutique packaging and direct delivery to niche markets. It involves quality checks at multiple stages, seasonal adjustments based on milk composition, and collaboration with local farmers and artisans to maintain traditional methods while ensuring compliance with food safety standards. The process culminates in personalized customer engagement and feedback integration to refine future batches and expand product varieties sustainably.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
sc = Transition(label='Starter Culture')
mp = Transition(label='Milk Pasteurize')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Draining')
pc = Transition(label='Pressing Cheese')
ss = Transition(label='Salting Stage')
fm = Transition(label='Fermentation')
ac = Transition(label='Aging Control')
ft = Transition(label='Flavor Tasting')
pa = Transition(label='Packaging Artisanal')
lp = Transition(label='Label Printing')
op = Transition(label='Order Processing')
dd = Transition(label='Direct Delivery')
cf = Transition(label='Customer Feedback')

# Build the main production sequence as a strict partial order
production = StrictPartialOrder(nodes=[
    ms, qt, sc, mp, cc, wd, pc, ss, fm, ac, ft, pa, lp, op, dd
])
production.order.add_edge(ms, qt)
production.order.add_edge(qt, sc)
production.order.add_edge(sc, mp)
production.order.add_edge(mp, cc)
production.order.add_edge(cc, wd)
production.order.add_edge(wd, pc)
production.order.add_edge(pc, ss)
production.order.add_edge(ss, fm)
production.order.add_edge(fm, ac)
production.order.add_edge(ac, ft)
production.order.add_edge(ft, pa)
production.order.add_edge(pa, lp)
production.order.add_edge(lp, op)
production.order.add_edge(op, dd)

# Wrap the production in a loop with customer feedback integration
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[production, cf]
)