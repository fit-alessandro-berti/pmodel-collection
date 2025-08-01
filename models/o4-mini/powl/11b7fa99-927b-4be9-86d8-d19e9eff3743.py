# Generated from: 11b7fa99-927b-4be9-86d8-d19e9eff3743.json
# Description: This process outlines the complex and atypical steps involved in establishing a fully operational urban vertical farm within a metropolitan environment. It includes site selection based on sunlight and logistics, modular structure assembly, installation of hydroponic and aeroponic systems, integration of IoT sensors for environmental monitoring, automated nutrient delivery calibration, pest management using biocontrol agents, staff training in controlled environment agriculture, regulatory compliance checks, and market launch preparations. The process ensures sustainability, scalability, and maximized crop yield in limited urban spaces, leveraging innovative agricultural technology and smart data analytics to optimize plant growth cycles and reduce resource consumption in a highly controlled indoor ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ss = Transition(label='Site Survey')
sun = Transition(label='Sunlight Map')
sb = Transition(label='Structure Build')
si = Transition(label='System Install')
sensor = Transition(label='Sensor Setup')
data = Transition(label='Data Sync')
nut = Transition(label='Nutrient Mix')
pest = Transition(label='Pest Control')
staff = Transition(label='Staff Train')
audit = Transition(label='Regulation Audit')
plan = Transition(label='Crop Plan')
gm = Transition(label='Growth Monitor')
hp = Transition(label='Harvest Prep')
wc = Transition(label='Waste Cycle')
ml = Transition(label='Market Launch')

# Define the inner sequence for the loop: Growth Monitor -> Harvest Prep
cycle_body = StrictPartialOrder(nodes=[gm, hp])
cycle_body.order.add_edge(gm, hp)

# Define the loop: execute (Growth Monitor -> Harvest Prep), then optionally Waste Cycle and repeat
cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_body, wc])

# Build the root partial order
root = StrictPartialOrder(
    nodes=[ss, sun, sb, si, sensor, data, nut, pest, staff, audit, plan, cycle_loop, ml]
)

# Site selection in parallel, then structure build
root.order.add_edge(ss, sb)
root.order.add_edge(sun, sb)

# Sequential setup and calibration steps
root.order.add_edge(sb, si)
root.order.add_edge(si, sensor)
root.order.add_edge(sensor, data)
root.order.add_edge(data, nut)
root.order.add_edge(nut, pest)
root.order.add_edge(pest, staff)
root.order.add_edge(staff, audit)
root.order.add_edge(audit, plan)

# After planning, start the crop-growth loop
root.order.add_edge(plan, cycle_loop)

# After exiting the loop, prepare for market launch
root.order.add_edge(cycle_loop, ml)