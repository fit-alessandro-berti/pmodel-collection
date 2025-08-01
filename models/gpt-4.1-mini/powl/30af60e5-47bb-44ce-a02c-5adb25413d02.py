# Generated from: 30af60e5-47bb-44ce-a02c-5adb25413d02.json
# Description: This process involves the systematic identification, adaptation, and implementation of innovations from unrelated industries to solve unique organizational challenges. It begins with cross-sector trend scanning, followed by feasibility evaluation and rapid prototyping adapted to the company's context. Stakeholder feedback is continuously integrated to refine solutions, while strategic partnerships are formed to access external expertise. The process concludes with scaling successful innovations through tailored training programs and performance tracking to ensure sustained impact and competitive advantage across diverse markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Trend_Scan = Transition(label='Trend Scan')
Idea_Harvest = Transition(label='Idea Harvest')
Feasibility_Check = Transition(label='Feasibility Check')
Concept_Design = Transition(label='Concept Design')
Prototype_Build = Transition(label='Prototype Build')
Stakeholder_Input = Transition(label='Stakeholder Input')
Partner_Align = Transition(label='Partner Align')
Pilot_Launch = Transition(label='Pilot Launch')
Feedback_Loop = Transition(label='Feedback Loop')
Iterate_Model = Transition(label='Iterate Model')
Training_Deploy = Transition(label='Training Deploy')
Scale_Rollout = Transition(label='Scale Rollout')
Impact_Review = Transition(label='Impact Review')
Knowledge_Share = Transition(label='Knowledge Share')
Market_Adapt = Transition(label='Market Adapt')

# Model the feedback loop: Feedback Loop and Iterate Model form a loop
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Iterate_Model])

# Strategic partnerships and feedback integration run concurrently after Stakeholder Input
post_stakeholder_PO = StrictPartialOrder(nodes=[feedback_loop, Partner_Align])

# Add no order edges between feedback_loop and Partner_Align, so they are concurrent

# Implementation and scaling phase after Pilot Launch:
# Training Deploy -> Scale Rollout -> Impact Review -> Knowledge Share -> Market Adapt
scaling_PO = StrictPartialOrder(
    nodes=[Training_Deploy, Scale_Rollout, Impact_Review, Knowledge_Share, Market_Adapt]
)
scaling_PO.order.add_edge(Training_Deploy, Scale_Rollout)
scaling_PO.order.add_edge(Scale_Rollout, Impact_Review)
scaling_PO.order.add_edge(Impact_Review, Knowledge_Share)
scaling_PO.order.add_edge(Knowledge_Share, Market_Adapt)

# After Prototype Build, Stakeholder Input and Pilot Launch occur
# Stakeholder Input leads to post_stakeholder_PO: feedback loop + partner align
# Pilot Launch leads to scaling_PO
implementation_PO = StrictPartialOrder(
    nodes=[Stakeholder_Input, post_stakeholder_PO, Pilot_Launch, scaling_PO]
)
implementation_PO.order.add_edge(Stakeholder_Input, post_stakeholder_PO)
# post_stakeholder_PO is a PO node, so edges to children handled internally
implementation_PO.order.add_edge(Stakeholder_Input, Pilot_Launch)
implementation_PO.order.add_edge(Pilot_Launch, scaling_PO)

# Before Prototype Build is Concept Design
# Flow: Feasibility Check -> Concept Design -> Prototype Build
design_PO = StrictPartialOrder(nodes=[Feasibility_Check, Concept_Design, Prototype_Build])
design_PO.order.add_edge(Feasibility_Check, Concept_Design)
design_PO.order.add_edge(Concept_Design, Prototype_Build)

# Beginning phase: Trend Scan -> Idea Harvest -> Feasibility Check
begin_PO = StrictPartialOrder(nodes=[Trend_Scan, Idea_Harvest, Feasibility_Check])
begin_PO.order.add_edge(Trend_Scan, Idea_Harvest)
begin_PO.order.add_edge(Idea_Harvest, Feasibility_Check)

# Compose full process partial order:
# begin_PO -> design_PO -> implementation_PO
root = StrictPartialOrder(
    nodes=[begin_PO, design_PO, implementation_PO]
)
root.order.add_edge(begin_PO, design_PO)
root.order.add_edge(design_PO, implementation_PO)