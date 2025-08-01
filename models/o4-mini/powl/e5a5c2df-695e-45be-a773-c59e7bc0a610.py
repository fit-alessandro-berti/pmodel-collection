# Generated from: e5a5c2df-695e-45be-a773-c59e7bc0a610.json
# Description: This process involves a multi-phase coordination of resources and stakeholders during unexpected crisis events such as natural disasters or large-scale technological failures. It includes rapid assessment, communication across agencies, resource mobilization, risk mitigation, and continuous monitoring to ensure timely recovery. The process requires dynamic decision-making, prioritization of critical actions, and integration of diverse information streams to adapt to evolving situations while maintaining transparency and accountability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
alert_trigger     = Transition(label='Alert Trigger')
initial_assess    = Transition(label='Initial Assess')
stakeholder_notify= Transition(label='Stakeholder Notify')
resource_check    = Transition(label='Resource Check')
risk_analyze      = Transition(label='Risk Analyze')
command_setup     = Transition(label='Command Setup')
deploy_teams      = Transition(label='Deploy Teams')

data_collect      = Transition(label='Data Collect')
situation_update  = Transition(label='Situation Update')
priority_adjust   = Transition(label='Priority Adjust')
external_liaison  = Transition(label='External Liaison')
supply_dispatch   = Transition(label='Supply Dispatch')
media_brief       = Transition(label='Media Brief')
impact_review     = Transition(label='Impact Review')

recovery_plan     = Transition(label='Recovery Plan')
process_audit     = Transition(label='Process Audit')

# Phase A: initial rapid assessment & mobilization
phase_a = StrictPartialOrder(nodes=[
    alert_trigger,
    initial_assess,
    stakeholder_notify,
    resource_check,
    risk_analyze,
    command_setup,
    deploy_teams
])
phase_a.order.add_edge(alert_trigger, initial_assess)
phase_a.order.add_edge(initial_assess, stakeholder_notify)
phase_a.order.add_edge(stakeholder_notify, resource_check)
phase_a.order.add_edge(resource_check, risk_analyze)
phase_a.order.add_edge(risk_analyze, command_setup)
phase_a.order.add_edge(command_setup, deploy_teams)

# Phase B: monitoring & iterative updates
phase_b = StrictPartialOrder(nodes=[
    data_collect,
    situation_update,
    priority_adjust,
    external_liaison,
    supply_dispatch,
    media_brief,
    impact_review
])
phase_b.order.add_edge(data_collect, situation_update)
phase_b.order.add_edge(situation_update, priority_adjust)
phase_b.order.add_edge(priority_adjust, external_liaison)
phase_b.order.add_edge(external_liaison, supply_dispatch)
phase_b.order.add_edge(supply_dispatch, media_brief)
phase_b.order.add_edge(media_brief, impact_review)

# Loop: do Phase A once, then zero-or-more repetitions of Phase B + Phase A
loop = OperatorPOWL(operator=Operator.LOOP, children=[phase_a, phase_b])

# Finalization: recovery planning and audit
root = StrictPartialOrder(nodes=[loop, recovery_plan, process_audit])
root.order.add_edge(loop, recovery_plan)
root.order.add_edge(recovery_plan, process_audit)