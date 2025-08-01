# Generated from: e5a5c2df-695e-45be-a773-c59e7bc0a610.json
# Description: This process involves a multi-phase coordination of resources and stakeholders during unexpected crisis events such as natural disasters or large-scale technological failures. It includes rapid assessment, communication across agencies, resource mobilization, risk mitigation, and continuous monitoring to ensure timely recovery. The process requires dynamic decision-making, prioritization of critical actions, and integration of diverse information streams to adapt to evolving situations while maintaining transparency and accountability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Alert_Trigger = Transition(label='Alert Trigger')
Initial_Assess = Transition(label='Initial Assess')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Resource_Check = Transition(label='Resource Check')
Risk_Analyze = Transition(label='Risk Analyze')
Command_Setup = Transition(label='Command Setup')
Deploy_Teams = Transition(label='Deploy Teams')
Data_Collect = Transition(label='Data Collect')
Situation_Update = Transition(label='Situation Update')
Priority_Adjust = Transition(label='Priority Adjust')
External_Liaison = Transition(label='External Liaison')
Supply_Dispatch = Transition(label='Supply Dispatch')
Media_Brief = Transition(label='Media Brief')
Impact_Review = Transition(label='Impact Review')
Recovery_Plan = Transition(label='Recovery Plan')
Process_Audit = Transition(label='Process Audit')

# Build partial orders and choices reflecting the multi-phase coordination

# Phase 1: Alert and Initial Assessment
phase1 = StrictPartialOrder(
    nodes=[Alert_Trigger, Initial_Assess, Stakeholder_Notify]
)
phase1.order.add_edge(Alert_Trigger, Initial_Assess)
phase1.order.add_edge(Alert_Trigger, Stakeholder_Notify)

# Phase 2: Resource Mobilization and Risk Analysis
phase2 = StrictPartialOrder(
    nodes=[Resource_Check, Risk_Analyze]
)
phase2.order.add_edge(Resource_Check, Risk_Analyze)

# Phase 3: Command Setup and Deployment preparation choices
# After Risk Analyze, Command Setup and Data Collection run concurrently
after_risk = StrictPartialOrder(
    nodes=[Command_Setup, Data_Collect]
)
# No order between them: concurrent

# Phase 4: Deploy Teams with a loop:
# Deploy Teams -> Situation Update -> choice(exit or Priority Adjust and External Liaison then loop again)
priority_branch = StrictPartialOrder(
    nodes=[Priority_Adjust, External_Liaison]
)
priority_branch.order.add_edge(Priority_Adjust, External_Liaison)

loop_body = StrictPartialOrder(
    nodes=[Deploy_Teams, Situation_Update]
)
loop_body.order.add_edge(Deploy_Teams, Situation_Update)

loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[loop_body, priority_branch]
)

# Phase 5: Supply Dispatch and Media Brief run concurrently after loop
phase5 = StrictPartialOrder(
    nodes=[Supply_Dispatch, Media_Brief]
)
# Concurrent, no edges

# Phase 6: Impact Review and Recovery Plan sequential
phase6 = StrictPartialOrder(
    nodes=[Impact_Review, Recovery_Plan]
)
phase6.order.add_edge(Impact_Review, Recovery_Plan)

# Final: Process Audit after Recovery Plan
final = StrictPartialOrder(
    nodes=[Process_Audit]
)

# Combine phases into overall workflow
# Order: phase1 -> phase2 -> after_risk -> loop -> phase5 -> phase6 -> final

root = StrictPartialOrder(
    nodes=[phase1, phase2, after_risk, loop, phase5, phase6, final]
)

root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, after_risk)
root.order.add_edge(after_risk, loop)
root.order.add_edge(loop, phase5)
root.order.add_edge(phase5, phase6)
root.order.add_edge(phase6, final)