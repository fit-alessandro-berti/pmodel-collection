# Generated from: a0502612-60b1-4f0f-b6e8-ffc86aa69e2a.json
# Description: This process outlines the assembly and deployment of custom drones tailored for specialized industrial applications. It begins with component sourcing from multiple niche suppliers, followed by precision calibration of sensors and flight systems. Subsequent steps include firmware customization, modular payload integration, and rigorous multi-environment testing. Quality assurance involves iterative feedback loops between engineers and test pilots to refine flight stability and sensor accuracy. Finally, the drones undergo packaging with tailored user manuals and are shipped under controlled conditions to ensure integrity upon delivery. This atypical process requires coordination across hardware, software, and logistics teams to meet highly specific client requirements within tight deadlines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
part_sourcing = Transition(label='Part Sourcing')
sensor_align = Transition(label='Sensor Align')
frame_build = Transition(label='Frame Build')
motor_install = Transition(label='Motor Install')
firmware_flash = Transition(label='Firmware Flash')
payload_fit = Transition(label='Payload Fit')
signal_tune = Transition(label='Signal Tune')
flight_test = Transition(label='Flight Test')
data_log = Transition(label='Data Log')
error_fix = Transition(label='Error Fix')
pilot_review = Transition(label='Pilot Review')
quality_audit = Transition(label='Quality Audit')
manual_write = Transition(label='Manual Write')
package_prep = Transition(label='Package Prep')
dispatch_arrange = Transition(label='Dispatch Arrange')
client_confirm = Transition(label='Client Confirm')
feedback_loop = Transition(label='Feedback Loop')

# Define the QA iterative loop:
# A = Flight Test -> Data Log -> Pilot Review -> Quality Audit
po_A = StrictPartialOrder(nodes=[flight_test, data_log, pilot_review, quality_audit])
po_A.order.add_edge(flight_test, data_log)
po_A.order.add_edge(data_log, pilot_review)
po_A.order.add_edge(pilot_review, quality_audit)

# B = Error Fix -> Feedback Loop (then back to A)
po_B = StrictPartialOrder(nodes=[error_fix, feedback_loop])
po_B.order.add_edge(error_fix, feedback_loop)

loop_qa = OperatorPOWL(operator=Operator.LOOP, children=[po_A, po_B])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    part_sourcing,
    sensor_align,
    frame_build,
    motor_install,
    firmware_flash,
    payload_fit,
    signal_tune,
    loop_qa,
    manual_write,
    package_prep,
    dispatch_arrange,
    client_confirm
])

# Define the control‐flow dependencies
# 1. Part Sourcing -> [Sensor Align, Frame Build]
root.order.add_edge(part_sourcing, sensor_align)
root.order.add_edge(part_sourcing, frame_build)

# 2. Frame Build -> Motor Install
root.order.add_edge(frame_build, motor_install)

# 3. Motor Install -> Firmware Flash -> Payload Fit -> Signal Tune
root.order.add_edge(motor_install, firmware_flash)
root.order.add_edge(firmware_flash, payload_fit)
root.order.add_edge(payload_fit, signal_tune)

# 4. Sensor Align also feeds into Signal Tune
root.order.add_edge(sensor_align, signal_tune)

# 5. After tuning, enter the QA loop
root.order.add_edge(signal_tune, loop_qa)

# 6. After QA loop, finalize packaging and delivery
root.order.add_edge(loop_qa, manual_write)
root.order.add_edge(manual_write, package_prep)
root.order.add_edge(package_prep, dispatch_arrange)
root.order.add_edge(dispatch_arrange, client_confirm)