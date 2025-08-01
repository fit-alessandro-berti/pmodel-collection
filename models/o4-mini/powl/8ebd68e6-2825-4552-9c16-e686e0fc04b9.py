# Generated from: 8ebd68e6-2825-4552-9c16-e686e0fc04b9.json
# Description: This process manages the complex flow of returned goods from customers back to the warehouse, ensuring accurate inspection, refurbishment, and redistribution or disposal. It involves coordination between multiple departments including customer service, quality control, and logistics to validate return reasons, assess product conditions, execute necessary repairs, and update inventory records. The process also incorporates compliance checks for hazardous materials and environmental regulations, re-packaging of items for resale, and financial reconciliation for refunds or credits. Continuous monitoring and reporting are embedded to optimize return rates and reduce waste, making the reverse logistics audit a critical yet atypical business operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
return_initiation   = Transition(label='Return Initiation')
label_generation    = Transition(label='Label Generation')
pickup_scheduling   = Transition(label='Pickup Scheduling')
goods_receipt       = Transition(label='Goods Receipt')
condition_inspection= Transition(label='Condition Inspection')
compliance_check    = Transition(label='Compliance Check')
disposal_decision   = Transition(label='Disposal Decision')
repair_assignment   = Transition(label='Repair Assignment')
refurbishment_work  = Transition(label='Refurbishment Work')
quality_approval    = Transition(label='Quality Approval')
inventory_update    = Transition(label='Inventory Update')
repackaging         = Transition(label='Repackaging')
restock_placement   = Transition(label='Restock Placement')
credit_processing   = Transition(label='Credit Processing')
performance_review  = Transition(label='Performance Review')
report_generation   = Transition(label='Report Generation')

# 1) Pre‐processing sequence: Return Initiation -> Label Generation -> Pickup Scheduling -> Goods Receipt -> Condition Inspection -> Compliance Check
po_pre = StrictPartialOrder(nodes=[
    return_initiation, label_generation, pickup_scheduling,
    goods_receipt, condition_inspection, compliance_check
])
po_pre.order.add_edge(return_initiation, label_generation)
po_pre.order.add_edge(label_generation, pickup_scheduling)
po_pre.order.add_edge(pickup_scheduling, goods_receipt)
po_pre.order.add_edge(goods_receipt, condition_inspection)
po_pre.order.add_edge(condition_inspection, compliance_check)

# 2) Refurbishment branch: Repair Assignment -> Refurbishment Work -> Quality Approval -> Inventory Update -> Repackaging -> Restock Placement
po_refurb = StrictPartialOrder(nodes=[
    repair_assignment, refurbishment_work,
    quality_approval, inventory_update,
    repackaging, restock_placement
])
po_refurb.order.add_edge(repair_assignment, refurbishment_work)
po_refurb.order.add_edge(refurbishment_work, quality_approval)
po_refurb.order.add_edge(quality_approval, inventory_update)
po_refurb.order.add_edge(inventory_update, repackaging)
po_refurb.order.add_edge(repackaging, restock_placement)

# 3) Choice after compliance: either Disposal Decision or Refurbishment branch
xor_after_check = OperatorPOWL(
    operator=Operator.XOR,
    children=[disposal_decision, po_refurb]
)

# 4) Continuous monitoring/reporting loop: Performance Review then Report Generation, looping
loop_monitoring = OperatorPOWL(
    operator=Operator.LOOP,
    children=[performance_review, report_generation]
)

# 5) Assemble the whole process: pre‐sequence -> XOR branch -> Credit Processing -> monitoring loop
root = StrictPartialOrder(nodes=[
    po_pre,
    xor_after_check,
    credit_processing,
    loop_monitoring
])
root.order.add_edge(po_pre, xor_after_check)
root.order.add_edge(xor_after_check, credit_processing)
root.order.add_edge(credit_processing, loop_monitoring)