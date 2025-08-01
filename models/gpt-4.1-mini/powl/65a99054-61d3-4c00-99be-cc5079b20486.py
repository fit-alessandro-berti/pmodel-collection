# Generated from: 65a99054-61d3-4c00-99be-cc5079b20486.json
# Description: This process governs the verification and authentication of rare historical artifacts submitted for appraisal or acquisition. It involves multi-disciplinary evaluation including provenance research, material composition analysis, expert consultations, and legal clearance checks. The workflow ensures that every artifact is thoroughly vetted for authenticity, condition, and legal ownership before final certification and cataloging. The process also integrates risk assessment for potential forgeries and coordinates with international artifact databases to prevent illicit trade. Final decisions are documented, and discrepancies trigger secondary evaluations or legal investigations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SubmissionReview = Transition(label='Submission Review')
InitialScreening = Transition(label='Initial Screening')
ProvenanceCheck = Transition(label='Provenance Check')
MaterialTesting = Transition(label='Material Testing')
ExpertConsultation = Transition(label='Expert Consultation')
ForgeryDetection = Transition(label='Forgery Detection')
LegalClearance = Transition(label='Legal Clearance')
RiskAssessment = Transition(label='Risk Assessment')
DatabaseCrosscheck = Transition(label='Database Crosscheck')
ConditionReport = Transition(label='Condition Report')
SecondaryReview = Transition(label='Secondary Review')
CertificationDraft = Transition(label='Certification Draft')
FinalApproval = Transition(label='Final Approval')
Documentation = Transition(label='Documentation')
ClientNotification = Transition(label='Client Notification')
ArchiveUpdate = Transition(label='Archive Update')

skip = SilentTransition()

# Secondary Review or Legal Investigation on discrepancies (choice)
secondary_or_legal = OperatorPOWL(operator=Operator.XOR, children=[SecondaryReview, LegalClearance])

# Loop to handle secondary evaluations or legal investigations triggered by discrepancies
# Loop structure: Execute Condition Report (A), then choose to exit or do secondary_or_legal (B)
# then Condition Report again, repeat until exit.
condition_loop = OperatorPOWL(operator=Operator.LOOP, children=[ConditionReport, secondary_or_legal])

# Multi-disciplinary evaluations can run partly in parallel (Provenance, Material, Expert)
# We'll model as a partial order with these three concurrent
multi_disciplinary_eval = StrictPartialOrder(nodes=[ProvenanceCheck, MaterialTesting, ExpertConsultation])

# Risk assessment and database crosscheck come after multidisciplinary evaluating
risk_and_db = StrictPartialOrder(nodes=[RiskAssessment, DatabaseCrosscheck])
risk_and_db.order.add_edge(RiskAssessment, DatabaseCrosscheck)

# Forgery detection after risk assessment and database check
# But ForgeryDetection probably after or concurrent with these? 
# To be safe, place ForgeryDetection after DatabaseCrosscheck.
seq_after_multidisciplinary = StrictPartialOrder(
    nodes=[multi_disciplinary_eval, risk_and_db, ForgeryDetection]
)
seq_after_multidisciplinary.order.add_edge(multi_disciplinary_eval, risk_and_db)
seq_after_multidisciplinary.order.add_edge(risk_and_db, ForgeryDetection)

# Initial screening before multidisciplinary evaluations
initial_and_evals = StrictPartialOrder(nodes=[InitialScreening, seq_after_multidisciplinary])
initial_and_evals.order.add_edge(InitialScreening, seq_after_multidisciplinary)

# Verification process after legal clearance (re-check legal clearance if needed)
# Note Legal Clearance is also part of the secondary_or_legal choice, so we need to avoid confusion.
# Main Legal Clearance after ForgeryDetection:
verification_seq = StrictPartialOrder(nodes=[seq_after_multidisciplinary, LegalClearance])
verification_seq.order.add_edge(seq_after_multidisciplinary, LegalClearance)

# Assemble main partial order:
# Submission Review -> Initial Screening -> (Provenance, Material, Expert)
# -> Risk Assessment -> Database Crosscheck -> Forgery Detection -> Legal Clearance
root_main_seq = StrictPartialOrder(nodes=[SubmissionReview, InitialScreening, multi_disciplinary_eval, risk_and_db,
                                         ForgeryDetection, LegalClearance])
root_main_seq.order.add_edge(SubmissionReview, InitialScreening)
root_main_seq.order.add_edge(InitialScreening, multi_disciplinary_eval)
root_main_seq.order.add_edge(multi_disciplinary_eval, risk_and_db)
root_main_seq.order.add_edge(risk_and_db, ForgeryDetection)
root_main_seq.order.add_edge(ForgeryDetection, LegalClearance)

# After legal clearance is Condition Report with possible loops for secondary or legal investigations
verification_with_condition = StrictPartialOrder(nodes=[root_main_seq, condition_loop])
verification_with_condition.order.add_edge(root_main_seq, condition_loop)

# After condition loop: Certification Draft -> Final Approval -> Documentation -> Client Notification -> Archive Update
finalization_seq = StrictPartialOrder(nodes=[CertificationDraft, FinalApproval, Documentation, ClientNotification, ArchiveUpdate])
finalization_seq.order.add_edge(CertificationDraft, FinalApproval)
finalization_seq.order.add_edge(FinalApproval, Documentation)
finalization_seq.order.add_edge(Documentation, ClientNotification)
finalization_seq.order.add_edge(ClientNotification, ArchiveUpdate)

# Complete process
root = StrictPartialOrder(nodes=[verification_with_condition, finalization_seq])
root.order.add_edge(verification_with_condition, finalization_seq)