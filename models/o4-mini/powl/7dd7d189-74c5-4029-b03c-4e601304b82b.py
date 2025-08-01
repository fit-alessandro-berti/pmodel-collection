# Generated from: 7dd7d189-74c5-4029-b03c-4e601304b82b.json
# Description: This process manages the sourcing, customization, and distribution of rare artisan materials used in bespoke product creation. It involves intricate coordination between local artisans, quality assurance teams, custom order management, and eco-friendly logistics providers. The process ensures traceability from raw material harvest to final delivery, incorporating sustainability checks and dynamic inventory adjustments based on artisan availability and regional demand fluctuations. It also includes a feedback loop with artisans to refine material quality and adapt supply strategies in real-time, balancing tradition with modern efficiency to meet unique customer specifications worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
ms = Transition(label='Material Sourcing')
sv = Transition(label='Supplier Vetting')
qi = Transition(label='Quality Inspect')
sa = Transition(label='Sustainability Audit')
df = Transition(label='Demand Forecast')
sr = Transition(label='Stock Replenish')
ic = Transition(label='Inventory Check')
cd = Transition(label='Custom Design')
ov = Transition(label='Order Validation')
pp = Transition(label='Packaging Prep')
lp = Transition(label='Logistics Planning')
sb = Transition(label='Shipment Book')
cc = Transition(label='Customs Clearance')
dt = Transition(label='Delivery Tracking')
cf = Transition(label='Customer Feedback')
ac = Transition(label='Artisan Coordination')

# 1) Inventory adjustment loop: Forecast -> (optionally) Replenish & Check, repeat until exit
inv_po = StrictPartialOrder(nodes=[sr, ic])
inv_po.order.add_edge(sr, ic)
inventory_loop = OperatorPOWL(operator=Operator.LOOP, children=[df, inv_po])

# 2) Packaging and shipping in parallel
#    shipping sequence: Planning -> Booking -> Customs -> Tracking
shipping_seq = StrictPartialOrder(nodes=[lp, sb, cc, dt])
shipping_seq.order.add_edge(lp, sb)
shipping_seq.order.add_edge(sb, cc)
shipping_seq.order.add_edge(cc, dt)

pack_and_ship = StrictPartialOrder(nodes=[pp, shipping_seq])
# no order edge between pp and shipping_seq => they run in parallel

# 3) Feedback loop with artisans: collect feedback, then optionally coordinate, re-inspect, re-audit, repeat
ac_fb = Transition(label='Artisan Coordination')
qi_fb = Transition(label='Quality Inspect')
sa_fb = Transition(label='Sustainability Audit')
fb_body = StrictPartialOrder(nodes=[ac_fb, qi_fb, sa_fb])
fb_body.order.add_edge(ac_fb, qi_fb)
fb_body.order.add_edge(qi_fb, sa_fb)

feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[cf, fb_body])

# 4) Main process partial order
root = StrictPartialOrder(
    nodes=[ms, sv, qi, sa, inventory_loop, cd, ov, pack_and_ship, feedback_loop]
)
root.order.add_edge(ms, sv)
root.order.add_edge(sv, qi)
root.order.add_edge(qi, sa)
root.order.add_edge(sa, inventory_loop)
root.order.add_edge(inventory_loop, cd)
root.order.add_edge(cd, ov)
root.order.add_edge(ov, pack_and_ship)
root.order.add_edge(pack_and_ship, feedback_loop)