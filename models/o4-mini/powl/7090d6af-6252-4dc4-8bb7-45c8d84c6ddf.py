# Generated from: 7090d6af-6252-4dc4-8bb7-45c8d84c6ddf.json
# Description: This process involves the intricate steps required to craft a bespoke artisanal perfume from raw botanical ingredients. It begins with sourcing rare flowers and essential oils, followed by precise extraction techniques including enfleurage and steam distillation. The extracted essences are then carefully blended in varying proportions to create unique scent profiles. Each blend undergoes maturation in controlled environments to allow scent harmonization. Quality assessment is performed through blind olfactory tests by expert perfumers. Finally, the perfume is bottled in handcrafted containers, labeled, and prepared for exclusive boutique distribution. This process combines traditional craftsmanship with modern quality controls to produce a distinctive, high-value fragrance product.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
source = Transition(label='Source Botanicals')
extract = Transition(label='Extract Essences')
steam = Transition(label='Steam Distill')
enfleurage = Transition(label='Enfleurage Step')
blend = Transition(label='Blend Scents')
mature = Transition(label='Mature Blend')

test_profiles = Transition(label='Test Profiles')
olfactory_test = Transition(label='Olfactory Test')
quality_check = Transition(label='Quality Check')
adjust_formula = Transition(label='Adjust Formula')
# separate instance for re-maturation in the loop
mature_again = Transition(label='Mature Blend')

bottle_perfume = Transition(label='Bottle Perfume')
label_design = Transition(label='Label Design')
package_goods = Transition(label='Package Goods')
distribute_stock = Transition(label='Distribute Stock')
record_batch = Transition(label='Record Batch')

# LOOP node: perform tests, if unsatisfactory adjust & re-mature then repeat tests
body = StrictPartialOrder(nodes=[test_profiles, olfactory_test, quality_check])
body.order.add_edge(test_profiles, olfactory_test)
body.order.add_edge(olfactory_test, quality_check)

redo = StrictPartialOrder(nodes=[adjust_formula, mature_again])
redo.order.add_edge(adjust_formula, mature_again)

loop = OperatorPOWL(operator=Operator.LOOP, children=[body, redo])

# Main partial order
root = StrictPartialOrder(nodes=[
    source, extract, steam, enfleurage, blend, mature,
    loop,
    bottle_perfume, label_design, package_goods, distribute_stock, record_batch
])
root.order.add_edge(source, extract)
root.order.add_edge(extract, steam)
root.order.add_edge(extract, enfleurage)
root.order.add_edge(steam, blend)
root.order.add_edge(enfleurage, blend)
root.order.add_edge(blend, mature)
root.order.add_edge(mature, loop)
root.order.add_edge(loop, bottle_perfume)
root.order.add_edge(bottle_perfume, label_design)
root.order.add_edge(label_design, package_goods)
root.order.add_edge(package_goods, distribute_stock)
root.order.add_edge(distribute_stock, record_batch)