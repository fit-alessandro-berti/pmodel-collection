# Generated from: e1fe67b2-7539-49a2-bc1e-9289b9844df9.json
# Description: This process involves the end-to-end assembly of custom drones tailored to specific client requirements. It starts with requirement gathering and design customization, followed by sourcing specialized components, firmware configuration, precision mechanical assembly, and multi-stage quality assurance. Each drone undergoes individual flight calibration and environmental testing before packaging. The process also includes software integration, remote control pairing, and final documentation. Post-assembly, the drones are registered for regulatory compliance and scheduled for client training sessions, ensuring full operational readiness and support.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
gather_specs   = Transition(label="Gather Specs")
design_custom  = Transition(label="Design Custom")
source_parts   = Transition(label="Source Parts")
firmware_load  = Transition(label="Firmware Load")
mechanical_fit = Transition(label="Mechanical Fit")
cable_routing  = Transition(label="Cable Routing")
sensor_align   = Transition(label="Sensor Align")
component_test = Transition(label="Component Test")
software_sync  = Transition(label="Software Sync")
remote_pair    = Transition(label="Remote Pair")
quality_check  = Transition(label="Quality Check")
flight_calib   = Transition(label="Flight Calibrate")
enviro_test    = Transition(label="Enviro Test")
package_unit   = Transition(label="Package Unit")
register_drone = Transition(label="Register Drone")
client_train   = Transition(label="Client Train")

# Build the partial order (strictly sequential in this model)
nodes = [
    gather_specs,
    design_custom,
    source_parts,
    firmware_load,
    mechanical_fit,
    cable_routing,
    sensor_align,
    component_test,
    software_sync,
    remote_pair,
    quality_check,
    flight_calib,
    enviro_test,
    package_unit,
    register_drone,
    client_train
]

root = StrictPartialOrder(nodes=nodes)
# Add sequence edges
for src, tgt in zip(nodes, nodes[1:]):
    root.order.add_edge(src, tgt)