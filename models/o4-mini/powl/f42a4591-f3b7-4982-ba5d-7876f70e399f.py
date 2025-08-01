# Generated from: f42a4591-f3b7-4982-ba5d-7876f70e399f.json
# Description: This process outlines the intricate steps involved in restoring valuable antiques to their original condition while preserving historical integrity. It begins with detailed inspection and provenance verification, followed by careful disassembly and cleaning using specialized techniques. After assessment, necessary repairs are performed using period-appropriate materials and methods. Surface treatments and finishes are applied to match the original appearance. The process concludes with reassembly, quality assurance, and archival documentation to ensure transparency and authenticity for future owners or exhibitions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions for each activity
inspect_item      = Transition(label='Inspect Item')
verify_prov       = Transition(label='Verify Provenance')
disassemble_parts = Transition(label='Disassemble Parts')
clean_comp        = Transition(label='Clean Components')
document_cond     = Transition(label='Document Condition')
analyze_dmg       = Transition(label='Analyze Damage')
select_mats       = Transition(label='Select Materials')
perform_reps      = Transition(label='Perform Repairs')
match_finishes    = Transition(label='Match Finishes')
apply_treatments  = Transition(label='Apply Treatments')
reassemble_item   = Transition(label='Reassemble Item')
quality_check     = Transition(label='Quality Check')
photograph_res    = Transition(label='Photograph Results')
update_archive    = Transition(label='Update Archive')
client_review     = Transition(label='Client Review')
finalize_report   = Transition(label='Finalize Report')

# Build the partial order
root = StrictPartialOrder(nodes=[
    inspect_item, verify_prov, disassemble_parts, clean_comp,
    document_cond, analyze_dmg, select_mats, perform_reps,
    match_finishes, apply_treatments, reassemble_item,
    quality_check, photograph_res, update_archive,
    client_review, finalize_report
])

# Add the control-flow order
root.order.add_edge(inspect_item, verify_prov)
root.order.add_edge(verify_prov, disassemble_parts)
root.order.add_edge(disassemble_parts, clean_comp)
root.order.add_edge(clean_comp, document_cond)
root.order.add_edge(document_cond, analyze_dmg)
root.order.add_edge(analyze_dmg, select_mats)
root.order.add_edge(select_mats, perform_reps)
root.order.add_edge(perform_reps, match_finishes)
root.order.add_edge(match_finishes, apply_treatments)
root.order.add_edge(apply_treatments, reassemble_item)
root.order.add_edge(reassemble_item, quality_check)
root.order.add_edge(quality_check, photograph_res)
root.order.add_edge(photograph_res, update_archive)
root.order.add_edge(update_archive, client_review)
root.order.add_edge(client_review, finalize_report)