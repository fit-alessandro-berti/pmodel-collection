# Generated from: 1c2d786d-6197-42e2-872a-9159e67c66a0.json
# Description: This process involves the coordinated preparation, calibration, and deployment of a commercial drone fleet for large-scale agricultural monitoring. It begins with environmental data collection and drone diagnostics, followed by flight path optimization using AI algorithms. The drones are then equipped with sensor payloads, undergo pre-flight safety checks, and are dispatched in staggered waves to cover diverse terrain. As drones collect multispectral imagery, onboard AI performs in-flight anomaly detection to flag crop health issues. The data is transmitted in real-time to a centralized system for further analysis, while drones are continuously monitored for battery status and mechanical integrity. Post-mission, drones return to designated charging stations for automated maintenance and firmware updates. Throughout, compliance with aviation regulations and data privacy protocols is ensured, integrating stakeholder communications and incident reporting mechanisms to maintain operational transparency and efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Data_Collect = Transition(label='Data Collect')
Diagnostics_Run = Transition(label='Diagnostics Run')

Flight_Plan = Transition(label='Flight Plan')
AI_Optimize = Transition(label='AI Optimize')

Drone_Setup = Transition(label='Drone Setup')
Sensor_Install = Transition(label='Sensor Install')
Payload_Load = Transition(label='Payload Load')
Safety_Check = Transition(label='Safety Check')

Launch_Drones = Transition(label='Launch Drones')

In_Flight_AI = Transition(label='In-Flight AI')
Data_Stream = Transition(label='Data Stream')
Status_Monitor = Transition(label='Status Monitor')

Return_Fleet = Transition(label='Return Fleet')
Auto_Maintain = Transition(label='Auto Maintain')
Firmware_Update = Transition(label='Firmware Update')

Regulation_Check = Transition(label='Regulation Check')
Incident_Report = Transition(label='Incident Report')
Stakeholder_Notify = Transition(label='Stakeholder Notify')

# Phase 1: Environmental data collection and drone diagnostics
# Data Collect --> Diagnostics Run (strict order)
phase1 = StrictPartialOrder(nodes=[Data_Collect, Diagnostics_Run])
phase1.order.add_edge(Data_Collect, Diagnostics_Run)

# Phase 2: Flight path optimization using AI algorithms
# Flight Plan --> AI Optimize (strict order)
phase2 = StrictPartialOrder(nodes=[Flight_Plan, AI_Optimize])
phase2.order.add_edge(Flight_Plan, AI_Optimize)

# Phase 3: Drone preparation: setup, install sensors and payload, safety check
# These 4 activities can be partially ordered:
# - Drone Setup before Payload Load (assume we load payload after setup)
# - Sensor Install before Payload Load (sensors installed before payload)
# - Safety Check after Payload Load
# So:
# Drone Setup --> Payload Load
# Sensor Install --> Payload Load
# Payload Load --> Safety Check

phase3 = StrictPartialOrder(
    nodes=[Drone_Setup, Sensor_Install, Payload_Load, Safety_Check]
)
phase3.order.add_edge(Drone_Setup, Payload_Load)
phase3.order.add_edge(Sensor_Install, Payload_Load)
phase3.order.add_edge(Payload_Load, Safety_Check)

# Phase 4: Launch drones
# Launch Drones happens after Safety Check
phase4 = Launch_Drones

# Phase 5: In-flight data collection and monitoring
# In-Flight AI, Data Stream and Status Monitor run concurrently (partial order with no edges)
phase5 = StrictPartialOrder(nodes=[In_Flight_AI, Data_Stream, Status_Monitor])

# Phase 6: Return fleet and maintenance
# Return Fleet --> Auto Maintain --> Firmware Update
phase6 = StrictPartialOrder(nodes=[Return_Fleet, Auto_Maintain, Firmware_Update])
phase6.order.add_edge(Return_Fleet, Auto_Maintain)
phase6.order.add_edge(Auto_Maintain, Firmware_Update)

# Phase 7: Compliance and reporting
# Regulation Check must happen before Incident Report and Stakeholder Notify
# Incident Report and Stakeholder Notify can be concurrent
phase7 = StrictPartialOrder(nodes=[Regulation_Check, Incident_Report, Stakeholder_Notify])
phase7.order.add_edge(Regulation_Check, Incident_Report)
phase7.order.add_edge(Regulation_Check, Stakeholder_Notify)

# Compose the full workflow partial order
# Top-level: phases in this order:
# phase1 --> phase2 --> phase3 --> Launch Drones --> phase5 --> phase6 --> phase7

# Putting all phases except Launch Drones in a sequence
# Use StrictPartialOrder nodes including all submodels and single nodes for Launch Drones
# For conciseness, represent the top-level partial order with nodes:
# [phase1, phase2, phase3, Launch_Drones, phase5, phase6, phase7]

top_nodes = [phase1, phase2, phase3, Launch_Drones, phase5, phase6, phase7]
root = StrictPartialOrder(nodes=top_nodes)

root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, Launch_Drones)
root.order.add_edge(Launch_Drones, phase5)
root.order.add_edge(phase5, phase6)
root.order.add_edge(phase6, phase7)