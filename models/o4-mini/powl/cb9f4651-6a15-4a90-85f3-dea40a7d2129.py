# Generated from: cb9f4651-6a15-4a90-85f3-dea40a7d2129.json
# Description: This process outlines the end-to-end supply chain for artisan cheese production, starting from selecting rare milk sources and managing microbial cultures to aging, quality testing, and niche market distribution. It involves coordinating small-scale farmers, custom fermentation, manual aging conditions, rigorous sensory evaluation, and targeted logistics to specialty retailers and gourmet restaurants. The process emphasizes traceability, batch uniqueness, and maintaining optimal conditions for flavor development while handling fluctuating seasonal inputs and demand forecasts.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
ms   = Transition(label='Milk Sourcing')
cp   = Transition(label='Culture Prep')
mp   = Transition(label='Milk Pasteurize')
mi   = Transition(label='Milk Inoculate')
cf   = Transition(label='Curd Formation')
cc   = Transition(label='Curd Cut')
wd   = Transition(label='Whey Drain')
mIn  = Transition(label='Mold Inoculate')
pc   = Transition(label='Press Cheese')
asu  = Transition(label='Aging Setup')
hCon = Transition(label='Humidity Control')
tMon = Transition(label='Temperature Monitor')
qt   = Transition(label='Quality Test')
pa   = Transition(label='Packaging')
of   = Transition(label='Order Fulfill')
rd   = Transition(label='Retail Deliver')
fc   = Transition(label='Feedback Collect')

# Build the loop for repeated quality‐test adjustments
# Loop semantics: do Quality Test, then either exit or do the adjustment (humidity→temperature) and repeat
adjust = StrictPartialOrder(nodes=[hCon, tMon])
adjust.order.add_edge(hCon, tMon)
loop_qt = OperatorPOWL(operator=Operator.LOOP, children=[qt, adjust])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    ms, cp, mp, mi, cf, cc, wd, mIn, pc, asu,
    loop_qt, pa, of, rd, fc
])

# Add the sequential edges
edges = [
    (ms,   cp),
    (cp,   mp),
    (mp,   mi),
    (mi,   cf),
    (cf,   cc),
    (cc,   wd),
    (wd,   mIn),
    (mIn,  pc),
    (pc,   asu),
    (asu,  loop_qt),
    (loop_qt, pa),
    (pa,   of),
    (of,   rd),
    (rd,   fc)
]
for src, tgt in edges:
    root.order.add_edge(src, tgt)