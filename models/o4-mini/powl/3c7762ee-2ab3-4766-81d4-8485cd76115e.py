# Generated from: 3c7762ee-2ab3-4766-81d4-8485cd76115e.json
# Description: This process outlines the intricate steps involved in assembling custom drones tailored to specific client requirements. It begins with component selection based on desired drone capabilities, followed by intricate circuit integration and firmware customization. Quality checks ensure compliance with safety and performance standards, while iterative flight testing validates operational stability. The process also includes environmental resilience testing, packaging with personalized branding, and coordination with logistics for expedited delivery. Throughout, detailed documentation and client feedback loops optimize future iterations and enhance overall product reliability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
component_pick   = Transition(label='Component Pick')
circuit_mount    = Transition(label='Circuit Mount')
firmware_flash   = Transition(label='Firmware Flash')
sensor_align     = Transition(label='Sensor Align')
propeller_fit    = Transition(label='Propeller Fit')
battery_install  = Transition(label='Battery Install')
signal_test      = Transition(label='Signal Test')
calibrate_gyro   = Transition(label='Calibrate Gyro')
flight_trial     = Transition(label='Flight Trial')
data_log         = Transition(label='Data Log')
stress_test      = Transition(label='Stress Test')
weather_proof    = Transition(label='Weather Proof')
package_drone    = Transition(label='Package Drone')
brand_label      = Transition(label='Brand Label')
shipping_prep    = Transition(label='Shipping Prep')
client_review    = Transition(label='Client Review')

# Loop for iterative flight testing: Flight Trial, then either exit or Data Log + Flight Trial again
flight_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[flight_trial, data_log]
)

# Environmental resilience testing sequence: Stress Test -> Weather Proof
env_seq = StrictPartialOrder(nodes=[stress_test, weather_proof])
env_seq.order.add_edge(stress_test, weather_proof)

# Packaging sequence: Package Drone -> Brand Label -> Shipping Prep
packaging_op = StrictPartialOrder(nodes=[package_drone, brand_label, shipping_prep])
packaging_op.order.add_edge(package_drone, brand_label)
packaging_op.order.add_edge(brand_label, shipping_prep)

# Feedback loop around packaging: do packaging, then either exit or Client Review + re-package
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[packaging_op, client_review]
)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    component_pick,
    circuit_mount,
    firmware_flash,
    sensor_align,
    propeller_fit,
    battery_install,
    signal_test,
    calibrate_gyro,
    flight_loop,
    env_seq,
    feedback_loop
])

# Define the control-flow / data dependencies
root.order.add_edge(component_pick,  circuit_mount)
root.order.add_edge(circuit_mount,   firmware_flash)

# After firmware flash, the three assembly checks can run in parallel
root.order.add_edge(firmware_flash,  sensor_align)
root.order.add_edge(firmware_flash,  propeller_fit)
root.order.add_edge(firmware_flash,  battery_install)

# All three must complete before signal testing
root.order.add_edge(sensor_align,    signal_test)
root.order.add_edge(propeller_fit,   signal_test)
root.order.add_edge(battery_install, signal_test)

# Then calibrate gyro, then enter flight testing loop
root.order.add_edge(signal_test,     calibrate_gyro)
root.order.add_edge(calibrate_gyro,  flight_loop)

# After flight testing is stabilized, do environmental tests
root.order.add_edge(flight_loop,     env_seq)

# Then packaging with a feedback loop
root.order.add_edge(env_seq,         feedback_loop)