# Generated from: b94b1815-4681-4c83-9edf-58c003916c0e.json
# Description: This process governs the authentication of rare historical artifacts submitted by collectors or museums. It involves multidisciplinary examination including material analysis, provenance verification, and expert consensus. The process begins with artifact intake and initial documentation, followed by non-invasive imaging and chemical testing. Parallel provenance research and comparative stylistic analysis are conducted by separate teams. Findings are compiled into a preliminary report, which undergoes peer review before scheduling an expert panel discussion. Upon consensus, a final authentication certificate is issued. The process also includes dispute resolution and archival storage of all documentation for future reference, ensuring traceability and integrity of artifact validation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
artifact_intake     = Transition(label='Artifact Intake')
initial_docs        = Transition(label='Initial Docs')
material_scan       = Transition(label='Material Scan')
chemical_test       = Transition(label='Chemical Test')
provenance_check    = Transition(label='Provenance Check')
stylistic_review    = Transition(label='Stylistic Review')
parallel_research   = Transition(label='Parallel Research')  # join node
prelim_report       = Transition(label='Prelim Report')
peer_review         = Transition(label='Peer Review')
panel_meeting       = Transition(label='Panel Meeting')
consensus_vote      = Transition(label='Consensus Vote')
certificate_issue   = Transition(label='Certificate Issue')
dispute_handling    = Transition(label='Dispute Handling')
archival_storage    = Transition(label='Archival Storage')
followup_audit      = Transition(label='Follow-up Audit')

# Silent transitions for XOR choices
skip1 = SilentTransition()
skip2 = SilentTransition()

# Optional dispute handling after certificate issuance
xor_dispute = OperatorPOWL(
    operator=Operator.XOR,
    children=[skip1, dispute_handling]
)

# Optional follow-up audit after archival storage
xor_audit = OperatorPOWL(
    operator=Operator.XOR,
    children=[skip2, followup_audit]
)

# Build the strict partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    initial_docs,
    material_scan,
    chemical_test,
    provenance_check,
    stylistic_review,
    parallel_research,
    prelim_report,
    peer_review,
    panel_meeting,
    consensus_vote,
    certificate_issue,
    xor_dispute,
    archival_storage,
    xor_audit
])

# Define the partial order edges
# Sequential intake and documentation
root.order.add_edge(artifact_intake, initial_docs)

# Parallel scans after docs
root.order.add_edge(initial_docs, material_scan)
root.order.add_edge(initial_docs, chemical_test)

# Parallel research after scans
root.order.add_edge(material_scan, provenance_check)
root.order.add_edge(chemical_test, provenance_check)
root.order.add_edge(material_scan, stylistic_review)
root.order.add_edge(chemical_test, stylistic_review)

# Join research into a single node
root.order.add_edge(provenance_check, parallel_research)
root.order.add_edge(stylistic_review, parallel_research)

# Reporting and review sequence
root.order.add_edge(parallel_research, prelim_report)
root.order.add_edge(prelim_report, peer_review)
root.order.add_edge(peer_review, panel_meeting)
root.order.add_edge(panel_meeting, consensus_vote)
root.order.add_edge(consensus_vote, certificate_issue)

# Optional dispute handling
root.order.add_edge(certificate_issue, xor_dispute)
root.order.add_edge(xor_dispute, archival_storage)

# Optional follow-up audit
root.order.add_edge(archival_storage, xor_audit)