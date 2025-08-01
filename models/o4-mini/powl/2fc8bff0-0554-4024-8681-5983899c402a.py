# Generated from: 2fc8bff0-0554-4024-8681-5983899c402a.json
# Description: This process outlines the complex operations involved in managing an urban vertical farm, integrating advanced hydroponics, AI-driven environmental controls, and community engagement. Activities include seed selection based on seasonal data, nutrient formula adjustments, automated lighting calibration, pest monitoring through drone surveillance, real-time growth analytics, waste recycling, and crop harvesting. Post-harvest steps involve quality grading, packaging with sustainable materials, distribution logistics tailored to minimize carbon footprint, and feedback collection from local customers. The cycle emphasizes sustainability, technology integration, and urban food security, requiring coordination between agronomists, engineers, and marketing teams to optimize yield and community impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ss = Transition(label='Seed Select')
nm = Transition(label='Nutrient Mix')
wc = Transition(label='Water Calibrate')
la = Transition(label='Light Adjust')
ds = Transition(label='Drone Scan')
pd = Transition(label='Pest Detect')
gt = Transition(label='Growth Track')
wp = Transition(label='Waste Process')
hc = Transition(label='Harvest Crop')
qg = Transition(label='Quality Grade')
pg = Transition(label='Package Goods')
rp = Transition(label='Route Plan')
dd = Transition(label='Delivery Dispatch')
cs = Transition(label='Customer Survey')
fa = Transition(label='Feedback Analyze')
su = Transition(label='System Update')

# Build the pest‐monitoring loop: Drone Scan -> Pest Detect
monitor_body = StrictPartialOrder(nodes=[ds, pd])
monitor_body.order.add_edge(ds, pd)
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_body, monitor_body])

# Build the main process body
body = StrictPartialOrder(
    nodes=[ss, nm, wc, la, monitor_loop, gt, wp, hc, qg, pg, rp, dd, cs, fa, su]
)
body.order.add_edge(ss, nm)
body.order.add_edge(nm, wc)
body.order.add_edge(wc, la)
body.order.add_edge(la, monitor_loop)
body.order.add_edge(monitor_loop, gt)
body.order.add_edge(monitor_loop, hc)
body.order.add_edge(gt, hc)
body.order.add_edge(hc, qg)
body.order.add_edge(qg, pg)
body.order.add_edge(pg, rp)
body.order.add_edge(rp, dd)
body.order.add_edge(dd, cs)
body.order.add_edge(cs, fa)
body.order.add_edge(fa, su)

# Wrap the entire cycle in a LOOP operator
root = OperatorPOWL(operator=Operator.LOOP, children=[body, body])