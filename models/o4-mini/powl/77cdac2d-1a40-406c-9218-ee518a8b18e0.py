# Generated from: 77cdac2d-1a40-406c-9218-ee518a8b18e0.json
# Description: This process covers the end-to-end assembly of custom drones tailored to client specifications. It involves initial client consultation to determine unique requirements, followed by component sourcing from specialized suppliers. The process continues with prototype design, iterative testing with embedded AI software, and precision mechanical assembly. Quality assurance includes environmental stress tests and real-world flight simulations. After successful validation, drones undergo final calibration, packaging, and logistics coordination for delivery. Post-delivery support includes remote diagnostics and firmware updates, ensuring optimal performance and client satisfaction over the drone's lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
client_consult   = Transition(label='Client Consult')
specs_review     = Transition(label='Specs Review')
supplier_vetting = Transition(label='Supplier Vetting')
order_components = Transition(label='Order Components')
prototype_design = Transition(label='Prototype Design')
software_embed   = Transition(label='Software Embed')
mechanical_build = Transition(label='Mechanical Build')
initial_testing  = Transition(label='Initial Testing')
ai_optimization  = Transition(label='AI Optimization')
stress_testing   = Transition(label='Stress Testing')
flight_simulate  = Transition(label='Flight Simulate')
quality_audit    = Transition(label='Quality Audit')
final_calibrate  = Transition(label='Final Calibrate')
package_drone    = Transition(label='Package Drone')
arrange_shipping = Transition(label='Arrange Shipping')
post_support     = Transition(label='Post Support')
firmware_update  = Transition(label='Firmware Update')

# Loop for iterative testing and AI optimization
loop_test_opt = OperatorPOWL(
    operator=Operator.LOOP,
    children=[initial_testing, ai_optimization]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    client_consult,
    specs_review,
    supplier_vetting,
    order_components,
    prototype_design,
    software_embed,
    loop_test_opt,
    mechanical_build,
    stress_testing,
    flight_simulate,
    quality_audit,
    final_calibrate,
    package_drone,
    arrange_shipping,
    post_support,
    firmware_update
])

# Define the control-flow edges
o = root.order
o.add_edge(client_consult, specs_review)
o.add_edge(specs_review, supplier_vetting)
o.add_edge(supplier_vetting, order_components)
o.add_edge(order_components, prototype_design)
o.add_edge(prototype_design, software_embed)
o.add_edge(software_embed, loop_test_opt)
o.add_edge(loop_test_opt, mechanical_build)
o.add_edge(mechanical_build, stress_testing)
o.add_edge(stress_testing, flight_simulate)
o.add_edge(flight_simulate, quality_audit)
o.add_edge(quality_audit, final_calibrate)
o.add_edge(final_calibrate, package_drone)
o.add_edge(package_drone, arrange_shipping)
o.add_edge(arrange_shipping, post_support)
o.add_edge(post_support, firmware_update)