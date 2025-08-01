# Generated from: ca65d08d-90d6-44e4-b9b4-4ff89c24e406.json
# Description: This process outlines the establishment of an urban vertical farming facility designed to optimize limited city space for sustainable food production. It involves site selection within dense urban areas, modular system design, environmental control setup, crop selection based on microclimate data, automated nutrient delivery, and integration of IoT sensors for real-time monitoring. The process also includes staff training on vertical farming techniques, waste recycling protocols, and establishing supply chain links with local markets. The goal is to create a resilient, scalable, and eco-friendly food production system that leverages technology and urban infrastructure to reduce food miles and improve fresh produce availability in metropolitan regions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ss = Transition(label='Site Survey')
dl = Transition(label='Design Layout')
sb = Transition(label='System Build')
isens = Transition(label='Install Sensors')
scrop = Transition(label='Select Crops')
slight = Transition(label='Setup Lighting')
cclim = Transition(label='Configure Climate')
nmix = Transition(label='Nutrient Mix')
aw = Transition(label='Automate Watering')
ts = Transition(label='Test Systems')
tsf = Transition(label='Train Staff')
wp = Transition(label='Waste Plan')
ml = Transition(label='Market Link')
dm1 = Transition(label='Data Monitor')
oy1 = Transition(label='Optimize Yield')
dm2 = Transition(label='Data Monitor')
oy2 = Transition(label='Optimize Yield')

# Build the loop body A (initial) and B (repeat) as simple sequences DM -> OY
A_loop = StrictPartialOrder(nodes=[dm1, oy1])
A_loop.order.add_edge(dm1, oy1)
B_loop = StrictPartialOrder(nodes=[dm2, oy2])
B_loop.order.add_edge(dm2, oy2)

# Loop operator: execute A_loop once, then choose exit or B_loop then A_loop again, etc.
loop = OperatorPOWL(operator=Operator.LOOP, children=[A_loop, B_loop])

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[ss, dl, sb,
           isens, scrop, slight, cclim, nmix, aw,
           ts,
           tsf, wp, ml,
           loop]
)

# Define the control-flow dependencies
# 1) ss -> dl -> sb
root.order.add_edge(ss, dl)
root.order.add_edge(dl, sb)

# 2) After `System Build`, the six setup activities can run in parallel
for prep in [isens, scrop, slight, cclim, nmix, aw]:
    root.order.add_edge(sb, prep)

# 3) All six setups must finish before `Test Systems`
for prep in [isens, scrop, slight, cclim, nmix, aw]:
    root.order.add_edge(prep, ts)

# 4) After testing, run staff training, waste plan, and market link in parallel
root.order.add_edge(ts, tsf)
root.order.add_edge(ts, wp)
root.order.add_edge(ts, ml)

# 5) Only once training, waste plan, and market link are done, enter the monitoring/optimization loop
for n in [tsf, wp, ml]:
    root.order.add_edge(n, loop)