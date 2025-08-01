# Generated from: cfe9cf78-0585-427c-9169-f11d08cd2a50.json
# Description: This process outlines the end-to-end setup and operational launch of an urban vertical farming facility. It begins with site analysis and environmental assessment, followed by modular system design tailored to urban constraints. Procurement of specialized hydroponic equipment and organic seeds is followed by installation, calibration, and testing of climate control systems. Staff training emphasizes sustainable farming techniques and technology use. Once operational, crop cycles are monitored through IoT sensors, with data analytics optimizing nutrient delivery and light exposure. Regular maintenance and pest management ensure crop health, while direct-to-consumer logistics and marketing strategies complete the process, ensuring fresh produce efficiently reaches urban markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
sa = Transition(label='Site Analysis')
ea = Transition(label='Env Assessment')
sd = Transition(label='System Design')
eo = Transition(label='Equipment Order')
ss = Transition(label='Seed Selection')
im = Transition(label='Install Modules')
cs = Transition(label='Calibrate Systems')
st = Transition(label='Staff Training')
ps = Transition(label='Plant Seeding')
iot = Transition(label='IoT Monitoring')
da = Transition(label='Data Analytics')
na = Transition(label='Nutrient Adjust')
mc = Transition(label='Maintenance Check')
pc = Transition(label='Pest Control')
ml = Transition(label='Market Launch')
ls = Transition(label='Logistics Setup')

# Build the monitoring/maintenance cycle as a partial order
cycle = StrictPartialOrder(nodes=[iot, da, na, mc, pc])
cycle.order.add_edge(iot, da)
cycle.order.add_edge(da, na)
# After adjusting nutrients, maintenance and pest control can occur in parallel
cycle.order.add_edge(na, mc)
cycle.order.add_edge(na, pc)

# Wrap the cycle into a loop (repeat the cycle until exit)
loop_cycle = OperatorPOWL(operator=Operator.LOOP, children=[cycle, cycle])

# Build the top‐level workflow as a partial order
root = StrictPartialOrder(
    nodes=[sa, ea, sd, eo, ss, im, cs, st, ps, loop_cycle, ml, ls]
)
# Sequence: Site Analysis -> Env Assessment -> System Design
root.order.add_edge(sa, ea)
root.order.add_edge(ea, sd)
# After design, equipment order and seed selection can run in parallel
root.order.add_edge(sd, eo)
root.order.add_edge(sd, ss)
# Both procurement tasks must finish before installation
root.order.add_edge(eo, im)
root.order.add_edge(ss, im)
# Then calibrate systems, then staff training, then seeding
root.order.add_edge(im, cs)
root.order.add_edge(cs, st)
root.order.add_edge(st, ps)
# After seeding, enter the monitoring/maintenance loop
root.order.add_edge(ps, loop_cycle)
# Once loop exits, launch market and setup logistics in parallel
root.order.add_edge(loop_cycle, ml)
root.order.add_edge(loop_cycle, ls)