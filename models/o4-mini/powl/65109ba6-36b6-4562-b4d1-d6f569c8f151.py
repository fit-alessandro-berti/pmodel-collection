# Generated from: 65109ba6-36b6-4562-b4d1-d6f569c8f151.json
# Description: This process involves leveraging a global community to generate, evaluate, and refine innovative ideas for new product development. It starts by broadcasting challenge themes to a diverse participant base, encouraging submission of novel concepts. These ideas undergo automated and peer review stages to filter feasible proposals. Selected ideas enter prototyping, where rapid virtual models are created and tested using simulation tools. Feedback loops from community experts and end-users drive iterative improvements. Concurrently, intellectual property assessments and market viability analyses are conducted to ensure alignment with strategic goals. Final concepts proceed to a pilot launch phase, coupled with targeted marketing experiments and data collection to validate user engagement and scalability before full-scale production is authorized.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
theme_launch = Transition(label='Theme Launch')
idea_submit = Transition(label='Idea Submit')
auto_filter = Transition(label='Auto Filter')
peer_review = Transition(label='Peer Review')
feasibility_check = Transition(label='Feasibility Check')

prototype_build = Transition(label='Prototype Build')
simulate_test = Transition(label='Simulate Test')
expert_feedback = Transition(label='Expert Feedback')
user_review = Transition(label='User Review')
iterate_design = Transition(label='Iterate Design')

ip_audit = Transition(label='IP Audit')
market_scan = Transition(label='Market Scan')

pilot_launch = Transition(label='Pilot Launch')
data_collect = Transition(label='Data Collect')
scale_approve = Transition(label='Scale Approve')

# Phase A: Prototype Build -> Simulate Test
phaseA = StrictPartialOrder(nodes=[prototype_build, simulate_test])
phaseA.order.add_edge(prototype_build, simulate_test)

# Phase B: Expert Feedback and User Review -> Iterate Design
phaseB = StrictPartialOrder(nodes=[expert_feedback, user_review, iterate_design])
phaseB.order.add_edge(expert_feedback, iterate_design)
phaseB.order.add_edge(user_review, iterate_design)

# Loop: repeat (Phase A) then either exit or do (Phase B) and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[phaseA, phaseB])

# Pilot phase: Pilot Launch -> Data Collect -> Scale Approve
pilot = StrictPartialOrder(nodes=[pilot_launch, data_collect, scale_approve])
pilot.order.add_edge(pilot_launch, data_collect)
pilot.order.add_edge(data_collect, scale_approve)

# Root model combining everything
root = StrictPartialOrder(
    nodes=[
        theme_launch, idea_submit, auto_filter, peer_review, feasibility_check,
        loop, ip_audit, market_scan, pilot
    ]
)

# Control-flow dependencies
root.order.add_edge(theme_launch, idea_submit)
root.order.add_edge(idea_submit, auto_filter)
root.order.add_edge(auto_filter, peer_review)
root.order.add_edge(peer_review, feasibility_check)

# After feasibility check, start the prototyping loop and the IP/market analyses in parallel
root.order.add_edge(feasibility_check, loop)
root.order.add_edge(feasibility_check, ip_audit)
root.order.add_edge(feasibility_check, market_scan)

# Pilot phase starts only after loop, IP audit, and market scan complete
root.order.add_edge(loop, pilot)
root.order.add_edge(ip_audit, pilot)
root.order.add_edge(market_scan, pilot)