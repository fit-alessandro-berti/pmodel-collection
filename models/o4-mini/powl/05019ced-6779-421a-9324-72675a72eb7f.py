# Generated from: 05019ced-6779-421a-9324-72675a72eb7f.json
# Description: This complex process outlines the journey of artisanal cheese production and distribution, beginning with raw milk sourcing from specialized farms. It includes quality testing, maturation under controlled conditions, custom flavor infusion, packaging with eco-friendly materials, and finally, niche market distribution. The process involves coordination between farmers, microbiologists, flavor experts, logistic teams, and retail partners to ensure product authenticity, safety, and uniqueness. Continuous feedback loops support refinement of both product and delivery, adapting to seasonal variations and customer preferences while maintaining traditional craftsmanship standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
ms   = Transition(label='Milk Sourcing')
fi   = Transition(label='Farm Inspection')
qt   = Transition(label='Quality Testing')
sc   = Transition(label='Starter Culture')
coag = Transition(label='Coagulation')
cut  = Transition(label='Curd Cutting')
wd   = Transition(label='Whey Draining')
mc   = Transition(label='Molding Cheese')
ca   = Transition(label='Controlled Aging')
tc   = Transition(label='Texture Checking')
fl   = Transition(label='Flavor Infusion')
ep   = Transition(label='Eco Packaging')
lp   = Transition(label='Label Printing')
il   = Transition(label='Inventory Logging')
op   = Transition(label='Order Processing')
shh  = Transition(label='Special Handling')
sd   = Transition(label='Shipment Dispatch')
rs   = Transition(label='Retail Setup')

# Loop for controlled aging: 
#    execute one aging cycle (ca), then texture check (tc), 
#    then either exit or do another aging cycle + check
loop_aging = OperatorPOWL(
    operator=Operator.LOOP,
    children=[tc, ca]
)

# Build the distribution sub‐process as a small PO:
dist_po = StrictPartialOrder(nodes=[op, shh, sd, rs])
dist_po.order.add_edge(op, shh)
dist_po.order.add_edge(shh, sd)
dist_po.order.add_edge(sd, rs)

# Loop for order‐driven distribution: 
#    inventory logging (il) then either exit or do an order‐dispatch cycle
distribution_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[il, dist_po]
)

# Assemble the top‐level workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    ms, fi, qt, sc, coag, cut, wd, mc, ca, 
    loop_aging, fl, ep, lp, distribution_loop
])

# Define the global ordering (a mostly sequential backbone)
root.order.add_edge(ms, fi)
root.order.add_edge(fi, qt)
root.order.add_edge(qt, sc)
root.order.add_edge(sc, coag)
root.order.add_edge(coag, cut)
root.order.add_edge(cut, wd)
root.order.add_edge(wd, mc)

# Initial aging + feedback loop
root.order.add_edge(mc, ca)
root.order.add_edge(ca, loop_aging)
root.order.add_edge(loop_aging, fl)

# Packaging and labeling
root.order.add_edge(fl, ep)
root.order.add_edge(ep, lp)

# Distribution loop
root.order.add_edge(lp, distribution_loop)