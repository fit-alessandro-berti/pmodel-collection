# Generated from: a3a62fb1-a32c-436c-87d4-1bf10367857d.json
# Description: This process outlines the comprehensive steps involved in authenticating rare historical artifacts for a private museum collection. It integrates multidisciplinary expert evaluations, scientific testing, provenance research, legal compliance verification, and ethical sourcing assessments. The workflow ensures that every artifact undergoes rigorous scrutiny to confirm authenticity, legal ownership, and cultural significance before acquisition, minimizing risks of forgery, illicit trade, and ethical conflicts. The process is iterative, requiring multiple rounds of expert consensus and documentation updates, culminating in final approval for museum display or archival storage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Scientific_Test = Transition(label='Scientific Test')
Material_Analysis = Transition(label='Material Analysis')
Expert_Consult = Transition(label='Expert Consult')
Historical_Context = Transition(label='Historical Context')
Legal_Verify = Transition(label='Legal Verify')
Ethics_Assess = Transition(label='Ethics Assess')
Forgery_Detect = Transition(label='Forgery Detect')
Consensus_Meet = Transition(label='Consensus Meet')
Documentation = Transition(label='Documentation')
Condition_Report = Transition(label='Condition Report')
Acquisition_Vote = Transition(label='Acquisition Vote')
Display_Plan = Transition(label='Display Plan')
Archival_Store = Transition(label='Archival Store')
Compliance_Audit = Transition(label='Compliance Audit')
Final_Approval = Transition(label='Final Approval')

skip = SilentTransition()

# Define the iterative expert consensus and documentation loop:
# Loop body: 
#   B = (Expert Consult -> Historical Context -> Forgery Detect -> Consensus Meet -> Documentation -> Condition Report)
# Loop A is the Initial Review + core checks before loop start:
#   A = (Initial Review -> Provenance Check -> Scientific Test -> Material Analysis -> Legal Verify -> Ethics Assess -> Compliance Audit)
A = StrictPartialOrder(
    nodes=[Initial_Review, Provenance_Check, Scientific_Test, Material_Analysis, Legal_Verify, Ethics_Assess, Compliance_Audit]
)
A.order.add_edge(Initial_Review, Provenance_Check)
A.order.add_edge(Provenance_Check, Scientific_Test)
A.order.add_edge(Scientific_Test, Material_Analysis)
A.order.add_edge(Material_Analysis, Legal_Verify)
A.order.add_edge(Legal_Verify, Ethics_Assess)
A.order.add_edge(Ethics_Assess, Compliance_Audit)

B = StrictPartialOrder(
    nodes=[Expert_Consult, Historical_Context, Forgery_Detect, Consensus_Meet, Documentation, Condition_Report]
)
B.order.add_edge(Expert_Consult, Historical_Context)
B.order.add_edge(Historical_Context, Forgery_Detect)
B.order.add_edge(Forgery_Detect, Consensus_Meet)
B.order.add_edge(Consensus_Meet, Documentation)
B.order.add_edge(Documentation, Condition_Report)

# Define the loop: * (A, B)
# meaning: execute A once, then either exit or execute B then A again repeatedly
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# After the loop, final activities: Acquisition Vote -> choice Display Plan OR Archival Store -> Final Approval
vote = Acquisition_Vote
display = Display_Plan
archive = Archival_Store
final = Final_Approval

choice_after_vote = OperatorPOWL(operator=Operator.XOR, children=[display, archive])

# Build the PO for final phase
final_phase = StrictPartialOrder(
    nodes=[vote, choice_after_vote, final]
)
final_phase.order.add_edge(vote, choice_after_vote)
final_phase.order.add_edge(choice_after_vote, final)

# Compose overall process: loop -> final_phase
root = StrictPartialOrder(
    nodes=[loop, final_phase]
)
root.order.add_edge(loop, final_phase)