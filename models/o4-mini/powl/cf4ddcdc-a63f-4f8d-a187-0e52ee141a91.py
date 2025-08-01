# Generated from: cf4ddcdc-a63f-4f8d-a187-0e52ee141a91.json
# Description: This process manages the return and recovery of used or defective products from customers back to the manufacturer or recycler. It involves initial return authorization, transportation scheduling, quality inspection, sorting for refurbishing or disposal, inventory updating, and final disposition. The process ensures efficient handling to minimize waste and maximize value recovery, incorporating coordination between customer service, logistics, warehouse, and environmental compliance teams. It also includes feedback loops for continuous improvement and reporting for regulatory compliance and cost analysis.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
return_request      = Transition(label='Return Request')
authorization_check = Transition(label='Authorization Check')
pickup_schedule     = Transition(label='Pickup Schedule')
transport_dispatch  = Transition(label='Transport Dispatch')
receiving_goods     = Transition(label='Receiving Goods')
quality_inspect     = Transition(label='Quality Inspect')
sort_items          = Transition(label='Sort Items')
refurbish_prep      = Transition(label='Refurbish Prep')
recycle_process     = Transition(label='Recycle Process')
inventory_update    = Transition(label='Inventory Update')
customer_notify     = Transition(label='Customer Notify')
disposal_arrange    = Transition(label='Disposal Arrange')
compliance_audit    = Transition(label='Compliance Audit')
cost_analysis       = Transition(label='Cost Analysis')
report_generate     = Transition(label='Report Generate')

# Subflow: Refurbishing branch
refurbish_branch = StrictPartialOrder(nodes=[refurbish_prep, inventory_update, customer_notify])
refurbish_branch.order.add_edge(refurbish_prep, inventory_update)
refurbish_branch.order.add_edge(inventory_update, customer_notify)

# Subflow: Recycling/Disposal branch
recycle_branch = StrictPartialOrder(nodes=[recycle_process, disposal_arrange])
recycle_branch.order.add_edge(recycle_process, disposal_arrange)

# Choice after sorting
sort_choice = OperatorPOWL(operator=Operator.XOR, children=[refurbish_branch, recycle_branch])

# Main linear flow up to sorting
main_flow = StrictPartialOrder(
    nodes=[
        return_request,
        authorization_check,
        pickup_schedule,
        transport_dispatch,
        receiving_goods,
        quality_inspect,
        sort_items,
        sort_choice
    ]
)
main_flow.order.add_edge(return_request, authorization_check)
main_flow.order.add_edge(authorization_check, pickup_schedule)
main_flow.order.add_edge(pickup_schedule, transport_dispatch)
main_flow.order.add_edge(transport_dispatch, receiving_goods)
main_flow.order.add_edge(receiving_goods, quality_inspect)
main_flow.order.add_edge(quality_inspect, sort_items)
main_flow.order.add_edge(sort_items, sort_choice)

# Feedback/reporting subflow for continuous improvement
feedback_flow = StrictPartialOrder(
    nodes=[compliance_audit, cost_analysis, report_generate]
)
feedback_flow.order.add_edge(compliance_audit, cost_analysis)
feedback_flow.order.add_edge(cost_analysis, report_generate)

# Wrap the whole process in a LOOP for continuous improvement
root = OperatorPOWL(operator=Operator.LOOP, children=[main_flow, feedback_flow])