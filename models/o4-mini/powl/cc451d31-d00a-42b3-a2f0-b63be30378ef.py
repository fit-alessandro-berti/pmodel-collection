# Generated from: cc451d31-d00a-42b3-a2f0-b63be30378ef.json
# Description: This process describes a multi-phase crowdsourced innovation cycle within a large organization aiming to harness external and internal creative ideas. It begins with idea solicitation from diverse participants, followed by automated filtering using AI algorithms. Promising concepts undergo community voting and expert evaluation before entering rapid prototyping. Feedback loops involve iterative testing with targeted user groups and refinement sessions. Successful prototypes are then prepared for pilot launch, including detailed risk assessments and compliance checks. Post-launch, performance data is gathered for impact analysis, and insights feed back into the next innovation cycle to continuously improve idea quality and implementation effectiveness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
idea_solicitation = Transition(label='Idea Solicitation')
ai_filtering       = Transition(label='AI Filtering')
community_voting   = Transition(label='Community Voting')
expert_review      = Transition(label='Expert Review')
prototype_build    = Transition(label='Prototype Build')
user_testing       = Transition(label='User Testing')
iterate_feedback   = Transition(label='Iterate Feedback')
risk_assess        = Transition(label='Risk Assess')
compliance_check   = Transition(label='Compliance Check')
pilot_launch       = Transition(label='Pilot Launch')
performance_track  = Transition(label='Performance Track')
impact_analyze     = Transition(label='Impact Analyze')
insight_gather     = Transition(label='Insight Gather')
cycle_adjust       = Transition(label='Cycle Adjust')
final_report       = Transition(label='Final Report')

# Parallel community & expert evaluation
co_review = StrictPartialOrder(nodes=[community_voting, expert_review])
# no order edges ==> they can proceed concurrently

# Feedback loop: user testing then iterate feedback, repeat
loop_feedback = OperatorPOWL(
    operator=Operator.LOOP,
    children=[user_testing, iterate_feedback]
)

# Build the overall workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    idea_solicitation,
    ai_filtering,
    co_review,
    prototype_build,
    loop_feedback,
    risk_assess,
    compliance_check,
    pilot_launch,
    performance_track,
    impact_analyze,
    insight_gather,
    cycle_adjust,
    final_report
])

# Add sequencing constraints
root.order.add_edge(idea_solicitation, ai_filtering)
root.order.add_edge(ai_filtering, co_review)
root.order.add_edge(co_review, prototype_build)
root.order.add_edge(prototype_build, loop_feedback)
root.order.add_edge(loop_feedback, risk_assess)
root.order.add_edge(risk_assess, compliance_check)
root.order.add_edge(compliance_check, pilot_launch)
root.order.add_edge(pilot_launch, performance_track)
root.order.add_edge(performance_track, impact_analyze)
root.order.add_edge(impact_analyze, insight_gather)
root.order.add_edge(insight_gather, cycle_adjust)
root.order.add_edge(cycle_adjust, final_report)