# Generated from: ab399c8c-a391-4ef7-99c5-558691184609.json
# Description: This process involves the detailed examination and verification of antique artifacts to establish their authenticity and provenance. It starts with initial artifact intake and visual inspection, followed by multi-disciplinary scientific testing including radiocarbon dating, material composition analysis, and microscopic surface evaluation. Expert consultations with historians and art conservators are incorporated to cross-reference historical records and stylistic attributes. Documentation is meticulously prepared, and legal provenance is verified through archival research. The process concludes with an authentication report and recommendations for preservation or restoration, ensuring the artifact's historical integrity is maintained while enabling confident acquisition or exhibition decisions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ArtifactIntake = Transition(label='Artifact Intake')
VisualInspect = Transition(label='Visual Inspect')

RadiocarbonTest = Transition(label='Radiocarbon Test')
MaterialAnalysis = Transition(label='Material Analysis')
SurfaceMicroscopy = Transition(label='Surface Microscopy')

HistoricalReview = Transition(label='Historical Review')
ProvenanceCheck = Transition(label='Provenance Check')

ExpertConsult = Transition(label='Expert Consult')
StylisticCompare = Transition(label='Stylistic Compare')

ArchivalResearch = Transition(label='Archival Research')

ConditionReport = Transition(label='Condition Report')
LegalVerification = Transition(label='Legal Verification')

AuthenticationDraft = Transition(label='Authentication Draft')
PreservationPlan = Transition(label='Preservation Plan')
FinalReport = Transition(label='Final Report')

# Scientific testing partial order (RadiocarbonTest, MaterialAnalysis, SurfaceMicroscopy) concurrent
science_tests = StrictPartialOrder(nodes=[RadiocarbonTest, MaterialAnalysis, SurfaceMicroscopy])
# No order between them, fully concurrent

# Expert consultations partial order (HistoricalReview, ProvenanceCheck, ExpertConsult, StylisticCompare)
expert_consultations = StrictPartialOrder(nodes=[HistoricalReview, ProvenanceCheck, ExpertConsult, StylisticCompare])
# Order: HistoricalReview --> ExpertConsult and StylisticCompare
#        ProvenanceCheck --> ExpertConsult and StylisticCompare
expert_consultations.order.add_edge(HistoricalReview, ExpertConsult)
expert_consultations.order.add_edge(ProvenanceCheck, ExpertConsult)
expert_consultations.order.add_edge(HistoricalReview, StylisticCompare)
expert_consultations.order.add_edge(ProvenanceCheck, StylisticCompare)

# Legal provenance verification partial order (ArchivalResearch)
# It appears ArchivalResearch is single activity, just use directly

# Documentation partial order (ConditionReport, LegalVerification)
documentation = StrictPartialOrder(nodes=[ConditionReport, LegalVerification])
# LegalVerification depends on ArchivalResearch
# So we'll handle archiving first

# Compose the flow:

# Start partial order: ArtifactIntake --> VisualInspect --> science_tests --> expert_consultations
# We have a partial order linking these parts:

# First partial order: Artifact Intake --> Visual Inspect
start = StrictPartialOrder(nodes=[ArtifactIntake, VisualInspect])
start.order.add_edge(ArtifactIntake, VisualInspect)

# Then Visual Inspect --> science_tests
start_science = StrictPartialOrder(nodes=[start, science_tests])
start_science.order.add_edge(start, science_tests)

# Then science_tests --> expert_consultations
science_expert = StrictPartialOrder(nodes=[science_tests, expert_consultations])
science_expert.order.add_edge(science_tests, expert_consultations)

# Then expert_consultations --> ArchivalResearch
expert_archival = StrictPartialOrder(nodes=[expert_consultations, ArchivalResearch])
expert_archival.order.add_edge(expert_consultations, ArchivalResearch)

# Documentation includes ConditionReport (which depends on expert_consultations and archivalResearch)
# and LegalVerification which depends on ArchivalResearch

# ConditionReport depends on expert_consultations and archivalResearch (both)
doc_nodes = [ConditionReport, LegalVerification]
documentation = StrictPartialOrder(nodes=doc_nodes)
documentation.order.add_edge(ConditionReport, LegalVerification)  # LegalVerification after ConditionReport

