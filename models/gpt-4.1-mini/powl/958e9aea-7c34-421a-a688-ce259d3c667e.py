# Generated from: 958e9aea-7c34-421a-a688-ce259d3c667e.json
# Description: This process involves the sourcing, crafting, quality validation, and distribution of bespoke artisan goods. It begins with material scouting in niche markets, followed by artisan assignment based on skill compatibility. Subsequent steps include prototype creation, peer review, refinement cycles, and final approval. Once approved, goods undergo packaging with unique branding, logistics coordination for multi-modal transport, customs clearance for international shipments, and finally, delivery to exclusive retail partners. The entire process integrates feedback loops from customer insights and artisan performance metrics to ensure continual improvement and maintain the high standards expected in luxury artisan markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Material_Scout = Transition(label='Material Scout')
Skill_Match = Transition(label='Skill Match')
Assign_Artisan = Transition(label='Assign Artisan')
Prototype_Build = Transition(label='Prototype Build')
Peer_Review = Transition(label='Peer Review')
Refine_Design = Transition(label='Refine Design')
Approval_Check = Transition(label='Approval Check')
Brand_Package = Transition(label='Brand Package')
Logistics_Plan = Transition(label='Logistics Plan')
Transport_Book = Transition(label='Transport Book')
Customs_Clear = Transition(label='Customs Clear')
Retail_Deliver = Transition(label='Retail Deliver')
Customer_Feedback = Transition(label='Customer Feedback')
Performance_Audit = Transition(label='Performance Audit')
Continuous_Improve = Transition(label='Continuous Improve')

# Construct the refinement loop: Refine Design <-> Peer Review until Approval Check passes
# Loop semantics: *(A, B) means execute A once then iterate B then A until exit
# Here, we model the cycle: Peer Review -> Refine Design, repeated until approval

# We'll encode the loop as:
# A = Peer Review
# B = Refine Design
refinement_loop = OperatorPOWL(operator=Operator.LOOP, children=[Peer_Review, Refine_Design])

# The process flow:
# Material Scout --> Skill Match --> Assign Artisan --> Prototype Build 
# --> refinement loop --> Approval Check --> packaging and logistics --> final delivery

# Sequence of packaging & logistics flow modeled as partial order with edges:
# Brand Package --> Logistics Plan --> Transport Book --> Customs Clear --> Retail Deliver

packaging_logistics = StrictPartialOrder(
    nodes=[Brand_Package, Logistics_Plan, Transport_Book, Customs_Clear, Retail_Deliver]
)
packaging_logistics.order.add_edge(Brand_Package, Logistics_Plan)
packaging_logistics.order.add_edge(Logistics_Plan, Transport_Book)
packaging_logistics.order.add_edge(Transport_Book, Customs_Clear)
packaging_logistics.order.add_edge(Customs_Clear, Retail_Deliver)

# Feedback and improvement loop is a choice between two feedback activities feeding into Continuous Improve
feedback_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[Customer_Feedback, Performance_Audit]
)

# Loop with Continuous Improve
# The continuous improvement loop: *(Continuous_Improve, feedback_choice)
continuous_improve_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Continuous_Improve, feedback_choice]
)

# Compose the main flow partial order

# All nodes together, including loops and sequential steps
nodes = [
    Material_Scout,
    Skill_Match,
    Assign_Artisan,
    Prototype_Build,
    refinement_loop,
    Approval_Check,
    packaging_logistics,
    continuous_improve_loop
]

root = StrictPartialOrder(nodes=nodes)

# Add edges to represent control flow
root.order.add_edge(Material_Scout, Skill_Match)
root.order.add_edge(Skill_Match, Assign_Artisan)
root.order.add_edge(Assign_Artisan, Prototype_Build)
root.order.add_edge(Prototype_Build, refinement_loop)
root.order.add_edge(refinement_loop, Approval_Check)
root.order.add_edge(Approval_Check, packaging_logistics)
root.order.add_edge(packaging_logistics, continuous_improve_loop)