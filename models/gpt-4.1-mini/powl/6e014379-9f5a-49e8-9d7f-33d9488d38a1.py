# Generated from: 6e014379-9f5a-49e8-9d7f-33d9488d38a1.json
# Description: This process manages the complex coordination of loaning valuable art pieces between multiple international museums and private collectors. It involves provenance verification, condition reporting, diplomatic clearance, insurance arrangements, logistical planning for secure transport, installation oversight, exhibition scheduling, and post-loan audits. The process requires collaboration between curators, legal teams, conservators, transport specialists, and financial departments to ensure artworks are safely and legally moved, displayed, and returned, maintaining cultural heritage integrity and compliance with international laws.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Verify_Provenance = Transition(label='Verify Provenance')
Assess_Condition = Transition(label='Assess Condition')
Draft_Contract = Transition(label='Draft Contract')
Obtain_Clearance = Transition(label='Obtain Clearance')
Arrange_Insurance = Transition(label='Arrange Insurance')
Schedule_Transport = Transition(label='Schedule Transport')
Pack_Artwork = Transition(label='Pack Artwork')
Track_Shipment = Transition(label='Track Shipment')
Install_Exhibit = Transition(label='Install Exhibit')
Monitor_Environment = Transition(label='Monitor Environment')
Conduct_Tours = Transition(label='Conduct Tours')
Handle_Queries = Transition(label='Handle Queries')
Deinstall_Art = Transition(label='Deinstall Art')
Return_Shipment = Transition(label='Return Shipment')
Audit_Records = Transition(label='Audit Records')
Review_Feedback = Transition(label='Review Feedback')

# Step 1: Provenance verification and condition reporting (sequential)
step1 = StrictPartialOrder(nodes=[Verify_Provenance, Assess_Condition])
step1.order.add_edge(Verify_Provenance, Assess_Condition)

# Step 2: Draft contract, obtain diplomatic clearance, arrange insurance (all sequential)
step2 = StrictPartialOrder(nodes=[Draft_Contract, Obtain_Clearance, Arrange_Insurance])
step2.order.add_edge(Draft_Contract, Obtain_Clearance)
step2.order.add_edge(Obtain_Clearance, Arrange_Insurance)

# Step 3: Logistics for transport - schedule transport, pack artwork (sequential)
logistics_packing = StrictPartialOrder(nodes=[Schedule_Transport, Pack_Artwork])
logistics_packing.order.add_edge(Schedule_Transport, Pack_Artwork)

# Step 4: Transport and installation handled as a loop: shipment tracking and installation oversight potentially repeated
# Transport oversight loop: Track Shipment -> Install Exhibit -> Monitor Environment (monitor environment might be continuous during exhibition)
# For modeling a loop, assume after install and monitor the exhibit, we either exit or replay tracking and install again if needed.
install_monitor = StrictPartialOrder(nodes=[Install_Exhibit, Monitor_Environment])
install_monitor.order.add_edge(Install_Exhibit, Monitor_Environment)

transport_loop_body = StrictPartialOrder(nodes=[Track_Shipment, install_monitor])
transport_loop_body.order.add_edge(Track_Shipment, install_monitor)

# Loop over transport and installation: execute transport_loop_body, then either exit or repeat
transport_loop = OperatorPOWL(operator=Operator.LOOP, children=[transport_loop_body, SilentTransition()])

# Step 5: Exhibition side activities - Conduct Tours and Handle Queries concurrently
exhibition_activities = StrictPartialOrder(nodes=[Conduct_Tours, Handle_Queries])

# Step 6: End of loan - Deinstall art, return shipment (sequential)
end_loan = StrictPartialOrder(nodes=[Deinstall_Art, Return_Shipment])
end_loan.order.add_edge(Deinstall_Art, Return_Shipment)

# Step 7: Post loan audits - audit records, review feedback (sequential)
post_loan_audit = StrictPartialOrder(nodes=[Audit_Records, Review_Feedback])
post_loan_audit.order.add_edge(Audit_Records, Review_Feedback)

# Compose logistics step including scheduling, packing, and transport loop
logistics = StrictPartialOrder(nodes=[logistics_packing, transport_loop])
logistics.order.add_edge(logistics_packing, transport_loop)

# Compose exhibition step: exhibition activities and then end loan sequentially
exhibition_and_end = StrictPartialOrder(nodes=[exhibition_activities, end_loan])
exhibition_and_end.order.add_edge(exhibition_activities, end_loan)

# Compose post loan step after end loan
post_loan = post_loan_audit

# Compose the overall process partial order:
# 1. Provenance and condition checking
# 2. Contract, clearance, insurance
# 3. Logistics (schedule, pack, transport loop)
# 4. Exhibition and end loan
# 5. Post loan audits

root = StrictPartialOrder(
    nodes=[step1, step2, logistics, exhibition_and_end, post_loan]
)

root.order.add_edge(step1, step2)
root.order.add_edge(step2, logistics)
root.order.add_edge(logistics, exhibition_and_end)
root.order.add_edge(exhibition_and_end, post_loan)