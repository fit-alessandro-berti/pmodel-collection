# Generated from: a3a62fb1-a32c-436c-87d4-1bf10367857d.json
# Description: This process outlines the comprehensive steps involved in authenticating rare historical artifacts for a private museum collection. It integrates multidisciplinary expert evaluations, scientific testing, provenance research, legal compliance verification, and ethical sourcing assessments. The workflow ensures that every artifact undergoes rigorous scrutiny to confirm authenticity, legal ownership, and cultural significance before acquisition, minimizing risks of forgery, illicit trade, and ethical conflicts. The process is iterative, requiring multiple rounds of expert consensus and documentation updates, culminating in final approval for museum display or archival storage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
initial_review    = Transition(label='Initial Review')
provenance_check  = Transition(label='Provenance Check')
scientific_test   = Transition(label='Scientific Test')
material_analysis = Transition(label='Material Analysis')
expert_consult    = Transition(label='Expert Consult')
historical_ctx    = Transition(label='Historical Context')
forgery_detect    = Transition(label='Forgery Detect')
legal_verify      = Transition(label='Legal Verify')
ethics_assess     = Transition(label='Ethics Assess')
compliance_audit  = Transition(label='Compliance Audit')
consensus_meet    = Transition(label='Consensus Meet')
documentation     = Transition(label='Documentation')
condition_report  = Transition(label='Condition Report')
acquisition_vote  = Transition(label='Acquisition Vote')
final_approval    = Transition(label='Final Approval')
display_plan      = Transition(label='Display Plan')
archival_store    = Transition(label='Archival Store')

# Build the loop for iterative consensus & documentation updates
# Body A = consensus_meet
# Body B = (documentation -> condition_report)
doc_seq = StrictPartialOrder(nodes=[documentation, condition_report])
doc_seq.order.add_edge(documentation, condition_report)

loop_consensus = OperatorPOWL(
    operator=Operator.LOOP,
    children=[consensus_meet, doc_seq]
)

# Build the XOR choice for final disposition
xor_end = OperatorPOWL(
    operator=Operator.XOR,
    children=[display_plan, archival_store]
)

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    initial_review,
    provenance_check,
    scientific_test,
    material_analysis,
    expert_consult,
    historical_ctx,
    forgery_detect,
    legal_verify,
    ethics_assess,
    compliance_audit,
    loop_consensus,
    acquisition_vote,
    final_approval,
    xor_end
])

# Define the control‐flow dependencies
root.order.add_edge(initial_review,   provenance_check)
root.order.add_edge(provenance_check, scientific_test)
root.order.add_edge(provenance_check, material_analysis)
root.order.add_edge(scientific_test,  expert_consult)
root.order.add_edge(material_analysis, expert_consult)
root.order.add_edge(expert_consult,   historical_ctx)
root.order.add_edge(historical_ctx,   forgery_detect)
root.order.add_edge(forgery_detect,   legal_verify)
root.order.add_edge(legal_verify,     ethics_assess)
root.order.add_edge(ethics_assess,    compliance_audit)
root.order.add_edge(compliance_audit, loop_consensus)
root.order.add_edge(loop_consensus,   acquisition_vote)
root.order.add_edge(acquisition_vote, final_approval)
root.order.add_edge(final_approval,   xor_end)