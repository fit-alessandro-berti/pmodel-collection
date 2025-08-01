# Generated from: 231422f5-ae3e-43a4-af61-d60d81ea5ea3.json
# Description: This process outlines the comprehensive management cycle of an urban vertical farm integrating hydroponic and aeroponic systems across multiple stacked layers. It begins with seed selection based on environmental adaptability, followed by nutrient solution preparation tailored for each crop type. Automated planting robots sow seeds in specialized growth media. Continuous monitoring of microclimate variables such as humidity, CO2 levels, and light spectrum is performed via IoT sensors. Pest detection employs AI-driven image recognition to trigger targeted biocontrol releases. Harvesting robots operate with precision timing to optimize yield quality. Post-harvest, modular packaging units sanitize and pack produce for local distribution. Data analytics refine each cycle by correlating growth metrics with environmental adjustments, promoting sustainable resource use and minimizing waste. The process concludes with system sanitation and maintenance, ensuring readiness for subsequent planting cycles while integrating feedback loops from urban consumer demand patterns.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ss = Transition(label='Seed Select')
nm = Transition(label='Nutrient Mix')
mp = Transition(label='Media Prep')
pr = Transition(label='Planting Robot')
cm = Transition(label='Climate Monitor')
cc = Transition(label='CO2 Control')
la = Transition(label='Light Adjust')
hc = Transition(label='Humidity Check')
pd = Transition(label='Pest Detect')
bd = Transition(label='BioControl Deploy')
hr = Transition(label='Harvest Robot')
pp = Transition(label='Pack Produce')
gr = Transition(label='Growth Analyze')
ds = Transition(label='Data Sync')
dr = Transition(label='Demand Review')
sc = Transition(label='System Clean')

# A: seeding and planting preparation
A = StrictPartialOrder(nodes=[ss, nm, mp, pr])
A.order.add_edge(ss, nm)
A.order.add_edge(nm, mp)
A.order.add_edge(mp, pr)

# B: monitoring, control, harvest, packaging, analysis, review, cleaning
B = StrictPartialOrder(nodes=[cm, cc, la, hc, pd, bd, hr, pp, gr, ds, dr, sc])
# concurrent environmental monitoring feeds into pest detection
B.order.add_edge(cm, pd)
B.order.add_edge(cc, pd)
B.order.add_edge(la, pd)
B.order.add_edge(hc, pd)
# subsequent flow
B.order.add_edge(pd, bd)
B.order.add_edge(bd, hr)
B.order.add_edge(hr, pp)
B.order.add_edge(pp, gr)
B.order.add_edge(gr, ds)
B.order.add_edge(ds, dr)
B.order.add_edge(dr, sc)

# Looping the full cycle: do A, then either exit or do B then repeat A
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])