# Generated from: b8fe8e8d-1b06-4a0e-8812-a729b87f69db.json
# Description: This process describes the comprehensive operational cycle of an urban vertical farming facility specializing in multi-layer hydroponic vegetable production. It begins with nutrient solution preparation, followed by seed germination under controlled LED lighting. The seedlings are then transplanted into vertical racks where climate control systems optimize temperature, humidity, and CO2 levels. Automated sensors monitor plant health and growth metrics, triggering targeted nutrient adjustments. Periodic pest management employs integrated biological controls instead of chemicals. Harvesting is synchronized with market demand forecasts, while waste biomass is processed via onsite composting units. Finally, produce is packaged in eco-friendly materials and distributed through urban logistics channels, closing the loop with data-driven yield analysis for continuous improvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
np = Transition(label='Nutrient Prep')
sg = Transition(label='Seed Germinate')
lc = Transition(label='Light Control')
ts = Transition(label='Transplant Seedlings')
ca = Transition(label='Climate Adjust')
cm = Transition(label='CO2 Monitor')
ss = Transition(label='Sensor Scan')
na = Transition(label='Nutrient Adjust')
pc = Transition(label='Pest Control')
gr = Transition(label='Growth Record')
hs = Transition(label='Harvest Schedule')
wc = Transition(label='Waste Compost')
ep = Transition(label='Eco Package')
ud = Transition(label='Urban Dispatch')
ya = Transition(label='Yield Analyze')

# Concurrent climate control activities
climateCO2 = StrictPartialOrder(nodes=[ca, cm])

# Body of the monitoring loop: nutrient adjust, pest control, growth record (concurrent)
monitor_body = StrictPartialOrder(nodes=[na, pc, gr])

# Loop: sensor scan then either exit or execute body then scan again
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[ss, monitor_body])

# Assemble the top‐level partial order
root = StrictPartialOrder(
    nodes=[np, sg, lc, ts, climateCO2, sensor_loop, hs, wc, ep, ud, ya]
)

# Define the control‐flow dependencies
root.order.add_edge(np, sg)
root.order.add_edge(sg, lc)
root.order.add_edge(lc, ts)
root.order.add_edge(ts, climateCO2)
root.order.add_edge(climateCO2, sensor_loop)
root.order.add_edge(sensor_loop, hs)
root.order.add_edge(hs, wc)
root.order.add_edge(wc, ep)
root.order.add_edge(ep, ud)
root.order.add_edge(ud, ya)