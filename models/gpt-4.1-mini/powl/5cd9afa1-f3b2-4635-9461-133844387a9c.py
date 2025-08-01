# Generated from: 5cd9afa1-f3b2-4635-9461-133844387a9c.json
# Description: This process involves the intricate validation and certification of rare cultural artifacts using a multi-disciplinary approach. It begins with provenance review, followed by material analysis using advanced spectroscopy. Next, experts conduct stylistic and historical cross-referencing. Digital watermarking is applied for future tracking. Legal clearances are obtained through international heritage law offices. Finally, a tamper-evident seal is issued and logged in a decentralized ledger, ensuring authenticity and preventing illicit trade. The entire workflow requires coordination across legal, scientific, and archival domains to maintain integrity and trust in the artifact authentication process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
ProvenanceReview = Transition(label='Provenance Review')

# Material analysis sub-process: Material Scan -> Spectral Test (strict order)
MaterialScan = Transition(label='Material Scan')
SpectralTest = Transition(label='Spectral Test')
MaterialAnalysis = StrictPartialOrder(nodes=[MaterialScan, SpectralTest])
MaterialAnalysis.order.add_edge(MaterialScan, SpectralTest)

# Expert review sub-process:
# Stylistic and Historical crossref concurrent, then Expert Panel
StyleCheck = Transition(label='Style Check')
HistoricalCrossref = Transition(label='Historical Crossref')
ExpertPanel = Transition(label='Expert Panel')
ExpertReview = StrictPartialOrder(nodes=[StyleCheck, HistoricalCrossref, ExpertPanel])
ExpertReview.order.add_edge(StyleCheck, ExpertPanel)
ExpertReview.order.add_edge(HistoricalCrossref, ExpertPanel)

# Digital watermarking
DigitalWatermark = Transition(label='Digital Watermark')

# Legal clearance sub-process: Legal Clearance -> Heritage Audit
LegalClearance = Transition(label='Legal Clearance')
HeritageAudit = Transition(label='Heritage Audit')
LegalClearanceProcess = StrictPartialOrder(nodes=[LegalClearance, HeritageAudit])
LegalClearanceProcess.order.add_edge(LegalClearance, HeritageAudit)

# Final sealing and logging sub-process:
# Seal Issuance -> Ledger Logging -> Tamper Proof (strict order)
SealIssuance = Transition(label='Seal Issuance')
LedgerLogging = Transition(label='Ledger Logging')
TamperProof = Transition(label='Tamper Proof')
FinalSealProcess = StrictPartialOrder(nodes=[SealIssuance, LedgerLogging, TamperProof])
FinalSealProcess.order.add_edge(SealIssuance, LedgerLogging)
FinalSealProcess.order.add_edge(LedgerLogging, TamperProof)

# Notification and approval concurrent, then artifact dispatch
StakeholderNotify = Transition(label='Stakeholder Notify')
FinalApproval = Transition(label='Final Approval')
ArtifactDispatch = Transition(label='Artifact Dispatch')
NotifyApprove = StrictPartialOrder(nodes=[StakeholderNotify, FinalApproval])
# Stakeholder Notify and Final Approval are concurrent - no order edge

# From NotifyApprove -> ArtifactDispatch
root = StrictPartialOrder(nodes=[
    ProvenanceReview, MaterialAnalysis, ExpertReview, DigitalWatermark,
    LegalClearanceProcess, FinalSealProcess, NotifyApprove, ArtifactDispatch
])

# Add partial order dependencies according to the process description:
# Provenance Review -> Material Analysis
root.order.add_edge(ProvenanceReview, MaterialAnalysis)
# Material Analysis -> Expert Review
root.order.add_edge(MaterialAnalysis, ExpertReview)
# Expert Review -> Digital Watermark
root.order.add_edge(ExpertReview, DigitalWatermark)
# Digital Watermark -> Legal Clearance Process
root.order.add_edge(DigitalWatermark, LegalClearanceProcess)
# Legal Clearance Process -> Final Seal Process
root.order.add_edge(LegalClearanceProcess, FinalSealProcess)
# Final Seal Process -> NotifyApprove
root.order.add_edge(FinalSealProcess, NotifyApprove)
# NotifyApprove -> Artifact Dispatch
root.order.add_edge(NotifyApprove, ArtifactDispatch)