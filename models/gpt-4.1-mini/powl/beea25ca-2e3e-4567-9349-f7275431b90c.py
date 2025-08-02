# Generated from: beea25ca-2e3e-4567-9349-f7275431b90c.json
# Description: This complex business process governs the authentication and provenance verification of rare historical artifacts before acquisition or exhibition. It involves multidisciplinary evaluations including chemical composition analysis, historical documentation cross-referencing, expert consultations, and advanced imaging techniques. The process ensures that artifacts meet stringent authenticity criteria by integrating scientific data with archival research. Each artifact undergoes risk assessment for forgery, condition appraisal, and legal clearance. The workflow culminates in a detailed provenance report and a decision on acquisition or loan, safeguarding institutional collections and maintaining public trust in exhibited items.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SampleCollection = Transition(label='Sample Collection')
ChemicalScan = Transition(label='Chemical Scan')
ImageCapture = Transition(label='Image Capture')
DataAnalysis = Transition(label='Data Analysis')
ExpertReview = Transition(label='Expert Review')
ArchivalSearch = Transition(label='Archival Search')
ForgeryCheck = Transition(label='Forgery Check')
ConditionSurvey = Transition(label='Condition Survey')
LegalReview = Transition(label='Legal Review')
RiskAssess = Transition(label='Risk Assess')
ReportDraft = Transition(label='Report Draft')
ProvenanceVerify = Transition(label='Provenance Verify')
AcquisitionVote = Transition(label='Acquisition Vote')
LoanSetup = Transition(label='Loan Setup')
FinalApproval = Transition(label='Final Approval')
Documentation = Transition(label='Documentation')

# Step1: Initial scientific and archival evaluation (parallel)
# Scientific branch: Sample Collection -> Chemical Scan & Image Capture (parallel) -> Data Analysis
sci_PO = StrictPartialOrder(nodes=[SampleCollection, ChemicalScan, ImageCapture, DataAnalysis])
sci_PO.order.add_edge(SampleCollection, ChemicalScan)
sci_PO.order.add_edge(SampleCollection, ImageCapture)
sci_PO.order.add_edge(ChemicalScan, DataAnalysis)
sci_PO.order.add_edge(ImageCapture, DataAnalysis)

# Archival branch: Expert Review and Archival Search in parallel
arch_PO = StrictPartialOrder(nodes=[ExpertReview, ArchivalSearch])

# Merge sci_PO and arch_PO in parallel (no order between the two branches)
eval_PO = StrictPartialOrder(nodes=[sci_PO, arch_PO])

# Step2: Risk assessment: Forgery Check, Condition Survey, Legal Review in parallel, 
# all ordered before Risk Assess
risk_nodes = [ForgeryCheck, ConditionSurvey, LegalReview, RiskAssess]
risk_PO = StrictPartialOrder(nodes=risk_nodes)
risk_PO.order.add_edge(ForgeryCheck, RiskAssess)
risk_PO.order.add_edge(ConditionSurvey, RiskAssess)
risk_PO.order.add_edge(LegalReview, RiskAssess)

# Step3: After evaluations and risk assessment, provenance verify
# So ordering is: evaluation (both) -> risk_PO -> Provenance Verify
# Use a PO with nodes = [eval_PO, risk_PO, ProvenanceVerify]
# Add edges: eval_PO -> risk_PO, risk_PO -> ProvenanceVerify
mid_PO = StrictPartialOrder(nodes=[eval_PO, risk_PO, ProvenanceVerify])
mid_PO.order.add_edge(eval_PO, risk_PO)
mid_PO.order.add_edge(risk_PO, ProvenanceVerify)

# Step4: Report draft after Provenance Verify
# Then choice between Acquisition Vote and Loan Setup (xor)
# Then Final Approval and Documentation in sequence after choice
choice_acquire_loan = OperatorPOWL(operator=Operator.XOR, children=[AcquisitionVote, LoanSetup])

final_PO = StrictPartialOrder(nodes=[ProvenanceVerify, ReportDraft, choice_acquire_loan, FinalApproval, Documentation])
final_PO.order.add_edge(ProvenanceVerify, ReportDraft)
final_PO.order.add_edge(ReportDraft, choice_acquire_loan)
final_PO.order.add_edge(choice_acquire_loan, FinalApproval)
final_PO.order.add_edge(FinalApproval, Documentation)

# Step5: Compose entire process as sequence of mid_PO and final_PO
root = StrictPartialOrder(nodes=[mid_PO, final_PO])
root.order.add_edge(mid_PO, final_PO)