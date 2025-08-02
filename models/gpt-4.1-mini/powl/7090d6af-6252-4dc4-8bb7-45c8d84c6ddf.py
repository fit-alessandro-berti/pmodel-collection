# Generated from: 7090d6af-6252-4dc4-8bb7-45c8d84c6ddf.json
# Description: This process involves the intricate steps required to craft a bespoke artisanal perfume from raw botanical ingredients. It begins with sourcing rare flowers and essential oils, followed by precise extraction techniques including enfleurage and steam distillation. The extracted essences are then carefully blended in varying proportions to create unique scent profiles. Each blend undergoes maturation in controlled environments to allow scent harmonization. Quality assessment is performed through blind olfactory tests by expert perfumers. Finally, the perfume is bottled in handcrafted containers, labeled, and prepared for exclusive boutique distribution. This process combines traditional craftsmanship with modern quality controls to produce a distinctive, high-value fragrance product.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
source_botanicals = Transition(label='Source Botanicals')
extract_essences = Transition(label='Extract Essences')
steam_distill = Transition(label='Steam Distill')
enfleurage_step = Transition(label='Enfleurage Step')
blend_scents = Transition(label='Blend Scents')
mature_blend = Transition(label='Mature Blend')
test_profiles = Transition(label='Test Profiles')
quality_check = Transition(label='Quality Check')
olfactory_test = Transition(label='Olfactory Test')
adjust_formula = Transition(label='Adjust Formula')
bottle_perfume = Transition(label='Bottle Perfume')
label_design = Transition(label='Label Design')
package_goods = Transition(label='Package Goods')
distribute_stock = Transition(label='Distribute Stock')
record_batch = Transition(label='Record Batch')

# Extraction step: choice between 'Steam Distill' and 'Enfleurage Step' after 'Extract Essences'
extract_choice = OperatorPOWL(operator=Operator.XOR, children=[steam_distill, enfleurage_step])

# Loop for testing and adjusting: (Test Profiles, loop body (Adjust Formula then Test Profiles))
test_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_profiles, adjust_formula])

# Quality assessment: Quality Check then Olfactory Test then possibility to loop test_loop again
# Model this as a partial order:
# quality_check --> olfactory_test --> test_loop
# test_loop loops back until exit
quality_seq = StrictPartialOrder(nodes=[quality_check, olfactory_test, test_loop])
quality_seq.order.add_edge(quality_check, olfactory_test)
quality_seq.order.add_edge(olfactory_test, test_loop)

# Blending and maturation occur before quality assessment
blend_and_mature = StrictPartialOrder(nodes=[blend_scents, mature_blend])
blend_and_mature.order.add_edge(blend_scents, mature_blend)

# Packaging steps are sequential
packaging = StrictPartialOrder(nodes=[bottle_perfume, label_design, package_goods, distribute_stock])
packaging.order.add_edge(bottle_perfume, label_design)
packaging.order.add_edge(label_design, package_goods)
packaging.order.add_edge(package_goods, distribute_stock)

# Entire process partial order nodes:
# 1. Source Botanicals --> Extract Essences --> extract_choice (Steam Distill or Enfleurage)
# 2. extract_choice --> blend_and_mature (Blend Scents --> Mature Blend)
# 3. blend_and_mature --> quality_seq (Quality Check etc)
# 4. quality_seq --> packaging (Bottle ... Distribute)
# 5. After packaging --> Record Batch

root = StrictPartialOrder(nodes=[
    source_botanicals,
    extract_essences,
    extract_choice,
    blend_and_mature,
    quality_seq,
    packaging,
    record_batch
])

root.order.add_edge(source_botanicals, extract_essences)
root.order.add_edge(extract_essences, extract_choice)
root.order.add_edge(extract_choice, blend_and_mature)
root.order.add_edge(blend_and_mature, quality_seq)
root.order.add_edge(quality_seq, packaging)
root.order.add_edge(packaging, record_batch)