# Generated from: ffd2b596-7887-4ac3-bdb3-35c150e0cb58.json
# Description: This process outlines the complex and highly customized assembly of drones tailored for specific environmental conditions and client requirements. It begins with detailed component sourcing, followed by precision calibration of sensors and motors. Quality assurance is integrated at multiple stages to ensure durability under varied weather conditions. Software integration involves adaptive flight algorithms that adjust to real-time data inputs. Final testing simulates extreme operational scenarios before packaging and logistics coordination for global distribution. Throughout, cross-functional teams collaborate closely to manage supply chain variability and maintain compliance with international aviation standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
comp_src        = Transition(label='Component Sourcing')
frame_build     = Transition(label='Frame Build')
sensor_calib    = Transition(label='Sensor Calibrate')
motor_assembly  = Transition(label='Motor Assembly')
battery_int     = Transition(label='Battery Integrate')
software_inst   = Transition(label='Software Install')
algo_tune       = Transition(label='Algorithm Tune')
signal_test     = Transition(label='Signal Test')
flight_sim      = Transition(label='Flight Simulate')
durability_chk  = Transition(label='Durability Check')
quality_insp    = Transition(label='Quality Inspect')
compliance_rev  = Transition(label='Compliance Review')
pack_prep       = Transition(label='Packaging Prep')
logistics_pl    = Transition(label='Logistics Plan')
client_feedback = Transition(label='Client Feedback')

# Build the loop body (B): testing → simulation → durability → inspection → compliance
loop_body = StrictPartialOrder(nodes=[
    signal_test, flight_sim, durability_chk, quality_insp, compliance_rev
])
loop_body.order.add_edge(signal_test,   flight_sim)
loop_body.order.add_edge(flight_sim,     durability_chk)
loop_body.order.add_edge(durability_chk, quality_insp)
loop_body.order.add_edge(quality_insp,   compliance_rev)

# Build the LOOP operator: tune algorithm, then optionally run the loop body and retune
tuning_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[algo_tune, loop_body]
)

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    comp_src, frame_build, sensor_calib, motor_assembly,
    battery_int, software_inst, tuning_loop,
    pack_prep, logistics_pl, client_feedback
])

# Define the control-flow / data dependencies
# 1) Component sourcing before frame build, sensor calibration, motor assembly
root.order.add_edge(comp_src,       frame_build)
root.order.add_edge(comp_src,       sensor_calib)
root.order.add_edge(comp_src,       motor_assembly)

# 2) Frame build & motor assembly before battery integration
root.order.add_edge(frame_build,    battery_int)
root.order.add_edge(motor_assembly, battery_int)

# 3) Sensor calibration & battery integration before software install
root.order.add_edge(sensor_calib,   software_inst)
root.order.add_edge(battery_int,    software_inst)

# 4) Software install before algorithm tuning (loop head)
root.order.add_edge(software_inst, tuning_loop)

# 5) After tuning loop completes, proceed to packaging & logistics in parallel
root.order.add_edge(tuning_loop, pack_prep)
root.order.add_edge(tuning_loop, logistics_pl)

# 6) Packaging & logistics before final client feedback
root.order.add_edge(pack_prep,       client_feedback)
root.order.add_edge(logistics_pl,    client_feedback)