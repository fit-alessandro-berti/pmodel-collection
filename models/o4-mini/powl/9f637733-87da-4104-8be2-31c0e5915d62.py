# Generated from: 9f637733-87da-4104-8be2-31c0e5915d62.json
# Description: This process outlines the intricate steps involved in restoring vintage musical instruments to playable and collectible condition. It begins with initial assessment, followed by detailed documentation of damage and provenance verification. Specialized cleaning techniques are applied to remove years of grime without harming original finishes. Structural repairs require precise woodworking or metalwork to preserve authenticity. Acoustic tuning is performed to balance sound quality. Custom replacement parts are fabricated when originals are unavailable, ensuring historical accuracy. Final polishing enhances aesthetic appeal, while quality control verifies functionality. The process concludes with archival recording of restoration details and client handover, maintaining a comprehensive history for collectors and musicians alike.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
initial_assess = Transition(label='Initial Assess')
damage_doc     = Transition(label='Damage Document')
prov_check     = Transition(label='Provenance Check')
surface_clean  = Transition(label='Surface Clean')
finish_protect = Transition(label='Finish Protect')
struct_repair  = Transition(label='Structural Repair')
wood_fix       = Transition(label='Woodwork Fix')
metal_fix      = Transition(label='Metalwork Fix')
acoustic_tune  = Transition(label='Acoustic Tune')
sound_test     = Transition(label='Sound Test')
part_fab       = Transition(label='Part Fabricate')
polish_finish  = Transition(label='Polish Finish')
quality_insp   = Transition(label='Quality Inspect')
archive_rec    = Transition(label='Archive Record')
client_handover= Transition(label='Client Handover')
skip           = SilentTransition()  # for optional fabrication

# Choice: either Woodwork Fix or Metalwork Fix after structural repair
repair_choice = OperatorPOWL(operator=Operator.XOR, children=[wood_fix, metal_fix])

# Choice: either fabricate parts or skip if originals are available
fabricate_choice = OperatorPOWL(operator=Operator.XOR, children=[part_fab, skip])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    initial_assess,
    damage_doc,
    prov_check,
    surface_clean,
    finish_protect,
    struct_repair,
    repair_choice,
    acoustic_tune,
    sound_test,
    fabricate_choice,
    polish_finish,
    quality_insp,
    archive_rec,
    client_handover
])

# Define the control‐flow (partial order) dependencies
root.order.add_edge(initial_assess,   damage_doc)
root.order.add_edge(damage_doc,       prov_check)
root.order.add_edge(prov_check,       surface_clean)
root.order.add_edge(surface_clean,    finish_protect)
root.order.add_edge(finish_protect,   struct_repair)
root.order.add_edge(struct_repair,    repair_choice)
root.order.add_edge(repair_choice,    acoustic_tune)
root.order.add_edge(acoustic_tune,    sound_test)
root.order.add_edge(sound_test,       fabricate_choice)
root.order.add_edge(fabricate_choice, polish_finish)
root.order.add_edge(polish_finish,    quality_insp)
root.order.add_edge(quality_insp,     archive_rec)
root.order.add_edge(archive_rec,      client_handover)