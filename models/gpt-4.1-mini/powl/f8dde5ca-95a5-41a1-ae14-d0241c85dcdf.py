# Generated from: f8dde5ca-95a5-41a1-ae14-d0241c85dcdf.json
# Description: This process involves a multi-disciplinary approach to authenticate rare artifacts sourced from various global locations. It begins with preliminary provenance checks, followed by advanced material analysis using spectrometry and radiocarbon dating. Specialists then perform stylistic comparisons against extensive historical databases. Concurrently, blockchain registration is prepared to ensure traceability. Legal consultants review ownership legitimacy while conservators assess preservation needs. Finally, a comprehensive report is compiled, validated by an expert panel, and submitted to both the client and relevant cultural heritage authorities to ensure compliance and facilitate potential acquisition or exhibition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Radiocarbon_Test = Transition(label='Radiocarbon Test')
Style_Compare = Transition(label='Style Compare')
Database_Query = Transition(label='Database Query')
Blockchain_Prep = Transition(label='Blockchain Prep')
Legal_Review = Transition(label='Legal Review')
Ownership_Audit = Transition(label='Ownership Audit')
Conservation_Plan = Transition(label='Conservation Plan')
Expert_Panel = Transition(label='Expert Panel')
Report_Draft = Transition(label='Report Draft')
Client_Review = Transition(label='Client Review')
Authority_Submit = Transition(label='Authority Submit')
Exhibit_Setup = Transition(label='Exhibit Setup')
Final_Approval = Transition(label='Final Approval')

# Material analysis parallel activities after Provenance Check:
# Material Scan and Radiocarbon Test run in parallel
material_analysis = StrictPartialOrder(nodes=[Material_Scan, Radiocarbon_Test])

# Specialists perform stylistic comparisons against historical databases
# Style Compare and Database Query run in parallel
stylistic_analysis = StrictPartialOrder(nodes=[Style_Compare, Database_Query])

# Legal consultants and conservators run in parallel
legal_and_conservation = StrictPartialOrder(nodes=[Legal_Review, Ownership_Audit, Conservation_Plan])

# Client Review, Authority Submit, Exhibit Setup proceed concurrently after Expert Panel and Report Draft
final_submissions = StrictPartialOrder(nodes=[Client_Review, Authority_Submit, Exhibit_Setup])

# Compose the process in order, adding dependencies accordingly

# Provenance Check -> material analysis
# material_analysis -> stylistic_analysis
# stylistic_analysis and blockchain prep run concurrently, then both join on legal_and_conservation
# legal_and_conservation -> Report Draft -> Expert Panel -> final_submissions -> Final Approval

# Define initial partial orders for the main sequence parts

# 1) material_analysis order: no dependencies between Material_Scan and Radiocarbon_Test

# 2) stylistic_analysis order: no dependencies between Style_Compare and Database_Query

# 3) legal_and_conservation order: all three can run concurrently, no dependencies among Legal_Review, Ownership_Audit, Conservation_Plan


# Now build the main ordered nodes list:

# Starting from Provenance Check

# Create all top-level nodes to connect:

# - Provenance Check

# - material_analysis (Material_Scan, Radiocarbon_Test)

# - stylistic_analysis (Style_Compare, Database_Query)

# - Blockchain_Prep

# - legal_and_conservation (Legal_Review, Ownership_Audit, Conservation_Plan)

# - Report Draft

# - Expert Panel

# - final_submissions (Client Review, Authority Submit, Exhibit Setup)

# - Final Approval

# Top-level nodes for main flow:
top_nodes = [
    Provenance_Check,
    material_analysis,
    stylistic_analysis,
    Blockchain_Prep,
    legal_and_conservation,
    Report_Draft,
    Expert_Panel,
    final_submissions,
    Final_Approval,
]

root = StrictPartialOrder(nodes=top_nodes)

# Add edges to express the ordering constraints

# Provenance Check before material_analysis
root.order.add_edge(Provenance_Check, material_analysis)

# material_analysis before stylistic_analysis
root.order.add_edge(material_analysis, stylistic_analysis)

# stylistic_analysis and Blockchain_Prep proceed concurrently,
# so both should precede legal_and_conservation

root.order.add_edge(stylistic_analysis, legal_and_conservation)
root.order.add_edge(Blockchain_Prep, legal_and_conservation)

# legal_and_conservation before Report Draft
root.order.add_edge(legal_and_conservation, Report_Draft)

# Report Draft before Expert Panel
root.order.add_edge(Report_Draft, Expert_Panel)

# Expert Panel before final submissions
root.order.add_edge(Expert_Panel, final_submissions)

# final submissions before Final Approval
root.order.add_edge(final_submissions, Final_Approval)