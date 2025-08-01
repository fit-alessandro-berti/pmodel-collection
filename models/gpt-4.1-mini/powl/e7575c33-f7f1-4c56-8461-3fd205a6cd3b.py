# Generated from: e7575c33-f7f1-4c56-8461-3fd205a6cd3b.json
# Description: This process involves the detailed examination and validation of antique artifacts to verify their authenticity and provenance. It begins with initial artifact intake and cataloging, followed by expert visual inspection and advanced material analysis using spectroscopy. Historical research is conducted to trace ownership and origin, complemented by comparative stylistic evaluation with verified pieces. The process includes digital 3D scanning for condition assessment and creating a preservation plan. Legal compliance checks ensure adherence to cultural heritage laws. Finally, a comprehensive authentication report is generated and archived, with recommendations for conservation or sale preparation if applicable.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ArtifactIntake = Transition(label='Artifact Intake')
CatalogEntry = Transition(label='Catalog Entry')
VisualInspect = Transition(label='Visual Inspect')
MaterialTest = Transition(label='Material Test')
Spectroscopy = Transition(label='Spectroscopy')
HistoricalCheck = Transition(label='Historical Check')
ProvenanceTrace = Transition(label='Provenance Trace')
StyleCompare = Transition(label='Style Compare')
Scan3D = Transition(label='3D Scanning')
ConditionAssess = Transition(label='Condition Assess')
PreservationPlan = Transition(label='Preservation Plan')
LegalReview = Transition(label='Legal Review')
ReportDraft = Transition(label='Report Draft')
ReportFinalize = Transition(label='Report Finalize')
ArchiveData = Transition(label='Archive Data')
SalePrep = Transition(label='Sale Prep')

# Material analysis parallel: Material Test then Spectroscopy partial order
materialAnalysis = StrictPartialOrder(nodes=[MaterialTest, Spectroscopy])
materialAnalysis.order.add_edge(MaterialTest, Spectroscopy)

# Historical research parallel: Historical Check then Provenance Trace partial order
historicalResearch = StrictPartialOrder(nodes=[HistoricalCheck, ProvenanceTrace])
historicalResearch.order.add_edge(HistoricalCheck, ProvenanceTrace)

# Stylistic evaluation defined as Style Compare directly (single activity)

# Combine historicalResearch and Style Compare in parallel
historyAndStyle = StrictPartialOrder(nodes=[historicalResearch, StyleCompare])
# no order edges -> concurrent

# Digital scanning subprocess: 3D Scanning -> Condition Assess -> Preservation Plan (sequential)
digitalScanning = StrictPartialOrder(
    nodes=[Scan3D, ConditionAssess, PreservationPlan]
)
digitalScanning.order.add_edge(Scan3D, ConditionAssess)
digitalScanning.order.add_edge(ConditionAssess, PreservationPlan)

# Report creation sequential: Report Draft -> Report Finalize
reportCreation = StrictPartialOrder(
    nodes=[ReportDraft, ReportFinalize]
)
reportCreation.order.add_edge(ReportDraft, ReportFinalize)

# Final reporting partial order: reportCreation -> Archive Data (then choice with Sale Prep)
# Final choice: after report creation and archive data, either finish or Sale Prep

# Final block before archiving is reportCreation, then Archive Data
finalReportBlock = StrictPartialOrder(
    nodes=[reportCreation, ArchiveData]
)
finalReportBlock.order.add_edge(reportCreation, ArchiveData)

# Choice for recommendations after archiving: either silent skip or Sale Prep
# Since silent activities were not explicitly allowed here for skip, we can use a silent transition
from pm4py.objects.powl.obj import SilentTransition
skip = SilentTransition()

recommendationChoice = OperatorPOWL(operator=Operator.XOR, children=[skip, SalePrep])

# Combine finalReportBlock then recommendation choice in partial order
finalBlock = StrictPartialOrder(
    nodes=[finalReportBlock, recommendationChoice]
)
finalBlock.order.add_edge(finalReportBlock, recommendationChoice)

# After initial steps: Artifact Intake -> Catalog Entry -> Visual Inspect -> materialAnalysis and historyAndStyle parallel -> digitalScanning -> Legal Review -> finalBlock

# Parallel materialAnalysis and historyAndStyle
materialAndHistory = StrictPartialOrder(
    nodes=[materialAnalysis, historyAndStyle]
)
# Run materialAnalysis and historyAndStyle in parallel (no order edges)

# Build full process with partial orders chaining steps
root = StrictPartialOrder(
    nodes=[
        ArtifactIntake,
        CatalogEntry,
        VisualInspect,
        materialAndHistory,
        digitalScanning,
        LegalReview,
        finalBlock
    ]
)

# Define order edges according to sequence:
root.order.add_edge(ArtifactIntake, CatalogEntry)
root.order.add_edge(CatalogEntry, VisualInspect)
root.order.add_edge(VisualInspect, materialAndHistory)
root.order.add_edge(materialAndHistory, digitalScanning)
root.order.add_edge(digitalScanning, LegalReview)
root.order.add_edge(LegalReview, finalBlock)