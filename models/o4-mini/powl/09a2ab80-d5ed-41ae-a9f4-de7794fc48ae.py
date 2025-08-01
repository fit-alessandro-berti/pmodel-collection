# Generated from: 09a2ab80-d5ed-41ae-a9f4-de7794fc48ae.json
# Description: This process involves managing an organization's response to an unexpected large-scale crisis that affects multiple departments and external stakeholders simultaneously. It includes rapid assessment of the situation, mobilizing cross-functional teams, prioritizing resource allocation, communicating with authorities and media, adapting operational workflows in real-time, and documenting all actions for post-crisis analysis. The goal is to minimize damage, maintain stakeholder trust, and restore normal operations efficiently while ensuring compliance with regulatory requirements and internal policies under high-pressure conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
alert_initiation    = Transition(label='Alert Initiation')
situation_scan      = Transition(label='Situation Scan')
team_mobilize       = Transition(label='Team Mobilize')
communication_plan  = Transition(label='Communication Plan')
stakeholder_notify  = Transition(label='Stakeholder Notify')
media_brief         = Transition(label='Media Brief')
operational_shift   = Transition(label='Operational Shift')
resource_check      = Transition(label='Resource Check')
supply_reallocate   = Transition(label='Supply Reallocate')
risk_assess         = Transition(label='Risk Assess')
priority_set        = Transition(label='Priority Set')
data_log            = Transition(label='Data Log')
compliance_review   = Transition(label='Compliance Review')
feedback_gather     = Transition(label='Feedback Gather')
recovery_plan       = Transition(label='Recovery Plan')
after_action        = Transition(label='After Action')

# Loop body: in‐crisis adaptation (resource & risk tasks can run concurrently, each with its own ordering)
body = StrictPartialOrder(nodes=[resource_check, supply_reallocate, risk_assess, priority_set])
body.order.add_edge(resource_check,    supply_reallocate)
body.order.add_edge(risk_assess,       priority_set)

# LOOP operator: first operational_shift, then zero‐or‐more iterations of the body
loop = OperatorPOWL(operator=Operator.LOOP, children=[operational_shift, body])

# Root partial order: initial alert -> scan -> team mobilize -> communications -> loop -> documentation
root = StrictPartialOrder(nodes=[
    alert_initiation, situation_scan, team_mobilize,
    communication_plan, stakeholder_notify, media_brief,
    loop,
    data_log, compliance_review, feedback_gather, recovery_plan, after_action
])

# Add the control‐flow dependencies
root.order.add_edge(alert_initiation, situation_scan)
root.order.add_edge(situation_scan,    team_mobilize)
root.order.add_edge(team_mobilize,     communication_plan)
root.order.add_edge(communication_plan, stakeholder_notify)
root.order.add_edge(communication_plan, media_brief)
root.order.add_edge(stakeholder_notify, loop)
root.order.add_edge(media_brief,        loop)
root.order.add_edge(loop,               data_log)
root.order.add_edge(data_log,           compliance_review)
root.order.add_edge(compliance_review,  feedback_gather)
root.order.add_edge(feedback_gather,    recovery_plan)
root.order.add_edge(recovery_plan,      after_action)