# Generated from: 77cdac2d-1a40-406c-9218-ee518a8b18e0.json
# Description: This process covers the end-to-end assembly of custom drones tailored to client specifications. It involves initial client consultation to determine unique requirements, followed by component sourcing from specialized suppliers. The process continues with prototype design, iterative testing with embedded AI software, and precision mechanical assembly. Quality assurance includes environmental stress tests and real-world flight simulations. After successful validation, drones undergo final calibration, packaging, and logistics coordination for delivery. Post-delivery support includes remote diagnostics and firmware updates, ensuring optimal performance and client satisfaction over the drone's lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
client_consult = Transition(label='Client Consult')
specs_review = Transition(label='Specs Review')
supplier_vetting = Transition(label='Supplier Vetting')
order_components = Transition(label='Order Components')
prototype_design = Transition(label='Prototype Design')
software_embed = Transition(label='Software Embed')
mechanical_build = Transition(label='Mechanical Build')
initial_testing = Transition(label='Initial Testing')
ai_optimization = Transition(label='AI Optimization')
stress_testing = Transition(label='Stress Testing')
flight_simulate = Transition(label='Flight Simulate')
quality_audit = Transition(label='Quality Audit')
final_calibrate = Transition(label='Final Calibrate')
package_drone = Transition(label='Package Drone')
arrange_shipping = Transition(label='Arrange Shipping')
post_support = Transition(label='Post Support')
firmware_update = Transition(label='Firmware Update')

# Loop for iterative testing with AI optimization:
# Loop = * ( Initial Testing, AI Optimization )
loop_testing = OperatorPOWL(
    operator=Operator.LOOP,
    children=[initial_testing, ai_optimization]
)

# Quality Assurance partial order:
# Stress Testing & Flight Simulate in parallel, both must finish before Quality Audit
qa_po = StrictPartialOrder(
    nodes=[stress_testing, flight_simulate, quality_audit]
)
qa_po.order.add_edge(stress_testing, quality_audit)
qa_po.order.add_edge(flight_simulate, quality_audit)

# Final steps partial order:
final_po = StrictPartialOrder(
    nodes=[final_calibrate, package_drone, arrange_shipping]
)
final_po.order.add_edge(final_calibrate, package_drone)
final_po.order.add_edge(package_drone, arrange_shipping)

# Post delivery support partial order (sequential)
post_support_po = StrictPartialOrder(
    nodes=[post_support, firmware_update]
)
post_support_po.order.add_edge(post_support, firmware_update)

# Assemble main partial order nodes
nodes = [
    client_consult,
    specs_review,
    supplier_vetting,
    order_components,
    prototype_design,
    software_embed,
    mechanical_build,
    loop_testing,
    qa_po,
    final_po,
    post_support_po
]

root = StrictPartialOrder(nodes=nodes)

# Define control flow (precedence edges)
root.order.add_edge(client_consult, specs_review)
root.order.add_edge(specs_review, supplier_vetting)
root.order.add_edge(supplier_vetting, order_components)
root.order.add_edge(order_components, prototype_design)
root.order.add_edge(prototype_design, software_embed)
root.order.add_edge(software_embed, mechanical_build)
root.order.add_edge(mechanical_build, loop_testing)        # loop_testing: iterative testing
root.order.add_edge(loop_testing, qa_po)                  # QA after testing loop
root.order.add_edge(qa_po, final_po)                      # final calibrate and packaging after QA
root.order.add_edge(final_po, post_support_po)            # post delivery support after shipping