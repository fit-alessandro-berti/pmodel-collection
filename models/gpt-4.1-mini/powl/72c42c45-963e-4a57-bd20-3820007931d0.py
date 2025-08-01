# Generated from: 72c42c45-963e-4a57-bd20-3820007931d0.json
# Description: This process outlines the end-to-end workflow for assembling bespoke drones tailored to client specifications. It begins with design consultation and component sourcing, followed by precision machining and custom firmware development. Each drone undergoes iterative calibration and environmental testing to ensure performance under diverse conditions. The process integrates real-time feedback loops between assembly and software teams to address emerging issues. Final steps include packaging with personalized branding and coordinated logistics for delivery, ensuring each unit meets stringent quality and regulatory standards before reaching the customer. This atypical yet practical process combines hardware craft, software innovation, and supply chain agility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition objects
client_brief = Transition(label='Client Brief')
design_draft = Transition(label='Design Draft')
part_sourcing = Transition(label='Part Sourcing')
machining_parts = Transition(label='Machining Parts')
firmware_dev = Transition(label='Firmware Dev')
hardware_assembling = Transition(label='Hardware Assembling')
initial_testing = Transition(label='Initial Testing')
calibration_loop = Transition(label='Calibration Loop')
enviro_testing = Transition(label='Enviro Testing')
software_tuning = Transition(label='Software Tuning')
quality_audit = Transition(label='Quality Audit')
brand_packaging = Transition(label='Brand Packaging')
logistics_plan = Transition(label='Logistics Plan')
final_review = Transition(label='Final Review')
customer_handover = Transition(label='Customer Handover')

# Define the loop of calibration & testing with feedback on software tuning
# Loop body: Calibration Loop + Enviro Testing, then choice to exit or software tuning then retry

# The loop is: * (Body, Software Tuning)
calibration_test_po = StrictPartialOrder(nodes=[calibration_loop, enviro_testing])
# calibration_loop and enviro_testing are concurrent, no order between them
# Real-time feedback: hardware assembly <-> software tuning, we model this by a partial order edge from initial testing to software tuning
# but software tuning is inside loop; model the loop first

# Loop node with body being partial order of calibration_loop and enviro_testing run concurrently
loop_body = calibration_test_po
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, software_tuning])

# Now build main partial order reflecting process flow:
# Client Brief -> Design Draft -> Part Sourcing -> Machining Parts -> Firmware Dev -> Hardware Assembling -> Initial Testing -> loop_node -> Quality Audit -> Brand Packaging -> Logistics Plan -> Final Review -> Customer Handover

root = StrictPartialOrder(
    nodes=[
        client_brief,
        design_draft,
        part_sourcing,
        machining_parts,
        firmware_dev,
        hardware_assembling,
        initial_testing,
        loop_node,
        quality_audit,
        brand_packaging,
        logistics_plan,
        final_review,
        customer_handover,
    ]
)

# Add edges to model the sequential dependencies
root.order.add_edge(client_brief, design_draft)
root.order.add_edge(design_draft, part_sourcing)
root.order.add_edge(part_sourcing, machining_parts)
root.order.add_edge(machining_parts, firmware_dev)
root.order.add_edge(firmware_dev, hardware_assembling)
root.order.add_edge(hardware_assembling, initial_testing)

# Initial Testing precedes the calibration & testing loop
root.order.add_edge(initial_testing, loop_node)

# After loop ends, go to quality audit
root.order.add_edge(loop_node, quality_audit)
root.order.add_edge(quality_audit, brand_packaging)
root.order.add_edge(brand_packaging, logistics_plan)
root.order.add_edge(logistics_plan, final_review)
root.order.add_edge(final_review, customer_handover)