# Generated from: af2ad303-7f6a-4093-8dcd-fff50c8d6bbf.json
# Description: This process orchestrates the synchronization of customer loyalty data across multiple sales channels including in-store, online, mobile app, and third-party partners. It involves real-time data validation, conflict resolution for overlapping rewards, dynamic points recalculation based on channel-specific promotions, and secure data exchange protocols. Additionally, it incorporates anomaly detection to flag suspicious activity, automated customer notifications about point updates or expirations, and a feedback loop to update marketing strategies based on loyalty trends. The process ensures consistency and accuracy of loyalty benefits while enhancing customer engagement and preventing fraud across diverse platforms.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
ingest      = Transition(label='Data Ingest')
validate    = Transition(label='Validate Entries')
conflict    = Transition(label='Conflict Check')
promo       = Transition(label='Promo Apply')
recalc      = Transition(label='Points Recalc')
fraud       = Transition(label='Fraud Scan')
sync        = Transition(label='Sync Partners')
update      = Transition(label='Update Ledger')
notify      = Transition(label='Notify User')
trend       = Transition(label='Trend Analyze')
feedback    = Transition(label='Feedback Loop')
adjust      = Transition(label='Adjust Rules')
archive     = Transition(label='Archive Logs')
report      = Transition(label='Report Generate')
audit       = Transition(label='Audit Trail')

# Build the feedback‐loop substructure: after Trend Analyze,
# execute Feedback Loop then Adjust Rules, then return.
feedback_po = StrictPartialOrder(nodes=[feedback, adjust])
feedback_po.order.add_edge(feedback, adjust)
loop        = OperatorPOWL(operator=Operator.LOOP, children=[trend, feedback_po])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    ingest, validate, conflict, promo, recalc, fraud,
    sync, update, notify, loop, archive, report, audit
])

# Define the sequencing dependencies
root.order.add_edge(ingest,   validate)
root.order.add_edge(validate, conflict)
root.order.add_edge(conflict, promo)
root.order.add_edge(promo,    recalc)
root.order.add_edge(recalc,   fraud)
root.order.add_edge(fraud,    sync)
root.order.add_edge(sync,     update)
root.order.add_edge(update,   notify)
root.order.add_edge(notify,   loop)
root.order.add_edge(loop,     archive)
root.order.add_edge(archive,  report)
root.order.add_edge(report,   audit)