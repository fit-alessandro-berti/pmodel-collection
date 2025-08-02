# Generated from: 9eb2eabc-7c50-4710-b772-a6198654b1e7.json
# Description: This process outlines the end-to-end assembly of custom drones tailored to specific client requirements. It involves initial design consultation, component sourcing from multiple suppliers, firmware customization, iterative prototype testing, regulatory compliance checks, final quality assurance, and packaging. The process also includes dynamic risk assessment, supply chain adjustments based on inventory fluctuations, and post-production client training to ensure proper drone operation. Each stage requires coordination among engineering, procurement, and logistics teams to deliver a fully functional, reliable drone solution meeting both performance and safety standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Design_Brief = Transition(label='Design Brief')
Component_Sourcing = Transition(label='Component Sourcing')
Firmware_Setup = Transition(label='Firmware Setup')
Prototype_Build = Transition(label='Prototype Build')
Flight_Testing = Transition(label='Flight Testing')
Regulatory_Review = Transition(label='Regulatory Review')
Risk_Assessment = Transition(label='Risk Assessment')
Supplier_Audit = Transition(label='Supplier Audit')
Inventory_Check = Transition(label='Inventory Check')
Quality_Control = Transition(label='Quality Control')
Packaging_Prep = Transition(label='Packaging Prep')
Client_Training = Transition(label='Client Training')
Feedback_Review = Transition(label='Feedback Review')
Production_Ramp = Transition(label='Production Ramp')
Shipping_Schedule = Transition(label='Shipping Schedule')

# Model the loop for iterative prototype testing and regulatory review:
# Loop body: Prototype Build -> Flight Testing -> Regulatory Review -> Risk Assessment (dynamic risk assessment after regulatory checks)
proto_test_seq = StrictPartialOrder(nodes=[Prototype_Build, Flight_Testing, Regulatory_Review, Risk_Assessment])
proto_test_seq.order.add_edge(Prototype_Build, Flight_Testing)
proto_test_seq.order.add_edge(Flight_Testing, Regulatory_Review)
proto_test_seq.order.add_edge(Regulatory_Review, Risk_Assessment)

# The loop: execute prototype testing sequence, then choose exit or do supplier audit + inventory check then redo prototype testing
supplier_inventory = StrictPartialOrder(nodes=[Supplier_Audit, Inventory_Check])
# Supplier Audit and Inventory Check concurrent (both sourcing side checks)
# So no ordering edges => concurrent

# The body to repeat: supplier_inventory then prototype testing sequence again
body_loop = StrictPartialOrder(nodes=[supplier_inventory, proto_test_seq])
# supplier_inventory before prototype testing sequence in next iteration
body_loop.order.add_edge(supplier_inventory, proto_test_seq)

loop_testing = OperatorPOWL(operator=Operator.LOOP, children=[proto_test_seq, body_loop])

# Assemble main flow (partial order with coordination of teams)
# From Design Brief to Component Sourcing and Firmware Setup (parallel after design)
design_to_sources = StrictPartialOrder(nodes=[Design_Brief, Component_Sourcing, Firmware_Setup])
design_to_sources.order.add_edge(Design_Brief, Component_Sourcing)
design_to_sources.order.add_edge(Design_Brief, Firmware_Setup)

# After sourcing and firmware setup, do prototype testing loop
after_proto_loop = OperatorPOWL(operator=Operator.XOR, children=[loop_testing, SilentTransition()]) # optional looping (exit loop)

# Feedback Review and Production Ramp after loop exit
feedback_and_production = StrictPartialOrder(nodes=[Feedback_Review, Production_Ramp])
feedback_and_production.order.add_edge(Feedback_Review, Production_Ramp)

# Quality Control after production ramp
# Packaging Prep after Quality Control
qc_packaging = StrictPartialOrder(nodes=[Quality_Control, Packaging_Prep])
qc_packaging.order.add_edge(Quality_Control, Packaging_Prep)

# Shipping Schedule after packaging
# Client Training after shipping schedule (post-production client training)
shipping_to_training = StrictPartialOrder(nodes=[Shipping_Schedule, Client_Training])
shipping_to_training.order.add_edge(Shipping_Schedule, Client_Training)

# Full order top-level assembly
top_level = StrictPartialOrder(nodes=[
    design_to_sources,
    after_proto_loop,
    feedback_and_production,
    qc_packaging,
    shipping_to_training
])

# Link partial orders respecting logical process flow
top_level.order.add_edge(design_to_sources, after_proto_loop)
top_level.order.add_edge(after_proto_loop, feedback_and_production)
top_level.order.add_edge(feedback_and_production, qc_packaging)
top_level.order.add_edge(qc_packaging, shipping_to_training)

root = top_level