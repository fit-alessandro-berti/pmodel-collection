# Generated from: d79d0a4e-23ac-4a2a-8172-4c61ae83de78.json
# Description: This process outlines the complex assembly and customization of drones tailored to specific industrial applications. It begins with component selection based on client specifications, followed by precision frame assembly and integration of proprietary navigation software. Quality assurance includes multi-layer sensor calibration and environmental stress testing under simulated conditions. The process also involves iterative firmware updating driven by real-time feedback loops and final packaging with comprehensive documentation before shipment. Maintenance scheduling and remote diagnostic setups complete the workflow, ensuring long-term operational efficiency and client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
spec_review      = Transition(label='Spec Review')
component_pick   = Transition(label='Component Pick')
frame_build      = Transition(label='Frame Build')
motor_mount      = Transition(label='Motor Mount')
sensor_fit       = Transition(label='Sensor Fit')
wiring_setup     = Transition(label='Wiring Setup')
software_load    = Transition(label='Software Load')
calibration_test = Transition(label='Calibration Test')
stress_check     = Transition(label='Stress Check')
firmware_flash   = Transition(label='Firmware Flash')
feedback_loop    = Transition(label='Feedback Loop')
package_prep     = Transition(label='Package Prep')
doc_compile      = Transition(label='Doc Compile')
ship_arrange     = Transition(label='Ship Arrange')
remote_setup     = Transition(label='Remote Setup')

# Frame assembly sequence: Frame Build -> Motor Mount -> Sensor Fit -> Wiring Setup
frame_assembly = StrictPartialOrder(nodes=[frame_build, motor_mount, sensor_fit, wiring_setup])
frame_assembly.order.add_edge(frame_build, motor_mount)
frame_assembly.order.add_edge(motor_mount, sensor_fit)
frame_assembly.order.add_edge(sensor_fit, wiring_setup)

# Quality assurance sequence: Calibration Test -> Stress Check
qa = StrictPartialOrder(nodes=[calibration_test, stress_check])
qa.order.add_edge(calibration_test, stress_check)

# Iterative firmware update loop: Firmware Flash followed by optional Feedback Loop repeats
firmware_loop = OperatorPOWL(operator=Operator.LOOP, children=[firmware_flash, feedback_loop])

# Packaging sequence: Package Prep -> Doc Compile -> Ship Arrange
packaging = StrictPartialOrder(nodes=[package_prep, doc_compile, ship_arrange])
packaging.order.add_edge(package_prep, doc_compile)
packaging.order.add_edge(doc_compile, ship_arrange)

# Build the top-level workflow
root = StrictPartialOrder(nodes=[
    spec_review,
    component_pick,
    frame_assembly,
    software_load,
    qa,
    firmware_loop,
    packaging,
    remote_setup
])
root.order.add_edge(spec_review, component_pick)
root.order.add_edge(component_pick, frame_assembly)
root.order.add_edge(frame_assembly, software_load)
root.order.add_edge(software_load, qa)
root.order.add_edge(qa, firmware_loop)
root.order.add_edge(firmware_loop, packaging)
root.order.add_edge(packaging, remote_setup)