# Generated from: af7090ae-6cf5-487c-8eab-2842aaa09c57.json
# Description: This process outlines the comprehensive steps involved in authenticating historical artifacts for museum acquisition. It begins with initial artifact receipt and condition assessment, followed by multi-disciplinary analysis including chemical composition testing, provenance documentation verification, and stylistic comparison by experts. The workflow incorporates advanced imaging techniques and carbon dating, cross-referencing global databases to confirm artifact origin and legitimacy. Legal compliance checks and risk assessment for potential forgeries are conducted before final authentication approval. The process ends with detailed reporting and secure artifact cataloging to ensure traceability and preservation standards are met throughout the acquisition lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions for each activity
artifact_receipt   = Transition(label='Artifact Receipt')
condition_check    = Transition(label='Condition Check')
sample_extraction  = Transition(label='Sample Extraction')
chemical_testing   = Transition(label='Chemical Testing')
provenance_review  = Transition(label='Provenance Review')
stylistic_audit    = Transition(label='Stylistic Audit')
imaging_scan       = Transition(label='Imaging Scan')
carbon_dating      = Transition(label='Carbon Dating')
db_crosscheck      = Transition(label='Database Crosscheck')
forgery_analysis   = Transition(label='Forgery Analysis')
legal_review       = Transition(label='Legal Review')
risk_assessment    = Transition(label='Risk Assessment')
approval_meeting   = Transition(label='Approval Meeting')
report_drafting    = Transition(label='Report Drafting')
catalog_entry      = Transition(label='Catalog Entry')
secure_storage     = Transition(label='Secure Storage')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    artifact_receipt, condition_check,
    sample_extraction, chemical_testing,
    provenance_review, stylistic_audit,
    imaging_scan, carbon_dating,
    db_crosscheck, forgery_analysis,
    legal_review, risk_assessment,
    approval_meeting, report_drafting,
    catalog_entry, secure_storage
])

# Sequential start
root.order.add_edge(artifact_receipt, condition_check)

# Branch into multi-disciplinary analysis
root.order.add_edge(condition_check, sample_extraction)
root.order.add_edge(condition_check, provenance_review)
root.order.add_edge(condition_check, stylistic_audit)

# Chain Sample Extraction → Chemical Testing
root.order.add_edge(sample_extraction, chemical_testing)

# All three analysis outputs feed into imaging and carbon dating
for pred in [chemical_testing, provenance_review, stylistic_audit]:
    root.order.add_edge(pred, imaging_scan)
    root.order.add_edge(pred, carbon_dating)

# Imaging Scan & Carbon Dating must finish before DB Crosscheck
root.order.add_edge(imaging_scan, db_crosscheck)
root.order.add_edge(carbon_dating, db_crosscheck)

# Continue sequentially through the rest of the process
root.order.add_edge(db_crosscheck, forgery_analysis)
root.order.add_edge(forgery_analysis, legal_review)
root.order.add_edge(legal_review, risk_assessment)
root.order.add_edge(risk_assessment, approval_meeting)
root.order.add_edge(approval_meeting, report_drafting)
root.order.add_edge(report_drafting, catalog_entry)
root.order.add_edge(catalog_entry, secure_storage)