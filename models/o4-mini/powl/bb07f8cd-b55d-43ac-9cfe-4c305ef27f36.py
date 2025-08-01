# Generated from: bb07f8cd-b55d-43ac-9cfe-4c305ef27f36.json
# Description: This process outlines the steps involved in commissioning a custom piece of artwork from initial client inquiry through final delivery and post-sale support. It begins with client briefing and concept development, followed by iterative design approvals and material sourcing. Mid-process includes detailed progress updates, client feedback incorporation, and quality assurance checks. Once the artwork is completed, logistics coordination ensures safe packaging and shipping. Finally, the process concludes with client satisfaction surveys and optional framing or installation services, ensuring a tailored, high-quality art experience that meets unique client needs while maintaining artist standards and timelines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
client_inquiry    = Transition(label='Client Inquiry')
brief_gathering   = Transition(label='Brief Gathering')
concept_sketch    = Transition(label='Concept Sketch')
design_review     = Transition(label='Design Review')
material_sourcing = Transition(label='Material Sourcing')
progress_update   = Transition(label='Progress Update')
feedback_loop     = Transition(label='Feedback Loop')
midway_approval   = Transition(label='Midway Approval')
detail_refinement = Transition(label='Detail Refinement')
quality_check     = Transition(label='Quality Check')
final_approval    = Transition(label='Final Approval')
packaging_prep    = Transition(label='Packaging Prep')
shipping_arrange  = Transition(label='Shipping Arrange')
delivery_confirm  = Transition(label='Delivery Confirm')
satisfaction_survey = Transition(label='Satisfaction Survey')
installation_setup  = Transition(label='Installation Setup')

# Silent transition for optional installation
skip = SilentTransition()

# Loop for design-review cycles: do Design Review, then optionally Feedback Loop -> Detail Refinement, repeat
design_loop_body = StrictPartialOrder(nodes=[feedback_loop, detail_refinement])
design_loop_body.order.add_edge(feedback_loop, detail_refinement)
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_review, design_loop_body])

# XOR for optional installation after satisfaction survey
xor_install = OperatorPOWL(operator=Operator.XOR, children=[installation_setup, skip])

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        client_inquiry,
        brief_gathering,
        concept_sketch,
        design_loop,
        midway_approval,
        material_sourcing,
        progress_update,
        quality_check,
        final_approval,
        packaging_prep,
        shipping_arrange,
        delivery_confirm,
        satisfaction_survey,
        xor_install
    ]
)

# Define the control-flow dependencies
root.order.add_edge(client_inquiry, brief_gathering)
root.order.add_edge(brief_gathering, concept_sketch)
root.order.add_edge(concept_sketch, design_loop)
root.order.add_edge(design_loop, midway_approval)
root.order.add_edge(midway_approval, material_sourcing)
root.order.add_edge(material_sourcing, progress_update)
root.order.add_edge(progress_update, quality_check)
root.order.add_edge(quality_check, final_approval)
root.order.add_edge(final_approval, packaging_prep)
root.order.add_edge(packaging_prep, shipping_arrange)
root.order.add_edge(shipping_arrange, delivery_confirm)
root.order.add_edge(delivery_confirm, satisfaction_survey)
root.order.add_edge(satisfaction_survey, xor_install)