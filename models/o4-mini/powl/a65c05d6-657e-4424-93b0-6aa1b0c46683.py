# Generated from: a65c05d6-657e-4424-93b0-6aa1b0c46683.json
# Description: This process coordinates a decentralized network of subject matter experts (SMEs) who provide real-time consultancy for complex, niche problems across diverse industries. It begins with client intake and problem classification, followed by automated expert matching using AI-driven profiles. Experts collaborate asynchronously and synchronously to diagnose issues, propose solutions, and validate outcomes. The system integrates feedback loops to refine expert recommendations and continuously update profiles based on performance metrics. Additionally, it handles dynamic scheduling, multi-channel communications, and secure document exchanges. The process concludes with quality assurance reviews and client satisfaction assessments, ensuring that the network evolves through adaptive learning and trust-building among participants.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
client_intake     = Transition(label="Client Intake")
problem_classify  = Transition(label="Problem Classify")
expert_match      = Transition(label="Expert Match")
collaborate_async = Transition(label="Collaborate Async")
schedule_sync     = Transition(label="Schedule Sync")
issue_diagnose    = Transition(label="Issue Diagnose")
solution_propose  = Transition(label="Solution Propose")
secure_exchange   = Transition(label="Secure Exchange")
validate_outcome  = Transition(label="Validate Outcome")
feedback_loop     = Transition(label="Feedback Loop")
profile_update    = Transition(label="Profile Update")
quality_review    = Transition(label="Quality Review")
client_assess     = Transition(label="Client Assess")
trust_build       = Transition(label="Trust Build")
adaptive_learn    = Transition(label="Adaptive Learn")

# Main loop body (A): match experts, collaborate, diagnose, propose, exchange, validate
A = StrictPartialOrder(nodes=[
    expert_match,
    collaborate_async,
    schedule_sync,
    issue_diagnose,
    solution_propose,
    secure_exchange,
    validate_outcome
])
A.order.add_edge(expert_match,      collaborate_async)
A.order.add_edge(expert_match,      schedule_sync)
A.order.add_edge(collaborate_async, issue_diagnose)
A.order.add_edge(schedule_sync,     issue_diagnose)
A.order.add_edge(issue_diagnose,    solution_propose)
A.order.add_edge(solution_propose,  secure_exchange)
A.order.add_edge(secure_exchange,   validate_outcome)

# Loop continuation (B): feedback and profile update
B = StrictPartialOrder(nodes=[feedback_loop, profile_update])
B.order.add_edge(feedback_loop, profile_update)

# LOOP operator: do A once, then optionally repeat B + A until exit
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Root partial order for the entire process
root = StrictPartialOrder(nodes=[
    client_intake,
    problem_classify,
    loop_node,
    quality_review,
    client_assess,
    trust_build,
    adaptive_learn
])
root.order.add_edge(client_intake,    problem_classify)
root.order.add_edge(problem_classify, loop_node)
root.order.add_edge(loop_node,        quality_review)
root.order.add_edge(quality_review,   client_assess)
root.order.add_edge(client_assess,    trust_build)
root.order.add_edge(client_assess,    adaptive_learn)