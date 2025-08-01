# Generated from: fb46e5c2-00d3-4d86-bf9c-326d5c813417.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a dense metropolitan area. It begins with site analysis and environmental impact assessment, followed by modular infrastructure design and integration of hydroponic systems. Subsequent activities include climate control calibration, nutrient solution optimization, and automated lighting configuration. The process also covers workforce training on advanced cultivation techniques, pest monitoring with AI drones, and real-time crop health analytics. Finally, it concludes with supply chain synchronization for local distribution and continuous system maintenance planning to ensure sustainable production and minimal ecological footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
sa = Transition(label='Site Analysis')
ir = Transition(label='Impact Review')
md = Transition(label='Modular Design')
si = Transition(label='System Integration')
cs = Transition(label='Climate Setup')
nm = Transition(label='Nutrient Mix')
lc = Transition(label='Light Config')
st = Transition(label='Staff Training')
pm = Transition(label='Pest Monitor')
dd = Transition(label='Drone Deploy')
hs = Transition(label='Health Scan')
dl = Transition(label='Data Logging')
ss = Transition(label='Supply Sync')
mp = Transition(label='Maintenance Plan')
wm = Transition(label='Waste Manage')

# Stage 1: Site Analysis -> Impact Review
stage1 = StrictPartialOrder(nodes=[sa, ir])
stage1.order.add_edge(sa, ir)

# Stage 2: Modular Design -> System Integration
stage2 = StrictPartialOrder(nodes=[md, si])
stage2.order.add_edge(md, si)

# Stage 3: Climate Setup, Nutrient Mix, Light Config (concurrent)
stage3 = StrictPartialOrder(nodes=[cs, nm, lc])
# no edges = fully concurrent

# Stage 4: Staff Training -> Pest Monitor -> Drone Deploy -> Health Scan -> Data Logging
stage4 = StrictPartialOrder(nodes=[st, pm, dd, hs, dl])
stage4.order.add_edge(st, pm)
stage4.order.add_edge(pm, dd)
stage4.order.add_edge(dd, hs)
stage4.order.add_edge(hs, dl)

# Stage 5: Supply Sync
# Stage 6: Continuous Maintenance Loop: execute Maintenance Plan, then optionally Waste Manage, then back
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[mp, wm])

# Top‐level partial order stitching all stages
root = StrictPartialOrder(nodes=[stage1, stage2, stage3, stage4, ss, maintenance_loop])
root.order.add_edge(stage1, stage2)
root.order.add_edge(stage2, stage3)
root.order.add_edge(stage3, stage4)
root.order.add_edge(stage4, ss)
root.order.add_edge(ss, maintenance_loop)