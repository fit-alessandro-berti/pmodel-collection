# Generated from: 6326417a-dbac-4344-8077-8ab9a5a47c2d.json
# Description: This process involves the authentication of rare cultural artifacts through a multi-step approach integrating scientific analysis, provenance verification, expert consultation, and legal compliance checks. Initially, the artifact undergoes non-invasive material scanning to detect composition and condition. Concurrently, provenance data is gathered from historical records and previous ownership chains. Specialists in art history and archaeology review the combined data to assess authenticity. Legal teams verify export and import permissions to ensure compliance with international heritage laws. Finally, a digital certificate of authenticity is generated and archived, while stakeholders receive a comprehensive report. This atypical workflow ensures the artifact's legitimacy, protects cultural heritage, and supports collectors' and institutions' trust in acquisitions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
initial_scan    = Transition(label='Initial Scan')
material_test   = Transition(label='Material Test')
provenance_check= Transition(label='Provenance Check')
ownership_trace = Transition(label='Ownership Trace')
condition_report= Transition(label='Condition Report')
data_consolidate= Transition(label='Data Consolidate')
historical_rev  = Transition(label='Historical Review')
expert_consult  = Transition(label='Expert Consult')
legal_verify    = Transition(label='Legal Verify')
export_audit    = Transition(label='Export Audit')
import_audit    = Transition(label='Import Audit')
fraud_screening = Transition(label='Fraud Screening')
certificate_gen = Transition(label='Certificate Gen')
report_draft    = Transition(label='Report Draft')
stakeholder_not = Transition(label='Stakeholder Notify')
archive_record  = Transition(label='Archive Record')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    initial_scan, material_test,
    provenance_check, ownership_trace,
    condition_report, data_consolidate,
    historical_rev, expert_consult,
    legal_verify, export_audit, import_audit, fraud_screening,
    certificate_gen, report_draft,
    stakeholder_not, archive_record
])

# 1. Scanning pipeline
root.order.add_edge(initial_scan, material_test)
root.order.add_edge(material_test, condition_report)

# 2. Provenance gathering
# (provenance_check and ownership_trace are independent of scanning but
#  all three feed into data_consolidate)
root.order.add_edge(provenance_check, data_consolidate)
root.order.add_edge(ownership_trace, data_consolidate)
root.order.add_edge(condition_report, data_consolidate)

# 3. Expert review (two concurrent reviews)
root.order.add_edge(data_consolidate, historical_rev)
root.order.add_edge(data_consolidate, expert_consult)

# 4. Legal compliance checks
root.order.add_edge(historical_rev, legal_verify)
root.order.add_edge(expert_consult, legal_verify)
root.order.add_edge(legal_verify, export_audit)
root.order.add_edge(legal_verify, import_audit)
root.order.add_edge(legal_verify, fraud_screening)

# 5. Final outputs (all legal subtasks must finish first)
for legal_task in (export_audit, import_audit, fraud_screening):
    root.order.add_edge(legal_task, certificate_gen)
    root.order.add_edge(legal_task, report_draft)

# 6. Archiving and notification
root.order.add_edge(certificate_gen, archive_record)
root.order.add_edge(report_draft, stakeholder_not)