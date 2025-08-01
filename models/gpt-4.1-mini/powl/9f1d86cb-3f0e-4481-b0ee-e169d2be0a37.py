# Generated from: 9f1d86cb-3f0e-4481-b0ee-e169d2be0a37.json
# Description: This process involves the comprehensive verification and authentication of historical artifacts using a multi-disciplinary approach. It includes initial provenance research, scientific material analysis, contextual historical comparison, expert peer review, digital imaging, and blockchain certification. Each artifact undergoes condition assessment, restoration feasibility evaluation, and risk management before final authentication. The process integrates advanced AI pattern recognition with manual expert validation, ensuring both technological precision and human judgment. The cycle concludes with secure cataloging and controlled public disclosure, balancing conservation needs with scholarly access while maintaining a transparent audit trail for future reference and potential repatriation claims.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions with given labels
ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
ContextReview = Transition(label='Context Review')
ExpertConsult = Transition(label='Expert Consult')
ImagingCapture = Transition(label='Imaging Capture')
AIAnalysis = Transition(label='AI Analysis')
ConditionAssess = Transition(label='Condition Assess')
RestorationPlan = Transition(label='Restoration Plan')
RiskEvaluate = Transition(label='Risk Evaluate')
PeerReview = Transition(label='Peer Review')
BlockchainCert = Transition(label='Blockchain Cert')
CatalogEntry = Transition(label='Catalog Entry')
PublicRelease = Transition(label='Public Release')
AuditLog = Transition(label='Audit Log')
RepatriationEval = Transition(label='Repatriation Eval')

# Initial provenance research (= ProvenanceCheck)
# Scientific material analysis = MaterialScan
# Contextual historical comparison = ContextReview
# Expert peer review included later; Expert Consult likely between ContextReview and PeerReview
# Digital imaging = ImagingCapture
# AI analysis = AIAnalysis
# Condition assessment, restoration feasibility evaluation, risk management grouped as ConditionAssess -> RestorationPlan -> RiskEvaluate
# Expert peer review = PeerReview
# Blockchain certification = BlockchainCert
# Catalog entry = CatalogEntry
# Public release = PublicRelease
# Audit log = AuditLog
# Repatriation evaluation = RepatriationEval

# First partial order for the initial research phase:
# ProvenanceCheck --> MaterialScan and ContextReview (concurrent after ProvenanceCheck)
initial_PO = StrictPartialOrder(
    nodes=[ProvenanceCheck, MaterialScan, ContextReview]
)
initial_PO.order.add_edge(ProvenanceCheck, MaterialScan)
initial_PO.order.add_edge(ProvenanceCheck, ContextReview)

# ExpertConsult likely depends on ContextReview
expert_PO = StrictPartialOrder(
    nodes=[ContextReview, ExpertConsult]
)
expert_PO.order.add_edge(ContextReview, ExpertConsult)

# ImagingCapture and AIAnalysis are part of scientific & imaging analysis, can run concurrently after MaterialScan and ExpertConsult
imaging_ai_PO = StrictPartialOrder(
    nodes=[MaterialScan, ExpertConsult, ImagingCapture, AIAnalysis]
)
imaging_ai_PO.order.add_edge(MaterialScan, ImagingCapture)
imaging_ai_PO.order.add_edge(ExpertConsult, AIAnalysis)

# Next, condition assessment, restoration plan, risk evaluation should be strictly ordered
condition_PO = StrictPartialOrder(
    nodes=[ConditionAssess, RestorationPlan, RiskEvaluate]
)
condition_PO.order.add_edge(ConditionAssess, RestorationPlan)
condition_PO.order.add_edge(RestorationPlan, RiskEvaluate)

# Peer review depends on AIAnalysis, RiskEvaluate, and possibly ExpertConsult
peer_review_PO = StrictPartialOrder(
    nodes=[AIAnalysis, RiskEvaluate, PeerReview]
)
peer_review_PO.order.add_edge(AIAnalysis, PeerReview)
peer_review_PO.order.add_edge(RiskEvaluate, PeerReview)

# Blockchain cert follows PeerReview
blockchain_PO = StrictPartialOrder(
    nodes=[PeerReview, BlockchainCert]
)
blockchain_PO.order.add_edge(PeerReview, BlockchainCert)

# After certification: catalog entry
catalog_PO = StrictPartialOrder(
    nodes=[BlockchainCert, CatalogEntry]
)
catalog_PO.order.add_edge(BlockchainCert, CatalogEntry)

# Public release and audit log run in parallel after CatalogEntry - 
# but audit log must still reflect cataloging and other traceability
release_audit_PO = StrictPartialOrder(
    nodes=[CatalogEntry, PublicRelease, AuditLog]
)
release_audit_PO.order.add_edge(CatalogEntry, PublicRelease)
release_audit_PO.order.add_edge(CatalogEntry, AuditLog)

# Repatriation evaluation depends on AuditLog (audit trail for future claims)
repatriation_PO = StrictPartialOrder(
    nodes=[AuditLog, RepatriationEval]
)
repatriation_PO.order.add_edge(AuditLog, RepatriationEval)

# Combine initial_PO and expert_PO:
first_phase = StrictPartialOrder(
    nodes=[initial_PO, expert_PO]
)
first_phase.order.add_edge(initial_PO, expert_PO)  # after initial_PO finish, expert_PO

