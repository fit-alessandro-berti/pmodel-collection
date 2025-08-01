# Generated from: 8ebd68e6-2825-4552-9c16-e686e0fc04b9.json
# Description: This process manages the complex flow of returned goods from customers back to the warehouse, ensuring accurate inspection, refurbishment, and redistribution or disposal. It involves coordination between multiple departments including customer service, quality control, and logistics to validate return reasons, assess product conditions, execute necessary repairs, and update inventory records. The process also incorporates compliance checks for hazardous materials and environmental regulations, re-packaging of items for resale, and financial reconciliation for refunds or credits. Continuous monitoring and reporting are embedded to optimize return rates and reduce waste, making the reverse logistics audit a critical yet atypical business operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Return_Initiation = Transition(label='Return Initiation')
Label_Generation = Transition(label='Label Generation')
Pickup_Scheduling = Transition(label='Pickup Scheduling')
Goods_Receipt = Transition(label='Goods Receipt')
Condition_Inspection = Transition(label='Condition Inspection')
Compliance_Check = Transition(label='Compliance Check')
Repair_Assignment = Transition(label='Repair Assignment')
Refurbishment_Work = Transition(label='Refurbishment Work')
Quality_Approval = Transition(label='Quality Approval')
Inventory_Update = Transition(label='Inventory Update')
Repackaging = Transition(label='Repackaging')
Restock_Placement = Transition(label='Restock Placement')
Disposal_Decision = Transition(label='Disposal Decision')
Credit_Processing = Transition(label='Credit Processing')
Performance_Review = Transition(label='Performance Review')
Report_Generation = Transition(label='Report Generation')

# Disposal path or restock path choice after Quality Approval
restock_path = StrictPartialOrder(nodes=[Inventory_Update, Repackaging, Restock_Placement])
restock_path.order.add_edge(Inventory_Update, Repackaging)
restock_path.order.add_edge(Repackaging, Restock_Placement)

disposal_path = StrictPartialOrder(nodes=[Disposal_Decision])

after_quality_choice = OperatorPOWL(operator=Operator.XOR, children=[restock_path, disposal_path])

# Credit processing and Performance Review + Report Generation (concurrent)
credit_and_review = StrictPartialOrder(nodes=[Credit_Processing, Performance_Review, Report_Generation])
credit_and_review.order.add_edge(Performance_Review, Report_Generation)

# Condition Inspection -> Compliance Check -> (Repair cycle or skip repair)
# Loop: do Repair_Assignment -> Refurbishment_Work -> Quality_Approval, then either exit or repeat
repair_loop_body = StrictPartialOrder(nodes=[Repair_Assignment, Refurbishment_Work, Quality_Approval])
repair_loop_body.order.add_edge(Repair_Assignment, Refurbishment_Work)
repair_loop_body.order.add_edge(Refurbishment_Work, Quality_Approval)

repair_loop = OperatorPOWL(operator=Operator.LOOP, children=[repair_loop_body, SilentTransition()])

# After Quality Approval: choose disposal or restock
quality_and_after = StrictPartialOrder(nodes=[repair_loop, after_quality_choice])
quality_and_after.order.add_edge(repair_loop, after_quality_choice)

# Goods Receipt -> Condition Inspection -> Compliance Check -> repair_loop + after_quality_choice sequence
inspection_flow = StrictPartialOrder(
    nodes=[Goods_Receipt, Condition_Inspection, Compliance_Check, quality_and_after]
)
inspection_flow.order.add_edge(Goods_Receipt, Condition_Inspection)
inspection_flow.order.add_edge(Condition_Inspection, Compliance_Check)
inspection_flow.order.add_edge(Compliance_Check, quality_and_after)

# Pickup Scheduling -> Goods Receipt (pickup delivered, then goods received)
pickup_flow = StrictPartialOrder(nodes=[Pickup_Scheduling, inspection_flow])
pickup_flow.order.add_edge(Pickup_Scheduling, inspection_flow)

# Return Initiation -> Label Generation -> Pickup Scheduling flow
initial_flow = StrictPartialOrder(nodes=[Return_Initiation, Label_Generation, pickup_flow])
initial_flow.order.add_edge(Return_Initiation, Label_Generation)
initial_flow.order.add_edge(Label_Generation, pickup_flow)

# Final concurrent with Credit Processing + Performance Review & Report Generation
root = StrictPartialOrder(
    nodes=[initial_flow, credit_and_review]
)
root.order.add_edge(initial_flow, credit_and_review)