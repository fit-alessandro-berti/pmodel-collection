# Generated from: 1c2d786d-6197-42e2-872a-9159e67c66a0.json
# Description: This process involves the coordinated preparation, calibration, and deployment of a commercial drone fleet for large-scale agricultural monitoring. It begins with environmental data collection and drone diagnostics, followed by flight path optimization using AI algorithms. The drones are then equipped with sensor payloads, undergo pre-flight safety checks, and are dispatched in staggered waves to cover diverse terrain. As drones collect multispectral imagery, onboard AI performs in-flight anomaly detection to flag crop health issues. The data is transmitted in real-time to a centralized system for further analysis, while drones are continuously monitored for battery status and mechanical integrity. Post-mission, drones return to designated charging stations for automated maintenance and firmware updates. Throughout, compliance with aviation regulations and data privacy protocols is ensured, integrating stakeholder communications and incident reporting mechanisms to maintain operational transparency and efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
data_collect      = Transition(label="Data Collect")
diagnostics_run   = Transition(label="Diagnostics Run")
drone_setup       = Transition(label="Drone Setup")
sensor_install    = Transition(label="Sensor Install")
flight_plan       = Transition(label="Flight Plan")
ai_optimize       = Transition(label="AI Optimize")
payload_load      = Transition(label="Payload Load")
safety_check      = Transition(label="Safety Check")
launch_drones     = Transition(label="Launch Drones")
in_flight_ai      = Transition(label="In-Flight AI")
data_stream       = Transition(label="Data Stream")
status_monitor    = Transition(label="Status Monitor")
return_fleet      = Transition(label="Return Fleet")
auto_maintain     = Transition(label="Auto Maintain")
firmware_update   = Transition(label="Firmware Update")
regulation_check  = Transition(label="Regulation Check")
incident_report   = Transition(label="Incident Report")
stakeholder_notify= Transition(label="Stakeholder Notify")

# Build the partial order model
root = StrictPartialOrder(nodes=[
    # initial activities
    data_collect, diagnostics_run,
    # flight‐planning branch
    flight_plan, ai_optimize,
    # drone‐preparation branch
    drone_setup, sensor_install, payload_load, safety_check,
    # launching & in‐flight
    launch_drones, in_flight_ai, data_stream, status_monitor,
    # post‐mission
    return_fleet, auto_maintain, firmware_update,
    # compliance & communication
    regulation_check, incident_report, stakeholder_notify
])

# Sequence for environmental data → flight planning
root.order.add_edge(data_collect, flight_plan)
root.order.add_edge(flight_plan, ai_optimize)

# Sequence for diagnostics → drone setup → sensor install → payload load → safety check
root.order.add_edge(diagnostics_run, drone_setup)
root.order.add_edge(drone_setup, sensor_install)
root.order.add_edge(sensor_install, payload_load)
root.order.add_edge(payload_load, safety_check)

# Synchronize before launch
root.order.add_edge(ai_optimize, launch_drones)
root.order.add_edge(safety_check, launch_drones)

# In‐flight parallel activities
root.order.add_edge(launch_drones, in_flight_ai)
root.order.add_edge(launch_drones, data_stream)
root.order.add_edge(launch_drones, status_monitor)

# Post‐flight return and maintenance
root.order.add_edge(in_flight_ai, return_fleet)
root.order.add_edge(data_stream, return_fleet)
root.order.add_edge(status_monitor, return_fleet)
root.order.add_edge(return_fleet, auto_maintain)
root.order.add_edge(auto_maintain, firmware_update)

# Compliance, reporting, and stakeholder notifications (can occur after data collect)
root.order.add_edge(data_collect, regulation_check)
root.order.add_edge(data_collect, incident_report)
root.order.add_edge(data_collect, stakeholder_notify)