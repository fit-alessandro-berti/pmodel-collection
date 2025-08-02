# Generated from: b94b1815-4681-4c83-9edf-58c003916c0e.json
# Description: This process governs the authentication of rare historical artifacts submitted by collectors or museums. It involves multidisciplinary examination including material analysis, provenance verification, and expert consensus. The process begins with artifact intake and initial documentation, followed by non-invasive imaging and chemical testing. Parallel provenance research and comparative stylistic analysis are conducted by separate teams. Findings are compiled into a preliminary report, which undergoes peer review before scheduling an expert panel discussion. Upon consensus, a final authentication certificate is issued. The process also includes dispute resolution and archival storage of all documentation for future reference, ensuring traceability and integrity of artifact validation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Artifact_Intake = Transition(label='Artifact Intake')
Initial_Docs = Transition(label='Initial Docs')
Material_Scan = Transition(label='Material Scan')
Chemical_Test = Transition(label='Chemical Test')
Provenance_Check = Transition(label='Provenance Check')
Stylistic_Review = Transition(label='Stylistic Review')
Parallel_Research = Transition(label='Parallel Research')
Prelim_Report = Transition(label='Prelim Report')
Peer_Review = Transition(label='Peer Review')
Panel_Meeting = Transition(label='Panel Meeting')
Consensus_Vote = Transition(label='Consensus Vote')
Certificate_Issue = Transition(label='Certificate Issue')
Dispute_Handling = Transition(label='Dispute Handling')
Archival_Storage = Transition(label='Archival Storage')
Follow_up_Audit = Transition(label='Follow-up Audit')

# Step 1: Artifact Intake -> Initial Docs
step1 = StrictPartialOrder(nodes=[Artifact_Intake, Initial_Docs])
step1.order.add_edge(Artifact_Intake, Initial_Docs)

# Step 2: Non-invasive imaging and chemical testing concurrent:
step2 = StrictPartialOrder(nodes=[Material_Scan, Chemical_Test])
# no order edges -> concurrent

# Step 3: Parallel provenance research and comparative stylistic analysis concurrent:
step3 = StrictPartialOrder(nodes=[Provenance_Check, Stylistic_Review])
# no edges -> concurrent

# Step 4: Combine step3 results into Parallel Research activity (since description calls it a team)
# Instead of combining them into a single node directly, join these two concurrent activities with 
# a 'Parallel Research' node after they finish.
# So make order: Provenance_Check and Stylistic_Review both precede Parallel_Research

step3_and_research = StrictPartialOrder(
    nodes=[Provenance_Check, Stylistic_Review, Parallel_Research]
)
step3_and_research.order.add_edge(Provenance_Check, Parallel_Research)
step3_and_research.order.add_edge(Stylistic_Review, Parallel_Research)

# Step 5: Preliminary report after step2 and step3_and_research:
# step2 and step3_and_research are concurrent groups -> need to join before Prelim_Report

step5_nodes = [step2, step3_and_research, Prelim_Report]

# To build partial order including these StrictPartialOrders as nodes, flatten them properly:
# According to pm4py, nodes are Transition or OperatorPOWL or StrictPartialOrder objects.
# We'll keep step2 and step3_and_research as nodes in next StrictPartialOrder.

step5 = StrictPartialOrder(nodes=step5_nodes)
# Both step2 and step3_and_research must finish before Prelim_Report
step5.order.add_edge(step2, Prelim_Report)
step5.order.add_edge(step3_and_research, Prelim_Report)

# Step 6: Peer Review after Prelim Report
step6 = StrictPartialOrder(nodes=[Prelim_Report, Peer_Review])
step6.order.add_edge(Prelim_Report, Peer_Review)

# Step 7: Panel Meeting after Peer Review
step7 = StrictPartialOrder(nodes=[Peer_Review, Panel_Meeting])
step7.order.add_edge(Peer_Review, Panel_Meeting)

# Step 8: Consensus Vote after Panel Meeting
step8 = StrictPartialOrder(nodes=[Panel_Meeting, Consensus_Vote])
step8.order.add_edge(Panel_Meeting, Consensus_Vote)

# Step 9: Certificate Issue after Consensus Vote
step9 = StrictPartialOrder(nodes=[Consensus_Vote, Certificate_Issue])
step9.order.add_edge(Consensus_Vote, Certificate_Issue)

# Step 10: Dispute Handling and Follow-up Audit are alternative paths after Certificate Issue
# Either we have disputes that go through Dispute Handling or skip to Follow-up Audit (or both)?
# The description includes dispute resolution and archival storage ensuring traceability.
# The dispute handling likely happens after Certificate Issue if disputes occur,
# Possibly it's a choice followed by archival storage in every case.

# We'll model Dispute Handling and Follow-up Audit as choices post Certificate Issue.
# Archival Storage likely happens regardless after these.

# Let's create a choice between:
# X(Dispute_Handling then Follow_up_Audit, Follow_up_Audit alone)

# Model "Dispute Handling then Follow-up Audit" sequence
dispute_seq = StrictPartialOrder(nodes=[Dispute_Handling, Follow_up_Audit])
dispute_seq.order.add_edge(Dispute_Handling, Follow_up_Audit)

# Choice between dispute_seq and Follow_up_Audit alone
post_certificate_choice = OperatorPOWL(operator=Operator.XOR, children=[dispute_seq, Follow_up_Audit])

# Archival Storage after choice
final_seq = StrictPartialOrder(nodes=[post_certificate_choice, Archival_Storage])
final_seq.order.add_edge(post_certificate_choice, Archival_Storage)

# Now link Certificate Issue to final_seq
final_part = StrictPartialOrder(nodes=[Certificate_Issue, final_seq])
final_part.order.add_edge(Certificate_Issue, final_seq)

# Now build the overall sequence by linking all parts stepwise:
# Steps: step1 -> step2 -> step5 -> step6 -> step7 -> step8 -> step9 (Certificate Issue) -> final_seq

# Wait, step1 had [Artifact Intake, Initial Docs], step2 is concurrent non-invasive imaging steps,
# actually step2 should come after step1 in overall order.

# Steps summary:
# step1 done first
# step2 concurrent activities after step1's Initial Docs finish?
# Description: process begins with artifact intake and initial documentation, followed by non-invasive imaging and chemical testing.

# So step1 is sequential, then step2, then step3_and_research, then Prelim_Report etc.

# But step5 includes step2 and step3_and_research with Prelim_Report.

# So the order is:
# step1 -> step5 -> step6 -> step7 -> step8 -> step9 -> final_part

# We'll combine step1 and step5 in a big StrictPartialOrder with order edges.

# Because step5 includes step2 and step3_and_research inside.

# Construct whole process:

root_nodes = [step1, step5, step6, step7, step8, step9, final_part]

root = StrictPartialOrder(nodes=root_nodes)

root.order.add_edge(step1, step5)     # Step1 before Step5
root.order.add_edge(step5, step6)     # Step5 before Peer Review
root.order.add_edge(step6, step7)     # Peer Review before Panel Meeting
root.order.add_edge(step7, step8)     # Panel Meeting before Consensus Vote
root.order.add_edge(step8, step9)     # Consensus Vote before Certificate Issue
root.order.add_edge(step9, final_part) # Certificate Issue before final handling

# This completes the model.