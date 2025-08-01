# Generated from: 9f8ce7b3-e869-47a7-969b-b0c8e9250007.json
# Description: This process outlines the intricate steps involved in assembling custom drones tailored to unique client specifications. Starting from component sourcing, it includes specialized firmware integration, dynamic propeller calibration, environmental resistance testing under varying conditions, and adaptive AI training for autonomous flight behaviors. Quality assurance involves iterative stress simulations and real-time telemetry analysis to ensure reliability. Finally, packaging integrates modular upgrade options, and the delivery schedule adapts based on client feedback and seasonal demand fluctuations, ensuring a highly personalized and responsive manufacturing workflow.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities
component_sourcing = Transition(label='Component Sourcing')
frame_assembly      = Transition(label='Frame Assembly')
firmware_upload     = Transition(label='Firmware Upload')
propeller_mount     = Transition(label='Propeller Mount')
balance_check       = Transition(label='Balance Check')
sensor_install      = Transition(label='Sensor Install')
battery_fit         = Transition(label='Battery Fit')
wiring_route        = Transition(label='Wiring Route')
resistance_test     = Transition(label='Resistance Test')
ai_training         = Transition(label='AI Training')
stress_testing      = Transition(label='Stress Testing')
telemetry_sync      = Transition(label='Telemetry Sync')
flight_trial        = Transition(label='Flight Trial')
packaging_prep      = Transition(label='Packaging Prep')
upgrade_config      = Transition(label='Upgrade Config')
client_feedback     = Transition(label='Client Feedback')
delivery_plan       = Transition(label='Delivery Plan')

# Silent transitions for loop and choice
skip_qa       = SilentTransition()
skip_upgrade  = SilentTransition()

# QA loop: iterative Stress Testing -> Telemetry Sync
qa_seq = StrictPartialOrder(nodes=[stress_testing, telemetry_sync])
qa_seq.order.add_edge(stress_testing, telemetry_sync)
qa_loop = OperatorPOWL(operator=Operator.LOOP, children=[qa_seq, skip_qa])

# Optional upgrade after packaging
upgrade_xor = OperatorPOWL(operator=Operator.XOR, children=[upgrade_config, skip_upgrade])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    component_sourcing, frame_assembly, firmware_upload,
    propeller_mount, balance_check, sensor_install,
    battery_fit, wiring_route, resistance_test,
    ai_training, qa_loop, flight_trial,
    packaging_prep, upgrade_xor, client_feedback,
    delivery_plan
])

# Define the control-flow/order relations
o = root.order
o.add_edge(component_sourcing, frame_assembly)
o.add_edge(frame_assembly, firmware_upload)
o.add_edge(firmware_upload, propeller_mount)
o.add_edge(propeller_mount, balance_check)
o.add_edge(balance_check, sensor_install)
o.add_edge(sensor_install, battery_fit)
o.add_edge(battery_fit, wiring_route)
o.add_edge(wiring_route, resistance_test)
o.add_edge(resistance_test, ai_training)
o.add_edge(ai_training, qa_loop)
o.add_edge(qa_loop, flight_trial)
o.add_edge(flight_trial, packaging_prep)
o.add_edge(packaging_prep, upgrade_xor)
o.add_edge(upgrade_xor, client_feedback)
o.add_edge(client_feedback, delivery_plan)