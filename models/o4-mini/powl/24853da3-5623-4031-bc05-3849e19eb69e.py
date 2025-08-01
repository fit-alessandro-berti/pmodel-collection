# Generated from: 24853da3-5623-4031-bc05-3849e19eb69e.json
# Description: This process outlines the intricate steps involved in designing and assembling bespoke drones tailored for specialized industrial applications. It begins with client consultation to determine precise specifications, followed by iterative design adjustments using advanced CAD tools. Components are sourced from multiple niche suppliers ensuring optimal performance. Assembly requires precision alignment of sensors, motors, and control units, followed by rigorous multi-phase testing including environmental stress and flight simulation. Calibration is fine-tuned according to test results, and final quality assurance ensures compliance with safety and operational standards before packaging and delivery coordination. Post-delivery support includes remote diagnostics and firmware updates to adapt to evolving user needs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
client_consult    = Transition(label='Client Consult')
design_draft      = Transition(label='Design Draft')
spec_review       = Transition(label='Spec Review')
supplier_select   = Transition(label='Supplier Select')
component_order   = Transition(label='Component Order')
parts_inspect     = Transition(label='Parts Inspect')
frame_assemble    = Transition(label='Frame Assemble')
sensor_mount      = Transition(label='Sensor Mount')
motor_install     = Transition(label='Motor Install')
control_setup     = Transition(label='Control Setup')
initial_test      = Transition(label='Initial Test')
stress_test       = Transition(label='Stress Test')
flight_sim        = Transition(label='Flight Sim')
calibration       = Transition(label='Calibration')
qa_inspect        = Transition(label='QA Inspect')
package_ship      = Transition(label='Package Ship')
post_support      = Transition(label='Post Support')

# Model the iterative design adjustment loop: do Design Draft then either exit or do Spec Review + repeat
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_draft, spec_review])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    client_consult,
    design_loop,
    supplier_select,
    component_order,
    parts_inspect,
    frame_assemble,
    sensor_mount,
    motor_install,
    control_setup,
    initial_test,
    stress_test,
    flight_sim,
    calibration,
    qa_inspect,
    package_ship,
    post_support
])

# Define the control-flow (sequence) edges
root.order.add_edge(client_consult, design_loop)
root.order.add_edge(design_loop, supplier_select)
root.order.add_edge(supplier_select, component_order)
root.order.add_edge(component_order, parts_inspect)
root.order.add_edge(parts_inspect, frame_assemble)
root.order.add_edge(frame_assemble, sensor_mount)
root.order.add_edge(sensor_mount, motor_install)
root.order.add_edge(motor_install, control_setup)
root.order.add_edge(control_setup, initial_test)
root.order.add_edge(initial_test, stress_test)
root.order.add_edge(stress_test, flight_sim)
root.order.add_edge(flight_sim, calibration)
root.order.add_edge(calibration, qa_inspect)
root.order.add_edge(qa_inspect, package_ship)
root.order.add_edge(package_ship, post_support)