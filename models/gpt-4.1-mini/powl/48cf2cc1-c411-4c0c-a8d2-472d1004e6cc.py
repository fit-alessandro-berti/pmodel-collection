# Generated from: 48cf2cc1-c411-4c0c-a8d2-472d1004e6cc.json
# Description: This process involves locating, authenticating, and reintegrating lost or stolen corporate artifacts, such as proprietary prototypes, rare documents, or legacy technology components. It includes cross-departmental coordination between legal, security, R&D, and external recovery agents to ensure artifacts are safely recovered, verified for authenticity, and reintegrated into corporate archives or production lines. The process requires risk assessment, covert operations, chain-of-custody documentation, and final disposition planning to mitigate potential intellectual property loss and uphold corporate heritage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
initiate_request = Transition(label='Initiate Request')
assign_agent = Transition(label='Assign Agent')
conduct_audit = Transition(label='Conduct Audit')
gather_intel = Transition(label='Gather Intel')
perform_surveillance = Transition(label='Perform Surveillance')
legal_review = Transition(label='Legal Review')
risk_assessment = Transition(label='Risk Assessment')
coordinate_teams = Transition(label='Coordinate Teams')
secure_funding = Transition(label='Secure Funding')
plan_recovery = Transition(label='Plan Recovery')
execute_retrieval = Transition(label='Execute Retrieval')
authenticate_item = Transition(label='Authenticate Item')
document_chain = Transition(label='Document Chain')
archive_artifact = Transition(label='Archive Artifact')
report_outcome = Transition(label='Report Outcome')
review_process = Transition(label='Review Process')

# Modeling covert operations as choice between Gather Intel and Perform Surveillance
covert_ops = OperatorPOWL(operator=Operator.XOR, children=[gather_intel, perform_surveillance])

# Chain-of-custody documentation is Document Chain
# Final disposition includes Archive Artifact and Report Outcome in parallel (partial order with no order edges)
final_disposition = StrictPartialOrder(nodes=[archive_artifact, report_outcome])

# Cross-departmental coordination includes Legal Review, Risk Assessment, Coordinate Teams, Secure Funding (assume partial order)
coordination = StrictPartialOrder(nodes=[legal_review, risk_assessment, coordinate_teams, secure_funding])
# Add edges reflecting dependencies in coordination:
# Risk Assessment depends on Legal Review
coordination.order.add_edge(legal_review, risk_assessment)
# Coordinate Teams depends on Risk Assessment
coordination.order.add_edge(risk_assessment, coordinate_teams)
# Secure Funding depends on Coordinate Teams
coordination.order.add_edge(coordinate_teams, secure_funding)

# Recovery plan and execution sequence
plan_and_execute = StrictPartialOrder(nodes=[plan_recovery, execute_retrieval])
plan_and_execute.order.add_edge(plan_recovery, execute_retrieval)

# Authentication and documentation after execution
auth_and_doc = StrictPartialOrder(nodes=[authenticate_item, document_chain])
auth_and_doc.order.add_edge(authenticate_item, document_chain)

# Audit and covert ops can be partially concurrent but audit likely precedes covert_ops
audit_and_covert = StrictPartialOrder(nodes=[conduct_audit, covert_ops])
audit_and_covert.order.add_edge(conduct_audit, covert_ops)

# Entire process partial order nodes
# 1. Initiate Request -> Assign Agent -> conduct audit & covert ops
# 2. Then coordination
# 3. Then plan_and_execute
# 4. Then auth_and_doc
# 5. Then final_disposition
# 6. Then Review Process

root = StrictPartialOrder(nodes=[
    initiate_request,
    assign_agent,
    audit_and_covert,
    coordination,
    plan_and_execute,
    auth_and_doc,
    final_disposition,
    review_process
])

# Add the order edges for the main flow
root.order.add_edge(initiate_request, assign_agent)
root.order.add_edge(assign_agent, audit_and_covert)
root.order.add_edge(audit_and_covert, coordination)
root.order.add_edge(coordination, plan_and_execute)
root.order.add_edge(plan_and_execute, auth_and_doc)
root.order.add_edge(auth_and_doc, final_disposition)
root.order.add_edge(final_disposition, review_process)