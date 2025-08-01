# Generated from: 24aaa3ff-58f6-4583-9386-e6983494d109.json
# Description: This process outlines the collaborative patent filing workflow in a multinational corporation involving cross-departmental coordination. It begins with invention disclosure and proceeds through prior art search, legal review, and strategic claim drafting. The workflow integrates iterative feedback loops among R&D, legal, and marketing teams to refine patent scope and applicability. Following internal approvals, the application undergoes formatting, electronic submission, and formal examination request. Post-filing, monitoring competitor filings and managing office actions ensure sustained patent prosecution. The process demands careful version control, confidentiality maintenance, and timely compliance with jurisdiction-specific regulations, culminating in patent grant and portfolio integration for commercialization support.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities
inv_disc         = Transition(label='Invention Disclose')
prior_art        = Transition(label='Prior Art')
legal_rev        = Transition(label='Legal Review')
claim_draft      = Transition(label='Claim Drafting')
team_feedback    = Transition(label='Team Feedback')
scope_refine     = Transition(label='Scope Refinement')
version_ctrl     = Transition(label='Version Control')
confidentiality  = Transition(label='Confidentiality')
compliance_check = Transition(label='Compliance Check')
internal_approve = Transition(label='Internal Approve')
doc_format       = Transition(label='Doc Formatting')
e_submit         = Transition(label='E-Submit')
exam_request     = Transition(label='Exam Request')
competitor_watch = Transition(label='Competitor Watch')
office_action    = Transition(label='Office Action')
patent_grant     = Transition(label='Patent Grant')
portfolio_add    = Transition(label='Portfolio Add')

# Sequence for iterative feedback & refinement
refine_seq = StrictPartialOrder(nodes=[
    team_feedback,
    scope_refine,
    version_ctrl,
    confidentiality,
    compliance_check
])
refine_seq.order.add_edge(team_feedback,    scope_refine)
refine_seq.order.add_edge(scope_refine,     version_ctrl)
refine_seq.order.add_edge(version_ctrl,     confidentiality)
refine_seq.order.add_edge(confidentiality,  compliance_check)

# Loop around claim drafting with feedback/refinement
refinement_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[claim_draft, refine_seq]
)

# Loop for post-filing monitoring and office actions
comp_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[competitor_watch, office_action]
)

# Top‐level workflow partial order
root = StrictPartialOrder(nodes=[
    inv_disc,
    prior_art,
    legal_rev,
    refinement_loop,
    internal_approve,
    doc_format,
    e_submit,
    exam_request,
    comp_loop,
    patent_grant,
    portfolio_add
])
# Define the control-flow order
root.order.add_edge(inv_disc,         prior_art)
root.order.add_edge(prior_art,        legal_rev)
root.order.add_edge(legal_rev,        refinement_loop)
root.order.add_edge(refinement_loop,  internal_approve)
root.order.add_edge(internal_approve, doc_format)
root.order.add_edge(doc_format,       e_submit)
root.order.add_edge(e_submit,         exam_request)
root.order.add_edge(exam_request,     comp_loop)
root.order.add_edge(comp_loop,        patent_grant)
root.order.add_edge(patent_grant,     portfolio_add)