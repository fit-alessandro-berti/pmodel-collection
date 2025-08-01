# Generated from: fb3d1733-390e-44f3-996f-015fa340740d.json
# Description: This process involves the meticulous restoration of vintage mechanical watches, combining delicate craftsmanship with historical research. It begins with initial assessment to evaluate the watch's condition and authenticity, followed by disassembly and ultrasonic cleaning of all parts. Components are then inspected for wear or damage, with custom fabrication of missing or broken gears when necessary. Dial restoration includes color correction and repainting faded markers. The movement is reassembled, lubricated, and calibrated for accurate timekeeping. Finally, the case is polished and re-cased, and the watch undergoes rigorous quality testing before packaging. Throughout, detailed documentation preserves the watch’s provenance and restoration steps to maintain its collectible value.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
initial_assess      = Transition(label="Initial Assess")
disassemble_parts   = Transition(label="Disassemble Parts")
ultrasonic_clean    = Transition(label="Ultrasonic Clean")
inspect_components  = Transition(label="Inspect Components")
fabricate_gears     = Transition(label="Fabricate Gears")
dial_restoration    = Transition(label="Dial Restoration")
repaint_markers     = Transition(label="Repaint Markers")
reassemble_movement = Transition(label="Reassemble Movement")
lubricate_bearings  = Transition(label="Lubricate Bearings")
calibrate_timing    = Transition(label="Calibrate Timing")
polish_case         = Transition(label="Polish Case")
re_case_watch       = Transition(label="Re-case Watch")
quality_testing     = Transition(label="Quality Testing")
document_process    = Transition(label="Document Process")
package_product     = Transition(label="Package Product")

# Silent transition for skipping fabrication when not needed
skip = SilentTransition()

# XOR choice: either fabricate gears or skip
xor_fabrication = OperatorPOWL(operator=Operator.XOR, children=[skip, fabricate_gears])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    initial_assess,
    disassemble_parts,
    ultrasonic_clean,
    inspect_components,
    xor_fabrication,
    dial_restoration,
    repaint_markers,
    reassemble_movement,
    lubricate_bearings,
    calibrate_timing,
    polish_case,
    re_case_watch,
    quality_testing,
    document_process,
    package_product
])

# Add the sequencing relations
root.order.add_edge(initial_assess,      disassemble_parts)
root.order.add_edge(disassemble_parts,   ultrasonic_clean)
root.order.add_edge(ultrasonic_clean,    inspect_components)
root.order.add_edge(inspect_components,  xor_fabrication)
root.order.add_edge(xor_fabrication,     dial_restoration)
root.order.add_edge(dial_restoration,    repaint_markers)
root.order.add_edge(repaint_markers,     reassemble_movement)
root.order.add_edge(reassemble_movement, lubricate_bearings)
root.order.add_edge(lubricate_bearings,  calibrate_timing)
root.order.add_edge(calibrate_timing,    polish_case)
root.order.add_edge(polish_case,         re_case_watch)
root.order.add_edge(re_case_watch,       quality_testing)
root.order.add_edge(quality_testing,     package_product)

# Documentation runs in parallel, from initial assessment until packaging
root.order.add_edge(initial_assess,   document_process)
root.order.add_edge(document_process, package_product)