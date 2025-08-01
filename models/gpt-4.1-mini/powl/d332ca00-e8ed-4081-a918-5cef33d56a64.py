# Generated from: d332ca00-e8ed-4081-a918-5cef33d56a64.json
# Description: This process involves the meticulous examination and verification of rare artifacts to confirm their authenticity and provenance. It integrates multidisciplinary evaluations including historical research, material science analysis, and expert consultation. The process begins with initial artifact intake and documentation, followed by non-invasive imaging and chemical composition testing. Concurrently, provenance records are cross-checked against global databases. If anomalies arise, advanced forensic techniques and carbon dating are employed. The process culminates in a comprehensive authentication report, which informs acquisition decisions and insurance appraisals. Risk assessment and secure storage recommendations are also generated to preserve artifact integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
IntakeDocument = Transition(label='Intake Document')
VisualInspect = Transition(label='Visual Inspect')
ImagingScan = Transition(label='Imaging Scan')
MaterialTest = Transition(label='Material Test')
DatabaseCross = Transition(label='Database Cross')
ProvenanceCheck = Transition(label='Provenance Check')
ExpertConsult = Transition(label='Expert Consult')
CarbonDating = Transition(label='Carbon Dating')
ForensicAnalyze = Transition(label='Forensic Analyze')
AnomalyReview = Transition(label='Anomaly Review')
RiskAssess = Transition(label='Risk Assess')
ReportDraft = Transition(label='Report Draft')
InsuranceQuote = Transition(label='Insurance Quote')
StoragePlan = Transition(label='Storage Plan')
FinalApproval = Transition(label='Final Approval')
skip = SilentTransition()

# Concurrency: Visual Inspect, (Imaging Scan + Material Test), and (Database Cross + Provenance Check + Expert Consult)
# First group after intake: Visual Inspect
# Second group: Imaging Scan and Material Test in partial order (Imaging Scan always before Material Test)
# Third group: Database Cross, Provenance Check, and Expert Consult are concurrent

# Partial order for Imaging Scan and Material Test
imaging_and_material = StrictPartialOrder(nodes=[ImagingScan, MaterialTest])
imaging_and_material.order.add_edge(ImagingScan, MaterialTest)

# Partial order for Database Cross, Provenance Check, and Expert Consult (all concurrent)
db_prov_expert = StrictPartialOrder(nodes=[DatabaseCross, ProvenanceCheck, ExpertConsult])

# Now compose a partial order for all three above concurrent parts:
# Visual Inspect concurrent with imaging_and_material and db_prov_expert
# So create a strict partial order with no edges between these groups (fully concurrent)
concurrent_checks = StrictPartialOrder(
    nodes=[VisualInspect, imaging_and_material, db_prov_expert]
)
# No order edges: fully concurrent

# Anomaly review:
# If anomalies arise, advanced forensic techniques (Forensic Analyze), Carbon Dating, and Anomaly Review are done.
# Then the main routine continues.

# Model "if anomalies arise" as an XOR between (Anomaly path) and skip (no anomaly)
anomaly_path = StrictPartialOrder(
    nodes=[ForensicAnalyze, CarbonDating, AnomalyReview]
)
# Add order ForensicAnalyze --> CarbonDating --> AnomalyReview
anomaly_path.order.add_edge(ForensicAnalyze, CarbonDating)
anomaly_path.order.add_edge(CarbonDating, AnomalyReview)

anomaly_choice = OperatorPOWL(operator=Operator.XOR, children=[anomaly_path, skip])

# Loop: after anomaly_choice, control returns to the concurrent_checks to allow multiple anomaly checks if needed.
# Description said: "If anomalies arise ... repeated until exit"
# Actually, loop behaviour: execute A (concurrent_checks), then choose exit or execute B then A again.
# Here, A=concurrent_checks, B=anomaly_choice

loop_checks = OperatorPOWL(operator=Operator.LOOP, children=[concurrent_checks, anomaly_choice])

# The full model starts with Intake Document -> Visual Inspect + imaging + db checks loop -> proceed to final steps.

# We add order IntakeDocument --> loop_checks
# Then final sequential activities after loop: Report Draft -> Risk Assess -> Insurance Quote -> Storage Plan -> Final Approval

final_seq = StrictPartialOrder(nodes=[ReportDraft, RiskAssess, InsuranceQuote, StoragePlan, FinalApproval])
final_seq.order.add_edge(ReportDraft, RiskAssess)
final_seq.order.add_edge(RiskAssess, InsuranceQuote)
final_seq.order.add_edge(InsuranceQuote, StoragePlan)
final_seq.order.add_edge(StoragePlan, FinalApproval)

# Connect loop_checks --> final_seq in partial order
root = StrictPartialOrder(nodes=[IntakeDocument, loop_checks, final_seq])
root.order.add_edge(IntakeDocument, loop_checks)
root.order.add_edge(loop_checks, final_seq)