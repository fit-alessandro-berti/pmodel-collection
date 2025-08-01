# Generated from: 84288aef-d199-4f10-b7be-47b149d16b94.json
# Description: This process outlines the intricate steps involved in restoring vintage musical instruments to their former glory while preserving original materials and craftsmanship. The workflow involves detailed assessment of the instrument's condition, sourcing rare and period-accurate components, careful disassembly, cleaning, structural repairs, refinishing using traditional methods, fine tuning of acoustics, and final aesthetic treatments. Each step requires specialized skills to balance authenticity with functional improvement, ensuring that the restored instrument not only looks as it did originally but also performs at professional standards. Documentation and provenance verification are integral, along with customer consultation and post-restoration maintenance planning, making this restoration process both an art and a science.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Initial_Survey = Transition(label='Initial Survey')
Condition_Report = Transition(label='Condition Report')
Provenance_Check = Transition(label='Provenance Check')
Parts_Sourcing = Transition(label='Parts Sourcing')
Component_Removal = Transition(label='Component Removal')
Surface_Cleaning = Transition(label='Surface Cleaning')
Wood_Repair = Transition(label='Wood Repair')
Metalwork_Fix = Transition(label='Metalwork Fix')
Finish_Stripping = Transition(label='Finish Stripping')
Traditional_Stain = Transition(label='Traditional Stain')
Structural_Rebuild = Transition(label='Structural Rebuild')
Acoustic_Tuning = Transition(label='Acoustic Tuning')
Hardware_Refit = Transition(label='Hardware Refit')
Final_Polish = Transition(label='Final Polish')
Quality_Review = Transition(label='Quality Review')
Customer_Demo = Transition(label='Customer Demo')
Maintenance_Plan = Transition(label='Maintenance Plan')

# Partial order 1: Initial survey, condition report, provenance check in sequence
po_initial = StrictPartialOrder(nodes=[Initial_Survey, Condition_Report, Provenance_Check])
po_initial.order.add_edge(Initial_Survey, Condition_Report)
po_initial.order.add_edge(Condition_Report, Provenance_Check)

# Parts sourcing depends on Provenance Check
po_parts = StrictPartialOrder(nodes=[Parts_Sourcing])
# later linked

# Disassembly and cleaning branch (can be concurrent tasks)
po_disassembly = StrictPartialOrder(
    nodes=[Component_Removal, Surface_Cleaning, Wood_Repair, Metalwork_Fix]
)
# order Component Removal before all repairs and cleaning
po_disassembly.order.add_edge(Component_Removal, Surface_Cleaning)
po_disassembly.order.add_edge(Component_Removal, Wood_Repair)
po_disassembly.order.add_edge(Component_Removal, Metalwork_Fix)
# Surface Cleaning can run in parallel with Wood Repair and Metalwork Fix (no order edges between them)

# Refinishing branch order: Finish Stripping -> Traditional Stain -> Structural Rebuild
po_refinish = StrictPartialOrder(nodes=[Finish_Stripping, Traditional_Stain, Structural_Rebuild])
po_refinish.order.add_edge(Finish_Stripping, Traditional_Stain)
po_refinish.order.add_edge(Traditional_Stain, Structural_Rebuild)

# Tuning and hardware refit and polish in sequence
po_final_tuning = StrictPartialOrder(
    nodes=[Acoustic_Tuning, Hardware_Refit, Final_Polish]
)
po_final_tuning.order.add_edge(Acoustic_Tuning, Hardware_Refit)
po_final_tuning.order.add_edge(Hardware_Refit, Final_Polish)

# Quality review depends on polishes done
po_quality = StrictPartialOrder(nodes=[Quality_Review])
# later linked

# Customer demo and maintenance plan in parallel, both after Quality Review
po_customer = StrictPartialOrder(nodes=[Customer_Demo, Maintenance_Plan])
# parallel, no order edge

# Assemble sub-processes together with dependencies

# After Provenance Check: Parts Sourcing starts
# After Parts Sourcing: disassembly & cleaning can start concurrently
po_after_provenance = StrictPartialOrder(
    nodes=[po_parts, po_disassembly]
)
po_after_provenance.order.add_edge(po_parts, po_disassembly)

