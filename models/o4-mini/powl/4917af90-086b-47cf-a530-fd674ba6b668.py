# Generated from: 4917af90-086b-47cf-a530-fd674ba6b668.json
# Description: This process outlines the complex assembly and calibration of custom drones tailored for specialized industrial applications. Starting from component sourcing through iterative firmware tuning, the workflow includes precision mechanical integration, sensor alignment, and multi-environment testing. Each drone undergoes adaptive software calibration based on mission-specific parameters, followed by compliance verification with aviation regulations. The process concludes with detailed quality reporting and client-specific customization before final packaging and delivery, ensuring high reliability and performance in diverse operational conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
component_sourcing = Transition(label='Component Sourcing')
frame_assembly = Transition(label='Frame Assembly')
motor_installation = Transition(label='Motor Installation')
wiring_setup = Transition(label='Wiring Setup')
sensor_mounting = Transition(label='Sensor Mounting')
firmware_upload = Transition(label='Firmware Upload')
calibration_stage = Transition(label='Calibration Stage')
software_tuning = Transition(label='Software Tuning')
env_testing = Transition(label='Env Testing')
flight_simulation = Transition(label='Flight Simulation')
compliance_check = Transition(label='Compliance Check')
performance_audit = Transition(label='Performance Audit')
client_customization = Transition(label='Client Customization')
quality_reporting = Transition(label='Quality Reporting')
final_packaging = Transition(label='Final Packaging')
delivery_scheduling = Transition(label='Delivery Scheduling')

# Loop for iterative calibration and tuning
tuning_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[calibration_stage, software_tuning]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    component_sourcing,
    frame_assembly,
    motor_installation,
    wiring_setup,
    sensor_mounting,
    firmware_upload,
    tuning_loop,
    env_testing,
    flight_simulation,
    compliance_check,
    performance_audit,
    quality_reporting,
    client_customization,
    final_packaging,
    delivery_scheduling
])

# Define the control-flow dependencies
root.order.add_edge(component_sourcing, frame_assembly)
root.order.add_edge(frame_assembly, motor_installation)
root.order.add_edge(motor_installation, wiring_setup)
root.order.add_edge(wiring_setup, sensor_mounting)
root.order.add_edge(sensor_mounting, firmware_upload)
root.order.add_edge(firmware_upload, tuning_loop)
root.order.add_edge(tuning_loop, env_testing)
root.order.add_edge(env_testing, flight_simulation)
root.order.add_edge(flight_simulation, compliance_check)
root.order.add_edge(flight_simulation, performance_audit)
root.order.add_edge(compliance_check, quality_reporting)
root.order.add_edge(performance_audit, quality_reporting)
root.order.add_edge(quality_reporting, client_customization)
root.order.add_edge(client_customization, final_packaging)
root.order.add_edge(final_packaging, delivery_scheduling)