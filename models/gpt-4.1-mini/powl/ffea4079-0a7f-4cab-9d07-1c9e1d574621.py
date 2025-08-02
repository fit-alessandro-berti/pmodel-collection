# Generated from: ffea4079-0a7f-4cab-9d07-1c9e1d574621.json
# Description: This process involves designing, deploying, and managing a large-scale crisis simulation for emergency response teams across multiple agencies. It includes scenario creation, resource allocation, real-time monitoring, dynamic adjustment of variables, inter-agency communication protocols, and post-simulation analysis and reporting. The process requires coordination between technology teams, field operatives, and decision-makers to ensure realistic conditions and effective training outcomes. Feedback loops and iterative refinement are essential to improve future simulations and validate response strategies under evolving threat landscapes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
scenario_setup = Transition(label='Scenario Setup')
resource_mapping = Transition(label='Resource Mapping')
team_briefing = Transition(label='Team Briefing')
tech_deployment = Transition(label='Tech Deployment')
data_sync = Transition(label='Data Sync')
comm_setup = Transition(label='Comm Setup')
live_monitoring = Transition(label='Live Monitoring')
variable_adjust = Transition(label='Variable Adjust')
incident_injection = Transition(label='Incident Injection')
response_tracking = Transition(label='Response Tracking')
interlock_check = Transition(label='Interlock Check')
real_time_feedback = Transition(label='Real-time Feedback')
debrief_session = Transition(label='Debrief Session')
outcome_analysis = Transition(label='Outcome Analysis')
report_generation = Transition(label='Report Generation')
improvement_plan = Transition(label='Improvement Plan')

# Construct partial orders and loops representing the process logic:

# Preparation phase: Scenario Setup and Resource Mapping can be concurrent, followed by Team Briefing
prep_phase = StrictPartialOrder(nodes=[scenario_setup, resource_mapping, team_briefing])
prep_phase.order.add_edge(scenario_setup, team_briefing)
prep_phase.order.add_edge(resource_mapping, team_briefing)

# Deployment phase: Tech Deployment and Data Sync run in parallel, both must finish before Comm Setup
deploy_phase = StrictPartialOrder(nodes=[tech_deployment, data_sync, comm_setup])
deploy_phase.order.add_edge(tech_deployment, comm_setup)
deploy_phase.order.add_edge(data_sync, comm_setup)

# Monitoring & Adjustment phase with a loop:
# Loop = execute live_monitoring, then choice: exit or execute variable_adjust + incident_injection and repeat live_monitoring
monitoring_loop_body = StrictPartialOrder(nodes=[variable_adjust, incident_injection])
monitoring_loop_body.order.add_edge(variable_adjust, incident_injection)

monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[live_monitoring, monitoring_loop_body])

# After monitoring loop, interlock_check then real_time_feedback concurrently
post_monitor = StrictPartialOrder(nodes=[interlock_check, real_time_feedback])
# No order between interlock_check and real_time_feedback for concurrency

# Reporting phase: Debrief Session -> Outcome Analysis -> Report Generation -> Improvement Plan
reporting = StrictPartialOrder(nodes=[debrief_session, outcome_analysis, report_generation, improvement_plan])
reporting.order.add_edge(debrief_session, outcome_analysis)
reporting.order.add_edge(outcome_analysis, report_generation)
reporting.order.add_edge(report_generation, improvement_plan)

# Response tracking depends to start after comm_setup and team_briefing, concurrent with monitoring phase
# We'll integrate response_tracking as parallel to monitoring loop and post_monitor but depends on comm_setup and team_briefing
response_tracking_node = response_tracking

# Construct the top-level partial order:
# Prep phase -> Deploy phase -> [response_tracking || monitoring_loop + post_monitor] -> reporting

# Create a parallel block for monitoring_loop and post_monitor
monitoring_plus_post = StrictPartialOrder(nodes=[monitoring_loop, post_monitor])
monitoring_plus_post.order.add_edge(monitoring_loop, post_monitor)

# The response_tracking happens in parallel with monitoring_plus_post
concurrent_monitoring_and_tracking = StrictPartialOrder(nodes=[monitoring_plus_post, response_tracking_node])
# No edges between these nodes for concurrency

# Top-level order
root = StrictPartialOrder(
    nodes=[prep_phase, deploy_phase, concurrent_monitoring_and_tracking, reporting]
)
root.order.add_edge(prep_phase, deploy_phase)
root.order.add_edge(prep_phase, concurrent_monitoring_and_tracking)
root.order.add_edge(deploy_phase, concurrent_monitoring_and_tracking)
root.order.add_edge(concurrent_monitoring_and_tracking, reporting)