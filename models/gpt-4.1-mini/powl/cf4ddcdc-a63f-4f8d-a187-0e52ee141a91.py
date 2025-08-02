# Generated from: cf4ddcdc-a63f-4f8d-a187-0e52ee141a91.json
# Description: This process manages the return and recovery of used or defective products from customers back to the manufacturer or recycler. It involves initial return authorization, transportation scheduling, quality inspection, sorting for refurbishing or disposal, inventory updating, and final disposition. The process ensures efficient handling to minimize waste and maximize value recovery, incorporating coordination between customer service, logistics, warehouse, and environmental compliance teams. It also includes feedback loops for continuous improvement and reporting for regulatory compliance and cost analysis.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
Return_Request = Transition(label='Return Request')
Authorization_Check = Transition(label='Authorization Check')
Pickup_Schedule = Transition(label='Pickup Schedule')
Transport_Dispatch = Transition(label='Transport Dispatch')
Receiving_Goods = Transition(label='Receiving Goods')
Quality_Inspect = Transition(label='Quality Inspect')
Sort_Items = Transition(label='Sort Items')
Refurbish_Prep = Transition(label='Refurbish Prep')
Recycle_Process = Transition(label='Recycle Process')
Inventory_Update = Transition(label='Inventory Update')
Customer_Notify = Transition(label='Customer Notify')
Disposal_Arrange = Transition(label='Disposal Arrange')
Compliance_Audit = Transition(label='Compliance Audit')
Cost_Analysis = Transition(label='Cost Analysis')
Report_Generate = Transition(label='Report Generate')

skip = SilentTransition()

# Loop for continuous improvement and feedback:
# loop = *(Quality_Inspect + downstream, Compliance_Audit + Cost_Analysis and Report_Generate)
# model loop as LOOP(primary=Quality_Inspect with downstream activities, secondary=feedback + report)

# Subprocess: Refurbish or Recycle choice after sorting
refurbish_path = StrictPartialOrder(nodes=[Refurbish_Prep, Inventory_Update, Customer_Notify])
refurbish_path.order.add_edge(Refurbish_Prep, Inventory_Update)
refurbish_path.order.add_edge(Inventory_Update, Customer_Notify)

recycle_path = StrictPartialOrder(nodes=[Recycle_Process, Inventory_Update])
recycle_path.order.add_edge(Recycle_Process, Inventory_Update)

disposal_path = StrictPartialOrder(nodes=[Disposal_Arrange, Inventory_Update])
disposal_path.order.add_edge(Disposal_Arrange, Inventory_Update)

# Choice after Sort_Items among refurbish, recycle, disposal (disposal optional but included)
refurbish_recycle_disposal_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[refurbish_path, recycle_path, disposal_path]
)

# Main partial order for initial process until Sort_Items
initial_process = StrictPartialOrder(
    nodes=[
        Return_Request, Authorization_Check, Pickup_Schedule,
        Transport_Dispatch, Receiving_Goods, Quality_Inspect, Sort_Items
    ]
)
initial_process.order.add_edge(Return_Request, Authorization_Check)
initial_process.order.add_edge(Authorization_Check, Pickup_Schedule)
initial_process.order.add_edge(Pickup_Schedule, Transport_Dispatch)
initial_process.order.add_edge(Transport_Dispatch, Receiving_Goods)
initial_process.order.add_edge(Receiving_Goods, Quality_Inspect)
initial_process.order.add_edge(Quality_Inspect, Sort_Items)

# From Sort_Items to refurbish/recycle/disposal choices
# Order edges to connect Sort_Items to the choice operator
main_with_choice = StrictPartialOrder(
    nodes=[initial_process, refurbish_recycle_disposal_choice]
)
main_with_choice.order.add_edge(initial_process, refurbish_recycle_disposal_choice)

# Loop to model continuous improvement and reporting feedback:
# loop: execute Quality_Inspect and then either exit or do Compliance_Audit + Cost_Analysis + Report_Generate then Quality_Inspect again

feedback_report = StrictPartialOrder(
    nodes=[Compliance_Audit, Cost_Analysis, Report_Generate]
)
feedback_report.order.add_edge(Compliance_Audit, Cost_Analysis)
feedback_report.order.add_edge(Cost_Analysis, Report_Generate)

loop_feedback = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Quality_Inspect, feedback_report]
)

# Assemble the top-level partial order:
# the process consists of initial steps (until Quality_Inspect, Sort, refurb/recycle/disposal),
# plus loop_feedback triggered at Quality_Inspect (so Sort_Items waits for first Quality_Inspect, loop on Quality_Inspect after feedback)

# To integrate loop_feedback properly, we replace Quality_Inspect in initial_process with the loop

# Build the initial steps before Quality_Inspect:
before_QI = StrictPartialOrder(
    nodes=[Return_Request, Authorization_Check, Pickup_Schedule,
           Transport_Dispatch, Receiving_Goods]
)
before_QI.order.add_edge(Return_Request, Authorization_Check)
before_QI.order.add_edge(Authorization_Check, Pickup_Schedule)
before_QI.order.add_edge(Pickup_Schedule, Transport_Dispatch)
before_QI.order.add_edge(Transport_Dispatch, Receiving_Goods)

# Order before_QI --> loop_feedback --> Sort_Items --> refurbish_recycle_disposal_choice

top_level = StrictPartialOrder(
    nodes=[before_QI, loop_feedback, Sort_Items, refurbish_recycle_disposal_choice]
)
top_level.order.add_edge(before_QI, loop_feedback)
top_level.order.add_edge(loop_feedback, Sort_Items)
top_level.order.add_edge(Sort_Items, refurbish_recycle_disposal_choice)

root = top_level