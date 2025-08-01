# Generated from: d4e147b7-259b-4a0b-b104-cd7a29a2dc0c.json
# Description: This process involves the meticulous examination and validation of historical artifacts to verify their authenticity and provenance. It includes initial physical inspection, advanced scientific testing, provenance research through archival databases, expert consultations across multiple disciplines, and legal verification of ownership. Each step ensures that artifacts meet stringent cultural and legal standards before being approved for exhibition or sale. The workflow requires coordination between historians, scientists, legal advisors, and curators, integrating physical, digital, and documentary evidence to form a conclusive authentication report.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions for each activity
artifact_intake     = Transition(label='Artifact Intake')
visual_scan         = Transition(label='Visual Scan')
microscope_exam     = Transition(label='Microscope Exam')
infrared_scan       = Transition(label='Infrared Scan')
condition_report    = Transition(label='Condition Report')
material_test       = Transition(label='Material Test')
radiocarbon_check   = Transition(label='Radiocarbon Check')
provenance_search   = Transition(label='Provenance Search')
archive_review      = Transition(label='Archive Review')
expert_consult      = Transition(label='Expert Consult')
legal_verify        = Transition(label='Legal Verify')
ownership_audit     = Transition(label='Ownership Audit')
digital_catalog     = Transition(label='Digital Catalog')
restoration_plan    = Transition(label='Restoration Plan')
final_approval      = Transition(label='Final Approval')
authentication_cert = Transition(label='Authentication Cert')

# Create the root partial order with all nodes
root = StrictPartialOrder(nodes=[
    artifact_intake,
    visual_scan,
    microscope_exam,
    infrared_scan,
    condition_report,
    material_test,
    radiocarbon_check,
    provenance_search,
    archive_review,
    expert_consult,
    legal_verify,
    ownership_audit,
    digital_catalog,
    restoration_plan,
    final_approval,
    authentication_cert
])

# Define control-flow dependencies (→)
# Initial intake before all inspections and tests
root.order.add_edge(artifact_intake, visual_scan)
root.order.add_edge(artifact_intake, microscope_exam)
root.order.add_edge(artifact_intake, infrared_scan)
root.order.add_edge(artifact_intake, material_test)
root.order.add_edge(artifact_intake, radiocarbon_check)
root.order.add_edge(artifact_intake, provenance_search)

# Physical inspections lead to the condition report
root.order.add_edge(visual_scan, condition_report)
root.order.add_edge(microscope_exam, condition_report)
root.order.add_edge(infrared_scan, condition_report)

# Provenance research steps
root.order.add_edge(provenance_search, archive_review)

# All inspection & testing results feed into the expert consultation
root.order.add_edge(condition_report, expert_consult)
root.order.add_edge(material_test, expert_consult)
root.order.add_edge(radiocarbon_check, expert_consult)
root.order.add_edge(archive_review, expert_consult)

# Expert consultation → legal verification → ownership audit
root.order.add_edge(expert_consult, legal_verify)
root.order.add_edge(legal_verify, ownership_audit)

# After ownership audit, parallel digital catalog and restoration plan
root.order.add_edge(ownership_audit, digital_catalog)
root.order.add_edge(ownership_audit, restoration_plan)

# Both cataloging and restoration must finish before final approval
root.order.add_edge(digital_catalog, final_approval)
root.order.add_edge(restoration_plan, final_approval)

# Final approval → issue the authentication certificate
root.order.add_edge(final_approval, authentication_cert)