# Generated from: 24aaa3ff-58f6-4583-9386-e6983494d109.json
# Description: This process outlines the collaborative patent filing workflow in a multinational corporation involving cross-departmental coordination. It begins with invention disclosure and proceeds through prior art search, legal review, and strategic claim drafting. The workflow integrates iterative feedback loops among R&D, legal, and marketing teams to refine patent scope and applicability. Following internal approvals, the application undergoes formatting, electronic submission, and formal examination request. Post-filing, monitoring competitor filings and managing office actions ensure sustained patent prosecution. The process demands careful version control, confidentiality maintenance, and timely compliance with jurisdiction-specific regulations, culminating in patent grant and portfolio integration for commercialization support.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Invention_Disclose = Transition(label='Invention Disclose')
Prior_Art = Transition(label='Prior Art')
Legal_Review = Transition(label='Legal Review')
Claim_Drafting = Transition(label='Claim Drafting')
Team_Feedback = Transition(label='Team Feedback')
Scope_Refinement = Transition(label='Scope Refinement')
Internal_Approve = Transition(label='Internal Approve')
Doc_Formatting = Transition(label='Doc Formatting')
E_Submit = Transition(label='E-Submit')
Exam_Request = Transition(label='Exam Request')
Competitor_Watch = Transition(label='Competitor Watch')
Office_Action = Transition(label='Office Action')
Version_Control = Transition(label='Version Control')
Confidentiality = Transition(label='Confidentiality')
Compliance_Check = Transition(label='Compliance Check')
Patent_Grant = Transition(label='Patent Grant')
Portfolio_Add = Transition(label='Portfolio Add')

# Loop for iterative feedback among R&D, Legal, Marketing: 
# (Team Feedback -> Scope Refinement) looped before Internal Approve
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Team_Feedback, Scope_Refinement])

# Define the core sequential order before the loop
# Invention Disclose --> Prior Art --> Legal Review --> Claim Drafting --> feedback_loop --> Internal Approve
# Following that, after Internal Approve is the post-approval sequence and monitoring

# Post approval sequential steps
post_approval_nodes = [
    Doc_Formatting,
    E_Submit,
    Exam_Request,
    # After Exam_Request, continuous monitoring and handling office actions happens concurrently
]
post_approval_po = StrictPartialOrder(nodes=post_approval_nodes)
post_approval_po.order.add_edge(Doc_Formatting, E_Submit)
post_approval_po.order.add_edge(E_Submit, Exam_Request)

# Monitoring loop (Competitor Watch and Office Action) that repeats post filing
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[Competitor_Watch, Office_Action])

# After monitoring loop, final compliance checks and grant additions happen in sequence
final_sequence_nodes = [
    Version_Control,
    Confidentiality,
    Compliance_Check,
    Patent_Grant,
    Portfolio_Add,
]
final_sequence_po = StrictPartialOrder(nodes=final_sequence_nodes)
final_sequence_po.order.add_edge(Version_Control, Confidentiality)
final_sequence_po.order.add_edge(Confidentiality, Compliance_Check)
final_sequence_po.order.add_edge(Compliance_Check, Patent_Grant)
final_sequence_po.order.add_edge(Patent_Grant, Portfolio_Add)

# Concurrently run the monitoring loop and final sequence after Exam Request
post_monitoring_root = StrictPartialOrder(
    nodes=[monitor_loop] + final_sequence_nodes
)
# monitor_loop and Version_Control start concurrently, so no edges between them.
# The final sequence is chained internally, no extra edges needed here.

# Build the full process PO
root = StrictPartialOrder(
    nodes=[
        Invention_Disclose,
        Prior_Art,
        Legal_Review,
        Claim_Drafting,
        feedback_loop,
        Internal_Approve,
        post_approval_po,
        post_monitoring_root,
    ]
)

# Sequential edges from start to post approval PO (treated as one node in nodes)
root.order.add_edge(Invention_Disclose, Prior_Art)
root.order.add_edge(Prior_Art, Legal_Review)
root.order.add_edge(Legal_Review, Claim_Drafting)
root.order.add_edge(Claim_Drafting, feedback_loop)
root.order.add_edge(feedback_loop, Internal_Approve)
root.order.add_edge(Internal_Approve, post_approval_po)
root.order.add_edge(post_approval_po, post_monitoring_root)