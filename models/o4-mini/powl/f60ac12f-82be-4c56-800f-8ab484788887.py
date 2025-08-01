# Generated from: f60ac12f-82be-4c56-800f-8ab484788887.json
# Description: This process describes the end-to-end supply chain for artisan cheese production and distribution, starting from raw milk sourcing to aging, quality testing, packaging, and delivery. It includes unique steps like microbial culture blending, environmental condition monitoring, and niche market allocation. The process ensures traceability, maintains artisanal quality standards, and incorporates customer feedback loops for continuous improvement while coordinating with local farms, specialty retailers, and export partners.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ms = Transition(label='Milk Sourcing')
cb = Transition(label='Culture Blending')
mp = Transition(label='Milk Pasteurize')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Drain')
mi = Transition(label='Mold Inoculate')
pc = Transition(label='Press Cheese')
sb = Transition(label='Salt Brine')
am = Transition(label='Age Monitor')
qt = Transition(label='Quality Test')
pp = Transition(label='Packaging Prep')
ld = Transition(label='Label Design')
oa = Transition(label='Order Allocation')
rs = Transition(label='Retail Sync')
ta = Transition(label='Transport Arrange')
cr = Transition(label='Customer Review')
fa = Transition(label='Feedback Analyze')

# 1) Loop for aging & quality testing: do Age Monitor, then either exit or do Quality Test and repeat
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[am, qt])

# 2) Exclusive choice for distribution channel: either Retail Sync or Transport Arrange
xor_distribution = OperatorPOWL(operator=Operator.XOR, children=[rs, ta])

# 3) Main straight‐line process (from milk sourcing up to customer review)
po_main = StrictPartialOrder(nodes=[
    ms, cb, mp, cc, wd, mi, pc, sb,
    loop_aging,
    pp, ld, oa,
    xor_distribution,
    cr
])
po_main.order.add_edge(ms, cb)
po_main.order.add_edge(cb, mp)
po_main.order.add_edge(mp, cc)
po_main.order.add_edge(cc, wd)
po_main.order.add_edge(wd, mi)
po_main.order.add_edge(mi, pc)
po_main.order.add_edge(pc, sb)
po_main.order.add_edge(sb, loop_aging)
po_main.order.add_edge(loop_aging, pp)
po_main.order.add_edge(pp, ld)
po_main.order.add_edge(ld, oa)
po_main.order.add_edge(oa, xor_distribution)
po_main.order.add_edge(xor_distribution, cr)

# 4) Top‐level feedback loop: run the main process once, then optionally analyze feedback and repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[po_main, fa])