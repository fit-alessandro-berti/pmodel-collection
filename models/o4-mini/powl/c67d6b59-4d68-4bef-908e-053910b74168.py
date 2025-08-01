# Generated from: c67d6b59-4d68-4bef-908e-053910b74168.json
# Description: This process outlines the intricate steps involved in designing, assembling, and delivering custom drones tailored to unique client specifications. It includes initial consultation, component sourcing from multiple vendors, precision assembly, multi-phase quality testing including flight simulation, software integration, and final client demonstration. The process also involves iterative adjustments based on client feedback, regulatory compliance checks, and specialized packaging for sensitive drone components. Each stage requires cross-functional collaboration between engineering, procurement, quality assurance, and customer service teams to ensure the drone meets all performance and safety standards before shipment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
client_meet     = Transition(label='Client Meet')
design_draft    = Transition(label='Design Draft')
vendor_select   = Transition(label='Vendor Select')
component_order = Transition(label='Component Order')
parts_inspect   = Transition(label='Parts Inspect')
frame_build     = Transition(label='Frame Build')
wiring_setup    = Transition(label='Wiring Setup')
software_load   = Transition(label='Software Load')
flight_sim      = Transition(label='Flight Sim')
quality_test    = Transition(label='Quality Test')
feedback_review = Transition(label='Feedback Review')
adjust_design   = Transition(label='Adjust Design')
compliance_check= Transition(label='Compliance Check')
packaging_prep  = Transition(label='Packaging Prep')
final_demo      = Transition(label='Final Demo')
ship_drone      = Transition(label='Ship Drone')

# Create the testing+feedback sequence for the loop's "A" part
test_sequence = StrictPartialOrder(nodes=[flight_sim, quality_test, feedback_review])
test_sequence.order.add_edge(flight_sim, quality_test)
test_sequence.order.add_edge(quality_test, feedback_review)

# Create the LOOP: execute test_sequence, then either exit or do adjust_design and repeat
testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_sequence, adjust_design])

# Build the main process partial order
root = StrictPartialOrder(nodes=[
    client_meet, design_draft, vendor_select, component_order,
    parts_inspect, frame_build, wiring_setup, software_load,
    testing_loop, compliance_check, packaging_prep, final_demo, ship_drone
])

# Define the control-flow (partial order edges)
root.order.add_edge(client_meet,    design_draft)
root.order.add_edge(design_draft,   vendor_select)
root.order.add_edge(vendor_select,  component_order)
root.order.add_edge(component_order, parts_inspect)
root.order.add_edge(parts_inspect,  frame_build)
root.order.add_edge(frame_build,    wiring_setup)
root.order.add_edge(wiring_setup,   software_load)
root.order.add_edge(software_load,  testing_loop)
root.order.add_edge(testing_loop,   compliance_check)
root.order.add_edge(compliance_check, packaging_prep)
root.order.add_edge(packaging_prep, final_demo)
root.order.add_edge(final_demo,     ship_drone)