# We add edges expert_consultations --> ConditionReport and ArchivalResearch --> ConditionReport
doc_start = StrictPartialOrder(nodes=[expert_consultations, ArchivalResearch, ConditionReport])
doc_start.order.add_edge(expert_consultations, ConditionReport)
doc_start.order.add_edge(ArchivalResearch, ConditionReport)

# Then ConditionReport --> LegalVerification
doc_with_legal = StrictPartialOrder(nodes=[doc_start, LegalVerification])
doc_with_legal.order.add_edge(doc_start, LegalVerification)

# Now combine all to: up to expert_consultations/archivalResearch, then documentation
all_before_doc = StrictPartialOrder(nodes=[science_tests, expert_consultations, ArchivalResearch])
all_before_doc.order.add_edge(science_tests, expert_consultations)
all_before_doc.order.add_edge(expert_consultations, ArchivalResearch)

# Combine start and all_before_doc
start_to_all = StrictPartialOrder(nodes=[start, science_tests, expert_consultations, ArchivalResearch])
start_to_all.order.add_edge(start, science_tests)
start_to_all.order.add_edge(science_tests, expert_consultations)
start_to_all.order.add_edge(expert_consultations, ArchivalResearch)

# To avoid duplications, unify the previous orderings to a single chain:

root_pre_doc = StrictPartialOrder(
    nodes=[ArtifactIntake, VisualInspect, RadiocarbonTest, MaterialAnalysis, SurfaceMicroscopy,
           HistoricalReview, ProvenanceCheck, ExpertConsult, StylisticCompare, ArchivalResearch]
)

# Orders:
# Artifact Intake --> Visual Inspect
root_pre_doc.order.add_edge(ArtifactIntake, VisualInspect)

# Visual Inspect --> all science_tests (which are concurrent)
root_pre_doc.order.add_edge(VisualInspect, RadiocarbonTest)
root_pre_doc.order.add_edge(VisualInspect, MaterialAnalysis)
root_pre_doc.order.add_edge(VisualInspect, SurfaceMicroscopy)

# Science tests all --> HistoricalReview, ProvenanceCheck (start of expert consultations)
root_pre_doc.order.add_edge(RadiocarbonTest, HistoricalReview)
root_pre_doc.order.add_edge(MaterialAnalysis, HistoricalReview)
root_pre_doc.order.add_edge(SurfaceMicroscopy, HistoricalReview)
root_pre_doc.order.add_edge(RadiocarbonTest, ProvenanceCheck)
root_pre_doc.order.add_edge(MaterialAnalysis, ProvenanceCheck)
root_pre_doc.order.add_edge(SurfaceMicroscopy, ProvenanceCheck)

# HistoricalReview and ProvenanceCheck --> ExpertConsult and StylisticCompare
root_pre_doc.order.add_edge(HistoricalReview, ExpertConsult)
root_pre_doc.order.add_edge(ProvenanceCheck, ExpertConsult)
root_pre_doc.order.add_edge(HistoricalReview, StylisticCompare)
root_pre_doc.order.add_edge(ProvenanceCheck, StylisticCompare)

# ExpertConsult and StylisticCompare --> ArchivalResearch
root_pre_doc.order.add_edge(ExpertConsult, ArchivalResearch)
root_pre_doc.order.add_edge(StylisticCompare, ArchivalResearch)

# Now Documentation partial order:
# ArchivalResearch --> ConditionReport --> LegalVerification
documentation = StrictPartialOrder(nodes=[ArchivalResearch, ConditionReport, LegalVerification])
documentation.order.add_edge(ArchivalResearch, ConditionReport)
documentation.order.add_edge(ConditionReport, LegalVerification)

# Final steps partial order: AuthenticationDraft, PreservationPlan, FinalReport
# They appear sequential
final_steps = StrictPartialOrder(nodes=[AuthenticationDraft, PreservationPlan, FinalReport])
final_steps.order.add_edge(AuthenticationDraft, PreservationPlan)
final_steps.order.add_edge(PreservationPlan, FinalReport)

# Combine all partial orders into a final single root partial order:
root = StrictPartialOrder(
    nodes=[root_pre_doc, documentation, final_steps]
)
# root_pre_doc --> documentation --> final_steps
root.order.add_edge(root_pre_doc, documentation)
root.order.add_edge(documentation, final_steps)