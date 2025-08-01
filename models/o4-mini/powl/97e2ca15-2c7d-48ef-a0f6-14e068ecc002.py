# Generated from: 97e2ca15-2c7d-48ef-a0f6-14e068ecc002.json
# Description: This process involves the seamless coordination of inbound and outbound shipments through a cross-docking facility to minimize storage time and optimize delivery speed. It includes receiving goods, verifying shipment accuracy, sorting items based on destination, real-time inventory synchronization with multiple warehouses, coordinating transport schedules with third-party carriers, handling unexpected discrepancies or delays, updating tracking systems, and ensuring compliance with customs and safety regulations. The process demands close communication between logistics teams, warehouse operators, and IT systems to maintain a continuous flow of goods without bottlenecks, thereby reducing costs and improving customer satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sr       = Transition(label='Shipment Receive')
vg       = Transition(label='Verify Goods')
sort_it  = Transition(label='Sort Items')
upd_inv  = Transition(label='Update Inventory')
sync_db  = Transition(label='Sync Databases')
sched    = Transition(label='Schedule Transport')
notif    = Transition(label='Notify Carriers')
hd       = Transition(label='Handle Discrepancies')
cust     = Transition(label='Customs Check')
safety   = Transition(label='Safety Inspect')
load_v   = Transition(label='Load Vehicles')
conf     = Transition(label='Confirm Dispatch')
track    = Transition(label='Track Shipments')
report   = Transition(label='Report Status')
audit    = Transition(label='Audit Records')
feedback = Transition(label='Feedback Collect')

# Loop for handling discrepancies (zero or more times)
skip     = SilentTransition()
disc_loop = OperatorPOWL(operator=Operator.LOOP, children=[skip, hd])

# Build the partial order
root = StrictPartialOrder(nodes=[
    sr, vg, sort_it,
    upd_inv, sync_db,
    sched, notif,
    disc_loop,
    cust, safety,
    load_v, conf,
    track, report,
    audit, feedback
])

# Sequential and concurrent dependencies
root.order.add_edge(sr, vg)
root.order.add_edge(vg, sort_it)

# After sorting, update inventory and sync databases in parallel
root.order.add_edge(sort_it, upd_inv)
root.order.add_edge(sort_it, sync_db)

# Both upd_inv and sync_db precede scheduling
root.order.add_edge(upd_inv, sched)
root.order.add_edge(sync_db, sched)

root.order.add_edge(sched, notif)
root.order.add_edge(notif, disc_loop)

# After discrepancy loop, do customs check and safety inspect in parallel
root.order.add_edge(disc_loop, cust)
root.order.add_edge(disc_loop, safety)

# Customs and safety both precede loading
root.order.add_edge(cust, load_v)
root.order.add_edge(safety, load_v)

root.order.add_edge(load_v, conf)

# After confirm, track and report in parallel
root.order.add_edge(conf, track)
root.order.add_edge(conf, report)

# Track and report both precede audit
root.order.add_edge(track, audit)
root.order.add_edge(report, audit)

root.order.add_edge(audit, feedback)