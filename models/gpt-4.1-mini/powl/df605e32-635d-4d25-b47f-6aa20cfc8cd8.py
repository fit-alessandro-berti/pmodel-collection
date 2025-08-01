# Generated from: df605e32-635d-4d25-b47f-6aa20cfc8cd8.json
# Description: This process governs the identification, authentication, and retrieval of lost or stolen corporate artifacts that hold significant historical or intellectual value. It involves cross-departmental coordination, legal compliance verification, covert negotiation with third parties, and secure logistics to ensure the artifact's safe return while preserving its confidentiality and integrity. Each step requires meticulous documentation, risk assessment, and contingency planning to mitigate potential reputational and financial damages associated with artifact loss. The process concludes with restoration and archival procedures to reintegrate the artifact within corporate heritage assets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Artifact_Scan = Transition(label='Artifact Scan')
Ownership_Verify = Transition(label='Ownership Verify')
Risk_Assess = Transition(label='Risk Assess')
Legal_Review = Transition(label='Legal Review')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Recovery_Plan = Transition(label='Recovery Plan')
Third_Party_Contact = Transition(label='Third-Party Contact')
Negotiation_Setup = Transition(label='Negotiation Setup')
Secure_Transport = Transition(label='Secure Transport')
Condition_Inspect = Transition(label='Condition Inspect')
Restoration_Begin = Transition(label='Restoration Begin')
Documentation_Log = Transition(label='Documentation Log')
Heritage_Archive = Transition(label='Heritage Archive')
Final_Audit = Transition(label='Final Audit')
Process_Close = Transition(label='Process Close')

# Initial partial order: Artifact Scan -> Ownership Verify -> Risk Assess
initial_po = StrictPartialOrder(nodes=[Artifact_Scan, Ownership_Verify, Risk_Assess])
initial_po.order.add_edge(Artifact_Scan, Ownership_Verify)
initial_po.order.add_edge(Ownership_Verify, Risk_Assess)

# Legal compliance branch: Legal Review must happen after Risk Assess
legal_branch = StrictPartialOrder(nodes=[Risk_Assess, Legal_Review, Stakeholder_Notify])
legal_branch.order.add_edge(Risk_Assess, Legal_Review)
legal_branch.order.add_edge(Legal_Review, Stakeholder_Notify)

# Recovery plan after Stakeholder Notify
recovery_plan_po = StrictPartialOrder(nodes=[Stakeholder_Notify, Recovery_Plan])
recovery_plan_po.order.add_edge(Stakeholder_Notify, Recovery_Plan)

# Third-party negotiation loop: (Third-Party Contact, Negotiation Setup) repeated until exit
negotiation_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Third_Party_Contact,
        Negotiation_Setup
    ]
)

# Secure transport and condition inspect after negotiation loop and recovery planning
post_negotiation_po = StrictPartialOrder(
    nodes=[recovery_plan_po, negotiation_loop, Secure_Transport, Condition_Inspect])
# Link recovery plan -> negotiation loop (loop start)
post_negotiation_po.order.add_edge(recovery_plan_po, negotiation_loop)
# negotiation loop done before secure transport
post_negotiation_po.order.add_edge(negotiation_loop, Secure_Transport)
# secure transport before condition inspect
post_negotiation_po.order.add_edge(Secure_Transport, Condition_Inspect)

# Documentation log can happen concurrently with condition inspect (they are concurrent)
doc_log_node = Documentation_Log

# After condition inspect and documentation, Restoration Begin
restoration_po = StrictPartialOrder(
    nodes=[Condition_Inspect, doc_log_node, Restoration_Begin])
restoration_po.order.add_edge(Condition_Inspect, Restoration_Begin)
restoration_po.order.add_edge(doc_log_node, Restoration_Begin)

# Heritage archive -> Final Audit -> Process Close sequence
final_po = StrictPartialOrder(nodes=[Heritage_Archive, Final_Audit, Process_Close])
final_po.order.add_edge(Heritage_Archive, Final_Audit)
final_po.order.add_edge(Final_Audit, Process_Close)

# Heritage archive occurs after Restoration Begin
heritage_edge = (Restoration_Begin, Heritage_Archive)

# Build the full PO combining all parts
# We'll combine initial_po, legal_branch, post_negotiation_po, restoration_po, final_po into one PO

# Nodes:
all_nodes = [
    Artifact_Scan, Ownership_Verify, Risk_Assess, Legal_Review, Stakeholder_Notify, Recovery_Plan,
    Third_Party_Contact, Negotiation_Setup, Secure_Transport, Condition_Inspect, Documentation_Log,
    Restoration_Begin, Heritage_Archive, Final_Audit, Process_Close,
    negotiation_loop  # loop operator node
]

root = StrictPartialOrder(nodes=all_nodes)

# Add all edges from the pieces

# initial_po edges
root.order.add_edge(Artifact_Scan, Ownership_Verify)
root.order.add_edge(Ownership_Verify, Risk_Assess)

# legal_branch edges
root.order.add_edge(Risk_Assess, Legal_Review)
root.order.add_edge(Legal_Review, Stakeholder_Notify)

# recovery_plan edges
root.order.add_edge(Stakeholder_Notify, Recovery_Plan)

# post_negotiation_po edges
root.order.add_edge(Recovery_Plan, negotiation_loop)
root.order.add_edge(negotiation_loop, Secure_Transport)
root.order.add_edge(Secure_Transport, Condition_Inspect)

# restoration_po edges
root.order.add_edge(Condition_Inspect, Restoration_Begin)
root.order.add_edge(Documentation_Log, Restoration_Begin)

# Documentation_Log concurrent with Condition_Inspect, no edge needed (both are nodes in root).

# final_po edges
root.order.add_edge(Restoration_Begin, Heritage_Archive)
root.order.add_edge(Heritage_Archive, Final_Audit)
root.order.add_edge(Final_Audit, Process_Close)