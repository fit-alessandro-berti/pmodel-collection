# Generated from: a67d2465-fefd-4fbf-820c-ab55de0cfdb7.json
# Description: This process describes an atypical yet realistic approach to driving innovation by integrating insights from multiple unrelated industries. It begins with trend spotting and opportunity mapping across sectors, followed by ideation sessions involving cross-disciplinary teams. Concepts undergo rapid prototyping using hybrid technologies, then move to experimental deployment in controlled environments. Feedback loops incorporate data analytics, user behavior studies, and scenario simulations to refine solutions. Strategic partnerships are formed with external experts and startups to accelerate development. Finally, scalable rollouts are planned alongside continuous monitoring to adapt innovations dynamically in response to evolving market and technological landscapes. This cyclical process fosters disruptive breakthroughs by challenging conventional industry boundaries and leveraging diverse knowledge bases.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
trend_spotting    = Transition(label='Trend Spotting')
opportunity_map  = Transition(label='Opportunity Map')
team_assemble    = Transition(label='Team Assemble')
idea_workshop    = Transition(label='Idea Workshop')
tech_hybridize   = Transition(label='Tech Hybridize')
proto_build      = Transition(label='Proto Build')
test_deploy      = Transition(label='Test Deploy')
data_analyze     = Transition(label='Data Analyze')
behavior_study   = Transition(label='Behavior Study')
scenario_sim     = Transition(label='Scenario Sim')
partner_engage   = Transition(label='Partner Engage')
startup_scout    = Transition(label='Startup Scout')
scale_plan       = Transition(label='Scale Plan')
monitor_adapt    = Transition(label='Monitor Adapt')
cycle_repeat     = Transition(label='Cycle Repeat')

# Build the main sequence partial order (the body of the loop)
main_seq = StrictPartialOrder(nodes=[
    trend_spotting, opportunity_map, team_assemble, idea_workshop,
    tech_hybridize, proto_build, test_deploy,
    data_analyze, behavior_study, scenario_sim,
    partner_engage, startup_scout,
    scale_plan, monitor_adapt
])

# Add ordering constraints for the main sequence
main_seq.order.add_edge(trend_spotting, opportunity_map)
main_seq.order.add_edge(opportunity_map, team_assemble)
main_seq.order.add_edge(team_assemble, idea_workshop)
main_seq.order.add_edge(idea_workshop, tech_hybridize)
main_seq.order.add_edge(tech_hybridize, proto_build)
main_seq.order.add_edge(proto_build, test_deploy)

# After Test Deploy, the three analysis tasks run (concurrently with respect to each other)
main_seq.order.add_edge(test_deploy, data_analyze)
main_seq.order.add_edge(test_deploy, behavior_study)
main_seq.order.add_edge(test_deploy, scenario_sim)

# After each analysis task finishes, partnerships can proceed
for src in [data_analyze, behavior_study, scenario_sim]:
    main_seq.order.add_edge(src, partner_engage)
    main_seq.order.add_edge(src, startup_scout)

# Partnerships (Partner Engage, Startup Scout) flow into rollout planning
main_seq.order.add_edge(partner_engage, scale_plan)
main_seq.order.add_edge(startup_scout, scale_plan)

# Rollout planning and monitoring
main_seq.order.add_edge(scale_plan, monitor_adapt)

# Define the loop: execute main_seq, then optionally do 'Cycle Repeat' before re-running main_seq
loop = OperatorPOWL(operator=Operator.LOOP, children=[main_seq, cycle_repeat])

# The root of the POWL model
root = loop