# Generated from: 6b479d57-c0d4-459e-acdd-ca1d1d137d3f.json
# Description: This process involves dynamically adjusting supply chain operations in response to real-time market fluctuations, supplier disruptions, and customer demand shifts. It integrates predictive analytics, autonomous procurement, and collaborative logistics to minimize delays and costs while maximizing responsiveness. The process requires continuous monitoring, rapid decision-making, and cross-functional coordination between procurement, production, and distribution teams to maintain optimal inventory levels and service quality under uncertain conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as Transitions
Demand_Forecast = Transition(label='Demand Forecast')
Supplier_Audit = Transition(label='Supplier Audit')
Risk_Assess = Transition(label='Risk Assess')
Inventory_Sync = Transition(label='Inventory Sync')
Order_Prioritize = Transition(label='Order Prioritize')
Procure_Auto = Transition(label='Procure Auto')
Quality_Check = Transition(label='Quality Check')
Logistics_Plan = Transition(label='Logistics Plan')
Route_Optimize = Transition(label='Route Optimize')
Shipment_Track = Transition(label='Shipment Track')
Exception_Alert = Transition(label='Exception Alert')
Stock_Rebalance = Transition(label='Stock Rebalance')
Customer_Notify = Transition(label='Customer Notify')
Feedback_Capture = Transition(label='Feedback Capture')
Performance_Review = Transition(label='Performance Review')
Adjust_Strategy = Transition(label='Adjust Strategy')

# Define silent transition used in choices or loop exits
skip = SilentTransition()

# Define choice branches for monitoring and assessing risks:
# After Demand Forecast, do either Supplier Audit or Risk Assess (choice)
monitoring_choice = OperatorPOWL(operator=Operator.XOR, children=[Supplier_Audit, Risk_Assess])

# Synchronize inventory and prioritize orders in sequence (partial order)
inv_order_PO = StrictPartialOrder(nodes=[Inventory_Sync, Order_Prioritize])
inv_order_PO.order.add_edge(Inventory_Sync, Order_Prioritize)

# Procurement followed by Quality Check - partial order
procure_PO = StrictPartialOrder(nodes=[Procure_Auto, Quality_Check])
procure_PO.order.add_edge(Procure_Auto, Quality_Check)

# Logistics plan, Route optimization, Shipment track run sequentially
logistics_PO = StrictPartialOrder(nodes=[Logistics_Plan, Route_Optimize, Shipment_Track])
logistics_PO.order.add_edge(Logistics_Plan, Route_Optimize)
logistics_PO.order.add_edge(Route_Optimize, Shipment_Track)

# Exception alert can happen concurrently with logistics
exception_alert = Exception_Alert

# Stock Rebalance triggered after exception alert or normal flow completes - choice
stock_rebalance_choice = OperatorPOWL(operator=Operator.XOR, children=[Stock_Rebalance, skip])

# Customer notify and feedback capture run sequentially
customer_PO = StrictPartialOrder(nodes=[Customer_Notify, Feedback_Capture])
customer_PO.order.add_edge(Customer_Notify, Feedback_Capture)

# Performance review and adjustment strategy form a loop:
# Perform Performance Review, then choose to exit or Adjust Strategy then repeat
perf_loop = OperatorPOWL(operator=Operator.LOOP, children=[Performance_Review, Adjust_Strategy])

# Now combine all as partial order:

# Nodes:
# Demand_Forecast --> monitoring_choice
# monitoring_choice --> inv_order_PO
# inv_order_PO --> procure_PO
# procure_PO --> logistics_PO
# logistics_PO and exception_alert concurrent (no order)
# exception_alert and logistics_PO --> stock_rebalance_choice
# stock_rebalance_choice --> customer_PO
# customer_PO --> perf_loop

nodes = [
    Demand_Forecast,
    monitoring_choice,
    inv_order_PO,
    procure_PO,
    logistics_PO,
    exception_alert,
    stock_rebalance_choice,
    customer_PO,
    perf_loop
]

root = StrictPartialOrder(nodes=nodes)

# Set order edges according to above description:
root.order.add_edge(Demand_Forecast, monitoring_choice)
root.order.add_edge(monitoring_choice, inv_order_PO)
root.order.add_edge(inv_order_PO, procure_PO)
root.order.add_edge(procure_PO, logistics_PO)
# logistics_PO and exception_alert concurrent => no edge

root.order.add_edge(logistics_PO, stock_rebalance_choice)
root.order.add_edge(exception_alert, stock_rebalance_choice)

root.order.add_edge(stock_rebalance_choice, customer_PO)
root.order.add_edge(customer_PO, perf_loop)