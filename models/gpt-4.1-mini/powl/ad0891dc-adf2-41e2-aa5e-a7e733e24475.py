# Generated from: ad0891dc-adf2-41e2-aa5e-a7e733e24475.json
# Description: This process outlines the intricate steps involved in assembling custom drones tailored for specialized industrial applications. It begins with component sourcing, followed by precision calibration of sensors and flight controllers. The assembly involves iterative software-hardware integration, rigorous environmental testing under simulated conditions, and final quality certification. Each drone undergoes a unique flight pattern programming to match client specifications, including payload configurations and emergency protocols. The process concludes with packaging and logistics coordination, ensuring safe delivery and post-deployment support scheduling.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Component_Sourcing = Transition(label='Component Sourcing')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Frame_Assembly = Transition(label='Frame Assembly')
Wiring_Harness = Transition(label='Wiring Harness')
Controller_Install = Transition(label='Controller Install')
Software_Load = Transition(label='Software Load')
Firmware_Update = Transition(label='Firmware Update')
Payload_Setup = Transition(label='Payload Setup')
Flight_Pattern = Transition(label='Flight Pattern')
Stress_Testing = Transition(label='Stress Testing')
Enviro_Simulate = Transition(label='Enviro Simulate')
Quality_Check = Transition(label='Quality Check')
Certify_Drone = Transition(label='Certify Drone')
Package_Unit = Transition(label='Package Unit')
Ship_Logistics = Transition(label='Ship Logistics')
Support_Schedule = Transition(label='Support Schedule')

# Software-hardware iterative integration loop:
# Loop body B = Payload_Setup then Flight_Pattern.
# Loop header A = Firmware_Update.
# Loop: execute Firmware_Update, then either exit or Payload_Setup + Flight_Pattern then Firmware_Update again.

software_hardware_integration = OperatorPOWL(operator=Operator.LOOP, children=[Firmware_Update, StrictPartialOrder(nodes=[Payload_Setup, Flight_Pattern])])
# Note: The StrictPartialOrder inside the loop enforces Payload_Setup and Flight_Pattern concurrent, no order needed
# because the description suggests "Each drone undergoes a unique flight pattern programming including payload configurations..."
# so best modeled as concurrent inside iteration.

# Environmental testing partial order (concurrent Stress Testing and Enviro Simulate):
testing = StrictPartialOrder(nodes=[Stress_Testing, Enviro_Simulate])

# Assembly partial order with connections:
# Frame Assembly -> Wiring Harness -> Controller Install
assembly = StrictPartialOrder(nodes=[Frame_Assembly, Wiring_Harness, Controller_Install])
assembly.order.add_edge(Frame_Assembly, Wiring_Harness)
assembly.order.add_edge(Wiring_Harness, Controller_Install)

# Quality and certification partial order: Quality Check -> Certify Drone
quality = StrictPartialOrder(nodes=[Quality_Check, Certify_Drone])
quality.order.add_edge(Quality_Check, Certify_Drone)

# Packaging and shipment partial order: Package Unit -> Ship Logistics -> Support Schedule
shipping = StrictPartialOrder(nodes=[Package_Unit, Ship_Logistics, Support_Schedule])
shipping.order.add_edge(Package_Unit, Ship_Logistics)
shipping.order.add_edge(Ship_Logistics, Support_Schedule)

# High level strict partial order to connect main phases in order:
# Component Sourcing -> Sensor Calibrate -> assembly -> Software Load -> software_hardware_integration -> testing -> quality -> shipping

root = StrictPartialOrder(nodes=[
    Component_Sourcing, Sensor_Calibrate,
    assembly,
    Software_Load,
    software_hardware_integration,
    testing,
    quality,
    shipping
])

root.order.add_edge(Component_Sourcing, Sensor_Calibrate)
root.order.add_edge(Sensor_Calibrate, assembly)
root.order.add_edge(assembly, Software_Load)
root.order.add_edge(Software_Load, software_hardware_integration)
root.order.add_edge(software_hardware_integration, testing)
root.order.add_edge(testing, quality)
root.order.add_edge(quality, shipping)