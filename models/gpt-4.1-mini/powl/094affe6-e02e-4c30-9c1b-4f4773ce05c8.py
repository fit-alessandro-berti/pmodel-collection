# Generated from: 094affe6-e02e-4c30-9c1b-4f4773ce05c8.json
# Description: This process involves the continuous identification and integration of innovative technologies and practices from unrelated industries to create breakthrough products or services. It starts with environmental scanning to detect emerging trends, followed by cross-domain brainstorming sessions to ideate novel applications. Next, feasibility assessments are conducted with multidisciplinary teams, incorporating rapid prototyping and iterative testing. Strategic partnerships are formed to leverage external expertise and resources. Feedback loops from pilot deployments guide refinements before full-scale implementation. The process emphasizes agility, knowledge sharing, and risk management to ensure sustainable innovation that disrupts markets and drives competitive advantage across diverse sectors.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Trend_Scan = Transition(label='Trend Scan')
Idea_Harvest = Transition(label='Idea Harvest')
Feasibility_Check = Transition(label='Feasibility Check')
Concept_Workshop = Transition(label='Concept Workshop')
Partner_Outreach = Transition(label='Partner Outreach')
Prototype_Build = Transition(label='Prototype Build')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Analysis = Transition(label='Data Analysis')
Risk_Review = Transition(label='Risk Review')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Resource_Align = Transition(label='Resource Align')
Feedback_Loop = Transition(label='Feedback Loop')
Scale_Plan = Transition(label='Scale Plan')
Market_Test = Transition(label='Market Test')
Final_Rollout = Transition(label='Final Rollout')

# Step 1: Environmental scanning
step1 = Trend_Scan

# Step 2: Cross-domain brainstorming sessions (Idea Harvest and Concept Workshop concurrent)
step2 = StrictPartialOrder(nodes=[Idea_Harvest, Concept_Workshop])

# Step 3: Feasibility assessments (Feasibility Check) with multidisciplinary teams, incorporating Prototype Build and iterative testing via loop with Feedback Loop and Data Analysis

# Define the inner loop body: (Prototype Build -> Pilot Launch -> Data Analysis -> Risk Review)
loop_body_nodes = [Prototype_Build, Pilot_Launch, Data_Analysis, Risk_Review]
loop_body = StrictPartialOrder(nodes=loop_body_nodes)
loop_body.order.add_edge(Prototype_Build, Pilot_Launch)
loop_body.order.add_edge(Pilot_Launch, Data_Analysis)
loop_body.order.add_edge(Data_Analysis, Risk_Review)

# After Risk Review: choice to either exit or do Feedback Loop then again the loop_body
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        loop_body,       # A
        Feedback_Loop    # B
    ]
)

# Feasibility Check followed by loop (the check and the loop are sequential)
step3 = StrictPartialOrder(nodes=[Feasibility_Check, loop])
step3.order.add_edge(Feasibility_Check, loop)

# Step 4: Strategic partnerships
step4 = Partner_Outreach

# Step 5: Risk management and alignment: Stakeholder Sync and Resource Align concurrent
step5 = StrictPartialOrder(nodes=[Stakeholder_Sync, Resource_Align])

# Step 6: Scale Plan, Market Test, Final Rollout sequential
step6 = StrictPartialOrder(nodes=[Scale_Plan, Market_Test, Final_Rollout])
step6.order.add_edge(Scale_Plan, Market_Test)
step6.order.add_edge(Market_Test, Final_Rollout)

# Assemble the overall process as partial order of steps 1 to 6 in sequence
root = StrictPartialOrder(
    nodes=[step1, step2, step3, step4, step5, step6]
)
root.order.add_edge(step1, step2)
root.order.add_edge(step2, step3)
root.order.add_edge(step3, step4)
root.order.add_edge(step4, step5)
root.order.add_edge(step5, step6)