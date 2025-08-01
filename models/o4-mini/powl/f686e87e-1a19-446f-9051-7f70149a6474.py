# Generated from: f686e87e-1a19-446f-9051-7f70149a6474.json
# Description: This process involves the intricate coordination of sourcing raw milk from multiple small-scale farms, ensuring quality through microbial testing, and managing seasonal variations. It includes curdling, aging under controlled humidity and temperature, and packaging with detailed provenance labels. The distribution phase requires temperature-controlled logistics to specialty retailers and direct-to-consumer channels. Additionally, the process entails continuous feedback collection from customers to refine aging profiles and innovate new cheese varieties, while complying with stringent food safety and organic certification standards throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
bc = Transition(label='Batch Curdling')
wr = Transition(label='Whey Removal')
mi = Transition(label='Mold Inoculation')
hc = Transition(label='Humidity Control')
ta = Transition(label='Temperature Aging')
rb = Transition(label='Rind Brushing')
fs = Transition(label='Flavor Sampling')
lp = Transition(label='Label Printing')
pp = Transition(label='Packaging Prep')
cs = Transition(label='Cold Storage')
oc = Transition(label='Order Consolidation')
ls = Transition(label='Logistics Scheduling')
cf = Transition(label='Customer Feedback')
ca = Transition(label='Certification Audit')
ra = Transition(label='Recipe Adjustment')

# Loop for continuous improvement: Customer Feedback -> Recipe Adjustment, repeat
improvementLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cf, ra]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    ms, qt, bc, wr, mi, hc, ta, rb, fs, lp, pp, cs, oc, ls, ca, improvementLoop
])

# Define control‐flow dependencies
root.order.add_edge(ms, qt)
root.order.add_edge(qt, ca)   # certification audit can run concurrently after testing
root.order.add_edge(qt, bc)
root.order.add_edge(bc, wr)
root.order.add_edge(wr, mi)
root.order.add_edge(mi, hc)
root.order.add_edge(hc, ta)
root.order.add_edge(ta, rb)
root.order.add_edge(rb, fs)
root.order.add_edge(fs, lp)
root.order.add_edge(lp, pp)
root.order.add_edge(pp, cs)
root.order.add_edge(cs, oc)
root.order.add_edge(oc, ls)
root.order.add_edge(ls, improvementLoop)