# Generated from: 9e7179a4-900a-48b3-8e1b-3a0b74893867.json
# Description: This process involves leveraging a global community of experts and enthusiasts to validate the novelty and feasibility of patent applications before formal submission. It includes initial patent idea submission, community voting, expert reviews, iterative feedback incorporation, and final consensus reporting. This crowdsourced approach reduces the risk of patent rejections and improves patent quality by integrating diverse perspectives early in the patent lifecycle. The process also manages intellectual property confidentiality through secure channels and anonymizes contributor identities to mitigate bias, ultimately creating a collaborative yet controlled environment for innovation validation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
IdeaSubmit = Transition(label='Idea Submit')
PreliminaryCheck = Transition(label='Preliminary Check')
CommunityVote = Transition(label='Community Vote')
ExpertAssign = Transition(label='Expert Assign')
ReviewDraft = Transition(label='Review Draft')
FeedbackGather = Transition(label='Feedback Gather')
IterateRevision = Transition(label='Iterate Revision')
ConfidentialityLock = Transition(label='Confidentiality Lock')
BiasAudit = Transition(label='Bias Audit')
ConsensusScore = Transition(label='Consensus Score')
FinalReport = Transition(label='Final Report')
LegalReview = Transition(label='Legal Review')
SubmissionPrep = Transition(label='Submission Prep')
ComplianceCheck = Transition(label='Compliance Check')
ArchiveRecords = Transition(label='Archive Records')

# Loop for iterative feedback incorporation:
# Loop(Do ReviewDraft, FeedbackGather; Loop exit or iterate revision again)
# Loop(A,B) = execute A, then choose to exit or do B and again A..
review_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[ReviewDraft, FeedbackGather])

# The iteration: once feedback gathered, user can either exit loop or do IterateRevision then ReviewDraft again
# So in loop terms:
# A = ReviewDraft
# B = FeedbackGather + IterateRevision
# But OperatorPOWL.LOOP uses 2 children only: A, B.
# So we must model B as FeedbackGather followed by IterateRevision sequentially.
# We'll build a PO for B: FeedbackGather --> IterateRevision
B_loop = StrictPartialOrder(nodes=[FeedbackGather, IterateRevision])
B_loop.order.add_edge(FeedbackGather, IterateRevision)

review_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[ReviewDraft, B_loop])

# Community validation phase after preliminary check:
# CommunityVote and ExpertAssign happen in parallel (no order specified)
# After ExpertAssign, review_feedback_loop happens
# So ExpertAssign must precede review_feedback_loop; CommunityVote concurrent

community_validation = StrictPartialOrder(
    nodes=[CommunityVote, ExpertAssign, review_feedback_loop]
)
community_validation.order.add_edge(ExpertAssign, review_feedback_loop)

# ConfidentialityLock and BiasAudit together: concurrency (parallel)
confidentiality_bias = StrictPartialOrder(nodes=[ConfidentialityLock, BiasAudit])

# ConsensusScore after community validation and confidentiality/bias audit both finish
consensus_score = ConsensusScore
# FinalReport after consensus score
final_report = FinalReport

# Legal Review, Submission Prep, Compliance Check in sequence after FinalReport
legal_submission_seq = StrictPartialOrder(
    nodes=[LegalReview, SubmissionPrep, ComplianceCheck]
)
legal_submission_seq.order.add_edge(LegalReview, SubmissionPrep)
legal_submission_seq.order.add_edge(SubmissionPrep, ComplianceCheck)

# ArchiveRecords last

# Assemble the whole process partial order:

# Start with IdeaSubmit -> PreliminaryCheck
# PreliminaryCheck -> community_validation and confidentiality_bias (in parallel)
# both must finish before ConsensusScore
# ConsensusScore -> FinalReport -> legal_submission_seq -> ArchiveRecords

root = StrictPartialOrder(
    nodes=[
        IdeaSubmit,
        PreliminaryCheck,
        community_validation,
        confidentiality_bias,
        consensus_score,
        final_report,
        legal_submission_seq,
        ArchiveRecords,
    ]
)

root.order.add_edge(IdeaSubmit, PreliminaryCheck)
root.order.add_edge(PreliminaryCheck, community_validation)
root.order.add_edge(PreliminaryCheck, confidentiality_bias)

root.order.add_edge(community_validation, consensus_score)
root.order.add_edge(confidentiality_bias, consensus_score)

root.order.add_edge(consensus_score, final_report)

root.order.add_edge(final_report, legal_submission_seq)

root.order.add_edge(legal_submission_seq, ArchiveRecords)