# Generated from: 072c3d66-ad38-45f5-919d-5e66e8f9abf5.json
# Description: This process involves the meticulous restoration of antique furniture and artifacts to preserve their historical and aesthetic value. It begins with detailed condition assessment, followed by documentation and research on the item's provenance. The workflow includes careful disassembly, cleaning using specialized solvents, and stabilization of fragile components. Surface treatments such as paint consolidation or veneer repair are applied next. After structural repairs, the piece undergoes controlled drying and curing phases. The process also involves selective inpainting or gilding to restore visual continuity while respecting original materials. Finally, the item is reassembled, given a protective finish, and subjected to quality inspection before being returned to the client or museum. Each step requires specialized skills and adherence to conservation ethics to ensure authenticity and longevity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
assess = Transition(label="Assess Condition")
document = Transition(label="Document Item")
research = Transition(label="Research Provenance")
disassemble = Transition(label="Disassemble Parts")
clean = Transition(label="Clean Surfaces")
stabilize = Transition(label="Stabilize Components")
repair_veneer = Transition(label="Repair Veneer")
consolidate_paint = Transition(label="Consolidate Paint")
structural_fix = Transition(label="Structural Fix")
dry = Transition(label="Dry Components")
cure = Transition(label="Cure Treatments")
inpaint = Transition(label="Inpaint Details")
gild = Transition(label="Apply Gilding")
reassemble = Transition(label="Reassemble Item")
protect = Transition(label="Protective Finish")
inspect = Transition(label="Quality Inspect")

# Model the choice between inpainting and gilding
surface_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[inpaint, gild]
)

# Build the strict partial order
root = StrictPartialOrder(
    nodes=[
        assess, document, research, disassemble, clean, stabilize,
        repair_veneer, consolidate_paint, structural_fix,
        dry, cure, surface_choice,
        reassemble, protect, inspect
    ]
)

# Add the precedence relations
o = root.order
o.add_edge(assess, document)
o.add_edge(document, research)
o.add_edge(research, disassemble)
o.add_edge(disassemble, clean)
o.add_edge(clean, stabilize)

# Surface treatments (can be concurrent), both must complete before structural fix
o.add_edge(stabilize, repair_veneer)
o.add_edge(stabilize, consolidate_paint)
o.add_edge(repair_veneer, structural_fix)
o.add_edge(consolidate_paint, structural_fix)

# Structural repair and cure phases
o.add_edge(structural_fix, dry)
o.add_edge(dry, cure)

# Choice between inpainting and gilding, then reassembly and finish
o.add_edge(cure, surface_choice)
o.add_edge(surface_choice, reassemble)
o.add_edge(reassemble, protect)
o.add_edge(protect, inspect)