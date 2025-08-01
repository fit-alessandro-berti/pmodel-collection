# Generated from: b15c4c9f-2dbd-4a44-ab53-2cbffe646493.json
# Description: This process manages the end-to-end supply chain for handcrafted artisan goods, integrating unpredictable raw material sourcing from remote locations, specialized artisan scheduling, quality validation by expert panels, and bespoke packaging options. It includes dynamic demand forecasting based on cultural trends, adaptive logistics for fragile items, and collaborative marketing with local communities to preserve authenticity while scaling distribution globally. The process ensures traceability of materials, artisan skill certification, and sustainable practices compliance, creating a unique blend of traditional craftsmanship and modern supply chain management that supports niche markets and ethical consumerism.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
sm = Transition(label='Source Materials')
vo = Transition(label='Verify Origins')
mt = Transition(label='Material Trace')
sa = Transition(label='Schedule Artisans')
cs = Transition(label='Certify Skills')
ao = Transition(label='Assign Orders')
ci = Transition(label='Craft Items')
qr = Transition(label='Quality Review')
pa = Transition(label='Panel Approval')
pc = Transition(label='Package Custom')
pl = Transition(label='Plan Logistics')
as2 = Transition(label='Arrange Shipping')
td = Transition(label='Track Deliveries')
cf = Transition(label='Collect Feedback')
uf = Transition(label='Update Forecast')
ec = Transition(label='Engage Communities')
sc = Transition(label='Sustainability Audit')
mc = Transition(label='Market Collaborate')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for raw material sourcing retries: Source Materials -> Verify Origins
raw_body = StrictPartialOrder(nodes=[sm, vo])
raw_body.order.add_edge(sm, vo)
raw_loop = OperatorPOWL(operator=Operator.LOOP, children=[raw_body, skip])

# Loop for continuous feedback & forecast updating: Collect Feedback -> Update Forecast
forecast_body = StrictPartialOrder(nodes=[cf, uf])
forecast_body.order.add_edge(cf, uf)
forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[forecast_body, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    raw_loop,    # dynamic sourcing retries
    mt,          # traceability
    sa, cs, ao, ci,  # artisan scheduling & crafting
    qr, pa,     # quality review & panel approval
    pc,         # bespoke packaging
    pl, as2, td,  # logistics, shipping, tracking
    forecast_loop,  # dynamic demand forecasting loop
    ec, mc, sc     # community engagement, marketing, sustainability audit
])

# Define the control-flow dependencies
root.order.add_edge(raw_loop, mt)
root.order.add_edge(mt, sa)
root.order.add_edge(sa, cs)
root.order.add_edge(cs, ao)
root.order.add_edge(ao, ci)
root.order.add_edge(ci, qr)
root.order.add_edge(qr, pa)
root.order.add_edge(pa, pc)
root.order.add_edge(pc, pl)
root.order.add_edge(pl, as2)
root.order.add_edge(as2, td)
root.order.add_edge(td, forecast_loop)
# After forecasting loop, branch out concurrently
root.order.add_edge(forecast_loop, ec)
root.order.add_edge(forecast_loop, mc)
root.order.add_edge(forecast_loop, sc)