# Generated from: f12eafc3-5120-477a-b7ca-1049422757ad.json
# Description: This process outlines the complex and highly specialized steps involved in exporting artisanal cheese from a small-scale farm to international gourmet markets. It begins with milk selection and quality testing, followed by traditional cheese crafting and aging under controlled conditions. The matured cheese then undergoes sensory evaluation and packaging using custom materials to preserve flavor and texture. Regulatory compliance checks for export documentation and customs clearance are conducted before the product is shipped via temperature-controlled logistics. Post-shipment tracking and customer feedback analysis complete the cycle, ensuring continuous improvement and market adaptation for this niche product.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# define the activities
ms = Transition(label="Milk Selection")
qt = Transition(label="Quality Testing")
mp = Transition(label="Milk Pasteurize")
ccr = Transition(label="Cheese Crafting")
ca = Transition(label="Controlled Aging")
sr = Transition(label="Sensory Review")
cp = Transition(label="Custom Packaging")
lp = Transition(label="Label Printing")
el = Transition(label="Export Licensing")
dp = Transition(label="Documentation Prep")
cc = Transition(label="Customs Clearance")
cs = Transition(label="Cold Shipping")
dt = Transition(label="Delivery Tracking")
fr = Transition(label="Feedback Review")
ma = Transition(label="Market Analysis")

# assemble into a partial order
root = StrictPartialOrder(
    nodes=[ms, qt, mp, ccr, ca, sr, cp, lp, el, dp, cc, cs, dt, fr, ma]
)

# core sequence: milk selection -> quality testing -> pasteurize -> crafting -> aging -> sensory review
root.order.add_edge(ms, qt)
root.order.add_edge(qt, mp)
root.order.add_edge(mp, ccr)
root.order.add_edge(ccr, ca)
root.order.add_edge(ca, sr)

# packaging tasks in parallel after sensory review
root.order.add_edge(sr, cp)
root.order.add_edge(sr, lp)

# regulatory checks: export licensing and documentation prep can run in parallel
# both must finish before customs clearance
root.order.add_edge(cp, el)
root.order.add_edge(cp, dp)
root.order.add_edge(lp, el)
root.order.add_edge(lp, dp)
root.order.add_edge(el, cc)
root.order.add_edge(dp, cc)

# shipping and post‐shipment steps
root.order.add_edge(cc, cs)
root.order.add_edge(cs, dt)
root.order.add_edge(dt, fr)
root.order.add_edge(fr, ma)