# Generated from: 5d48f8fe-345f-4790-b182-418d2c7ee4bd.json
# Description: This process involves the complex evaluation and authentication of antique artifacts, combining historical research, scientific analysis, and expert consultations. It begins with initial artifact intake and condition assessment, followed by provenance verification through archival research. Scientific tests such as radiocarbon dating and material composition analysis are then conducted to validate the artifact's age and origin. Concurrently, expert appraisers evaluate stylistic and craftsmanship details. Results are synthesized into a comprehensive authentication report, which undergoes peer review before final certification is issued. The process also includes risk assessment for forgery and fraud prevention, culminating in secure documentation and artifact registration in a centralized database for future reference.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ArtifactIntake = Transition(label='Artifact Intake')
ConditionCheck = Transition(label='Condition Check')
ProvenanceSearch = Transition(label='Provenance Search')
ArchiveReview = Transition(label='Archive Review')
RadiocarbonTest = Transition(label='Radiocarbon Test')
MaterialScan = Transition(label='Material Scan')
StyleAssessment = Transition(label='Style Assessment')
CraftsmanshipEval = Transition(label='Craftsmanship Eval')
ExpertConsultation = Transition(label='Expert Consultation')
ForgeryRisk = Transition(label='Forgery Risk')
PeerReview = Transition(label='Peer Review')
ReportDraft = Transition(label='Report Draft')
FinalCertification = Transition(label='Final Certification')
SecureRegistration = Transition(label='Secure Registration')
DatabaseEntry = Transition(label='Database Entry')

# Provenance verification partial order (ProvenanceSearch --> ArchiveReview)
provenancePO = StrictPartialOrder(nodes=[ProvenanceSearch, ArchiveReview])
provenancePO.order.add_edge(ProvenanceSearch, ArchiveReview)

# Scientific tests partial order (RadiocarbonTest and MaterialScan concurrent)
scientificPO = StrictPartialOrder(nodes=[RadiocarbonTest, MaterialScan])

# Expert evaluations partial order (StyleAssessment --> CraftsmanshipEval --> ExpertConsultation)
expertEvalPO = StrictPartialOrder(
    nodes=[StyleAssessment, CraftsmanshipEval, ExpertConsultation]
)
expertEvalPO.order.add_edge(StyleAssessment, CraftsmanshipEval)
expertEvalPO.order.add_edge(CraftsmanshipEval, ExpertConsultation)

# Synthesis: ReportDraft after scientific tests and expert consultation (both concurrent before)
# So the two (scientificPO and expertEvalPO) are concurrent, then both precede ReportDraft
synthesisPredecessors = StrictPartialOrder(
    nodes=[scientificPO, expertEvalPO]
)
# No order edges between scientificPO and expertEvalPO => concurrent

# Combined scientific and expert evaluations concurrency, then ReportDraft
synthPO = StrictPartialOrder(
    nodes=[scientificPO, expertEvalPO, ReportDraft]
)
synthPO.order.add_edge(scientificPO, ReportDraft)
synthPO.order.add_edge(expertEvalPO, ReportDraft)

# Initial steps: ArtifactIntake --> ConditionCheck --> Provenance and then merge
initialPO = StrictPartialOrder(nodes=[ArtifactIntake, ConditionCheck, provenancePO])
initialPO.order.add_edge(ArtifactIntake, ConditionCheck)
initialPO.order.add_edge(ConditionCheck, provenancePO)

# After Provenance verification, scientific tests and expert evaluation start concurrently
# The two after Provenance verification (provenancePO --> scientificPO and expertEvalPO)
# And then go to synthesis (including ReportDraft)

# We can create a partial order where provenancePO precedes both scientificPO and expertEvalPO,
# which are concurrent, then leading to ReportDraft

# We need to merge initialPO, scientificPO, expertEvalPO, and synthesis.

# Build the partial order:
root = StrictPartialOrder(
    nodes=[
        initialPO,              # ArtifactIntake -> ConditionCheck -> ProvenancePO
        scientificPO,           # RadiocarbonTest || MaterialScan
        expertEvalPO,           # StyleAssessment -> CraftsmanshipEval -> ExpertConsultation
        ReportDraft,
        ForgeryRisk,
        PeerReview,
        FinalCertification,
        SecureRegistration,
        DatabaseEntry,
    ]
)

# Add ordering edges:
# initialPO --> scientificPO and expertEvalPO
root.order.add_edge(initialPO, scientificPO)
root.order.add_edge(initialPO, expertEvalPO)

# scientificPO and expertEvalPO --> ReportDraft
root.order.add_edge(scientificPO, ReportDraft)
root.order.add_edge(expertEvalPO, ReportDraft)

# ForgeryRisk occurs concurrently with ReportDraft synthesis? The description says "includes risk assessment" and presumably can run concurrently.
# We'll assume ForgeryRisk starts after ConditionCheck and after Provenance (to be safe parallel after Provenance just like scientific and expert eval)
root.order.add_edge(initialPO, ForgeryRisk)

# After ReportDraft:
# ReportDraft --> PeerReview --> FinalCertification --> SecureRegistration --> DatabaseEntry
root.order.add_edge(ReportDraft, PeerReview)
root.order.add_edge(PeerReview, FinalCertification)
root.order.add_edge(FinalCertification, SecureRegistration)
root.order.add_edge(SecureRegistration, DatabaseEntry)