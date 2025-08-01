# Generated from: 6bb6dd23-1fe4-4277-9c73-298a17aa8ef2.json
# Description: This process describes the end-to-end flow of sourcing rare, handcrafted materials from remote artisans, verifying authenticity through blockchain certification, coordinating bespoke production schedules with multiple small workshops, and managing bespoke logistics for fragile goods. The process involves collaborative design reviews, custom packaging development, and adaptive marketing strategies tailored to niche collectors, ensuring exclusivity and traceability throughout the supply chain while maintaining sustainability and fair trade practices.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Supplier_Onboard = Transition(label='Supplier Onboard')
Material_Verify = Transition(label='Material Verify')
Auth_Certify = Transition(label='Auth Certify')
Design_Review = Transition(label='Design Review')
Sample_Produce = Transition(label='Sample Produce')
Quality_Inspect = Transition(label='Quality Inspect')
Order_Schedule = Transition(label='Order Schedule')
Workshop_Align = Transition(label='Workshop Align')
Packaging_Develop = Transition(label='Packaging Develop')
Logistics_Plan = Transition(label='Logistics Plan')
Custom_Label = Transition(label='Custom Label')
Shipment_Track = Transition(label='Shipment Track')
Customer_Notify = Transition(label='Customer Notify')
Feedback_Collect = Transition(label='Feedback Collect')
Sustain_Audit = Transition(label='Sustain Audit')
Trade_Compliance = Transition(label='Trade Compliance')

# Model components according to the description:

# 1. Initial onboarding and verification flow:
# Supplier onboard -> Material verify -> Auth certify
initial_flow = StrictPartialOrder(nodes=[Supplier_Onboard, Material_Verify, Auth_Certify])
initial_flow.order.add_edge(Supplier_Onboard, Material_Verify)
initial_flow.order.add_edge(Material_Verify, Auth_Certify)

# 2. Bespoke production schedules with workshops:
# Order Schedule -> Workshop Align (these two can be parallel to packaging development)
# Bespoke production line: Design Review -> Sample Produce -> Quality Inspect
prod_review = StrictPartialOrder(nodes=[Design_Review, Sample_Produce, Quality_Inspect])
prod_review.order.add_edge(Design_Review, Sample_Produce)
prod_review.order.add_edge(Sample_Produce, Quality_Inspect)

workshops = StrictPartialOrder(nodes=[Order_Schedule, Workshop_Align])
workshops.order.add_edge(Order_Schedule, Workshop_Align)

# 3. Custom packaging: Packaging Develop -> Custom Label
package_flow = StrictPartialOrder(nodes=[Packaging_Develop, Custom_Label])
package_flow.order.add_edge(Packaging_Develop, Custom_Label)

# 4. Logistics and shipment: Logistics Plan -> Shipment Track
logistics_flow = StrictPartialOrder(nodes=[Logistics_Plan, Shipment_Track])
logistics_flow.order.add_edge(Logistics_Plan, Shipment_Track)

# 5. Customer interaction: Customer Notify -> Feedback Collect (loop for improvements based on feedback)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Customer_Notify, Feedback_Collect])

# 6. Sustainability and compliance checks (can be parallel and final checks before completing)
# Sustain Audit and Trade Compliance could run concurrently
sustain_compliance = StrictPartialOrder(nodes=[Sustain_Audit, Trade_Compliance])

# Compose parallel flows after Auth Certify:
# After Auth Certify, three main parallel branches:
# - Production branch (prod_review + workshops, workshops after order schedule, production after design review)
# - Packaging branch (package_flow)
# - Logistics branch (logistics_flow)

# Combine production and workshops into one PO with edges from workshops to production (align before producing)
prod_and_workshops = StrictPartialOrder(nodes=[Order_Schedule, Workshop_Align, Design_Review, Sample_Produce, Quality_Inspect])
prod_and_workshops.order.add_edge(Order_Schedule, Workshop_Align)
prod_and_workshops.order.add_edge(Workshop_Align, Design_Review)
prod_and_workshops.order.add_edge(Design_Review, Sample_Produce)
prod_and_workshops.order.add_edge(Sample_Produce, Quality_Inspect)

# After production+workshops, packaging and logistics can be concurrent with sustainability/compliance 
# but packaging depends on production finishing (i.e. Custom Label logically after Quality Inspect)
packaging_and_logistics = StrictPartialOrder(nodes=[Packaging_Develop, Custom_Label, Logistics_Plan, Shipment_Track, Sustain_Audit, Trade_Compliance])
# Packaging Develop can start after Quality Inspect
packaging_and_logistics.order.add_edge(Packaging_Develop, Custom_Label)
packaging_and_logistics.order.add_edge(Custom_Label, Logistics_Plan)
packaging_and_logistics.order.add_edge(Logistics_Plan, Shipment_Track)
# Sustain audit and trade compliance run in parallel; for simplicity no explicit edges connecting them

# Now create a bigger PO with Auth Certify leading into the concurrent big block:
post_auth = StrictPartialOrder(
    nodes=[prod_and_workshops, packaging_and_logistics, feedback_loop]
)
post_auth.order.add_edge(prod_and_workshops, packaging_and_logistics)
post_auth.order.add_edge(packaging_and_logistics, feedback_loop)

# Final root PO: initial -> post_auth
root = StrictPartialOrder(nodes=[initial_flow, post_auth])
root.order.add_edge(initial_flow, post_auth)