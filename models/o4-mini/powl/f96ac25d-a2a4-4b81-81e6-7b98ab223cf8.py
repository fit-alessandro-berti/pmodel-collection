# Generated from: f96ac25d-a2a4-4b81-81e6-7b98ab223cf8.json
# Description: This process governs the lifecycle of a custom art commission from initial client inquiry to final delivery and post-sale support. It begins with client briefing and concept ideation, followed by iterative design reviews and adjustments. The artist then proceeds with material sourcing and prototype creation, coordinating with external vendors for specialty supplies. Quality assurance involves both technical and aesthetic evaluations, ensuring the artwork meets client expectations and industry standards. After final approval, packaging and logistics are arranged with eco-friendly considerations. Post-delivery, the process includes client feedback collection, documentation for portfolio updates, and scheduling of potential future commissions or maintenance services. Throughout, communication and contract management maintain transparency and protect intellectual property rights, ensuring a seamless experience for both artist and client.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
contract_sign = Transition(label='Contract Sign')
ip_management = Transition(label='IP Management')
client_brief = Transition(label='Client Brief')
concept_sketch = Transition(label='Concept Sketch')
design_review = Transition(label='Design Review')
material_sourcing = Transition(label='Material Sourcing')
vendor_coordination = Transition(label='Vendor Coordination')
prototype_build = Transition(label='Prototype Build')
quality_check = Transition(label='Quality Check')
client_approval = Transition(label='Client Approval')
packaging_prep = Transition(label='Packaging Prep')
shipping_arrange = Transition(label='Shipping Arrange')
feedback_collect = Transition(label='Feedback Collect')
portfolio_update = Transition(label='Portfolio Update')
future_schedule = Transition(label='Future Schedule')
maintenance_plan = Transition(label='Maintenance Plan')

# Loop for iterative design reviews and adjustments:
#   A: Concept Sketch -> Design Review
#   B: Design Review -> Concept Sketch (repeat)
A = StrictPartialOrder(nodes=[concept_sketch, design_review])
A.order.add_edge(concept_sketch, design_review)
B = StrictPartialOrder(nodes=[design_review, concept_sketch])
B.order.add_edge(design_review, concept_sketch)
loop_design = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Exclusive choice between future scheduling or maintenance planning
xor_future = OperatorPOWL(operator=Operator.XOR, children=[future_schedule, maintenance_plan])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    contract_sign, ip_management,
    client_brief,
    loop_design,
    material_sourcing, vendor_coordination, prototype_build,
    quality_check, client_approval,
    packaging_prep, shipping_arrange,
    feedback_collect, portfolio_update,
    xor_future
])

# Define the ordering relations
root.order.add_edge(contract_sign, client_brief)
root.order.add_edge(ip_management, client_brief)
root.order.add_edge(client_brief, loop_design)
root.order.add_edge(loop_design, material_sourcing)
root.order.add_edge(material_sourcing, vendor_coordination)
root.order.add_edge(vendor_coordination, prototype_build)
root.order.add_edge(prototype_build, quality_check)
root.order.add_edge(quality_check, client_approval)
root.order.add_edge(client_approval, packaging_prep)
root.order.add_edge(packaging_prep, shipping_arrange)
root.order.add_edge(shipping_arrange, feedback_collect)
root.order.add_edge(feedback_collect, portfolio_update)
root.order.add_edge(portfolio_update, xor_future)