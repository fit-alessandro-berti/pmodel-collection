# Generated from: 0de7f5de-af68-4da7-b506-ca653b9da774.json
# Description: This process outlines the intricate and atypical supply chain of artisanal cheese production, involving unique steps such as milk sourcing from rare breeds, controlled fermentation environments, and a multi-level quality authentication system. The process integrates traditional craftsmanship with modern traceability technology, ensuring each batch maintains distinct regional characteristics while complying with stringent food safety standards. It also includes bespoke packaging design tailored to seasonal markets, customized logistics coordination for temperature-sensitive deliveries, and direct consumer engagement through curated tasting events. The complexity arises from managing small-scale producers, variable raw material quality, and fluctuating demand cycles, requiring adaptive scheduling, real-time quality feedback loops, and collaborative innovation with local farmers and artisans to sustain authenticity and profitability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
bs = Transition(label="Breed Selection")
mh = Transition(label="Milk Harvest")
it = Transition(label="Initial Testing")
ba = Transition(label="Batch Allocation")
fs = Transition(label="Fermentation Start")
hc = Transition(label="Humidity Control")
fl = Transition(label="Flavor Sampling")
rt = Transition(label="Rind Treatment")
am = Transition(label="Aging Monitor")
qa = Transition(label="Quality Audit")
tl = Transition(label="Trace Logging")
pd = Transition(label="Packaging Design")
mf = Transition(label="Market Forecast")
lp = Transition(label="Logistics Plan")
es = Transition(label="Event Setup")
cf = Transition(label="Customer Feedback")

# Build the fermentation feedback loop:
#  First child: Fermentation Start
#  Second child: the control and audit cycle
fermentation_cycle = StrictPartialOrder(nodes=[hc, fl, rt, am, qa])
# humidity and flavor sampling can run in parallel, both precede rind treatment
fermentation_cycle.order.add_edge(hc, rt)
fermentation_cycle.order.add_edge(fl, rt)
# then rind treatment -> aging monitor -> quality audit
fermentation_cycle.order.add_edge(rt, am)
fermentation_cycle.order.add_edge(am, qa)

fermentation_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[fs, fermentation_cycle]
)

# Assemble the overall workflow
root = StrictPartialOrder(
    nodes=[
        bs, mh, it, ba,
        fermentation_loop,
        mf, pd, lp, es, cf,
        tl  # Trace logging runs concurrently
    ]
)

# Define the partial order edges
root.order.add_edge(bs, mh)
root.order.add_edge(mh, it)
root.order.add_edge(it, ba)
root.order.add_edge(ba, fermentation_loop)
# Market forecast can start after initial testing, in parallel with fermentation
root.order.add_edge(it, mf)
# Packaging design after both fermentation (loop) and market forecast
root.order.add_edge(fermentation_loop, pd)
root.order.add_edge(mf, pd)
# Then logistics plan -> event setup -> customer feedback
root.order.add_edge(pd, lp)
root.order.add_edge(lp, es)
root.order.add_edge(es, cf)