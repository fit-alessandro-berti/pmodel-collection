# Generated from: df348b50-86c0-476a-acb7-612f8785539b.json
# Description: This process involves the intricate crafting of bespoke perfumes using rare botanical extracts and traditional techniques. It begins with raw material sourcing from remote locations, followed by precise extraction methods such as enfleurage or steam distillation. The next steps include blending scent accords, aging the mixture to develop complexity, and iterative olfactory testing to ensure balance and uniqueness. Packaging is customized with artisan labels and hand-blown bottles. Quality control includes sensory panels and stability tests before limited edition release. The process demands coordination between botanists, chemists, and craftsmen, ensuring each perfume reflects distinctive artistry and exceptional quality.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Material_Sourcing = Transition(label='Material Sourcing')
Botanical_Harvest = Transition(label='Botanical Harvest')
Extraction_Phase = Transition(label='Extraction Phase')
Accord_Blending = Transition(label='Accord Blending')
Olfactory_Testing = Transition(label='Olfactory Testing')
Aging_Process = Transition(label='Aging Process')
Stability_Check = Transition(label='Stability Check')
Sensory_Panel = Transition(label='Sensory Panel')
Label_Design = Transition(label='Label Design')
Bottle_Crafting = Transition(label='Bottle Crafting')
Batch_Mixing = Transition(label='Batch Mixing')
Quality_Review = Transition(label='Quality Review')
Packaging_Final = Transition(label='Packaging Final')
Inventory_Update = Transition(label='Inventory Update')
Market_Launch = Transition(label='Market Launch')

# Olfactory testing loop: after Aging_Process, repeat Olfactory_Testing and Batch_Mixing until satisfied
# Loop: * (Aging_Process, PO=(nodes=[Batch_Mixing, Olfactory_Testing], order={Batch_Mixing-->Olfactory_Testing}))
feedback_order = StrictPartialOrder(nodes=[Batch_Mixing, Olfactory_Testing])
feedback_order.order.add_edge(Batch_Mixing, Olfactory_Testing)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Process, feedback_order])

# Quality control partial order: Stability_Check and Sensory_Panel can be concurrent before Quality_Review
quality_control = StrictPartialOrder(
    nodes=[Stability_Check, Sensory_Panel, Quality_Review]
)
quality_control.order.add_edge(Stability_Check, Quality_Review)
quality_control.order.add_edge(Sensory_Panel, Quality_Review)

# Packaging preparation partial order: Label_Design and Bottle_Crafting are concurrent before Packaging_Final
packaging_preparation = StrictPartialOrder(
    nodes=[Label_Design, Bottle_Crafting, Packaging_Final]
)
packaging_preparation.order.add_edge(Label_Design, Packaging_Final)
packaging_preparation.order.add_edge(Bottle_Crafting, Packaging_Final)

# Beginning sourcing and harvesting partial order: Material_Sourcing followed by Botanical_Harvest
sourcing = StrictPartialOrder(
    nodes=[Material_Sourcing, Botanical_Harvest]
)
sourcing.order.add_edge(Material_Sourcing, Botanical_Harvest)

# Extraction follows harvesting
extraction_after_harvest = StrictPartialOrder(
    nodes=[Botanical_Harvest, Extraction_Phase]
)
extraction_after_harvest.order.add_edge(Botanical_Harvest, Extraction_Phase)

# Accord Blending after Extraction_Phase
blending_after_extraction = StrictPartialOrder(
    nodes=[Extraction_Phase, Accord_Blending]
)
blending_after_extraction.order.add_edge(Extraction_Phase, Accord_Blending)

# Connect sourcing, extraction, blending in a single partial order
first_phases = StrictPartialOrder(
    nodes=[Material_Sourcing, Botanical_Harvest, Extraction_Phase, Accord_Blending]
)
first_phases.order.add_edge(Material_Sourcing, Botanical_Harvest)
first_phases.order.add_edge(Botanical_Harvest, Extraction_Phase)
first_phases.order.add_edge(Extraction_Phase, Accord_Blending)

# Compose the full process partial order stepwise

# After Accord Blending, start feedback loop (aging+testing)
after_blending = StrictPartialOrder(
    nodes=[Accord_Blending, feedback_loop]
)
after_blending.order.add_edge(Accord_Blending, feedback_loop)

# After feedback loop, start quality control
after_feedback = StrictPartialOrder(
    nodes=[feedback_loop, quality_control]
)
after_feedback.order.add_edge(feedback_loop, quality_control)

# After quality control, packaging preparation
after_quality = StrictPartialOrder(
    nodes=[quality_control, packaging_preparation]
)
after_quality.order.add_edge(quality_control, packaging_preparation)

# After packaging preparation, Inventory_Update then Market_Launch
final_steps = StrictPartialOrder(
    nodes=[Packaging_Final, Inventory_Update, Market_Launch]
)
final_steps.order.add_edge(Packaging_Final, Inventory_Update)
final_steps.order.add_edge(Inventory_Update, Market_Launch)

# Now we join all phases making sure dependencies are respected:
# first_phases --> after_blending --> after_feedback --> after_quality --> final_steps

# To merge all nodes and edges, put them all in one StrictPartialOrder and add all edges

all_nodes = [
    Material_Sourcing, Botanical_Harvest, Extraction_Phase, Accord_Blending,
    feedback_loop,
    Stability_Check, Sensory_Panel, Quality_Review,
    Label_Design, Bottle_Crafting, Packaging_Final,
    Inventory_Update, Market_Launch,
    Batch_Mixing, Olfactory_Testing,
    Aging_Process,
]

root = StrictPartialOrder(nodes=all_nodes)

# Add edges from first_phases
root.order.add_edge(Material_Sourcing, Botanical_Harvest)
root.order.add_edge(Botanical_Harvest, Extraction_Phase)
root.order.add_edge(Extraction_Phase, Accord_Blending)

# Accord_Blending -> feedback_loop (feedback loop = Aging_Process plus iteration)
root.order.add_edge(Accord_Blending, feedback_loop)

# Edges inside feedback_loop:
# Loop children: Aging_Process and partial order of {Batch_Mixing-->Olfactory_Testing}
root.order.add_edge(Batch_Mixing, Olfactory_Testing)

# feedback_loop is a special operator node, no further edge needed inside root for looping semantics

# feedback_loop -> quality_control nodes
root.order.add_edge(feedback_loop, Stability_Check)
root.order.add_edge(feedback_loop, Sensory_Panel)

# quality control edges
root.order.add_edge(Stability_Check, Quality_Review)
root.order.add_edge(Sensory_Panel, Quality_Review)

# quality_control -> packaging_preparation nodes:
root.order.add_edge(Quality_Review, Label_Design)
root.order.add_edge(Quality_Review, Bottle_Crafting)

# packaging_preparation edges
root.order.add_edge(Label_Design, Packaging_Final)
root.order.add_edge(Bottle_Crafting, Packaging_Final)

# packaging_final -> inventory_update -> market_launch
root.order.add_edge(Packaging_Final, Inventory_Update)
root.order.add_edge(Inventory_Update, Market_Launch)