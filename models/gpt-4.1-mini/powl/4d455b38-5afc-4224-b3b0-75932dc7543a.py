# Generated from: 4d455b38-5afc-4224-b3b0-75932dc7543a.json
# Description: This process involves the detailed verification and certification of rare cultural artifacts before acquisition or sale. It integrates multidisciplinary expert analysis, provenance research, non-invasive material testing, and legal clearance. Activities include coordinating with historians, forensic labs, and legal advisors to ensure authenticity and compliance with international trade laws. The workflow also manages digital archiving of findings, stakeholder communications, and final certification issuance, ensuring transparency and traceability throughout the artifact's lifecycle from discovery to market placement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities as Transitions
InitialReview = Transition(label='Initial Review')
ProvenanceCheck = Transition(label='Provenance Check')
ExpertConsultation = Transition(label='Expert Consultation')
MaterialSampling = Transition(label='Material Sampling')
LabAnalysis = Transition(label='Lab Analysis')
DataSynthesis = Transition(label='Data Synthesis')
LegalClearance = Transition(label='Legal Clearance')
DigitalArchiving = Transition(label='Digital Archiving')
StakeholderUpdate = Transition(label='Stakeholder Update')
RiskAssessment = Transition(label='Risk Assessment')
MarketEvaluation = Transition(label='Market Evaluation')
CertificationDraft = Transition(label='Certification Draft')
QualityAssurance = Transition(label='Quality Assurance')
FinalApproval = Transition(label='Final Approval')
DocumentIssuance = Transition(label='Document Issuance')
PostSaleAudit = Transition(label='Post-Sale Audit')

# Modelling loops for Quality Assurance cycle: loop of (Quality Assurance, Risk Assessment)
loopQA = OperatorPOWL(operator=Operator.LOOP, children=[QualityAssurance, RiskAssessment])

# Partial order for artifact evaluation and testing:
# InitialReview -> ProvenanceCheck and ExpertConsultation and MaterialSampling concurrent after InitialReview
# MaterialSampling -> LabAnalysis
# LabAnalysis -> DataSynthesis -> LegalClearance
po1_nodes = [InitialReview, ProvenanceCheck, ExpertConsultation, MaterialSampling, LabAnalysis, DataSynthesis, LegalClearance]
po1 = StrictPartialOrder(nodes=po1_nodes)
po1.order.add_edge(InitialReview, ProvenanceCheck)
po1.order.add_edge(InitialReview, ExpertConsultation)
po1.order.add_edge(InitialReview, MaterialSampling)
po1.order.add_edge(MaterialSampling, LabAnalysis)
po1.order.add_edge(LabAnalysis, DataSynthesis)
po1.order.add_edge(DataSynthesis, LegalClearance)

# After Legal Clearance, digital archiving starts in parallel with stakeholder update and market evaluation
po2_nodes = [LegalClearance, DigitalArchiving, StakeholderUpdate, MarketEvaluation]
po2 = StrictPartialOrder(nodes=po2_nodes)
po2.order.add_edge(LegalClearance, DigitalArchiving)
po2.order.add_edge(LegalClearance, StakeholderUpdate)
po2.order.add_edge(LegalClearance, MarketEvaluation)

# Certification process after market evaluation and stakeholder update + loopQA cycle
po3_nodes = [MarketEvaluation, StakeholderUpdate, loopQA, CertificationDraft, FinalApproval, DocumentIssuance]
po3 = StrictPartialOrder(nodes=po3_nodes)
po3.order.add_edge(MarketEvaluation, CertificationDraft)
po3.order.add_edge(StakeholderUpdate, CertificationDraft)
po3.order.add_edge(CertificationDraft, loopQA)  # loopQA before final approval
po3.order.add_edge(loopQA, FinalApproval)
po3.order.add_edge(FinalApproval, DocumentIssuance)

# Post-sale audit after document issuance
po4_nodes = [DocumentIssuance, PostSaleAudit]
po4 = StrictPartialOrder(nodes=po4_nodes)
po4.order.add_edge(DocumentIssuance, PostSaleAudit)

# Compose entire process partial order - all components linked linearly
root_nodes = [po1, po2, po3, po4]
root = StrictPartialOrder(nodes=root_nodes)
root.order.add_edge(po1, po2)
root.order.add_edge(po2, po3)
root.order.add_edge(po3, po4)