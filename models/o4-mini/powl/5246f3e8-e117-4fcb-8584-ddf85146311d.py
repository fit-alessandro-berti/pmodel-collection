# Generated from: 5246f3e8-e117-4fcb-8584-ddf85146311d.json
# Description: This process outlines the intricate steps involved in the custom assembly and configuration of drones tailored for specialized industrial applications. It begins with detailed client requirement analysis, followed by component sourcing from multiple suppliers with varying lead times. Quality inspections are conducted on incoming parts before assembly. The workflow includes iterative firmware customization and real-time sensor calibration. Post-assembly, drones undergo environmental stress testing and autonomous flight simulations to validate performance under diverse conditions. The process concludes with packaging, client training sessions, and post-deployment support scheduling to ensure seamless integration into client operations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
client_brief    = Transition(label='Client Brief')
component_src   = Transition(label='Component Sourcing')
parts_insp      = Transition(label='Parts Inspection')
frame_asm       = Transition(label='Frame Assembly')
battery_inst    = Transition(label='Battery Installation')
fw_upload       = Transition(label='Firmware Upload')
sensor_setup    = Transition(label='Sensor Setup')
motor_calib     = Transition(label='Motor Calibration')
initial_test    = Transition(label='Initial Testing')
stress_test     = Transition(label='Stress Testing')
flight_sim      = Transition(label='Flight Simulation')
quality_audit   = Transition(label='Quality Audit')
pack_prep       = Transition(label='Packaging Prep')
client_train    = Transition(label='Client Training')
support_sched   = Transition(label='Support Scheduling')

# Define the loop for iterative firmware customization and sensor/motor calibration
# A = fw_upload, B = (sensor_setup -> motor_calib)
calib_order = StrictPartialOrder(nodes=[sensor_setup, motor_calib])
calib_order.order.add_edge(sensor_setup, motor_calib)
firmware_loop = OperatorPOWL(operator=Operator.LOOP, children=[fw_upload, calib_order])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    client_brief,
    component_src,
    parts_insp,
    frame_asm,
    battery_inst,
    firmware_loop,
    initial_test,
    stress_test,
    flight_sim,
    quality_audit,
    pack_prep,
    client_train,
    support_sched
])

# Define the control‐flow dependencies
root.order.add_edge(client_brief, component_src)
root.order.add_edge(component_src, parts_insp)
root.order.add_edge(parts_insp, frame_asm)
root.order.add_edge(frame_asm, battery_inst)
root.order.add_edge(battery_inst, firmware_loop)
root.order.add_edge(firmware_loop, initial_test)
root.order.add_edge(initial_test, stress_test)
root.order.add_edge(stress_test, flight_sim)
root.order.add_edge(flight_sim, quality_audit)
root.order.add_edge(quality_audit, pack_prep)
root.order.add_edge(pack_prep, client_train)
root.order.add_edge(client_train, support_sched)