# Generated from: 8792e585-9a96-451e-9bed-69be84e0768c.json
# Description: This process involves the remote calibration of IoT sensor networks deployed in harsh and inaccessible environments such as deep forests or offshore platforms. The workflow starts with data acquisition from multiple sensor nodes, followed by anomaly detection using adaptive algorithms. Once anomalies are confirmed, the system initiates remote calibration commands, adjusting sensor parameters to maintain data accuracy. Periodic validation through cross-referencing sensor outputs ensures long-term reliability. Additionally, the process includes fallback manual overrides and synchronization with central data repositories to guarantee seamless integration and continuous monitoring despite network latency or disruptions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Data_Grab = Transition(label='Data Grab')
Anomaly_Check = Transition(label='Anomaly Check')
Signal_Boost = Transition(label='Signal Boost')
Param_Adjust = Transition(label='Param Adjust')
Sync_Time = Transition(label='Sync Time')
Validation_Run = Transition(label='Validation Run')
Fallback_Mode = Transition(label='Fallback Mode')
Override_Cmd = Transition(label='Override Cmd')
Cross_Ref = Transition(label='Cross Ref')
Data_Archive = Transition(label='Data Archive')
Status_Poll = Transition(label='Status Poll')
Error_Log = Transition(label='Error Log')
Report_Gen = Transition(label='Report Gen')
Alert_Send = Transition(label='Alert Send')
Network_Reset = Transition(label='Network Reset')
Calibration_End = Transition(label='Calibration End')

# The process described:
# 1) Start with Data Grab from multiple sensor nodes (this suggests concurrent nodes, but simplified as one activity here)
# 2) Followed by Anomaly Check
# 3) Once anomalies are confirmed, we have Remote calibration commands that adjust sensor parameters:
#    This can be a loop: execute Signal Boost, Param Adjust repeatedly until calibration end
# 4) Periodic Validation Run with Cross Ref for long-term reliability (these are likely concurrent with calibration or after)
# 5) Fallback manual override enables Override Cmd (likely a choice/fallback path)
# 6) Synchronization with central repositories (Sync Time, Data Archive)
# 7) Monitoring activities: Status_Poll, Error_Log, Report_Gen, Alert_Send, Network_Reset (likely concurrent monitoring)
# 8) Calibration End ends the process

# Build the calibration loop: After Anomaly_Check, enter loop:
# loop body: Signal Boost (B), then Param Adjust (A)
# Loop modeled as * (A=Param Adjust, B=Signal Boost)
calibration_loop = OperatorPOWL(operator=Operator.LOOP, children=[Param_Adjust, Signal_Boost])

# Fallback manual override as choice with Override Cmd and Fallback Mode
fallback_xor = OperatorPOWL(operator=Operator.XOR, children=[Fallback_Mode, Override_Cmd])

# Validation branch: Validation Run then Cross Ref (this can be a partial order)
validation_po = StrictPartialOrder(nodes=[Validation_Run, Cross_Ref])
validation_po.order.add_edge(Validation_Run, Cross_Ref)

# Synchronization branch: Sync Time and Data Archive (can be partial order with Sync Time before Data Archive)
sync_po = StrictPartialOrder(nodes=[Sync_Time, Data_Archive])
sync_po.order.add_edge(Sync_Time, Data_Archive)

# Monitoring activities partial order:
monitoring_activities = [Status_Poll, Error_Log, Report_Gen, Alert_Send, Network_Reset]
monitoring_po = StrictPartialOrder(nodes=monitoring_activities)

# Combine fallback_xor and monitoring_po in parallel (they are concurrent)
fallback_monitoring_po = StrictPartialOrder(nodes=[fallback_xor, monitoring_po])
# No order edges between fallback_xor and monitoring_po => concurrent

# Now combine all after Anomaly_Check concurrently:
# calibration_loop, validation_po, sync_po, fallback_monitoring_po run concurrently after Anomaly_Check
after_anomaly_po = StrictPartialOrder(
    nodes=[calibration_loop, validation_po, sync_po, fallback_monitoring_po]
)
# No order edges among these four => concurrent

# Overall process PO:
# Data Grab --> Anomaly Check --> after_anomaly_po --> Calibration End
root = StrictPartialOrder(
    nodes=[Data_Grab, Anomaly_Check, after_anomaly_po, Calibration_End]
)
root.order.add_edge(Data_Grab, Anomaly_Check)
root.order.add_edge(Anomaly_Check, after_anomaly_po)
# After_anomaly_po concurrent activities end before Calibration_End
root.order.add_edge(after_anomaly_po, Calibration_End)