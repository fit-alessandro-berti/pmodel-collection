# Generated from: 187f0feb-e4fa-4431-8f73-0362caf67b1f.json
# Description: This process involves the identification, verification, acquisition, and quality assurance of rare and exotic ingredients used in high-end culinary and pharmaceutical products. It encompasses global supplier scouting, compliance with international regulations, ethical sourcing verification, logistics coordination, and risk mitigation strategies to ensure timely delivery and maintain ingredient integrity throughout transport and storage. Cross-functional collaboration between procurement, legal, quality assurance, and logistics teams is critical to navigate complex import restrictions, cultural considerations, and sustainability certifications. Continuous supplier performance monitoring and contingency planning for geopolitical disruptions are integral parts of the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
supplier_scout    = Transition(label='Supplier Scout')
regulation_check  = Transition(label='Regulation Check')
ethics_verify     = Transition(label='Ethics Verify')
sample_request    = Transition(label='Sample Request')
quality_test      = Transition(label='Quality Test')
backup_plan       = Transition(label='Backup Plan')
contract_draft    = Transition(label='Contract Draft')
customs_clear     = Transition(label='Customs Clear')
transport_book    = Transition(label='Transport Book')
delivery_confirm  = Transition(label='Delivery Confirm')
storage_monitor   = Transition(label='Storage Monitor')
invoice_process   = Transition(label='Invoice Process')
supplier_review   = Transition(label='Supplier Review')
risk_assess       = Transition(label='Risk Assess')
performance_track = Transition(label='Performance Track')
compliance_audit  = Transition(label='Compliance Audit')

# Loop for sample‐quality cycle: do (Sample Request → Quality Test),
# then optionally (Backup Plan → Sample Request → Quality Test) → repeat
ql_seq = StrictPartialOrder(nodes=[sample_request, quality_test])
ql_seq.order.add_edge(sample_request, quality_test)
ql_body = StrictPartialOrder(nodes=[backup_plan, sample_request, quality_test])
ql_body.order.add_edge(backup_plan, sample_request)
ql_body.order.add_edge(sample_request, quality_test)
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[ql_seq, ql_body])

# Loop for continuous risk & performance monitoring:
# do (Risk Assess → Performance Track → Compliance Audit),
# then optionally (Backup Plan → Risk Assess → Performance Track → Compliance Audit) → repeat
pr_seq = StrictPartialOrder(nodes=[risk_assess, performance_track, compliance_audit])
pr_seq.order.add_edge(risk_assess, performance_track)
pr_seq.order.add_edge(performance_track, compliance_audit)
pr_body = StrictPartialOrder(nodes=[backup_plan, risk_assess, performance_track, compliance_audit])
pr_body.order.add_edge(backup_plan, risk_assess)
pr_body.order.add_edge(risk_assess, performance_track)
pr_body.order.add_edge(performance_track, compliance_audit)
performance_loop = OperatorPOWL(operator=Operator.LOOP, children=[pr_seq, pr_body])

# Root partial order
root = StrictPartialOrder(nodes=[
    supplier_scout,
    regulation_check,
    ethics_verify,
    quality_loop,
    contract_draft,
    customs_clear,
    transport_book,
    delivery_confirm,
    storage_monitor,
    invoice_process,
    supplier_review,
    performance_loop
])
# Dependencies
root.order.add_edge(supplier_scout,   regulation_check)
root.order.add_edge(supplier_scout,   ethics_verify)
root.order.add_edge(regulation_check, quality_loop)
root.order.add_edge(ethics_verify,    quality_loop)
root.order.add_edge(quality_loop,     contract_draft)
root.order.add_edge(contract_draft,   customs_clear)
root.order.add_edge(customs_clear,    transport_book)
root.order.add_edge(transport_book,   delivery_confirm)
root.order.add_edge(delivery_confirm, storage_monitor)
root.order.add_edge(delivery_confirm, invoice_process)
root.order.add_edge(storage_monitor,  supplier_review)
root.order.add_edge(invoice_process,  supplier_review)
root.order.add_edge(supplier_review,  performance_loop)