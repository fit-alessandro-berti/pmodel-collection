# Generated from: d79d0a4e-23ac-4a2a-8172-4c61ae83de78.json
# Description: This process outlines the complex assembly and customization of drones tailored to specific industrial applications. It begins with component selection based on client specifications, followed by precision frame assembly and integration of proprietary navigation software. Quality assurance includes multi-layer sensor calibration and environmental stress testing under simulated conditions. The process also involves iterative firmware updating driven by real-time feedback loops and final packaging with comprehensive documentation before shipment. Maintenance scheduling and remote diagnostic setups complete the workflow, ensuring long-term operational efficiency and client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

spec_review = Transition(label='Spec Review')
component_pick = Transition(label='Component Pick')

# Frame Build composite partial order: Frame Build --> Motor Mount, Sensor Fit, Wiring Setup all concurrent after Frame Build
frame_build = Transition(label='Frame Build')
motor_mount = Transition(label='Motor Mount')
sensor_fit = Transition(label='Sensor Fit')
wiring_setup = Transition(label='Wiring Setup')
frame_sub_po = StrictPartialOrder(nodes=[motor_mount, sensor_fit, wiring_setup])
# no edges among motor_mount,sensor_fit,wiring_setup => concurrent

frame_build_po = StrictPartialOrder(nodes=[frame_build, frame_sub_po])
frame_build_po.order.add_edge(frame_build, frame_sub_po)  # frame_build before sub activities

software_load = Transition(label='Software Load')

calibration_test = Transition(label='Calibration Test')
stress_check = Transition(label='Stress Check')

# Quality assurance partial order: Calibration Test and Stress Check concurrent (no order)
qa_po = StrictPartialOrder(nodes=[calibration_test, stress_check])

firmware_flash = Transition(label='Firmware Flash')
feedback_loop = Transition(label='Feedback Loop')
# Loop: execute Firmware Flash, then choose to exit or iterate Feedback Loop then Firmware Flash again
firmware_loop = OperatorPOWL(operator=Operator.LOOP, children=[firmware_flash, feedback_loop])

package_prep = Transition(label='Package Prep')
doc_compile = Transition(label='Doc Compile')
# Package preparation and documentation concurrent
package_doc_po = StrictPartialOrder(nodes=[package_prep, doc_compile])

ship_arrange = Transition(label='Ship Arrange')
remote_setup = Transition(label='Remote Setup')

# Build the overall partial order with ordering:
# Spec Review -> Component Pick -> Frame Build PO -> Software Load -> QA (calibration+stress) -> firmware loop ->
# package/doc concurrent -> Ship Arrange -> Remote Setup

root = StrictPartialOrder(
    nodes=[
        spec_review,
        component_pick,
        frame_build_po,
        software_load,
        qa_po,
        firmware_loop,
        package_doc_po,
        ship_arrange,
        remote_setup
    ])

root.order.add_edge(spec_review, component_pick)
root.order.add_edge(component_pick, frame_build_po)
root.order.add_edge(frame_build_po, software_load)
root.order.add_edge(software_load, qa_po)
root.order.add_edge(qa_po, firmware_loop)
root.order.add_edge(firmware_loop, package_doc_po)
root.order.add_edge(package_doc_po, ship_arrange)
root.order.add_edge(ship_arrange, remote_setup)