# Generated from: d7288683-2666-4c15-88a1-85e659489353.json
# Description: This process details the end-to-end assembly and customization of bespoke drones tailored for specialized industrial applications. Starting from component sourcing, the workflow includes precision calibration, firmware integration, environmental stress testing, and adaptive AI module installation. Each drone undergoes iterative flight pattern optimization based on simulated mission profiles before final quality assurance and packaging. This atypical process requires coordination across mechanical, software, and electronics teams to ensure each unit meets unique client specifications and regulatory compliance, culminating in secure delivery logistics.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
comp_src        = Transition(label='Component Sourcing')
frame_asm       = Transition(label='Frame Assembly')
motor_inst      = Transition(label='Motor Installation')
sensor_mount    = Transition(label='Sensor Mounting')
wiring_setup    = Transition(label='Wiring Setup')
calibration     = Transition(label='Calibration Phase')
firmware_upload = Transition(label='Firmware Upload')
stress_test     = Transition(label='Stress Testing')
ai_module       = Transition(label='AI Module')
flight_sim      = Transition(label='Flight Simulation')
pattern_adj     = Transition(label='Pattern Adjustment')
quality_inspect = Transition(label='Quality Inspect')
compliance_chk  = Transition(label='Compliance Check')
packaging_fin   = Transition(label='Packaging Final')
delivery_setup  = Transition(label='Delivery Setup')

# Build the loop for iterative flight optimization:
# Execute flight_sim, then optionally exit or do pattern_adj and repeat
flight_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[flight_sim, pattern_adj]
)

# Assemble the overall partial order
root = StrictPartialOrder(
    nodes=[
        comp_src,
        frame_asm,
        motor_inst,
        sensor_mount,
        wiring_setup,
        calibration,
        firmware_upload,
        stress_test,
        ai_module,
        flight_loop,
        quality_inspect,
        compliance_chk,
        packaging_fin,
        delivery_setup
    ]
)

# Define the control‐flow (precedence) relations
o = root.order
o.add_edge(comp_src, frame_asm)
o.add_edge(frame_asm, motor_inst)
o.add_edge(motor_inst, sensor_mount)
o.add_edge(sensor_mount, wiring_setup)
o.add_edge(wiring_setup, calibration)
o.add_edge(calibration, firmware_upload)
o.add_edge(firmware_upload, stress_test)
o.add_edge(stress_test, ai_module)
o.add_edge(ai_module, flight_loop)
o.add_edge(flight_loop, quality_inspect)
o.add_edge(quality_inspect, compliance_chk)
o.add_edge(compliance_chk, packaging_fin)
o.add_edge(packaging_fin, delivery_setup)