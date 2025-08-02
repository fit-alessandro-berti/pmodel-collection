# Generated from: 872d66a6-5966-4af4-a8d6-e75ccc4c473f.json
# Description: This process involves the intricate verification and validation of antique artifacts to establish provenance, authenticity, and historical significance. It begins with initial artifact intake and visual inspection, followed by scientific testing such as radiocarbon dating and material composition analysis. Experts then conduct stylistic comparisons against known historical records and previous auction results. Concurrently, archival research is performed to trace ownership lineage and contextual history. A forensic examination checks for restoration or forgery signs. Findings are compiled into a detailed report, which undergoes peer review by external historians and scientists. Finally, the artifact is either certified, cataloged for sale, or returned to its owner with recommendations for preservation or further study.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

ArtifactIntake = Transition(label='Artifact Intake')
VisualInspect = Transition(label='Visual Inspect')

RadiocarbonTest = Transition(label='Radiocarbon Test')
MaterialAnalysis = Transition(label='Material Analysis')

StylisticCompare = Transition(label='Stylistic Compare')

HistoricalResearch = Transition(label='Historical Research')
OwnershipTrace = Transition(label='Ownership Trace')

ForensicCheck = Transition(label='Forensic Check')

RestorationInspect = Transition(label='Restoration Inspect')
ForgeryDetect = Transition(label='Forgery Detect')

DataCompile = Transition(label='Data Compile')
ReportDraft = Transition(label='Report Draft')

PeerReview = Transition(label='Peer Review')

Certification = Transition(label='Certification')
CatalogEntry = Transition(label='Catalog Entry')

OwnerFeedback = Transition(label='Owner Feedback')
PreservationAdvise = Transition(label='Preservation Advise')

# Scientific testing = RadiocarbonTest and MaterialAnalysis (concurrent)
scientific_testing = StrictPartialOrder(nodes=[RadiocarbonTest, MaterialAnalysis])
# no order between them, so concurrent

# Archival research = HistoricalResearch and OwnershipTrace concurrent
archival_research = StrictPartialOrder(nodes=[HistoricalResearch, OwnershipTrace])
# no order between them, so concurrent

# Forensic examination: ForensicCheck followed by two checks in sequence RestorationInspect --> ForgeryDetect
forensic_checks = StrictPartialOrder(
    nodes=[ForensicCheck, RestorationInspect, ForgeryDetect])
forensic_checks.order.add_edge(ForensicCheck, RestorationInspect)
forensic_checks.order.add_edge(RestorationInspect, ForgeryDetect)

# Experts conduct stylistic comparisons: StylisticCompare
# (done after scientific testing)
# Both archival_research and forensic_checks run concurrently after scientific testing and stylistic compare
# So order: scientific_testing and StylisticCompare before archival_research and forensic_checks
# But the description reads: "Experts then conduct stylistic comparisons" AFTER scientific testing,
# And concurrently at the same time archival research and forensic examination.
# So stylistic compare goes with scientific testing completion, then archival research and forensic check run concurrently.

# So we build a PO for:
# scientific_testing and stylistic_compare in order [scientific_testing --> StylisticCompare]
# Then archival_research and forensic_checks concurrent, both after StylisticCompare

after_scientific = StrictPartialOrder(
    nodes=[StylisticCompare, archival_research, forensic_checks])

# Add order StylisticCompare --> archival_research and StylisticCompare --> forensic_checks

after_scientific.order.add_edge(StylisticCompare, archival_research)
after_scientific.order.add_edge(StylisticCompare, forensic_checks)

# Build scientific_test + stylistic compare PO with order:

# Combine scientific testing concurrent with order then StylisticCompare
scientific_and_stylistic = StrictPartialOrder(
    nodes=[scientific_testing, StylisticCompare])
scientific_and_stylistic.order.add_edge(scientific_testing, StylisticCompare)

# Because scientific_testing is a POWL (all transitions concurrent), so we can embed it.

# Combine all: ArtifactIntake and VisualInspect first sequentially

initial_phase = StrictPartialOrder(nodes=[ArtifactIntake, VisualInspect])
initial_phase.order.add_edge(ArtifactIntake, VisualInspect)

# Combine: initial_phase --> scientific_testing --> StylisticCompare --> (archival_research || forensic_checks)

first_big = StrictPartialOrder(
    nodes=[initial_phase, scientific_and_stylistic, archival_research, forensic_checks])

first_big.order.add_edge(initial_phase, scientific_and_stylistic)
first_big.order.add_edge(scientific_and_stylistic, archival_research)
first_big.order.add_edge(scientific_and_stylistic, forensic_checks)

# After all those, data compile and report draft sequentially

compile_phase = StrictPartialOrder(nodes=[DataCompile, ReportDraft])
compile_phase.order.add_edge(DataCompile, ReportDraft)

# Then Peer Review

# PeerReview after report draft

# So after the previous phase finishes, compile_phase, then PeerReview

review_phase = StrictPartialOrder(nodes=[compile_phase, PeerReview])
review_phase.order.add_edge(compile_phase, PeerReview)

# Then final choice: either Certification OR CatalogEntry OR (OwnerFeedback --> PreservationAdvise)

owner_preservation = StrictPartialOrder(nodes=[OwnerFeedback, PreservationAdvise])
owner_preservation.order.add_edge(OwnerFeedback, PreservationAdvise)

final_choice = OperatorPOWL(operator=Operator.XOR,
                           children=[Certification, CatalogEntry, owner_preservation])

# Combine review_phase then final_choice

end_phase = StrictPartialOrder(nodes=[review_phase, final_choice])
end_phase.order.add_edge(review_phase, final_choice)

# Finally combine entire process in order:
# first_big --> end_phase

root = StrictPartialOrder(nodes=[first_big, end_phase])
root.order.add_edge(first_big, end_phase)