# Generated from: 34a2c51d-9bce-4097-ab23-fab549721bea.json
# Description: This process involves dynamically managing a multi-tier supply chain using real-time data feeds and AI-driven decision making to optimize inventory levels, transportation routes, and supplier selection. It integrates continuous risk assessment with automated contingency planning to mitigate disruptions caused by geopolitical events, natural disasters, or sudden demand shifts. The process requires constant synchronization between procurement, logistics, and production units, enabling rapid adaptation to market variability while maintaining cost efficiency and customer satisfaction. It employs predictive analytics to forecast demand fluctuations and leverages blockchain for transparent transaction tracking across all stakeholders, ensuring compliance and traceability throughout the supply chain lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
Data_Ingestion = Transition(label='Data Ingestion')
Risk_Scanning = Transition(label='Risk Scanning')
Demand_Forecast = Transition(label='Demand Forecast')
Supplier_Scoring = Transition(label='Supplier Scoring')
Inventory_Sync = Transition(label='Inventory Sync')
Route_Optimize = Transition(label='Route Optimize')
Order_Validation = Transition(label='Order Validation')
Contingency_Plan = Transition(label='Contingency Plan')
Contract_Review = Transition(label='Contract Review')
Logistics_Align = Transition(label='Logistics Align')
Production_Sync = Transition(label='Production Sync')
Compliance_Check = Transition(label='Compliance Check')
Anomaly_Detect = Transition(label='Anomaly Detect')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Blockchain_Audit = Transition(label='Blockchain Audit')
Performance_Review = Transition(label='Performance Review')

# Silent transition for flexible choice points or concurrency blockers if needed
skip = SilentTransition()

# Predictive analytics and anomaly detection feeding into demand forecast
analytics_po = StrictPartialOrder(nodes=[Demand_Forecast, Anomaly_Detect])
analytics_po.order.add_edge(Anomaly_Detect, Demand_Forecast)

# Risk scanning leads to contingency plan and contract review loop (continuous risk assessment)
risk_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Risk_Scanning,
        StrictPartialOrder(nodes=[Contingency_Plan, Contract_Review])
    ]
)

# Procurement branch: Supplier scoring then contract review (contract review involved also in risk loop)
procurement_po = StrictPartialOrder(nodes=[Supplier_Scoring, Contract_Review])
procurement_po.order.add_edge(Supplier_Scoring, Contract_Review)

# Inventory and route optimization running concurrently but after demand forecast and procurement scoring
inventory_route_po = StrictPartialOrder(nodes=[Inventory_Sync, Route_Optimize])
# No order edges -> concurrent

# Logistics and production synchronization must align after inventory and route optimization
logistics_production_po = StrictPartialOrder(nodes=[Logistics_Align, Production_Sync])
logistics_production_po.order.add_edge(Logistics_Align, Production_Sync)

# Order validation follows logistics and production sync
order_validation_po = StrictPartialOrder(nodes=[Production_Sync, Order_Validation])
order_validation_po.order.add_edge(Production_Sync, Order_Validation)

# Blockchain audit and compliance check run concurrently, then stakeholder notify and performance review
audit_compliance_po = StrictPartialOrder(nodes=[Blockchain_Audit, Compliance_Check])
# No order edge → concurrent

notify_performance_po = StrictPartialOrder(nodes=[Stakeholder_Notify, Performance_Review])
notify_performance_po.order.add_edge(Stakeholder_Notify, Performance_Review)

# Connect the whole process in partial order:
# Start with data ingestion
# -> parallel: risk loop and predictive analytics (analytics_po) and procurement scoring
# After demand forecast, procurement scoring, and risk loop are done,
# inventory and route optimize start
# Then logistics align -> production sync -> order validation
# Simultaneously with or after order validation:
# blockchain audit and compliance check
# Then stakeholder notify -> performance review

# Create a root StrictPartialOrder, nodes are:
nodes = [
    Data_Ingestion,
    risk_loop,
    analytics_po,
    procurement_po,
    inventory_route_po,
    logistics_production_po,
    order_validation_po,
    audit_compliance_po,
    notify_performance_po
]

root = StrictPartialOrder(nodes=nodes)

# Define order relations:
# Data ingestion -> risk loop, analytics, procurement scoring
root.order.add_edge(Data_Ingestion, risk_loop)
root.order.add_edge(Data_Ingestion, analytics_po)
root.order.add_edge(Data_Ingestion, procurement_po)

# After analytics and procurement and risk:
# demand forecast (inside analytics_po) and procurement_po and risk_loop must complete before inventory_route_po

# So add edges from analytics_po, procurement_po, risk_loop to inventory_route_po
root.order.add_edge(analytics_po, inventory_route_po)
root.order.add_edge(procurement_po, inventory_route_po)
root.order.add_edge(risk_loop, inventory_route_po)

# inventory_route_po -> logistics_production_po
root.order.add_edge(inventory_route_po, logistics_production_po)

# logistics_production_po -> order_validation_po
root.order.add_edge(logistics_production_po, order_validation_po)

# order_validation_po -> audit_compliance_po
root.order.add_edge(order_validation_po, audit_compliance_po)

# audit_compliance_po -> notify_performance_po
root.order.add_edge(audit_compliance_po, notify_performance_po)