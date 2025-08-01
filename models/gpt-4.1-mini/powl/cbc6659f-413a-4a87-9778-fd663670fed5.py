# Generated from: cbc6659f-413a-4a87-9778-fd663670fed5.json
# Description: This process involves the comprehensive verification and authentication of historical artifacts before acquisition by a museum. It includes provenance research, material analysis, expert consultations, and legal compliance checks. The workflow ensures that each artifact's origin is verified, authenticity confirmed through scientific and historical methods, and ownership legally cleared. Detailed documentation is maintained throughout, with cross-departmental reviews involving curators, legal advisors, and conservation specialists. The process concludes with final approval and cataloging for exhibit or storage, safeguarding heritage and minimizing acquisition risks.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
ExpertReview = Transition(label='Expert Review')
LegalAudit = Transition(label='Legal Audit')
ConditionReport = Transition(label='Condition Report')
CarbonDating = Transition(label='Carbon Dating')
OwnershipVerify = Transition(label='Ownership Verify')
HistoricalMatch = Transition(label='Historical Match')
CustomsClearance = Transition(label='Customs Clearance')
RiskAssessment = Transition(label='Risk Assessment')
EthicsApproval = Transition(label='Ethics Approval')
RestorationPlan = Transition(label='Restoration Plan')
FinalApproval = Transition(label='Final Approval')
CatalogEntry = Transition(label='Catalog Entry')
ExhibitPrep = Transition(label='Exhibit Prep')

# Build the provenance verification branch (Provenance Check, Historical Match, Carbon Dating)
provenance_check_branch = StrictPartialOrder(nodes=[ProvenanceCheck, HistoricalMatch, CarbonDating])
provenance_check_branch.order.add_edge(ProvenanceCheck, HistoricalMatch)
provenance_check_branch.order.add_edge(HistoricalMatch, CarbonDating)

# Material analysis branch (Material Scan, Carbon Dating, Condition Report)
material_analysis = StrictPartialOrder(nodes=[MaterialScan, CarbonDating, ConditionReport])
material_analysis.order.add_edge(MaterialScan, CarbonDating)
material_analysis.order.add_edge(CarbonDating, ConditionReport)

# Expert consultations branch (Expert Review, Ethics Approval, Restoration Plan)
expert_review_branch = StrictPartialOrder(nodes=[ExpertReview, EthicsApproval, RestorationPlan])
expert_review_branch.order.add_edge(ExpertReview, EthicsApproval)
expert_review_branch.order.add_edge(EthicsApproval, RestorationPlan)

# Legal compliance branch (Legal Audit, Ownership Verify, Customs Clearance)
legal_compliance = StrictPartialOrder(nodes=[LegalAudit, OwnershipVerify, CustomsClearance])
legal_compliance.order.add_edge(LegalAudit, OwnershipVerify)
legal_compliance.order.add_edge(OwnershipVerify, CustomsClearance)

# Risk assessment branch (Risk Assessment)
risk_assessment = RiskAssessment

# Cross-departmental reviews = combine Condition Report, Restoration Plan, Risk Assessment, Legal Compliance, Expert Review branch
# ConditionReport, RestorationPlan, RiskAssessment, CustomsClearance are the review activities we want partially ordered

# Let's build a partial order for the review phase where:
# - Condition Report and Legal Compliance (Customs Clearance) and Expert Review branch must finish
# - Risk Assessment can be concurrent with others

# Build partial order with nodes: ConditionReport, CustomsClearance, RestorationPlan, RiskAssessment
review_phase = StrictPartialOrder(
    nodes=[ConditionReport, CustomsClearance, RestorationPlan, RiskAssessment]
)
# Order edges:
# ConditionReport --> RiskAssessment (assessment after conditions known)
review_phase.order.add_edge(ConditionReport, RiskAssessment)
# RestorationPlan --> RiskAssessment (restoration informs assessment)
review_phase.order.add_edge(RestorationPlan, RiskAssessment)
# CustomsClearance --> RiskAssessment
review_phase.order.add_edge(CustomsClearance, RiskAssessment)
# To capture cross-departmental reviews, no other strict ordering

# Now, merge initial verifications: provenance_check_branch, material_analysis, expert_review_branch, legal_compliance
# Material Analysis and Provenance check converge before continuing with reviews - need ordering.

# Create a strict partial order joining provenance_check_branch and material_analysis:
verifications = StrictPartialOrder(
    nodes=[provenance_check_branch, material_analysis]
)
verifications.order.add_edge(provenance_check_branch, material_analysis)
# Let's embed the expert_review_branch and legal_compliance as well, so full initial verifications are:
initial_verifications = StrictPartialOrder(
    nodes=[verifications, expert_review_branch, legal_compliance]
)
# Ordering:
# verifications (provenance -> material) must be before expert_review_branch and legal_compliance
initial_verifications.order.add_edge(verifications, expert_review_branch)
initial_verifications.order.add_edge(verifications, legal_compliance)

# Now, after initial_verifications, we have review_phase:
# Combine initial_verifications and review_phase:
all_checks = StrictPartialOrder(
    nodes=[initial_verifications, review_phase]
)
all_checks.order.add_edge(initial_verifications, review_phase)

# Final approval follows cross-departmental reviews
# Then catalog entry and exhibit prep are sequential
final_steps = StrictPartialOrder(
    nodes=[FinalApproval, CatalogEntry, ExhibitPrep]
)
final_steps.order.add_edge(FinalApproval, CatalogEntry)
final_steps.order.add_edge(CatalogEntry, ExhibitPrep)

# Combine all_checks and final_steps
root = StrictPartialOrder(
    nodes=[all_checks, final_steps]
)
root.order.add_edge(all_checks, final_steps)