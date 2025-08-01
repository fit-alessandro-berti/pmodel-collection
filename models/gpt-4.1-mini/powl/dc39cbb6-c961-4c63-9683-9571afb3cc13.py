# Generated from: dc39cbb6-c961-4c63-9683-9571afb3cc13.json
# Description: This process outlines the workflow for managing custom art commissions from initial client inquiry through to final delivery and post-sale support. It begins with client consultation to understand project requirements, followed by concept development and iterative feedback cycles. After client approval, the artist proceeds with detailed creation, periodic progress updates, and quality assurance reviews. Once the artwork is complete, it undergoes final adjustments before invoicing and shipping. Post-delivery includes client satisfaction confirmation and optional framing or digital licensing arrangements. The process ensures clear communication, creative alignment, and efficient resource allocation to meet unique artistic demands in a timely manner.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Client_Inquiry = Transition(label='Client Inquiry')
Requirement_Gather = Transition(label='Requirement Gather')
Concept_Sketch = Transition(label='Concept Sketch')
Client_Feedback = Transition(label='Client Feedback')
Revision_Cycle = Transition(label='Revision Cycle')
Final_Approval = Transition(label='Final Approval')
Art_Creation = Transition(label='Art Creation')
Progress_Update = Transition(label='Progress Update')
Quality_Check = Transition(label='Quality Check')
Final_Adjust = Transition(label='Final Adjust')
Invoice_Issue = Transition(label='Invoice Issue')
Shipment_Prep = Transition(label='Shipment Prep')
Delivery_Confirm = Transition(label='Delivery Confirm')
Post_Support = Transition(label='Post Support')
License_Setup = Transition(label='License Setup')
Frame_Arrange = Transition(label='Frame Arrange')

skip = SilentTransition()

# Loop for iterative feedback cycles (Client Feedback and Revision Cycle):
# LOOP = *(A, B), execute A, then either exit or execute B then A again
# Here: loop = *(Client_Feedback, Revision_Cycle)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Client_Feedback, Revision_Cycle])

# After client consultation and concept sketch, enter feedback loop
# The sequence is: Client Inquiry --> Requirement Gather --> Concept Sketch --> feedback_loop --> Final Approval

# After Final Approval, detailed art creation with periodic progress updates and quality checks.
# Sequence: Art Creation --> Progress Update --> Quality Check
# On completion of Quality Check, Final Adjust

# After Final Adjust, Invoice Issue --> Shipment Prep --> Delivery Confirm

# After Delivery Confirm, post-delivery includes Client Satisfaction Confirmation (Post Support)
# and OPTIONAL framing or digital licensing arrangements - choice between License Setup or Frame Arrange or skip both

# Post Support followed by XOR( License Setup, Frame Arrange, skip )

post_delivery_choice = OperatorPOWL(operator=Operator.XOR, children=[License_Setup, Frame_Arrange, skip])

post_delivery = StrictPartialOrder(nodes=[Post_Support, post_delivery_choice])
post_delivery.order.add_edge(Post_Support, post_delivery_choice)

# Art creation partial order
art_creation_po = StrictPartialOrder(
    nodes=[Art_Creation, Progress_Update, Quality_Check, Final_Adjust]
)
art_creation_po.order.add_edge(Art_Creation, Progress_Update)
art_creation_po.order.add_edge(Progress_Update, Quality_Check)
art_creation_po.order.add_edge(Quality_Check, Final_Adjust)

# Shipping partial order
shipping_po = StrictPartialOrder(
    nodes=[Invoice_Issue, Shipment_Prep, Delivery_Confirm]
)
shipping_po.order.add_edge(Invoice_Issue, Shipment_Prep)
shipping_po.order.add_edge(Shipment_Prep, Delivery_Confirm)

# Main process partial order

# nodes:
# start: Client_Inquiry --> Requirement_Gather --> Concept_Sketch --> feedback_loop --> Final_Approval
# then art_creation_po --> shipping_po --> post_delivery

nodes_main = [
    Client_Inquiry,
    Requirement_Gather,
    Concept_Sketch,
    feedback_loop,
    Final_Approval,
    art_creation_po,
    shipping_po,
    post_delivery,
]

root = StrictPartialOrder(nodes=nodes_main)

# Add order edges in main flow:
root.order.add_edge(Client_Inquiry, Requirement_Gather)
root.order.add_edge(Requirement_Gather, Concept_Sketch)
root.order.add_edge(Concept_Sketch, feedback_loop)
root.order.add_edge(feedback_loop, Final_Approval)
root.order.add_edge(Final_Approval, art_creation_po)
root.order.add_edge(art_creation_po, shipping_po)
root.order.add_edge(shipping_po, post_delivery)