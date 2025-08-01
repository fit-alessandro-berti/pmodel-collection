# Generated from: 872d66a6-5966-4af4-a8d6-e75ccc4c473f.json
# Description: This process involves the intricate verification and validation of antique artifacts to establish provenance, authenticity, and historical significance. It begins with initial artifact intake and visual inspection, followed by scientific testing such as radiocarbon dating and material composition analysis. Experts then conduct stylistic comparisons against known historical records and previous auction results. Concurrently, archival research is performed to trace ownership lineage and contextual history. A forensic examination checks for restoration or forgery signs. Findings are compiled into a detailed report, which undergoes peer review by external historians and scientists. Finally, the artifact is either certified, cataloged for sale, or returned to its owner with recommendations for preservation or further study.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_intake      = Transition(label='Artifact Intake')
visual_inspect       = Transition(label='Visual Inspect')
radiocarbon_test     = Transition(label='Radiocarbon Test')
material_analysis    = Transition(label='Material Analysis')
stylistic_compare    = Transition(label='Stylistic Compare')
historical_research  = Transition(label='Historical Research')
ownership_trace      = Transition(label='Ownership Trace')
forensic_check       = Transition(label='Forensic Check')
restoration_inspect  = Transition(label='Restoration Inspect')
forgery_detect       = Transition(label='Forgery Detect')
data_compile         = Transition(label='Data Compile')
report_draft         = Transition(label='Report Draft')
peer_review          = Transition(label='Peer Review')
certification        = Transition(label='Certification')
catalog_entry        = Transition(label='Catalog Entry')
owner_feedback       = Transition(label='Owner Feedback')
preservation_advise  = Transition(label='Preservation Advise')

# Sub-model for forensic examination (branching into two parallel checks)
forensic_sub = StrictPartialOrder(nodes=[forensic_check,
                                         restoration_inspect,
                                         forgery_detect])
forensic_sub.order.add_edge(forensic_check, restoration_inspect)
forensic_sub.order.add_edge(forensic_check, forgery_detect)

# Sub-model for the "return to owner" branch
owner_branch = StrictPartialOrder(nodes=[owner_feedback,
                                         preservation_advise])
owner_branch.order.add_edge(owner_feedback, preservation_advise)

# XOR operator for final disposition
final_xor = OperatorPOWL(operator=Operator.XOR,
                         children=[certification,
                                   catalog_entry,
                                   owner_branch])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    visual_inspect,
    radiocarbon_test,
    material_analysis,
    stylistic_compare,
    historical_research,
    ownership_trace,
    forensic_sub,
    data_compile,
    report_draft,
    peer_review,
    final_xor
])

# Sequence: Artifact intake -> visual inspection -> two tests in parallel
root.order.add_edge(artifact_intake, visual_inspect)
root.order.add_edge(visual_inspect, radiocarbon_test)
root.order.add_edge(visual_inspect, material_analysis)

# After both tests, start analysis branches in parallel
for next_act in [stylistic_compare, historical_research, ownership_trace, forensic_sub]:
    root.order.add_edge(radiocarbon_test, next_act)
    root.order.add_edge(material_analysis, next_act)

# After analysis & forensic, compile data
root.order.add_edge(stylistic_compare, data_compile)
root.order.add_edge(historical_research, data_compile)
root.order.add_edge(ownership_trace, data_compile)
root.order.add_edge(forensic_sub, data_compile)

# Draft report and peer review
root.order.add_edge(data_compile, report_draft)
root.order.add_edge(report_draft, peer_review)

# Final choice after peer review
root.order.add_edge(peer_review, final_xor)