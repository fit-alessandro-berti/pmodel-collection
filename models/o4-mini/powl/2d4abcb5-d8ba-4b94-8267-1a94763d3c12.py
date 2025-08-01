# Generated from: 2d4abcb5-d8ba-4b94-8267-1a94763d3c12.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a repurposed warehouse. It begins with site analysis and structural reinforcement, followed by climate system installation to optimize growth conditions. The process continues with hydroponic system setup, integration of IoT sensors for real-time monitoring, and selection of crop varieties tailored to urban demand. Subsequent activities include staff training on automated maintenance, pest control protocols, nutrient solution management, and energy efficiency auditing. Finally, the process covers harvest scheduling, packaging optimization for urban distribution, and customer feedback loops to continuously refine production and delivery methods, ensuring sustainability and profitability in a challenging urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
sa    = Transition(label='Site Analysis')
sc    = Transition(label='Structure Check')
cs    = Transition(label='Climate Setup')
hi    = Transition(label='Hydroponics Install')
si    = Transition(label='Sensor Integration')
csel  = Transition(label='Crop Selection')
st    = Transition(label='Staff Training')
pc    = Transition(label='Pest Control')
nm    = Transition(label='Nutrient Mix')
ea    = Transition(label='Energy Audit')
maint = Transition(label='Maintenance')
hp    = Transition(label='Harvest Plan')
po    = Transition(label='Packaging Opt')
ds    = Transition(label='Delivery Setup')
fb    = Transition(label='Feedback Loop')
dr    = Transition(label='Data Review')

# Define the looping structure over Packaging & Delivery with Feedback
# A_loop = Packaging Opt --> Delivery Setup
A_loop = StrictPartialOrder(nodes=[po, ds])
A_loop.order.add_edge(po, ds)

# B_loop = Feedback Loop --> Data Review
B_loop = StrictPartialOrder(nodes=[fb, dr])
B_loop.order.add_edge(fb, dr)

loop_node = OperatorPOWL(operator=Operator.LOOP, children=[A_loop, B_loop])

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        sa, sc, cs, hi, si, csel,
        st, pc, nm, ea, maint,
        hp, loop_node
    ]
)

# Sequential flow up to Crop Selection
root.order.add_edge(sa, sc)
root.order.add_edge(sc, cs)
root.order.add_edge(cs, hi)
root.order.add_edge(hi, si)
root.order.add_edge(si, csel)

# After Crop Selection, five activities in parallel
for task in [st, pc, nm, ea, maint]:
    root.order.add_edge(csel, task)

# All those five must complete before Harvest Plan
for task in [st, pc, nm, ea, maint]:
    root.order.add_edge(task, hp)

# After harvesting, enter the loop node
root.order.add_edge(hp, loop_node)