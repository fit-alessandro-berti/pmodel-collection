# Generated from: c45d4277-1042-4f37-a771-c3cdb80e84c3.json
# Description: This process outlines the strategic approach for fostering innovation by integrating insights and technologies from multiple unrelated industries. It begins with opportunity scouting through market and technology trend analysis, followed by cross-domain ideation sessions involving experts from diverse fields. Next, rapid prototyping is conducted to validate ideas, utilizing agile methodologies and iterative feedback loops. Concurrent risk assessments and intellectual property evaluations ensure feasibility and protection of innovations. Subsequent activities involve pilot testing in controlled environments, stakeholder alignment workshops, and resource reallocation to support scaling. The process culminates with post-implementation reviews, knowledge dissemination across departments, and continuous monitoring for emergent opportunities, thereby promoting sustainable and disruptive innovation beyond traditional industry boundaries.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
Trend_Scan = Transition(label='Trend Scan')
Opportunity_Map = Transition(label='Opportunity Map')
Expert_Gather = Transition(label='Expert Gather')
Idea_Sprint = Transition(label='Idea Sprint')
Proto_Build = Transition(label='Proto Build')
User_Feedback = Transition(label='User Feedback')
Risk_Review = Transition(label='Risk Review')
IP_Audit = Transition(label='IP Audit')
Pilot_Launch = Transition(label='Pilot Launch')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Resource_Shift = Transition(label='Resource Shift')
Scale_Up = Transition(label='Scale Up')
Impact_Assess = Transition(label='Impact Assess')
Knowledge_Share = Transition(label='Knowledge Share')
Monitor_Trends = Transition(label='Monitor Trends')

# Model construction:

# Beginning sequence: Trend Scan --> Opportunity Map
start_seq = StrictPartialOrder(nodes=[Trend_Scan, Opportunity_Map])
start_seq.order.add_edge(Trend_Scan, Opportunity_Map)

# Cross-domain ideation sessions: Expert Gather --> Idea Sprint
ideation_seq = StrictPartialOrder(nodes=[Expert_Gather, Idea_Sprint])
ideation_seq.order.add_edge(Expert_Gather, Idea_Sprint)

# Rapid prototyping with iterative feedback loops:
# Loop: (Proto Build, User Feedback) 
#   execute Proto Build, then either exit or do User Feedback then Proto Build again, repeated
loop_prototyping = OperatorPOWL(operator=Operator.LOOP, children=[Proto_Build, User_Feedback])

# Concurrent risk assessment and IP audit (concurrent, unordered)
risk_ip = StrictPartialOrder(nodes=[Risk_Review, IP_Audit])  # no order between them = concurrency

# Pilot testing --> Stakeholder Meet --> Resource Shift --> Scale Up (sequential)
pilot_seq_nodes = [Pilot_Launch, Stakeholder_Meet, Resource_Shift, Scale_Up]
pilot_sequence = StrictPartialOrder(nodes=pilot_seq_nodes)
for i in range(len(pilot_seq_nodes) - 1):
    pilot_sequence.order.add_edge(pilot_seq_nodes[i], pilot_seq_nodes[i+1])

# Post-implementation: Impact Assess --> Knowledge Share --> Monitor Trends (sequential)
post_impl_nodes = [Impact_Assess, Knowledge_Share, Monitor_Trends]
post_impl_seq = StrictPartialOrder(nodes=post_impl_nodes)
for i in range(len(post_impl_nodes) -1):
    post_impl_seq.order.add_edge(post_impl_nodes[i], post_impl_nodes[i+1])

# Combine stages in partial order following description:

# After Opportunity Map, do ideation (Expert Gather to Idea Sprint)
# Opportunity Map --> Expert Gather
# Ideation leads into prototyping loop: Idea Sprint --> loop_prototyping (Proto Build/User Feedback loop)
# Concurrent risk_ip can start after Idea Sprint:
# Idea Sprint --> risk_ip (Risk Review, IP Audit concurrent)

# After prototyping and risk_ip, pilot sequence can start:
# loop_prototyping --> Pilot_Launch
# risk_ip --> Pilot_Launch

# After pilot_seq, post implementation sequence:
# Scale Up --> Impact_Assess

# Combine all nodes in one StrictPartialOrder, adding edges accordingly
all_nodes = [
    Trend_Scan, Opportunity_Map,
    Expert_Gather, Idea_Sprint,
    loop_prototyping,
    Risk_Review, IP_Audit,
    pilot_sequence,  # pilot_sequence is a StrictPartialOrder, flatten nodes
    Impact_Assess, Knowledge_Share, Monitor_Trends
]

# We need to flatten pilot_sequence nodes to add them to the top-level nodes list.
# The top-level needs all nodes, including nodes inside StrictPartialOrders and OperatorPOWL.
# So we expand pilot_sequence nodes manually.

# Compose the main top-level nodes list: 
# All atomic transitions + loop_prototyping + pilot_sequence (as nodes inside the top root)
top_nodes = [
    Trend_Scan, Opportunity_Map,
    Expert_Gather, Idea_Sprint,
    loop_prototyping,
    Risk_Review, IP_Audit,
    Pilot_Launch, Stakeholder_Meet, Resource_Shift, Scale_Up,
    Impact_Assess, Knowledge_Share, Monitor_Trends
]

root = StrictPartialOrder(nodes=top_nodes)

# Add edges as described:

# Beginning
root.order.add_edge(Trend_Scan, Opportunity_Map)

# Opportunity Map --> Expert Gather
root.order.add_edge(Opportunity_Map, Expert_Gather)

# Expert Gather --> Idea Sprint
root.order.add_edge(Expert_Gather, Idea_Sprint)

# Idea Sprint --> prototyping loop
root.order.add_edge(Idea_Sprint, loop_prototyping)

# Idea Sprint --> concurrent risk and IP audit
root.order.add_edge(Idea_Sprint, Risk_Review)
root.order.add_edge(Idea_Sprint, IP_Audit)

# loop_prototyping and risk_ip converge before Pilot Launch:
root.order.add_edge(loop_prototyping, Pilot_Launch)
root.order.add_edge(Risk_Review, Pilot_Launch)
root.order.add_edge(IP_Audit, Pilot_Launch)

# Pilot Launch --> Stakeholder Meet --> Resource Shift --> Scale Up
root.order.add_edge(Pilot_Launch, Stakeholder_Meet)
root.order.add_edge(Stakeholder_Meet, Resource_Shift)
root.order.add_edge(Resource_Shift, Scale_Up)

# Scale Up --> Impact Assess
root.order.add_edge(Scale_Up, Impact_Assess)

# Impact Assess --> Knowledge Share --> Monitor Trends
root.order.add_edge(Impact_Assess, Knowledge_Share)
root.order.add_edge(Knowledge_Share, Monitor_Trends)