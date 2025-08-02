# Generated from: cbc2fe47-5242-461d-99bf-57635fdccdab.json
# Description: This process involves a detailed and atypical workflow used by museums and private collectors to authenticate rare historical artifacts. It integrates multidisciplinary expertise including provenance research, scientific analysis, and expert panel reviews. The process begins with initial artifact intake and documentation, followed by layered provenance verification involving archival searches and previous ownership validation. Scientific testing such as radiocarbon dating, spectroscopy, and material composition analysis is then conducted to identify anachronisms or forgeries. Concurrently, a panel of historians and art experts assess the stylistic and contextual authenticity. The findings are compiled into a comprehensive authentication report, which then undergoes a final quality review. If authenticated, the artifact is cataloged and insured; otherwise, recommendations for further investigation or rejection are made. The workflow also includes secure data archiving and periodic re-evaluation triggered by new research or technological advancements, ensuring ongoing verification integrity over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ArtifactIntake = Transition(label='Artifact Intake')
DocumentCheck = Transition(label='Document Check')

ProvenanceSearch = Transition(label='Provenance Search')
OwnershipValidate = Transition(label='Ownership Validate')

RadiocarbonTest = Transition(label='Radiocarbon Test')
SpectroscopyScan = Transition(label='Spectroscopy Scan')
MaterialAnalysis = Transition(label='Material Analysis')

StyleAssessment = Transition(label='Style Assessment')
ContextReview = Transition(label='Context Review')
ExpertPanel = Transition(label='Expert Panel')

ReportDraft = Transition(label='Report Draft')
QualityReview = Transition(label='Quality Review')

CatalogEntry = Transition(label='Catalog Entry')
InsuranceSetup = Transition(label='Insurance Setup')

ArchiveData = Transition(label='Archive Data')
ReevaluationTrigger = Transition(label='Reevaluation Trigger')

# Layered provenance verification: ProvenanceSearch then OwnershipValidate (partial order with order edge)
ProvenanceVerification = StrictPartialOrder(
    nodes=[ProvenanceSearch, OwnershipValidate],
)
ProvenanceVerification.order.add_edge(ProvenanceSearch, OwnershipValidate)

# Scientific Testing: RadiocarbonTest, SpectroscopyScan, MaterialAnalysis in parallel (no edges)
ScientificTesting = StrictPartialOrder(
    nodes=[RadiocarbonTest, SpectroscopyScan, MaterialAnalysis],
    # no order edges since concurrent
)

# Panel assessment: StyleAssessment, ContextReview then ExpertPanel depends on both
PanelAssessment = StrictPartialOrder(
    nodes=[StyleAssessment, ContextReview, ExpertPanel],
)
PanelAssessment.order.add_edge(StyleAssessment, ExpertPanel)
PanelAssessment.order.add_edge(ContextReview, ExpertPanel)

# Concurrent ScientificTesting and PanelAssessment
TestingAndAssessment = StrictPartialOrder(
    nodes=[ScientificTesting, PanelAssessment],
    # no edges between ScientificTesting and PanelAssessment -> concurrent
)

# Authentication report: ReportDraft after TestingAndAssessment (partial order with order edges)
AfterTestingAndAssessment = StrictPartialOrder(
    nodes=[TestingAndAssessment, ReportDraft],
)
AfterTestingAndAssessment.order.add_edge(TestingAndAssessment, ReportDraft)

# Final quality review after report draft
ReportAndReview = StrictPartialOrder(
    nodes=[AfterTestingAndAssessment, QualityReview],
)
ReportAndReview.order.add_edge(AfterTestingAndAssessment, QualityReview)

# Choice after QualityReview: either catalog+insurance or recommendations (modeled by XOR)
CatalogAndInsurance = StrictPartialOrder(
    nodes=[CatalogEntry, InsuranceSetup],
)
CatalogAndInsurance.order.add_edge(CatalogEntry, InsuranceSetup)

Recommendations = SilentTransition()  # recommendations modeled as silent transition (for simplicity)

PostReviewChoice = OperatorPOWL(operator=Operator.XOR, children=[CatalogAndInsurance, Recommendations])

# Secure Data Archiving and Periodic Re-evaluation run concurrently with the main flow
# ArchiveData and ReevaluationTrigger concurrent nodes (could be loosely linked later)
ArchiveAndReevaluation = StrictPartialOrder(
    nodes=[ArchiveData, ReevaluationTrigger],
    # no edges, concurrent
)

# Start: Artifact Intake then Document Check
Start = StrictPartialOrder(
    nodes=[ArtifactIntake, DocumentCheck],
)
Start.order.add_edge(ArtifactIntake, DocumentCheck)

# Provenance Verification after Document Check
StartToProvenance = StrictPartialOrder(
    nodes=[Start, ProvenanceVerification],
)
StartToProvenance.order.add_edge(Start, ProvenanceVerification)

# Main chain: Provenance Verification -> Testing and Assessment -> Report and Review -> Choice
MainChain = StrictPartialOrder(
    nodes=[StartToProvenance, TestingAndAssessment, ReportDraft, QualityReview, PostReviewChoice],
)
MainChain.order.add_edge(StartToProvenance, TestingAndAssessment)
MainChain.order.add_edge(TestingAndAssessment, ReportDraft)
MainChain.order.add_edge(ReportDraft, QualityReview)
MainChain.order.add_edge(QualityReview, PostReviewChoice)

# Instead of duplicating ReportDraft and QualityReview in MainChain, let's link consistent objects:
# We already defined AfterTestingAndAssessment and ReportAndReview, so reuse them correctly:

# Let's rebuild the main chain respecting the data flow exactly:

# Step1: StartToProvenance
# Step2: ProvenanceVerification (already in StartToProvenance)
# Step3: TestingAndAssessment
# Step4: ReportDraft (already in AfterTestingAndAssessment)
# Step5: QualityReview (already in ReportAndReview)
# Step6: PostReviewChoice

# Redefine the main flow with all parts correctly linked in StrictPartialOrder:

# Actually better to combine all steps piecewise now:

# Main partial order with nodes and edges:
nodes_main = [
    Start,
    ProvenanceVerification,
    TestingAndAssessment,
    ReportDraft,
    QualityReview,
    PostReviewChoice,
    ArchiveData,
    ReevaluationTrigger,
]

root = StrictPartialOrder(nodes=nodes_main)
# Define order edges for sequential dependencies
root.order.add_edge(Start, ProvenanceVerification)
root.order.add_edge(ProvenanceVerification, TestingAndAssessment)
root.order.add_edge(TestingAndAssessment, ReportDraft)
root.order.add_edge(ReportDraft, QualityReview)
root.order.add_edge(QualityReview, PostReviewChoice)
# ArchiveData and ReevaluationTrigger are concurrent with main flow, so no edges connected to them

# The above covers the full process with concurrency and choice
