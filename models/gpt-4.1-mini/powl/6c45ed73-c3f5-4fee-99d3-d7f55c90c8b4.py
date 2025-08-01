# Generated from: 6c45ed73-c3f5-4fee-99d3-d7f55c90c8b4.json
# Description: This process outlines a cross-industry innovation cycle where ideas from unrelated sectors are systematically extracted, evaluated, and adapted to create novel solutions. The cycle begins with trend scouting across diverse markets, followed by interdisciplinary workshops to generate hybrid concepts. Concepts are then prototyped using agile sprints and validated through multi-sector pilot programs. Feedback loops integrate stakeholder insights from contrasting industries, ensuring robust iteration. Intellectual property strategies are tailored to protect innovations spanning multiple regulatory environments. Finally, strategic partnerships are formed to scale the innovation globally, leveraging complementary distribution channels and joint marketing campaigns. This atypical process fosters breakthrough innovation by embracing complexity and diversity beyond traditional single-sector approaches.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Trend_Scouting = Transition(label='Trend Scouting')
Idea_Harvest = Transition(label='Idea Harvest')
Cross_Workshops = Transition(label='Cross-Workshops')
Concept_Fusion = Transition(label='Concept Fusion')
Rapid_Prototyping = Transition(label='Rapid Prototyping')
Pilot_Testing = Transition(label='Pilot Testing')
Stakeholder_Review = Transition(label='Stakeholder Review')
Feedback_Loop = Transition(label='Feedback Loop')
IP_Strategy = Transition(label='IP Strategy')
Regulatory_Scan = Transition(label='Regulatory Scan')
Partnership_Build = Transition(label='Partnership Build')
Market_Alignment = Transition(label='Market Alignment')
Scaling_Plan = Transition(label='Scaling Plan')
Joint_Marketing = Transition(label='Joint Marketing')
Innovation_Audit = Transition(label='Innovation Audit')

# Sub partial order: Trend Scouting -> Idea Harvest -> Cross-Workshops -> Concept Fusion
phase1 = StrictPartialOrder(nodes=[Trend_Scouting, Idea_Harvest, Cross_Workshops, Concept_Fusion])
phase1.order.add_edge(Trend_Scouting, Idea_Harvest)
phase1.order.add_edge(Idea_Harvest, Cross_Workshops)
phase1.order.add_edge(Cross_Workshops, Concept_Fusion)

# Sub partial order: Rapid Prototyping -> Pilot Testing
phase2 = StrictPartialOrder(nodes=[Rapid_Prototyping, Pilot_Testing])
phase2.order.add_edge(Rapid_Prototyping, Pilot_Testing)

# Loop: (Stakeholder Review, Feedback Loop)
# Means: execute Stakeholder Review then loop:
#   choose to exit or do Feedback Loop then Stakeholder Review again
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[Stakeholder_Review, Feedback_Loop])

# IP Strategy phase: IP Strategy and Regulatory Scan concurrent
ip_phase = StrictPartialOrder(nodes=[IP_Strategy, Regulatory_Scan])  # no order -> concurrent

# Partnership phase: Partnership Build -> (Market Alignment XOR Joint Marketing)
partnership_choice = OperatorPOWL(operator=Operator.XOR, children=[Market_Alignment, Joint_Marketing])
partnership_phase = StrictPartialOrder(nodes=[Partnership_Build, partnership_choice])
partnership_phase.order.add_edge(Partnership_Build, partnership_choice)

# Final phase: Scaling Plan -> Innovation Audit
final_phase = StrictPartialOrder(nodes=[Scaling_Plan, Innovation_Audit])
final_phase.order.add_edge(Scaling_Plan, Innovation_Audit)

# Compose all phases in order with concurrency where suitable:
# The process flow in sequence:
# phase1 -> phase2 -> loop_feedback -> ip_phase -> partnership_phase -> final_phase
root = StrictPartialOrder(nodes=[phase1, phase2, loop_feedback, ip_phase, partnership_phase, final_phase])
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, loop_feedback)
root.order.add_edge(loop_feedback, ip_phase)
root.order.add_edge(ip_phase, partnership_phase)
root.order.add_edge(partnership_phase, final_phase)