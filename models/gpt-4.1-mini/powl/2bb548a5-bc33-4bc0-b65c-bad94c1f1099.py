# Generated from: 2bb548a5-bc33-4bc0-b65c-bad94c1f1099.json
# Description: This process outlines the comprehensive workflow for authenticating rare historical artifacts prior to acquisition by a museum or collector. It involves multidisciplinary evaluation including provenance verification, scientific analysis, expert consultation, and legal clearance. The process begins with initial artifact intake, followed by detailed condition assessment and documentation. Next, provenance research is conducted through archival searches and ownership history tracing. Scientific analysis employs various techniques such as radiocarbon dating, spectroscopy, and material composition tests to confirm period authenticity. Parallel to these, expert appraisals are collected from historians, archaeologists, and cultural specialists to validate findings. Legal teams then perform due diligence to ensure no ownership disputes or export restrictions apply. The final phase includes consolidation of all findings into a comprehensive authentication report, review by senior curators, and decision-making regarding acquisition or rejection. This atypical process ensures rigorous validation to mitigate risks related to forgery, misattribution, and legal complications, preserving institutional integrity and cultural heritage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ArtifactIntake = Transition(label='Artifact Intake')

ConditionCheck = Transition(label='Condition Check')
PhotoDocumentation = Transition(label='Photo Documentation')

ProvenanceSearch = Transition(label='Provenance Search')
ArchiveReview = Transition(label='Archive Review')
OwnershipTrace = Transition(label='Ownership Trace')

RadiocarbonTest = Transition(label='Radiocarbon Test')
SpectroscopyScan = Transition(label='Spectroscopy Scan')
MaterialAnalysis = Transition(label='Material Analysis')

ExpertConsult = Transition(label='Expert Consult')
AppraisalCollection = Transition(label='Appraisal Collection')

LegalReview = Transition(label='Legal Review')
ExportCheck = Transition(label='Export Check')

ReportCompilation = Transition(label='Report Compilation')
CuratorReview = Transition(label='Curator Review')
FinalDecision = Transition(label='Final Decision')

# Partial order for Provenance Search branch: ArchiveReview --> OwnershipTrace --> ProvenanceSearch
# Note: Provenance Search is described as "conducted through archival searches and ownership history tracing"
# So "Provenance Search" is after ArchiveReview and OwnershipTrace. We put ProvenanceSearch last in this branch.
provenance_po = StrictPartialOrder(nodes=[ArchiveReview, OwnershipTrace, ProvenanceSearch])
provenance_po.order.add_edge(ArchiveReview, OwnershipTrace)
provenance_po.order.add_edge(OwnershipTrace, ProvenanceSearch)

# Partial order for Scientific Analysis branch: RadiocarbonTest, SpectroscopyScan, MaterialAnalysis are concurrent
scientific_po = StrictPartialOrder(nodes=[RadiocarbonTest, SpectroscopyScan, MaterialAnalysis])

# Partial order for Expert Appraisal branch: ExpertConsult --> AppraisalCollection
expert_po = StrictPartialOrder(nodes=[ExpertConsult, AppraisalCollection])
expert_po.order.add_edge(ExpertConsult, AppraisalCollection)

# Partial order for Legal Review branch: LegalReview --> ExportCheck
legal_po = StrictPartialOrder(nodes=[LegalReview, ExportCheck])
legal_po.order.add_edge(LegalReview, ExportCheck)

# Parallel join of 4 branches after initial steps:
# ProvenanceSearch, Scientific Analysis, Expert Appraisal, Legal Review
# These four are concurrent (no order edges)
parallel_branches = StrictPartialOrder(
    nodes=[provenance_po, scientific_po, expert_po, legal_po]
)
# No edges between these: all parallel

# Initial steps ConditionCheck and PhotoDocumentation happen after ArtifactIntake sequentially
initial_po = StrictPartialOrder(nodes=[ArtifactIntake, ConditionCheck, PhotoDocumentation])
initial_po.order.add_edge(ArtifactIntake, ConditionCheck)
initial_po.order.add_edge(ConditionCheck, PhotoDocumentation)

# After the parallel branches finish, a partial order with:
# ReportCompilation --> CuratorReview --> FinalDecision
final_po = StrictPartialOrder(nodes=[ReportCompilation, CuratorReview, FinalDecision])
final_po.order.add_edge(ReportCompilation, CuratorReview)
final_po.order.add_edge(CuratorReview, FinalDecision)

# Now, integrate all steps in order:
# After initial_po ends (PhotoDocumentation), then the parallel_branches can start
# Finally, after parallel_branches, final_po starts

root = StrictPartialOrder(
    nodes=[initial_po, parallel_branches, final_po]
)
root.order.add_edge(initial_po, parallel_branches)
root.order.add_edge(parallel_branches, final_po)