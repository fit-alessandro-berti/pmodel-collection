# Generated from: 2910b74d-5ab6-49d2-b6de-d4599d7ec6a7.json
# Description: This process outlines the intricate steps involved in producing and distributing artisanal cheese from small-scale farms to gourmet retailers. It includes sourcing rare milk varieties, controlled fermentation, manual curdling, delicate aging in microclimates, quality testing, custom packaging, and niche marketing. The process demands precise coordination between farmers, cheesemakers, quality inspectors, and logistics teams to maintain the unique flavor profiles and artisanal qualities. Additionally, it involves seasonal adjustments, compliance with food safety regulations, and direct consumer feedback loops to refine product offerings and maintain exclusivity in a competitive gourmet market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
ms = Transition(label="Milk Sourcing")
mp = Transition(label="Milk Pasteurize")
sc = Transition(label="Starter Culture")
cf = Transition(label="Curd Formation")
cc = Transition(label="Cutting Curd")
wd = Transition(label="Whey Drain")
mc = Transition(label="Molding Cheese")
ss = Transition(label="Salting Stage")
ac = Transition(label="Aging Control")
hc = Transition(label="Humidity Check")
fs = Transition(label="Flavor Sampling")
qt = Transition(label="Quality Testing")
pp = Transition(label="Packaging Prep")
lp = Transition(label="Label Printing")
of = Transition(label="Order Fulfill")
rd = Transition(label="Retail Delivery")
cfb = Transition(label="Customer Feedback")

# Silent transition for optional paths
skip = SilentTransition()

# 1) Production sequence up to salting
production = StrictPartialOrder(nodes=[ms, mp, sc, cf, cc, wd, mc, ss])
production.order.add_edge(ms, mp)
production.order.add_edge(mp, sc)
production.order.add_edge(sc, cf)
production.order.add_edge(cf, cc)
production.order.add_edge(cc, wd)
production.order.add_edge(wd, mc)
production.order.add_edge(mc, ss)

# 2) Aging loop: age, then check humidity & sample flavor, iterate until done
flavor_check = StrictPartialOrder(nodes=[hc, fs])
flavor_check.order.add_edge(hc, fs)
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[ac, flavor_check])

# 3) Packaging choice: sometimes skip label printing if pre-printed
pack_choice = OperatorPOWL(operator=Operator.XOR, children=[lp, skip])
packaging = StrictPartialOrder(nodes=[pp, pack_choice])
packaging.order.add_edge(pp, pack_choice)

# 4) Main root partial order
root = StrictPartialOrder(nodes=[production, aging_loop, qt, packaging, of, rd, cfb])
root.order.add_edge(production, aging_loop)
root.order.add_edge(aging_loop, qt)
root.order.add_edge(qt, packaging)
root.order.add_edge(packaging, of)
root.order.add_edge(of, rd)
root.order.add_edge(rd, cfb)