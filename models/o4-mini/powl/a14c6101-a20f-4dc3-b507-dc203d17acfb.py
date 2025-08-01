# Generated from: a14c6101-a20f-4dc3-b507-dc203d17acfb.json
# Description: This process involves the meticulous restoration of vintage mechanical watches, combining expertise in horology, materials science, and historical research. The workflow begins with an initial inspection to assess the watch’s condition and authenticity, followed by disassembly where each component is carefully cataloged. Cleaning involves ultrasonic baths and gentle chemical treatments tailored to delicate parts. Repair focuses on fabricating or sourcing rare replacement components, including gears and springs, often requiring custom machining or handcrafting. Reassembly demands precision alignment and lubrication using specialized oils. The process includes timing calibration to ensure accuracy, aesthetic restoration of dials and hands, and final quality control under various conditions. Documentation of provenance and restoration steps is maintained for collectors. This atypical process blends technical skill with conservation ethics, ensuring the watch's functional revival while preserving its historical integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
initial_inspect   = Transition(label='Initial Inspect')
disassemble_parts = Transition(label='Disassemble Parts')
component_catalog = Transition(label='Component Catalog')
ultrasonic_clean  = Transition(label='Ultrasonic Clean')
chemical_treat    = Transition(label='Chemical Treat')
fabricate_gears   = Transition(label='Fabricate Gears')
source_springs    = Transition(label='Source Springs')
handcraft_parts   = Transition(label='Handcraft Parts')
align_mechanism   = Transition(label='Align Mechanism')
apply_lubricate   = Transition(label='Apply Lubricate')
final_assembly    = Transition(label='Final Assembly')
calibrate_timing  = Transition(label='Calibrate Timing')
restore_dial      = Transition(label='Restore Dial')
refinish_hands    = Transition(label='Refinish Hands')
quality_control   = Transition(label='Quality Control')
test_function     = Transition(label='Test Function')
document_history  = Transition(label='Document History')

# Build the partial order
root = StrictPartialOrder(nodes=[
    initial_inspect, disassemble_parts, component_catalog,
    ultrasonic_clean, chemical_treat,
    fabricate_gears, source_springs, handcraft_parts,
    align_mechanism, apply_lubricate,
    final_assembly, calibrate_timing,
    restore_dial, refinish_hands,
    quality_control, test_function, document_history
])

# Define the control-flow dependencies
# Inspection → Disassembly → Cataloging
root.order.add_edge(initial_inspect,   disassemble_parts)
root.order.add_edge(disassemble_parts, component_catalog)

# Cataloging → Cleaning (parallel)
root.order.add_edge(component_catalog, ultrasonic_clean)
root.order.add_edge(component_catalog, chemical_treat)

# Cleaning → Repair (parallel)
for clean in [ultrasonic_clean, chemical_treat]:
    root.order.add_edge(clean, fabricate_gears)
    root.order.add_edge(clean, source_springs)
    root.order.add_edge(clean, handcraft_parts)

# Repair → Alignment → Lubrication → Final Assembly
for repair in [fabricate_gears, source_springs, handcraft_parts]:
    root.order.add_edge(repair, align_mechanism)
root.order.add_edge(align_mechanism, apply_lubricate)
root.order.add_edge(apply_lubricate, final_assembly)

# Final Assembly → Calibration → Aesthetic Restoration (parallel)
root.order.add_edge(final_assembly,   calibrate_timing)
root.order.add_edge(calibrate_timing, restore_dial)
root.order.add_edge(calibrate_timing, refinish_hands)

# Aesthetic Restoration → Quality Control → Testing → Documentation
root.order.add_edge(restore_dial,    quality_control)
root.order.add_edge(refinish_hands,  quality_control)
root.order.add_edge(quality_control, test_function)
root.order.add_edge(test_function,   document_history)