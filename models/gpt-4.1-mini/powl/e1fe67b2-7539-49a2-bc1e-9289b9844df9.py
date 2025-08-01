# Generated from: e1fe67b2-7539-49a2-bc1e-9289b9844df9.json
# Description: This process involves the end-to-end assembly of custom drones tailored to specific client requirements. It starts with requirement gathering and design customization, followed by sourcing specialized components, firmware configuration, precision mechanical assembly, and multi-stage quality assurance. Each drone undergoes individual flight calibration and environmental testing before packaging. The process also includes software integration, remote control pairing, and final documentation. Post-assembly, the drones are registered for regulatory compliance and scheduled for client training sessions, ensuring full operational readiness and support.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

gather_specs = Transition(label='Gather Specs')
design_custom = Transition(label='Design Custom')
source_parts = Transition(label='Source Parts')
firmware_load = Transition(label='Firmware Load')
mechanical_fit = Transition(label='Mechanical Fit')
cable_routing = Transition(label='Cable Routing')
sensor_align = Transition(label='Sensor Align')
component_test = Transition(label='Component Test')
software_sync = Transition(label='Software Sync')
flight_calibrate = Transition(label='Flight Calibrate')
enviro_test = Transition(label='Enviro Test')
remote_pair = Transition(label='Remote Pair')
quality_check = Transition(label='Quality Check')
package_unit = Transition(label='Package Unit')
register_drone = Transition(label='Register Drone')
client_train = Transition(label='Client Train')

# Partial order 1: initial gathering and design
po1 = StrictPartialOrder(nodes=[gather_specs, design_custom])
po1.order.add_edge(gather_specs, design_custom)

# Partial order 2: sourcing and firmware + mechanical assembly steps
hardware_prep_nodes = [
    source_parts, 
    firmware_load, 
    mechanical_fit, 
    cable_routing, 
    sensor_align, 
    component_test,
]
po2 = StrictPartialOrder(nodes=hardware_prep_nodes)
po2.order.add_edge(source_parts, firmware_load)
po2.order.add_edge(firmware_load, mechanical_fit)
po2.order.add_edge(mechanical_fit, cable_routing)
po2.order.add_edge(cable_routing, sensor_align)
po2.order.add_edge(sensor_align, component_test)

# Partial order 3: software and remote pairing (can be concurrent with some hardware testing)
software_remote = StrictPartialOrder(nodes=[software_sync, remote_pair])
# No order between software_sync and remote_pair → concurrent

# Partial order 4: quality assurance chain
qa_nodes = [quality_check, flight_calibrate, enviro_test]
po4 = StrictPartialOrder(nodes=qa_nodes)
po4.order.add_edge(quality_check, flight_calibrate)
po4.order.add_edge(flight_calibrate, enviro_test)

# Partial order 5: final packaging
packaging = package_unit

# Partial order 6: post assembly registration and training (in order)
post_assembly = StrictPartialOrder(nodes=[register_drone, client_train])
post_assembly.order.add_edge(register_drone, client_train)

# Compose a partial order between hardware prep (po2) and software_remote (po3) as concurrent
hardware_software = StrictPartialOrder(nodes=[po2, software_remote])
# No edges: po2 and software_remote concurrent

# Compose order after design_custom:
# design_custom --> hardware_software (start hardware + software)
po5 = StrictPartialOrder(nodes=[po1, hardware_software])
po5.order.add_edge(po1, hardware_software)  # design_custom done before hardware/software

# Then hardware_software must finish before quality_check in po4
# So hardware_software --> quality_check (start QA)
po6 = StrictPartialOrder(nodes=[po5, po4])
po6.order.add_edge(po5, po4)

# Then enviro_test --> package_unit (packaging)
po7 = StrictPartialOrder(nodes=[po6, packaging])
po7.order.add_edge(po6, packaging)

# Then packaging --> register_drone (post assembly)
po8 = StrictPartialOrder(nodes=[po7, post_assembly])
po8.order.add_edge(po7, post_assembly)

root = po8