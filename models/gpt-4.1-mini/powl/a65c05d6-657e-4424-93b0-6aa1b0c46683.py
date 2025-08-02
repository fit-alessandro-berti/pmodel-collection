# Generated from: a65c05d6-657e-4424-93b0-6aa1b0c46683.json
# Description: This process coordinates a decentralized network of subject matter experts (SMEs) who provide real-time consultancy for complex, niche problems across diverse industries. It begins with client intake and problem classification, followed by automated expert matching using AI-driven profiles. Experts collaborate asynchronously and synchronously to diagnose issues, propose solutions, and validate outcomes. The system integrates feedback loops to refine expert recommendations and continuously update profiles based on performance metrics. Additionally, it handles dynamic scheduling, multi-channel communications, and secure document exchanges. The process concludes with quality assurance reviews and client satisfaction assessments, ensuring that the network evolves through adaptive learning and trust-building among participants.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Client_Intake = Transition(label='Client Intake')
Problem_Classify = Transition(label='Problem Classify')
Expert_Match = Transition(label='Expert Match')

Schedule_Sync = Transition(label='Schedule Sync')
Issue_Diagnose = Transition(label='Issue Diagnose')
Solution_Propose = Transition(label='Solution Propose')
Collaborate_Async = Transition(label='Collaborate Async')
Validate_Outcome = Transition(label='Validate Outcome')

Feedback_Loop = Transition(label='Feedback Loop')
Profile_Update = Transition(label='Profile Update')

Secure_Exchange = Transition(label='Secure Exchange')

Quality_Review = Transition(label='Quality Review')
Client_Assess = Transition(label='Client Assess')

Trust_Build = Transition(label='Trust Build')
Adaptive_Learn = Transition(label='Adaptive Learn')

# Model expert collaboration: Concurrency of asynchronous and synchronous parts:
# Here synchronous is Schedule Sync + (Issue Diagnose -> Solution Propose)
# Asynchronous is Collaborate Async
# So compose (Schedule Sync PO Issue Diagnose --> Solution Propose) concurrent with Collaborate Async

# Construct synchronous collaboration partial order
sync_PO = StrictPartialOrder(nodes=[Schedule_Sync, Issue_Diagnose, Solution_Propose])
sync_PO.order.add_edge(Schedule_Sync, Issue_Diagnose)
sync_PO.order.add_edge(Issue_Diagnose, Solution_Propose)

# Collaboration partial order: asynchronous concurrent with synchronous
Collaboration = StrictPartialOrder(nodes=[sync_PO, Collaborate_Async])
# No order edges means async and sync run concurrently

# Feedback loop is a LOOP: execute Feedback Loop then either exit or (Profile Update then Feedback Loop again)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Profile_Update])

# After validate outcome, feedback loop happens to refine recommendations and update profiles
# Model sequence (Validate Outcome --> feedback_loop)

# Communication and secure exchanges can be concurrent to some extent with collaboration,
# but both are in the problem description part of the process after expert match and collaboration.
# We'll model Secure Exchange concurrent with Collaboration & Feedback

# Sequence after Expert Match:
# (Schedule_Sync + Diagnosing-Solution + Collaborate Async concurrent)
# then Validate Outcome
# then feedback loop
# Secure Exchange also runs in parallel with collaboration and feedback

# Model concurrent Collaboration, Secure Exchange and feedback_loop

# Partial order with nodes: Collaboration, Validate_Outcome, feedback_loop, Secure_Exchange
post_match_PO = StrictPartialOrder(nodes=[Collaboration, Validate_Outcome, feedback_loop, Secure_Exchange])
# Collaboration --> Validate_Outcome --> feedback_loop
post_match_PO.order.add_edge(Collaboration, Validate_Outcome)
post_match_PO.order.add_edge(Validate_Outcome, feedback_loop)
# Secure_Exchange concurrent (no order edges added)

# Final stage: Quality Review then Client Assess then concurrent Trust Build and Adaptive Learn

final_review_PO = StrictPartialOrder(
    nodes=[Quality_Review, Client_Assess, Trust_Build, Adaptive_Learn])
final_review_PO.order.add_edge(Quality_Review, Client_Assess)
# Trust Build and Adaptive Learn run concurrently after Client Assess
final_review_PO.order.add_edge(Client_Assess, Trust_Build)
final_review_PO.order.add_edge(Client_Assess, Adaptive_Learn)

# Overall start to end process partial order:
# Client Intake --> Problem Classify --> Expert Match --> post_match_PO --> final_review_PO

root = StrictPartialOrder(nodes=[
    Client_Intake,
    Problem_Classify,
    Expert_Match,
    post_match_PO,
    final_review_PO
])

root.order.add_edge(Client_Intake, Problem_Classify)
root.order.add_edge(Problem_Classify, Expert_Match)
root.order.add_edge(Expert_Match, post_match_PO)
root.order.add_edge(post_match_PO, final_review_PO)