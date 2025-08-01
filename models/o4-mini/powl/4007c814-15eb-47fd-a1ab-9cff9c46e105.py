# Generated from: 4007c814-15eb-47fd-a1ab-9cff9c46e105.json
# Description: This process outlines the unique and intricate supply chain for producing artisanal cheese, involving rare milk sourcing, traditional fermentation, customized aging, and niche market distribution. It includes quality inspections at multiple stages, environmental condition monitoring, and collaboration with local farmers. The process ensures the preservation of heritage techniques while integrating modern traceability and customer feedback loops to maintain product authenticity and high quality. Seasonal variations and small batch production add complexity, requiring adaptive scheduling and logistics coordination to meet demand without compromising artisanal standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Milk Sourcing')
qc = Transition(label='Quality Check')
mp = Transition(label='Milk Pasteurize')
cp = Transition(label='Culture Prepare')
mi = Transition(label='Milk Inoculate')
cm = Transition(label='Coagulate Milk')
cc = Transition(label='Curd Cut')
wd = Transition(label='Whey Drain')
mf = Transition(label='Mold Fill')
pc = Transition(label='Press Cheese')
sr = Transition(label='Salt Rub')
am = Transition(label='Aging Monitor')
hc = Transition(label='Humidity Control')
ft = Transition(label='Flavor Test')
pk = Transition(label='Packaging')
iu = Transition(label='Inventory Update')
of = Transition(label='Order Fulfill')
cf = Transition(label='Customer Feedback')

# Silent transition for optional feedback
skip = SilentTransition()

# Define the aging sub‐process: monitor humidity and temperature concurrently
aging_body = StrictPartialOrder(nodes=[am, hc])
# No order edges => 'Aging Monitor' and 'Humidity Control' can run in parallel

# Define the loop: do aging_body, then choose to exit or do Flavor Test then age again
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_body, ft])

# Define optional customer feedback (either do it, or skip)
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[cf, skip])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    ms, qc, mp, cp, mi, cm, cc, wd, mf, pc, sr,
    loop_aging,
    pk, iu, of,
    xor_feedback
])

# Sequential order of the main process
root.order.add_edge(ms, qc)
root.order.add_edge(qc, mp)
root.order.add_edge(mp, cp)
root.order.add_edge(cp, mi)
root.order.add_edge(mi, cm)
root.order.add_edge(cm, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mf)
root.order.add_edge(mf, pc)
root.order.add_edge(pc, sr)

# After salting, enter the aging loop
root.order.add_edge(sr, loop_aging)

# After aging completes, do packaging, inventory update, order fulfillment
root.order.add_edge(loop_aging, pk)
root.order.add_edge(pk, iu)
root.order.add_edge(iu, of)

# After an order is fulfilled, optionally gather customer feedback
root.order.add_edge(of, xor_feedback)