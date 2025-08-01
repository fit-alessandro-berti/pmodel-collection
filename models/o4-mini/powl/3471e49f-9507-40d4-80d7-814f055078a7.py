# Generated from: 3471e49f-9507-40d4-80d7-814f055078a7.json
# Description: This process outlines the intricate supply chain of artisan cheese production, starting from sourcing rare milk varieties from remote farms, followed by precise fermentation and aging under controlled conditions. It includes quality assessments at multiple stages, packaging with eco-friendly materials, and coordinating niche market distribution. The process also involves compliance checks with food safety regulations, demand forecasting for seasonal variations, and handling customer feedback to continuously improve product quality and supply efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
mp = Transition(label='Milk Pasteurization')
sc = Transition(label='Starter Culture')
cf = Transition(label='Curd Formation')
ws = Transition(label='Whey Separation')
pc = Transition(label='Pressing Cheese')
asu = Transition(label='Aging Setup')
hc = Transition(label='Humidity Control')
fs = Transition(label='Flavor Sampling')
pp = Transition(label='Packaging Prep')
ep = Transition(label='Eco Packaging')
ra = Transition(label='Regulatory Audit')
mf = Transition(label='Market Forecast')
of = Transition(label='Order Fulfillment')
cr = Transition(label='Customer Review')

# Loop for humidity control and flavor sampling until exit
loop_humidity = OperatorPOWL(operator=Operator.LOOP, children=[hc, fs])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ms, qt, mp, sc, cf, ws, pc, asu,
    loop_humidity,
    pp, ep, ra, mf, of, cr
])

# Define the control-flow dependencies
root.order.add_edge(ms, qt)
root.order.add_edge(qt, mp)
root.order.add_edge(mp, sc)
root.order.add_edge(sc, cf)
root.order.add_edge(cf, ws)
root.order.add_edge(ws, pc)
root.order.add_edge(pc, asu)
root.order.add_edge(asu, loop_humidity)
root.order.add_edge(loop_humidity, pp)
root.order.add_edge(pp, ep)
root.order.add_edge(ep, ra)
root.order.add_edge(ra, mf)
root.order.add_edge(mf, of)
root.order.add_edge(of, cr)