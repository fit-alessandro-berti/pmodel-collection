# Generated from: d196cfd5-bc4d-40e3-bb03-6935395fd0ef.json
# Description: This process outlines the end-to-end coordination of a global remote hackathon involving diverse participants across multiple time zones. It begins with concept ideation and sponsor alignment, followed by participant registration and team formation using AI matchmaking. Next, preparatory workshops are scheduled and delivered virtually. During the hackathon, continuous monitoring, live support, and iterative feedback loops ensure smooth progress. Submission validation and automated plagiarism checks precede jury evaluations conducted via a secure portal. Finally, winners are announced through a synchronized global livestream, and post-event analytics drive future improvements, ensuring an engaging and equitable competition experience for all participants worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
concept_ideation   = Transition(label='Concept Ideation')
sponsor_alignment  = Transition(label='Sponsor Alignment')
participant_signup = Transition(label='Participant SignUp')
team_formation     = Transition(label='Team Formation')
workshop_setup     = Transition(label='Workshop Setup')
workshop_delivery  = Transition(label='Workshop Delivery')
progress_monitor   = Transition(label='Progress Monitor')
live_support       = Transition(label='Live Support')
feedback_loop      = Transition(label='Feedback Loop')
submission_check   = Transition(label='Submission Check')
plagiarism_scan    = Transition(label='Plagiarism Scan')
jury_evaluation    = Transition(label='Jury Evaluation')
result_compilation = Transition(label='Result Compilation')
winner_announcement= Transition(label='Winner Announcement')
post_analytics     = Transition(label='Post Analytics')

# Hackathon iterative monitoring loop: do (monitor -> live support), then optionally feedback -> repeat
loop_body = StrictPartialOrder(nodes=[progress_monitor, live_support])
loop_body.order.add_edge(progress_monitor, live_support)
hackathon_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, feedback_loop])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    concept_ideation,
    sponsor_alignment,
    participant_signup,
    team_formation,
    workshop_setup,
    workshop_delivery,
    hackathon_loop,
    submission_check,
    plagiarism_scan,
    jury_evaluation,
    result_compilation,
    winner_announcement,
    post_analytics
])

# Sequence edges
root.order.add_edge(concept_ideation,   sponsor_alignment)
root.order.add_edge(sponsor_alignment,  participant_signup)
root.order.add_edge(participant_signup, team_formation)
root.order.add_edge(team_formation,     workshop_setup)
root.order.add_edge(workshop_setup,     workshop_delivery)
root.order.add_edge(workshop_delivery,  hackathon_loop)
root.order.add_edge(hackathon_loop,     submission_check)
root.order.add_edge(submission_check,   plagiarism_scan)
root.order.add_edge(plagiarism_scan,    jury_evaluation)
root.order.add_edge(jury_evaluation,    result_compilation)
root.order.add_edge(result_compilation, winner_announcement)
root.order.add_edge(winner_announcement, post_analytics)