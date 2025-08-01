# Generated from: ed95eec0-2fa8-4404-91b3-a159ff27c87f.json
# Description: This process involves systematically integrating unconventional ideas from unrelated industries into a core business to foster groundbreaking innovation. It begins with identifying external trends, followed by cross-sector brainstorming sessions, prototype development using hybrid methodologies, and iterative feedback loops involving diverse stakeholder groups. The process emphasizes adaptive learning, risk mitigation through scenario testing, and strategic alignment with long-term corporate goals. Final steps include pilot launches in controlled markets, data-driven refinement, and scaling strategies that incorporate continuous market sensing and knowledge transfer across departments, ensuring sustainable competitive advantage through atypical innovation practices.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activity nodes as Transitions
Trend_Scan = Transition(label='Trend Scan')
Idea_Harvest = Transition(label='Idea Harvest')
Sector_Match = Transition(label='Sector Match')
Brainstorm_Hub = Transition(label='Brainstorm Hub')
Concept_Filter = Transition(label='Concept Filter')
Prototype_Build = Transition(label='Prototype Build')
Hybrid_Testing = Transition(label='Hybrid Testing')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Risk_Assess = Transition(label='Risk Assess')
Scenario_Map = Transition(label='Scenario Map')
Strategy_Align = Transition(label='Strategy Align')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Capture = Transition(label='Data Capture')
Market_Sense = Transition(label='Market Sense')
Scale_Plan = Transition(label='Scale Plan')

# 1. Initial sequential part:
# Trend Scan -> Idea Harvest -> Sector Match -> Brainstorm Hub -> Concept Filter
initial_sequence = StrictPartialOrder(nodes=[Trend_Scan, Idea_Harvest, Sector_Match, Brainstorm_Hub, Concept_Filter])
initial_sequence.order.add_edge(Trend_Scan, Idea_Harvest)
initial_sequence.order.add_edge(Idea_Harvest, Sector_Match)
initial_sequence.order.add_edge(Sector_Match, Brainstorm_Hub)
initial_sequence.order.add_edge(Brainstorm_Hub, Concept_Filter)

# 2. Prototype development and hybrid testing part:
# Concept Filter -> Prototype Build -> Hybrid Testing
prototype_part = StrictPartialOrder(nodes=[Concept_Filter, Prototype_Build, Hybrid_Testing])
prototype_part.order.add_edge(Concept_Filter, Prototype_Build)
prototype_part.order.add_edge(Prototype_Build, Hybrid_Testing)

# 3. Iterative feedback loop involving diverse stakeholders and risk mitigation & strategy:
# Loop node with:
#   A = Stakeholder Sync
#   B = (Risk Assess -> Scenario Map -> Strategy Align)
risk_loop_body = StrictPartialOrder(nodes=[Risk_Assess, Scenario_Map, Strategy_Align])
risk_loop_body.order.add_edge(Risk_Assess, Scenario_Map)
risk_loop_body.order.add_edge(Scenario_Map, Strategy_Align)

risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[Stakeholder_Sync, risk_loop_body])

# 4. After iterative feedback loop: Pilot Launch -> Data Capture
pilot_part = StrictPartialOrder(nodes=[Pilot_Launch, Data_Capture])
pilot_part.order.add_edge(Pilot_Launch, Data_Capture)

# 5. Final scaling strategy with continuous market sensing and knowledge transfer:
# Market Sense and Scale Plan concurrent but Scale Plan depends on Market Sense, so Market Sense --> Scale Plan
scaling_part = StrictPartialOrder(nodes=[Market_Sense, Scale_Plan])
scaling_part.order.add_edge(Market_Sense, Scale_Plan)

# 6. Combine prototype+loop into one PO, where Concept Filter leads to prototype_part,
# prototype_part leads to loop, loop leads to pilot_part, pilot_part leads to scaling_part

# To combine prototype_part and risk_loop
pt_loop = StrictPartialOrder(nodes=[prototype_part, risk_loop])
pt_loop.order.add_edge(prototype_part, risk_loop)

pilot_scaling = StrictPartialOrder(nodes=[pilot_part, scaling_part])
pilot_scaling.order.add_edge(pilot_part, scaling_part)

# Combine all after initial_sequence
middle = StrictPartialOrder(nodes=[pt_loop, pilot_scaling])
middle.order.add_edge(pt_loop, pilot_scaling)

# Complete root PO:
# initial_sequence -> middle

root = StrictPartialOrder(nodes=[initial_sequence, middle])
root.order.add_edge(initial_sequence, middle)