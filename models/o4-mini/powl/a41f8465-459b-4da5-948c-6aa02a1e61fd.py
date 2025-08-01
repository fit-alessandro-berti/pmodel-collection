# Generated from: a41f8465-459b-4da5-948c-6aa02a1e61fd.json
# Description: This process outlines the intricate steps involved in designing, assembling, and testing customized drones tailored for specific client requirements. It begins with requirement gathering and concept design, followed by component sourcing that involves rare materials and specialized suppliers. The assembly phase integrates advanced electronics and precision mechanical parts, necessitating rigorous quality checks at each stage. Post-assembly, drones undergo environmental stress testing and software calibration to ensure optimal performance in diverse conditions. Final approval includes client demonstration and feedback incorporation before shipment. This atypical process demands coordination across engineering, procurement, and quality assurance teams to deliver bespoke unmanned aerial vehicles that meet stringent operational standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
req_gathering     = Transition(label='Req Gathering')
concept_design    = Transition(label='Concept Design')
supplier_vetting  = Transition(label='Supplier Vetting')
material_sourcing = Transition(label='Material Sourcing')
component_test    = Transition(label='Component Testing')
frame_assembly    = Transition(label='Frame Assembly')
electronics_install = Transition(label='Electronics Install')
wiring_setup      = Transition(label='Wiring Setup')
software_upload   = Transition(label='Software Upload')
calibration_check = Transition(label='Calibration Check')
stress_testing    = Transition(label='Stress Testing')
flight_simulation = Transition(label='Flight Simulation')
client_demo       = Transition(label='Client Demo')
feedback_fix      = Transition(label='Feedback Fix')
final_approval    = Transition(label='Final Approval')
packaging_ship    = Transition(label='Packaging Ship')

# Build the partial order
root = StrictPartialOrder(nodes=[
    req_gathering,
    concept_design,
    supplier_vetting,
    material_sourcing,
    component_test,
    frame_assembly,
    electronics_install,
    wiring_setup,
    software_upload,
    calibration_check,
    stress_testing,
    flight_simulation,
    client_demo,
    feedback_fix,
    final_approval,
    packaging_ship
])

# Define dependencies
o = root.order
o.add_edge(req_gathering, concept_design)
o.add_edge(concept_design, supplier_vetting)
o.add_edge(concept_design, material_sourcing)
o.add_edge(supplier_vetting, component_test)
o.add_edge(material_sourcing, component_test)
o.add_edge(component_test, frame_assembly)
o.add_edge(frame_assembly, electronics_install)
o.add_edge(electronics_install, wiring_setup)
o.add_edge(wiring_setup, software_upload)
o.add_edge(software_upload, calibration_check)
o.add_edge(calibration_check, stress_testing)
o.add_edge(stress_testing, flight_simulation)
o.add_edge(flight_simulation, client_demo)
o.add_edge(client_demo, feedback_fix)
o.add_edge(feedback_fix, final_approval)
o.add_edge(final_approval, packaging_ship)