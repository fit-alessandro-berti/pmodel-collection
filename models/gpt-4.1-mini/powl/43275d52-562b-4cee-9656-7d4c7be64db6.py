# Generated from: 43275d52-562b-4cee-9656-7d4c7be64db6.json
# Description: This process integrates diverse industry insights to foster breakthrough innovations by combining unconventional resources and knowledge. It begins with trend extraction from unrelated sectors, followed by ideation sessions involving multidisciplinary teams. Prototypes are rapidly developed using agile sprints and are then evaluated through simulated market conditions and real-time feedback loops. Concurrently, intellectual property scouting ensures unique solution protection, while strategic partnerships are formed to leverage external capabilities. The process concludes with scaled pilot deployments and post-launch adaptability reviews, facilitating continuous evolution and competitive advantage in volatile markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Trend_Scan = Transition(label='Trend Scan')
Idea_Harvest = Transition(label='Idea Harvest')
Team_Align = Transition(label='Team Align')
Prototype_Build = Transition(label='Prototype Build')
Sprint_Review = Transition(label='Sprint Review')
Market_Simulate = Transition(label='Market Simulate')
Feedback_Loop = Transition(label='Feedback Loop')
IP_Scouting = Transition(label='IP Scouting')
Partner_Vetting = Transition(label='Partner Vetting')
Capability_Merge = Transition(label='Capability Merge')
Pilot_Deploy = Transition(label='Pilot Deploy')
Adapt_Review = Transition(label='Adapt Review')
Risk_Assess = Transition(label='Risk Assess')
Resource_Shift = Transition(label='Resource Shift')
Scale_Plan = Transition(label='Scale Plan')
Innovation_Audit = Transition(label='Innovation Audit')

# Loop for sprints: Prototype Build followed by Sprint Review, repeated with evaluation via Market Simulate and Feedback Loop
# Model feedback loop as a loop with condition exit

# Loop body:
# A = Prototype Build + Sprint Review (partial order)
# B = Market Simulate + Feedback Loop (concurrent)
# After B, loop again to A or exit

# Construct partial order for Prototype Build and Sprint Review (sequential)
prototype_sprint = StrictPartialOrder(nodes=[Prototype_Build, Sprint_Review])
prototype_sprint.order.add_edge(Prototype_Build, Sprint_Review)

# Concurrent evaluation nodes: Market Simulate and Feedback Loop
evaluation = StrictPartialOrder(nodes=[Market_Simulate, Feedback_Loop])

# Loop: (Prototype Build + Sprint Review), then either exit or do (Market Simulate + Feedback Loop) followed by loop again
loop_sprint = OperatorPOWL(operator=Operator.LOOP, children=[prototype_sprint, evaluation])

# Concurrent intellectual property scouting and partnerships preparation (IP Scouting, Partner Vetting)
ip_partners = StrictPartialOrder(nodes=[IP_Scouting, Partner_Vetting])  # concurrent

# Then Capability Merge after IP Scouting and Partner Vetting
capability_merge = Capability_Merge

ip_partners_cap_merge = StrictPartialOrder(nodes=[ip_partners, capability_merge])
ip_partners_cap_merge.order.add_edge(ip_partners, capability_merge)

# Concurrently with the sprint loop, IP scouting and partners+capability merge run
concurrent_mid = StrictPartialOrder(nodes=[loop_sprint, ip_partners_cap_merge])  # no order between them means concurrent

# Pilot deploy and Adapt Review are sequential after concurrent mid activities
deploy_adapt = StrictPartialOrder(nodes=[Pilot_Deploy, Adapt_Review])
deploy_adapt.order.add_edge(Pilot_Deploy, Adapt_Review)

# Risk Assess, Resource Shift, Scale Plan, Innovation Audit come after Adapt Review sequentially
post_adapt_seq = StrictPartialOrder(nodes=[Risk_Assess, Resource_Shift, Scale_Plan, Innovation_Audit])
post_adapt_seq.order.add_edge(Risk_Assess, Resource_Shift)
post_adapt_seq.order.add_edge(Resource_Shift, Scale_Plan)
post_adapt_seq.order.add_edge(Scale_Plan, Innovation_Audit)

# Combine Pilot Deploy + Adapt Review and Post Adapt sequence into one partial order (all sequential)
deploy_adapt_post = StrictPartialOrder(nodes=[deploy_adapt, post_adapt_seq])
deploy_adapt_post.order.add_edge(deploy_adapt, post_adapt_seq)

# Initial partial order: Trend Scan --> Idea Harvest --> Team Align
initial_seq = StrictPartialOrder(nodes=[Trend_Scan, Idea_Harvest, Team_Align])
initial_seq.order.add_edge(Trend_Scan, Idea_Harvest)
initial_seq.order.add_edge(Idea_Harvest, Team_Align)

# After Team Align, start concurrent mid activities and then sequential deploy/adapt/post adapt
full_process = StrictPartialOrder(
    nodes=[initial_seq, concurrent_mid, deploy_adapt_post]
)
full_process.order.add_edge(initial_seq, concurrent_mid)
full_process.order.add_edge(concurrent_mid, deploy_adapt_post)

root = full_process