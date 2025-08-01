# Generated from: af7090ae-6cf5-487c-8eab-2842aaa09c57.json
# Description: This process outlines the comprehensive steps involved in authenticating historical artifacts for museum acquisition. It begins with initial artifact receipt and condition assessment, followed by multi-disciplinary analysis including chemical composition testing, provenance documentation verification, and stylistic comparison by experts. The workflow incorporates advanced imaging techniques and carbon dating, cross-referencing global databases to confirm artifact origin and legitimacy. Legal compliance checks and risk assessment for potential forgeries are conducted before final authentication approval. The process ends with detailed reporting and secure artifact cataloging to ensure traceability and preservation standards are met throughout the acquisition lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

ArtifactReceipt = Transition(label='Artifact Receipt')
ConditionCheck = Transition(label='Condition Check')

SampleExtraction = Transition(label='Sample Extraction')
ChemicalTesting = Transition(label='Chemical Testing')
ProvenanceReview = Transition(label='Provenance Review')
StylisticAudit = Transition(label='Stylistic Audit')

ImagingScan = Transition(label='Imaging Scan')
CarbonDating = Transition(label='Carbon Dating')
DatabaseCrosscheck = Transition(label='Database Crosscheck')

ForgeryAnalysis = Transition(label='Forgery Analysis')
LegalReview = Transition(label='Legal Review')
RiskAssessment = Transition(label='Risk Assessment')

ApprovalMeeting = Transition(label='Approval Meeting')

ReportDrafting = Transition(label='Report Drafting')
CatalogEntry = Transition(label='Catalog Entry')
SecureStorage = Transition(label='Secure Storage')

# Multidisciplinary analysis partial order: SampleExtraction -> ChemicalTesting; SampleExtraction -> ProvenanceReview; SampleExtraction -> StylisticAudit
multi_analysis = StrictPartialOrder(nodes=[SampleExtraction, ChemicalTesting, ProvenanceReview, StylisticAudit])
multi_analysis.order.add_edge(SampleExtraction, ChemicalTesting)
multi_analysis.order.add_edge(SampleExtraction, ProvenanceReview)
multi_analysis.order.add_edge(SampleExtraction, StylisticAudit)

# Imaging techniques partial order: ImagingScan -> CarbonDating -> DatabaseCrosscheck
imaging = StrictPartialOrder(nodes=[ImagingScan, CarbonDating, DatabaseCrosscheck])
imaging.order.add_edge(ImagingScan, CarbonDating)
imaging.order.add_edge(CarbonDating, DatabaseCrosscheck)

# Legal and risk checks partial order: ForgeryAnalysis -> LegalReview -> RiskAssessment
checks = StrictPartialOrder(nodes=[ForgeryAnalysis, LegalReview, RiskAssessment])
checks.order.add_edge(ForgeryAnalysis, LegalReview)
checks.order.add_edge(LegalReview, RiskAssessment)

# Final steps partial order: ReportDrafting -> CatalogEntry -> SecureStorage
final_steps = StrictPartialOrder(nodes=[ReportDrafting, CatalogEntry, SecureStorage])
final_steps.order.add_edge(ReportDrafting, CatalogEntry)
final_steps.order.add_edge(CatalogEntry, SecureStorage)

# Compose the workflow:

# Initial sequence: ArtifactReceipt -> ConditionCheck -> multi_analysis -> imaging -> checks -> ApprovalMeeting -> final_steps

root = StrictPartialOrder(
    nodes=[
        ArtifactReceipt,
        ConditionCheck,
        multi_analysis,
        imaging,
        checks,
        ApprovalMeeting,
        final_steps
    ]
)

root.order.add_edge(ArtifactReceipt, ConditionCheck)
root.order.add_edge(ConditionCheck, multi_analysis)
root.order.add_edge(multi_analysis, imaging)
root.order.add_edge(imaging, checks)
root.order.add_edge(checks, ApprovalMeeting)
root.order.add_edge(ApprovalMeeting, final_steps)