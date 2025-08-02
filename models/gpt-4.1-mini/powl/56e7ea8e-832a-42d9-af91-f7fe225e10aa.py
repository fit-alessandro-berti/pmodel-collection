# Generated from: 56e7ea8e-832a-42d9-af91-f7fe225e10aa.json
# Description: This process involves the complex and meticulous evaluation of antique artifacts to verify their authenticity and provenance. It includes initial visual inspection, material analysis using advanced spectroscopy, historical research through archival records, expert consultations, and multi-layered documentation. The process must navigate legal restrictions, cultural sensitivities, and potential forgeries. Each artifact undergoes condition assessment, digital imaging, and comparison against known databases. Finally, results are compiled into a comprehensive report that supports insurance, sale, or museum acquisition decisions. The process requires interdisciplinary collaboration and can take several months to complete due to the depth of analysis and verification steps involved.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
InitialInspection = Transition(label='Initial Inspection')
MaterialAnalysis = Transition(label='Material Analysis')
HistoricalResearch = Transition(label='Historical Research')
ExpertConsult = Transition(label='Expert Consult')
LegalReview = Transition(label='Legal Review')
ConditionCheck = Transition(label='Condition Check')
DigitalImaging = Transition(label='Digital Imaging')
DatabaseCompare = Transition(label='Database Compare')
ForgeryDetection = Transition(label='Forgery Detection')
ProvenanceTrace = Transition(label='Provenance Trace')
CulturalAssessment = Transition(label='Cultural Assessment')
Documentation = Transition(label='Documentation')
InsuranceReview = Transition(label='Insurance Review')
ReportCompilation = Transition(label='Report Compilation')
FinalApproval = Transition(label='Final Approval')

# Modelling the complex process given the description

# First phase: Initial Inspection
# Follow with parallel evaluations (Material Analysis, Historical Research, Expert Consult)
initial_phase = StrictPartialOrder(
    nodes=[InitialInspection, MaterialAnalysis, HistoricalResearch, ExpertConsult]
)
# Initial Inspection precedes the parallel evaluations
initial_phase.order.add_edge(InitialInspection, MaterialAnalysis)
initial_phase.order.add_edge(InitialInspection, HistoricalResearch)
initial_phase.order.add_edge(InitialInspection, ExpertConsult)

# Material Analysis leads to Legal Review (for legal restrictions)
mat_legal = StrictPartialOrder(nodes=[MaterialAnalysis, LegalReview])
mat_legal.order.add_edge(MaterialAnalysis, LegalReview)

# Historical Research and Expert Consult feed into Cultural Assessment
hist_exp_cultural = StrictPartialOrder(
    nodes=[HistoricalResearch, ExpertConsult, CulturalAssessment]
)
hist_exp_cultural.order.add_edge(HistoricalResearch, CulturalAssessment)
hist_exp_cultural.order.add_edge(ExpertConsult, CulturalAssessment)

# Parallel join of the legal and cultural assessments before Documentation
legal_cultural = StrictPartialOrder(
    nodes=[LegalReview, CulturalAssessment]
)
# No order between them (concurrent)

# Next, condition assessment is grouped (Condition Check, Digital Imaging, Database Compare)
# These can be done in parallel
condition_assessment = StrictPartialOrder(
    nodes=[ConditionCheck, DigitalImaging, DatabaseCompare]
)
# All three concurrent

# Forgery Detection and Provenance Trace are sequential (Forgery Detection precedes Provenance Trace)
forgery_provenance = StrictPartialOrder(
    nodes=[ForgeryDetection, ProvenanceTrace]
)
forgery_provenance.order.add_edge(ForgeryDetection, ProvenanceTrace)

# Combine forgery_provenance with condition_assessment (concurrent)
cond_forgery = StrictPartialOrder(
    nodes=[condition_assessment, forgery_provenance]
)
# No direct order between them

