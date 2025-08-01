# Generated from: f5fe2cd7-bbd4-45ef-a60b-a2c18794f20e.json
# Description: This process outlines the intricate steps involved in authenticating historical artifacts for museum acquisition. It begins with initial provenance research, followed by material analysis using spectrometry and radiocarbon dating. Expert consultations are conducted to verify stylistic elements and historical context. Legal documentation is reviewed to ensure acquisition legitimacy. If discrepancies arise, re-examination or alternative sourcing is pursued. The process concludes with final approval by the acquisitions committee and secure cataloging for exhibit planning. This workflow ensures both scientific and legal rigor in artifact authentication, minimizing the risk of forgery or misattribution in cultural heritage collections.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Radiocarbon_Test = Transition(label='Radiocarbon Test')
Stylistic_Review = Transition(label='Stylistic Review')
Expert_Consult = Transition(label='Expert Consult')
Document_Audit = Transition(label='Document Audit')
Legal_Verify = Transition(label='Legal Verify')
Condition_Report = Transition(label='Condition Report')
Discrepancy_Flag = Transition(label='Discrepancy Flag')
Reexamination = Transition(label='Re-examination')
Alternative_Source = Transition(label='Alternative Source')
Acquisition_Vote = Transition(label='Acquisition Vote')
Catalog_Entry = Transition(label='Catalog Entry')
Exhibit_Plan = Transition(label='Exhibit Plan')
Final_Approval = Transition(label='Final Approval')

# First partial order: Material Scan and Radiocarbon Test in parallel after Provenance Check
material_tests = StrictPartialOrder(nodes=[Material_Scan, Radiocarbon_Test])
# no edges between Material_Scan and Radiocarbon_Test: concurrent

# Then Stylistic Review and Expert Consult in parallel
stylistic_expert = StrictPartialOrder(nodes=[Stylistic_Review, Expert_Consult])

# Choice after Legal Verify (either Condition Report or Discrepancy Flag)
# Discrepancy branch leads to a loop: Discrepancy Flag -> loop(re-examination or alternative) repeated
# We model "if discrepancies arise" by a XOR between:
# - Condition Report (no problems)
# - Discrepancy branch with loop

# Loop node: execute Re-examination, then choose to exit or execute Alternative Source then Re-examination again
loop = OperatorPOWL(operator=Operator.LOOP, children=[Reexamination, Alternative_Source])

# Discrepancy branch: Discrepancy Flag --> loop
discrepancy_branch = StrictPartialOrder(nodes=[Discrepancy_Flag, loop])
discrepancy_branch.order.add_edge(Discrepancy_Flag, loop)

# Choice between Condition Report and discrepancy branch (exclusive choice)
condition_or_discrepancy = OperatorPOWL(operator=Operator.XOR, children=[Condition_Report, discrepancy_branch])

# Legal Verify --> choice (Condition Report or Discrepancy branch)
legal_choice = StrictPartialOrder(nodes=[Legal_Verify, condition_or_discrepancy])
legal_choice.order.add_edge(Legal_Verify, condition_or_discrepancy)

# After choice, Acquisition Vote --> Catalog Entry --> Exhibit Plan --> Final Approval
final_sequence = StrictPartialOrder(
    nodes=[Acquisition_Vote, Catalog_Entry, Exhibit_Plan, Final_Approval]
)
final_sequence.order.add_edge(Acquisition_Vote, Catalog_Entry)
final_sequence.order.add_edge(Catalog_Entry, Exhibit_Plan)
final_sequence.order.add_edge(Exhibit_Plan, Final_Approval)

# Now build the main sequence with partial orders and operators
# Provenance Check --> material_tests --> stylistic_expert --> Document Audit --> legal_choice --> final_sequence
root = StrictPartialOrder(
    nodes=[Provenance_Check, material_tests, stylistic_expert, Document_Audit, legal_choice, final_sequence]
)
root.order.add_edge(Provenance_Check, material_tests)
root.order.add_edge(material_tests, stylistic_expert)
root.order.add_edge(stylistic_expert, Document_Audit)
root.order.add_edge(Document_Audit, legal_choice)
root.order.add_edge(legal_choice, final_sequence)