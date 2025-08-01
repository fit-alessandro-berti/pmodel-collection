# Generated from: b47a393f-f1ba-4ebc-b1ef-b1fb6ed623e4.json
# Description: This process encapsulates a complex cycle of generating, validating, and implementing innovative ideas across multiple industries simultaneously. It involves capturing emerging trends, conducting cross-sector feasibility studies, engaging diverse expert panels, iterating prototypes with real-time user feedback, and integrating adaptive regulatory compliance checks. The process culminates in scalable pilot launches, extensive market impact analysis, and continuous refinement through data-driven insights, ensuring sustainable innovation that transcends conventional industry boundaries while managing multidimensional risks and opportunities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities (transitions)
Trend_Scan = Transition(label='Trend Scan')
Idea_Capture = Transition(label='Idea Capture')
Feasibility_Test = Transition(label='Feasibility Test')
Expert_Review = Transition(label='Expert Review')
Prototype_Build = Transition(label='Prototype Build')
User_Feedback = Transition(label='User Feedback')
Compliance_Check = Transition(label='Compliance Check')
Risk_Assess = Transition(label='Risk Assess')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Gather = Transition(label='Data Gather')
Impact_Analyze = Transition(label='Impact Analyze')
Market_Adjust = Transition(label='Market Adjust')
Scaling_Plan = Transition(label='Scaling Plan')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Continuous_Improve = Transition(label='Continuous Improve')

# Model the iterative cycle:
# cycle = LOOP(body= Prototype Build -> User Feedback -> Compliance Check -> Risk Assess,
#              redo= Expert Review -> Feasibility Test -> Idea Capture -> Trend Scan)
cycle_body = StrictPartialOrder(nodes=[Prototype_Build, User_Feedback, Compliance_Check, Risk_Assess])
cycle_body.order.add_edge(Prototype_Build, User_Feedback)
cycle_body.order.add_edge(User_Feedback, Compliance_Check)
cycle_body.order.add_edge(Compliance_Check, Risk_Assess)

cycle_redo = StrictPartialOrder(nodes=[Expert_Review, Feasibility_Test, Idea_Capture, Trend_Scan])
cycle_redo.order.add_edge(Expert_Review, Feasibility_Test)
cycle_redo.order.add_edge(Feasibility_Test, Idea_Capture)
cycle_redo.order.add_edge(Idea_Capture, Trend_Scan)

cycle = OperatorPOWL(operator=Operator.LOOP, children=[cycle_body, cycle_redo])

# After cycle ends, continue with Pilot Launch and downstream activities:
post_cycle = StrictPartialOrder(
    nodes=[Pilot_Launch, Data_Gather, Impact_Analyze, Market_Adjust, Scaling_Plan, Stakeholder_Sync, Continuous_Improve]
)
post_cycle.order.add_edge(Pilot_Launch, Data_Gather)
post_cycle.order.add_edge(Data_Gather, Impact_Analyze)
post_cycle.order.add_edge(Impact_Analyze, Market_Adjust)
post_cycle.order.add_edge(Market_Adjust, Scaling_Plan)
post_cycle.order.add_edge(Scaling_Plan, Stakeholder_Sync)
post_cycle.order.add_edge(Stakeholder_Sync, Continuous_Improve)

# The full process:
# Start with Trend_Scan, Idea_Capture, Feasibility_Test, Expert_Review before entering cycle? 
# The cycle_redo includes those, so no need to separate.

# Combine Trend Scan and Idea Capture with cycle:
# Actually, cycle_redo includes these "capture and test" steps leading into cycle_body.
# So we place the cycle as a loop with those two children, that controls iterative flow.

# Add a starting partial order to lead into cycle: Trend Scan -> Idea Capture -> Feasibility Test -> Expert Review
start_lead = StrictPartialOrder(nodes=[Trend_Scan, Idea_Capture, Feasibility_Test, Expert_Review])
start_lead.order.add_edge(Trend_Scan, Idea_Capture)
start_lead.order.add_edge(Idea_Capture, Feasibility_Test)
start_lead.order.add_edge(Feasibility_Test, Expert_Review)

# Now redefine the cycle to loop the cycle_body with Expert Review only as redo,
# because start_lead covers initial progression to Expert Review.
# Looping means after cycle_body, choose to exit or redo cycle_body preceded by Expert Review.
cycle = OperatorPOWL(operator=Operator.LOOP, children=[cycle_body, Expert_Review])

# Compose model:
# start_lead -> cycle -> post_cycle
root = StrictPartialOrder(nodes=[start_lead, cycle, post_cycle])
root.order.add_edge(start_lead, cycle)
root.order.add_edge(cycle, post_cycle)