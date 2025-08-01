# Generated from: ccdbefad-10dd-4877-a709-0f47d3f9ca54.json
# Description: This process outlines the unconventional supply chain management for a handcrafted artisan goods company that integrates local sourcing, community collaboration, and sustainable packaging. The process begins with raw material scouting in niche markets, followed by artisan vetting and skill validation. Production scheduling is highly flexible to accommodate custom orders and seasonal availability. Quality control extends beyond product inspection to include social impact assessments. Logistics involve multi-modal transport with eco-friendly carriers and dynamic routing to reduce carbon footprint. Customer feedback loops are incorporated early and continuously to refine craftsmanship and material selection. The process concludes with adaptive inventory management that balances scarcity with demand, and a community-driven marketing strategy emphasizing storytelling and heritage preservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
ms   = Transition(label="Material Scout")
sv   = Transition(label="Supplier Vetting")
sa   = Transition(label="Skill Audit")
of   = Transition(label="Order Forecast")
cs   = Transition(label="Custom Scheduling")
pi   = Transition(label="Product Inspect")
ir   = Transition(label="Impact Review")
ep   = Transition(label="Eco Packaging")
mt   = Transition(label="Multi Transport")
ro   = Transition(label="Route Optimize")
fl   = Transition(label="Feedback Loop")
cr   = Transition(label="Craft Refine")
ib   = Transition(label="Inventory Balance")
da   = Transition(label="Demand Adjust")
sm   = Transition(label="Story Marketing")
hs   = Transition(label="Heritage Share")
csync = Transition(label="Community Sync")

# Build a loop for the continuous feedback/refinement
# LOOP(children=[A, B]) means: do A, then zero or more times do (B then A), then exit
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[fl, cr])

# Assemble all nodes into one partial‐order model
root = StrictPartialOrder(nodes=[
    ms, sv, sa,
    of, cs,
    pi, ir,
    ep, mt, ro,
    ib, da,
    sm, hs,
    csync,
    feedback_loop
])

# Define the main process sequence
root.order.add_edge(ms, sv)
root.order.add_edge(sv, sa)

root.order.add_edge(sa, of)
root.order.add_edge(of, cs)
root.order.add_edge(cs, pi)
root.order.add_edge(pi, ir)

root.order.add_edge(ir, ep)
root.order.add_edge(ep, mt)
root.order.add_edge(mt, ro)

root.order.add_edge(ro, ib)
root.order.add_edge(ib, da)

root.order.add_edge(da, sm)
root.order.add_edge(da, hs)

root.order.add_edge(sm, csync)
root.order.add_edge(hs, csync)

# Connect the feedback/refinement loop so it starts after Skill Audit
# and runs in parallel (concurrently) with the rest of the flow
root.order.add_edge(sa, feedback_loop)