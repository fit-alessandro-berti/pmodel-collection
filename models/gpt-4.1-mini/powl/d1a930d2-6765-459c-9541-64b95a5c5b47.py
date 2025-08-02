# Generated from: d1a930d2-6765-459c-9541-64b95a5c5b47.json
# Description: This process involves the detailed verification and authentication of antique artifacts sourced from various international locations. It combines historical research, scientific analysis, provenance validation, and expert consultation. The process begins with initial artifact intake, followed by condition assessment, material testing, stylistic comparison, and carbon dating. Parallelly, provenance documents are scrutinized for legitimacy, and digital imaging techniques are applied to detect restorations or forgeries. The findings are reviewed by a panel of historians and conservators, culminating in a comprehensive authentication report. This rigorous approach ensures the artifact's authenticity is confirmed beyond reasonable doubt before it is cataloged or auctioned.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ArtifactIntake = Transition(label='Artifact Intake')
ConditionCheck = Transition(label='Condition Check')
MaterialTest = Transition(label='Material Test')
StyleCompare = Transition(label='Style Compare')
CarbonDating = Transition(label='Carbon Dating')
DocumentReview = Transition(label='Document Review')
ProvenanceCheck = Transition(label='Provenance Check')
DigitalImaging = Transition(label='Digital Imaging')
ForgeryScan = Transition(label='Forgery Scan')
ExpertConsult = Transition(label='Expert Consult')
HistoricalResearch = Transition(label='Historical Research')
PanelReview = Transition(label='Panel Review')
ReportDraft = Transition(label='Report Draft')
FinalApproval = Transition(label='Final Approval')
CatalogEntry = Transition(label='Catalog Entry')

# Historical research and expert consult probably parallel
# The process:

# initial artifact intake
# followed by condition assessment, material testing, stylistic comparison, and carbon dating (ordered)
# parallel to provenance documents scrutiny branch: document review -> provenance check
# and digital imaging branch: digital imaging -> forgery scan

# After these parallel branches, findings reviewed by panel (panel review)
# panel review then leads to report draft -> final approval -> catalog entry

# Build the linear branch after artifact intake
artifact_branch = StrictPartialOrder(
    nodes=[ConditionCheck, MaterialTest, StyleCompare, CarbonDating]
)
artifact_branch.order.add_edge(ConditionCheck, MaterialTest)
artifact_branch.order.add_edge(MaterialTest, StyleCompare)
artifact_branch.order.add_edge(StyleCompare, CarbonDating)

# Build provenance branch (document review -> provenance check)
provenance_branch = StrictPartialOrder(
    nodes=[DocumentReview, ProvenanceCheck]
)
provenance_branch.order.add_edge(DocumentReview, ProvenanceCheck)

# Build imaging branch (digital imaging -> forgery scan)
imaging_branch = StrictPartialOrder(
    nodes=[DigitalImaging, ForgeryScan]
)
imaging_branch.order.add_edge(DigitalImaging, ForgeryScan)

# Combine provenance and imaging in partial order (concurrent)
prov_imaging = StrictPartialOrder(
    nodes=[provenance_branch, imaging_branch]
)

# panel review waits for all these to complete: artifact_branch, prov_imaging, HistoricalResearch and ExpertConsult
# HistoricalResearch and ExpertConsult run concurrently
hist_expert = StrictPartialOrder(
    nodes=[HistoricalResearch, ExpertConsult]
)

# combine all parallel branches after artifact intake
parallel_after_intake = StrictPartialOrder(
    nodes=[artifact_branch, prov_imaging, hist_expert]
)

# Overall partial order:
# Artifact Intake --> parallel branches --> Panel Review --> Report Draft --> Final Approval --> Catalog Entry

root = StrictPartialOrder(
    nodes=[ArtifactIntake, parallel_after_intake, PanelReview, ReportDraft, FinalApproval, CatalogEntry]
)

# artifact intake before parallel branches
root.order.add_edge(ArtifactIntake, parallel_after_intake)
# all parallel branches before panel review
root.order.add_edge(parallel_after_intake, PanelReview)
# sequential order after panel review
root.order.add_edge(PanelReview, ReportDraft)
root.order.add_edge(ReportDraft, FinalApproval)
root.order.add_edge(FinalApproval, CatalogEntry)