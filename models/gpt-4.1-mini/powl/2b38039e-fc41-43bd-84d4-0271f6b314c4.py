# Generated from: 2b38039e-fc41-43bd-84d4-0271f6b314c4.json
# Description: This process involves the systematic identification, adaptation, and integration of innovative practices across unrelated industries to foster breakthrough product development. It begins with market scanning for emerging trends outside the company's sector, followed by feasibility assessments incorporating cross-disciplinary expert panels. Next, pilot projects are initiated to adapt external innovations, supported by iterative feedback loops involving prototype testing, user experience evaluation, and scalability analysis. The process also includes knowledge transfer sessions to internal teams, regulatory compliance reviews tailored to new application contexts, and strategic alignment workshops to ensure innovation fits the company’s long-term goals. Finally, successful innovations undergo full-scale deployment supported by change management and performance monitoring, creating a continuous loop that enhances competitive advantage through unconventional knowledge fusion.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Trend_Scan = Transition(label='Trend Scan')
Expert_Panel = Transition(label='Expert Panel')
Feasibility_Check = Transition(label='Feasibility Check')
Idea_Adapt = Transition(label='Idea Adapt')
Pilot_Launch = Transition(label='Pilot Launch')
Prototype_Test = Transition(label='Prototype Test')
User_Review = Transition(label='User Review')
Scalability_Eval = Transition(label='Scalability Eval')
Knowledge_Share = Transition(label='Knowledge Share')
Compliance_Audit = Transition(label='Compliance Audit')
Strategy_Align = Transition(label='Strategy Align')
Change_Manage = Transition(label='Change Manage')
Performance_Track = Transition(label='Performance Track')
Feedback_Loop = Transition(label='Feedback Loop')
Full_Deploy = Transition(label='Full Deploy')

# Construct the iterative feedback loop sub-process:
# feedback_loop = loop of (Prototype_Test -> User_Review -> Scalability_Eval) with Feedback_Loop controlling iteration
feedback_order = StrictPartialOrder(nodes=[Prototype_Test, User_Review, Scalability_Eval])
feedback_order.order.add_edge(Prototype_Test, User_Review)
feedback_order.order.add_edge(User_Review, Scalability_Eval)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_order, Feedback_Loop])

# Pilot projects supported by iterative feedback loop: Pilot_Launch then feedback_loop
pilot_feedback_order = StrictPartialOrder(nodes=[Pilot_Launch, feedback_loop])
pilot_feedback_order.order.add_edge(Pilot_Launch, feedback_loop)

# Early phase: Market scanning and feasibility checks with expert panels
feasibility_order = StrictPartialOrder(nodes=[Expert_Panel, Feasibility_Check])
feasibility_order.order.add_edge(Expert_Panel, Feasibility_Check)

early_phase_order = StrictPartialOrder(nodes=[Trend_Scan, feasibility_order])
early_phase_order.order.add_edge(Trend_Scan, feasibility_order)

# Adaptation phase: Idea Adapt followed by pilot_feedback_order
adaptation_order = StrictPartialOrder(nodes=[Idea_Adapt, pilot_feedback_order])
adaptation_order.order.add_edge(Idea_Adapt, pilot_feedback_order)

# Mid phase: Knowledge Share, Compliance Audit and Strategy Align are concurrent
mid_phase = StrictPartialOrder(nodes=[Knowledge_Share, Compliance_Audit, Strategy_Align])
# no order edges => concurrent

# Final phase loop:
# after mid_phase: Full_Deploy, then loop of (Change_Manage -> Performance_Track)
final_loop_body = StrictPartialOrder(nodes=[Change_Manage, Performance_Track])
final_loop_body.order.add_edge(Change_Manage, Performance_Track)
final_loop = OperatorPOWL(operator=Operator.LOOP, children=[Full_Deploy, final_loop_body])

# Combine the full process:
# early_phase -> adaptation_order -> mid_phase -> final_loop

root = StrictPartialOrder(nodes=[early_phase_order, adaptation_order, mid_phase, final_loop])
root.order.add_edge(early_phase_order, adaptation_order)
root.order.add_edge(adaptation_order, mid_phase)
root.order.add_edge(mid_phase, final_loop)