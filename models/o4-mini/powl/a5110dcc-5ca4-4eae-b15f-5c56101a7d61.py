# Generated from: a5110dcc-5ca4-4eae-b15f-5c56101a7d61.json
# Description: This process involves the end-to-end management of a remote drone fleet used for agricultural monitoring. It includes scheduling drone missions based on crop data, performing pre-flight health diagnostics, establishing secure communication channels, conducting autonomous flight operations, collecting multispectral imagery, transmitting data to cloud servers, processing images with AI algorithms, generating actionable insights for farmers, managing battery swaps and maintenance, updating firmware remotely, handling emergency recalls, coordinating with air traffic control, and archiving flight logs for regulatory compliance. The process ensures efficient and compliant drone utilization to optimize crop yields while minimizing operational risks and costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
t_mission   = Transition(label='Mission Setup')
t_health    = Transition(label='Health Check')
t_comm      = Transition(label='Comm Link')
t_launch    = Transition(label='Flight Launch')
t_traffic   = Transition(label='Traffic Coord')
t_capture   = Transition(label='Data Capture')
t_upload    = Transition(label='Data Upload')
t_ip        = Transition(label='Image Process')
t_insight   = Transition(label='Insight Gen')
t_log       = Transition(label='Log Archive')
t_recall    = Transition(label='Recall Handle')
t_swap      = Transition(label='Battery Swap')
t_maint     = Transition(label='Maintenance')
t_fw        = Transition(label='Firmware Update')
t_compl1    = Transition(label='Compliance Check')  # after recall
t_compl2    = Transition(label='Compliance Check')  # after firmware update

# 1) Flight subprocess: Flight Launch -> Traffic Coord & Data Capture -> Data Upload -> Image Process -> Insight Gen -> Log Archive
flight_po = StrictPartialOrder(nodes=[t_launch, t_traffic, t_capture, t_upload, t_ip, t_insight, t_log])
flight_po.order.add_edge(t_launch,  t_traffic)
flight_po.order.add_edge(t_launch,  t_capture)
flight_po.order.add_edge(t_traffic, t_capture)
flight_po.order.add_edge(t_capture, t_upload)
flight_po.order.add_edge(t_upload,  t_ip)
flight_po.order.add_edge(t_ip,      t_insight)
flight_po.order.add_edge(t_insight, t_log)

# 2) Recall subprocess: Recall Handle -> Log Archive -> Compliance Check
recall_po = StrictPartialOrder(nodes=[t_recall, t_log, t_compl1])
recall_po.order.add_edge(t_recall, t_log)
recall_po.order.add_edge(t_log,    t_compl1)

# 3) XOR between normal flight and emergency recall
xor_branch = OperatorPOWL(operator=Operator.XOR, children=[flight_po, recall_po])

# 4) Mission setup sequence: Mission Setup -> Health Check -> Comm Link -> (XOR branch)
mission_po = StrictPartialOrder(nodes=[t_mission, t_health, t_comm, xor_branch])
mission_po.order.add_edge(t_mission, t_health)
mission_po.order.add_edge(t_health,  t_comm)
mission_po.order.add_edge(t_comm,    xor_branch)

# 5) Maintenance loop after missions:
#    A = Battery Swap -> Maintenance
#    B = Firmware Update -> Compliance Check
A = StrictPartialOrder(nodes=[t_swap, t_maint])
A.order.add_edge(t_swap,  t_maint)
B = StrictPartialOrder(nodes=[t_fw, t_compl2])
B.order.add_edge(t_fw,   t_compl2)
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# 6) Root: mission flow followed by maintenance loop
root = StrictPartialOrder(nodes=[mission_po, maintenance_loop])
root.order.add_edge(mission_po, maintenance_loop)