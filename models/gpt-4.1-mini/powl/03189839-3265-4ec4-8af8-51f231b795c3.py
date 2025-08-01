# Generated from: 03189839-3265-4ec4-8af8-51f231b795c3.json
# Description: This process outlines the coordinated steps taken by an organization during an unexpected crisis, such as a natural disaster or cybersecurity breach. It involves rapid assessment, resource mobilization, stakeholder communication, and continuous monitoring to mitigate impact. The process requires cross-department collaboration, real-time data analysis, and adaptive decision-making to ensure operational continuity and public safety. Each phase includes verification, escalation, and documentation to support transparency and post-crisis review, ensuring lessons learned enhance future preparedness and resilience.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Alert_Received = Transition(label='Alert Received')
Initial_Assess = Transition(label='Initial Assess')
Risk_Evaluate = Transition(label='Risk Evaluate')
Activate_Team = Transition(label='Activate Team')
Resource_Allocate = Transition(label='Resource Allocate')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Communication_Setup = Transition(label='Communication Setup')
Data_Gather = Transition(label='Data Gather')
Impact_Analyze = Transition(label='Impact Analyze')
Response_Deploy = Transition(label='Response Deploy')
Progress_Monitor = Transition(label='Progress Monitor')
Issue_Escalate = Transition(label='Issue Escalate')
Situation_Report = Transition(label='Situation Report')
Recovery_Plan = Transition(label='Recovery Plan')
Post_Review = Transition(label='Post Review')

# Verification: After key activities, perform verification (Issue Escalate chosen as escalation),
# and documentation (Situation Report).
# The process phases could be modeled roughly as follows:

# Phase 1: Initial assessment and risk evaluation with verification and documentation
Verif1 = StrictPartialOrder(nodes=[Risk_Evaluate, Issue_Escalate, Situation_Report])
Verif1.order.add_edge(Risk_Evaluate, Issue_Escalate)
Verif1.order.add_edge(Risk_Evaluate, Situation_Report)

# Phase 2: Activation and resource allocation with verification and documentation
Verif2 = StrictPartialOrder(nodes=[Resource_Allocate, Issue_Escalate, Situation_Report])
Verif2.order.add_edge(Resource_Allocate, Issue_Escalate)
Verif2.order.add_edge(Resource_Allocate, Situation_Report)

# Phase 3: Stakeholder communication setup and notification with verification and documentation
Verif3 = StrictPartialOrder(nodes=[Stakeholder_Notify, Communication_Setup, Issue_Escalate, Situation_Report])
Verif3.order.add_edge(Stakeholder_Notify, Issue_Escalate)
Verif3.order.add_edge(Stakeholder_Notify, Situation_Report)
Verif3.order.add_edge(Communication_Setup, Issue_Escalate)
Verif3.order.add_edge(Communication_Setup, Situation_Report)

# Phase 4: Data gathering and impact analysis with verification and documentation
Verif4 = StrictPartialOrder(nodes=[Data_Gather, Impact_Analyze, Issue_Escalate, Situation_Report])
Verif4.order.add_edge(Data_Gather, Issue_Escalate)
Verif4.order.add_edge(Data_Gather, Situation_Report)
Verif4.order.add_edge(Impact_Analyze, Issue_Escalate)
Verif4.order.add_edge(Impact_Analyze, Situation_Report)

# Phase 5: Response deployment and progress monitoring with verification and documentation
Verif5 = StrictPartialOrder(nodes=[Response_Deploy, Progress_Monitor, Issue_Escalate, Situation_Report])
Verif5.order.add_edge(Response_Deploy, Issue_Escalate)
Verif5.order.add_edge(Response_Deploy, Situation_Report)
Verif5.order.add_edge(Progress_Monitor, Issue_Escalate)
Verif5.order.add_edge(Progress_Monitor, Situation_Report)

# Loop structure for continuous monitoring until recovery plan is enacted
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        StrictPartialOrder(nodes=[Progress_Monitor, Issue_Escalate, Situation_Report]),
        SilentTransition()
    ]
)

# Recovery and post-review after loop exit
recovery_and_review = StrictPartialOrder(nodes=[Recovery_Plan, Post_Review])
recovery_and_review.order.add_edge(Recovery_Plan, Post_Review)

# Compose the full process as partial order with suitable ordering and concurrency
root = StrictPartialOrder(nodes=[
    Alert_Received,
    Initial_Assess,
    Verif1,
    Activate_Team,
    Verif2,
    Verif3,
    Verif4,
    Verif5,
    monitor_loop,
    recovery_and_review
])

# Define the order of execution following logical sequence

# Alert Received -> Initial Assess
root.order.add_edge(Alert_Received, Initial_Assess)

# Initial Assess -> Verif1 (Risk Evaluate etc)
root.order.add_edge(Initial_Assess, Verif1)

# Verif1 -> Activate Team
root.order.add_edge(Verif1, Activate_Team)

# Activate Team -> Verif2 (Resource Allocate etc)
root.order.add_edge(Activate_Team, Verif2)

# Verif2 -> Verif3 (Stakeholder Notify etc)
root.order.add_edge(Verif2, Verif3)

# Verif3 -> Verif4 (Data Gather etc)
root.order.add_edge(Verif3, Verif4)

# Verif4 -> Verif5 (Response Deploy etc)
root.order.add_edge(Verif4, Verif5)

# Verif5 -> monitor_loop
root.order.add_edge(Verif5, monitor_loop)

# monitor_loop -> recovery_and_review
root.order.add_edge(monitor_loop, recovery_and_review)