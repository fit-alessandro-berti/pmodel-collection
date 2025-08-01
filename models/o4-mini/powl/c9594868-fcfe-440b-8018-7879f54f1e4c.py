# Generated from: c9594868-fcfe-440b-8018-7879f54f1e4c.json
# Description: This process outlines the atypical business workflow for establishing a sustainable urban rooftop farm on commercial buildings. It involves site evaluation, structural assessment, soil and hydroponic system design, regulatory compliance checks, sourcing eco-friendly materials, community engagement, installation, crop selection tailored to urban climate, ongoing monitoring with IoT sensors, pest management using organic methods, harvest scheduling, and finally, direct-to-consumer distribution through local markets and digital platforms, ensuring a closed-loop, environmentally conscious urban agriculture initiative.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ss = Transition(label='Site Survey')
lt = Transition(label='Load Test')
pr = Transition(label='Permit Review')
dl = Transition(label='Design Layout')
ms = Transition(label='Material Sourcing')
cm = Transition(label='Community Meet')
cs = Transition(label='Crop Select')
sp = Transition(label='Soil Prep')
hs = Transition(label='Hydroponic Setup')
si = Transition(label='Sensor Install')
gm = Transition(label='Growth Monitor')
pt = Transition(label='Pest Control')
wt = Transition(label='Water Testing')
hp = Transition(label='Harvest Plan')
ml = Transition(label='Market Launch')
fc = Transition(label='Feedback Collect')

# Build the monitoring loop: zero or more repetitions of concurrent monitoring tasks
skip = SilentTransition()
monitoring_po = StrictPartialOrder(nodes=[gm, pt, wt])
# no ordering edges inside monitoring_po (they run concurrently each cycle)

loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[skip, monitoring_po])

# Assemble the overall partial order
root = StrictPartialOrder(
    nodes=[ss, lt, pr, dl,
           ms, cm, cs,
           sp, hs,
           si, loop_monitor,
           hp, ml, fc]
)

# Define the control-flow dependencies
# 1. Site evaluation and structural assessment
root.order.add_edge(ss, lt)
# 2. Regulatory compliance
root.order.add_edge(lt, pr)
# 3. Design layout
root.order.add_edge(pr, dl)
# 4. After design, sourcing materials and community engagement can run in parallel
root.order.add_edge(dl, ms)
root.order.add_edge(dl, cm)
# 5. Crop selection depends on both materials and community input
root.order.add_edge(ms, cs)
root.order.add_edge(cm, cs)
# 6. Soil preparation and hydroponic setup after crop selection (can be concurrent)
root.order.add_edge(cs, sp)
root.order.add_edge(cs, hs)
# 7. Sensor installation after both preparation streams
root.order.add_edge(sp, si)
root.order.add_edge(hs, si)
# 8. Enter the monitoring loop
root.order.add_edge(si, loop_monitor)
# 9. After monitoring is finished, proceed to harvest planning
root.order.add_edge(loop_monitor, hp)
# 10. Launch to market and collect feedback
root.order.add_edge(hp, ml)
root.order.add_edge(ml, fc)