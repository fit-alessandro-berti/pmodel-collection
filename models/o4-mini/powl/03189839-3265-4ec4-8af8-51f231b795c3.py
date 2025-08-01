# Generated from: 03189839-3265-4ec4-8af8-51f231b795c3.json
# Description: This process outlines the coordinated steps taken by an organization during an unexpected crisis, such as a natural disaster or cybersecurity breach. It involves rapid assessment, resource mobilization, stakeholder communication, and continuous monitoring to mitigate impact. The process requires cross-department collaboration, real-time data analysis, and adaptive decision-making to ensure operational continuity and public safety. Each phase includes verification, escalation, and documentation to support transparency and post-crisis review, ensuring lessons learned enhance future preparedness and resilience.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
t_alert      = Transition(label="Alert Received")
t_initial    = Transition(label="Initial Assess")
t_risk       = Transition(label="Risk Evaluate")
t_activate   = Transition(label="Activate Team")
t_allocate   = Transition(label="Resource Allocate")
t_notify     = Transition(label="Stakeholder Notify")
t_comm       = Transition(label="Communication Setup")
t_data       = Transition(label="Data Gather")
t_analyze    = Transition(label="Impact Analyze")
t_deploy     = Transition(label="Response Deploy")
t_monitor    = Transition(label="Progress Monitor")
t_escalate   = Transition(label="Issue Escalate")
t_report     = Transition(label="Situation Report")
t_recovery   = Transition(label="Recovery Plan")
t_post       = Transition(label="Post Review")
skip         = SilentTransition()

# Build the repeated monitoring‐and‐escalation loop:
#   * ( Progress Monitor , XOR(Issue Escalate, τ) )
escalate_choice = OperatorPOWL(operator=Operator.XOR, children=[t_escalate, skip])
monitor_loop    = OperatorPOWL(operator=Operator.LOOP, children=[t_monitor, escalate_choice])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    t_alert, t_initial, t_risk, t_activate, t_allocate,
    t_notify, t_comm,
    t_data, t_analyze,
    t_deploy,
    monitor_loop,
    t_report, t_recovery, t_post
])

# Define the causal edges
root.order.add_edge(t_alert,    t_initial)
root.order.add_edge(t_initial,  t_risk)
root.order.add_edge(t_risk,     t_activate)
root.order.add_edge(t_activate, t_allocate)

# After resource allocation, notify and comms happen in parallel
root.order.add_edge(t_allocate, t_notify)
root.order.add_edge(t_allocate, t_comm)

# Data gathering and impact analysis wait for both notify & comm
root.order.add_edge(t_notify,  t_data)
root.order.add_edge(t_comm,    t_data)
root.order.add_edge(t_notify,  t_analyze)
root.order.add_edge(t_comm,    t_analyze)

# Deploy response after both data & analysis
root.order.add_edge(t_data,    t_deploy)
root.order.add_edge(t_analyze, t_deploy)

# After deploy, enter the monitoring‐escalation loop
root.order.add_edge(t_deploy,  monitor_loop)

# Once loop finishes, produce situation report → recovery → post-review
root.order.add_edge(monitor_loop, t_report)
root.order.add_edge(t_report,     t_recovery)
root.order.add_edge(t_recovery,   t_post)