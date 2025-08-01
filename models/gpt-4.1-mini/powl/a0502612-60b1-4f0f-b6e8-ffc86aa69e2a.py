# Generated from: a0502612-60b1-4f0f-b6e8-ffc86aa69e2a.json
# Description: This process outlines the assembly and deployment of custom drones tailored for specialized industrial applications. It begins with component sourcing from multiple niche suppliers, followed by precision calibration of sensors and flight systems. Subsequent steps include firmware customization, modular payload integration, and rigorous multi-environment testing. Quality assurance involves iterative feedback loops between engineers and test pilots to refine flight stability and sensor accuracy. Finally, the drones undergo packaging with tailored user manuals and are shipped under controlled conditions to ensure integrity upon delivery. This atypical process requires coordination across hardware, software, and logistics teams to meet highly specific client requirements within tight deadlines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
Part_Sourcing = Transition(label='Part Sourcing')
Sensor_Align = Transition(label='Sensor Align')
Frame_Build = Transition(label='Frame Build')
Motor_Install = Transition(label='Motor Install')
Firmware_Flash = Transition(label='Firmware Flash')
Payload_Fit = Transition(label='Payload Fit')
Signal_Tune = Transition(label='Signal Tune')
Flight_Test = Transition(label='Flight Test')
Data_Log = Transition(label='Data Log')
Error_Fix = Transition(label='Error Fix')
Pilot_Review = Transition(label='Pilot Review')
Quality_Audit = Transition(label='Quality Audit')
Manual_Write = Transition(label='Manual Write')
Package_Prep = Transition(label='Package Prep')
Dispatch_Arrange = Transition(label='Dispatch Arrange')
Client_Confirm = Transition(label='Client Confirm')
Feedback_Loop = Transition(label='Feedback Loop')

# Build assembly partial order: after Part Sourcing
# Precision calibration of sensors and flight systems
# We'll model Frame Build and Motor Install concurrently after Sensor Align
# After Part Sourcing --> Sensor Align
# Sensor Align --> Frame Build and Motor Install (concurrent)
assembly_PO = StrictPartialOrder(nodes=[Part_Sourcing, Sensor_Align, Frame_Build, Motor_Install])
assembly_PO.order.add_edge(Part_Sourcing, Sensor_Align)
assembly_PO.order.add_edge(Sensor_Align, Frame_Build)
assembly_PO.order.add_edge(Sensor_Align, Motor_Install)

# Firmware customization and Payload Fit and Signal Tune in sequence
firmware_PO = StrictPartialOrder(nodes=[Firmware_Flash, Payload_Fit, Signal_Tune])
firmware_PO.order.add_edge(Firmware_Flash, Payload_Fit)
firmware_PO.order.add_edge(Payload_Fit, Signal_Tune)

# Multi-environment testing sequence: Flight Test then Data Log
testing_PO = StrictPartialOrder(nodes=[Flight_Test, Data_Log])
testing_PO.order.add_edge(Flight_Test, Data_Log)

# Quality assurance with iterative feedback loops between engineers (Error Fix) and test pilots (Pilot Review)
# Model as a loop: run Feedback Loop (which is iterative interaction) after Data Log before Quality Audit
# We'll approximate the feedback loop with LOOP operator:
# LOOP with A = Quality_Audit, B = partial order: Pilot Review and Error Fix and Feedback Loop concurrent?

# Make the feedback activities partially ordered:
feedback_nodes = [Pilot_Review, Error_Fix, Feedback_Loop]
feedback_PO = StrictPartialOrder(nodes=feedback_nodes)
# Assume these three are concurrent (can happen independently)
# Loop operator children: first child = Quality_Audit, second child = feedback_PO

loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Audit, feedback_PO])

# Packaging and shipping in sequence: Manual Write --> Package Prep --> Dispatch Arrange --> Client Confirm
packaging_PO = StrictPartialOrder(nodes=[Manual_Write, Package_Prep, Dispatch_Arrange, Client_Confirm])
packaging_PO.order.add_edge(Manual_Write, Package_Prep)
packaging_PO.order.add_edge(Package_Prep, Dispatch_Arrange)
packaging_PO.order.add_edge(Dispatch_Arrange, Client_Confirm)

# Now build the entire process partial order:
# After assembly_PO, run firmware_PO
# After firmware_PO, run Signal_Tune
# After Signal_Tune, run testing_PO
# After testing_PO, run loop_feedback
# After loop_feedback, run packaging_PO

root = StrictPartialOrder(nodes=[assembly_PO, firmware_PO, testing_PO, loop_feedback, packaging_PO])
root.order.add_edge(assembly_PO, firmware_PO)
root.order.add_edge(firmware_PO, testing_PO)
root.order.add_edge(testing_PO, loop_feedback)
root.order.add_edge(loop_feedback, packaging_PO)