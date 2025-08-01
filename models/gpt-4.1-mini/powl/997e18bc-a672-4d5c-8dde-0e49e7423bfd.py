# Generated from: 997e18bc-a672-4d5c-8dde-0e49e7423bfd.json
# Description: This process governs the authentication and provenance verification of unique cultural artifacts submitted by private collectors for museum acquisition. It involves multi-stage verification including material analysis, historical record cross-referencing, expert consensus gathering, and provenance chain validation. The process incorporates both physical testing and digital archival research, ensuring that the artifact's origin, authenticity, and ownership history are rigorously confirmed before acceptance. It also manages risk assessment for potential forgery and coordinates legal compliance with cultural heritage laws, concluding with a final authentication report and decision.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
ArtifactIntake = Transition(label='Artifact Intake')
MaterialSampling = Transition(label='Material Sampling')
ChemicalTesting = Transition(label='Chemical Testing')
PhotographicSurvey = Transition(label='Photographic Survey')
ArchiveSearch = Transition(label='Archive Search')
ProvenanceCheck = Transition(label='Provenance Check')
ExpertPanel = Transition(label='Expert Panel')
ForgeryAnalysis = Transition(label='Forgery Analysis')
LegalReview = Transition(label='Legal Review')
RiskScoring = Transition(label='Risk Scoring')
DatabaseUpdate = Transition(label='Database Update')
OwnerInterview = Transition(label='Owner Interview')
ReportDrafting = Transition(label='Report Drafting')
FinalReview = Transition(label='Final Review')
DecisionIssuance = Transition(label='Decision Issuance')
RecordArchival = Transition(label='Record Archival')

# Define parts of the process:

# Physical testing branch: Material Sampling -> Chemical Testing + Photographic Survey (concurrent)
physical_tests = StrictPartialOrder(nodes=[MaterialSampling, ChemicalTesting, PhotographicSurvey])
physical_tests.order.add_edge(MaterialSampling, ChemicalTesting)
physical_tests.order.add_edge(MaterialSampling, PhotographicSurvey)
# Chemical Testing and Photographic Survey are concurrent after Material Sampling

# Digital archival research: Archive Search -> Provenance Check (sequence)
digital_research = StrictPartialOrder(nodes=[ArchiveSearch, ProvenanceCheck])
digital_research.order.add_edge(ArchiveSearch, ProvenanceCheck)

# Expert consensus: Expert Panel
expert_consensus = ExpertPanel

# Risk assessment: Forger Analysis and Risk Scoring concurrent
risk_assessment = StrictPartialOrder(nodes=[ForgeryAnalysis, RiskScoring])
# no edges => concurrent

# Legal compliance: Legal Review
legal_compliance = LegalReview

# Owner Interview (can be done in parallel with legal or risk?)
# We'll put Owner Interview concurrent with legal and risk for coverage before report

# Group Risk, Legal, and Owner Interview concurrently
risk_legal_owner = StrictPartialOrder(nodes=[risk_assessment, legal_compliance, OwnerInterview])
risk_legal_owner.order.add_edge(risk_assessment, legal_compliance)  # let's assume risk before legal
# OwnerInterview concurrent with both (no edges)

# Merge all verification phases that must happen after Artifact Intake:
# 1) physical_tests
# 2) digital_research
# 3) expert_consensus
# 4) risk_legal_owner

verification_phase = StrictPartialOrder(
    nodes=[physical_tests, digital_research, expert_consensus, risk_legal_owner]
)
verification_phase.order.add_edge(physical_tests, digital_research)
verification_phase.order.add_edge(physical_tests, expert_consensus)
verification_phase.order.add_edge(physical_tests, risk_legal_owner)
# digital_research, expert_consensus, risk_legal_owner after physical_tests, concurrent otherwise

# Database update can happen after expert consensus & risk_legal_owner (assuming data updated after these)
db_update_pre = StrictPartialOrder(nodes=[expert_consensus, risk_legal_owner, DatabaseUpdate])
db_update_pre.order.add_edge(expert_consensus, DatabaseUpdate)
db_update_pre.order.add_edge(risk_legal_owner, DatabaseUpdate)

# To keep structure consistent, we'll make verification_phase to include physical_tests followed by
# digital_research, expert_consensus, risk_legal_owner
# Then db_update after expert_consensus, risk_legal_owner

# We'll combine all as:
verification_and_update = StrictPartialOrder(
    nodes=[physical_tests, digital_research, db_update_pre]
)
verification_and_update.order.add_edge(physical_tests, digital_research)
verification_and_update.order.add_edge(digital_research, db_update_pre)
# note db_update_pre contains expert_consensus, risk_legal_owner, DatabaseUpdate
# so the edges inside db_update_pre hold those relations

# Report drafting and final review before decision issuance
# Sequence: Report Drafting -> Final Review -> Decision Issuance
reporting = StrictPartialOrder(nodes=[ReportDrafting, FinalReview, DecisionIssuance])
reporting.order.add_edge(ReportDrafting, FinalReview)
reporting.order.add_edge(FinalReview, DecisionIssuance)

# Record Archival after Decision Issuance
final_phase = StrictPartialOrder(nodes=[reporting, RecordArchival])
final_phase.order.add_edge(reporting, RecordArchival)

# Full process: Artifact Intake -> verification_and_update -> final_phase
root = StrictPartialOrder(
    nodes=[ArtifactIntake, verification_and_update, final_phase]
)
root.order.add_edge(ArtifactIntake, verification_and_update)
root.order.add_edge(verification_and_update, final_phase)