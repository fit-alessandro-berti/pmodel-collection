# Generated from: 25bca7e9-a9d7-47ba-b3a5-b42aaa9385f1.json
# Description: This process outlines the complex assembly and configuration of custom drones tailored for specialized industrial applications. It involves initial client specification gathering, component sourcing from multiple suppliers with quality verification, precision assembly under controlled environmental conditions, firmware customization based on mission parameters, multi-stage testing including flight simulation and stress analysis, iterative adjustments for performance optimization, regulatory compliance checks, packaging with anti-static measures, and final shipment coordination with logistics partners. Each activity ensures the drone meets strict client requirements and industry standards before deployment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Client_Specs = Transition(label='Client Specs')
Component_Sourcing = Transition(label='Component Sourcing')
Quality_Check = Transition(label='Quality Check')
Frame_Assembly = Transition(label='Frame Assembly')
Wiring_Setup = Transition(label='Wiring Setup')
Firmware_Load = Transition(label='Firmware Load')
Calibration_Run = Transition(label='Calibration Run')
Flight_Sim = Transition(label='Flight Sim')
Stress_Test = Transition(label='Stress Test')
Adjust_Settings = Transition(label='Adjust Settings')
Compliance_Audit = Transition(label='Compliance Audit')
Packaging_Prep = Transition(label='Packaging Prep')
Static_Shield = Transition(label='Static Shield')
Logistics_Plan = Transition(label='Logistics Plan')
Final_Dispatch = Transition(label='Final Dispatch')

# Multi-stage testing sequence: Flight Sim and Stress Test are concurrent, both before Adjust Settings
testing = StrictPartialOrder(nodes=[Flight_Sim, Stress_Test])
# no order edges between Flight Sim and Stress Test => concurrent

# After testing, Adjust Settings (iterative loop: Adjust_Settings then calibration run, flight sim & stress test again)
# Define loop body:
# Loop semantics (* (A, B)):
#  - A = Adjust Settings
#  - B = testing sub-process + Calibration Run (since calibration is part of performance optimization)
# The loop: do Adjust_Settings (A), then either exit or do (B then A again)
# B is: Calibration_Run followed by concurrent testing (Flight_Sim & Stress_Test)
# We model B as partial order with nodes [Calibration_Run, testing], order {Calibration_Run --> Flight_Sim and Calibration_Run --> Stress_Test}

calibration_and_testing = StrictPartialOrder(nodes=[Calibration_Run, Flight_Sim, Stress_Test])
calibration_and_testing.order.add_edge(Calibration_Run, Flight_Sim)
calibration_and_testing.order.add_edge(Calibration_Run, Stress_Test)

loop_body = OperatorPOWL(operator=Operator.LOOP, children=[Adjust_Settings, calibration_and_testing])

# Frame Assembly and Wiring Setup are sequential prior to Firmware Load
assembly = StrictPartialOrder(nodes=[Frame_Assembly, Wiring_Setup, Firmware_Load])
assembly.order.add_edge(Frame_Assembly, Wiring_Setup)
assembly.order.add_edge(Wiring_Setup, Firmware_Load)

# Component sourcing and quality check sequential
sourcing_quality = StrictPartialOrder(nodes=[Component_Sourcing, Quality_Check])
sourcing_quality.order.add_edge(Component_Sourcing, Quality_Check)

# Packaging Prep and Static Shield concurrent (packing with anti-static measures)
packaging = StrictPartialOrder(nodes=[Packaging_Prep, Static_Shield])
# no edges means concurrent

# Logistics Plan and Final Dispatch sequential
dispatch = StrictPartialOrder(nodes=[Logistics_Plan, Final_Dispatch])
dispatch.order.add_edge(Logistics_Plan, Final_Dispatch)

# Compliance Audit after loop (the iterative adjustments and testing)
# Then packaging
# Then logistics

# Build main partial order of the process:
# Start with Client Specs
# Then sourcing_quality
# Then assembly
# Then loop_body (iterative adjustments/testing)
# Then Compliance Audit
# Then packaging
# Then dispatch

root = StrictPartialOrder(
    nodes=[
        Client_Specs,
        sourcing_quality,
        assembly,
        loop_body,
        Compliance_Audit,
        packaging,
        dispatch
    ]
)

# Add control flow dependencies:
root.order.add_edge(Client_Specs, sourcing_quality)
root.order.add_edge(sourcing_quality, assembly)
root.order.add_edge(assembly, loop_body)
root.order.add_edge(loop_body, Compliance_Audit)
root.order.add_edge(Compliance_Audit, packaging)
root.order.add_edge(packaging, dispatch)