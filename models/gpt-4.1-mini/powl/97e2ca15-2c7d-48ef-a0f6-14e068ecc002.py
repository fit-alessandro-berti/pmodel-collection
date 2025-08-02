# Generated from: 97e2ca15-2c7d-48ef-a0f6-14e068ecc002.json
# Description: This process involves the seamless coordination of inbound and outbound shipments through a cross-docking facility to minimize storage time and optimize delivery speed. It includes receiving goods, verifying shipment accuracy, sorting items based on destination, real-time inventory synchronization with multiple warehouses, coordinating transport schedules with third-party carriers, handling unexpected discrepancies or delays, updating tracking systems, and ensuring compliance with customs and safety regulations. The process demands close communication between logistics teams, warehouse operators, and IT systems to maintain a continuous flow of goods without bottlenecks, thereby reducing costs and improving customer satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions with exact labels
Shipment_Receive = Transition(label='Shipment Receive')
Verify_Goods = Transition(label='Verify Goods')
Sort_Items = Transition(label='Sort Items')
Update_Inventory = Transition(label='Update Inventory')
Schedule_Transport = Transition(label='Schedule Transport')
Notify_Carriers = Transition(label='Notify Carriers')
Handle_Discrepancies = Transition(label='Handle Discrepancies')
Customs_Check = Transition(label='Customs Check')
Safety_Inspect = Transition(label='Safety Inspect')
Sync_Databases = Transition(label='Sync Databases')
Load_Vehicles = Transition(label='Load Vehicles')
Track_Shipments = Transition(label='Track Shipments')
Confirm_Dispatch = Transition(label='Confirm Dispatch')
Report_Status = Transition(label='Report Status')
Audit_Records = Transition(label='Audit Records')
Feedback_Collect = Transition(label='Feedback Collect')

# Model multiple warehouses inventory sync and third-party carrier coord as parallel branches after Sort_Items

# Branch1: Inventory sync (Sync multiple warehouses)
inventory_sync = StrictPartialOrder(nodes=[Update_Inventory, Sync_Databases])
inventory_sync.order.add_edge(Update_Inventory, Sync_Databases)

# Branch2: Transport schedule with carriers (possibly concurrent with inventory sync)
schedule_notify = StrictPartialOrder(nodes=[Schedule_Transport, Notify_Carriers])
schedule_notify.order.add_edge(Schedule_Transport, Notify_Carriers)

# After sorting, inventory sync and transport scheduling/notify run concurrently
post_sort_parallel = StrictPartialOrder(nodes=[inventory_sync, schedule_notify])
# No order edges between inventory_sync and schedule_notify = they are concurrent

# Handle discrepancies or delays modeled as choice after Verify Goods or during Notify Carriers and Schedule Transport
discrepancy_choice = OperatorPOWL(operator=Operator.XOR, children=[Handle_Discrepancies, SilentTransition()])

# Customs and safety checks likely sequential, after inventory and transport scheduling synced
checks = StrictPartialOrder(nodes=[Customs_Check, Safety_Inspect])
checks.order.add_edge(Customs_Check, Safety_Inspect)

# Loading vehicles after checks
load_and_confirm = StrictPartialOrder(nodes=[Load_Vehicles, Confirm_Dispatch])
load_and_confirm.order.add_edge(Load_Vehicles, Confirm_Dispatch)

# Tracking shipments and reporting status proceed after confirm dispatch
track_and_report = StrictPartialOrder(nodes=[Track_Shipments, Report_Status])
track_and_report.order.add_edge(Track_Shipments, Report_Status)

# Audit records and feedback collected as concluding tasks (possibly concurrent)
audit_feedback = StrictPartialOrder(nodes=[Audit_Records, Feedback_Collect])
# no order edges, concurrent

# Assemble main flow ---------------------------------------------

# Sequence:
# Shipment Receive --> Verify Goods --> discrepancy_choice --> Sort Items --> post_sort_parallel -->
# checks --> load_and_confirm --> track_and_report --> audit_feedback 

root = StrictPartialOrder(nodes=[
    Shipment_Receive,
    Verify_Goods,
    discrepancy_choice,
    Sort_Items,
    post_sort_parallel,
    checks,
    load_and_confirm,
    track_and_report,
    audit_feedback
])

# Add order edges to establish the main sequences
root.order.add_edge(Shipment_Receive, Verify_Goods)
root.order.add_edge(Verify_Goods, discrepancy_choice)
root.order.add_edge(discrepancy_choice, Sort_Items)
root.order.add_edge(Sort_Items, post_sort_parallel)
root.order.add_edge(post_sort_parallel, checks)
root.order.add_edge(checks, load_and_confirm)
root.order.add_edge(load_and_confirm, track_and_report)
root.order.add_edge(track_and_report, audit_feedback)