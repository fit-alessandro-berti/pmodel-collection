# Generated from: ef1a0fbc-d3ef-4b0e-a3d3-13ea033dcc6c.json
# Description: This process details the intricate and highly specialized supply chain management for artisanal cheese production, starting from sourcing rare milk varieties from micro-farms, through controlled fermentation and aging in unique environmental conditions, to bespoke packaging and distribution to niche gourmet retailers worldwide. It involves coordination with local farmers, quality testing at multiple stages, compliance with food safety regulations, custom labeling, and handling of rare ingredient procurement. Additionally, the process integrates seasonal adjustments based on milk availability, real-time inventory tracking, and direct consumer feedback loops for continuous product refinement and artisan branding enhancement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
farm = Transition(label='Farm Selection')
sourcing = Transition(label='Milk Sourcing')
qc = Transition(label='Quality Testing')
pasteurize = Transition(label='Milk Pasteurize')
starter = Transition(label='Starter Culture')
coag = Transition(label='Coagulation')
cutting = Transition(label='Curd Cutting')
draining = Transition(label='Whey Draining')
mold = Transition(label='Mold Inoculate')
aging = Transition(label='Aging Control')
tasting = Transition(label='Flavor Tasting')
pack_design = Transition(label='Packaging Design')
label = Transition(label='Label Approval')
inventory = Transition(label='Inventory Audit')
order = Transition(label='Order Fulfill')
shipping = Transition(label='Retail Shipping')

# Silent transition for seasonal adjustment placeholder
seasonal = SilentTransition()

# Packaging refinement loop:
#   Body = (Packaging Design -> Label Approval)
#   Recursion = Flavor Tasting (consumer feedback)
pack_seq = StrictPartialOrder(nodes=[pack_design, label])
pack_seq.order.add_edge(pack_design, label)
pack_loop = OperatorPOWL(operator=Operator.LOOP, children=[pack_seq, tasting])

# Distribution & inventory loop:
#   Body = (Order Fulfill -> Retail Shipping)
#   Recursion = Inventory Audit (real-time tracking)
dist_seq = StrictPartialOrder(nodes=[order, shipping])
dist_seq.order.add_edge(order, shipping)
dist_loop = OperatorPOWL(operator=Operator.LOOP, children=[dist_seq, inventory])

# Main production pipeline (one season iteration)
main_nodes = [
    farm,
    sourcing,
    qc,
    pasteurize,
    starter,
    coag,
    cutting,
    draining,
    mold,
    aging,
    pack_loop,
    dist_loop
]
main = StrictPartialOrder(nodes=main_nodes)
# Define the sequential control-flow
main.order.add_edge(farm, sourcing)
main.order.add_edge(sourcing, qc)
main.order.add_edge(qc, pasteurize)
main.order.add_edge(pasteurize, starter)
main.order.add_edge(starter, coag)
main.order.add_edge(coag, cutting)
main.order.add_edge(cutting, draining)
main.order.add_edge(draining, mold)
main.order.add_edge(mold, aging)
main.order.add_edge(aging, pack_loop)
main.order.add_edge(pack_loop, dist_loop)

# Top‐level seasonal loop:
#   Body = one full production iteration (main)
#   Recursion = seasonal adjustment (silent placeholder)
root = OperatorPOWL(operator=Operator.LOOP, children=[main, seasonal])