# Generated from: 0b4e8ea1-a440-4817-a9cd-470d5e04d44c.json
# Description: Dynamic Talent Allocation is a multifaceted process designed to optimize workforce distribution across multiple projects in real-time by leveraging predictive analytics and continuous feedback loops. The process starts with skill profiling and project requirement mapping, followed by availability forecasting using AI-driven models. Concurrently, employee preferences and historical performance metrics are analyzed to match talents with evolving project demands. Throughout the project lifecycle, dynamic reassignment and upskilling initiatives are executed based on emerging skill gaps and shifting priorities. Continuous performance monitoring and stakeholder feedback ensure alignment with organizational goals while minimizing downtime and maximizing productivity. The process concludes with post-project evaluation and knowledge retention activities to enhance future allocation cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Skill_Profiling = Transition(label='Skill Profiling')
Requirement_Map = Transition(label='Requirement Map')
Availability_Check = Transition(label='Availability Check')
Preference_Survey = Transition(label='Preference Survey')
Performance_Review = Transition(label='Performance Review')
Demand_Forecast = Transition(label='Demand Forecast')
Talent_Match = Transition(label='Talent Match')
Assignment_Notify = Transition(label='Assignment Notify')
Onboard_Brief = Transition(label='Onboard Brief')
Progress_Monitor = Transition(label='Progress Monitor')
Gap_Identify = Transition(label='Gap Identify')
Upskill_Plan = Transition(label='Upskill Plan')
Reassign_Talent = Transition(label='Reassign Talent')
Feedback_Gather = Transition(label='Feedback Gather')
Project_Closeout = Transition(label='Project Closeout')
Knowledge_Archive = Transition(label='Knowledge Archive')

# First phase: skill profiling and requirement mapping, then availability forecasting
# Skill Profiling --> Requirement Map --> Availability Check
phase1 = StrictPartialOrder(nodes=[Skill_Profiling, Requirement_Map, Availability_Check])
phase1.order.add_edge(Skill_Profiling, Requirement_Map)
phase1.order.add_edge(Requirement_Map, Availability_Check)

# Concurrent analysis of preferences and performance metrics:
# Preference Survey and Performance Review can run in parallel before Demand Forecast
pref_perf = StrictPartialOrder(nodes=[Preference_Survey, Performance_Review])
# no order edges to allow concurrency

# After both, Demand Forecast happens
phase2 = StrictPartialOrder(nodes=[pref_perf, Demand_Forecast])
phase2.order.add_edge(pref_perf, Demand_Forecast)

# Talent Match after Demand Forecast
talent_match_order = StrictPartialOrder(nodes=[Demand_Forecast, Talent_Match])
talent_match_order.order.add_edge(Demand_Forecast, Talent_Match)

# Notify Assignment and Onboard Brief sequentially after Talent Match
assign_onboard = StrictPartialOrder(nodes=[Assignment_Notify, Onboard_Brief])
assign_onboard.order.add_edge(Assignment_Notify, Onboard_Brief)

# Build initial PO combining above partial orders:
# Availability Check --> pref_perf
# pref_perf --> Demand Forecast
# Demand Forecast --> Talent Match
# Talent Match --> Assignment Notify --> Onboard Brief

init_nodes = [phase1, phase2, talent_match_order, assign_onboard]

root_init = StrictPartialOrder(nodes=init_nodes)
root_init.order.add_edge(phase1, phase2)       # Availability Check --> pref_perf + Demand Forecast
root_init.order.add_edge(phase2, talent_match_order)  # Demand Forecast --> Talent Match
root_init.order.add_edge(talent_match_order, assign_onboard) # Talent Match --> Assignment Notify + Onboard Brief

# Loop representing the project lifecycle activities:
# Loop body: 
# Progress Monitor --> (Gap Identify --> Upskill Plan) AND Reassign Talent AND Feedback Gather (concurrent)
# Loop iteration: first execute Progress Monitor, then choice:
#   exit, or 
#   execute sequence (Gap Identify --> Upskill Plan), 
#   and concurrently Reassign Talent and Feedback Gather 
#   and then Progress Monitor again

# Build gap identify --> upskill plan
gap_upskill = StrictPartialOrder(nodes=[Gap_Identify, Upskill_Plan])
gap_upskill.order.add_edge(Gap_Identify, Upskill_Plan)

# Concurrent Reassign Talent and Feedback Gather
reassign_feedback = StrictPartialOrder(nodes=[Reassign_Talent, Feedback_Gather])
# no edges, they are concurrent

# Combine gap_upskill and reassign_feedback as partial order concurrent nodes after Progress Monitor
#  so after Progress Monitor: nodes = [gap_upskill, reassign_feedback]
# But they need to be executed together before next Progress Monitor iteration

# Create a partial order for the body loop portion after Progress Monitor:
loop_body_after_pm = StrictPartialOrder(nodes=[gap_upskill, reassign_feedback])
# no edges => concurrent

# Build the loop body:
# Progress Monitor --> loop body tasks
loop_body = StrictPartialOrder(nodes=[Progress_Monitor, loop_body_after_pm])
loop_body.order.add_edge(Progress_Monitor, loop_body_after_pm)

# LOOP: execute Progress Monitor, then choice to exit or 
# (loop_body_after_pm then loop_body again)
# According to definition:
# LOOP(A, B) = Execute A, then choose to exit or execute B then A again repeated until exit.
# Here, A = Progress Monitor, B = combined loop body after Progress Monitor (gap_upskill+reassign+feedback)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Progress_Monitor, loop_body_after_pm])

# After the loop ends, Project Closeout and Knowledge Archive happen sequentially
post_project = StrictPartialOrder(nodes=[Project_Closeout, Knowledge_Archive])
post_project.order.add_edge(Project_Closeout, Knowledge_Archive)

# Final root combining initial part, loop, and post-project activities
root = StrictPartialOrder(nodes=[root_init, loop, post_project])
# root_init --> loop --> post_project
root.order.add_edge(root_init, loop)
root.order.add_edge(loop, post_project)