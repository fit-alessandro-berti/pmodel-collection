# Generated from: 4ad59123-736d-4d4d-8a1c-b472e119b654.json
# Description: This process involves the bespoke assembly of drones tailored to individual client specifications. It begins with requirement analysis, followed by component sourcing from multiple suppliers with varying lead times. Custom firmware is developed in parallel while mechanical assembly and initial calibration occur. Rigorous multi-environment testing is conducted, including wind tunnel and obstacle navigation simulations. After successful testing, final quality assurance and packaging are performed before shipment scheduling and delivery confirmation. Post-delivery, remote diagnostics and software updates are managed to ensure optimal performance and client satisfaction throughout the drone's operational lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
client_intake     = Transition(label="Client Intake")
specs_review      = Transition(label="Specs Review")
component_order   = Transition(label="Component Order")
firmware_dev      = Transition(label="Firmware Dev")
chassis_build     = Transition(label="Chassis Build")
motor_install     = Transition(label="Motor Install")
sensor_align      = Transition(label="Sensor Align")
initial_calib     = Transition(label="Initial Calib")
wind_test         = Transition(label="Wind Test")
nav_sim           = Transition(label="Nav Sim")
quality_check     = Transition(label="Quality Check")
final_assembly    = Transition(label="Final Assembly")
packaging_prep    = Transition(label="Packaging Prep")
ship_schedule     = Transition(label="Ship Schedule")
delivery_confirm  = Transition(label="Delivery Confirm")
remote_support    = Transition(label="Remote Support")

# Create the root partial order with all nodes
root = StrictPartialOrder(nodes=[
    client_intake,
    specs_review,
    component_order,
    firmware_dev,
    chassis_build,
    motor_install,
    sensor_align,
    initial_calib,
    wind_test,
    nav_sim,
    quality_check,
    final_assembly,
    packaging_prep,
    ship_schedule,
    delivery_confirm,
    remote_support
])

# Define the control-flow (order) dependencies

# Requirement analysis
root.order.add_edge(client_intake, specs_review)

# After specs review, three streams run in parallel:
# 1) Component ordering
# 2) Firmware development
# 3) Mechanical assembly -> calibration
root.order.add_edge(specs_review, component_order)
root.order.add_edge(specs_review, firmware_dev)
root.order.add_edge(specs_review, chassis_build)

# Mechanical assembly chain
root.order.add_edge(chassis_build, motor_install)
root.order.add_edge(motor_install, sensor_align)
root.order.add_edge(sensor_align, initial_calib)

# After all three streams complete, multi-environment testing (in parallel)
for prep in (component_order, firmware_dev, initial_calib):
    root.order.add_edge(prep, wind_test)
    root.order.add_edge(prep, nav_sim)

# After both tests, do quality check and subsequent steps
root.order.add_edge(wind_test, quality_check)
root.order.add_edge(nav_sim, quality_check)

root.order.add_edge(quality_check, final_assembly)
root.order.add_edge(final_assembly, packaging_prep)
root.order.add_edge(packaging_prep, ship_schedule)
root.order.add_edge(ship_schedule, delivery_confirm)

# After delivery confirmation, remote support happens
root.order.add_edge(delivery_confirm, remote_support)