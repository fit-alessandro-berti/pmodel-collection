# Generated from: edd7d61f-72d2-43f7-b83c-e9fb7cd9e85b.json
# Description: This process involves the intricate verification and authentication of antique artifacts for museums, collectors, and auction houses. It includes provenance research, material analysis, and expert consultations to ensure the artifact's legitimacy and historical significance. The workflow requires coordination between historians, chemists, and appraisers, often involving cross-border documentation verification and advanced imaging techniques. The process culminates in a detailed certification report, which is critical for insurance, sale, or exhibition purposes, ensuring the artifact’s value and authenticity are thoroughly established through multidisciplinary validation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Initial_Review = Transition(label='Initial Review')

Provenance_Check = Transition(label='Provenance Check')

Material_Scan = Transition(label='Material Scan')
Chemical_Test = Transition(label='Chemical Test')

Imaging_Capture = Transition(label='Imaging Capture')

Expert_Consult = Transition(label='Expert Consult')
Historical_Match = Transition(label='Historical Match')
Forgery_Detect = Transition(label='Forgery Detect')

Documentation_Verify = Transition(label='Documentation Verify')
Cross_Border_Check = Transition(label='Cross-Border Check')

Condition_Assess = Transition(label='Condition Assess')
Value_Estimate = Transition(label='Value Estimate')

Report_Draft = Transition(label='Report Draft')
Report_Review = Transition(label='Report Review')
Client_Approval = Transition(label='Client Approval')

Certification_Issue = Transition(label='Certification Issue')
Archive_Record = Transition(label='Archive Record')

# Provenance research branch (Provenance Check then Expert Consult branch)
# Expert Consult expands in choice between Historical Match (success) or Forgery Detect (failure)
expert_choice = OperatorPOWL(operator=Operator.XOR, children=[Historical_Match, Forgery_Detect])
provenance_branch = StrictPartialOrder(nodes=[Provenance_Check, Expert_Consult, expert_choice])
provenance_branch.order.add_edge(Provenance_Check, Expert_Consult)
provenance_branch.order.add_edge(Expert_Consult, expert_choice)

# Material analysis branch: Material Scan and Chemical Test done in parallel (unordered)
material_analysis = StrictPartialOrder(nodes=[Material_Scan, Chemical_Test])

# Imaging branch: Imaging Capture then two verifications in partial order with choice for cross-check
doc_xborder_choice = OperatorPOWL(operator=Operator.XOR, children=[Cross_Border_Check, Documentation_Verify])
imaging_branch = StrictPartialOrder(nodes=[Imaging_Capture, doc_xborder_choice])
imaging_branch.order.add_edge(Imaging_Capture, doc_xborder_choice)

# Coordination of initial review, provenance, material analysis, imaging (all concurrent but order from initial review)
initial_and_branches = StrictPartialOrder(nodes=[Initial_Review, provenance_branch, material_analysis, imaging_branch])
initial_and_branches.order.add_edge(Initial_Review, provenance_branch)
initial_and_branches.order.add_edge(Initial_Review, material_analysis)
initial_and_branches.order.add_edge(Initial_Review, imaging_branch)

# Condition Assess and Value Estimate concurrent, after provenance and others
cond_val = StrictPartialOrder(nodes=[Condition_Assess, Value_Estimate])
# No internal order between them (concurrent)

# Report drafting, then review, then client approval sequentially
report_seq = StrictPartialOrder(
    nodes=[Report_Draft, Report_Review, Client_Approval]
)
report_seq.order.add_edge(Report_Draft, Report_Review)
report_seq.order.add_edge(Report_Review, Client_Approval)

# Certification Issue then Archive Record sequentially
final_seq = StrictPartialOrder(nodes=[Certification_Issue, Archive_Record])
final_seq.order.add_edge(Certification_Issue, Archive_Record)

# Assemble main workflow partial order:
# initial_and_branches --> cond_val --> report_seq --> final_seq
root = StrictPartialOrder(
    nodes=[initial_and_branches, cond_val, report_seq, final_seq]
)
root.order.add_edge(initial_and_branches, cond_val)
root.order.add_edge(cond_val, report_seq)
root.order.add_edge(report_seq, final_seq)