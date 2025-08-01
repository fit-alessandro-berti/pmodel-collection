# Generated from: 9fd091fe-4478-4538-9e40-b50fad1fc9f4.json
# Description: This process involves the intricate assembly and customization of drones tailored for specialized industrial applications. Starting with component verification, it includes firmware integration, dynamic calibration, and environmental adaptability testing. The workflow demands rigorous quality assurance and compliance checks, followed by client-specific software loading and remote diagnostics setup. Final steps cover packaging with augmented reality manuals and logistics coordination for secure delivery. The process ensures drones meet unique operational demands while maintaining safety and performance standards in diverse environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
comp_check      = Transition(label='Component Check')
frame_assem     = Transition(label='Frame Assembly')
motor_mount     = Transition(label='Motor Mount')
sensor_setup    = Transition(label='Sensor Setup')
wiring_harness  = Transition(label='Wiring Harness')
firmware_load   = Transition(label='Firmware Load')
calibration     = Transition(label='Calibration Run')
flight_test     = Transition(label='Flight Test')
env_adaptation  = Transition(label='Env Adaptation')
qa_inspection   = Transition(label='QA Inspection')
compliance      = Transition(label='Compliance Verify')
software_install= Transition(label='Software Install')
diagnostics     = Transition(label='Diagnostics Setup')
packaging_ar    = Transition(label='Packaging AR')
logistics_plan  = Transition(label='Logistics Plan')
customer_handoff= Transition(label='Customer Handoff')
skip            = SilentTransition()

# Build the calibration+testing partial order: Calibration Run -> Flight Test -> Env Adaptation
cal_flow = StrictPartialOrder(nodes=[calibration, flight_test, env_adaptation])
cal_flow.order.add_edge(calibration, flight_test)
cal_flow.order.add_edge(flight_test, env_adaptation)

# Build the loop: do calibration/testing, then either exit or repeat
cal_loop = OperatorPOWL(operator=Operator.LOOP, children=[cal_flow, skip])

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    comp_check, frame_assem, motor_mount,
    sensor_setup, wiring_harness, firmware_load,
    cal_loop,
    qa_inspection, compliance,
    software_install, diagnostics,
    packaging_ar, logistics_plan,
    customer_handoff
])

# Define the workflow dependencies
# 1. Component Check -> Frame Assembly -> Motor Mount
root.order.add_edge(comp_check,     frame_assem)
root.order.add_edge(frame_assem,    motor_mount)

# 2. After motor mount, Sensor Setup and Wiring Harness in parallel
root.order.add_edge(motor_mount,    sensor_setup)
root.order.add_edge(motor_mount,    wiring_harness)

# 3. Both Sensor Setup and Wiring Harness -> Firmware Load
root.order.add_edge(sensor_setup,   firmware_load)
root.order.add_edge(wiring_harness, firmware_load)

# 4. Firmware Load -> Calibration/Test Loop
root.order.add_edge(firmware_load,  cal_loop)

# 5. After exiting loop -> QA Inspection -> Compliance Verify
root.order.add_edge(cal_loop,       qa_inspection)
root.order.add_edge(qa_inspection,  compliance)

# 6. Compliance Verify -> Software Install -> Diagnostics Setup
root.order.add_edge(compliance,        software_install)
root.order.add_edge(software_install,  diagnostics)

# 7. Diagnostics Setup -> Packaging AR and Logistics Plan (in parallel)
root.order.add_edge(diagnostics,    packaging_ar)
root.order.add_edge(diagnostics,    logistics_plan)

# 8. Both Packaging AR and Logistics Plan -> Customer Handoff
root.order.add_edge(packaging_ar,      customer_handoff)
root.order.add_edge(logistics_plan,    customer_handoff)