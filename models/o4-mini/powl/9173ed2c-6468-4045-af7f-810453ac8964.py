# Generated from: 9173ed2c-6468-4045-af7f-810453ac8964.json
# Description: This process outlines the intricate supply chain management for an artisan cheese producer specializing in rare, aged varieties. It involves sourcing unique milk from selected farms, monitoring fermentation environments, managing aging conditions in specialized caves, coordinating packaging with hand-labeling, and ensuring traceability through blockchain recording. The process also includes quality inspections at multiple stages, custom order handling from boutique retailers, logistics planning for temperature-controlled transport, and real-time inventory balancing to meet fluctuating demand while preserving product integrity and artisanal value.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
fs = Transition(label='Farm Sourcing')
mt = Transition(label='Milk Testing')
qi1 = Transition(label='Quality Inspect')
bm = Transition(label='Batch Mixing')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Draining')
mi = Transition(label='Mold Inoculation')
fc = Transition(label='Fermentation Check')
ca = Transition(label='Cave Aging')
qi2 = Transition(label='Quality Inspect')
rc = Transition(label='Retail Coordination')
oc = Transition(label='Order Customizing')
pp = Transition(label='Packaging Prep')
hl = Transition(label='Hand Labeling')
ct = Transition(label='Cold Transport')
bl = Transition(label='Blockchain Log')
df = Transition(label='Demand Forecast')
ia = Transition(label='Inventory Audit')

# Loop for fermentation checks
skip = SilentTransition()
loop_fc = OperatorPOWL(operator=Operator.LOOP, children=[fc, skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    fs, mt, qi1, bm, cc, wd, mi,
    loop_fc, ca, qi2, rc, oc, pp, hl,
    ct, bl, df, ia
])

# Define the control-flow order
o = root.order
o.add_edge(fs, mt)
o.add_edge(mt, qi1)
o.add_edge(qi1, bm)
o.add_edge(bm, cc)
o.add_edge(cc, wd)
o.add_edge(wd, mi)
o.add_edge(mi, loop_fc)
o.add_edge(loop_fc, ca)
o.add_edge(ca, qi2)
o.add_edge(qi2, rc)
o.add_edge(rc, oc)
o.add_edge(oc, pp)
o.add_edge(pp, hl)
o.add_edge(hl, ct)
o.add_edge(hl, bl)
o.add_edge(hl, df)
o.add_edge(df, ia)