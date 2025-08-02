# Generated from: f707c6be-c839-4f52-acd4-7d36c01dc85a.json
# Description: This process involves the verification and authentication of ancient artifacts using a combination of forensic analysis, historical research, and advanced imaging technologies. The process starts with initial artifact intake and condition assessment, followed by multi-spectral scanning and material composition testing. Experts cross-reference findings with historical databases and provenance records to identify inconsistencies or confirm authenticity. Additionally, the process includes collaboration with external historians and laboratories, legal documentation preparation, and final certification. The authentication process ensures the artifact's legitimacy for museums, collectors, and auction houses, reducing the risk of forgeries entering the market while preserving cultural heritage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ArtifactIntake = Transition(label='Artifact Intake')
ConditionCheck = Transition(label='Condition Check')
MultiSpectralScan = Transition(label='Multi-spectral Scan')
MaterialTest = Transition(label='Material Test')
DatabaseMatch = Transition(label='Database Match')
ProvenanceCheck = Transition(label='Provenance Check')
ExpertReview = Transition(label='Expert Review')
HistoricalQuery = Transition(label='Historical Query')
LabCollaboration = Transition(label='Lab Collaboration')
ImagingAnalysis = Transition(label='Imaging Analysis')
ForgeryDetection = Transition(label='Forgery Detection')
LegalDrafting = Transition(label='Legal Drafting')
CertificationIssue = Transition(label='Certification Issue')
ClientBriefing = Transition(label='Client Briefing')
ArchivalUpdate = Transition(label='Archival Update')

# Build partial orders to capture dependencies and concurrency:
# 1) Intake and condition check sequential
# 2) Then concurrent scans and tests: MultiSpectralScan and MaterialTest
# 3) Then expert analysis phase, which has parallel but partially ordered activities:
#    - DatabaseMatch and ProvenanceCheck run concurrently
#    - ExpertReview depends on both above
#    - HistoricalQuery is triggered concurrently and feeds into ExpertReview
#    - LabCollaboration and ImagingAnalysis concurrent with above but feed into ForgeryDetection
# 4) ForgeryDetection depends on ExpertReview, LabCollaboration and ImagingAnalysis
# 5) Then legal drafting, certification issue, client briefing, and archival update sequentially

# First phase: Artifact Intake -> Condition Check
phase1 = StrictPartialOrder(nodes=[ArtifactIntake, ConditionCheck])
phase1.order.add_edge(ArtifactIntake, ConditionCheck)

# Second phase: scans and tests concurrent after Condition Check
phase2 = StrictPartialOrder(nodes=[MultiSpectralScan, MaterialTest])
# No order edges between scans/tests (concurrent)

# Third phase: expert analysis and detection
# DatabaseMatch and ProvenanceCheck concurrent
db_prov = StrictPartialOrder(nodes=[DatabaseMatch, ProvenanceCheck])
# HistoricalQuery runs concurrently, no ordering edges with db_prov
# ExpertReview depends on DatabaseMatch, ProvenanceCheck, HistoricalQuery
expert_analysis = StrictPartialOrder(nodes=[db_prov, HistoricalQuery, ExpertReview])
# Add edges: db_prov --> ExpertReview, HistoricalQuery --> ExpertReview
expert_analysis.order.add_edge(db_prov, ExpertReview)
expert_analysis.order.add_edge(HistoricalQuery, ExpertReview)

# LabCollaboration and ImagingAnalysis concurrent, both precede ForgeryDetection
lab_imaging = StrictPartialOrder(nodes=[LabCollaboration, ImagingAnalysis])
# ForgeryDetection depends on expert_analysis and lab_imaging
detection_phase = StrictPartialOrder(nodes=[expert_analysis, lab_imaging, ForgeryDetection])
detection_phase.order.add_edge(expert_analysis, ForgeryDetection)
detection_phase.order.add_edge(lab_imaging, ForgeryDetection)

# Final phase: legal drafting -> certification issue -> client briefing -> archival update
final_phase = StrictPartialOrder(nodes=[LegalDrafting, CertificationIssue, ClientBriefing, ArchivalUpdate])
final_phase.order.add_edge(LegalDrafting, CertificationIssue)
final_phase.order.add_edge(CertificationIssue, ClientBriefing)
final_phase.order.add_edge(ClientBriefing, ArchivalUpdate)

# Compose main flow as partial order:
# phase1 --> phase2 --> detection_phase --> final_phase
root = StrictPartialOrder(nodes=[phase1, phase2, detection_phase, final_phase])
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, detection_phase)
root.order.add_edge(detection_phase, final_phase)