# After disassembly & cleaning, refinishing starts
po_after_disassembly = StrictPartialOrder(
    nodes=[po_disassembly, po_refinish]
)
po_after_disassembly.order.add_edge(po_disassembly, po_refinish)

# After refinishing, final tuning etc.
po_after_refinish = StrictPartialOrder(
    nodes=[po_refinish, po_final_tuning]
)
po_after_refinish.order.add_edge(po_refinish, po_final_tuning)

# After final polishing: quality review
po_after_final = StrictPartialOrder(
    nodes=[po_final_tuning, po_quality]
)
po_after_final.order.add_edge(po_final_tuning, po_quality)

# After quality review: customer demo and maintenance plan parallel
po_after_quality = StrictPartialOrder(
    nodes=[po_quality, po_customer]
)
po_after_quality.order.add_edge(po_quality, po_customer)

# Build incrementally from start to finish

# Combine initial survey chain with parts sourcing
po_init_parts = StrictPartialOrder(
    nodes=[po_initial, po_parts]
)
po_init_parts.order.add_edge(po_initial, po_parts)

# Combine po_init_parts with disassembly (parts sourcing before disassembly)
po_init_to_disassembly = StrictPartialOrder(
    nodes=[po_init_parts, po_disassembly]
)
po_init_to_disassembly.order.add_edge(po_init_parts, po_disassembly)
# Actually parts sourcing is inside po_init_parts and disassembly after parts sourcing,
# to keep precision, just chain po_init_parts --> po_disassembly

# But we modeled a bit differently above, prefer connecting all parts carefully:

# Ultimately, build final root PO combining all steps properly:
# Steps:
# 1) Initial Survey -> Condition Report -> Provenance Check
# 2) Provenance Check -> Parts Sourcing
# 3) Parts Sourcing -> Component Removal
# 4) Component Removal -> Surface Cleaning, Wood Repair, Metalwork Fix (concurrent)
# 5) All repairs and cleaning done -> Finish Stripping
# 6) Finish Stripping -> Traditional Stain -> Structural Rebuild
# 7) Structural Rebuild -> Acoustic Tuning -> Hardware Refit -> Final Polish
# 8) Final Polish -> Quality Review
# 9) Quality Review -> Customer Demo and Maintenance Plan (parallel)

# We'll represent the repair/cleaning step as a PO with the Component Removal before the 3 other branches concurrent
po_repair_clean = StrictPartialOrder(
    nodes=[Component_Removal, Surface_Cleaning, Wood_Repair, Metalwork_Fix]
)
po_repair_clean.order.add_edge(Component_Removal, Surface_Cleaning)
po_repair_clean.order.add_edge(Component_Removal, Wood_Repair)
po_repair_clean.order.add_edge(Component_Removal, Metalwork_Fix)

# Top-level PO nodes (activities and POs)
root = StrictPartialOrder(
    nodes=[
        Initial_Survey,
        Condition_Report,
        Provenance_Check,
        Parts_Sourcing,
        po_repair_clean,
        Finish_Stripping,
        Traditional_Stain,
        Structural_Rebuild,
        Acoustic_Tuning,
        Hardware_Refit,
        Final_Polish,
        Quality_Review,
        Customer_Demo,
        Maintenance_Plan,
    ]
)

# Add order edges according to dependencies
root.order.add_edge(Initial_Survey, Condition_Report)
root.order.add_edge(Condition_Report, Provenance_Check)
root.order.add_edge(Provenance_Check, Parts_Sourcing)
root.order.add_edge(Parts_Sourcing, po_repair_clean)
# Component Removal inside po_repair_clean occurs before Surface Cleaning, Wood Repair, Metalwork Fix already set internally

root.order.add_edge(po_repair_clean, Finish_Stripping)
root.order.add_edge(Finish_Stripping, Traditional_Stain)
root.order.add_edge(Traditional_Stain, Structural_Rebuild)
root.order.add_edge(Structural_Rebuild, Acoustic_Tuning)
root.order.add_edge(Acoustic_Tuning, Hardware_Refit)
root.order.add_edge(Hardware_Refit, Final_Polish)
root.order.add_edge(Final_Polish, Quality_Review)
root.order.add_edge(Quality_Review, Customer_Demo)
root.order.add_edge(Quality_Review, Maintenance_Plan)