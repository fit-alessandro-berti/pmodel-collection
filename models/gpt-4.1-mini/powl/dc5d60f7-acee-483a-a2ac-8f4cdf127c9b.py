# Generated from: dc5d60f7-acee-483a-a2ac-8f4cdf127c9b.json
# Description: This process outlines the comprehensive workflow for authenticating rare historical artifacts through multidisciplinary evaluation, provenance verification, scientific testing, and expert consultation. It involves initial artifact intake, condition assessment, advanced material analysis, stylistic comparison with known exemplars, blockchain provenance logging, and collaborative expert panel review. The workflow also includes risk assessment for forgery, legal compliance checks, report generation, and final certification. Throughout the process, iterative feedback loops ensure data integrity and accuracy before artifact release or acquisition recommendation. This atypical yet realistic process supports museums, collectors, and auction houses in validating artifact authenticity while minimizing fraudulent risks.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Intake_Review = Transition(label='Intake Review')
Condition_Scan = Transition(label='Condition Scan')
Material_Test = Transition(label='Material Test')
Style_Match = Transition(label='Style Match')
Provenance_Log = Transition(label='Provenance Log')
Forgery_Risk = Transition(label='Forgery Risk')
Legal_Audit = Transition(label='Legal Audit')
Expert_Panel = Transition(label='Expert Panel')
Data_Crosscheck = Transition(label='Data Crosscheck')
Report_Draft = Transition(label='Report Draft')
Blockchain_Tag = Transition(label='Blockchain Tag')
Certification = Transition(label='Certification')
Client_Feedback = Transition(label='Client Feedback')
Final_Approval = Transition(label='Final Approval')
Release_Prep = Transition(label='Release Prep')

# Loop representing iterative feedback loops for data integrity and accuracy:
# Loop body:
#   A = Data Crosscheck (assessment step)
#   B = Client Feedback (feedback before repeating data crosscheck)
# The pattern: exec A, then either exit or exec B then A again (loop).
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Data_Crosscheck, Client_Feedback])

# Parallel / partial order construction:
# Initial intake and condition assessment in sequence
initial_seq = StrictPartialOrder(nodes=[Intake_Review, Condition_Scan])
initial_seq.order.add_edge(Intake_Review, Condition_Scan)

# After condition scan, start Material Test and Style Match in parallel (no order edge)
material_style = StrictPartialOrder(nodes=[Material_Test, Style_Match])

# Provenance Log and Blockchain Tag form a parallel subblock after Material Test and Style Match
prov_block = StrictPartialOrder(nodes=[Provenance_Log, Blockchain_Tag])

# Join these: material_style and prov_block sequentially - material_style then prov_block
# We can create a combined PO:
mat_style_prov = StrictPartialOrder(nodes=[Material_Test, Style_Match, Provenance_Log, Blockchain_Tag])
mat_style_prov.order.add_edge(Material_Test, Provenance_Log)
mat_style_prov.order.add_edge(Style_Match, Provenance_Log)
mat_style_prov.order.add_edge(Material_Test, Blockchain_Tag)
mat_style_prov.order.add_edge(Style_Match, Blockchain_Tag)

# After provenance and blockchain tagging, there is the Expert Panel review concurrently with Forgery Risk and Legal Audit in parallel
expert_forgery_legal = StrictPartialOrder(nodes=[Expert_Panel, Forgery_Risk, Legal_Audit])
# No edges => these three are concurrent

# After expert panel and checks, we do the feedback loop
# So, order all expert_forgery_legal dependencies before feedback loop
expert_checks_feedback = StrictPartialOrder(
    nodes=[Expert_Panel, Forgery_Risk, Legal_Audit, feedback_loop]
)
expert_checks_feedback.order.add_edge(Expert_Panel, feedback_loop)
expert_checks_feedback.order.add_edge(Forgery_Risk, feedback_loop)
expert_checks_feedback.order.add_edge(Legal_Audit, feedback_loop)

# After feedback completed and finalized, comes Report Draft
# Then Final Approval
report_approval = StrictPartialOrder(nodes=[Report_Draft, Final_Approval])
report_approval.order.add_edge(Report_Draft, Final_Approval)

# Followed finally by Certification and Release Prep in sequence
cert_release = StrictPartialOrder(nodes=[Certification, Release_Prep])
cert_release.order.add_edge(Certification, Release_Prep)

# Connect all parts in a big partial order:

# All nodes combined:
all_nodes = [
    Intake_Review,
    Condition_Scan,
    Material_Test,
    Style_Match,
    Provenance_Log,
    Blockchain_Tag,
    Expert_Panel,
    Forgery_Risk,
    Legal_Audit,
    feedback_loop,
    Report_Draft,
    Final_Approval,
    Certification,
    Release_Prep,
]

root = StrictPartialOrder(nodes=all_nodes)

# Define order edges:

# Initial sequence
root.order.add_edge(Intake_Review, Condition_Scan)

# Condition Scan leads to Material Test and Style Match concurrently
root.order.add_edge(Condition_Scan, Material_Test)
root.order.add_edge(Condition_Scan, Style_Match)

# Material Test and Style Match lead to Provenance Log and Blockchain Tag concurrently
root.order.add_edge(Material_Test, Provenance_Log)
root.order.add_edge(Style_Match, Provenance_Log)
root.order.add_edge(Material_Test, Blockchain_Tag)
root.order.add_edge(Style_Match, Blockchain_Tag)

# Provenance Log and Blockchain Tag lead to Expert Panel, Forgery Risk, and Legal Audit (all concurrent)
root.order.add_edge(Provenance_Log, Expert_Panel)
root.order.add_edge(Provenance_Log, Forgery_Risk)
root.order.add_edge(Provenance_Log, Legal_Audit)
root.order.add_edge(Blockchain_Tag, Expert_Panel)
root.order.add_edge(Blockchain_Tag, Forgery_Risk)
root.order.add_edge(Blockchain_Tag, Legal_Audit)

# Expert Panel, Forgery Risk, and Legal Audit lead to feedback loop
root.order.add_edge(Expert_Panel, feedback_loop)
root.order.add_edge(Forgery_Risk, feedback_loop)
root.order.add_edge(Legal_Audit, feedback_loop)

# Feedback loop leads to Report Draft
root.order.add_edge(feedback_loop, Report_Draft)

# Report Draft leads to Final Approval
root.order.add_edge(Report_Draft, Final_Approval)

# Final Approval leads to Certification
root.order.add_edge(Final_Approval, Certification)

# Certification leads to Release Prep
root.order.add_edge(Certification, Release_Prep)