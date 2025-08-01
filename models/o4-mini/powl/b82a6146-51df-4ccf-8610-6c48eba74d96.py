# Generated from: b82a6146-51df-4ccf-8610-6c48eba74d96.json
# Description: This process involves the sourcing, crafting, and distribution of small-batch artisan cheeses with an emphasis on traditional methods and quality control. Starting from selecting rare milk varieties, the process includes multiple fermentation stages, aging in controlled environments, and detailed sensory evaluations. Packaging is customized for different markets, followed by a logistics phase targeting niche retailers and direct consumer deliveries. Throughout, traceability and sustainability metrics are continuously monitored to ensure product integrity and minimal environmental impact, making this supply chain complex yet highly specialized and adaptive to market preferences.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
sp = Transition(label='Starter Prep')
mp = Transition(label='Milk Pasteurize')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Draining')
pm_t = Transition(label='Press Molding')
sa = Transition(label='Salt Application')
fs = Transition(label='Fermentation Stage')
ac = Transition(label='Aging Control')
sr = Transition(label='Sensory Review')
pd = Transition(label='Packaging Design')
lp = Transition(label='Label Printing')
op = Transition(label='Order Processing')
dpl = Transition(label='Distribution Plan')
saudit = Transition(label='Sustainability Audit')
cf = Transition(label='Customer Feedback')

# Inner partial order of the core cheese‐making and distribution process
inner = StrictPartialOrder(nodes=[
    ms, qt, sp, mp, cc, wd, pm_t, sa, fs, ac,
    sr, pd, lp, op, dpl, saudit
])
# Define the main flow dependencies
inner.order.add_edge(ms, qt)
inner.order.add_edge(qt, sp)
inner.order.add_edge(sp, mp)
inner.order.add_edge(mp, cc)
inner.order.add_edge(cc, wd)
inner.order.add_edge(wd, pm_t)
inner.order.add_edge(pm_t, sa)
inner.order.add_edge(sa, fs)
inner.order.add_edge(fs, ac)
inner.order.add_edge(ac, sr)
inner.order.add_edge(sr, pd)
inner.order.add_edge(pd, lp)
inner.order.add_edge(lp, op)
inner.order.add_edge(op, dpl)
# 'Sustainability Audit' remains unconnected to show continuous concurrent monitoring

# Wrap the entire process in a loop to account for customer-feedback-driven adaptation
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[inner, cf]
)