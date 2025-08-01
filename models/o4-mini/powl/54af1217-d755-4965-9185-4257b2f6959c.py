# Generated from: 54af1217-d755-4965-9185-4257b2f6959c.json
# Description: This process outlines the complex series of steps involved in authenticating ancient artifacts for museums or private collectors. It begins with initial artifact intake and condition assessment, followed by provenance research and material analysis using advanced spectroscopy. Expert consultations and historical context alignment are conducted to verify authenticity. Parallel to scientific testing, legal checks on ownership and export compliance are performed. Results are compiled into a comprehensive authentication report. If authenticity is confirmed, preservation recommendations are made and the artifact is cataloged into secure storage. In case of doubts, additional testing or third-party review is initiated. The process concludes with client approval and final documentation archiving, ensuring traceability and compliance with cultural heritage laws.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
artifact_intake    = Transition(label='Artifact Intake')
condition_check    = Transition(label='Condition Check')
provenance_search  = Transition(label='Provenance Search')
material_test      = Transition(label='Material Test')
spectroscopy_scan  = Transition(label='Spectroscopy Scan')
expert_review      = Transition(label='Expert Review')
context_align      = Transition(label='Context Align')
legal_verify       = Transition(label='Legal Verify')
export_check       = Transition(label='Export Check')
report_compile     = Transition(label='Report Compile')
additional_tests   = Transition(label='Additional Tests')
third_party_review = Transition(label='Third-Party Review')
preservation_plan  = Transition(label='Preservation Plan')
catalog_entry      = Transition(label='Catalog Entry')
client_approval    = Transition(label='Client Approval')
archive_docs       = Transition(label='Archive Docs')

# Scientific testing branch: Provenance Search -> Material Test -> Spectroscopy Scan -> Expert Review -> Context Align
scientific_branch = StrictPartialOrder(nodes=[
    provenance_search, material_test, spectroscopy_scan, expert_review, context_align
])
scientific_branch.order.add_edge(provenance_search, material_test)
scientific_branch.order.add_edge(material_test, spectroscopy_scan)
scientific_branch.order.add_edge(spectroscopy_scan, expert_review)
scientific_branch.order.add_edge(expert_review, context_align)

# Legal checks branch: Legal Verify -> Export Check
legal_branch = StrictPartialOrder(nodes=[legal_verify, export_check])
legal_branch.order.add_edge(legal_verify, export_check)

# Additional-testing sequence for doubts
additional_seq = StrictPartialOrder(nodes=[additional_tests, third_party_review])
additional_seq.order.add_edge(additional_tests, third_party_review)

# Loop: Report Compile, then either exit or do additional tests & re-compile
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[report_compile, additional_seq])

# Root partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    scientific_branch,
    legal_branch,
    loop_node,
    preservation_plan,
    catalog_entry,
    client_approval,
    archive_docs
])

# Control-flow dependencies
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, scientific_branch)
root.order.add_edge(condition_check, legal_branch)
root.order.add_edge(scientific_branch, loop_node)
root.order.add_edge(legal_branch, loop_node)
root.order.add_edge(loop_node, preservation_plan)
root.order.add_edge(preservation_plan, catalog_entry)
root.order.add_edge(catalog_entry, client_approval)
root.order.add_edge(client_approval, archive_docs)