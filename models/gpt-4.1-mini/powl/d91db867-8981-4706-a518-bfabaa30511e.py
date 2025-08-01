# Generated from: d91db867-8981-4706-a518-bfabaa30511e.json
# Description: This process involves the detailed verification and authentication of rare cultural artifacts for auction houses and private collectors. It begins with initial provenance research, followed by scientific material analysis, historical context validation, and expert consultations. Each artifact undergoes multi-stage imaging, condition assessment, and legal compliance checks. Additionally, the process includes risk evaluation for forgery, coordination with international registries, and ethical clearance. The final steps involve documentation creation, certification issuance, and secure digital archiving, ensuring the artifact's authenticity and legal transferability for sale or display purposes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity nodes
ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
ContextReview = Transition(label='Context Review')
ExpertConsult = Transition(label='Expert Consult')
ImageCapture = Transition(label='Image Capture')
ConditionTest = Transition(label='Condition Test')
ForgeryRisk = Transition(label='Forgery Risk')
RegistryCrosscheck = Transition(label='Registry Crosscheck')
LegalVerify = Transition(label='Legal Verify')
EthicsReview = Transition(label='Ethics Review')
ReportDraft = Transition(label='Report Draft')
CertificateIssue = Transition(label='Certificate Issue')
DigitalArchive = Transition(label='Digital Archive')
TransferSetup = Transition(label='Transfer Setup')
FinalApproval = Transition(label='Final Approval')

# First phase: initial provenance research and scientific/historical/expert checks
phase1 = StrictPartialOrder(nodes=[ProvenanceCheck, MaterialScan, ContextReview, ExpertConsult])
# order: ProvenanceCheck before the other three, which can be concurrent
phase1.order.add_edge(ProvenanceCheck, MaterialScan)
phase1.order.add_edge(ProvenanceCheck, ContextReview)
phase1.order.add_edge(ProvenanceCheck, ExpertConsult)

# Second phase: multi-stage imaging, condition assessment, legal compliance
phase2 = StrictPartialOrder(nodes=[ImageCapture, ConditionTest, LegalVerify])
# Imaging then ConditionTest then LegalVerify sequentially
phase2.order.add_edge(ImageCapture, ConditionTest)
phase2.order.add_edge(ConditionTest, LegalVerify)

# Risk evaluation and coordination + ethics clearance in parallel
risk_and_others = StrictPartialOrder(nodes=[ForgeryRisk, RegistryCrosscheck, EthicsReview])
# No order among these: all concurrent

# Third phase: documentation creation, certification, digital archive
phase3 = StrictPartialOrder(nodes=[ReportDraft, CertificateIssue, DigitalArchive])
# Sequential order: ReportDraft -> CertificateIssue -> DigitalArchive
phase3.order.add_edge(ReportDraft, CertificateIssue)
phase3.order.add_edge(CertificateIssue, DigitalArchive)

# Final phase: Transfer Setup and Final Approval sequential
final_phase = StrictPartialOrder(nodes=[TransferSetup, FinalApproval])
final_phase.order.add_edge(TransferSetup, FinalApproval)

# Combine phases with correct partial ordering
root = StrictPartialOrder(
    nodes=[phase1, phase2, risk_and_others, phase3, final_phase]
)

# Add edges to order phases appropriately:
# phase1 before phase2, risk_and_others, and phase3 (they depend on previous checks)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase1, risk_and_others)
root.order.add_edge(phase1, phase3)  # documentation likely depends on initial research but...
# Actually documentation depends on legal verify and ethics review, so phase3 depends on phase2 and risk_and_others
root.order.add_edge(phase2, phase3)
root.order.add_edge(risk_and_others, phase3)

# Finally, final_phase depends on phase3 completing
root.order.add_edge(phase3, final_phase)