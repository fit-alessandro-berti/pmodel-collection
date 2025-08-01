# Generated from: dee43d2b-459b-4866-b006-fda69289f150.json
# Description: This process outlines the end-to-end management of a vertical urban farm, integrating advanced hydroponics, climate control, and AI-driven crop monitoring to optimize yield in limited city spaces. It involves seed selection, nutrient mixing, environmental adjustments, pest detection, harvest scheduling, and distribution logistics tailored for high-density urban environments. Continuous feedback loops with real-time data ensure sustainability and efficient resource usage, while compliance with urban agricultural regulations is maintained throughout the cycle. The process supports rapid adaptation to changing weather patterns and market demands, promoting local food security and minimizing carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ss = Transition(label="Seed Selection")
nm = Transition(label="Nutrient Mix")
ps = Transition(label="Planting Setup")

cc = Transition(label="Climate Control")
wc = Transition(label="Water Cycling")
gm = Transition(label="Growth Monitoring")
pd = Transition(label="Pest Detection")
la = Transition(label="Light Adjustment")
da = Transition(label="Data Analysis")

hp = Transition(label="Harvest Planning")
ch = Transition(label="Crop Harvest")
ys = Transition(label="Yield Sorting")
pp = Transition(label="Packaging Prep")
dp = Transition(label="Distribution Plan")

rc = Transition(label="Regulation Check")
wr = Transition(label="Waste Recycling")
sm = Transition(label="System Maintenance")

skip = SilentTransition()

# Define the monitoring & adjustment cycle
cycle = StrictPartialOrder(nodes=[cc, wc, gm, pd, la, da])
cycle.order.add_edge(cc, wc)
cycle.order.add_edge(wc, gm)
cycle.order.add_edge(gm, pd)
cycle.order.add_edge(pd, la)
cycle.order.add_edge(la, da)

# Loop: repeat the cycle until exit
loop_cycle = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip])

# Assemble the end-to-end process
root = StrictPartialOrder(nodes=[
    ss, nm, ps,
    loop_cycle, rc,
    hp, ch, ys, pp, dp,
    wr, sm
])

# Control-flow ordering
root.order.add_edge(ss, nm)
root.order.add_edge(nm, ps)

# After setup, start the growth cycle and check regulations in parallel
root.order.add_edge(ps, loop_cycle)
root.order.add_edge(ps, rc)

# Both lead to harvest planning
root.order.add_edge(loop_cycle, hp)
root.order.add_edge(rc, hp)

# Harvest to distribution path
root.order.add_edge(hp, ch)
root.order.add_edge(ch, ys)
root.order.add_edge(ys, pp)
root.order.add_edge(pp, dp)

# Post-distribution cleanup and maintenance
root.order.add_edge(dp, wr)
root.order.add_edge(wr, sm)