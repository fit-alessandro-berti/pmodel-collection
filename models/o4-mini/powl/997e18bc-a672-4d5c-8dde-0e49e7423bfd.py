# Generated from: 997e18bc-a672-4d5c-8dde-0e49e7423bfd.json
# Description: This process governs the authentication and provenance verification of unique cultural artifacts submitted by private collectors for museum acquisition. It involves multi-stage verification including material analysis, historical record cross-referencing, expert consensus gathering, and provenance chain validation. The process incorporates both physical testing and digital archival research, ensuring that the artifact's origin, authenticity, and ownership history are rigorously confirmed before acceptance. It also manages risk assessment for potential forgery and coordinates legal compliance with cultural heritage laws, concluding with a final authentication report and decision.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
intake = Transition(label='Artifact Intake')
material_sampling = Transition(label='Material Sampling')
chemical_testing = Transition(label='Chemical Testing')
photographic_survey = Transition(label='Photographic Survey')
owner_interview = Transition(label='Owner Interview')
archive_search = Transition(label='Archive Search')
provenance_check = Transition(label='Provenance Check')
expert_panel = Transition(label='Expert Panel')
forgery_analysis = Transition(label='Forgery Analysis')
risk_scoring = Transition(label='Risk Scoring')
legal_review = Transition(label='Legal Review')
report_drafting = Transition(label='Report Drafting')
final_review = Transition(label='Final Review')
decision_issuance = Transition(label='Decision Issuance')
db_update = Transition(label='Database Update')
record_archival = Transition(label='Record Archival')

# Physical testing subprocess: Sampling -> {Chemical Testing, Photographic Survey}
physical_testing = StrictPartialOrder(
    nodes=[material_sampling, chemical_testing, photographic_survey]
)
physical_testing.order.add_edge(material_sampling, chemical_testing)
physical_testing.order.add_edge(material_sampling, photographic_survey)

# Archival research subprocess: Owner Interview -> Archive Search -> Provenance Check
archival_research = StrictPartialOrder(
    nodes=[owner_interview, archive_search, provenance_check]
)
archival_research.order.add_edge(owner_interview, archive_search)
archival_research.order.add_edge(archive_search, provenance_check)

# Forgery & risk subprocess: Analysis -> Scoring
forgery_path = StrictPartialOrder(nodes=[forgery_analysis, risk_scoring])
forgery_path.order.add_edge(forgery_analysis, risk_scoring)

# Root workflow
root = StrictPartialOrder(nodes=[
    intake,
    physical_testing,
    archival_research,
    expert_panel,
    forgery_path,
    legal_review,
    report_drafting,
    final_review,
    decision_issuance,
    db_update,
    record_archival
])

# Define the control-flow partial order
# 1) Intake precedes both testing and research
root.order.add_edge(intake, physical_testing)
root.order.add_edge(intake, archival_research)

# 2) Both subprocesses must finish before Expert Panel, Forgery/Risk and Legal Review
for nxt in [expert_panel, forgery_path, legal_review]:
    root.order.add_edge(physical_testing, nxt)
    root.order.add_edge(archival_research, nxt)

# 3) After those three, draft the report
for src in [expert_panel, forgery_path, legal_review]:
    root.order.add_edge(src, report_drafting)

# 4) Sequence: Report Drafting -> Final Review -> Decision Issuance
root.order.add_edge(report_drafting, final_review)
root.order.add_edge(final_review, decision_issuance)

# 5) After decision, update database and archive record (concurrent)
root.order.add_edge(decision_issuance, db_update)
root.order.add_edge(decision_issuance, record_archival)