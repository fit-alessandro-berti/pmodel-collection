# Generated from: 9e7179a4-900a-48b3-8e1b-3a0b74893867.json
# Description: This process involves leveraging a global community of experts and enthusiasts to validate the novelty and feasibility of patent applications before formal submission. It includes initial patent idea submission, community voting, expert reviews, iterative feedback incorporation, and final consensus reporting. This crowdsourced approach reduces the risk of patent rejections and improves patent quality by integrating diverse perspectives early in the patent lifecycle. The process also manages intellectual property confidentiality through secure channels and anonymizes contributor identities to mitigate bias, ultimately creating a collaborative yet controlled environment for innovation validation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all basic activities
idea_submit       = Transition(label='Idea Submit')
prelim_check      = Transition(label='Preliminary Check')
conf_lock         = Transition(label='Confidentiality Lock')
bias_audit        = Transition(label='Bias Audit')
community_vote    = Transition(label='Community Vote')
expert_assign     = Transition(label='Expert Assign')
review_draft      = Transition(label='Review Draft')
feedback_gather   = Transition(label='Feedback Gather')
iterate_revision  = Transition(label='Iterate Revision')
consensus_score   = Transition(label='Consensus Score')
final_report      = Transition(label='Final Report')
legal_review      = Transition(label='Legal Review')
submission_prep   = Transition(label='Submission Prep')
compliance_check  = Transition(label='Compliance Check')
archive_records   = Transition(label='Archive Records')

# Define the review‐feedback loop:
#   A = Review Draft → Feedback Gather
#   B = Iterate Revision  (then A repeats)
loop_body = StrictPartialOrder(nodes=[review_draft, feedback_gather])
loop_body.order.add_edge(review_draft, feedback_gather)
loop_redo = iterate_revision
review_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_redo])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    idea_submit,
    prelim_check,
    conf_lock,
    bias_audit,
    community_vote,
    expert_assign,
    review_loop,
    consensus_score,
    final_report,
    legal_review,
    submission_prep,
    compliance_check,
    archive_records
])

# Add ordering constraints
root.order.add_edge(idea_submit,      prelim_check)
root.order.add_edge(prelim_check,     conf_lock)
root.order.add_edge(prelim_check,     bias_audit)
root.order.add_edge(conf_lock,        community_vote)
root.order.add_edge(bias_audit,       community_vote)
root.order.add_edge(community_vote,   expert_assign)
root.order.add_edge(expert_assign,    review_loop)
root.order.add_edge(review_loop,      consensus_score)
root.order.add_edge(consensus_score,  final_report)
root.order.add_edge(final_report,     legal_review)
root.order.add_edge(legal_review,     submission_prep)
root.order.add_edge(submission_prep,  compliance_check)
root.order.add_edge(compliance_check, archive_records)