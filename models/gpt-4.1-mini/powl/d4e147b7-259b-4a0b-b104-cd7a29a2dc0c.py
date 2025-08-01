# Generated from: d4e147b7-259b-4a0b-b104-cd7a29a2dc0c.json
# Description: This process involves the meticulous examination and validation of historical artifacts to verify their authenticity and provenance. It includes initial physical inspection, advanced scientific testing, provenance research through archival databases, expert consultations across multiple disciplines, and legal verification of ownership. Each step ensures that artifacts meet stringent cultural and legal standards before being approved for exhibition or sale. The workflow requires coordination between historians, scientists, legal advisors, and curators, integrating physical, digital, and documentary evidence to form a conclusive authentication report.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artifact_intake = Transition(label='Artifact Intake')
visual_scan = Transition(label='Visual Scan')
material_test = Transition(label='Material Test')
radiocarbon_check = Transition(label='Radiocarbon Check')
provenance_search = Transition(label='Provenance Search')
archive_review = Transition(label='Archive Review')
expert_consult = Transition(label='Expert Consult')
microscope_exam = Transition(label='Microscope Exam')
infrared_scan = Transition(label='Infrared Scan')
legal_verify = Transition(label='Legal Verify')
condition_report = Transition(label='Condition Report')
digital_catalog = Transition(label='Digital Catalog')
ownership_audit = Transition(label='Ownership Audit')
restoration_plan = Transition(label='Restoration Plan')
final_approval = Transition(label='Final Approval')
authentication_cert = Transition(label='Authentication Cert')

# Physical Inspection partial order: Visual Scan -> (Microscope Exam & Infrared Scan concurrent)
physical_inspection = StrictPartialOrder(nodes=[visual_scan, microscope_exam, infrared_scan])
physical_inspection.order.add_edge(visual_scan, microscope_exam)
physical_inspection.order.add_edge(visual_scan, infrared_scan)

# Scientific Testing partial order: Material Test -> Radiocarbon Check
scientific_testing = StrictPartialOrder(nodes=[material_test, radiocarbon_check])
scientific_testing.order.add_edge(material_test, radiocarbon_check)

# Provenance Research partial order: Provenance Search -> Archive Review
provenance_research = StrictPartialOrder(nodes=[provenance_search, archive_review])
provenance_research.order.add_edge(provenance_search, archive_review)

# Expert Consultation (single activity)
# Legal Verification partial order: Legal Verify -> Ownership Audit
legal_verification = StrictPartialOrder(nodes=[legal_verify, ownership_audit])
legal_verification.order.add_edge(legal_verify, ownership_audit)

# Reporting partial order: Condition Report -> Digital Catalog -> Restoration Plan
reporting = StrictPartialOrder(nodes=[condition_report, digital_catalog, restoration_plan])
reporting.order.add_edge(condition_report, digital_catalog)
reporting.order.add_edge(digital_catalog, restoration_plan)

# The overall process:
# Artifact Intake happens first
# Then Physical Inspection and Scientific Testing run in parallel
# After those, Provenance Research and Expert Consult run in parallel
# Then Legal Verification
# Then Reporting
# Then Final Approval
# Then Authentication Cert

# Group Physical Inspection and Scientific Testing (concurrent)
inspection_testing = StrictPartialOrder(nodes=[physical_inspection, scientific_testing])

# They both start after Artifact Intake
# Provenance Research and Expert Consult concurrent, start after inspection_testing
prov_exp_consult = StrictPartialOrder(nodes=[provenance_research, expert_consult])
# Legal verification after prov_exp_consult
# Reporting after legal verification
# Final Approval after reporting
# Authentication Cert after Final Approval

nodes = [
    artifact_intake,
    inspection_testing,
    prov_exp_consult,
    legal_verification,
    reporting,
    final_approval,
    authentication_cert
]

root = StrictPartialOrder(nodes=nodes)
# artifact intake --> inspection_testing
root.order.add_edge(artifact_intake, inspection_testing)
# inspection_testing --> prov_exp_consult
root.order.add_edge(inspection_testing, prov_exp_consult)
# prov_exp_consult --> legal_verification
root.order.add_edge(prov_exp_consult, legal_verification)
# legal_verification --> reporting
root.order.add_edge(legal_verification, reporting)
# reporting --> final_approval
root.order.add_edge(reporting, final_approval)
# final_approval --> authentication_cert
root.order.add_edge(final_approval, authentication_cert)