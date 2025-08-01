# Generated from: fb3d1733-390e-44f3-996f-015fa340740d.json
# Description: This process involves the meticulous restoration of vintage mechanical watches, combining delicate craftsmanship with historical research. It begins with initial assessment to evaluate the watch's condition and authenticity, followed by disassembly and ultrasonic cleaning of all parts. Components are then inspected for wear or damage, with custom fabrication of missing or broken gears when necessary. Dial restoration includes color correction and repainting faded markers. The movement is reassembled, lubricated, and calibrated for accurate timekeeping. Finally, the case is polished and re-cased, and the watch undergoes rigorous quality testing before packaging. Throughout, detailed documentation preserves the watch’s provenance and restoration steps to maintain its collectible value.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Initial_Assess = Transition(label='Initial Assess')
Disassemble_Parts = Transition(label='Disassemble Parts')
Ultrasonic_Clean = Transition(label='Ultrasonic Clean')
Inspect_Components = Transition(label='Inspect Components')
Fabricate_Gears = Transition(label='Fabricate Gears')
Dial_Restoration = Transition(label='Dial Restoration')
Repaint_Markers = Transition(label='Repaint Markers')
Reassemble_Movement = Transition(label='Reassemble Movement')
Lubricate_Bearings = Transition(label='Lubricate Bearings')
Calibrate_Timing = Transition(label='Calibrate Timing')
Polish_Case = Transition(label='Polish Case')
Re_case_Watch = Transition(label='Re-case Watch')
Quality_Testing = Transition(label='Quality Testing')
Document_Process = Transition(label='Document Process')
Package_Product = Transition(label='Package Product')

# Fabrication choice: either fabricate gears or skip (silent)
skip = SilentTransition()
fabricate_choice = OperatorPOWL(operator=Operator.XOR, children=[Fabricate_Gears, skip])

# Dial restoration partial order: Dial Restoration then Repaint Markers
dial_po = StrictPartialOrder(nodes=[Dial_Restoration, Repaint_Markers])
dial_po.order.add_edge(Dial_Restoration, Repaint_Markers)

# After Inspect Components: choice to fabricate gears or skip, then dial restoration
# So Inspect_Components --> fabricate_choice --> dial_po

# Movement assembly partial order: Reassemble Movement --> Lubricate Bearings --> Calibrate Timing
movement_po = StrictPartialOrder(nodes=[Reassemble_Movement, Lubricate_Bearings, Calibrate_Timing])
movement_po.order.add_edge(Reassemble_Movement, Lubricate_Bearings)
movement_po.order.add_edge(Lubricate_Bearings, Calibrate_Timing)

# Polishing partial order: Polish Case --> Re-case Watch
polish_po = StrictPartialOrder(nodes=[Polish_Case, Re_case_Watch])
polish_po.order.add_edge(Polish_Case, Re_case_Watch)

# Quality testing before packaging
quality_pack_po = StrictPartialOrder(nodes=[Quality_Testing, Package_Product])
quality_pack_po.order.add_edge(Quality_Testing, Package_Product)

# Document process runs concurrently with polishing, quality testing and packaging
# Document_Process runs concurrently to these final activities

# Compose the main linear flow:
# Initial Assess --> Disassemble Parts --> Ultrasonic Clean --> Inspect Components
# --> fabricate_choice --> dial_po --> movement_po --> polish_po + quality_pack_po + Document_Process concurrently

# Create a PO with these nodes:
nodes = [
    Initial_Assess,
    Disassemble_Parts,
    Ultrasonic_Clean,
    Inspect_Components,
    fabricate_choice,
    dial_po,
    movement_po,
    polish_po,
    quality_pack_po,
    Document_Process
]

root = StrictPartialOrder(nodes=nodes)

# Add linear order from Initial Assess to movement_po
root.order.add_edge(Initial_Assess, Disassemble_Parts)
root.order.add_edge(Disassemble_Parts, Ultrasonic_Clean)
root.order.add_edge(Ultrasonic_Clean, Inspect_Components)
root.order.add_edge(Inspect_Components, fabricate_choice)
root.order.add_edge(fabricate_choice, dial_po)
root.order.add_edge(dial_po, movement_po)
root.order.add_edge(movement_po, polish_po)

# polish_po, quality_pack_po, and Document_Process run concurrently after movement_po,
# so add order from movement_po to these three but no ordering between them
root.order.add_edge(movement_po, polish_po)
root.order.add_edge(movement_po, quality_pack_po)
root.order.add_edge(movement_po, Document_Process)