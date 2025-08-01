# Generated from: d14ba506-0d58-4af4-be6b-354e7d87b3f7.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed commercial building. It begins with site analysis and structural assessment, followed by modular rack installation for crops. Integrated hydroponic and aeroponic systems are then calibrated to optimize water and nutrient delivery. Environmental controls including LED lighting, temperature, and humidity sensors are programmed for crop-specific growth cycles. The process also includes waste recycling loops for organic matter and water reuse. Staff training on system maintenance and crop monitoring is conducted before initiating a test grow phase. Finally, continuous data analytics are implemented to refine yields and operational efficiency, ensuring sustainability and profitability in an urban agricultural setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
sa  = Transition(label='Site Analysis')
sc  = Transition(label='Structural Check')
ri  = Transition(label='Rack Install')
ss  = Transition(label='System Setup')
hc  = Transition(label='Hydroponics Config')
at  = Transition(label='Aeroponics Tune')
ls  = Transition(label='Lighting Setup')
ec  = Transition(label='Enviro Control')
sd  = Transition(label='Sensor Deploy')
wr  = Transition(label='Waste Recycle')
wru = Transition(label='Water Reuse')
st  = Transition(label='Staff Training')
tg  = Transition(label='Test Grow')
da  = Transition(label='Data Analytics')
yo  = Transition(label='Yield Optimize')

# Define the waste‐recycling loop: do Waste Recycle, then either exit or do Water Reuse and loop again
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[wr, wru])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    sa, sc, ri, ss,
    hc, at,
    ls, ec, sd,
    waste_loop,
    st, tg, da, yo
])

# Add precedence relations
root.order.add_edge(sa, sc)
root.order.add_edge(sc, ri)
root.order.add_edge(ri, ss)

# After system setup, calibrate hydroponics and aeroponics in parallel
root.order.add_edge(ss, hc)
root.order.add_edge(ss, at)

# After calibration, program environmental controls in parallel
root.order.add_edge(hc, ls)
root.order.add_edge(at, ls)
root.order.add_edge(hc, ec)
root.order.add_edge(at, ec)
root.order.add_edge(hc, sd)
root.order.add_edge(at, sd)

# All environmental tasks complete before entering the waste‐recycling loop
root.order.add_edge(ls, waste_loop)
root.order.add_edge(ec, waste_loop)
root.order.add_edge(sd, waste_loop)

# After the loop, train staff, then test grow, then analytics, then yield optimization
root.order.add_edge(waste_loop, st)
root.order.add_edge(st, tg)
root.order.add_edge(tg, da)
root.order.add_edge(da, yo)