# Generated from: a1ad6d6c-4a80-4675-b5ab-e17e19cd138e.json
# Description: This process outlines the steps involved in assembling custom drones tailored to unique client specifications. It begins with requirement analysis and component sourcing, followed by precision frame construction and intricate wiring. Firmware installation and sensor calibration are critical to ensure optimal performance. Rigorous flight testing and quality validation precede packaging. The process concludes with detailed client training and support setup to guarantee operational success and customer satisfaction. Each step demands coordination across engineering, logistics, and customer service teams to meet exacting standards within tight timelines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Req_Analysis = Transition(label='Req Analysis')
Part_Sourcing = Transition(label='Part Sourcing')
Frame_Build = Transition(label='Frame Build')
Wiring_Setup = Transition(label='Wiring Setup')
Firmware_Flash = Transition(label='Firmware Flash')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Motor_Install = Transition(label='Motor Install')
Propeller_Fit = Transition(label='Propeller Fit')
Battery_Test = Transition(label='Battery Test')
Flight_Check = Transition(label='Flight Check')
Quality_Audit = Transition(label='Quality Audit')
Package_Prep = Transition(label='Package Prep')
Client_Training = Transition(label='Client Training')
Support_Setup = Transition(label='Support Setup')
Delivery_Coord = Transition(label='Delivery Coord')

# Create the partial order nodes list in the described sequence

nodes = [
    Req_Analysis,
    Part_Sourcing,
    Frame_Build,
    Wiring_Setup,
    Firmware_Flash,
    Sensor_Calibrate,
    Motor_Install,
    Propeller_Fit,
    Battery_Test,
    Flight_Check,
    Quality_Audit,
    Package_Prep,
    Client_Training,
    Support_Setup,
    Delivery_Coord
]

root = StrictPartialOrder(nodes=nodes)

# Add edges that represent the sequence and partial concurrency implied by description:

# Initial requirements and sourcing sequential
root.order.add_edge(Req_Analysis, Part_Sourcing)

# Frame build after sourcing
root.order.add_edge(Part_Sourcing, Frame_Build)

# Wiring after frame build
root.order.add_edge(Frame_Build, Wiring_Setup)

# Firmware and Sensor steps after Wiring (likely sequential)
root.order.add_edge(Wiring_Setup, Firmware_Flash)
root.order.add_edge(Firmware_Flash, Sensor_Calibrate)

# Motor install and propeller fit after sensor calibrate, they are probably done in sequence
root.order.add_edge(Sensor_Calibrate, Motor_Install)
root.order.add_edge(Motor_Install, Propeller_Fit)

# Battery Test after propeller fit
root.order.add_edge(Propeller_Fit, Battery_Test)

# Flight check and quality audit after battery test (flight check must precede quality audit)
root.order.add_edge(Battery_Test, Flight_Check)
root.order.add_edge(Flight_Check, Quality_Audit)

# Packaging after quality audit
root.order.add_edge(Quality_Audit, Package_Prep)

# Client training and Support Setup after packaging (can be concurrent)
root.order.add_edge(Package_Prep, Client_Training)
root.order.add_edge(Package_Prep, Support_Setup)

# Delivery coordination after training and support setup (must wait for both)
root.order.add_edge(Client_Training, Delivery_Coord)
root.order.add_edge(Support_Setup, Delivery_Coord)