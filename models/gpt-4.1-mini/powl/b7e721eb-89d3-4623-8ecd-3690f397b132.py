# Generated from: b7e721eb-89d3-4623-8ecd-3690f397b132.json
# Description: This process governs the detailed authentication and provenance verification of rare historical artifacts before acquisition by a museum or private collector. It involves interdisciplinary collaboration between historians, chemists, and forensic analysts to validate the artifact's age, origin, and authenticity. Initial steps include digital scanning and material sampling, followed by isotopic and radiocarbon testing. Concurrently, provenance records are cross-checked against archival databases and known ownership chains. Legal experts then review compliance with cultural heritage laws. Finally, a multidisciplinary committee reviews all findings before issuing a formal authentication certificate. This process mitigates risks associated with forgeries and illicit trade, ensuring ethical acquisition and long-term preservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
InitialScan = Transition(label='Initial Scan')
MaterialSample = Transition(label='Material Sample')

IsotopeTest = Transition(label='Isotope Test')
CarbonDating = Transition(label='Carbon Dating')

ProvenanceCheck = Transition(label='Provenance Check')
ArchiveQuery = Transition(label='Archive Query')
OwnershipReview = Transition(label='Ownership Review')

LegalCompliance = Transition(label='Legal Compliance')

ForensicAnalysis = Transition(label='Forensic Analysis')
ExpertInterviews = Transition(label='Expert Interviews')
DatabaseCrosscheck = Transition(label='Database Crosscheck')

ConditionReport = Transition(label='Condition Report')
RiskAssessment = Transition(label='Risk Assessment')

CommitteeReview = Transition(label='Committee Review')
CertificateIssue = Transition(label='Certificate Issue')
FinalApproval = Transition(label='Final Approval')

# Step 1: Initial steps sequential: 'Initial Scan' -> 'Material Sample'
step1 = StrictPartialOrder(nodes=[InitialScan, MaterialSample])
step1.order.add_edge(InitialScan, MaterialSample)

# Step 2: Testing after Material Sample:
# Isotope Test and Carbon Dating are concurrent
step2_nodes = [IsotopeTest, CarbonDating]
step2 = StrictPartialOrder(nodes=step2_nodes)

# Step 3: Concurrently with testing, provenance records cross-checked (provenance check, archive query, ownership review in sequence)
provenance_po = StrictPartialOrder(nodes=[ProvenanceCheck, ArchiveQuery, OwnershipReview])
provenance_po.order.add_edge(ProvenanceCheck, ArchiveQuery)
provenance_po.order.add_edge(ArchiveQuery, OwnershipReview)

# Step 4: After testing & provenance checks finish, Legal Compliance review
# We create a PO with step2 and provenance_po as nodes, and both happen concurrently, then join to LegalCompliance

# To combine step2 and provenance checks into one PO concurrently:
testing_and_provenance = StrictPartialOrder(nodes=[step2, provenance_po])

# step2 and provenance_po run concurrently, so no edges between them

# Now define LegalCompliance node and edges from both step2 and provenance_po to LegalCompliance

root1 = StrictPartialOrder(nodes=[testing_and_provenance, LegalCompliance])
root1.order.add_edge(testing_and_provenance, LegalCompliance)

# But 'testing_and_provenance' is a PO that has step2 and provenance_po concurrently with no link.
# The above is correct: testing_and_provenance as a node aggregates step2 and provenance_po concurrently.
# We'll next merge root1 with step1.

# Step 5: ForensicAnalysis, ExpertInterviews, DatabaseCrosscheck are concurrent after LegalCompliance

forensic_concur = StrictPartialOrder(nodes=[ForensicAnalysis, ExpertInterviews, DatabaseCrosscheck])
# No order among these three; all concurrent

# Step 6: Condition Report and Risk Assessment after forensic analysis cluster
condition_risk = StrictPartialOrder(nodes=[ConditionReport, RiskAssessment])
condition_risk.order.add_edge(ConditionReport, RiskAssessment)

# Step 7: Multidisciplinary committee review after above
committee_cert_approval = StrictPartialOrder(nodes=[CommitteeReview, CertificateIssue, FinalApproval])
committee_cert_approval.order.add_edge(CommitteeReview, CertificateIssue)
committee_cert_approval.order.add_edge(CertificateIssue, FinalApproval)

# Now chain steps together:

# Combine step1 -> testing_and_provenance -> LegalCompliance -> forensic cluster -> condition & risk -> committee, cert issue & approval

# Create combined PO step by step:

# Step1 -> testing_and_provenance
po_1_2 = StrictPartialOrder(nodes=[step1, testing_and_provenance])
po_1_2.order.add_edge(step1, testing_and_provenance)

# Add LegalCompliance node after po_1_2
po_1_2_LC = StrictPartialOrder(nodes=[po_1_2, LegalCompliance])
po_1_2_LC.order.add_edge(po_1_2, LegalCompliance)

# LegalCompliance -> forensic cluster
po_legal_forensic = StrictPartialOrder(nodes=[LegalCompliance, forensic_concur])
po_legal_forensic.order.add_edge(LegalCompliance, forensic_concur)

# forensic cluster -> condition & risk
po_forensic_condition = StrictPartialOrder(nodes=[forensic_concur, condition_risk])
po_forensic_condition.order.add_edge(forensic_concur, condition_risk)

# condition & risk -> committee etc.
po_condition_committee = StrictPartialOrder(nodes=[condition_risk, committee_cert_approval])
po_condition_committee.order.add_edge(condition_risk, committee_cert_approval)

# Combine all big steps with edges connecting them:

root = StrictPartialOrder(
    nodes=[step1, step2, provenance_po, LegalCompliance, forensic_concur, condition_risk, committee_cert_approval]
)

# Connections:

# step1 -> step2 and provenance_po start concurrently after step1->Material Sample
# For clarity, steps 2 and provenance check occur concurrently after step1.

root.order.add_edge(step1, step2)
root.order.add_edge(step1, provenance_po)

# step2 and provenance_po concurrently, so no order between them

# step2 and provenance_po both precede LegalCompliance
root.order.add_edge(step2, LegalCompliance)
root.order.add_edge(provenance_po, LegalCompliance)

# LegalCompliance -> forensic cluster
root.order.add_edge(LegalCompliance, forensic_concur)

# forensic_concur -> condition_risk
root.order.add_edge(forensic_concur, condition_risk)

# condition_risk -> committee_cert_approval
root.order.add_edge(condition_risk, committee_cert_approval)