# Documentation depends on legal and cultural (legal_cultural) AND cond_forgery
documentation_phase = StrictPartialOrder(
    nodes=[legal_cultural, cond_forgery, Documentation]
)
# legal_cultural and cond_forgery must finish before Documentation
documentation_phase.order.add_edge(legal_cultural, Documentation)
documentation_phase.order.add_edge(cond_forgery, Documentation)

# Multi-layered documentation suggests there could be looping to review Documentation if issues arise
# Model a loop: Documentation then either exit or do Insurance Review then loop back on Documentation
loop_doc = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Documentation, InsuranceReview]
)

# After Documentation/Insurance Review loop, proceed to Report Compilation and Final Approval sequentially
final_phase = StrictPartialOrder(
    nodes=[loop_doc, ReportCompilation, FinalApproval]
)
final_phase.order.add_edge(loop_doc, ReportCompilation)
final_phase.order.add_edge(ReportCompilation, FinalApproval)

# Compose the full model sequentially:
# initial_phase -> mat_legal and hist_exp_cultural -> legal_cultural -> condition and forgery phases -> documentation loop -> final phase

# Because mat_legal and hist_exp_cultural share MaterialAnalysis, HistoricalResearch, ExpertConsult from initial_phase,
# carefully combine all partial orders respecting the ordering

# Combine all phases into one StrictPartialOrder
# Nodes include:
# - initial_phase nodes: InitialInspection, MaterialAnalysis, HistoricalResearch, ExpertConsult
# - mat_legal nodes: LegalReview (MaterialAnalysis already included)
# - hist_exp_cultural nodes: CulturalAssessment (HistoricalResearch, ExpertConsult included)
# - legal_cultural nodes: none new (LegalReview, CulturalAssessment known)
# - condition_assessment: ConditionCheck, DigitalImaging, DatabaseCompare
# - forgery_provenance: ForgeryDetection, ProvenanceTrace
# - documentation loop: loop_doc (Documentation, InsuranceReview)
# - final phase: ReportCompilation, FinalApproval

all_nodes = [
    InitialInspection,
    MaterialAnalysis,
    HistoricalResearch,
    ExpertConsult,
    LegalReview,
    CulturalAssessment,
    ConditionCheck,
    DigitalImaging,
    DatabaseCompare,
    ForgeryDetection,
    ProvenanceTrace,
    Documentation,
    InsuranceReview,
    ReportCompilation,
    FinalApproval,
    loop_doc
]

root = StrictPartialOrder(nodes=all_nodes)

# initial_phase order
root.order.add_edge(InitialInspection, MaterialAnalysis)
root.order.add_edge(InitialInspection, HistoricalResearch)
root.order.add_edge(InitialInspection, ExpertConsult)

# mat_legal order
root.order.add_edge(MaterialAnalysis, LegalReview)

# hist_exp_cultural order
root.order.add_edge(HistoricalResearch, CulturalAssessment)
root.order.add_edge(ExpertConsult, CulturalAssessment)

# legal_cultural no order, LegalReview and CulturalAssessment concurrent

# condition_assessment all concurrent - no edges among ConditionCheck, DigitalImaging, DatabaseCompare

# forgery_provenance order
root.order.add_edge(ForgeryDetection, ProvenanceTrace)

# cond_forgery concurrent (condition_assessment and forgery_provenance no order)

# Both legal_cultural and cond_forgery precede Documentation (which is part of loop_doc)
# Because Documentation and InsuranceReview are inside loop_doc,
# we use loop_doc as a node representing both

root.order.add_edge(LegalReview, Documentation)
root.order.add_edge(CulturalAssessment, Documentation)

root.order.add_edge(ConditionCheck, Documentation)
root.order.add_edge(DigitalImaging, Documentation)
root.order.add_edge(DatabaseCompare, Documentation)
root.order.add_edge(ForgeryDetection, Documentation)
root.order.add_edge(ProvenanceTrace, Documentation)

# Documentation and InsuranceReview inside loop_doc handle their own order by loop operator

# Loop exit leads to ReportCompilation, then FinalApproval
root.order.add_edge(loop_doc, ReportCompilation)
root.order.add_edge(ReportCompilation, FinalApproval)