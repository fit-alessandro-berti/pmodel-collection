# Generated from: 760dc89e-da5b-4370-b399-aac0443faa09.json
# Description: This process outlines the intricate steps involved in the production and distribution of artisan cheese, from sourcing rare milk varieties to aging and quality testing. It includes delicate decisions on fermentation duration, packaging with sustainable materials, coordinating with niche retailers, and managing seasonal demand fluctuations. The process also ensures compliance with regional food safety standards while incorporating customer feedback loops to refine flavor profiles and enhance brand reputation. Logistics coordination involves cold chain management, customs clearance for international shipments, and contingency planning for supply disruptions caused by environmental factors or animal health issues. Marketing efforts focus on storytelling and provenance verification to attract discerning consumers and maintain premium pricing strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms  = Transition(label='Milk Sourcing')
qt  = Transition(label='Quality Testing')
cs  = Transition(label='Culture Selection')
mp  = Transition(label='Milk Pasteurize')
cst = Transition(label='Coagulation Step')
ccu = Transition(label='Curd Cutting')
wd  = Transition(label='Whey Drain')
mc  = Transition(label='Molding Cheese')
pb  = Transition(label='Pressing Block')
sp  = Transition(label='Salting Process')
am  = Transition(label='Aging Monitor')
ft  = Transition(label='Flavor Tasting')
pp  = Transition(label='Packaging Prep')
sc  = Transition(label='Sustainability Check')
oc  = Transition(label='Order Coordination')
csd = Transition(label='Cold Storage')
cl  = Transition(label='Customs Clearance')
rd  = Transition(label='Retail Delivery')
cfb = Transition(label='Customer Feedback')
ma  = Transition(label='Market Analysis')

# Silent skip for optional paths
skip = SilentTransition()

# Loop for aging & tasting cycle: monitor aging, then optionally taste and repeat
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[am, ft])

# XOR for optional customs clearance (international vs. domestic)
xor_customs = OperatorPOWL(operator=Operator.XOR, children=[cl, skip])

# Main partial order of the cheese production & distribution process
main = StrictPartialOrder(nodes=[
    ms, qt, cs, mp, cst, ccu, wd, mc, pb, sp,
    loop_aging,
    pp, sc, oc, csd, xor_customs, rd, cfb
])

# Define the ordering dependencies
main.order.add_edge(ms,  qt)
main.order.add_edge(qt,  cs)
main.order.add_edge(cs,  mp)
main.order.add_edge(mp,  cst)
main.order.add_edge(cst, ccu)
main.order.add_edge(ccu, wd)
main.order.add_edge(wd,  mc)
main.order.add_edge(mc,  pb)
main.order.add_edge(pb,  sp)
main.order.add_edge(sp,  loop_aging)
main.order.add_edge(loop_aging, pp)
main.order.add_edge(pp,  sc)
main.order.add_edge(sc,  oc)
main.order.add_edge(oc,  csd)
main.order.add_edge(csd, xor_customs)
main.order.add_edge(xor_customs, rd)
main.order.add_edge(rd,  cfb)

# Top‐level loop: after customer feedback, perform market analysis, then repeat the whole process
root = OperatorPOWL(operator=Operator.LOOP, children=[main, ma])