# Generated from: 15841001-8519-459d-8d50-f40cae10ad80.json
# Description: This process outlines the comprehensive cycle of managing an urban vertical farm, integrating advanced hydroponics, automated nutrient delivery, environmental monitoring, and crop harvesting. It begins with site preparation and seed selection, followed by controlled germination, nutrient solution calibration, and continuous growth monitoring using IoT sensors. Pest and disease management is conducted with biocontrol agents, while energy optimization ensures sustainable operations. Harvesting is synchronized with market demand forecasts, and post-harvest processing includes quality grading and packaging. The cycle completes with waste recycling and system maintenance to ensure perpetual productivity within constrained urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
sp = Transition(label='Site Prep')
ss = Transition(label='Seed Select')
ge = Transition(label='Germination')
nm = Transition(label='Nutrient Mix')
gm = Transition(label='Growth Monitor')
pc = Transition(label='Pest Control')
dc = Transition(label='Disease Check')
ea = Transition(label='Energy Audit')
ca = Transition(label='Climate Adjust')
hp = Transition(label='Harvest Plan')
cp = Transition(label='Crop Picking')
qg = Transition(label='Quality Grade')
pg = Transition(label='Package Goods')
wr = Transition(label='Water Recycle')
wp = Transition(label='Waste Process')
sm = Transition(label='System Maintain')

# Initial one‐time setup sequence
initial = StrictPartialOrder(nodes=[sp, ss, ge, nm])
initial.order.add_edge(sp, ss)
initial.order.add_edge(ss, ge)
initial.order.add_edge(ge, nm)

# Main crop cycle: monitoring, protection, and harvesting
main_cycle = StrictPartialOrder(nodes=[gm, pc, dc, hp, cp, qg, pg])
# After germination and mixing:
#   monitor first
main_cycle.order.add_edge(gm, pc)
main_cycle.order.add_edge(gm, dc)
#   then harvest planning
main_cycle.order.add_edge(pc, hp)
main_cycle.order.add_edge(dc, hp)
main_cycle.order.add_edge(hp, cp)
main_cycle.order.add_edge(cp, qg)
main_cycle.order.add_edge(qg, pg)

# Maintenance and recycling tasks
maintenance = StrictPartialOrder(nodes=[ea, ca, wr, wp, sm])
maintenance.order.add_edge(ea, ca)
maintenance.order.add_edge(ca, wr)
maintenance.order.add_edge(wr, wp)
maintenance.order.add_edge(wp, sm)

# Loop: perform main cycle (A), then either exit or do maintenance (B) and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[main_cycle, maintenance])

# Root: initial setup once, then the cyclical loop
root = StrictPartialOrder(nodes=[initial, loop])
root.order.add_edge(initial, loop)