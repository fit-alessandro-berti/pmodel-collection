# Generated from: 73fb740b-86a2-4c31-88a6-cab5a351820b.json
# Description: This process outlines the complex supply chain and quality assurance workflow involved in producing and distributing artisanal cheese from small-scale dairy farms to niche gourmet retailers. It includes activities such as sourcing rare milk varieties, managing seasonal fermentation conditions, coordinating with independent aging specialists, conducting sensory evaluations, navigating local food safety regulations, and orchestrating tailored logistics for temperature-controlled deliveries. The process ensures product consistency, maintains traditional craftsmanship standards, and adapts dynamically to fluctuating supply and demand while preserving the unique flavor profiles and heritage of each cheese variety.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
fs = Transition(label='Fermentation Setup')
tc = Transition(label='Temperature Control')
cc = Transition(label='Curd Cutting')
ws = Transition(label='Whey Separation')
mc = Transition(label='Molding Cheese')
sp = Transition(label='Salting Process')
ac = Transition(label='Aging Coordination')
sr = Transition(label='Sensory Review')
pd = Transition(label='Packaging Design')
la = Transition(label='Label Approval')
rc = Transition(label='Regulation Check')
op = Transition(label='Order Processing')
cs = Transition(label='Cold Shipping')
ia = Transition(label='Inventory Audit')
cf = Transition(label='Customer Feedback')

# Loop for adjusting fermentation conditions:
#   Do Fermentation Setup, then either exit or perform Temperature Control and go back
loop_fermentation = OperatorPOWL(
    operator=Operator.LOOP,
    children=[fs, tc]
)

# Loop for refining packaging after sensory review:
#   Do Sensory Review, then either exit or perform Packaging Design and go back
loop_packaging = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sr, pd]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ms, qt,
    loop_fermentation,
    cc, ws, mc, sp,
    ac,
    loop_packaging,
    la, rc, op, cs, ia, cf
])

# Define the control-flow dependencies
root.order.add_edge(ms, qt)
root.order.add_edge(qt, loop_fermentation)
root.order.add_edge(loop_fermentation, cc)
root.order.add_edge(cc, ws)
root.order.add_edge(ws, mc)
root.order.add_edge(mc, sp)
root.order.add_edge(sp, ac)
root.order.add_edge(ac, loop_packaging)
root.order.add_edge(loop_packaging, la)
root.order.add_edge(la, rc)
root.order.add_edge(rc, op)
root.order.add_edge(op, cs)
root.order.add_edge(cs, ia)
root.order.add_edge(ia, cf)