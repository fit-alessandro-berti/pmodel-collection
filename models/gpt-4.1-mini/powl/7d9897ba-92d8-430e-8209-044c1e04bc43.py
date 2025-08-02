# Generated from: 7d9897ba-92d8-430e-8209-044c1e04bc43.json
# Description: This process outlines the intricate steps involved in assembling custom drones tailored for specific industrial applications. It begins with component sourcing, ensuring rare parts meet quality standards, followed by precision frame construction. Next, it covers advanced sensor integration and software calibration. The process includes iterative flight testing under varied environmental conditions to optimize performance. Finally, it addresses packaging with anti-static materials and detailed documentation for end-user training and maintenance schedules, ensuring the drone’s reliability and longevity in specialized operations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Component_Sourcing = Transition(label='Component Sourcing')
Quality_Review = Transition(label='Quality Review')
Frame_Assembly = Transition(label='Frame Assembly')
Motor_Installation = Transition(label='Motor Installation')
Sensor_Integration = Transition(label='Sensor Integration')
Wiring_Setup = Transition(label='Wiring Setup')
Software_Upload = Transition(label='Software Upload')
Calibration_Test = Transition(label='Calibration Test')
Battery_Fitting = Transition(label='Battery Fitting')
Flight_Simulation = Transition(label='Flight Simulation')
Environmental_Test = Transition(label='Environmental Test')
Performance_Tuning = Transition(label='Performance Tuning')
Packaging_Prep = Transition(label='Packaging Prep')
Documentation = Transition(label='Documentation')
Client_Training = Transition(label='Client Training')
Maintenance_Setup = Transition(label='Maintenance Setup')

# Iterative flight testing loop setup:
# LOOP(
#   A=Flight_Simulation --> Environmental_Test --> Performance_Tuning (strict partial order)
#   B=Calibration_Test
# )
# meaning execute A, then choose exit or execute B then A again.

# Build partial order A inside the loop
flight_test_A = StrictPartialOrder(nodes=[Flight_Simulation, Environmental_Test, Performance_Tuning])
flight_test_A.order.add_edge(Flight_Simulation, Environmental_Test)
flight_test_A.order.add_edge(Environmental_Test, Performance_Tuning)

loop_node = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        flight_test_A,
        Calibration_Test
    ]
)

# Package and Documentation partial order
packaging_doc = StrictPartialOrder(nodes=[Packaging_Prep, Documentation])
packaging_doc.order.add_edge(Packaging_Prep, Documentation)

# Client Training and Maintenance Setup partial order (these can be concurrent or sequential)
# From description: documentation for end-user training and maintenance schedules
# We interpret "ensuring reliability and longevity" as sequential dependencies:
# Documentation --> Client Training --> Maintenance Setup
train_maint = StrictPartialOrder(
    nodes=[Client_Training, Maintenance_Setup]
)
train_maint.order.add_edge(Client_Training, Maintenance_Setup)

# Compose the final strict partial order of the entire process:
# Component Sourcing --> Quality Review --> Frame Assembly --> Motor Installation --> Sensor Integration --> Wiring Setup --> Software Upload --> Battery Fitting --> {loop} --> packaging_doc --> Client Training --> Maintenance Setup

# Because "Calibration Test" is a child of loop (loop B),
# we keep it inside the loop definition

root = StrictPartialOrder(
    nodes=[
        Component_Sourcing,
        Quality_Review,
        Frame_Assembly,
        Motor_Installation,
        Sensor_Integration,
        Wiring_Setup,
        Software_Upload,
        Battery_Fitting,
        loop_node,
        packaging_doc,
        Client_Training,
        Maintenance_Setup
    ]
)

# Add order edges chaining the activities:
root.order.add_edge(Component_Sourcing, Quality_Review)
root.order.add_edge(Quality_Review, Frame_Assembly)
root.order.add_edge(Frame_Assembly, Motor_Installation)
root.order.add_edge(Motor_Installation, Sensor_Integration)
root.order.add_edge(Sensor_Integration, Wiring_Setup)
root.order.add_edge(Wiring_Setup, Software_Upload)
root.order.add_edge(Software_Upload, Battery_Fitting)
root.order.add_edge(Battery_Fitting, loop_node)
root.order.add_edge(loop_node, packaging_doc)
root.order.add_edge(packaging_doc, Client_Training)
root.order.add_edge(Client_Training, Maintenance_Setup)