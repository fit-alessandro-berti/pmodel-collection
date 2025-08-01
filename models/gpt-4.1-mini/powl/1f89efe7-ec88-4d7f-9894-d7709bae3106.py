# Generated from: 1f89efe7-ec88-4d7f-9894-d7709bae3106.json
# Description: This process describes the comprehensive workflow for authenticating rare historical artifacts before acquisition by a museum. It involves initial provenance research, multispectral imaging analysis, expert consultations across various disciplines, chemical composition testing, and digital ledger registration. The process ensures artifacts are verified for authenticity, legal ownership, and cultural significance, minimizing risks of forgery or illicit acquisition. It also incorporates stakeholder approvals, insurance appraisal, and final archival documentation, integrating technology with traditional expertise to uphold ethical and scholarly standards in artifact curation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ProvenanceCheck = Transition('Provenance Check')
VisualSurvey = Transition('Visual Survey')
MaterialScan = Transition('Material Scan')
XRayImaging = Transition('XRay Imaging')
ExpertReview = Transition('Expert Review')
CarbonDating = Transition('Carbon Dating')
SpectralAnalysis = Transition('Spectral Analysis')
LegalVerify = Transition('Legal Verify')
OwnershipTrace = Transition('Ownership Trace')
CulturalAssess = Transition('Cultural Assess')
StakeholderMeet = Transition('Stakeholder Meet')
InsuranceQuote = Transition('Insurance Quote')
RiskAssess = Transition('Risk Assess')
LedgerEntry = Transition('Ledger Entry')
ArchiveUpdate = Transition('Archive Update')
FinalApproval = Transition('Final Approval')

# Imaging analysis partial order: Visual Survey --> {Material Scan, XRay Imaging} concurrent
imaging_po = StrictPartialOrder(nodes=[VisualSurvey, MaterialScan, XRayImaging])
imaging_po.order.add_edge(VisualSurvey, MaterialScan)
imaging_po.order.add_edge(VisualSurvey, XRayImaging)

# Expert consultations partial order: Expert Review --> {Carbon Dating, Spectral Analysis} concurrent
expert_consult_po = StrictPartialOrder(nodes=[ExpertReview, CarbonDating, SpectralAnalysis])
expert_consult_po.order.add_edge(ExpertReview, CarbonDating)
expert_consult_po.order.add_edge(ExpertReview, SpectralAnalysis)

# Legal ownership checks partial order: Legal Verify --> {Ownership Trace, Cultural Assess} concurrent
legal_checks_po = StrictPartialOrder(nodes=[LegalVerify, OwnershipTrace, CulturalAssess])
legal_checks_po.order.add_edge(LegalVerify, OwnershipTrace)
legal_checks_po.order.add_edge(LegalVerify, CulturalAssess)

# Stakeholder approvals partial order: Stakeholder Meet --> Insurance Quote --> Risk Assess (linear)
stakeholder_po = StrictPartialOrder(nodes=[StakeholderMeet, InsuranceQuote, RiskAssess])
stakeholder_po.order.add_edge(StakeholderMeet, InsuranceQuote)
stakeholder_po.order.add_edge(InsuranceQuote, RiskAssess)

# Final archival partial order: Ledger Entry --> Archive Update --> Final Approval (linear)
final_archival_po = StrictPartialOrder(nodes=[LedgerEntry, ArchiveUpdate, FinalApproval])
final_archival_po.order.add_edge(LedgerEntry, ArchiveUpdate)
final_archival_po.order.add_edge(ArchiveUpdate, FinalApproval)

# Loop node for expert consultations (e.g. re-execution possible)
# Execute ExpertReview and its tests, then choose to loop or exit
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult_po, SilentTransition()])

# Start: Provenance Check --> Imaging Analysis --> expert_loop --> legal checks --> stakeholder approvals --> final archival
root = StrictPartialOrder(
    nodes=[ProvenanceCheck, imaging_po, expert_loop, legal_checks_po, stakeholder_po, final_archival_po]
)

root.order.add_edge(ProvenanceCheck, imaging_po)
root.order.add_edge(imaging_po, expert_loop)
root.order.add_edge(expert_loop, legal_checks_po)
root.order.add_edge(legal_checks_po, stakeholder_po)
root.order.add_edge(stakeholder_po, final_archival_po)