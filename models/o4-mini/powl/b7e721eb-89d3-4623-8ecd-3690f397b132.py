# Generated from: b7e721eb-89d3-4623-8ecd-3690f397b132.json
# Description: This process governs the detailed authentication and provenance verification of rare historical artifacts before acquisition by a museum or private collector. It involves interdisciplinary collaboration between historians, chemists, and forensic analysts to validate the artifact's age, origin, and authenticity. Initial steps include digital scanning and material sampling, followed by isotopic and radiocarbon testing. Concurrently, provenance records are cross-checked against archival databases and known ownership chains. Legal experts then review compliance with cultural heritage laws. Finally, a multidisciplinary committee reviews all findings before issuing a formal authentication certificate. This process mitigates risks associated with forgeries and illicit trade, ensuring ethical acquisition and long-term preservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define transitions for each activity
initial_scan        = Transition(label='Initial Scan')
material_sample     = Transition(label='Material Sample')
isotope_test        = Transition(label='Isotope Test')
carbon_dating       = Transition(label='Carbon Dating')
provenance_check    = Transition(label='Provenance Check')
archive_query       = Transition(label='Archive Query')
ownership_review    = Transition(label='Ownership Review')
database_crosscheck = Transition(label='Database Crosscheck')
forensic_analysis   = Transition(label='Forensic Analysis')
expert_interviews   = Transition(label='Expert Interviews')
condition_report    = Transition(label='Condition Report')
legal_compliance    = Transition(label='Legal Compliance')
risk_assessment     = Transition(label='Risk Assessment')
committee_review    = Transition(label='Committee Review')
certificate_issue   = Transition(label='Certificate Issue')
final_approval      = Transition(label='Final Approval')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    initial_scan,
    material_sample,
    isotope_test,
    carbon_dating,
    provenance_check,
    archive_query,
    ownership_review,
    database_crosscheck,
    forensic_analysis,
    expert_interviews,
    condition_report,
    legal_compliance,
    risk_assessment,
    committee_review,
    certificate_issue,
    final_approval
])

# 1. Initial Scan precedes Material Sample and Condition Report
root.order.add_edge(initial_scan, material_sample)
root.order.add_edge(initial_scan, condition_report)

# 2. After sampling, branch into lab tests, provenance checks, and forensic analysis
for nxt in [isotope_test, carbon_dating,
            provenance_check, archive_query,
            ownership_review, database_crosscheck,
            forensic_analysis]:
    root.order.add_edge(material_sample, nxt)

# 3. Forensic Analysis then Expert Interviews
root.order.add_edge(forensic_analysis, expert_interviews)

# 4. All key activities must complete before Legal Compliance
for pred in [
    isotope_test, carbon_dating,
    provenance_check, archive_query,
    ownership_review, database_crosscheck,
    expert_interviews, condition_report
]:
    root.order.add_edge(pred, legal_compliance)

# 5. Sequential final steps
root.order.add_edge(legal_compliance, risk_assessment)
root.order.add_edge(risk_assessment, committee_review)
root.order.add_edge(committee_review, certificate_issue)
root.order.add_edge(certificate_issue, final_approval)