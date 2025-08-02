# Generated from: 1a7c9004-7fa7-47c6-8648-79992abf5bea.json
# Description: This process details the intricate steps involved in sourcing, producing, and distributing artisan cheese with a focus on maintaining quality and authenticity. It begins with selecting rare milk sources, followed by specialized fermentation and aging stages. Quality control includes sensory evaluation and microbial testing to ensure safety and flavor consistency. Packaging is done in eco-friendly materials, with customized labeling reflecting the cheese’s origin. Distribution channels are unique, targeting niche gourmet retailers and direct-to-consumer subscriptions. Throughout the process, traceability and sustainability reporting are integral to meet regulatory and consumer demands, making this supply chain highly specialized and complex.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

MS = Transition(label='Milk Sourcing')

# Fermentation stage: Fermentation Start -> Curd Cutting -> Whey Removal -> Molding Cheese -> Salting Process -> Aging Control
FS = Transition(label='Fermentation Start')
CC = Transition(label='Curd Cutting')
WR = Transition(label='Whey Removal')
MC = Transition(label='Molding Cheese')
SP = Transition(label='Salting Process')
AC = Transition(label='Aging Control')
fermentation_po = StrictPartialOrder(nodes=[FS, CC, WR, MC, SP, AC])
fermentation_po.order.add_edge(FS, CC)
fermentation_po.order.add_edge(CC, WR)
fermentation_po.order.add_edge(WR, MC)
fermentation_po.order.add_edge(MC, SP)
fermentation_po.order.add_edge(SP, AC)

# Quality Testing activities: Sensory Review and Microbial Check in parallel, then Quality Testing sums both
SR = Transition(label='Sensory Review')
MCk = Transition(label='Microbial Check')
quality_review = StrictPartialOrder(nodes=[SR, MCk])
# These two are concurrent (no order edges)
QT = Transition(label='Quality Testing')
# Quality Testing after both reviews
quality_po = StrictPartialOrder(nodes=[quality_review, QT])
quality_po.order.add_edge(quality_review, QT)

# Packaging: Eco Packaging followed by Label Printing
EP = Transition(label='Eco Packaging')
LP = Transition(label='Label Printing')
packaging_po = StrictPartialOrder(nodes=[EP, LP])
packaging_po.order.add_edge(EP, LP)

# Distribution: choice between Niche Shipping and Order Processing (which leads to nothing else here)
NS = Transition(label='Niche Shipping')
OP = Transition(label='Order Processing')
distribution_xor = OperatorPOWL(operator=Operator.XOR, children=[NS, OP])

# Sustainability Audit (traceability, reporting), concurrent with distribution
SA = Transition(label='Sustainability Audit')

# Build overall partial order combining all:
# Milk Sourcing -> Fermentation -> Quality Testing -> Packaging -> (Distribution || Sustainability Audit)
# Distribution and Sustainability Audit concurrent (no order)
# For the "Quality Testing" we actually have Enclosing it properly in the po:
# Quality review is a PO no order between SR/MCk; we need to embed that in a node for order with QT:
# But our strict partial order nodes are only Transitions and Operators,
# So treat quality_review as an OperatorPOWL of concurrency is not given => better do a PO with SR and MCk unordered, then QT after

quality_reviews_po = StrictPartialOrder(nodes=[SR, MCk])
# no edges between SR and MCk, concurrent

quality_full_po = StrictPartialOrder(nodes=[quality_reviews_po, QT])
quality_full_po.order.add_edge(quality_reviews_po, QT)

# Since StrictPartialOrder nodes must be Transitions or OperatorPOWL or StrictPartialOrder, the nesting is allowed

# Now chain the sequence:

root = StrictPartialOrder(nodes=[MS, fermentation_po, quality_full_po, packaging_po, distribution_xor, SA])

root.order.add_edge(MS, fermentation_po)
root.order.add_edge(fermentation_po, quality_full_po)
root.order.add_edge(quality_full_po, packaging_po)
root.order.add_edge(packaging_po, distribution_xor)
# SA concurrent with distribution_xor, so no order edge between them