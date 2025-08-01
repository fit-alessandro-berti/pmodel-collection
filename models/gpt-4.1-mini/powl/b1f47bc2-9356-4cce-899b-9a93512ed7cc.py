# Generated from: b1f47bc2-9356-4cce-899b-9a93512ed7cc.json
# Description: This process involves cross-disciplinary teams from different organizations working together to ideate, prototype, test, and refine a novel product concept in a highly iterative manner. It begins with opportunity identification and moves through co-creation workshops, rapid prototyping, and multi-stage validation involving customers and stakeholders. The process requires dynamic resource allocation, continuous feedback loops, and risk assessment at every stage to ensure alignment with strategic goals and market viability. The final stages include joint intellectual property agreements, pilot deployment, and knowledge transfer sessions to embed innovations into operational frameworks.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Opportunity_Scan = Transition(label='Opportunity Scan')
Stakeholder_Map = Transition(label='Stakeholder Map')
Idea_Workshop = Transition(label='Idea Workshop')
Concept_Draft = Transition(label='Concept Draft')
Resource_Align = Transition(label='Resource Align')
Prototype_Build = Transition(label='Prototype Build')
User_Testing = Transition(label='User Testing')
Feedback_Loop = Transition(label='Feedback Loop')
Risk_Review = Transition(label='Risk Review')
Design_Iterate = Transition(label='Design Iterate')
IP_Negotiation = Transition(label='IP Negotiation')
Pilot_Launch = Transition(label='Pilot Launch')
Market_Monitor = Transition(label='Market Monitor')
Knowledge_Share = Transition(label='Knowledge Share')
Scale_Plan = Transition(label='Scale Plan')
Performance_Audit = Transition(label='Performance Audit')

# Model the iterative core with a loop:
# Loop body: Prototype_Build -> User_Testing -> Feedback_Loop (a silent to represent decision) -> Risk_Review -> Design_Iterate
# After Design_Iterate, loop back for next iteration or exit loop to proceed to final stages.
# We'll model the loop as LOOP(A,B): execute A, then optionally B then A again, until exit.
# In this context:
# A = Prototype_Build -> User_Testing -> Feedback_Loop -> Risk_Review -> Design_Iterate (sequential PO)
# B = SilentTransition to represent "go back" (loop continuation)
prototype_seq = StrictPartialOrder(nodes=[
    Prototype_Build, User_Testing, Feedback_Loop, Risk_Review, Design_Iterate
])
prototype_seq.order.add_edge(Prototype_Build, User_Testing)
prototype_seq.order.add_edge(User_Testing, Feedback_Loop)
prototype_seq.order.add_edge(Feedback_Loop, Risk_Review)
prototype_seq.order.add_edge(Risk_Review, Design_Iterate)

loop_body = prototype_seq
loop_continue = SilentTransition()

iterative_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_continue])

# Initial stages partial order:
# Opportunity_Scan and Stakeholder_Map can be concurrent (both "scan" and "mapping")
# These then flow into Idea_Workshop and Concept_Draft (these sequentially)
initial_PO = StrictPartialOrder(nodes=[Opportunity_Scan, Stakeholder_Map, Idea_Workshop, Concept_Draft, Resource_Align])
# Add order edges: Opportunity_Scan --> Idea_Workshop, Stakeholder_Map --> Idea_Workshop
initial_PO.order.add_edge(Opportunity_Scan, Idea_Workshop)
initial_PO.order.add_edge(Stakeholder_Map, Idea_Workshop)
# Idea_Workshop --> Concept_Draft --> Resource_Align
initial_PO.order.add_edge(Idea_Workshop, Concept_Draft)
initial_PO.order.add_edge(Concept_Draft, Resource_Align)

# Resource_Align precedes iterative_loop (dynamic resource allocation before prototyping/testing loop)
# Model final stages after loop:
# IP_Negotiation -> Pilot_Launch -> Market_Monitor and Knowledge_Share can be concurrent
# Both then precede Scale_Plan -> Performance_Audit (final audit)
final_stages_PO = StrictPartialOrder(nodes=[
    IP_Negotiation, Pilot_Launch, Market_Monitor, Knowledge_Share, Scale_Plan, Performance_Audit
])
final_stages_PO.order.add_edge(IP_Negotiation, Pilot_Launch)
final_stages_PO.order.add_edge(Pilot_Launch, Market_Monitor)
final_stages_PO.order.add_edge(Pilot_Launch, Knowledge_Share)
final_stages_PO.order.add_edge(Market_Monitor, Scale_Plan)
final_stages_PO.order.add_edge(Knowledge_Share, Scale_Plan)
final_stages_PO.order.add_edge(Scale_Plan, Performance_Audit)

# Combine initial_PO, Resource_Align, iterative_loop, final_stages_PO all into one PO
# Note Resource_Align, iterative_loop, final_stages_PO are partially ordered among themselves and with initial_PO
root_nodes = [
    Opportunity_Scan, Stakeholder_Map, Idea_Workshop, Concept_Draft, Resource_Align,
    iterative_loop,
    IP_Negotiation, Pilot_Launch, Market_Monitor, Knowledge_Share, Scale_Plan, Performance_Audit
]

root = StrictPartialOrder(nodes=root_nodes)

# Initial_PO edges
root.order.add_edge(Opportunity_Scan, Idea_Workshop)
root.order.add_edge(Stakeholder_Map, Idea_Workshop)
root.order.add_edge(Idea_Workshop, Concept_Draft)
root.order.add_edge(Concept_Draft, Resource_Align)

# Resource_Align precedes loop
root.order.add_edge(Resource_Align, iterative_loop)

# Add edges inside iterative_loop are handled internally by OperatorPOWL and prototype_seq, so no external edges here.

# Loop finishes before IP_Negotiation
root.order.add_edge(iterative_loop, IP_Negotiation)

# Final stages edges
root.order.add_edge(IP_Negotiation, Pilot_Launch)
root.order.add_edge(Pilot_Launch, Market_Monitor)
root.order.add_edge(Pilot_Launch, Knowledge_Share)
root.order.add_edge(Market_Monitor, Scale_Plan)
root.order.add_edge(Knowledge_Share, Scale_Plan)
root.order.add_edge(Scale_Plan, Performance_Audit)