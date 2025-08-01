# Generated from: 6bad82af-7ac5-4a26-8c72-b41a104f557e.json
# Description: This process details the complex steps involved in exporting artisanal cheese from small-scale farms to international gourmet markets. It begins with milk sourcing from specific breed cows, followed by precise curdling and aging under controlled conditions. The cheese is then carefully packaged with temperature monitoring and compliance with diverse export regulations. Logistics coordination includes cold chain management, customs clearance, and distribution to boutique retailers. The process requires continuous quality testing and feedback loops with producers to maintain product integrity and meet varying consumer tastes across regions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Milk Sourcing')
bs = Transition(label='Breed Selection')
cf = Transition(label='Curd Formation')
pc = Transition(label='Pressing Cheese')
ap = Transition(label='Aging Process')
qt = Transition(label='Quality Testing')
pp = Transition(label='Packaging Prep')
tm = Transition(label='Temp Monitoring')
lc = Transition(label='Label Compliance')
ed = Transition(label='Export Documentation')
cc = Transition(label='Cold Chain')
cl = Transition(label='Customs Clearance')
sb = Transition(label='Shipping Booking')
rc = Transition(label='Retail Coordination')
fr = Transition(label='Feedback Review')

# Packaging sub‐process: prep before monitoring and labeling (those in parallel)
packaging_po = StrictPartialOrder(nodes=[pp, tm, lc])
packaging_po.order.add_edge(pp, tm)
packaging_po.order.add_edge(pp, lc)

# Logistics sub‐process: documentation, then parallel cold‐chain & customs, then booking, then retail
logistics_po = StrictPartialOrder(nodes=[ed, cc, cl, sb, rc])
logistics_po.order.add_edge(ed, cc)
logistics_po.order.add_edge(ed, cl)
logistics_po.order.add_edge(cc, sb)
logistics_po.order.add_edge(cl, sb)
logistics_po.order.add_edge(sb, rc)

# Main production and export workflow
main_po = StrictPartialOrder(nodes=[
    ms, bs, cf, pc, ap, qt,
    packaging_po,
    logistics_po
])
main_po.order.add_edge(ms, bs)
main_po.order.add_edge(bs, cf)
main_po.order.add_edge(cf, pc)
main_po.order.add_edge(pc, ap)
main_po.order.add_edge(ap, qt)
main_po.order.add_edge(qt, packaging_po)
main_po.order.add_edge(packaging_po, logistics_po)

# Wrap in a loop with feedback review: after each full run of main_po, do feedback, then optionally repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[main_po, fr])