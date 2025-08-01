# Generated from: 187f0feb-e4fa-4431-8f73-0362caf67b1f.json
# Description: This process involves the identification, verification, acquisition, and quality assurance of rare and exotic ingredients used in high-end culinary and pharmaceutical products. It encompasses global supplier scouting, compliance with international regulations, ethical sourcing verification, logistics coordination, and risk mitigation strategies to ensure timely delivery and maintain ingredient integrity throughout transport and storage. Cross-functional collaboration between procurement, legal, quality assurance, and logistics teams is critical to navigate complex import restrictions, cultural considerations, and sustainability certifications. Continuous supplier performance monitoring and contingency planning for geopolitical disruptions are integral parts of the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Supplier_Scout = Transition(label='Supplier Scout')
Regulation_Check = Transition(label='Regulation Check')
Ethics_Verify = Transition(label='Ethics Verify')
Sample_Request = Transition(label='Sample Request')
Quality_Test = Transition(label='Quality Test')
Contract_Draft = Transition(label='Contract Draft')
Customs_Clear = Transition(label='Customs Clear')
Transport_Book = Transition(label='Transport Book')
Storage_Monitor = Transition(label='Storage Monitor')
Risk_Assess = Transition(label='Risk Assess')
Performance_Track = Transition(label='Performance Track')
Compliance_Audit = Transition(label='Compliance Audit')
Backup_Plan = Transition(label='Backup Plan')
Invoice_Process = Transition(label='Invoice Process')
Delivery_Confirm = Transition(label='Delivery Confirm')
Supplier_Review = Transition(label='Supplier Review')

# Procurement sequence: Supplier Scout -> Regulation Check -> Ethics Verify
procurement_seq = StrictPartialOrder(nodes=[Supplier_Scout, Regulation_Check, Ethics_Verify])
procurement_seq.order.add_edge(Supplier_Scout, Regulation_Check)
procurement_seq.order.add_edge(Regulation_Check, Ethics_Verify)

# Sample and quality test loop:
# Request sample, test quality, then either exit or repeat sample request
sample_request_test = OperatorPOWL(operator=Operator.LOOP, children=[Sample_Request, Quality_Test])

# Contract and customs clearance partial order (can be concurrent)
contract_clearance = StrictPartialOrder(nodes=[Contract_Draft, Customs_Clear])
# No order edges - can be done in parallel

# Logistics partial order
logistics = StrictPartialOrder(nodes=[Transport_Book, Storage_Monitor])
logistics.order.add_edge(Transport_Book, Storage_Monitor)

# Risk and compliance partial order: Risk Assess and Compliance Audit can be concurrent
risk_compliance = StrictPartialOrder(nodes=[Risk_Assess, Compliance_Audit])

# Performance tracking and supplier review partial order
performance_review = StrictPartialOrder(nodes=[Performance_Track, Supplier_Review])
performance_review.order.add_edge(Performance_Track, Supplier_Review)

# Invoice and delivery sequence
invoice_delivery = StrictPartialOrder(nodes=[Invoice_Process, Delivery_Confirm])
invoice_delivery.order.add_edge(Invoice_Process, Delivery_Confirm)

# Backup plan is a silent choice: either execute Backup Plan or skip
skip = SilentTransition()
backup_choice = OperatorPOWL(operator=Operator.XOR, children=[Backup_Plan, skip])

# Assemble compliance and backup: compliance activities followed by backup choice
compliance_backup = StrictPartialOrder(nodes=[risk_compliance, backup_choice])
compliance_backup.order.add_edge(risk_compliance, backup_choice)

# Assemble main process in partial order with edges representing logical flow:
# procurement_seq -> sample_request_test -> contract_clearance, logistics, compliance_backup in parallel
# contract_clearance and logistics precede invoice_delivery
# invoice_delivery precedes performance_review

# Nodes at top level
top_nodes = [
    procurement_seq,
    sample_request_test,
    contract_clearance,
    logistics,
    compliance_backup,
    invoice_delivery,
    performance_review
]

root = StrictPartialOrder(nodes=top_nodes)

# Add edges to model flow and dependencies
root.order.add_edge(procurement_seq, sample_request_test)
root.order.add_edge(sample_request_test, contract_clearance)
root.order.add_edge(sample_request_test, logistics)
root.order.add_edge(sample_request_test, compliance_backup)
root.order.add_edge(contract_clearance, invoice_delivery)
root.order.add_edge(logistics, invoice_delivery)
root.order.add_edge(compliance_backup, invoice_delivery)
root.order.add_edge(invoice_delivery, performance_review)