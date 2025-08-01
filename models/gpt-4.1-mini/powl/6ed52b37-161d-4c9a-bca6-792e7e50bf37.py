# Generated from: 6ed52b37-161d-4c9a-bca6-792e7e50bf37.json
# Description: This process involves verifying the authenticity and provenance of rare cultural artifacts before acquisition by a museum or private collector. It includes multi-stage scientific testing, historical record analysis, expert consultations across various domains, and coordination with international regulatory agencies. The process ensures comprehensive validation of artifact origin, condition assessment, legal clearance, and ethical sourcing. It incorporates iterative hypothesis refinement, cross-referencing with global databases, and final certification issuance, aiming to prevent fraud and protect cultural heritage while facilitating secure and transparent transactions in the artifact market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ArtifactIntake = Transition(label='Artifact Intake')
InitialSurvey = Transition(label='Initial Survey')
MaterialTesting = Transition(label='Material Testing')
HistoricalAudit = Transition(label='Historical Audit')
ExpertReview = Transition(label='Expert Review')
ProvenanceCheck = Transition(label='Provenance Check')
DatabaseQuery = Transition(label='Database Query')
LegalScreening = Transition(label='Legal Screening')
EthicsAssessment = Transition(label='Ethics Assessment')
ConditionReport = Transition(label='Condition Report')
HypothesisUpdate = Transition(label='Hypothesis Update')
RegulatoryLiaison = Transition(label='Regulatory Liaison')
CertificationPrep = Transition(label='Certification Prep')
FinalValidation = Transition(label='Final Validation')
OwnershipTransfer = Transition(label='Ownership Transfer')

# Scientific testing partial order
# InitialSurvey -> (MaterialTesting and HistoricalAudit concurrently)
Testing_PO = StrictPartialOrder(nodes=[InitialSurvey, MaterialTesting, HistoricalAudit])
Testing_PO.order.add_edge(InitialSurvey, MaterialTesting)
Testing_PO.order.add_edge(InitialSurvey, HistoricalAudit)

# Expert consultations partial order
# ExpertReview -> ProvenanceCheck -> DatabaseQuery concurrently with LegalScreening and EthicsAssessment
Expert_PO = StrictPartialOrder(
    nodes=[ExpertReview, ProvenanceCheck, DatabaseQuery, LegalScreening, EthicsAssessment]
)
Expert_PO.order.add_edge(ExpertReview, ProvenanceCheck)
Expert_PO.order.add_edge(ProvenanceCheck, DatabaseQuery)
# LegalScreening and EthicsAssessment are independent but come after ProvenanceCheck
Expert_PO.order.add_edge(ProvenanceCheck, LegalScreening)
Expert_PO.order.add_edge(ProvenanceCheck, EthicsAssessment)

# Condition Assessment and Hypothesis Update loop
# ConditionReport then loop: (HypothesisUpdate then ConditionReport) zero or more times
LoopCondition = OperatorPOWL(operator=Operator.LOOP, children=[ConditionReport, HypothesisUpdate])

# Validation and regulatory & certification sequence
# RegulatoryLiaison -> CertificationPrep -> FinalValidation -> OwnershipTransfer
Validation_PO = StrictPartialOrder(
    nodes=[RegulatoryLiaison, CertificationPrep, FinalValidation, OwnershipTransfer]
)
Validation_PO.order.add_edge(RegulatoryLiaison, CertificationPrep)
Validation_PO.order.add_edge(CertificationPrep, FinalValidation)
Validation_PO.order.add_edge(FinalValidation, OwnershipTransfer)

# Assemble full partial order of the process

# Nodes include Artifact Intake, Testing_PO, Expert_PO,
# LoopCondition, and Validation_PO, plus InitialSurvey, Testing_PO nodes, and so forth

root_nodes = [
    ArtifactIntake,
    Testing_PO,
    Expert_PO,
    LoopCondition,
    Validation_PO,
]

root = StrictPartialOrder(nodes=root_nodes)

# Define order relations between major phases

# Artifact Intake must come before Testing
root.order.add_edge(ArtifactIntake, Testing_PO)

# Testing must finish before Expert consultations
root.order.add_edge(Testing_PO, Expert_PO)

# Expert consultations must finish before Condition assessment + Hypothesis loop
root.order.add_edge(Expert_PO, LoopCondition)

# Condition assessment loop must finish before validation and certification
root.order.add_edge(LoopCondition, Validation_PO)