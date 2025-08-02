# Generated from: c25b7783-f083-483b-a95f-1b6c7cae2787.json
# Description: This process involves the meticulous authentication of antique artifacts for auction houses and private collectors. It begins with preliminary visual inspection followed by scientific material analysis including spectroscopy and radiocarbon dating. Experts then cross-reference the artifact's provenance with historical records and databases. If discrepancies arise, forensic imaging and microscopic surface analysis are conducted. The process also includes consultation with historians and artisans familiar with the era and style of the artifact. After comprehensive evaluation, a detailed authentication report is prepared, including possible restoration suggestions, risk assessment, and market valuation. Finally, the artifact undergoes secure packaging and certification before being released for sale or exhibition. This atypical process ensures both scientific rigor and historical accuracy, minimizing forgeries and preserving cultural heritage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
VisualInspect = Transition(label='Visual Inspect')
MaterialTest = Transition(label='Material Test')
SpectroAnalyze = Transition(label='Spectro Analyze')
RadiocarbonDate = Transition(label='Radiocarbon Date')
ProvenanceCheck = Transition(label='Provenance Check')
DatabaseSearch = Transition(label='Database Search')
DiscrepancyReview = Transition(label='Discrepancy Review')
ForensicImaging = Transition(label='Forensic Imaging')
SurfaceMicroscopy = Transition(label='Surface Microscopy')
ExpertConsult = Transition(label='Expert Consult')
HistoricalCrossref = Transition(label='Historical Crossref')
ReportDraft = Transition(label='Report Draft')
RestorationPlan = Transition(label='Restoration Plan')
RiskAssess = Transition(label='Risk Assess')
MarketValuate = Transition(label='Market Valuate')
SecurePackage = Transition(label='Secure Package')
CertificationIssue = Transition(label='Certification Issue')

# Scientific material analysis = SpectroAnalyze and RadiocarbonDate in partial order (can be parallel)
ScientificAnalysis = StrictPartialOrder(nodes=[SpectroAnalyze, RadiocarbonDate])

# Provenance and database crossreference = ProvenanceCheck --> DatabaseSearch --> HistoricalCrossref, ExpertConsult is concurrent with HistoricalCrossref
CrossReference_PO = StrictPartialOrder(
    nodes=[ProvenanceCheck, DatabaseSearch, HistoricalCrossref, ExpertConsult]
)
CrossReference_PO.order.add_edge(ProvenanceCheck, DatabaseSearch)
CrossReference_PO.order.add_edge(DatabaseSearch, HistoricalCrossref)
# ExpertConsult runs concurrent with HistoricalCrossref (no edge for concurrency)

# If discrepancy arises, forensic imaging and surface microscopy are done.
# Model discrepancy decision as XOR between skip and performing forensic+surface tests in partial order
ForensicPartialOrder = StrictPartialOrder(
    nodes=[ForensicImaging, SurfaceMicroscopy]
)
ForensicPartialOrder.order.add_edge(ForensicImaging, SurfaceMicroscopy)

DiscrepancyChoice = OperatorPOWL(operator=Operator.XOR, children=[SilentTransition(), ForensicPartialOrder])

# Full provenance and discrepancy review sequence 
# ProvenanceCheck -> DatabaseSearch -> DiscrepancyReview -> (DiscrepancyChoice) -> ExpertConsult and HistoricalCrossref
DiscrepancyReview_and_Choice_PO = StrictPartialOrder(
    nodes=[DiscrepancyReview, DiscrepancyChoice]
)
DiscrepancyReview_and_Choice_PO.order.add_edge(DiscrepancyReview, DiscrepancyChoice)

CrossReferenceFull_PO = StrictPartialOrder(
    nodes=[ProvenanceCheck, DatabaseSearch, DiscrepancyReview_and_Choice_PO, ExpertConsult, HistoricalCrossref]
)
CrossReferenceFull_PO.order.add_edge(ProvenanceCheck, DatabaseSearch)
CrossReferenceFull_PO.order.add_edge(DatabaseSearch, DiscrepancyReview_and_Choice_PO)
DiscrepancyReview_and_Choice_PO.order.add_edge(DiscrepancyReview, DiscrepancyChoice)
CrossReferenceFull_PO.order.add_edge(DiscrepancyReview_and_Choice_PO, ExpertConsult)
CrossReferenceFull_PO.order.add_edge(DiscrepancyReview_and_Choice_PO, HistoricalCrossref)
# ExpertConsult and HistoricalCrossref concurrent (no edge between them)

# MaterialTest includes the scientific material analyses (could be seen as MaterialTest overseeing SpectroAnalyze and RadiocarbonDate)
MaterialAnalysis_PO = StrictPartialOrder(
    nodes=[MaterialTest, ScientificAnalysis]
)
MaterialAnalysis_PO.order.add_edge(MaterialTest, ScientificAnalysis)

# Full flow: VisualInspect --> MaterialTest+ScientificAnalysis --> FullCrossReference --> ReportDraft partial order with restoration, risk and market valuation in partial order
ReportRelated_PO = StrictPartialOrder(
    nodes=[ReportDraft, RestorationPlan, RiskAssess, MarketValuate]
)
# All three report-related activities can be concurrent; no edges among RestorationPlan, RiskAssess, MarketValuate
ReportRelated_PO.order.add_edge(ReportDraft, RestorationPlan)
ReportRelated_PO.order.add_edge(ReportDraft, RiskAssess)
ReportRelated_PO.order.add_edge(ReportDraft, MarketValuate)

# Final packaging and certification partial order with SecurePackage --> CertificationIssue
Packaging_PO = StrictPartialOrder(
    nodes=[SecurePackage, CertificationIssue]
)
Packaging_PO.order.add_edge(SecurePackage, CertificationIssue)

# Assemble full partial order
root = StrictPartialOrder(
    nodes=[VisualInspect, MaterialAnalysis_PO, CrossReferenceFull_PO, ReportRelated_PO, Packaging_PO]
)
root.order.add_edge(VisualInspect, MaterialAnalysis_PO)
root.order.add_edge(MaterialAnalysis_PO, CrossReferenceFull_PO)
root.order.add_edge(CrossReferenceFull_PO, ReportRelated_PO)
root.order.add_edge(ReportRelated_PO, Packaging_PO)