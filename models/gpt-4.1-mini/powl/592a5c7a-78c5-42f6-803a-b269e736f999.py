# Generated from: 592a5c7a-78c5-42f6-803a-b269e736f999.json
# Description: This process manages the synchronization of quantum-encrypted supply chain data between multiple decentralized nodes in near real-time. It involves validating quantum keys, dynamically adjusting supply forecasts based on probabilistic models, and ensuring compliance with both local and international quantum data regulations. Activities include secure data handshake, anomaly detection in quantum states, and adaptive routing of encrypted packets to optimize throughput while maintaining high security. The process also incorporates feedback loops from predictive analytics to fine-tune inventory levels and distribution schedules in response to market volatility and quantum network performance metrics.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity label
KeyValidation = Transition(label='Key Validation')
DataHandshake = Transition(label='Data Handshake')
NodeSync = Transition(label='Node Sync')
PacketRouting = Transition(label='Packet Routing')
AnomalyScan = Transition(label='Anomaly Scan')
LoadBalance = Transition(label='Load Balance')
ForecastAdjust = Transition(label='Forecast Adjust')
ComplianceCheck = Transition(label='Compliance Check')
QuantumLog = Transition(label='Quantum Log')
StateUpdate = Transition(label='State Update')
DataEncrypt = Transition(label='Data Encrypt')
PacketQueue = Transition(label='Packet Queue')
FeedbackLoop = Transition(label='Feedback Loop')
InventorySync = Transition(label='Inventory Sync')
ScheduleUpdate = Transition(label='Schedule Update')
RiskAssess = Transition(label='Risk Assess')

# Build sub-parts according to the process description logic

# Step 1: Validation and handshake
validation_handshake_po = StrictPartialOrder(nodes=[KeyValidation, DataHandshake])
validation_handshake_po.order.add_edge(KeyValidation, DataHandshake)

# Step 2: Sync nodes and anomaly scan run in parallel after handshake
sync_anomaly_po = StrictPartialOrder(nodes=[NodeSync, AnomalyScan])
# No order edges (concurrent)

# Step 3: Packet routing after anomaly scan and node sync
packet_routing_po = StrictPartialOrder(nodes=[PacketRouting])
# PacketQueue and DataEncrypt happen after PacketRouting concurrently
packet_post_po = StrictPartialOrder(nodes=[PacketQueue, DataEncrypt])
# No edges implies concurrent after PacketRouting

# Step 4: Load balancing after routing related activities
load_bal_forecast_po = StrictPartialOrder(nodes=[LoadBalance, ForecastAdjust])
load_bal_forecast_po.order.add_edge(LoadBalance, ForecastAdjust)

# Step 5: Compliance check after forecast adjust
comp_check_po = StrictPartialOrder(nodes=[ComplianceCheck])
# Step 6: Quantum log and state update after compliance check, concurrent
log_state_po = StrictPartialOrder(nodes=[QuantumLog, StateUpdate])
# No edges = concurrent

# Step 7: Feedback loop (* loop operator) - feedback loop and risk assess and after that return to forecast adjust
loop_body_po = StrictPartialOrder(nodes=[FeedbackLoop, RiskAssess])
# These two can run concurrently, no edge
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[ForecastAdjust, loop_body_po])

# Step 8: Inventory sync and schedule update after feedback loop (can be concurrent)
inventory_schedule_po = StrictPartialOrder(nodes=[InventorySync, ScheduleUpdate])
# concurrent, no order edges

# Combine everything in partial order:

# Compose first main linear part:
# KeyValidation --> DataHandshake --> (NodeSync || AnomalyScan) --> PacketRouting --> (PacketQueue || DataEncrypt)
main1 = StrictPartialOrder(nodes=[validation_handshake_po, sync_anomaly_po, packet_routing_po, packet_post_po])
main1.order.add_edge(validation_handshake_po, sync_anomaly_po)
main1.order.add_edge(sync_anomaly_po, packet_routing_po)
main1.order.add_edge(packet_routing_po, packet_post_po)

# Then after these, LoadBalance and ForecastAdjust (ForecastAdjust nested inside loop)
# We already created a loop with ForecastAdjust and feedback body, so replace ForecastAdjust node in load_bal_forecast_po with the loop
load_bal_forecast_po_loop = StrictPartialOrder(nodes=[LoadBalance, feedback_loop])
load_bal_forecast_po_loop.order.add_edge(LoadBalance, feedback_loop)

# Compliance check after forecast adjust loop
comp_after_loop_po = StrictPartialOrder(nodes=[load_bal_forecast_po_loop, ComplianceCheck])
comp_after_loop_po.order.add_edge(load_bal_forecast_po_loop, ComplianceCheck)

# Quantum Log and State Update after Compliance Check (concurrent)
after_comp_po = StrictPartialOrder(nodes=[comp_after_loop_po, log_state_po])
after_comp_po.order.add_edge(comp_after_loop_po, log_state_po)

# Finally Inventory Sync and Schedule Update concurrent after QuantumLog and StateUpdate
final_po = StrictPartialOrder(nodes=[after_comp_po, inventory_schedule_po])
final_po.order.add_edge(after_comp_po, inventory_schedule_po)

# Now top level PO with main1 preceding final_po
root = StrictPartialOrder(nodes=[main1, final_po])
root.order.add_edge(main1, final_po)