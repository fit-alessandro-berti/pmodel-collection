# Generated from: 5246f3e8-e117-4fcb-8584-ddf85146311d.json
# Description: This process outlines the intricate steps involved in the custom assembly and configuration of drones tailored for specialized industrial applications. It begins with detailed client requirement analysis, followed by component sourcing from multiple suppliers with varying lead times. Quality inspections are conducted on incoming parts before assembly. The workflow includes iterative firmware customization and real-time sensor calibration. Post-assembly, drones undergo environmental stress testing and autonomous flight simulations to validate performance under diverse conditions. The process concludes with packaging, client training sessions, and post-deployment support scheduling to ensure seamless integration into client operations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Client_Brief = Transition(label='Client Brief')
Component_Sourcing = Transition(label='Component Sourcing')
Parts_Inspection = Transition(label='Parts Inspection')
Frame_Assembly = Transition(label='Frame Assembly')
Firmware_Upload = Transition(label='Firmware Upload')
Sensor_Setup = Transition(label='Sensor Setup')
Motor_Calibration = Transition(label='Motor Calibration')
Battery_Installation = Transition(label='Battery Installation')
Initial_Testing = Transition(label='Initial Testing')
Stress_Testing = Transition(label='Stress Testing')
Flight_Simulation = Transition(label='Flight Simulation')
Quality_Audit = Transition(label='Quality Audit')
Packaging_Prep = Transition(label='Packaging Prep')
Client_Training = Transition(label='Client Training')
Support_Scheduling = Transition(label='Support Scheduling')

skip = SilentTransition()

# Loop for iterative firmware customization and sensor calibration
# (Firmware Upload and then concurrent Sensor Setup + Motor Calibration + Battery Installation)
# then repeat or exit the loop
firmware_customization = StrictPartialOrder(
    nodes=[Firmware_Upload, Sensor_Setup, Motor_Calibration, Battery_Installation]
)
firmware_customization.order.add_edge(Firmware_Upload, Sensor_Setup)
firmware_customization.order.add_edge(Firmware_Upload, Motor_Calibration)
firmware_customization.order.add_edge(Firmware_Upload, Battery_Installation)

loop_firmware = OperatorPOWL(operator=Operator.LOOP, children=[firmware_customization, skip])

# Initial Testing - which includes Quality Audit and Initial Testing concurrently
# Initial Testing depends on Frame Assembly and the firmware loop
initial_testing_parallel = StrictPartialOrder(
    nodes=[Initial_Testing, Quality_Audit]
)
# These two can happen concurrently, no edges between them

# Post Assembly partial order
post_assembly = StrictPartialOrder(
    nodes=[Stress_Testing, Flight_Simulation]
)
# These two happen concurrently

# Packaging, Client Training, Support Scheduling happen sequentially after post assembly tests
final_sequence = StrictPartialOrder(
    nodes=[Packaging_Prep, Client_Training, Support_Scheduling]
)
final_sequence.order.add_edge(Packaging_Prep, Client_Training)
final_sequence.order.add_edge(Client_Training, Support_Scheduling)

# Frame Assembly depends on Parts Inspection
# Parts Inspection depends on Component Sourcing
# Component Sourcing depends on Client Brief

pre_assembly = StrictPartialOrder(
    nodes=[Client_Brief, Component_Sourcing, Parts_Inspection, Frame_Assembly]
)
pre_assembly.order.add_edge(Client_Brief, Component_Sourcing)
pre_assembly.order.add_edge(Component_Sourcing, Parts_Inspection)
pre_assembly.order.add_edge(Parts_Inspection, Frame_Assembly)

# Combine the firmware loop (which comes after Frame Assembly)
post_frame_assembly = StrictPartialOrder(
    nodes=[loop_firmware, Frame_Assembly]
)
post_frame_assembly.order.add_edge(Frame_Assembly, loop_firmware)

# Combine initial testing parallel after firmware loop
post_firmware_testing = StrictPartialOrder(
    nodes=[loop_firmware, initial_testing_parallel]
)
post_firmware_testing.order.add_edge(loop_firmware, initial_testing_parallel)

# Combine testing and post assembly tests
testing_and_postassembly = StrictPartialOrder(
    nodes=[initial_testing_parallel, post_assembly]
)
testing_and_postassembly.order.add_edge(initial_testing_parallel, post_assembly)

# Combine everything in overall flow

partial1 = StrictPartialOrder(
    nodes=[pre_assembly, post_frame_assembly]
)
partial1.order.add_edge(pre_assembly, post_frame_assembly)

partial2 = StrictPartialOrder(
    nodes=[post_frame_assembly, post_firmware_testing]
)
partial2.order.add_edge(post_frame_assembly, post_firmware_testing)

partial3 = StrictPartialOrder(
    nodes=[post_firmware_testing, testing_and_postassembly]
)
partial3.order.add_edge(post_firmware_testing, testing_and_postassembly)

partial4 = StrictPartialOrder(
    nodes=[testing_and_postassembly, final_sequence]
)
partial4.order.add_edge(testing_and_postassembly, final_sequence)

# Because these must be connected in a final chain, create a root PO including all the major steps 
# Note: each partial shares nodes; do a final StrictPartialOrder with all nodes and edges combined

all_nodes = {
    Client_Brief,
    Component_Sourcing,
    Parts_Inspection,
    Frame_Assembly,
    loop_firmware,
    Firmware_Upload,
    Sensor_Setup,
    Motor_Calibration,
    Battery_Installation,
    Initial_Testing,
    Quality_Audit,
    Stress_Testing,
    Flight_Simulation,
    Packaging_Prep,
    Client_Training,
    Support_Scheduling
}

root = StrictPartialOrder(nodes=list(all_nodes))

# Add edges for pre_assembly
root.order.add_edge(Client_Brief, Component_Sourcing)
root.order.add_edge(Component_Sourcing, Parts_Inspection)
root.order.add_edge(Parts_Inspection, Frame_Assembly)

# Loop edges:
# Firmware_Upload -> Sensor_Setup, Motor_Calibration, Battery_Installation
root.order.add_edge(Firmware_Upload, Sensor_Setup)
root.order.add_edge(Firmware_Upload, Motor_Calibration)
root.order.add_edge(Firmware_Upload, Battery_Installation)

# Frame Assembly -> loop_firmware
root.order.add_edge(Frame_Assembly, loop_firmware)

# loop_firmware -> Initial_Testing and Quality_Audit (both concurrent)
root.order.add_edge(loop_firmware, Initial_Testing)
root.order.add_edge(loop_firmware, Quality_Audit)

# No edge between Initial_Testing and Quality_Audit (concurrent)

# Initial_Testing and Quality_Audit -> Stress_Testing and Flight_Simulation (both concurrent)
root.order.add_edge(Initial_Testing, Stress_Testing)
root.order.add_edge(Quality_Audit, Stress_Testing)
root.order.add_edge(Initial_Testing, Flight_Simulation)
root.order.add_edge(Quality_Audit, Flight_Simulation)

# Stress_Testing and Flight_Simulation -> Packaging_Prep (both must finish before packaging)
root.order.add_edge(Stress_Testing, Packaging_Prep)
root.order.add_edge(Flight_Simulation, Packaging_Prep)

# Packaging Prep -> Client Training -> Support Scheduling (sequential)
root.order.add_edge(Packaging_Prep, Client_Training)
root.order.add_edge(Client_Training, Support_Scheduling)