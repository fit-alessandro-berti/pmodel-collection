# Generated from: d196cfd5-bc4d-40e3-bb03-6935395fd0ef.json
# Description: This process outlines the end-to-end coordination of a global remote hackathon involving diverse participants across multiple time zones. It begins with concept ideation and sponsor alignment, followed by participant registration and team formation using AI matchmaking. Next, preparatory workshops are scheduled and delivered virtually. During the hackathon, continuous monitoring, live support, and iterative feedback loops ensure smooth progress. Submission validation and automated plagiarism checks precede jury evaluations conducted via a secure portal. Finally, winners are announced through a synchronized global livestream, and post-event analytics drive future improvements, ensuring an engaging and equitable competition experience for all participants worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Concept_Ideation = Transition(label='Concept Ideation')
Sponsor_Alignment = Transition(label='Sponsor Alignment')
Participant_SignUp = Transition(label='Participant SignUp')
Team_Formation = Transition(label='Team Formation')
Workshop_Setup = Transition(label='Workshop Setup')
Workshop_Delivery = Transition(label='Workshop Delivery')
Progress_Monitor = Transition(label='Progress Monitor')
Live_Support = Transition(label='Live Support')
Feedback_Loop = Transition(label='Feedback Loop')
Submission_Check = Transition(label='Submission Check')
Plagiarism_Scan = Transition(label='Plagiarism Scan')
Jury_Evaluation = Transition(label='Jury Evaluation')
Result_Compilation = Transition(label='Result Compilation')
Winner_Announcement = Transition(label='Winner Announcement')
Post_Analytics = Transition(label='Post Analytics')

# Loop for continuous monitoring, live support, feedback
monitor_live_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Progress_Monitor, OperatorPOWL(operator=Operator.XOR, children=[Live_Support, Feedback_Loop])])

# Workshop setup and delivery sequence
workshops = StrictPartialOrder(nodes=[Workshop_Setup, Workshop_Delivery])
workshops.order.add_edge(Workshop_Setup, Workshop_Delivery)

# Jury evaluation process: submission check -> plagiarism scan -> jury evaluation
jury_eval_seq = StrictPartialOrder(nodes=[Submission_Check, Plagiarism_Scan, Jury_Evaluation])
jury_eval_seq.order.add_edge(Submission_Check, Plagiarism_Scan)
jury_eval_seq.order.add_edge(Plagiarism_Scan, Jury_Evaluation)

# Initial phase: Concept Ideation -> Sponsor Alignment -> (Participant SignUp -> Team Formation)
registration = StrictPartialOrder(nodes=[Participant_SignUp, Team_Formation])
registration.order.add_edge(Participant_SignUp, Team_Formation)

initial_phase = StrictPartialOrder(nodes=[Concept_Ideation, Sponsor_Alignment, registration])
initial_phase.order.add_edge(Concept_Ideation, Sponsor_Alignment)
initial_phase.order.add_edge(Sponsor_Alignment, registration)

# After registration and team formation -> workshops
after_registration = StrictPartialOrder(nodes=[initial_phase, workshops])
after_registration.order.add_edge(initial_phase, workshops)

# After workshops, start monitoring loop
after_workshops = StrictPartialOrder(nodes=[after_registration, monitor_live_feedback_loop])
after_workshops.order.add_edge(after_registration, monitor_live_feedback_loop)

# After loop finishes (loop exits), proceed to jury evaluation
after_monitoring = StrictPartialOrder(nodes=[after_workshops, jury_eval_seq])
after_monitoring.order.add_edge(after_workshops, jury_eval_seq)

# Final sequence: result compilation -> winner announcement -> post analytics
final_seq = StrictPartialOrder(nodes=[Result_Compilation, Winner_Announcement, Post_Analytics])
final_seq.order.add_edge(Result_Compilation, Winner_Announcement)
final_seq.order.add_edge(Winner_Announcement, Post_Analytics)

# After jury evaluation -> final sequence
final_process = StrictPartialOrder(nodes=[after_monitoring, final_seq])
final_process.order.add_edge(after_monitoring, final_seq)

root = final_process