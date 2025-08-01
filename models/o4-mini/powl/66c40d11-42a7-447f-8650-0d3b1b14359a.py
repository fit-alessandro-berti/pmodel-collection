# Generated from: 66c40d11-42a7-447f-8650-0d3b1b14359a.json
# Description: This process involves the complex validation and authentication of rare cultural artifacts sourced globally. It encompasses provenance research, multi-layered material analysis, expert consensus, and legal compliance verification. Each artifact undergoes detailed historical cross-referencing, advanced chemical testing, and digital imaging before final certification. The process also includes stakeholder coordination spanning archaeologists, legal advisors, and auction houses, ensuring authenticity, ethical acquisition, and traceability. Post-authentication, artifacts are cataloged with secure blockchain entries to prevent forgery, and continuous monitoring for ownership disputes is maintained, integrating international regulatory updates and client feedback loops.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artifact_intake   = Transition(label='Artifact Intake')
provenance_check  = Transition(label='Provenance Check')
material_scan     = Transition(label='Material Scan')
historical_match  = Transition(label='Historical Match')
imaging_capture   = Transition(label='Imaging Capture')
chemical_test     = Transition(label='Chemical Test')
legal_verify      = Transition(label='Legal Verify')
ethics_review     = Transition(label='Ethics Review')
market_analysis   = Transition(label='Market Analysis')
expert_review     = Transition(label='Expert Review')
consensus_vote    = Transition(label='Consensus Vote')
blockchain_log    = Transition(label='Blockchain Log')
ownership_audit   = Transition(label='Ownership Audit')
dispute_monitor   = Transition(label='Dispute Monitor')
regulation_sync   = Transition(label='Regulation Sync')
client_update     = Transition(label='Client Update')

# Expert consensus loop: perform Expert Review, then loop on Consensus Vote + Expert Review until consensus
ec_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[expert_review, consensus_vote]
)

# Continuous monitoring loop: Ownership Audit, then Dispute Monitor -> Regulation Sync -> Client Update, repeated
monitor_tasks = StrictPartialOrder(nodes=[dispute_monitor, regulation_sync, client_update])
monitor_tasks.order.add_edge(dispute_monitor, regulation_sync)
monitor_tasks.order.add_edge(regulation_sync, client_update)

monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ownership_audit, monitor_tasks]
)

# Root partial order combining all activities and control‐flow operators
root = StrictPartialOrder(nodes=[
    artifact_intake, provenance_check, material_scan, historical_match,
    imaging_capture, chemical_test, legal_verify, ethics_review,
    market_analysis, ec_loop, blockchain_log, monitor_loop
])

# Define ordering constraints
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, material_scan)
root.order.add_edge(artifact_intake, imaging_capture)
root.order.add_edge(artifact_intake, chemical_test)
root.order.add_edge(artifact_intake, legal_verify)
root.order.add_edge(artifact_intake, ethics_review)
root.order.add_edge(artifact_intake, market_analysis)

root.order.add_edge(provenance_check, historical_match)

# All the analyses and verifications must complete before consensus loop
for src in [material_scan, chemical_test, imaging_capture,
            historical_match, legal_verify, ethics_review, market_analysis]:
    root.order.add_edge(src, ec_loop)

# After consensus we log to blockchain, then enter continuous monitoring
root.order.add_edge(ec_loop, blockchain_log)
root.order.add_edge(blockchain_log, monitor_loop)