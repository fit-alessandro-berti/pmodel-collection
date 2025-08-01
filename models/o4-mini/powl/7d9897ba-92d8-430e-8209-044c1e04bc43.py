# Generated from: 7d9897ba-92d8-430e-8209-044c1e04bc43.json
# Description: This process outlines the intricate steps involved in assembling custom drones tailored for specific industrial applications. It begins with component sourcing, ensuring rare parts meet quality standards, followed by precision frame construction. Next, it covers advanced sensor integration and software calibration. The process includes iterative flight testing under varied environmental conditions to optimize performance. Finally, it addresses packaging with anti-static materials and detailed documentation for end-user training and maintenance schedules, ensuring the drone’s reliability and longevity in specialized operations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
comp_sourcing      = Transition(label='Component Sourcing')
quality_review     = Transition(label='Quality Review')
frame_assembly     = Transition(label='Frame Assembly')
motor_installation = Transition(label='Motor Installation')
sensor_integration = Transition(label='Sensor Integration')
wiring_setup       = Transition(label='Wiring Setup')
software_upload    = Transition(label='Software Upload')
calibration_test   = Transition(label='Calibration Test')
battery_fitting    = Transition(label='Battery Fitting')
flight_simulation  = Transition(label='Flight Simulation')
environmental_test = Transition(label='Environmental Test')
performance_tuning = Transition(label='Performance Tuning')
packaging_prep     = Transition(label='Packaging Prep')
documentation      = Transition(label='Documentation')
client_training    = Transition(label='Client Training')
maintenance_setup  = Transition(label='Maintenance Setup')

# Loop body for iterative flight testing
loop_body = StrictPartialOrder(nodes=[environmental_test, performance_tuning])
loop_body.order.add_edge(environmental_test, performance_tuning)

# Loop operator: do flight_simulation, then repeat [environmental_test -> performance_tuning] and flight_simulation until exit
flight_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulation, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    comp_sourcing, quality_review,
    frame_assembly, motor_installation,
    sensor_integration, wiring_setup,
    software_upload, calibration_test,
    battery_fitting, flight_test_loop,
    packaging_prep, documentation,
    client_training, maintenance_setup
])

# Add control-flow edges
root.order.add_edge(comp_sourcing,      quality_review)
root.order.add_edge(quality_review,     frame_assembly)
root.order.add_edge(frame_assembly,     motor_installation)
root.order.add_edge(motor_installation, sensor_integration)
root.order.add_edge(sensor_integration, wiring_setup)
root.order.add_edge(wiring_setup,       software_upload)
root.order.add_edge(software_upload,    calibration_test)
root.order.add_edge(calibration_test,   battery_fitting)
root.order.add_edge(battery_fitting,    flight_test_loop)
root.order.add_edge(flight_test_loop,   packaging_prep)
root.order.add_edge(packaging_prep,     documentation)
root.order.add_edge(documentation,      client_training)
root.order.add_edge(client_training,    maintenance_setup)