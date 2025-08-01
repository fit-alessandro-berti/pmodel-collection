# Generated from: 267c83c0-f51c-4720-848c-5e8736edfa05.json
# Description: This process orchestrates the seamless collaboration of diverse industry sectors to foster breakthrough innovations that leverage unique domain expertise and emerging technologies. Starting from opportunity scouting across unrelated fields, it integrates multidisciplinary ideation sessions followed by rapid prototyping using hybrid resource pools. The process includes iterative feedback loops involving external stakeholders, advanced risk evaluation tailored to unconventional markets, and adaptive regulatory alignment. It culminates in scalable pilot launches and knowledge dissemination to accelerate future innovation cycles, ensuring sustained competitive advantage in volatile environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Opportunity_Scan = Transition(label='Opportunity Scan')
Stakeholder_Map = Transition(label='Stakeholder Map')
Idea_Sprint = Transition(label='Idea Sprint')
Concept_Merge = Transition(label='Concept Merge')
Resource_Align = Transition(label='Resource Align')
Prototype_Build = Transition(label='Prototype Build')
Hybrid_Testing = Transition(label='Hybrid Testing')
Feedback_Loop = Transition(label='Feedback Loop')
Risk_Assess = Transition(label='Risk Assess')
Compliance_Check = Transition(label='Compliance Check')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Capture = Transition(label='Data Capture')
Impact_Review = Transition(label='Impact Review')
Scaling_Plan = Transition(label='Scaling Plan')
Knowledge_Share = Transition(label='Knowledge Share')
Market_Adapt = Transition(label='Market Adapt')

# Build the iterative feedback loop as a LOOP:
# Loop: Body = Feedback_Loop -> Risk_Assess -> Compliance_Check
#      Do = Hybrid_Testing
feedback_body = StrictPartialOrder(nodes=[Feedback_Loop, Risk_Assess, Compliance_Check])
feedback_body.order.add_edge(Feedback_Loop, Risk_Assess)
feedback_body.order.add_edge(Risk_Assess, Compliance_Check)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_body, Hybrid_Testing])

# After loop, Regulatory and Risk are done, then Pilot Launch and Data Capture etc.
# The scaling and knowledge sharing can be concurrent (partial order)

# Ideation and prototyping partial order (before loop)
ideation_proto = StrictPartialOrder(nodes=[Stakeholder_Map, Idea_Sprint, Concept_Merge, Resource_Align, Prototype_Build])
ideation_proto.order.add_edge(Stakeholder_Map, Idea_Sprint)
ideation_proto.order.add_edge(Idea_Sprint, Concept_Merge)
ideation_proto.order.add_edge(Concept_Merge, Resource_Align)
ideation_proto.order.add_edge(Resource_Align, Prototype_Build)

# Hybrid Testing is done repeatedly inside loop, so it is in loop children, skip here

# Connect Opportunity Scan -> ideation_proto
start_and_ideation = StrictPartialOrder(nodes=[Opportunity_Scan, ideation_proto])
start_and_ideation.order.add_edge(Opportunity_Scan, ideation_proto)

# After loop finish, Pilot Launch -> Data Capture
post_loop = StrictPartialOrder(nodes=[Pilot_Launch, Data_Capture, Impact_Review, Scaling_Plan, Knowledge_Share, Market_Adapt])
post_loop.order.add_edge(Pilot_Launch, Data_Capture)
post_loop.order.add_edge(Data_Capture, Impact_Review)
post_loop.order.add_edge(Impact_Review, Scaling_Plan)
post_loop.order.add_edge(Scaling_Plan, Knowledge_Share)
post_loop.order.add_edge(Knowledge_Share, Market_Adapt)

# Compose everything in a big partial order:
# start_and_ideation -> feedback_loop -> post_loop
root = StrictPartialOrder(nodes=[start_and_ideation, feedback_loop, post_loop])
root.order.add_edge(start_and_ideation, feedback_loop)
root.order.add_edge(feedback_loop, post_loop)