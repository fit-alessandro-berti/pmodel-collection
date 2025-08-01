# Generated from: 54af1217-d755-4965-9185-4257b2f6959c.json
# Description: This process outlines the complex series of steps involved in authenticating ancient artifacts for museums or private collectors. It begins with initial artifact intake and condition assessment, followed by provenance research and material analysis using advanced spectroscopy. Expert consultations and historical context alignment are conducted to verify authenticity. Parallel to scientific testing, legal checks on ownership and export compliance are performed. Results are compiled into a comprehensive authentication report. If authenticity is confirmed, preservation recommendations are made and the artifact is cataloged into secure storage. In case of doubts, additional testing or third-party review is initiated. The process concludes with client approval and final documentation archiving, ensuring traceability and compliance with cultural heritage laws.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition objects
Artifact_Intake = Transition(label='Artifact Intake')
Condition_Check = Transition(label='Condition Check')

Provenance_Search = Transition(label='Provenance Search')

Material_Test = Transition(label='Material Test')
Spectroscopy_Scan = Transition(label='Spectroscopy Scan')

Expert_Review = Transition(label='Expert Review')
Context_Align = Transition(label='Context Align')

Legal_Verify = Transition(label='Legal Verify')
Export_Check = Transition(label='Export Check')

Report_Compile = Transition(label='Report Compile')

Preservation_Plan = Transition(label='Preservation Plan')
Catalog_Entry = Transition(label='Catalog Entry')

Additional_Tests = Transition(label='Additional Tests')
Third_Party_Review = Transition(label='Third-Party Review')

Client_Approval = Transition(label='Client Approval')
Archive_Docs = Transition(label='Archive Docs')

# Build the partial orders and choices according to description

# Step 1-2: Initial artifact intake and condition check
intake_and_condition = StrictPartialOrder(nodes=[Artifact_Intake, Condition_Check])
intake_and_condition.order.add_edge(Artifact_Intake, Condition_Check)

# Step 3-5: Provenance search and scientific tests (Material Test then Spectroscopy Scan)
provenance = Provenance_Search
material_and_spectroscopy = StrictPartialOrder(nodes=[Material_Test, Spectroscopy_Scan])
material_and_spectroscopy.order.add_edge(Material_Test, Spectroscopy_Scan)

# Step 6-7: Expert Review and Context Align
expert_and_context = StrictPartialOrder(nodes=[Expert_Review, Context_Align])
# no explicit order mentioned; parallel

# Step 8-9: Legal Verify and Export Check in parallel
legal_and_export = StrictPartialOrder(nodes=[Legal_Verify, Export_Check])
# no explicit order, so concurrent

# Parallel block of Provenance, Scientific Tests, Expert/Context, Legal checks
# Provenance_Search (single)
# material_and_spectroscopy
# expert_and_context
# legal_and_export

parallel_nodes = [provenance, material_and_spectroscopy, expert_and_context, legal_and_export]
parallel_block = StrictPartialOrder(nodes=parallel_nodes)
# No order among them - all concurrent

# Step 10: Report Compile after all above
# Add ordering edges from all parallel nodes to Report Compile

nodes_before_report = [provenance, material_and_spectroscopy, expert_and_context, legal_and_export]
report_compile = Report_Compile

report_block = StrictPartialOrder(nodes=nodes_before_report + [report_compile])
for n in nodes_before_report:
    report_block.order.add_edge(n, report_compile)

# Step 11-14: If authenticity confirmed -> Preservation Plan and Catalog Entry
# If doubts -> Additional Tests or Third-Party Review (choice)
# Then after additional testing/review, loop back to Preservation Plan and Catalog Entry

# Loop = *(A,B), where A = "Preservation Plan" and "Catalog Entry" sequentially,
# B = choice between "Additional Tests" and "Third-Party Review"

# Preservation Plan and Catalog Entry sequential:
preservation_and_catalog = StrictPartialOrder(nodes=[Preservation_Plan, Catalog_Entry])
preservation_and_catalog.order.add_edge(Preservation_Plan, Catalog_Entry)

# choice between Additional Tests and Third-Party Review
additional_or_thirdparty = OperatorPOWL(operator=Operator.XOR,
                                       children=[Additional_Tests, Third_Party_Review])

# loop(* (A,B)) with A=preservation_and_catalog and B=additional_or_thirdparty
loop = OperatorPOWL(operator=Operator.LOOP,
                   children=[preservation_and_catalog, additional_or_thirdparty])

# After loop: Client Approval and Archive Docs sequentially
client_and_archive = StrictPartialOrder(nodes=[Client_Approval, Archive_Docs])
client_and_archive.order.add_edge(Client_Approval, Archive_Docs)

# Build final partial order combining Report Compile, Loop and Client Approval/Archive Docs in sequence
final_po = StrictPartialOrder(nodes=[report_block, loop, client_and_archive])
final_po.order.add_edge(report_block, loop)
final_po.order.add_edge(loop, client_and_archive)

# The whole beginning: intake_and_condition before parallel block
# So the very first part: intake_and_condition before parallel block (provenance etc)
start_to_parallel = StrictPartialOrder(nodes=[intake_and_condition, parallel_block])
start_to_parallel.order.add_edge(intake_and_condition, parallel_block)

# Then finally from parallel_block to final_po (which starts report_block)
# We have defined report_block to start after parallel_block, 
# but report_block nodes include parallel_block nodes, 
# but parallel_block is in fact the multiple activities inside report_block's nodes.
# To strictly separate them, 
# we did: report_block = StrictPartialOrder(nodes=nodes_before_report + [report_compile])
# nodes_before_report include parallel_block children.

# Let's rebuild the full structure for clarity:

# Full construction:

# 1) intake_and_condition
# 2) parallel block: Provenance_Search, material_and_spectroscopy, expert_and_context, legal_and_export
# 3) report_compile after parallel block
# 4) loop on preservation/catalog and additional/third party review
# 5) client approval and archive docs

# We have these components:
# intake_and_condition --> parallel block (all activities concurrent)
# each parallel activity --> report_compile
# report_compile --> loop
# loop --> client_and_archive

# Put all in one StrictPartialOrder with all nodes and edges

root_nodes = [
    intake_and_condition,
    provenance,
    material_and_spectroscopy,
    expert_and_context,
    legal_and_export,
    report_compile,
    loop,
    client_and_archive
]

root = StrictPartialOrder(nodes=root_nodes)

# intake_and_condition --> all parallel nodes
for parallel_node in [provenance, material_and_spectroscopy, expert_and_context, legal_and_export]:
    root.order.add_edge(intake_and_condition, parallel_node)

# all parallel nodes --> report_compile
for parallel_node in [provenance, material_and_spectroscopy, expert_and_context, legal_and_export]:
    root.order.add_edge(parallel_node, report_compile)

# report_compile --> loop
root.order.add_edge(report_compile, loop)
# loop --> client_and_archive
root.order.add_edge(loop, client_and_archive)