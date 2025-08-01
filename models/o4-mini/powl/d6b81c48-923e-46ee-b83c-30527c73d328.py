# Generated from: d6b81c48-923e-46ee-b83c-30527c73d328.json
# Description: This process governs the comprehensive maintenance cycle for a fleet of autonomous delivery drones operating in diverse urban environments. It includes pre-flight diagnostics, environmental adaptation calibrations, in-flight anomaly detection, post-mission data analysis, battery health optimization, dynamic route reconfiguration, and regulatory compliance reporting. The workflow integrates real-time telemetry monitoring with predictive analytics to minimize downtime and extend drone lifecycle. Specialized activities involve firmware patch deployment, sensor recalibration, damage assessment from minor collisions, and end-of-day performance summarization, ensuring operational efficiency and safety standards are continuously met across all units.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
preflight       = Transition(label="Preflight Check")
sensor_cal      = Transition(label="Sensor Calibrate")
battery_test    = Transition(label="Battery Test")
route_update    = Transition(label="Route Update")
firmware_patch  = Transition(label="Firmware Patch")
flight_launch   = Transition(label="Flight Launch")
telemetry       = Transition(label="Telemetry Monitor")
data_upload     = Transition(label="Data Upload")
postflight_rev  = Transition(label="Postflight Review")
battery_opt     = Transition(label="Battery Optimize")
compliance_rep  = Transition(label="Compliance Report")
performance_log = Transition(label="Performance Log")
mission_deb     = Transition(label="Mission Debrief")

# Build the anomaly‐handling sub‐process: either detect & repair, or skip
anomaly_detect = Transition(label="Anomaly Detect")
collision_assess = Transition(label="Collision Assess")
damage_repair = Transition(label="Damage Repair")

anomaly_seq = StrictPartialOrder(
    nodes=[anomaly_detect, collision_assess, damage_repair]
)
anomaly_seq.order.add_edge(anomaly_detect, collision_assess)
anomaly_seq.order.add_edge(collision_assess, damage_repair)

skip = SilentTransition()

anomaly_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[anomaly_seq, skip]
)

# Build one full maintenance & flight cycle as a partial order
cycle_body_nodes = [
    preflight, sensor_cal, battery_test, route_update, firmware_patch,
    flight_launch, telemetry, anomaly_choice,
    data_upload, postflight_rev, battery_opt, compliance_rep,
    performance_log, mission_deb
]
cycle_body = StrictPartialOrder(nodes=cycle_body_nodes)

# Sequential dependencies in the cycle
edges = [
    (preflight, sensor_cal),
    (sensor_cal, battery_test),
    (battery_test, route_update),
    (route_update, firmware_patch),
    (firmware_patch, flight_launch),
    (flight_launch, telemetry),
    (telemetry, anomaly_choice),
    (anomaly_choice, data_upload),
    (data_upload, postflight_rev),
    (postflight_rev, battery_opt),
    (battery_opt, compliance_rep),
    (compliance_rep, performance_log),
    (performance_log, mission_deb),
]
for src, tgt in edges:
    cycle_body.order.add_edge(src, tgt)

# Wrap the cycle in a loop: perform the cycle, then either exit or repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycle_body, skip]
)