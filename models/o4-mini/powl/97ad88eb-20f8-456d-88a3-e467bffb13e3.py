# Generated from: 97ad88eb-20f8-456d-88a3-e467bffb13e3.json
# Description: This process details the end-to-end supply chain of artisan cheese production, starting from raw milk sourcing from local farms, through specialized fermentation and aging stages in climate-controlled environments. It includes quality inspections, packaging with eco-friendly materials, and coordinating limited batch logistics to boutique retailers and gourmet restaurants. The process also involves seasonal recipe adjustments based on milk composition, direct customer feedback integration for flavor profiling, and regulatory compliance checks to ensure product safety and authenticity. This atypical process highlights the delicate balance between traditional craftsmanship and modern supply chain management in a niche food sector.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
mp = Transition(label='Milk Pasteurize')
sc = Transition(label='Starter Culture')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Drain')
pm_ = Transition(label='Press Mold')
bs = Transition(label='Brine Soak')
ac = Transition(label='Aging Control')
fc = Transition(label='Flavor Check')
ra = Transition(label='Recipe Adjust')
ep = Transition(label='Eco Packaging')
bl = Transition(label='Batch Label')
lp = Transition(label='Logistics Plan')
rd = Transition(label='Retail Delivery')
cr = Transition(label='Customer Review')
ca = Transition(label='Compliance Audit')

# Silent skip for the loop choice
skip = SilentTransition()

# Choice inside the loop: either adjust recipe or skip
choice_ra = OperatorPOWL(operator=Operator.XOR, children=[ra, skip])

# Build the B‐part of the loop: Flavor Check -> (Recipe Adjust ⊕ skip)
B_loop = StrictPartialOrder(nodes=[fc, choice_ra])
B_loop.order.add_edge(fc, choice_ra)

# Loop: do Aging Control, then optionally repeat Flavor Check + choice
loop = OperatorPOWL(operator=Operator.LOOP, children=[ac, B_loop])

# Full process model as a partial order
root = StrictPartialOrder(nodes=[
    ms, qt, mp, sc, cc, wd, pm_, bs,
    loop,
    ep, bl, ca, lp, rd, cr
])

# Define the sequencing (partial order)
root.order.add_edge(ms, qt)
root.order.add_edge(qt, mp)
root.order.add_edge(mp, sc)
root.order.add_edge(sc, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, pm_)
root.order.add_edge(pm_, bs)
root.order.add_edge(bs, loop)
root.order.add_edge(loop, ep)
root.order.add_edge(ep, bl)
root.order.add_edge(bl, ca)
root.order.add_edge(ca, lp)
root.order.add_edge(lp, rd)
root.order.add_edge(rd, cr)