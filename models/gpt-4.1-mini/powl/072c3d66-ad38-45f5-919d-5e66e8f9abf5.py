# Generated from: 072c3d66-ad38-45f5-919d-5e66e8f9abf5.json
# Description: This process involves the meticulous restoration of antique furniture and artifacts to preserve their historical and aesthetic value. It begins with detailed condition assessment, followed by documentation and research on the item's provenance. The workflow includes careful disassembly, cleaning using specialized solvents, and stabilization of fragile components. Surface treatments such as paint consolidation or veneer repair are applied next. After structural repairs, the piece undergoes controlled drying and curing phases. The process also involves selective inpainting or gilding to restore visual continuity while respecting original materials. Finally, the item is reassembled, given a protective finish, and subjected to quality inspection before being returned to the client or museum. Each step requires specialized skills and adherence to conservation ethics to ensure authenticity and longevity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Assess_Condition = Transition(label='Assess Condition')
Document_Item = Transition(label='Document Item')
Research_Provenance = Transition(label='Research Provenance')
Disassemble_Parts = Transition(label='Disassemble Parts')
Clean_Surfaces = Transition(label='Clean Surfaces')
Stabilize_Components = Transition(label='Stabilize Components')
Repair_Veneer = Transition(label='Repair Veneer')
Consolidate_Paint = Transition(label='Consolidate Paint')
Structural_Fix = Transition(label='Structural Fix')
Dry_Components = Transition(label='Dry Components')
Cure_Treatments = Transition(label='Cure Treatments')
Inpaint_Details = Transition(label='Inpaint Details')
Apply_Gilding = Transition(label='Apply Gilding')
Reassemble_Item = Transition(label='Reassemble Item')
Protective_Finish = Transition(label='Protective Finish')
Quality_Inspect = Transition(label='Quality Inspect')

# First phase: Assessment and documentation in partial order (concurrent ordering)
# The description suggests condition assessment first, then documentation & research
# We keep Document and Research concurrent following Assess

phase1 = StrictPartialOrder(nodes=[Assess_Condition, Document_Item, Research_Provenance])
phase1.order.add_edge(Assess_Condition, Document_Item)
phase1.order.add_edge(Assess_Condition, Research_Provenance)

# Second phase: Disassembly then cleaning then stabilization (strict order)
phase2 = StrictPartialOrder(nodes=[
    Disassemble_Parts,
    Clean_Surfaces,
    Stabilize_Components
])
phase2.order.add_edge(Disassemble_Parts, Clean_Surfaces)
phase2.order.add_edge(Clean_Surfaces, Stabilize_Components)

# Third phase: Surface treatments: repair veneer or consolidate paint (choice)
surface_treatment = OperatorPOWL(operator=Operator.XOR, children=[Repair_Veneer, Consolidate_Paint])

# Fourth phase: Structural repair (strict order after surface treatment)
phase4 = Structural_Fix

# Fifth phase: Dry and Cure (strict order)
phase5 = StrictPartialOrder(nodes=[Dry_Components, Cure_Treatments])
phase5.order.add_edge(Dry_Components, Cure_Treatments)

# Sixth phase: Inpainting or gilding (choice)
inpaint_or_gilding = OperatorPOWL(operator=Operator.XOR, children=[Inpaint_Details, Apply_Gilding])

# Seventh phase: Reassemble, protective finish and quality inspection (strict order)
phase7 = StrictPartialOrder(nodes=[
    Reassemble_Item,
    Protective_Finish,
    Quality_Inspect
])
phase7.order.add_edge(Reassemble_Item, Protective_Finish)
phase7.order.add_edge(Protective_Finish, Quality_Inspect)

# Compose all phases in strict partial order respecting dependencies:
# phase1 -> phase2 -> surface_treatment -> phase4 -> phase5 -> inpaint_or_gilding -> phase7

root = StrictPartialOrder(nodes=[
    phase1,
    phase2,
    surface_treatment,
    phase4,
    phase5,
    inpaint_or_gilding,
    phase7
])
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, surface_treatment)
root.order.add_edge(surface_treatment, phase4)
root.order.add_edge(phase4, phase5)
root.order.add_edge(phase5, inpaint_or_gilding)
root.order.add_edge(inpaint_or_gilding, phase7)