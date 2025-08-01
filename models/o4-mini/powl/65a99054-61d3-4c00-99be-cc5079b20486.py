# Generated from: 65a99054-61d3-4c00-99be-cc5079b20486.json
# Description: This process governs the verification and authentication of rare historical artifacts submitted for appraisal or acquisition. It involves multi-disciplinary evaluation including provenance research, material composition analysis, expert consultations, and legal clearance checks. The workflow ensures that every artifact is thoroughly vetted for authenticity, condition, and legal ownership before final certification and cataloging. The process also integrates risk assessment for potential forgeries and coordinates with international artifact databases to prevent illicit trade. Final decisions are documented, and discrepancies trigger secondary evaluations or legal investigations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sub_rev = Transition(label='Submission Review')
init_screen = Transition(label='Initial Screening')
prov_check = Transition(label='Provenance Check')
material_test = Transition(label='Material Testing')
expert_consult = Transition(label='Expert Consultation')
legal_clearance = Transition(label='Legal Clearance')
risk_assessment = Transition(label='Risk Assessment')
db_crosscheck = Transition(label='Database Crosscheck')
forgery_detection = Transition(label='Forgery Detection')
condition_report = Transition(label='Condition Report')
secondary_review = Transition(label='Secondary Review')
certification_draft = Transition(label='Certification Draft')
final_approval = Transition(label='Final Approval')
documentation = Transition(label='Documentation')
client_notification = Transition(label='Client Notification')
archive_update = Transition(label='Archive Update')

# Parallel evaluation phase
parallel_eval = StrictPartialOrder(nodes=[
    prov_check, material_test, expert_consult,
    legal_clearance, risk_assessment, db_crosscheck,
    forgery_detection
])
# No order edges => fully concurrent

# Normal certification path
normal_path = StrictPartialOrder(nodes=[
    certification_draft, final_approval,
    documentation, client_notification,
    archive_update
])
normal_path.order.add_edge(certification_draft, final_approval)
normal_path.order.add_edge(final_approval, documentation)
normal_path.order.add_edge(documentation, client_notification)
normal_path.order.add_edge(client_notification, archive_update)

# Secondary review path
secondary_path = StrictPartialOrder(nodes=[
    secondary_review, certification_draft,
    final_approval, documentation,
    client_notification, archive_update
])
secondary_path.order.add_edge(secondary_review, certification_draft)
secondary_path.order.add_edge(certification_draft, final_approval)
secondary_path.order.add_edge(final_approval, documentation)
secondary_path.order.add_edge(documentation, client_notification)
secondary_path.order.add_edge(client_notification, archive_update)

# Choice between normal and secondary
xor_decision = OperatorPOWL(
    operator=Operator.XOR,
    children=[normal_path, secondary_path]
)

# Root workflow
root = StrictPartialOrder(nodes=[
    sub_rev, init_screen,
    parallel_eval, condition_report,
    xor_decision
])
root.order.add_edge(sub_rev, init_screen)
root.order.add_edge(init_screen, parallel_eval)
root.order.add_edge(parallel_eval, condition_report)
root.order.add_edge(condition_report, xor_decision)