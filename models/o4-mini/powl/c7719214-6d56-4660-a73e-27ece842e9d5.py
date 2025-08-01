# Generated from: c7719214-6d56-4660-a73e-27ece842e9d5.json
# Description: This process outlines the intricate supply chain management for artisan cheese production, starting from sourcing rare milk varieties from micro-farms, monitoring seasonal animal diets, coordinating fermentation timing, to ensuring optimal aging conditions in climate-controlled caves. It integrates quality checks, custom packaging, and niche market distribution through boutique retailers and specialty food events. Each step involves close collaboration with local farmers, microbiologists, logistics experts, and marketing teams to maintain authentic flavor profiles while adapting to fluctuating demand and regulatory requirements. The process balances tradition with innovation, emphasizing traceability and sustainability at every stage, guaranteeing a product that meets exacting standards and satisfies discerning consumers in a competitive gourmet market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label="Milk Sourcing")
dm = Transition(label="Diet Monitoring")
cs = Transition(label="Culture Selection")
mp = Transition(label="Milk Pasteurize")
cc = Transition(label="Curd Cutting")
wd = Transition(label="Whey Draining")
mi = Transition(label="Mold Inoculate")
pf = Transition(label="Press Forming")
sa = Transition(label="Salt Application")
asu = Transition(label="Aging Setup")
hc = Transition(label="Humidity Control")
ft = Transition(label="Flavor Testing")
pd = Transition(label="Packaging Design")
op = Transition(label="Order Processing")
rd = Transition(label="Retail Delivery")
ec = Transition(label="Event Coordination")
fr = Transition(label="Feedback Review")

# Build the aging loop: perform Aging Setup, then zero or more iterations of (Humidity Control -> Flavor Testing)
loop_body = StrictPartialOrder(nodes=[hc, ft])
loop_body.order.add_edge(hc, ft)
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[asu, loop_body])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        ms, dm, cs, mp, cc, wd, mi, pf, sa,
        aging_loop,
        pd, op, rd, ec, fr
    ]
)

# Define the control‐flow dependencies
# Sourcing & monitoring before culture selection
root.order.add_edge(ms, dm)
root.order.add_edge(ms, cs)
root.order.add_edge(dm, cs)

# Culture selection → pasteurization → cutting → draining → inoculation → forming → salting → aging
root.order.add_edge(cs, mp)
root.order.add_edge(mp, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mi)
root.order.add_edge(mi, pf)
root.order.add_edge(pf, sa)
root.order.add_edge(sa, aging_loop)

# After aging completes → packaging & order processing (in parallel)
root.order.add_edge(aging_loop, pd)
root.order.add_edge(aging_loop, op)

# Packaging & order processing → distribution (retail & events)
root.order.add_edge(pd, rd)
root.order.add_edge(op, rd)
root.order.add_edge(pd, ec)
root.order.add_edge(op, ec)

# After distribution → feedback review
root.order.add_edge(rd, fr)
root.order.add_edge(ec, fr)