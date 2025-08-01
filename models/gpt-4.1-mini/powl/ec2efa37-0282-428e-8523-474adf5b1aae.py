# Generated from: ec2efa37-0282-428e-8523-474adf5b1aae.json
# Description: This process involves the integration of quantum computing algorithms into a traditional supply chain to optimize inventory levels, demand forecasting, and delivery schedules across multiple global warehouses in real-time. It requires coordination between quantum data processors, AI-driven analytics, and human decision-makers to dynamically adjust procurement, production, and distribution while minimizing costs and delays. The process also incorporates feedback loops from IoT sensors embedded in shipping containers, enabling predictive maintenance and risk mitigation for perishable goods under varying environmental conditions. This atypical approach aims to revolutionize supply chain resilience by leveraging quantum entanglement for instantaneous data sharing and synchronized decision-making among disparate nodes, ensuring seamless operations even under high uncertainty and fluctuating market demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Quantum_Init = Transition(label='Quantum Init')
Data_Ingest = Transition(label='Data Ingest')
AI_Forecast = Transition(label='AI Forecast')
Inventory_Sync = Transition(label='Inventory Sync')
Procurement_Plan = Transition(label='Procurement Plan')
Production_Align = Transition(label='Production Align')
Distribution_Map = Transition(label='Distribution Map')
IoT_Monitor = Transition(label='IoT Monitor')
Risk_Assess = Transition(label='Risk Assess')
Maintenance_Alert = Transition(label='Maintenance Alert')
Quantum_Compute = Transition(label='Quantum Compute')
Feedback_Loop = Transition(label='Feedback Loop')
Schedule_Adjust = Transition(label='Schedule Adjust')
Demand_Update = Transition(label='Demand Update')
Delivery_Track = Transition(label='Delivery Track')
Compliance_Check = Transition(label='Compliance Check')

# The process integration generally:
# Quantum_Init --> Data_Ingest --> AI_Forecast --> Inventory_Sync --> 
# Procurement_Plan & Production_Align & Distribution_Map concurrently (partial order)
# Then Quantum_Compute integrates all previous computations.
#
# Loop: Feedback_Loop influences IoT_Monitor and Risk_Assess, then Maintenance_Alert
# After Maintenance_Alert, the process loops back via Feedback_Loop until exit.
#
# After loop ends, Schedule_Adjust --> Demand_Update --> Delivery_Track --> Compliance_Check

# Define the core partial order for initial part before loop
initial_PO = StrictPartialOrder(nodes=[
    Quantum_Init, Data_Ingest, AI_Forecast, Inventory_Sync,
    Procurement_Plan, Production_Align, Distribution_Map,
    Quantum_Compute
])

# Define edges
initial_PO.order.add_edge(Quantum_Init, Data_Ingest)
initial_PO.order.add_edge(Data_Ingest, AI_Forecast)
initial_PO.order.add_edge(AI_Forecast, Inventory_Sync)

# Procurement Plan, Production Align, Distribution Map are concurrent but all start after Inventory Sync
initial_PO.order.add_edge(Inventory_Sync, Procurement_Plan)
initial_PO.order.add_edge(Inventory_Sync, Production_Align)
initial_PO.order.add_edge(Inventory_Sync, Distribution_Map)

# All three must finish before Quantum Compute
initial_PO.order.add_edge(Procurement_Plan, Quantum_Compute)
initial_PO.order.add_edge(Production_Align, Quantum_Compute)
initial_PO.order.add_edge(Distribution_Map, Quantum_Compute)

# Loop body partial order
loop_body_PO = StrictPartialOrder(nodes=[IoT_Monitor, Risk_Assess, Maintenance_Alert])

# IoT Monitor and Risk Assess are concurrent starting the loop body
# Both must complete before Maintenance Alert
loop_body_PO.order.add_edge(IoT_Monitor, Maintenance_Alert)
loop_body_PO.order.add_edge(Risk_Assess, Maintenance_Alert)

# Loop: execute Feedback Loop, then loop body, then back to Feedback Loop or exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, loop_body_PO])

# After loop ends
post_loop_PO = StrictPartialOrder(nodes=[Schedule_Adjust, Demand_Update, Delivery_Track, Compliance_Check])
post_loop_PO.order.add_edge(Schedule_Adjust, Demand_Update)
post_loop_PO.order.add_edge(Demand_Update, Delivery_Track)
post_loop_PO.order.add_edge(Delivery_Track, Compliance_Check)

# Final root PO with all main parts (initial_PO, loop, post_loop_PO)
root = StrictPartialOrder(nodes=[initial_PO, loop, post_loop_PO])

# Ordering between these main parts:
root.order.add_edge(initial_PO, loop)
root.order.add_edge(loop, post_loop_PO)