# Generated from: 6c460305-49fb-4167-949d-6f58fedef4b6.json
# Description: This process involves the intricate verification and authentication of rare historical artifacts for high-profile clients. It starts with initial provenance research, followed by multi-layered physical examinations including spectroscopy and carbon dating. Expert consultations are organized to validate findings, and legal compliance with international trade laws is ensured. Digital fingerprinting and blockchain registration provide immutable tracking, while insurance valuation and client briefing close the cycle. This atypical process demands coordination between archaeologists, legal experts, technologists, and insurers to guarantee authenticity and secure ownership transfer in a highly specialized market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
ProvenanceCheck = Transition(label='Provenance Check')

# Physical Exams parallel activities
MaterialScan = Transition(label='Material Scan')
CarbonDate = Transition(label='Carbon Date')
SpectralTest = Transition(label='Spectral Test')

# Expert consultation
ExpertReview = Transition(label='Expert Review')

# Legal compliance: composed of Legal Audit then Trade Verify
LegalAudit = Transition(label='Legal Audit')
TradeVerify = Transition(label='Trade Verify')
LegalCompliance = StrictPartialOrder(nodes=[LegalAudit, TradeVerify])
LegalCompliance.order.add_edge(LegalAudit, TradeVerify)

# Digital fingerprinting and blockchain registration in sequence
Fingerprinting = Transition(label='Fingerprinting')
BlockchainReg = Transition(label='Blockchain Reg')
DigitalTrack = StrictPartialOrder(nodes=[Fingerprinting, BlockchainReg])
DigitalTrack.order.add_edge(Fingerprinting, BlockchainReg)

# Insurance valuation steps
ValuationAssess = Transition(label='Valuation Assess')
InsuranceQuote = Transition(label='Insurance Quote')
InsuranceProc = StrictPartialOrder(nodes=[ValuationAssess, InsuranceQuote])
InsuranceProc.order.add_edge(ValuationAssess, InsuranceQuote)

# Closing and final archiving steps
ClientBrief = Transition(label='Client Brief')
OwnershipLog = Transition(label='Ownership Log')
TransferApprove = Transition(label='Transfer Approve')
FinalArchive = Transition(label='Final Archive')

Closing = StrictPartialOrder(nodes=[ClientBrief, OwnershipLog, TransferApprove, FinalArchive])
Closing.order.add_edge(ClientBrief, OwnershipLog)
Closing.order.add_edge(OwnershipLog, TransferApprove)
Closing.order.add_edge(TransferApprove, FinalArchive)

# Physical examinations are concurrent: MaterialScan, CarbonDate, SpectralTest
PhysicalExams = StrictPartialOrder(nodes=[MaterialScan, CarbonDate, SpectralTest])
# no order edges: all concurrent

# Combine physical exams followed by ExpertReview sequentially
PostPhysical = StrictPartialOrder(nodes=[PhysicalExams, ExpertReview])
PostPhysical.order.add_edge(PhysicalExams, ExpertReview)

# Legal compliance and digital tracking can be concurrent after expert review
LegalAndDigital = StrictPartialOrder(nodes=[LegalCompliance, DigitalTrack])
# no order edges: concurrent

# Insurance and closing steps are sequential after legal and digital
InsAndClose = StrictPartialOrder(nodes=[InsuranceProc, Closing])
InsAndClose.order.add_edge(InsuranceProc, Closing)

# Merge all after ProvenanceCheck:
MiddlePhase = StrictPartialOrder(nodes=[PostPhysical, LegalAndDigital, InsAndClose])
# Execution order:
# PostPhysical --> LegalAndDigital --> InsAndClose
MiddlePhase.order.add_edge(PostPhysical, LegalAndDigital)
MiddlePhase.order.add_edge(LegalAndDigital, InsAndClose)

# Root partial order: ProvenanceCheck --> MiddlePhase
root = StrictPartialOrder(nodes=[ProvenanceCheck, MiddlePhase])
root.order.add_edge(ProvenanceCheck, MiddlePhase)