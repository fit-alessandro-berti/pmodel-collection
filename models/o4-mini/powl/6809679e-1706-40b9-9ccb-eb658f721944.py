# Generated from: 6809679e-1706-40b9-9ccb-eb658f721944.json
# Description: This process outlines the steps required to establish a sustainable urban rooftop farm in a dense city environment. It involves assessing rooftop structural integrity, designing modular planting systems, sourcing organic soil and seeds, installing automated irrigation and climate control, integrating renewable energy sources such as solar panels, and implementing pest control methods using natural predators. The process also includes community engagement for educational workshops, establishing distribution channels for local markets, and continuous monitoring through IoT sensors to optimize crop yield and resource usage. Finally, it covers maintenance routines and scalability planning for expanding the farm footprint across multiple rooftops in the city.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
a1  = Transition(label='Site Survey')
a2  = Transition(label='Load Testing')
a3  = Transition(label='Design Layout')
a4  = Transition(label='Material Sourcing')
a5  = Transition(label='Soil Preparation')
a6  = Transition(label='Seed Selection')
a7  = Transition(label='Irrigation Setup')
a8  = Transition(label='Climate Control')
a9  = Transition(label='Energy Integration')
a10 = Transition(label='Pest Management')
a11 = Transition(label='Community Outreach')
a12 = Transition(label='Market Setup')
a13 = Transition(label='Sensor Installation')
a14 = Transition(label='Data Monitoring')
a15 = Transition(label='Routine Maintenance')
a16 = Transition(label='Expansion Planning')

# Define loop: continuous monitoring and maintenance until exit
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[a14, a15]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, monitor_loop, a16
])

# Add ordering edges
root.order.add_edge(a1,  a2)
root.order.add_edge(a2,  a3)
root.order.add_edge(a3,  a4)
root.order.add_edge(a4,  a5)
root.order.add_edge(a5,  a6)
root.order.add_edge(a6,  a7)
root.order.add_edge(a7,  a8)
root.order.add_edge(a8,  a9)
root.order.add_edge(a9,  a10)
root.order.add_edge(a10, a11)
root.order.add_edge(a11, a12)
root.order.add_edge(a12, a13)
root.order.add_edge(a13, monitor_loop)
root.order.add_edge(monitor_loop, a16)