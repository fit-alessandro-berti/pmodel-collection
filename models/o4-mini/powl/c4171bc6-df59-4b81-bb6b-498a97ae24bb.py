# Generated from: c4171bc6-df59-4b81-bb6b-498a97ae24bb.json
# Description: This process outlines the complex steps involved in producing and delivering artisanal cheese from local farms to niche gourmet retailers. It starts with milk sourcing from specialized livestock, followed by quality testing, traditional curdling, and aging under controlled environments. The process includes periodic sensory evaluations, packaging with sustainable materials, coordinating cold-chain logistics, and managing limited batch releases. Additionally, it involves tracking provenance for authenticity, handling customer feedback for continuous improvement, and adapting production schedules based on seasonal milk variations and demand forecasting to maintain product excellence and exclusivity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
mp = Transition(label='Milk Pasteurize')
cf = Transition(label='Curd Formation')
ws = Transition(label='Whey Separation')
pc = Transition(label='Press Cheese')
sa = Transition(label='Salt Application')
ca = Transition(label='Controlled Aging')
sc = Transition(label='Sensory Check')
bp = Transition(label='Batch Packaging')
lp = Transition(label='Label Printing')
cs = Transition(label='Cold Storage')
pl = Transition(label='Logistics Plan')
rd = Transition(label='Retail Delivery')
fr = Transition(label='Feedback Review')
pt = Transition(label='Provenance Track')
df = Transition(label='Demand Forecast')

# Loop for periodic sensory evaluations during aging
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ca, sc]
)

# Define the body of one batch-production cycle as a partial order
process_PO = StrictPartialOrder(
    nodes=[
        ms, qt, mp, cf, ws, pc, sa,
        aging_loop,
        bp, lp, cs, pl, rd,
        pt, fr
    ]
)
# Sequencing edges
process_PO.order.add_edge(ms, qt)
process_PO.order.add_edge(qt, mp)
process_PO.order.add_edge(mp, cf)
process_PO.order.add_edge(cf, ws)
process_PO.order.add_edge(ws, pc)
process_PO.order.add_edge(pc, sa)
process_PO.order.add_edge(sa, aging_loop)
process_PO.order.add_edge(aging_loop, bp)
process_PO.order.add_edge(bp, lp)
process_PO.order.add_edge(lp, cs)
process_PO.order.add_edge(cs, pl)
process_PO.order.add_edge(pl, rd)
# After delivery, provenance tracking and feedback review run concurrently
process_PO.order.add_edge(rd, pt)
process_PO.order.add_edge(rd, fr)

# Wrap the batch cycle in an outer loop to adapt to demand forecasting
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[process_PO, df]
)