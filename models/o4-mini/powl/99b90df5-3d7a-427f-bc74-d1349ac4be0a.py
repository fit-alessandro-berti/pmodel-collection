# Generated from: 99b90df5-3d7a-427f-bc74-d1349ac4be0a.json
# Description: This process involves sourcing rare, handcrafted materials from remote artisans across multiple continents, verifying authenticity through blockchain certification, coordinating bespoke production schedules, managing fluctuating artisan availability, and ensuring timely delivery to niche luxury boutiques. The workflow integrates cultural considerations, sustainable practices, dynamic pricing negotiation, quality assurance audits, and custom packaging design to maintain exclusivity and traceability throughout the supply chain. Customer feedback loops and artisan development programs further enhance product uniqueness and community impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
ms = Transition(label='Material Sourcing')
sc = Transition(label='Sustainability Check')
ac = Transition(label='Authenticity Check')
ba = Transition(label='Blockchain Audit')
ss = Transition(label='Schedule Sync')
al = Transition(label='Artisan Liaison')
pn = Transition(label='Price Negotiation')
ps = Transition(label='Production Setup')
qr = Transition(label='Quality Review')
cp = Transition(label='Custom Packaging')
lp = Transition(label='Logistics Plan')
bd = Transition(label='Boutique Delivery')
iu = Transition(label='Inventory Update')
fa = Transition(label='Feedback Analysis')
cs = Transition(label='Community Support')

# Build a loop for continuous feedback & artisan development:
#   * first do Feedback Analysis,
#   * then either exit or do Community Support then Feedback Analysis again.
loop = OperatorPOWL(operator=Operator.LOOP, children=[fa, cs])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    ms, sc, ac, ba, ss, al, pn, ps, qr, cp, lp, bd, iu, loop
])

# Define the control-flow order
root.order.add_edge(ms, sc)
root.order.add_edge(sc, ac)
root.order.add_edge(ac, ba)
# After blockchain audit, schedule sync and artisan liaison can run in parallel
root.order.add_edge(ba, ss)
root.order.add_edge(ba, al)
# Both feed into price negotiation
root.order.add_edge(ss, pn)
root.order.add_edge(al, pn)
# Then production setup, quality review, custom packaging
root.order.add_edge(pn, ps)
root.order.add_edge(ps, qr)
root.order.add_edge(qr, cp)
# Logistics planning and delivery
root.order.add_edge(cp, lp)
root.order.add_edge(lp, bd)
# Inventory update before entering the feedback loop
root.order.add_edge(bd, iu)
root.order.add_edge(iu, loop)