# Generated from: 8eaa6472-5ab2-468e-be5c-af211837e059.json
# Description: This process outlines the detailed steps involved in authenticating historical artifacts for museum acquisition. It includes initial provenance research, multispectral imaging analysis, material composition testing, expert panel review, and legal clearance. The workflow integrates interdisciplinary collaboration, ensuring both scientific validation and cultural significance are verified before final cataloging and insurance appraisal. Each stage involves iterative feedback loops to address discrepancies and confirm authenticity, culminating in secure digital archiving of all findings and certification issuance to guarantee artifact legitimacy and traceability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic transitions for activities
Provenance_Check = Transition(label='Provenance Check')
Imaging_Scan = Transition(label='Imaging Scan')
Material_Test = Transition(label='Material Test')
Carbon_Dating = Transition(label='Carbon Dating')
Expert_Review = Transition(label='Expert Review')
Legal_Verify = Transition(label='Legal Verify')
Condition_Assess = Transition(label='Condition Assess')
Cultural_Context = Transition(label='Cultural Context')
Digital_Archive = Transition(label='Digital Archive')
Feedback_Loop = Transition(label='Feedback Loop')
Report_Draft = Transition(label='Report Draft')
Insurance_Appraise = Transition(label='Insurance Appraise')
Certification_Issue = Transition(label='Certification Issue')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Final_Approval = Transition(label='Final Approval')

# Scientific validation partial order before expert panel:
# Provenance Check --> (Imaging Scan and Material Test in parallel),
# Material Test --> Carbon Dating,
# Imaging Scan and Carbon Dating are concurrent (after Provenance Check and Material Test),
# both precede Expert Review.
scientific_val = StrictPartialOrder(nodes=[
    Provenance_Check,
    Imaging_Scan,
    Material_Test,
    Carbon_Dating,
    Expert_Review
])
scientific_val.order.add_edge(Provenance_Check, Imaging_Scan)
scientific_val.order.add_edge(Provenance_Check, Material_Test)
scientific_val.order.add_edge(Material_Test, Carbon_Dating)
scientific_val.order.add_edge(Imaging_Scan, Expert_Review)
scientific_val.order.add_edge(Carbon_Dating, Expert_Review)

# Feedback loop around Expert Review and related checks:
# Loop body: Feedback_Loop then scientific_val again
loop_body = StrictPartialOrder(nodes=[Feedback_Loop, scientific_val])
loop_body.order.add_edge(Feedback_Loop, scientific_val)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[scientific_val, Feedback_Loop])

# Cultural and legal validation partial order before cataloging:
# Stakeholder Meet precedes Cultural Context and Legal Verify,
# Cultural Context and Legal Verify concurrent, both precede Condition Assess,
# which precedes Report Draft.
cultural_legal_val = StrictPartialOrder(nodes=[
    Stakeholder_Meet,
    Cultural_Context,
    Legal_Verify,
    Condition_Assess,
    Report_Draft
])
cultural_legal_val.order.add_edge(Stakeholder_Meet, Cultural_Context)
cultural_legal_val.order.add_edge(Stakeholder_Meet, Legal_Verify)
cultural_legal_val.order.add_edge(Cultural_Context, Condition_Assess)
cultural_legal_val.order.add_edge(Legal_Verify, Condition_Assess)
cultural_legal_val.order.add_edge(Condition_Assess, Report_Draft)

# Feedback loop around cultural_legal_val with Feedback Loop:
feedback_loop2 = OperatorPOWL(operator=Operator.LOOP, children=[cultural_legal_val, Feedback_Loop])

# Final sequence after validations:
# Report Draft --> Insurance Appraise --> Certification Issue --> Final Approval --> Digital Archive
final_seq = StrictPartialOrder(nodes=[
    Report_Draft,
    Insurance_Appraise,
    Certification_Issue,
    Final_Approval,
    Digital_Archive
])
final_seq.order.add_edge(Report_Draft, Insurance_Appraise)
final_seq.order.add_edge(Insurance_Appraise, Certification_Issue)
final_seq.order.add_edge(Certification_Issue, Final_Approval)
final_seq.order.add_edge(Final_Approval, Digital_Archive)

# Compose entire process:
# 1) feedback_loop (scientific validation with loop)
# 2) feedback_loop2 (cultural/legal validation with loop)
# 3) final_seq

root = StrictPartialOrder(nodes=[feedback_loop, feedback_loop2, final_seq])
root.order.add_edge(feedback_loop, feedback_loop2)
root.order.add_edge(feedback_loop2, final_seq)