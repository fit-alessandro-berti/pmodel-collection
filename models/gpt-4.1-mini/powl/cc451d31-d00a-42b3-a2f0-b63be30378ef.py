# Generated from: cc451d31-d00a-42b3-a2f0-b63be30378ef.json
# Description: This process describes a multi-phase crowdsourced innovation cycle within a large organization aiming to harness external and internal creative ideas. It begins with idea solicitation from diverse participants, followed by automated filtering using AI algorithms. Promising concepts undergo community voting and expert evaluation before entering rapid prototyping. Feedback loops involve iterative testing with targeted user groups and refinement sessions. Successful prototypes are then prepared for pilot launch, including detailed risk assessments and compliance checks. Post-launch, performance data is gathered for impact analysis, and insights feed back into the next innovation cycle to continuously improve idea quality and implementation effectiveness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Idea_Solicitation = Transition(label='Idea Solicitation')
AI_Filtering = Transition(label='AI Filtering')
Community_Voting = Transition(label='Community Voting')
Expert_Review = Transition(label='Expert Review')
Prototype_Build = Transition(label='Prototype Build')
User_Testing = Transition(label='User Testing')
Iterate_Feedback = Transition(label='Iterate Feedback')
Risk_Assess = Transition(label='Risk Assess')
Compliance_Check = Transition(label='Compliance Check')
Pilot_Launch = Transition(label='Pilot Launch')
Performance_Track = Transition(label='Performance Track')
Impact_Analyze = Transition(label='Impact Analyze')
Insight_Gather = Transition(label='Insight Gather')
Cycle_Adjust = Transition(label='Cycle Adjust')
Final_Report = Transition(label='Final Report')

# Rapid prototyping is Prototype_Build followed by a loop of (User_Testing then Iterate_Feedback)
# Loop: Execute User_Testing, then choose to exit or execute Iterate_Feedback then User_Testing again
# So LOOP(User_Testing, Iterate_Feedback)
prototype_loop = OperatorPOWL(operator=Operator.LOOP, children=[User_Testing, Iterate_Feedback])

# Prototype phase is Prototype_Build then the above loop
prototype_phase = StrictPartialOrder(nodes=[Prototype_Build, prototype_loop])
prototype_phase.order.add_edge(Prototype_Build, prototype_loop)

# Prepare for pilot launch is Risk_Assess and Compliance_Check which happen before Pilot_Launch
prep_pilot = StrictPartialOrder(nodes=[Risk_Assess, Compliance_Check, Pilot_Launch])
prep_pilot.order.add_edge(Risk_Assess, Pilot_Launch)
prep_pilot.order.add_edge(Compliance_Check, Pilot_Launch)

# Post launch tracking and analysis sequence: Performance_Track -> Impact_Analyze -> Insight_Gather -> Cycle_Adjust
post_launch = StrictPartialOrder(nodes=[Performance_Track, Impact_Analyze, Insight_Gather, Cycle_Adjust])
post_launch.order.add_edge(Performance_Track, Impact_Analyze)
post_launch.order.add_edge(Impact_Analyze, Insight_Gather)
post_launch.order.add_edge(Insight_Gather, Cycle_Adjust)

# Final report after Cycle_Adjust
final_phase = StrictPartialOrder(nodes=[Cycle_Adjust, Final_Report])
final_phase.order.add_edge(Cycle_Adjust, Final_Report)

# The main flow:
# Idea Solicitation --> AI Filtering --> Community Voting --> Expert Review --> prototype_phase --> prep_pilot --> post_launch --> final_phase

# Compose linear order of the main phases before final report:
main_flow = StrictPartialOrder(nodes=[
    Idea_Solicitation, AI_Filtering, Community_Voting, Expert_Review,
    prototype_phase,
    prep_pilot,
    post_launch,
    final_phase
])

# Add edges to chain nodes in main_flow respecting the sequence
main_flow.order.add_edge(Idea_Solicitation, AI_Filtering)
main_flow.order.add_edge(AI_Filtering, Community_Voting)
main_flow.order.add_edge(Community_Voting, Expert_Review)
main_flow.order.add_edge(Expert_Review, prototype_phase)
main_flow.order.add_edge(prototype_phase, prep_pilot)
main_flow.order.add_edge(prep_pilot, post_launch)
main_flow.order.add_edge(post_launch, final_phase)

root = main_flow