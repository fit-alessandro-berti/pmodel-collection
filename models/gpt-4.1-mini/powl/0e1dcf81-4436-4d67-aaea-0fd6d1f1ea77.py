# Generated from: 0e1dcf81-4436-4d67-aaea-0fd6d1f1ea77.json
# Description: This process manages the intricate repatriation of corporate artifacts loaned to international museums and exhibitions. It involves verifying artifact authenticity, navigating customs regulations, coordinating multi-party logistics, securing insurance coverage, and ensuring proper cultural sensitivity. The process requires cross-border legal compliance, stakeholder communication, condition reporting, restoration scheduling, and final reintegration into corporate archives or displays, often under strict confidentiality agreements and tight timelines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
Artifact_Verify = Transition(label='Artifact Verify')
Loan_Assessment = Transition(label='Loan Assessment')
Legal_Review = Transition(label='Legal Review')
Customs_Filing = Transition(label='Customs Filing')
Insurance_Setup = Transition(label='Insurance Setup')
Transport_Booking = Transition(label='Transport Booking')
Condition_Report = Transition(label='Condition Report')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Cultural_Review = Transition(label='Cultural Review')
Restoration_Plan = Transition(label='Restoration Plan')
Security_Audit = Transition(label='Security Audit')
Shipping_Monitor = Transition(label='Shipping Monitor')
Arrival_Inspect = Transition(label='Arrival Inspect')
Archive_Update = Transition(label='Archive Update')
Confidentiality_Sign = Transition(label='Confidentiality Sign')

# Model structure:
# Start with Artifact Verify and Loan Assessment in parallel (no order),
# followed by a partial order of legal compliance, customs, insurance.
# Then a partial order of logistics and condition report,
# followed by cultural review and restoration plan in order,
# security audit and shipping monitor can be concurrent,
# then arrival inspect, archive update, confidentiality sign in order.

# Partial order 1: Legal Review --> Customs Filing --> Insurance Setup
legal_customs_insurance = StrictPartialOrder(nodes=[Legal_Review, Customs_Filing, Insurance_Setup])
legal_customs_insurance.order.add_edge(Legal_Review, Customs_Filing)
legal_customs_insurance.order.add_edge(Customs_Filing, Insurance_Setup)

# Partial order 2: Transport Booking and Condition Report concurrent
logistics_condition = StrictPartialOrder(nodes=[Transport_Booking, Condition_Report])

# Partial order 3: Stakeholder Notify --> Cultural Review --> Restoration Plan
culture_flow = StrictPartialOrder(nodes=[Stakeholder_Notify, Cultural_Review, Restoration_Plan])
culture_flow.order.add_edge(Stakeholder_Notify, Cultural_Review)
culture_flow.order.add_edge(Cultural_Review, Restoration_Plan)

# Partial order 4: Security Audit and Shipping Monitor concurrent
security_shipping = StrictPartialOrder(nodes=[Security_Audit, Shipping_Monitor])

# Partial order 5: Arrival Inspect --> Archive Update --> Confidentiality Sign
final_steps = StrictPartialOrder(nodes=[Arrival_Inspect, Archive_Update, Confidentiality_Sign])
final_steps.order.add_edge(Arrival_Inspect, Archive_Update)
final_steps.order.add_edge(Archive_Update, Confidentiality_Sign)

# Compose the overall model in partial order
# Step 1 and 2 are parallel: (Artifact Verify, Loan Assessment) then legal compliance sequence,
# followed by logistics_condition,
# then cultural flow,
# then security_shipping,
# then final steps.

# Start with Artifact Verify and Loan Assessment concurrent
start_steps = StrictPartialOrder(nodes=[Artifact_Verify, Loan_Assessment])

# Overall nodes:
nodes = [start_steps, legal_customs_insurance, logistics_condition,
         culture_flow, security_shipping, final_steps]

# Define partial order between these groups
root = StrictPartialOrder(nodes=nodes)
# Start steps before legal compliance
root.order.add_edge(start_steps, legal_customs_insurance)
# legal compliance before logistics and condition report
root.order.add_edge(legal_customs_insurance, logistics_condition)
# logistics and condition report before cultural flow
root.order.add_edge(logistics_condition, culture_flow)
# cultural flow before security and shipping monitor
root.order.add_edge(culture_flow, security_shipping)
# security and shipping before final steps
root.order.add_edge(security_shipping, final_steps)