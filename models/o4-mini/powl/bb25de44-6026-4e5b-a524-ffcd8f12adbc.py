# Generated from: bb25de44-6026-4e5b-a524-ffcd8f12adbc.json
# Description: This process involves the intricate assembly and configuration of custom drones tailored for specialized industrial applications. It begins with the selection of bespoke components based on client specifications, followed by precision soldering of circuit boards and integration of unique sensor arrays. The workflow includes rigorous software calibration, iterative flight testing in controlled environments, and adaptive firmware updates. Quality assurance teams perform environmental stress simulations and cross-system compatibility checks before final packaging. The process concludes with personalized documentation and client training sessions to ensure optimal operational use in diverse scenarios.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
component_select  = Transition(label='Component Select')
frame_assemble    = Transition(label='Frame Assemble')
circuit_solder    = Transition(label='Circuit Solder')
sensor_install    = Transition(label='Sensor Install')
software_upload   = Transition(label='Software Upload')
calibration_run   = Transition(label='Calibration Run')
flight_testing    = Transition(label='Flight Testing')
firmware_update   = Transition(label='Firmware Update')
battery_configure = Transition(label='Battery Configure')
signal_optimize   = Transition(label='Signal Optimize')
stress_simulate   = Transition(label='Stress Simulate')
compatibility_check = Transition(label='Compatibility Check')
quality_inspect   = Transition(label='Quality Inspect')
packaging_final   = Transition(label='Packaging Final')
documentation_prep = Transition(label='Documentation Prep')
client_training   = Transition(label='Client Training')

# Concurrent configuration tasks after calibration
config_po = StrictPartialOrder(nodes=[battery_configure, signal_optimize])
# No order edges: battery_configure and signal_optimize can run in parallel

# Loop for iterative flight testing and firmware update
loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_testing, firmware_update])

# Root partial order
root = StrictPartialOrder(nodes=[
    component_select,
    frame_assemble,
    circuit_solder,
    sensor_install,
    software_upload,
    calibration_run,
    config_po,
    loop,
    stress_simulate,
    compatibility_check,
    quality_inspect,
    packaging_final,
    documentation_prep,
    client_training
])

# Define the control-flow dependencies
root.order.add_edge(component_select, frame_assemble)
root.order.add_edge(frame_assemble, circuit_solder)
root.order.add_edge(circuit_solder, sensor_install)
root.order.add_edge(sensor_install, software_upload)
root.order.add_edge(software_upload, calibration_run)
root.order.add_edge(calibration_run, config_po)
root.order.add_edge(config_po, loop)
root.order.add_edge(loop, stress_simulate)
root.order.add_edge(stress_simulate, compatibility_check)
root.order.add_edge(compatibility_check, quality_inspect)
root.order.add_edge(quality_inspect, packaging_final)
root.order.add_edge(packaging_final, documentation_prep)
root.order.add_edge(documentation_prep, client_training)