# Generated from: 0ddef569-63db-4f3b-92fe-11e57a1988b3.json
# Description: This process governs the end-to-end supply chain for specialized microbial cultures used in biotechnological research and pharmaceutical production. It begins with strain acquisition, followed by genetic verification, controlled cultivation, contamination monitoring, biomass harvesting, preservation through lyophilization, packaging under sterile conditions, cold chain logistics coordination, quality validation at multiple checkpoints, inventory management with real-time tracking, regulatory documentation compliance, customer-specific formulation adjustments, and finally, delivery with post-dispatch support for culture revival and viability confirmation. The process integrates scientific rigor with logistical precision to ensure live cultures arrive viable and uncontaminated at research or production facilities worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
sa  = Transition(label='Strain Acquire')
gv  = Transition(label='Genetic Verify')
ci  = Transition(label='Culture Initiate')
gm  = Transition(label='Growth Monitor')
cc  = Transition(label='Contam Check')
bh  = Transition(label='Biomass Harvest')
lyo = Transition(label='Lyophilize Sample')
sp  = Transition(label='Sterile Package')
cold = Transition(label='Cold Chain')
qv  = Transition(label='Quality Validate')
it  = Transition(label='Inventory Track')
rr  = Transition(label='Regulatory Review')
fa  = Transition(label='Formulation Adjust')
dp  = Transition(label='Dispatch Prepare')
cs  = Transition(label='Client Support')

# Create a strict partial order and add the nodes
nodes = [sa, gv, ci, gm, cc, bh, lyo, sp, cold, qv, it, rr, fa, dp, cs]
root = StrictPartialOrder(nodes=nodes)

# Add the sequential dependencies
for predecessor, successor in zip(nodes, nodes[1:]):
    root.order.add_edge(predecessor, successor)