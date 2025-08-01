# Generated from: e15f3d77-d62a-433a-b368-45e5b50daf98.json
# Description: This process details the end-to-end assembly of customized drones tailored to specific client requirements. It begins with requirements gathering and design adaptation, followed by specialized component sourcing from multiple vendors. The components undergo individual testing before precision assembly, firmware installation, and calibration. Post-assembly, drones are subjected to environmental stress testing and flight simulation to ensure operational reliability. Final quality checks include battery endurance and sensor accuracy validation. After successful validation, drones are packaged with customized manuals and shipped with tracking integration. Customer feedback is collected post-delivery to inform continuous improvement cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Gather_Specs = Transition(label='Gather Specs')
Adapt_Design = Transition(label='Adapt Design')

Source_Parts = Transition(label='Source Parts')

Component_Test = Transition(label='Component Test')

Assemble_Frame = Transition(label='Assemble Frame')
Install_Firmware = Transition(label='Install Firmware')
Calibrate_Sensors = Transition(label='Calibrate Sensors')

Stress_Test = Transition(label='Stress Test')
Flight_Simulate = Transition(label='Flight Simulate')

Validate_Battery = Transition(label='Validate Battery')
Check_Accuracy = Transition(label='Check Accuracy')

Package_Units = Transition(label='Package Units')
Create_Manuals = Transition(label='Create Manuals')

Ship_Drones = Transition(label='Ship Drones')

Collect_Feedback = Transition(label='Collect Feedback')

# Define partial orders for parallel or sequential steps

# 1. Initial sequence: Gather Specs --> Adapt Design
init_PO = StrictPartialOrder(nodes=[Gather_Specs, Adapt_Design])
init_PO.order.add_edge(Gather_Specs, Adapt_Design)

# 2. Source Parts alone (no concurrency mentioned, assume sequential after Adapt Design)
# We'll connect adapt_design to source_parts later in main PO

# 3. Component Test after Source Parts
# Later connect source_parts --> component_test

# 4. Assembly sequence: Assemble Frame --> Install Firmware --> Calibrate Sensors
assembly_PO = StrictPartialOrder(nodes=[Assemble_Frame, Install_Firmware, Calibrate_Sensors])
assembly_PO.order.add_edge(Assemble_Frame, Install_Firmware)
assembly_PO.order.add_edge(Install_Firmware, Calibrate_Sensors)

# 5. Stress Test and Flight Simulate happen post assembly and are sequential (Stress test then Flight simulate)
test_PO = StrictPartialOrder(nodes=[Stress_Test, Flight_Simulate])
test_PO.order.add_edge(Stress_Test, Flight_Simulate)

# 6. Validate Battery and Check Accuracy are final quality checks - no concurrency mentioned,
# assume Validate Battery --> Check Accuracy
validate_PO = StrictPartialOrder(nodes=[Validate_Battery, Check_Accuracy])
validate_PO.order.add_edge(Validate_Battery, Check_Accuracy)

# 7. Packaging and manuals done in parallel before shipping
packaging_PO = StrictPartialOrder(nodes=[Package_Units, Create_Manuals])
# No order edge means concurrent; assume parallel packaging/manuals

# Assemble packaging and then ship drones sequentially
pack_ship_PO = StrictPartialOrder(nodes=[packaging_PO, Ship_Drones])
pack_ship_PO.order.add_edge(packaging_PO, Ship_Drones)

# 8. Finally, Collect Feedback after shipping
# Connect ship_drones --> collect_feedback

# Now compose the entire process PO in partial order form:

# Nodes:
# - init_PO (Gather Specs -> Adapt Design)
# - Source_Parts
# - Component_Test
# - assembly_PO (Assemble Frame -> Install Firmware -> Calibrate Sensors)
# - test_PO (Stress Test -> Flight Simulate)
# - validate_PO (Validate Battery -> Check Accuracy)
# - pack_ship_PO (packaging_PO in parallel + Ship Drones)
# - Collect_Feedback

# Construct root PO integrating the above with edges describing their order.

root = StrictPartialOrder(
    nodes=[init_PO,
           Source_Parts,
           Component_Test,
           assembly_PO,
           test_PO,
           validate_PO,
           pack_ship_PO,
           Collect_Feedback]
)

# Add edges describing order dependencies per process description:

# init_PO --> Source_Parts --> Component_Test
root.order.add_edge(init_PO, Source_Parts)
root.order.add_edge(Source_Parts, Component_Test)

# Component_Test --> assembly_PO
root.order.add_edge(Component_Test, assembly_PO)

# assembly_PO --> test_PO
root.order.add_edge(assembly_PO, test_PO)

# test_PO --> validate_PO
root.order.add_edge(test_PO, validate_PO)

# validate_PO --> pack_ship_PO
root.order.add_edge(validate_PO, pack_ship_PO)

# pack_ship_PO --> Collect_Feedback
root.order.add_edge(pack_ship_PO, Collect_Feedback)