# Because expert_PO contains ContextReview and ExpertConsult and contextReview already in initial_PO, 
# but to preserve concurrency and ordering, instead of adding nodes twice use the expert_PO only after initial_PO completion.
# Since ContextReview is in both, let's keep initial_PO without ContextReview to avoid double counting.

# Redefine initial_PO without ContextReview (ContextReview in expert_PO)
initial_PO = StrictPartialOrder(
    nodes=[ProvenanceCheck, MaterialScan]
)
initial_PO.order.add_edge(ProvenanceCheck, MaterialScan)

# Now first_phase combining initial_PO and expert_PO again:
first_phase = StrictPartialOrder(
    nodes=[initial_PO, expert_PO]
)
first_phase.order.add_edge(initial_PO, expert_PO)

# Combine imaging_ai_PO after both initial_PO and expert_PO completed
# imaging_ai_PO depends on MaterialScan and ExpertConsult (largest predecessors)
imaging_ai_PO = StrictPartialOrder(
    nodes=[MaterialScan, ExpertConsult, ImagingCapture, AIAnalysis]
)
imaging_ai_PO.order.add_edge(MaterialScan, ImagingCapture)
imaging_ai_PO.order.add_edge(ExpertConsult, AIAnalysis)

# To avoid duplicate nodes as they are in other POs, nodes should be referenced once.
# We'll create atomic transitions once and compose the partial orders referencing those transitions.

# Build the model bottom-up referencing same transitions to avoid duplication:

# Step 1: initial provenance research and scientific analysis concurrency:
step1 = StrictPartialOrder(
    nodes=[ProvenanceCheck, MaterialScan, ContextReview]
)
step1.order.add_edge(ProvenanceCheck, MaterialScan)
step1.order.add_edge(ProvenanceCheck, ContextReview)

# Step 2: expert consult after ContextReview:
step2 = StrictPartialOrder(
    nodes=[ContextReview, ExpertConsult]
)
step2.order.add_edge(ContextReview, ExpertConsult)

# Step 3: imaging and AI analysis after MaterialScan and ExpertConsult
step3 = StrictPartialOrder(
    nodes=[MaterialScan, ExpertConsult, ImagingCapture, AIAnalysis]
)
step3.order.add_edge(MaterialScan, ImagingCapture)
step3.order.add_edge(ExpertConsult, AIAnalysis)

# Step 4: condition assessment sequence
step4 = StrictPartialOrder(
    nodes=[ConditionAssess, RestorationPlan, RiskEvaluate]
)
step4.order.add_edge(ConditionAssess, RestorationPlan)
step4.order.add_edge(RestorationPlan, RiskEvaluate)

# Step 5: peer review after AIAnalysis and RiskEvaluate
step5 = StrictPartialOrder(
    nodes=[AIAnalysis, RiskEvaluate, PeerReview]
)
step5.order.add_edge(AIAnalysis, PeerReview)
step5.order.add_edge(RiskEvaluate, PeerReview)

# Step 6: blockchain cert after peer review
step6 = StrictPartialOrder(
    nodes=[PeerReview, BlockchainCert]
)
step6.order.add_edge(PeerReview, BlockchainCert)

# Step 7: catalog entry after blockchain cert
step7 = StrictPartialOrder(
    nodes=[BlockchainCert, CatalogEntry]
)
step7.order.add_edge(BlockchainCert, CatalogEntry)

# Step 8: public release and audit log after catalog entry (concurrent)
step8 = StrictPartialOrder(
    nodes=[CatalogEntry, PublicRelease, AuditLog]
)
step8.order.add_edge(CatalogEntry, PublicRelease)
step8.order.add_edge(CatalogEntry, AuditLog)

# Step 9: repatriation eval after audit log
step9 = StrictPartialOrder(
    nodes=[AuditLog, RepatriationEval]
)
step9.order.add_edge(AuditLog, RepatriationEval)

# Now create partial orders combining these steps respecting dependencies:

# Combine step1 and step2 (step2 depends on ContextReview from step1)
phase1 = StrictPartialOrder(nodes=[step1, step2])
phase1.order.add_edge(step1, step2)

# Combine phase1 and step3 (step3 depends on MaterialScan and ExpertConsult, which are in step1 and step2)
phase2 = StrictPartialOrder(nodes=[phase1, step3])
phase2.order.add_edge(phase1, step3)

# Combine phase2 and step4 (condition assessment etc. after imaging/AI analysis)
phase3 = StrictPartialOrder(nodes=[phase2, step4])
phase3.order.add_edge(phase2, step4)

# Combine phase3 and step5 (peer review after AI analysis and risk evaluate)
phase4 = StrictPartialOrder(nodes=[phase3, step5])
# AIAnalysis is in step3 (in phase2), RiskEvaluate is in step4, so phase4 depends on both:
phase4.order.add_edge(phase3, step5)

# Combine phase4 and step6 (blockchain cert after peer review)
phase5 = StrictPartialOrder(nodes=[phase4, step6])
phase5.order.add_edge(phase4, step6)

# Combine phase5 and step7 (catalog entry after blockchain cert)
phase6 = StrictPartialOrder(nodes=[phase5, step7])
phase6.order.add_edge(phase5, step7)

# Combine phase6 and step8 (public release and audit log after catalog entry)
phase7 = StrictPartialOrder(nodes=[phase6, step8])
phase7.order.add_edge(phase6, step8)

# Combine phase7 and step9 (repatriation eval after audit log)
root = StrictPartialOrder(nodes=[phase7, step9])
root.order.add_edge(phase7, step9)