# Generated from: 4719141e-9342-437c-ba9e-39d0edee4df3.json
# Description: This process involves the design, customization, and assembly of bespoke drones tailored to specific client requirements. It includes initial consultation to determine unique operational needs, iterative prototype development, component sourcing from multiple suppliers, software customization, rigorous testing under various environmental conditions, regulatory compliance verification, and final quality assurance before delivery. Post-delivery support and firmware updates are also integrated into the process to ensure optimal performance and client satisfaction over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
client_consult    = Transition(label='Client Consult')
needs_analysis   = Transition(label='Needs Analysis')
component_source = Transition(label='Component Sourcing')
design_draft     = Transition(label='Design Draft')
prototype_build  = Transition(label='Prototype Build')
software_setup   = Transition(label='Software Setup')
firmware_install = Transition(label='Firmware Install')
initial_testing  = Transition(label='Initial Testing')
design_review    = Transition(label='Design Review')
compliance_check = Transition(label='Compliance Check')
environmental_test = Transition(label='Environmental Test')
quality_audit    = Transition(label='Quality Audit')
final_assembly   = Transition(label='Final Assembly')
delivery_schedule = Transition(label='Delivery Schedule')
client_training  = Transition(label='Client Training')
post_support     = Transition(label='Post Support')
firmware_update  = Transition(label='Firmware Update')

# Loop for the iterative prototype/design cycle:
#   init  = Design Draft
#   body  = Prototype Build -> Software Setup -> Firmware Install -> Initial Testing -> Design Review
design_loop_init = StrictPartialOrder(
    nodes=[design_draft]
)

design_loop_body = StrictPartialOrder(
    nodes=[
        prototype_build,
        software_setup,
        firmware_install,
        initial_testing,
        design_review
    ]
)
design_loop_body.order.add_edge(prototype_build, software_setup)
design_loop_body.order.add_edge(software_setup, firmware_install)
design_loop_body.order.add_edge(firmware_install, initial_testing)
design_loop_body.order.add_edge(initial_testing, design_review)

design_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[design_loop_init, design_loop_body]
)

# Sequential block for compliance and final assembly stages
compliance_block = StrictPartialOrder(
    nodes=[
        compliance_check,
        environmental_test,
        quality_audit,
        final_assembly
    ]
)
compliance_block.order.add_edge(compliance_check, environmental_test)
compliance_block.order.add_edge(environmental_test, quality_audit)
compliance_block.order.add_edge(quality_audit, final_assembly)

# Loop for post-delivery support & firmware updates
post_delivery_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[post_support, firmware_update]
)

# Build the overall process as a partial order
root = StrictPartialOrder(
    nodes=[
        client_consult,
        needs_analysis,
        component_source,
        design_loop,
        compliance_block,
        delivery_schedule,
        client_training,
        post_delivery_loop
    ]
)
# Define the high-level sequencing
root.order.add_edge(client_consult, needs_analysis)
root.order.add_edge(needs_analysis, component_source)
root.order.add_edge(component_source, design_loop)
root.order.add_edge(design_loop, compliance_block)
root.order.add_edge(compliance_block, delivery_schedule)
root.order.add_edge(delivery_schedule, client_training)
root.order.add_edge(client_training, post_delivery_loop)