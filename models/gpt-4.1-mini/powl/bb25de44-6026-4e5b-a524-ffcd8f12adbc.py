# Generated from: bb25de44-6026-4e5b-a524-ffcd8f12adbc.json
# Description: This process involves the intricate assembly and configuration of custom drones tailored for specialized industrial applications. It begins with the selection of bespoke components based on client specifications, followed by precision soldering of circuit boards and integration of unique sensor arrays. The workflow includes rigorous software calibration, iterative flight testing in controlled environments, and adaptive firmware updates. Quality assurance teams perform environmental stress simulations and cross-system compatibility checks before final packaging. The process concludes with personalized documentation and client training sessions to ensure optimal operational use in diverse scenarios.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Component_Select = Transition(label='Component Select')
Circuit_Solder = Transition(label='Circuit Solder')
Sensor_Install = Transition(label='Sensor Install')
Frame_Assemble = Transition(label='Frame Assemble')
Software_Upload = Transition(label='Software Upload')
Calibration_Run = Transition(label='Calibration Run')
Flight_Testing = Transition(label='Flight Testing')
Firmware_Update = Transition(label='Firmware Update')
Stress_Simulate = Transition(label='Stress Simulate')
Compatibility_Check = Transition(label='Compatibility Check')
Battery_Configure = Transition(label='Battery Configure')
Signal_Optimize = Transition(label='Signal Optimize')
Quality_Inspect = Transition(label='Quality Inspect')
Documentation_Prep = Transition(label='Documentation Prep')
Client_Training = Transition(label='Client Training')
Packaging_Final = Transition(label='Packaging Final')

# Assembly partial order:
# From description:
# Selection → soldering → sensor install → frame assembly
assembly_nodes = [
    Component_Select,
    Circuit_Solder,
    Sensor_Install,
    Frame_Assemble
]

assembly = StrictPartialOrder(nodes=assembly_nodes)
assembly.order.add_edge(Component_Select, Circuit_Solder)
assembly.order.add_edge(Circuit_Solder, Sensor_Install)
assembly.order.add_edge(Sensor_Install, Frame_Assemble)

# Software calibration loop:
# Software_Upload then iterative (Calibration_Run then Flight_Testing then Firmware_Update)
# modeled as LOOP(Software_Upload, PO(Calibration_Run, Flight_Testing, Firmware_Update))
# firmware update is after flight testing, and calibration run before flight testing,
# all in sequence during the loop body.
# We'll create the loop body first as PO

loop_body_nodes = [Calibration_Run, Flight_Testing, Firmware_Update]
loop_body = StrictPartialOrder(nodes=loop_body_nodes)
loop_body.order.add_edge(Calibration_Run, Flight_Testing)
loop_body.order.add_edge(Flight_Testing, Firmware_Update)

software_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Software_Upload, loop_body]
)

# Quality assurance:
# Stress_Simulate and Compatibility_Check performed by QA team before final packaging
# no explicit order between stress simulate and compatibility check (parallel)
# then Quality_Inspect after these two
quality_assurance_nodes = [
    Stress_Simulate,
    Compatibility_Check,
    Quality_Inspect
]
quality_assurance = StrictPartialOrder(nodes=quality_assurance_nodes)
quality_assurance.order.add_edge(Stress_Simulate, Quality_Inspect)
quality_assurance.order.add_edge(Compatibility_Check, Quality_Inspect)

# Battery and Signal (Battery_Configure and Signal_Optimize) likely concurrent after assembly and software_loop,
# we'll let them proceed concurrently before quality inspect
battery_signal_nodes = [Battery_Configure, Signal_Optimize]
battery_signal = StrictPartialOrder(nodes=battery_signal_nodes)  # no order edges, fully parallel

# Documentation and training parallel after quality inspection
doc_training_nodes = [Documentation_Prep, Client_Training]
doc_training = StrictPartialOrder(nodes=doc_training_nodes)  # parallel activities

# Final packaging after documentation and client training
# packaging_final after both documentation and training completed

# Now combine all in order:

# Step 1: assembly
# Step 2: software calibration loop
# Step 3: battery configure & signal optimize concurrent
# Step 4: quality assurance
# Step 5: documentation and client training concurrent
# Step 6: packaging final

# Create higher-level PO with all nodes
# We'll put children nodes inline and link edges accordingly

high_nodes = [
    assembly,
    software_loop,
    battery_signal,
    quality_assurance,
    doc_training,
    Packaging_Final
]

root = StrictPartialOrder(nodes=high_nodes)

# Define order edges:

# assembly --> software_loop
root.order.add_edge(assembly, software_loop)

# software_loop --> battery_signal and quality_assurance
# battery and signal configure before QA (both before QA seems logical)
root.order.add_edge(software_loop, battery_signal)
root.order.add_edge(battery_signal, quality_assurance)

# quality_assurance --> documentation and training
root.order.add_edge(quality_assurance, doc_training)

# documentation and training --> packaging final
root.order.add_edge(doc_training, Packaging_Final)