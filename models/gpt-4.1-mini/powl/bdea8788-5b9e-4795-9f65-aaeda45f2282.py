# Generated from: bdea8788-5b9e-4795-9f65-aaeda45f2282.json
# Description: This process coordinates rapid disaster response by leveraging a global network of volunteers, local authorities, and AI-driven resource allocation. It begins with hazard detection and public alerting, followed by volunteer mobilization through geotagged task assignments. Data from on-site volunteers is continuously aggregated and analyzed for situational awareness. Concurrently, supply chains are dynamically managed to deliver essential goods, while remote experts provide real-time guidance via digital platforms. The process integrates feedback loops to adapt resource allocation and volunteer deployment, ensuring efficient coverage despite unpredictable conditions and communication challenges. Post-event, the system facilitates impact assessment and lessons learned compilation for future preparedness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Hazard_Detect = Transition(label='Hazard Detect')
Issue_Alert = Transition(label='Issue Alert')
Mobilize_Volunteers = Transition(label='Mobilize Volunteers')
Assign_Tasks = Transition(label='Assign Tasks')
Collect_Data = Transition(label='Collect Data')
Analyze_Reports = Transition(label='Analyze Reports')
Allocate_Supplies = Transition(label='Allocate Supplies')
Coordinate_Transport = Transition(label='Coordinate Transport')
Provide_Guidance = Transition(label='Provide Guidance')
Monitor_Progress = Transition(label='Monitor Progress')
Update_Status = Transition(label='Update Status')
Adjust_Deployment = Transition(label='Adjust Deployment')
Manage_Feedback = Transition(label='Manage Feedback')
Conduct_Debrief = Transition(label='Conduct Debrief')
Compile_Lessons = Transition(label='Compile Lessons')

# Define partial order for initial activities: Hazard Detect --> Issue Alert
po_start = StrictPartialOrder(nodes=[Hazard_Detect, Issue_Alert])
po_start.order.add_edge(Hazard_Detect, Issue_Alert)

# After Issue Alert: Mobilize Volunteers --> Assign Tasks
po_mobilize = StrictPartialOrder(nodes=[Mobilize_Volunteers, Assign_Tasks])
po_mobilize.order.add_edge(Mobilize_Volunteers, Assign_Tasks)

# Data collection and analysis partial order: Collect Data --> Analyze Reports
po_data = StrictPartialOrder(nodes=[Collect_Data, Analyze_Reports])
po_data.order.add_edge(Collect_Data, Analyze_Reports)

# Supply chain partial order: Allocate Supplies --> Coordinate Transport
po_supply = StrictPartialOrder(nodes=[Allocate_Supplies, Coordinate_Transport])
po_supply.order.add_edge(Allocate_Supplies, Coordinate_Transport)

# Remote experts guidance is a single activity
guidance = Provide_Guidance

# Monitoring progression chain: Monitor Progress --> Update Status
po_monitor = StrictPartialOrder(nodes=[Monitor_Progress, Update_Status])
po_monitor.order.add_edge(Monitor_Progress, Update_Status)

# Feedback management and deployment adjustment loop body:
# Adjust Deployment --> Manage Feedback (then loop back)
loop_body = StrictPartialOrder(nodes=[Adjust_Deployment, Manage_Feedback])
loop_body.order.add_edge(Adjust_Deployment, Manage_Feedback)

# Loop = *(Adjust Deployment + Manage Feedback, Analyze Reports + Monitor Progress + Update Status)
# We model loop as: Loop(LoopBody, ConditionBody)
# ConditionBody is Analyze_Reports + Monitor_Progress + Update_Status in partial order

condition_body = StrictPartialOrder(
    nodes=[Analyze_Reports, Monitor_Progress, Update_Status]
)
condition_body.order.add_edge(Analyze_Reports, Monitor_Progress)
condition_body.order.add_edge(Monitor_Progress, Update_Status)

loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[loop_body, condition_body]
)

# Concurrent execution:
# Data collection and analysis + supply chain + guidance (all concurrent)
concurrent_subproc = StrictPartialOrder(
    nodes=[po_data, po_supply, guidance]
)
# No ordering edges: fully concurrent

# Partial order composing after Assign Tasks:
# Concurrent: (data & supply & guidance) --> loop
po_after_assign = StrictPartialOrder(
    nodes=[concurrent_subproc, loop]
)
po_after_assign.order.add_edge(concurrent_subproc, loop)

# Compose the process after Issue Alert:
po_after_alert = StrictPartialOrder(
    nodes=[po_mobilize, po_after_assign]
)
po_after_alert.order.add_edge(po_mobilize, po_after_assign)

# Compose initial process: start --> po_after_alert
po_main = StrictPartialOrder(
    nodes=[po_start, po_after_alert]
)
po_main.order.add_edge(po_start, po_after_alert)

# Final finishing activities post-event: Conduct Debrief --> Compile Lessons
po_debrief = StrictPartialOrder(
    nodes=[Conduct_Debrief, Compile_Lessons]
)
po_debrief.order.add_edge(Conduct_Debrief, Compile_Lessons)

# From loop exit to final activities
po_final = StrictPartialOrder(
    nodes=[po_main, po_debrief]
)
po_final.order.add_edge(po_main, po_debrief)

# Assign final POWL model to root
root = po_final