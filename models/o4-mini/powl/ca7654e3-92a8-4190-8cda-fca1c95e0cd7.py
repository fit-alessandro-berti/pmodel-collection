# Generated from: ca7654e3-92a8-4190-8cda-fca1c95e0cd7.json
# Description: This process covers the end-to-end supply chain for artisan cheese production, blending traditional methods with modern logistics. It begins with sourcing rare milk varieties from specialized farms, followed by precise curdling and aging techniques governed by seasonal conditions. Quality inspections and microbial testing are conducted repeatedly to ensure product integrity. Packaging involves eco-friendly materials tailored to preserve flavor and texture. Distribution requires coordination with boutique retailers and direct-to-consumer channels, including subscription services. The process integrates feedback loops from tastings and market trends to continuously refine recipes and supply strategies, balancing artisanal quality with scalable delivery demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ms = Transition(label='Milk Sourcing')
cp = Transition(label='Curd Preparation')
sc = Transition(label='starter Culture')
tc = Transition(label='Temperature Control')
pc = Transition(label='Pressing Cheese')
ss = Transition(label='Salting Stage')
ap = Transition(label='Aging Process')
mt = Transition(label='Microbial Test')
qc = Transition(label='Quality Check')
eco = Transition(label='Eco Packaging')
label = Transition(label='Label Printing')
audit = Transition(label='Inventory Audit')
order = Transition(label='Order Processing')
retail = Transition(label='Retail Shipping')
feedback = Transition(label='Customer Feedback')
update = Transition(label='Recipe Update')
analysis = Transition(label='Market Analysis')

# Silent transitions for loops
skip_ins = SilentTransition()
skip_glob = SilentTransition()

# Inner loop: repeated microbial testing and quality checks
inspection_seq = StrictPartialOrder(nodes=[mt, qc])
inspection_seq.order.add_edge(mt, qc)
loop_inspection = OperatorPOWL(operator=Operator.LOOP, children=[inspection_seq, skip_ins])

# Main linear workflow including the inspection loop
main_nodes = [
    ms, cp, sc, tc, pc, ss, ap,
    loop_inspection,
    eco, label,
    audit, order, retail,
    feedback, update, analysis
]
root_seq = StrictPartialOrder(nodes=main_nodes)

# Add the sequential dependencies
edges = [
    (ms, cp),
    (cp, sc),
    (sc, tc),
    (tc, pc),
    (pc, ss),
    (ss, ap),
    (ap, loop_inspection),
    (loop_inspection, eco),
    (eco, label),
    (label, audit),
    (audit, order),
    (order, retail),
    (retail, feedback),
    (feedback, update),
    (update, analysis)
]
for src, tgt in edges:
    root_seq.order.add_edge(src, tgt)

# Outer loop: repeat the entire end-to-end process for continuous refinement
root = OperatorPOWL(operator=Operator.LOOP, children=[root_seq, skip_glob])