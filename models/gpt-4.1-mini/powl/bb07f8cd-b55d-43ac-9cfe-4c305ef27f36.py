# Generated from: bb07f8cd-b55d-43ac-9cfe-4c305ef27f36.json
# Description: This process outlines the steps involved in commissioning a custom piece of artwork from initial client inquiry through final delivery and post-sale support. It begins with client briefing and concept development, followed by iterative design approvals and material sourcing. Mid-process includes detailed progress updates, client feedback incorporation, and quality assurance checks. Once the artwork is completed, logistics coordination ensures safe packaging and shipping. Finally, the process concludes with client satisfaction surveys and optional framing or installation services, ensuring a tailored, high-quality art experience that meets unique client needs while maintaining artist standards and timelines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Client_Inquiry = Transition(label='Client Inquiry')
Brief_Gathering = Transition(label='Brief Gathering')
Concept_Sketch = Transition(label='Concept Sketch')
Design_Review = Transition(label='Design Review')
Material_Sourcing = Transition(label='Material Sourcing')
Progress_Update = Transition(label='Progress Update')
Feedback_Loop = Transition(label='Feedback Loop')
Midway_Approval = Transition(label='Midway Approval')
Detail_Refinement = Transition(label='Detail Refinement')
Quality_Check = Transition(label='Quality Check')
Final_Approval = Transition(label='Final Approval')
Packaging_Prep = Transition(label='Packaging Prep')
Shipping_Arrange = Transition(label='Shipping Arrange')
Delivery_Confirm = Transition(label='Delivery Confirm')
Satisfaction_Survey = Transition(label='Satisfaction Survey')
Installation_Setup = Transition(label='Installation Setup')

# Construct the loop for iterative design approvals incorporating Feedback Loop and Detail Refinement,
# with Midway Approval as the condition to exit the loop.

# Loop children: body and redo
# Body is the design review, material sourcing, progress update, feedback incorporation, detail refinement, quality check
# After that Midway Approval is checked for loop exit
# We'll model this as LOOP(A,B):
# A = partial order of Design Review -> Material Sourcing -> Progress Update -> Feedback Loop -> Detail Refinement -> Quality Check -> Midway Approval
# B = Final Approval (to re-execute design from the start of the loop again)

A = StrictPartialOrder(nodes=[
    Design_Review,
    Material_Sourcing,
    Progress_Update,
    Feedback_Loop,
    Detail_Refinement,
    Quality_Check,
    Midway_Approval
])
A.order.add_edge(Design_Review, Material_Sourcing)
A.order.add_edge(Material_Sourcing, Progress_Update)
A.order.add_edge(Progress_Update, Feedback_Loop)
A.order.add_edge(Feedback_Loop, Detail_Refinement)
A.order.add_edge(Detail_Refinement, Quality_Check)
A.order.add_edge(Quality_Check, Midway_Approval)

B = Final_Approval

design_loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# After loop we package, ship, deliver
post_loop = StrictPartialOrder(nodes=[
    Packaging_Prep,
    Shipping_Arrange,
    Delivery_Confirm
])
post_loop.order.add_edge(Packaging_Prep, Shipping_Arrange)
post_loop.order.add_edge(Shipping_Arrange, Delivery_Confirm)

# After delivery we do satisfaction survey and optional installation setup
# They can be concurrent (parallel)
post_delivery = StrictPartialOrder(nodes=[
    Satisfaction_Survey,
    Installation_Setup
])
# no order edges, concurrent

# Partial order from start to design loop
start_to_loop = StrictPartialOrder(nodes=[
    Client_Inquiry,
    Brief_Gathering,
    Concept_Sketch,
    design_loop
])
start_to_loop.order.add_edge(Client_Inquiry, Brief_Gathering)
start_to_loop.order.add_edge(Brief_Gathering, Concept_Sketch)
start_to_loop.order.add_edge(Concept_Sketch, design_loop)

# Combine everything in partial order
root = StrictPartialOrder(nodes=[
    start_to_loop,
    post_loop,
    post_delivery
])
root.order.add_edge(start_to_loop, post_loop)
root.order.add_edge(post_loop, post_delivery)