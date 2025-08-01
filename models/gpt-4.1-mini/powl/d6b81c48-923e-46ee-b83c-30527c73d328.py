# Generated from: d6b81c48-923e-46ee-b83c-30527c73d328.json
# Description: This process governs the comprehensive maintenance cycle for a fleet of autonomous delivery drones operating in diverse urban environments. It includes pre-flight diagnostics, environmental adaptation calibrations, in-flight anomaly detection, post-mission data analysis, battery health optimization, dynamic route reconfiguration, and regulatory compliance reporting. The workflow integrates real-time telemetry monitoring with predictive analytics to minimize downtime and extend drone lifecycle. Specialized activities involve firmware patch deployment, sensor recalibration, damage assessment from minor collisions, and end-of-day performance summarization, ensuring operational efficiency and safety standards are continuously met across all units.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Preflight_Check = Transition(label='Preflight Check')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Battery_Test = Transition(label='Battery Test')
Route_Update = Transition(label='Route Update')
Firmware_Patch = Transition(label='Firmware Patch')
Flight_Launch = Transition(label='Flight Launch')
Telemetry_Monitor = Transition(label='Telemetry Monitor')
Anomaly_Detect = Transition(label='Anomaly Detect')
Collision_Assess = Transition(label='Collision Assess')
Data_Upload = Transition(label='Data Upload')
Postflight_Review = Transition(label='Postflight Review')
Battery_Optimize = Transition(label='Battery Optimize')
Damage_Repair = Transition(label='Damage Repair')
Compliance_Report = Transition(label='Compliance Report')
Performance_Log = Transition(label='Performance Log')
Mission_Debrief = Transition(label='Mission Debrief')

# Pre-flight sequence: Preflight Check -> Sensor Calibrate -> Battery Test -> Route Update -> Firmware Patch
preflight_seq = StrictPartialOrder(
    nodes=[Preflight_Check, Sensor_Calibrate, Battery_Test, Route_Update, Firmware_Patch]
)
preflight_seq.order.add_edge(Preflight_Check, Sensor_Calibrate)
preflight_seq.order.add_edge(Sensor_Calibrate, Battery_Test)
preflight_seq.order.add_edge(Battery_Test, Route_Update)
preflight_seq.order.add_edge(Route_Update, Firmware_Patch)

# Flight phase:
# Flight Launch starts flight
# Concurrent telemetry monitoring and anomaly detection during flight
flight = StrictPartialOrder(
    nodes=[Flight_Launch, Telemetry_Monitor, Anomaly_Detect]
)
# Flight Launch happens first
flight.order.add_edge(Flight_Launch, Telemetry_Monitor)
flight.order.add_edge(Flight_Launch, Anomaly_Detect)
# Telemetry Monitor and Anomaly Detect run concurrently (no order edge between them)

# Collision assessment and damage repair can follow anomaly detection, possibly concurrent with data upload and post flight review
collision_damage = StrictPartialOrder(
    nodes=[Collision_Assess, Damage_Repair]
)
collision_damage.order.add_edge(Collision_Assess, Damage_Repair)

postflight_seq = StrictPartialOrder(
    nodes=[Data_Upload, Postflight_Review, Battery_Optimize]
)
postflight_seq.order.add_edge(Data_Upload, Postflight_Review)
postflight_seq.order.add_edge(Postflight_Review, Battery_Optimize)

# Compliance report and performance log
final_reporting = StrictPartialOrder(
    nodes=[Compliance_Report, Performance_Log, Mission_Debrief]
)
final_reporting.order.add_edge(Compliance_Report, Performance_Log)
final_reporting.order.add_edge(Performance_Log, Mission_Debrief)

# Combine collision_damage concurrent with postflight_seq (no order edges between nodes of these two)
postflight_and_repair = StrictPartialOrder(
    nodes=[Collision_Assess, Damage_Repair, Data_Upload, Postflight_Review, Battery_Optimize]
)
postflight_and_repair.order.add_edge(Collision_Assess, Damage_Repair)
postflight_and_repair.order.add_edge(Data_Upload, Postflight_Review)
postflight_and_repair.order.add_edge(Postflight_Review, Battery_Optimize)

# Compose a partial order connecting phases:
# preflight_seq --> flight --> postflight_and_repair --> final_reporting

root = StrictPartialOrder(
    nodes=[preflight_seq, flight, postflight_and_repair, final_reporting]
)
root.order.add_edge(preflight_seq, flight)
root.order.add_edge(flight, postflight_and_repair)
root.order.add_edge(postflight_and_repair, final_reporting)