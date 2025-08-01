# Generated from: e3fbee47-9929-4f35-a2d8-3bf76e9b0d8c.json
# Description: This process details the end-to-end supply chain of artisan cheese production and distribution, involving unique steps such as milk sourcing from rare breed farms, custom fermentation monitoring, seasonal flavor adjustments, and niche market logistics. It integrates quality control with traditional craftsmanship, regulatory compliance, specialty packaging, and targeted retail partnerships. Each activity ensures the preservation of distinct cheese characteristics while optimizing delivery times to specialty shops and gourmet restaurants, balancing small-batch production constraints with demand forecasting and inventory management for limited edition releases.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
fs = Transition(label='Farm Selection')
mt = Transition(label='Milk Testing')
bp = Transition(label='Batch Pasteurize')
ca = Transition(label='Culture Add')
cc = Transition(label='Curd Cut')
wd = Transition(label='Whey Drain')
mi = Transition(label='Mold Inoculate')
pf = Transition(label='Press Form')
sr = Transition(label='Salt Rub')
am = Transition(label='Aging Monitor')
fa = Transition(label='Flavor Adjust')
pd = Transition(label='Packaging Design')
la = Transition(label='Label Approval')
op = Transition(label='Order Processing')
cs = Transition(label='Cold Storage')
ds = Transition(label='Delivery Schedule')
rs = Transition(label='Retail Setup')
fc = Transition(label='Feedback Collect')

# Model the fermentation loop: monitor aging, optionally adjust flavor, repeat until exit
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[am, fa])

# Build the overall partial order
nodes = [
    fs, mt, bp, ca, cc, wd, mi, pf, sr,
    fermentation_loop,
    pd, la, op, cs, ds, rs, fc
]
root = StrictPartialOrder(nodes=nodes)

# Define the control-flow ordering
root.order.add_edge(fs, mt)
root.order.add_edge(mt, bp)
root.order.add_edge(bp, ca)
root.order.add_edge(ca, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mi)
root.order.add_edge(mi, pf)
root.order.add_edge(pf, sr)
root.order.add_edge(sr, fermentation_loop)
# After finishing fermentation, proceed to packaging and distribution
root.order.add_edge(fermentation_loop, pd)
root.order.add_edge(pd, la)
root.order.add_edge(la, op)
root.order.add_edge(op, cs)
root.order.add_edge(cs, ds)
root.order.add_edge(ds, rs)
root.order.add_edge(rs, fc)