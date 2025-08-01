# Generated from: 9b8263b8-d9c8-4927-9f21-f08141872466.json
# Description: This process outlines the intricate steps involved in designing, assembling, and testing custom drones tailored for specialized industrial applications. It begins with client consultation to define unique specifications, followed by modular component selection, precision 3D printing of custom parts, and advanced circuit programming. Subsequent stages include meticulous mechanical assembly, multi-phase calibration, environmental stress testing, and iterative firmware optimization. Final steps involve comprehensive quality assurance, client demonstration, and deployment logistics planning, ensuring each drone meets exacting performance and safety standards in diverse operational environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
Client_Meeting = Transition(label='Client Meeting')
Spec_Definition = Transition(label='Spec Definition')
Module_Selection = Transition(label='Module Selection')
Printing_3D = Transition(label='3D Printing')
Circuit_Design = Transition(label='Circuit Design')
Firmware_Coding = Transition(label='Firmware Coding')
Mechanical_Build = Transition(label='Mechanical Build')
Calibration_Phase = Transition(label='Calibration Phase')
Stress_Testing = Transition(label='Stress Testing')
Software_Tuning = Transition(label='Software Tuning')
Quality_Check = Transition(label='Quality Check')
Demo_Preparation = Transition(label='Demo Preparation')
Client_Review = Transition(label='Client Review')
Packaging = Transition(label='Packaging')
Deployment_Plan = Transition(label='Deployment Plan')

# Build partial order with edges reflecting the described process sequence (partial order, so concurrency possible if no direct edge)
root = StrictPartialOrder(nodes=[
    Client_Meeting, Spec_Definition, Module_Selection, Printing_3D, Circuit_Design,
    Firmware_Coding, Mechanical_Build, Calibration_Phase, Stress_Testing, Software_Tuning,
    Quality_Check, Demo_Preparation, Client_Review, Packaging, Deployment_Plan
])

# Define order edges based on the process description sequentially:
root.order.add_edge(Client_Meeting, Spec_Definition)
root.order.add_edge(Spec_Definition, Module_Selection)
root.order.add_edge(Module_Selection, Printing_3D)
root.order.add_edge(Printing_3D, Circuit_Design)
root.order.add_edge(Circuit_Design, Firmware_Coding)
root.order.add_edge(Firmware_Coding, Mechanical_Build)
root.order.add_edge(Mechanical_Build, Calibration_Phase)
root.order.add_edge(Calibration_Phase, Stress_Testing)
root.order.add_edge(Stress_Testing, Software_Tuning)
root.order.add_edge(Software_Tuning, Quality_Check)
root.order.add_edge(Quality_Check, Demo_Preparation)
root.order.add_edge(Demo_Preparation, Client_Review)
root.order.add_edge(Client_Review, Packaging)
root.order.add_edge(Packaging, Deployment_Plan)