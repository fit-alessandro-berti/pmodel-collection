# Generated from: 0cd807f8-e76a-4965-9d27-8c92ce6d200f.json
# Description: This process involves the bespoke assembly of drones tailored to specific client requirements, integrating unique hardware and software components. It starts with requirement analysis, followed by parts sourcing from specialized vendors, custom frame fabrication, and component integration. Quality testing includes flight simulation and endurance trials. Final steps feature software calibration, safety certification, and packaging for delivery. The process requires coordination among design, engineering, procurement, and quality assurance teams to ensure each drone meets precise operational standards while maintaining adaptability for future upgrades and modifications.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
req_sync = Transition(label='Requirement Sync')
vendor_audit = Transition(label='Vendor Audit')
part_sourcing = Transition(label='Part Sourcing')
frame_design = Transition(label='Frame Design')
material_cut = Transition(label='Material Cut')
component_fit = Transition(label='Component Fit')
wiring_setup = Transition(label='Wiring Setup')
battery_install = Transition(label='Battery Install')
firmware_load = Transition(label='Firmware Load')
initial_testing = Transition(label='Initial Testing')
flight_sim = Transition(label='Flight Sim')
endurance_test = Transition(label='Endurance Test')
software_tune = Transition(label='Software Tune')
safety_cert = Transition(label='Safety Cert')
final_pack = Transition(label='Final Pack')

# Build the partially ordered workflow
root = StrictPartialOrder(nodes=[
    req_sync,
    vendor_audit,
    part_sourcing,
    frame_design,
    material_cut,
    component_fit,
    wiring_setup,
    battery_install,
    firmware_load,
    initial_testing,
    flight_sim,
    endurance_test,
    software_tune,
    safety_cert,
    final_pack
])

# Dependencies

# After requirement sync, procurement and design branches start
root.order.add_edge(req_sync, vendor_audit)
root.order.add_edge(req_sync, frame_design)

# Procurement branch: vendor audit -> part sourcing
root.order.add_edge(vendor_audit, part_sourcing)

# Design/fabrication branch: frame design -> material cut
root.order.add_edge(frame_design, material_cut)

# Converge both branches into component fitting
root.order.add_edge(part_sourcing, component_fit)
root.order.add_edge(material_cut, component_fit)

# Assembly sequence
root.order.add_edge(component_fit, wiring_setup)
root.order.add_edge(wiring_setup, battery_install)
root.order.add_edge(battery_install, firmware_load)

# Testing sequence: load firmware -> initial testing -> parallel tests
root.order.add_edge(firmware_load, initial_testing)
root.order.add_edge(initial_testing, flight_sim)
root.order.add_edge(initial_testing, endurance_test)

# After both tests, do software calibration
root.order.add_edge(flight_sim, software_tune)
root.order.add_edge(endurance_test, software_tune)

# Final steps: software tune -> safety cert -> packaging
root.order.add_edge(software_tune, safety_cert)
root.order.add_edge(safety_cert, final_pack)