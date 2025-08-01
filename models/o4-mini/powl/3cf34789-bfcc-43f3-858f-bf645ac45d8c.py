# Generated from: 3cf34789-bfcc-43f3-858f-bf645ac45d8c.json
# Description: This process manages the identification, evaluation, and integration of breakthrough technologies from unrelated industries into existing business models. It begins with cross-sector scouting to discover novel ideas outside the company’s domain, followed by multidisciplinary feasibility analysis involving experts from various fields. The process continues with iterative prototyping and pilot testing in controlled environments, ensuring adaptability and scalability. Strategic partnerships are established to leverage external capabilities and intellectual property. Market simulation and risk assessment are conducted concurrently to anticipate potential challenges. Finally, the process culminates in phased rollout plans and continuous feedback loops to refine the innovation and maximize impact across multiple business units, fostering sustained competitive advantage through unconventional innovation sources.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
idea_scouting      = Transition(label='Idea Scouting')
tech_screening    = Transition(label='Tech Screening')
feasibility_review = Transition(label='Feasibility Review')
expert_panel      = Transition(label='Expert Panel')
concept_modeling  = Transition(label='Concept Modeling')
partner_sourcing  = Transition(label='Partner Sourcing')
ip_analysis       = Transition(label='IP Analysis')
risk_mapping      = Transition(label='Risk Mapping')
market_testing    = Transition(label='Market Testing')
prototyping       = Transition(label='Prototyping')
pilot_launch      = Transition(label='Pilot Launch')
scale_planning    = Transition(label='Scale Planning')
rollout_phase     = Transition(label='Rollout Phase')
performance_tracking = Transition(label='Performance Tracking')
feedback_loop     = Transition(label='Feedback Loop')
impact_review     = Transition(label='Impact Review')

# Concurrent feasibility analysis
feasibility_analysis = StrictPartialOrder(
    nodes=[feasibility_review, expert_panel]
)

# Concurrent partnerships and IP analysis
partnerships_ip = StrictPartialOrder(
    nodes=[partner_sourcing, ip_analysis]
)

# Concurrent risk and market assessment
risk_market = StrictPartialOrder(
    nodes=[risk_mapping, market_testing]
)

# Iterative prototyping loop
iterative_test_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[prototyping, pilot_launch]
)

# Concurrent monitoring and review after rollout
post_rollout_review = StrictPartialOrder(
    nodes=[performance_tracking, feedback_loop, impact_review]
)

# Root model
root = StrictPartialOrder(
    nodes=[
        idea_scouting,
        tech_screening,
        feasibility_analysis,
        concept_modeling,
        partnerships_ip,
        risk_market,
        iterative_test_loop,
        scale_planning,
        rollout_phase,
        post_rollout_review
    ]
)

# Define the partial order edges
root.order.add_edge(idea_scouting, tech_screening)
root.order.add_edge(tech_screening, feasibility_analysis)
root.order.add_edge(feasibility_analysis, concept_modeling)
root.order.add_edge(concept_modeling, partnerships_ip)
root.order.add_edge(partnerships_ip, risk_market)
root.order.add_edge(risk_market, iterative_test_loop)
root.order.add_edge(iterative_test_loop, scale_planning)
root.order.add_edge(scale_planning, rollout_phase)
root.order.add_edge(rollout_phase, post_rollout_review)