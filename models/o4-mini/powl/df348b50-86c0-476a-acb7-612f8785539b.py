# Generated from: df348b50-86c0-476a-acb7-612f8785539b.json
# Description: This process involves the intricate crafting of bespoke perfumes using rare botanical extracts and traditional techniques. It begins with raw material sourcing from remote locations, followed by precise extraction methods such as enfleurage or steam distillation. The next steps include blending scent accords, aging the mixture to develop complexity, and iterative olfactory testing to ensure balance and uniqueness. Packaging is customized with artisan labels and hand-blown bottles. Quality control includes sensory panels and stability tests before limited edition release. The process demands coordination between botanists, chemists, and craftsmen, ensuring each perfume reflects distinctive artistry and exceptional quality.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
mat_src = Transition(label="Material Sourcing")
botan_harv = Transition(label="Botanical Harvest")
extr_phase = Transition(label="Extraction Phase")
accord_blend = Transition(label="Accord Blending")
olf_test = Transition(label="Olfactory Testing")
batch_mix = Transition(label="Batch Mixing")
aging_proc = Transition(label="Aging Process")
stability_check = Transition(label="Stability Check")
sensory_panel = Transition(label="Sensory Panel")
label_design = Transition(label="Label Design")
bottle_crafting = Transition(label="Bottle Crafting")
quality_review = Transition(label="Quality Review")
packaging_final = Transition(label="Packaging Final")
inventory_update = Transition(label="Inventory Update")
market_launch = Transition(label="Market Launch")

# Loop for iterative olfactory testing and remixing
test_mix_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[olf_test, batch_mix]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    mat_src,
    botan_harv,
    extr_phase,
    accord_blend,
    test_mix_loop,
    aging_proc,
    sensory_panel,
    stability_check,
    quality_review,
    label_design,
    bottle_crafting,
    packaging_final,
    inventory_update,
    market_launch
])

# Define the control‐flow edges
root.order.add_edge(mat_src, botan_harv)
root.order.add_edge(botan_harv, extr_phase)
root.order.add_edge(extr_phase, accord_blend)
root.order.add_edge(accord_blend, test_mix_loop)
root.order.add_edge(test_mix_loop, aging_proc)

root.order.add_edge(aging_proc, sensory_panel)
root.order.add_edge(aging_proc, stability_check)
root.order.add_edge(sensory_panel, quality_review)
root.order.add_edge(stability_check, quality_review)

root.order.add_edge(quality_review, label_design)
root.order.add_edge(quality_review, bottle_crafting)
root.order.add_edge(label_design, packaging_final)
root.order.add_edge(bottle_crafting, packaging_final)

root.order.add_edge(packaging_final, inventory_update)
root.order.add_edge(inventory_update, market_launch)