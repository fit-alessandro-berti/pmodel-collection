# Generated from: 1795163a-8ca8-46d7-8f0b-0dc4febfdabb.json
# Description: This process manages the complex coordination involved in swapping transport assets between multiple logistics providers across different regions. It includes verification of asset conditions, regulatory compliance checks, scheduling synchronized handoffs, and reconciling financial and legal obligations. The process ensures that assets such as containers, vehicles, or equipment are efficiently exchanged while minimizing downtime and maintaining traceability through digital ledgers and real-time communication channels, adapting dynamically to delays or discrepancies detected during transit or inspection phases.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions with the exact given labels
Asset_Verify = Transition(label='Asset Verify')
Condition_Check = Transition(label='Condition Check')
Compliance_Audit = Transition(label='Compliance Audit')
Schedule_Sync = Transition(label='Schedule Sync')
Handoff_Confirm = Transition(label='Handoff Confirm')
Documentation_Review = Transition(label='Documentation Review')
Financial_Reconcile = Transition(label='Financial Reconcile')
Legal_Validate = Transition(label='Legal Validate')
Ledger_Update = Transition(label='Ledger Update')
Communication_Alert = Transition(label='Communication Alert')
Delay_Monitor = Transition(label='Delay Monitor')
Discrepancy_Flag = Transition(label='Discrepancy Flag')
Transit_Track = Transition(label='Transit Track')
Inspection_Report = Transition(label='Inspection Report')
Final_Approval = Transition(label='Final Approval')
Swap_Execute = Transition(label='Swap Execute')

# Model inspection with possible delay/discrepancy detection loop
# Loop: do Transit_Track and Inspection_Report,
# then choose to either exit or handle issues: (Delay_Monitor XOR Discrepancy_Flag),
# then repeat the inspection after handling issues.
inspection_handling = OperatorPOWL(operator=Operator.XOR, children=[Delay_Monitor, Discrepancy_Flag])
inspection_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    StrictPartialOrder(nodes=[Transit_Track, Inspection_Report]),
    inspection_handling
])

# After inspection and handling, final approval must occur
# Followed by swap execution
final_part = StrictPartialOrder(nodes=[Final_Approval, Swap_Execute])
final_part.order.add_edge(Final_Approval, Swap_Execute)

# Build initial verification and audit partial order
# Asset Verify -> Condition Check -> Compliance Audit
verification_po = StrictPartialOrder(nodes=[Asset_Verify, Condition_Check, Compliance_Audit])
verification_po.order.add_edge(Asset_Verify, Condition_Check)
verification_po.order.add_edge(Condition_Check, Compliance_Audit)

# Scheduling and handoff partial order: Schedule Sync -> Handoff Confirm
scheduling_po = StrictPartialOrder(nodes=[Schedule_Sync, Handoff_Confirm])
scheduling_po.order.add_edge(Schedule_Sync, Handoff_Confirm)

# Documentation and reconciliation partial order:
# Documentation Review -> Financial Reconcile -> Legal Validate -> Ledger Update
doc_finance_po = StrictPartialOrder(nodes=[Documentation_Review, Financial_Reconcile, Legal_Validate, Ledger_Update])
doc_finance_po.order.add_edge(Documentation_Review, Financial_Reconcile)
doc_finance_po.order.add_edge(Financial_Reconcile, Legal_Validate)
doc_finance_po.order.add_edge(Legal_Validate, Ledger_Update)

# Communication alert can happen concurrently anytime after scheduling
# We'll model communication alert as parallel to handoff confirm or ledger update
# To model concurrency, include Communication Alert in partial order with no edges to/from scheduling_po and doc_finance_po (but they will be in the overall PO)

# Now combine all into the overall process partial order

# Nodes are:
# verification_po, scheduling_po, doc_finance_po, Communication_Alert,
# inspection_loop, final_part

# To keep finer control, embed verification_po, scheduling_po, doc_finance_po as nodes inside the root PO:
# Use the StrictPartialOrder on their nodes for their internal order.

# The overall order is:
# verification_po must complete before scheduling_po and doc_finance_po start
# scheduling_po and doc_finance_po must complete before inspection_loop starts
# inspection_loop finishes before final_part
# Communication_Alert is concurrent starting after scheduling or doc_finance_po start (to simplify, we put it concurrent with scheduling and doc_finance_po)

# Let's define root PO including all nodes:
root_nodes = [
    verification_po,
    scheduling_po,
    doc_finance_po,
    Communication_Alert,
    inspection_loop,
    final_part
]

root = StrictPartialOrder(nodes=root_nodes)

# Add edges based on dependencies:
# verification_po --> scheduling_po
root.order.add_edge(verification_po, scheduling_po)
# verification_po --> doc_finance_po
root.order.add_edge(verification_po, doc_finance_po)

# scheduling_po --> inspection_loop
root.order.add_edge(scheduling_po, inspection_loop)
# doc_finance_po --> inspection_loop
root.order.add_edge(doc_finance_po, inspection_loop)

# inspection_loop --> final_part
root.order.add_edge(inspection_loop, final_part)