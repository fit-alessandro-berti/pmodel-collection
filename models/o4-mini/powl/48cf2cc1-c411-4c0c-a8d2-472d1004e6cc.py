# Generated from: 48cf2cc1-c411-4c0c-a8d2-472d1004e6cc.json
# Description: This process involves locating, authenticating, and reintegrating lost or stolen corporate artifacts, such as proprietary prototypes, rare documents, or legacy technology components. It includes cross-departmental coordination between legal, security, R&D, and external recovery agents to ensure artifacts are safely recovered, verified for authenticity, and reintegrated into corporate archives or production lines. The process requires risk assessment, covert operations, chain-of-custody documentation, and final disposition planning to mitigate potential intellectual property loss and uphold corporate heritage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
initiate        = Transition(label='Initiate Request')
assign_agent    = Transition(label='Assign Agent')
conduct_audit   = Transition(label='Conduct Audit')
gather_intel    = Transition(label='Gather Intel')
perform_surv    = Transition(label='Perform Surveillance')
legal_review    = Transition(label='Legal Review')
risk_assessment = Transition(label='Risk Assessment')
coordinate      = Transition(label='Coordinate Teams')
secure_funding  = Transition(label='Secure Funding')
plan_recovery   = Transition(label='Plan Recovery')
execute_ret     = Transition(label='Execute Retrieval')
authenticate    = Transition(label='Authenticate Item')
document_chain  = Transition(label='Document Chain')
archive_artifact= Transition(label='Archive Artifact')
report_outcome  = Transition(label='Report Outcome')
review_process  = Transition(label='Review Process')

# Build a loop: Plan Recovery then Execute Retrieval; repeat until successful
recovery_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[plan_recovery, execute_ret]
)

# Assemble the global partial order
root = StrictPartialOrder(nodes=[
    initiate,
    assign_agent,
    conduct_audit,
    gather_intel,
    perform_surv,
    legal_review,
    risk_assessment,
    coordinate,
    secure_funding,
    recovery_loop,
    authenticate,
    document_chain,
    archive_artifact,
    report_outcome,
    review_process
])

# Define ordering: initiate → assign agent
root.order.add_edge(initiate, assign_agent)

# After assignment, all prep tasks run concurrently, then join into the recovery loop
for task in [
    conduct_audit,
    gather_intel,
    perform_surv,
    legal_review,
    risk_assessment,
    coordinate,
    secure_funding
]:
    root.order.add_edge(assign_agent, task)
    root.order.add_edge(task, recovery_loop)

# After successful recovery loop, continue sequentially
root.order.add_edge(recovery_loop, authenticate)
root.order.add_edge(authenticate, document_chain)
root.order.add_edge(document_chain, archive_artifact)
root.order.add_edge(archive_artifact, report_outcome)
root.order.add_edge(report_outcome, review_process)