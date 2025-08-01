# Generated from: e55b647a-caea-4357-b293-11c638134e4e.json
# Description: This process outlines the complex workflow involved in authenticating historical artifacts prior to acquisition or exhibition. It integrates multidisciplinary expertise including provenance research, material analysis, and legal verification. The process begins with initial artifact intake and proceeds through detailed scientific testing, expert consultations, and provenance tracing in international archives. Concurrently, legal teams verify ownership rights and ensure compliance with cultural heritage laws. Throughout the process, findings are documented and reviewed iteratively to build a comprehensive authentication report. Final approval requires consensus from multiple departments before the artifact is accepted or rejected. This atypical yet realistic process is critical to prevent fraud, protect cultural heritage, and maintain institutional credibility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ArtifactIntake = Transition(label='Artifact Intake')

ProvenanceCheck = Transition(label='Provenance Check')
MaterialSampling = Transition(label='Material Sampling')
ScientificTest = Transition(label='Scientific Test')
ExpertReview = Transition(label='Expert Review')
ArchiveSearch = Transition(label='Archive Search')

LegalVerify = Transition(label='Legal Verify')
OwnershipConfirm = Transition(label='Ownership Confirm')
ComplianceAudit = Transition(label='Compliance Audit')

DataDocumentation = Transition(label='Data Documentation')
InterimReport = Transition(label='Interim Report')

DepartmentReview = Transition(label='Department Review')
ConsensusMeeting = Transition(label='Consensus Meeting')

FinalApproval = Transition(label='Final Approval')
ArtifactRelease = Transition(label='Artifact Release')

# Define provenance branch (Provenance Check -> Material Sampling -> Scientific Test -> Expert Review -> Archive Search)
# We consider this as a strict partial order, because these are steps in a chain
provenance_po = StrictPartialOrder(
    nodes=[ProvenanceCheck, MaterialSampling, ScientificTest, ExpertReview, ArchiveSearch]
)
provenance_po.order.add_edge(ProvenanceCheck, MaterialSampling)
provenance_po.order.add_edge(MaterialSampling, ScientificTest)
provenance_po.order.add_edge(ScientificTest, ExpertReview)
provenance_po.order.add_edge(ExpertReview, ArchiveSearch)

# Define legal branch (Legal Verify -> Ownership Confirm -> Compliance Audit)
legal_po = StrictPartialOrder(
    nodes=[LegalVerify, OwnershipConfirm, ComplianceAudit]
)
legal_po.order.add_edge(LegalVerify, OwnershipConfirm)
legal_po.order.add_edge(OwnershipConfirm, ComplianceAudit)

# Both branches proceed concurrently after Artifact Intake
# So after Artifact Intake, both provenance_po and legal_po can proceed concurrently
# Combine these two branches in a PO with concurrent nodes:
# nodes = [ArtifactIntake, provenance_po, legal_po]
concurrent_branches_po = StrictPartialOrder(
    nodes=[provenance_po, legal_po]
)
# no order edges between provenance_po and legal_po to show concurrency

# After provenance and legal branches finish, we have documentation and iterative reporting:
# Data Documentation -> Interim Report -> loop back to Data Documentation or exit loop

# Loop: * (Data Documentation, Interim Report)
# meaning: execute Data Documentation, then choose:
#   - exit the loop or
#   - execute Interim Report then Data Documentation again
loop = OperatorPOWL(operator=Operator.LOOP, children=[DataDocumentation, InterimReport])

# Order from concurrent branches to loop
# To model that loop starts after both branches complete, we create a PO with nodes:
# - concurrent_branches_po
# - loop
# and add edges from both concurrent branches to loop

after_branches_po = StrictPartialOrder(
    nodes=[concurrent_branches_po, loop]
)
after_branches_po.order.add_edge(concurrent_branches_po, loop)

# Then Department Review -> Consensus Meeting -> Final Approval -> Artifact Release (strict sequence)
final_sequence = StrictPartialOrder(
    nodes=[DepartmentReview, ConsensusMeeting, FinalApproval, ArtifactRelease]
)
final_sequence.order.add_edge(DepartmentReview, ConsensusMeeting)
final_sequence.order.add_edge(ConsensusMeeting, FinalApproval)
final_sequence.order.add_edge(FinalApproval, ArtifactRelease)

# Finally, the full model:
# Artifact Intake -> [provenance_po || legal_po] -> loop -> final sequence

root = StrictPartialOrder(
    nodes=[ArtifactIntake, concurrent_branches_po, loop, final_sequence]
)
# Artifact Intake before concurrent branches
root.order.add_edge(ArtifactIntake, concurrent_branches_po)
# concurrent branches before loop already done inside after_branches_po, but now concurrent_branches_po node is directly part of root
root.order.add_edge(concurrent_branches_po, loop)
# loop before final sequence
root.order.add_edge(loop, final_sequence)