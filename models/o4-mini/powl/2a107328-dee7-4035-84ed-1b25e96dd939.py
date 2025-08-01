# Generated from: 2a107328-dee7-4035-84ed-1b25e96dd939.json
# Description: This process manages the entire supply chain of an urban vertical farming operation, integrating agricultural production, resource optimization, real-time environmental monitoring, crop harvesting, packaging, and distribution to local markets. It involves synchronous coordination between AI-driven climate control, automated nutrient delivery, pest management using bioagents, yield prediction, and dynamic order fulfillment. The process also addresses sustainability goals by recycling water and organic waste, while adapting to fluctuating demand patterns in densely populated urban areas. Each activity ensures minimal resource waste and maximizes freshness and quality through a digitally connected ecosystem of sensors, robots, and logistics partners.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ss    = Transition(label='Seed Selection')
cs    = Transition(label='Climate Setup')
nm    = Transition(label='Nutrient Mix')
wr    = Transition(label='Water Recycling')
pc    = Transition(label='Pest Control')
gm    = Transition(label='Growth Monitoring')
yf    = Transition(label='Yield Forecast')
ah    = Transition(label='Automated Harvest')
csort = Transition(label='Crop Sorting')
pp    = Transition(label='Packaging Prep')
op    = Transition(label='Order Processing')
dr    = Transition(label='Delivery Routing')
wm    = Transition(label='Waste Management')
et    = Transition(label='Energy Tracking')
mf    = Transition(label='Market Feedback')

# Loop for repeated monitoring & forecasting
skip = SilentTransition()
monitor_seq = StrictPartialOrder(nodes=[gm, yf])
monitor_seq.order.add_edge(gm, yf)
loop_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[monitor_seq, skip])

# Build root partial order
root = StrictPartialOrder(
    nodes=[ss, cs, nm, wr, pc, et, wm,
           loop_monitoring, ah, csort, pp, op, dr, mf]
)

# Seed selection precedes all setup/sustainability tasks
for setup in [cs, nm, wr, pc, et, wm]:
    root.order.add_edge(ss, setup)

# After setup, enter monitoring loop
for setup in [cs, nm, wr, pc, et, wm]:
    root.order.add_edge(setup, loop_monitoring)

# After monitoring loop, proceed to harvest and downstream steps
root.order.add_edge(loop_monitoring, ah)
root.order.add_edge(ah, csort)
root.order.add_edge(csort, pp)
root.order.add_edge(pp, op)
root.order.add_edge(op, dr)
root.order.add_edge(dr, mf)