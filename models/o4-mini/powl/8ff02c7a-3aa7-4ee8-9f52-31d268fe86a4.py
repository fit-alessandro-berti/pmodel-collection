# Generated from: 8ff02c7a-3aa7-4ee8-9f52-31d268fe86a4.json
# Description: This process outlines the integration of vertical farming systems within urban infrastructure to optimize food production, resource management, and sustainability. It involves site analysis, modular farm design, environmental control calibration, automated nutrient delivery, energy optimization, crop monitoring via IoT sensors, pest detection through AI image recognition, data-driven yield forecasting, community engagement initiatives, compliance checks with municipal regulations, waste recycling protocols, dynamic lighting adjustment, supply chain synchronization, urban market distribution planning, and continuous system upgrades to adapt to evolving urban needs and technology advancements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
sa = Transition(label='Site Analysis')
fd = Transition(label='Farm Design')
env = Transition(label='Env Calibration')
nd = Transition(label='Nutrient Delivery')
eo = Transition(label='Energy Optimization')
la = Transition(label='Lighting Adjust')
cm = Transition(label='Crop Monitoring')
pd = Transition(label='Pest Detection')
yf = Transition(label='Yield Forecasting')
co = Transition(label='Community Outreach')
cc = Transition(label='Compliance Check')
wr = Transition(label='Waste Recycling')
ss = Transition(label='Supply Sync')
mp = Transition(label='Market Planning')
su = Transition(label='System Upgrade')

# Build the main workflow (A)
A = StrictPartialOrder(nodes=[
    sa, fd, env,
    nd, eo, la,
    cm, pd, yf,
    co, cc, wr,
    ss, mp
])

# Site analysis and design
A.order.add_edge(sa, fd)
A.order.add_edge(fd, env)

# After calibration: resource-management tasks
A.order.add_edge(env, nd)
A.order.add_edge(env, eo)
A.order.add_edge(env, la)

# Monitoring and forecasting branch
A.order.add_edge(env, cm)
A.order.add_edge(cm, pd)
A.order.add_edge(pd, yf)

# From forecasting to supply & planning
A.order.add_edge(yf, ss)
A.order.add_edge(ss, mp)

# Compliance before market planning
A.order.add_edge(cc, mp)

# Community outreach & waste recycling are concurrent with others:
# (no extra edges needed for co, wr)

# Wrap in a loop to model continuous system upgrades
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[A, su]
)