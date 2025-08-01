# Generated from: 2b38039e-fc41-43bd-84d4-0271f6b314c4.json
# Description: This process involves the systematic identification, adaptation, and integration of innovative practices across unrelated industries to foster breakthrough product development. It begins with market scanning for emerging trends outside the company's sector, followed by feasibility assessments incorporating cross-disciplinary expert panels. Next, pilot projects are initiated to adapt external innovations, supported by iterative feedback loops involving prototype testing, user experience evaluation, and scalability analysis. The process also includes knowledge transfer sessions to internal teams, regulatory compliance reviews tailored to new application contexts, and strategic alignment workshops to ensure innovation fits the company’s long-term goals. Finally, successful innovations undergo full-scale deployment supported by change management and performance monitoring, creating a continuous loop that enhances competitive advantage through unconventional knowledge fusion.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
trend_scan      = Transition(label='Trend Scan')
expert_panel    = Transition(label='Expert Panel')
feasibility     = Transition(label='Feasibility Check')
idea_adapt      = Transition(label='Idea Adapt')
pilot_launch    = Transition(label='Pilot Launch')
prototype_test  = Transition(label='Prototype Test')
user_review     = Transition(label='User Review')
scalability     = Transition(label='Scalability Eval')
feedback_loop   = Transition(label='Feedback Loop')
knowledge_share = Transition(label='Knowledge Share')
compliance      = Transition(label='Compliance Audit')
strategy_align  = Transition(label='Strategy Align')
change_manage   = Transition(label='Change Manage')
performance_trk = Transition(label='Performance Track')
full_deploy     = Transition(label='Full Deploy')

# Build the inner loop of testing, review, scalability analysis, and feedback
inner_loop_po = StrictPartialOrder(nodes=[
    prototype_test,
    user_review,
    scalability,
    feedback_loop
])
inner_loop_po.order.add_edge(prototype_test, user_review)
inner_loop_po.order.add_edge(user_review, scalability)
inner_loop_po.order.add_edge(scalability, feedback_loop)

# Define the pilot‐feedback loop: do the launch, then iterate the inner loop
pilot_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pilot_launch, inner_loop_po]
)

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[
    trend_scan,
    expert_panel,
    feasibility,
    idea_adapt,
    pilot_loop,
    knowledge_share,
    compliance,
    strategy_align,
    change_manage,
    performance_trk,
    full_deploy
])

# Specify the control‐flow (partial order) dependencies
root.order.add_edge(trend_scan, expert_panel)
root.order.add_edge(trend_scan, feasibility)
root.order.add_edge(expert_panel, idea_adapt)
root.order.add_edge(feasibility, idea_adapt)
root.order.add_edge(idea_adapt, pilot_loop)
root.order.add_edge(pilot_loop, knowledge_share)
root.order.add_edge(knowledge_share, compliance)
root.order.add_edge(compliance, strategy_align)
root.order.add_edge(strategy_align, change_manage)
root.order.add_edge(strategy_align, performance_trk)
root.order.add_edge(change_manage, full_deploy)
root.order.add_edge(performance_trk, full_deploy)