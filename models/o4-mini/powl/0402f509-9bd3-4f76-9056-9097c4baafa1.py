# Generated from: 0402f509-9bd3-4f76-9056-9097c4baafa1.json
# Description: This process outlines the detailed workflow for authenticating historical artifacts prior to acquisition by a museum or private collector. It involves multidisciplinary examination phases including provenance verification, material composition analysis, stylistic comparison, and digital forensics. Each step requires collaboration among historians, chemists, and data scientists. The workflow also incorporates risk assessment, legal compliance checks, and final documentation preparation. The aim is to minimize forgery risk while ensuring cultural and legal integrity, involving iterative feedback loops between experts and external databases before final acquisition approval.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
initial_review    = Transition(label='Initial Review')
prov_check        = Transition(label='Provenance Check')
material_testing  = Transition(label='Material Testing')
style_analysis    = Transition(label='Style Analysis')
digital_scan      = Transition(label='Digital Scan')
forensic_audit    = Transition(label='Forensic Audit')
expert_panel      = Transition(label='Expert Panel')
data_crossref     = Transition(label='Data Crossref')
risk_assess       = Transition(label='Risk Assess')
legal_verify      = Transition(label='Legal Verify')
ethics_review     = Transition(label='Ethics Review')
ownership_trace   = Transition(label='Ownership Trace')
condition_report  = Transition(label='Condition Report')
auth_certify      = Transition(label='Auth Certify')
final_approval    = Transition(label='Final Approval')
archive_entry     = Transition(label='Archive Entry')

# Concurrent analysis phase
analysis = StrictPartialOrder(nodes=[
    prov_check,
    material_testing,
    style_analysis,
    digital_scan,
    forensic_audit
])
# No ordering edges => fully concurrent

# Feedback phase (sequence: expert panel -> cross-reference)
feedback = StrictPartialOrder(nodes=[expert_panel, data_crossref])
feedback.order.add_edge(expert_panel, data_crossref)

# Loop: do analysis, then optionally feedback then repeat
analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[analysis, feedback])

# Build the overall process partial order
root = StrictPartialOrder(nodes=[
    initial_review,
    analysis_loop,
    risk_assess,
    legal_verify,
    ethics_review,
    ownership_trace,
    condition_report,
    auth_certify,
    final_approval,
    archive_entry
])

# Add control‐flow edges
root.order.add_edge(initial_review, analysis_loop)
root.order.add_edge(analysis_loop, risk_assess)
root.order.add_edge(risk_assess, legal_verify)
root.order.add_edge(legal_verify, ethics_review)
root.order.add_edge(ethics_review, ownership_trace)
root.order.add_edge(ownership_trace, condition_report)
root.order.add_edge(condition_report, auth_certify)
root.order.add_edge(auth_certify, final_approval)
root.order.add_edge(final_approval, archive_entry)