# Generated from: 5e7b6d7a-2aa3-4b02-b3ac-048a336f1c05.json
# Description: This process involves the systematic verification and validation of ancient artifacts using interdisciplinary techniques combining historical research, material science, and digital imaging. Activities include provenance tracing, carbon dating, spectral analysis, and expert consultations. The workflow ensures accurate authentication for museums or private collectors, mitigating risks of forgery while preserving cultural heritage. The process further integrates legal compliance checks, condition assessment, and secure transportation planning to maintain artifact integrity throughout the chain of custody. Anomalies detected prompt iterative re-examinations and final certification issuance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Provenance_Check = Transition(label='Provenance Check')
Historical_Review = Transition(label='Historical Review')
Material_Sampling = Transition(label='Material Sampling')
Carbon_Dating = Transition(label='Carbon Dating')
Spectral_Scan = Transition(label='Spectral Scan')
Microscopic_Exam = Transition(label='Microscopic Exam')
Expert_Consult = Transition(label='Expert Consult')
Condition_Report = Transition(label='Condition Report')
Forgery_Screening = Transition(label='Forgery Screening')
Legal_Review = Transition(label='Legal Review')
Restoration_Plan = Transition(label='Restoration Plan')
Transport_Setup = Transition(label='Transport Setup')
Security_Audit = Transition(label='Security Audit')
Certification = Transition(label='Certification')
Reexamination = Transition(label='Reexamination')
skip = SilentTransition()

# Provenance tracing branch: Provenance Check --> Historical Review (can be concurrent with Material Sampling branch)
provenance_PO = StrictPartialOrder(nodes=[Provenance_Check, Historical_Review])
provenance_PO.order.add_edge(Provenance_Check, Historical_Review)

# Material Science Sampling branch: Material Sampling --> Carbon Dating --> Spectral Scan --> Microscopic Exam
material_PO = StrictPartialOrder(nodes=[Material_Sampling, Carbon_Dating, Spectral_Scan, Microscopic_Exam])
material_PO.order.add_edge(Material_Sampling, Carbon_Dating)
material_PO.order.add_edge(Carbon_Dating, Spectral_Scan)
material_PO.order.add_edge(Spectral_Scan, Microscopic_Exam)

# Expert Consult (can occur after Historical Review and Microscopic Exam)
expert_PO = StrictPartialOrder(nodes=[Historical_Review, Microscopic_Exam, Expert_Consult])
expert_PO.order.add_edge(Historical_Review, Expert_Consult)
expert_PO.order.add_edge(Microscopic_Exam, Expert_Consult)

# Condition report and Forgery screening branch (after Expert Consult)
cond_forgery_PO = StrictPartialOrder(nodes=[Expert_Consult, Condition_Report, Forgery_Screening])
cond_forgery_PO.order.add_edge(Expert_Consult, Condition_Report)
cond_forgery_PO.order.add_edge(Condition_Report, Forgery_Screening)

# Legal compliance checks (after Forgery Screening)
legal_PO = StrictPartialOrder(nodes=[Forgery_Screening, Legal_Review])
legal_PO.order.add_edge(Forgery_Screening, Legal_Review)

# Restoration Plan (after Legal Review)
restoration_PO = StrictPartialOrder(nodes=[Legal_Review, Restoration_Plan])
restoration_PO.order.add_edge(Legal_Review, Restoration_Plan)

# Transport Setup and Security Audit can be concurrent after Restoration Plan
transport_security_PO = StrictPartialOrder(nodes=[Restoration_Plan, Transport_Setup, Security_Audit])
transport_security_PO.order.add_edge(Restoration_Plan, Transport_Setup)
transport_security_PO.order.add_edge(Restoration_Plan, Security_Audit)

# Merge all preparatory activities into one partial order - provenance, material sampling, expert consult, etc.

# Build a main PO merging all concurrent and sequential parts:
# - provenance_PO and material_PO run in partial order: provenance_PO before expert_PO and material_PO before expert_PO.
# We can merge provenance_PO and material_PO concurrently, then both must precede expert_PO.

prep_PO = StrictPartialOrder(
    nodes=[
        Provenance_Check, Historical_Review,  # provenance_PO
        Material_Sampling, Carbon_Dating, Spectral_Scan, Microscopic_Exam,  # material_PO
        Expert_Consult  # expert_PO
    ]
)
# Add provenance_PO edges
prep_PO.order.add_edge(Provenance_Check, Historical_Review)
# Add material_PO edges
prep_PO.order.add_edge(Material_Sampling, Carbon_Dating)
prep_PO.order.add_edge(Carbon_Dating, Spectral_Scan)
prep_PO.order.add_edge(Spectral_Scan, Microscopic_Exam)
# Expert consult depends on Historical Review and Microscopic Exam
prep_PO.order.add_edge(Historical_Review, Expert_Consult)
prep_PO.order.add_edge(Microscopic_Exam, Expert_Consult)

# Sequence after Expert Consult (Condition Report, Forgery Screening, Legal Review, Restoration Plan, Transport Setup, Security Audit)

post_expert_PO = StrictPartialOrder(
    nodes=[
        Expert_Consult,
        Condition_Report,
        Forgery_Screening,
        Legal_Review,
        Restoration_Plan,
        Transport_Setup,
        Security_Audit
    ]
)
post_expert_PO.order.add_edge(Expert_Consult, Condition_Report)
post_expert_PO.order.add_edge(Condition_Report, Forgery_Screening)
post_expert_PO.order.add_edge(Forgery_Screening, Legal_Review)
post_expert_PO.order.add_edge(Legal_Review, Restoration_Plan)
post_expert_PO.order.add_edge(Restoration_Plan, Transport_Setup)
post_expert_PO.order.add_edge(Restoration_Plan, Security_Audit)

# Loop for reexamination triggered by anomalies:
# Loop node: * (post_expert_PO, Reexamination)
# After post_expert_PO activities, loop: if anomalies => Reexamination followed by post_expert_PO again, else exit.

loop = OperatorPOWL(operator=Operator.LOOP, children=[post_expert_PO, Reexamination])

# Finally, Certification follows completion of the loop (final certification issuance)

final_PO = StrictPartialOrder(nodes=[loop, Certification])
final_PO.order.add_edge(loop, Certification)

# The overall root PO is the preparation PO followed by the loop+certification sequence
root = StrictPartialOrder(nodes=[prep_PO, final_PO])
root.order.add_edge(prep_PO, final_PO)