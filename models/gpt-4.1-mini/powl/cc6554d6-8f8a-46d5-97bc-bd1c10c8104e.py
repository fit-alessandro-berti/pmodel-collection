# Generated from: cc6554d6-8f8a-46d5-97bc-bd1c10c8104e.json
# Description: This process involves dynamically adjusting the supply chain network in response to real-time disruptions such as supplier failures, transportation delays, or sudden demand fluctuations. It integrates predictive analytics with automated decision-making to reroute shipments, reallocate inventory, and engage alternative suppliers. The process ensures continuity by balancing cost, speed, and risk while maintaining compliance with regulatory constraints. Continuous feedback loops enable learning and refinement of strategies to improve resilience and agility over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Demand_Forecast = Transition(label='Demand Forecast')
Risk_Assess = Transition(label='Risk Assess')
Supplier_Audit = Transition(label='Supplier Audit')
Inventory_Scan = Transition(label='Inventory Scan')
Route_Optimize = Transition(label='Route Optimize')
Order_Prioritize = Transition(label='Order Prioritize')
Contract_Review = Transition(label='Contract Review')
Delay_Monitor = Transition(label='Delay Monitor')
Shipment_Reroute = Transition(label='Shipment Reroute')
Cost_Analyze = Transition(label='Cost Analyze')
Compliance_Check = Transition(label='Compliance Check')
Alternative_Engage = Transition(label='Alternative Engage')
Inventory_Reallocate = Transition(label='Inventory Reallocate')
Performance_Track = Transition(label='Performance Track')
Feedback_Loop = Transition(label='Feedback Loop')
Strategy_Update = Transition(label='Strategy Update')

# Partial order for analytics and initial assessments (concurrent where meaningful)
analytics_and_assess = StrictPartialOrder(nodes=[Demand_Forecast, Risk_Assess, Supplier_Audit, Inventory_Scan])
# No edges, all concurrent - these happen in parallel for real-time insight

# Partial order for decision making: 
# After analytics, Contract Review must happen before Route Optimize and Order Prioritize, which can be concurrent
decision_preparation = StrictPartialOrder(
    nodes=[Contract_Review, Route_Optimize, Order_Prioritize]
)
decision_preparation.order.add_edge(Contract_Review, Route_Optimize)
decision_preparation.order.add_edge(Contract_Review, Order_Prioritize)

# Partial order for disruption monitoring and reactive actions:
# Delay Monitor precedes Shipment Reroute; Alternative Engage and Inventory Reallocate happen after Shipment Reroute concurrently
disruption_response = StrictPartialOrder(
    nodes=[Delay_Monitor, Shipment_Reroute, Alternative_Engage, Inventory_Reallocate]
)
disruption_response.order.add_edge(Delay_Monitor, Shipment_Reroute)
disruption_response.order.add_edge(Shipment_Reroute, Alternative_Engage)
disruption_response.order.add_edge(Shipment_Reroute, Inventory_Reallocate)

# Partial order for cost, compliance and performance tracking:
cost_compliance_performance = StrictPartialOrder(
    nodes=[Cost_Analyze, Compliance_Check, Performance_Track]
)
cost_compliance_performance.order.add_edge(Cost_Analyze, Compliance_Check)
cost_compliance_performance.order.add_edge(Compliance_Check, Performance_Track)

# Feedback Loop and Strategy Update form a loop where:
# Execute Feedback Loop, then choose to exit or do Strategy Update and then repeat the Feedback Loop
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Feedback_Loop, Strategy_Update]
)

# Assemble the main process partial order:
# Step 1: analytics_and_assess
# Step 2: decision_preparation (depends on analytics_and_assess)
# Step 3 (can run concurrently after decision_preparation): disruption_response and cost_compliance_performance
# Step 4: feedback_loop runs after those

root = StrictPartialOrder(
    nodes=[analytics_and_assess, decision_preparation, disruption_response, cost_compliance_performance, feedback_loop]
)

# Add ordering edges:
root.order.add_edge(analytics_and_assess, decision_preparation)
root.order.add_edge(decision_preparation, disruption_response)
root.order.add_edge(decision_preparation, cost_compliance_performance)
root.order.add_edge(disruption_response, feedback_loop)
root.order.add_edge(cost_compliance_performance, feedback_loop)