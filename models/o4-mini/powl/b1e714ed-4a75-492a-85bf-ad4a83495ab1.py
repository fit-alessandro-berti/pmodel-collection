# Generated from: b1e714ed-4a75-492a-85bf-ad4a83495ab1.json
# Description: This process involves the comprehensive management of a multi-layer urban vertical farm integrating advanced hydroponics, IoT sensor networks, and AI-driven climate control. It includes seed selection and germination, nutrient solution calibration, pest detection via computer vision, robotic harvesting, and automated packaging. Continuous environmental monitoring adjusts light, humidity, and temperature to optimize crop yield and quality. The process further encompasses waste recycling, energy consumption analysis, real-time supply chain coordination, and dynamic market pricing updates to ensure sustainable and efficient production tailored to urban consumer demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activity transitions
ts = Transition(label='Seed Sowing')
gc = Transition(label='Germination Check')
nm = Transition(label='Nutrient Mix')
sc = Transition(label='Sensor Calibration')
ps = Transition(label='Pest Scan')
ca = Transition(label='Climate Adjust')
wc = Transition(label='Water Circulate')
gm = Transition(label='Growth Monitor')
hr = Transition(label='Harvest Robots')
qi = Transition(label='Quality Inspect')
ws = Transition(label='Waste Sort')
ea = Transition(label='Energy Audit')
pp = Transition(label='Pack Produce')
osync = Transition(label='Order Sync')
pu = Transition(label='Price Update')
dp = Transition(label='Delivery Plan')

# Sub‐process for continuous environmental monitoring
monitor_suite = StrictPartialOrder(nodes=[ca, wc, gm])
monitor_suite.order.add_edge(ca, wc)
monitor_suite.order.add_edge(wc, gm)

env_loop = OperatorPOWL(operator=Operator.LOOP, children=[sc, monitor_suite])

# Sub‐process for dynamic supply‐chain updates
supply_update_suite = StrictPartialOrder(nodes=[pu, dp])
supply_update_suite.order.add_edge(pu, dp)

supply_loop = OperatorPOWL(operator=Operator.LOOP, children=[osync, supply_update_suite])

# Root partial order stitching everything together
root = StrictPartialOrder(
    nodes=[ts, gc, nm, env_loop, ps, hr, qi, ws, ea, pp, supply_loop]
)
root.order.add_edge(ts, gc)
root.order.add_edge(gc, nm)
root.order.add_edge(nm, env_loop)
root.order.add_edge(env_loop, ps)
root.order.add_edge(ps, hr)
root.order.add_edge(hr, qi)
root.order.add_edge(qi, ws)
root.order.add_edge(qi, ea)
root.order.add_edge(ws, pp)
root.order.add_edge(ea, pp)
root.order.add_edge(pp, supply_loop)