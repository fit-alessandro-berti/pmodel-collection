# Generated from: ad0891dc-adf2-41e2-aa5e-a7e733e24475.json
# Description: This process outlines the intricate steps involved in assembling custom drones tailored for specialized industrial applications. It begins with component sourcing, followed by precision calibration of sensors and flight controllers. The assembly involves iterative software-hardware integration, rigorous environmental testing under simulated conditions, and final quality certification. Each drone undergoes a unique flight pattern programming to match client specifications, including payload configurations and emergency protocols. The process concludes with packaging and logistics coordination, ensuring safe delivery and post-deployment support scheduling.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
component_sourcing   = Transition(label='Component Sourcing')
sensor_calibrate     = Transition(label='Sensor Calibrate')
frame_assembly       = Transition(label='Frame Assembly')
wiring_harness       = Transition(label='Wiring Harness')
controller_install   = Transition(label='Controller Install')
software_load        = Transition(label='Software Load')
firmware_update      = Transition(label='Firmware Update')
enviro_simulate      = Transition(label='Enviro Simulate')
stress_testing       = Transition(label='Stress Testing')
quality_check        = Transition(label='Quality Check')
certify_drone        = Transition(label='Certify Drone')
flight_pattern       = Transition(label='Flight Pattern')
payload_setup        = Transition(label='Payload Setup')
package_unit         = Transition(label='Package Unit')
ship_logistics       = Transition(label='Ship Logistics')
support_schedule     = Transition(label='Support Schedule')

# Loop for software-hardware integration: Software Load -> (Firmware Update then back to Software Load)*
loop_integration = OperatorPOWL(
    operator=Operator.LOOP,
    children=[software_load, firmware_update]
)

# Loop for environmental testing: Enviro Simulate -> (Stress Testing then back to Enviro Simulate)*
loop_testing = OperatorPOWL(
    operator=Operator.LOOP,
    children=[enviro_simulate, stress_testing]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    component_sourcing,
    sensor_calibrate,
    frame_assembly,
    wiring_harness,
    controller_install,
    loop_integration,
    loop_testing,
    quality_check,
    certify_drone,
    flight_pattern,
    payload_setup,
    package_unit,
    ship_logistics,
    support_schedule
])

# Define the control-flow order
edges = [
    (component_sourcing, sensor_calibrate),
    (sensor_calibrate, frame_assembly),
    (frame_assembly, wiring_harness),
    (wiring_harness, controller_install),
    (controller_install, loop_integration),
    (loop_integration, loop_testing),
    (loop_testing, quality_check),
    (quality_check, certify_drone),
    (certify_drone, flight_pattern),
    (flight_pattern, payload_setup),
    (payload_setup, package_unit),
    (package_unit, ship_logistics),
    (ship_logistics, support_schedule)
]

for src, tgt in edges:
    root.order.add_edge(src, tgt)