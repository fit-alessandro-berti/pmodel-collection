# Generated from: 8edd5746-9994-49ff-977f-8195dc2765db.json
# Description: This process involves establishing a multi-layered urban vertical farm within a constrained city environment. It begins with site analysis and zoning approval, followed by modular infrastructure design tailored to limited space. The process includes hydroponic system installation, nutrient solution calibration, and automated climate control integration. Subsequent activities address seed selection, germination scheduling, and pest management using bio-controls. Continuous monitoring via IoT sensors ensures optimal growth conditions, while data analytics optimize yield cycles. The process concludes with harvest planning, packaging automation, and distribution logistics adapted to urban markets, focusing on sustainability and minimal carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SA = Transition(label='Site Analysis')
ZA = Transition(label='Zoning Approval')
MD = Transition(label='Modular Design')
HS = Transition(label='Hydroponic Setup')
NM = Transition(label='Nutrient Mix')
CC = Transition(label='Climate Control')
SS = Transition(label='Seed Selection')
GP = Transition(label='Germination Plan')
PC = Transition(label='Pest Control')
SI = Transition(label='Sensor Installation')
DM = Transition(label='Data Monitoring')
YA = Transition(label='Yield Analysis')
HP = Transition(label='Harvest Planning')
PS = Transition(label='Packaging Setup')
US = Transition(label='Urban Shipping')

# Define a monitoring loop: continuous data monitoring and yield analysis
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[DM, YA])

# Build the partial order of the entire process
root = StrictPartialOrder(nodes=[
    SA, ZA, MD, HS, NM, CC,
    SS, GP, PC,
    SI, monitor_loop,
    HP, PS, US
])

# Add sequencing edges
root.order.add_edge(SA, ZA)
root.order.add_edge(ZA, MD)
root.order.add_edge(MD, HS)
root.order.add_edge(HS, NM)
root.order.add_edge(NM, CC)
root.order.add_edge(CC, SS)
root.order.add_edge(SS, GP)
root.order.add_edge(GP, PC)
root.order.add_edge(PC, SI)
root.order.add_edge(SI, monitor_loop)
root.order.add_edge(monitor_loop, HP)
root.order.add_edge(HP, PS)
root.order.add_edge(PS, US)