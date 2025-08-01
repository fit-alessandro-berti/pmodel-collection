# Generated from: 09a2ab80-d5ed-41ae-a9f4-de7794fc48ae.json
# Description: This process involves managing an organization's response to an unexpected large-scale crisis that affects multiple departments and external stakeholders simultaneously. It includes rapid assessment of the situation, mobilizing cross-functional teams, prioritizing resource allocation, communicating with authorities and media, adapting operational workflows in real-time, and documenting all actions for post-crisis analysis. The goal is to minimize damage, maintain stakeholder trust, and restore normal operations efficiently while ensuring compliance with regulatory requirements and internal policies under high-pressure conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Alert_Initiation = Transition(label='Alert Initiation')
Situation_Scan = Transition(label='Situation Scan')
Team_Mobilize = Transition(label='Team Mobilize')
Resource_Check = Transition(label='Resource Check')
Risk_Assess = Transition(label='Risk Assess')
Priority_Set = Transition(label='Priority Set')
Communication_Plan = Transition(label='Communication Plan')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Media_Brief = Transition(label='Media Brief')
Operational_Shift = Transition(label='Operational Shift')
Supply_Reallocate = Transition(label='Supply Reallocate')
Data_Log = Transition(label='Data Log')
Compliance_Review = Transition(label='Compliance Review')
Feedback_Gather = Transition(label='Feedback Gather')
Recovery_Plan = Transition(label='Recovery Plan')
After_Action = Transition(label='After Action')

# Modeling sub-processes

# Choice: Notify Stakeholders and Media in parallel but modeled as choice (could be XOR)
Notify_Stakeholders = OperatorPOWL(operator=Operator.XOR, children=[Stakeholder_Notify, Media_Brief])

# Operational shifts and supply reallocations can occur together as partial order
Operational_Resources_PO = StrictPartialOrder(nodes=[Operational_Shift, Supply_Reallocate])
# no order edges means concurrent execution

# Loop for adapting workflows:
# Adaptation cycle: (Operational_Resources_PO, Feedback_Gather)
# do Operational_Resources_PO followed by optionally loop Feedback_Gather and Operational_Resources_PO repeatedly until exit
adapt_loop = OperatorPOWL(operator=Operator.LOOP, children=[Operational_Resources_PO, Feedback_Gather])

# Choice after Risk Assess/prioritization: Communication Plan or Recovery Plan?
Post_Assessment_Choice = OperatorPOWL(operator=Operator.XOR, children=[Communication_Plan, Recovery_Plan])

# Partial order for the initial assessment and mobilization
Initial_Assessment_PO = StrictPartialOrder(nodes=[Alert_Initiation, Situation_Scan, Team_Mobilize, Resource_Check, Risk_Assess, Priority_Set])
Initial_Assessment_PO.order.add_edge(Alert_Initiation, Situation_Scan)
Initial_Assessment_PO.order.add_edge(Situation_Scan, Team_Mobilize)
Initial_Assessment_PO.order.add_edge(Team_Mobilize, Resource_Check)
Initial_Assessment_PO.order.add_edge(Resource_Check, Risk_Assess)
Initial_Assessment_PO.order.add_edge(Risk_Assess, Priority_Set)

# Partial order for communication after plan decision
Communication_PO = StrictPartialOrder(nodes=[Post_Assessment_Choice, Notify_Stakeholders])
Communication_PO.order.add_edge(Post_Assessment_Choice, Notify_Stakeholders)

# Compliance review and data logging concurrent with adaptation and communication
Compliance_and_Logging_PO = StrictPartialOrder(nodes=[Compliance_Review, Data_Log])
# no order edge: concurrent

# Recovery and after action partial order
Recovery_PO = StrictPartialOrder(nodes=[Recovery_Plan, After_Action])
Recovery_PO.order.add_edge(Recovery_Plan, After_Action)

# Define main overall partial order
root = StrictPartialOrder(nodes=[
    Initial_Assessment_PO,
    Communication_PO,
    adapt_loop,
    Compliance_and_Logging_PO,
    Recovery_PO
])

# Define edges to capture main flow dependencies:
root.order.add_edge(Initial_Assessment_PO, Communication_PO)
root.order.add_edge(Communication_PO, adapt_loop)
root.order.add_edge(adapt_loop, Recovery_PO)
root.order.add_edge(adapt_loop, Compliance_and_Logging_PO)  # Compliance and logging happens concurrent with adaptation

# Note: Compliance and Logging can start any time after adaptation starts, so we connect it after adaptation loop.
