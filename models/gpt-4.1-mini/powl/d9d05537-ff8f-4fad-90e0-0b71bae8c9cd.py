# Generated from: d9d05537-ff8f-4fad-90e0-0b71bae8c9cd.json
# Description: This process involves managing an organization’s response to an unexpected crisis that impacts operations, reputation, and stakeholder trust. It includes rapid assessment, resource mobilization, communication strategies, legal compliance checks, and iterative recovery efforts. The process integrates cross-functional teams, external agencies, and continuous monitoring to adapt dynamically. Activities range from initial alert verification to post-crisis evaluation, ensuring resilience and minimizing damage while maintaining transparency and accountability throughout the response lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Alert_Verify = Transition(label='Alert Verify')
Impact_Assess = Transition(label='Impact Assess')
Team_Assemble = Transition(label='Team Assemble')
Resource_Allocate = Transition(label='Resource Allocate')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Legal_Review = Transition(label='Legal Review')
Media_Brief = Transition(label='Media Brief')
Response_Deploy = Transition(label='Response Deploy')
Situation_Monitor = Transition(label='Situation Monitor')
Data_Collect = Transition(label='Data Collect')
Risk_Mitigate = Transition(label='Risk Mitigate')
Recovery_Plan = Transition(label='Recovery Plan')
External_Consult = Transition(label='External Consult')
Status_Update = Transition(label='Status Update')
Post_Review = Transition(label='Post Review')

# Define a loop for continuous monitoring and adapting recovery efforts: 
# Loop body includes Situation Monitor, Data Collect, Risk Mitigate, Recovery Plan, External Consult, Status Update
monitoring_order = StrictPartialOrder(nodes=[
    Situation_Monitor, Data_Collect, Risk_Mitigate, Recovery_Plan, External_Consult, Status_Update])
monitoring_order.order.add_edge(Situation_Monitor, Data_Collect)
monitoring_order.order.add_edge(Data_Collect, Risk_Mitigate)
monitoring_order.order.add_edge(Risk_Mitigate, Recovery_Plan)
monitoring_order.order.add_edge(Recovery_Plan, External_Consult)
monitoring_order.order.add_edge(External_Consult, Status_Update)

# Loop: after Status_Update choose to exit or repeat monitoring
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_order, SilentTransition()])

# Partial order for initial assessment and mobilization
initial_order = StrictPartialOrder(nodes=[
    Alert_Verify, Impact_Assess, Team_Assemble, Resource_Allocate, Stakeholder_Notify,
    Legal_Review, Media_Brief, Response_Deploy])
initial_order.order.add_edge(Alert_Verify, Impact_Assess)
initial_order.order.add_edge(Impact_Assess, Team_Assemble)
initial_order.order.add_edge(Team_Assemble, Resource_Allocate)

# Stakeholder Notify, Legal Review, Media Brief can proceed in parallel after Resource Allocate
initial_order.order.add_edge(Resource_Allocate, Stakeholder_Notify)
initial_order.order.add_edge(Resource_Allocate, Legal_Review)
initial_order.order.add_edge(Resource_Allocate, Media_Brief)

# Wait for all these communication/legal activities to finish before Response Deploy
initial_order.order.add_edge(Stakeholder_Notify, Response_Deploy)
initial_order.order.add_edge(Legal_Review, Response_Deploy)
initial_order.order.add_edge(Media_Brief, Response_Deploy)

# Connect initial order to monitoring loop
root = StrictPartialOrder(nodes=[initial_order, monitoring_loop, Post_Review])
root.order.add_edge(initial_order, monitoring_loop)
root.order.add_edge(monitoring_loop, Post_Review)