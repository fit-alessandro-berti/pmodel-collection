# Generated from: d7288683-2666-4c15-88a1-85e659489353.json
# Description: This process details the end-to-end assembly and customization of bespoke drones tailored for specialized industrial applications. Starting from component sourcing, the workflow includes precision calibration, firmware integration, environmental stress testing, and adaptive AI module installation. Each drone undergoes iterative flight pattern optimization based on simulated mission profiles before final quality assurance and packaging. This atypical process requires coordination across mechanical, software, and electronics teams to ensure each unit meets unique client specifications and regulatory compliance, culminating in secure delivery logistics.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities as labeled transitions
Component_Sourcing = Transition(label='Component Sourcing')
Frame_Assembly = Transition(label='Frame Assembly')
Motor_Installation = Transition(label='Motor Installation')
Sensor_Mounting = Transition(label='Sensor Mounting')
Wiring_Setup = Transition(label='Wiring Setup')
Firmware_Upload = Transition(label='Firmware Upload')
AI_Module = Transition(label='AI Module')
Calibration_Phase = Transition(label='Calibration Phase')
Stress_Testing = Transition(label='Stress Testing')
Flight_Simulation = Transition(label='Flight Simulation')
Pattern_Adjustment = Transition(label='Pattern Adjustment')
Quality_Inspect = Transition(label='Quality Inspect')
Compliance_Check = Transition(label='Compliance Check')
Packaging_Final = Transition(label='Packaging Final')
Delivery_Setup = Transition(label='Delivery Setup')

skip = SilentTransition()

# Build the flight pattern optimization loop:
# loop = *(Calibration_Phase -> Flight_Simulation -> Pattern_Adjustment, skip)
sequence_opt = StrictPartialOrder(nodes=[Calibration_Phase, Flight_Simulation, Pattern_Adjustment])
sequence_opt.order.add_edge(Calibration_Phase, Flight_Simulation)
sequence_opt.order.add_edge(Flight_Simulation, Pattern_Adjustment)
loop_opt = OperatorPOWL(operator=Operator.LOOP, children=[sequence_opt, skip])

# Parallel assembly: frame assembly and motor installation and sensor mounting and wiring setup
# These 4 can be concurrent after component sourcing
assembly_parallel = StrictPartialOrder(nodes=[Frame_Assembly, Motor_Installation, Sensor_Mounting, Wiring_Setup])

# After assembly, firmware upload and AI module and calibration phase start
# Assuming firmware upload and AI module can run concurrently after assembly
firmware_ai_parallel = StrictPartialOrder(nodes=[Firmware_Upload, AI_Module])

# Stress testing after firmware and AI
# Stress_Testing depends on Firmware_Upload and AI_Module
stress_test_po = StrictPartialOrder(nodes=[Firmware_Upload, AI_Module, Stress_Testing])
stress_test_po.order.add_edge(Firmware_Upload, Stress_Testing)
stress_test_po.order.add_edge(AI_Module, Stress_Testing)

# Quality Inspect and Compliance Check can run in parallel after loop optimization and stress testing
quality_compliance_parallel = StrictPartialOrder(nodes=[Quality_Inspect, Compliance_Check])

# Packaging and Delivery Setup sequential after quality and compliance
packaging_delivery_po = StrictPartialOrder(nodes=[Packaging_Final, Delivery_Setup])
packaging_delivery_po.order.add_edge(Packaging_Final, Delivery_Setup)

# Now chain together the entire process respecting dependencies:

# 1. Component Sourcing -> assembly_parallel
step1 = StrictPartialOrder(nodes=[Component_Sourcing, assembly_parallel])
step1.order.add_edge(Component_Sourcing, assembly_parallel)

# Because assembly_parallel is a POWL model itself, but we must treat node and model correctly:
# To do so, use the nodes as list, then for edges add between transitions and operator nodes

# Actually pm4py expects nodes to be Transition or OperatorPOWL. 'assembly_parallel' is a StrictPartialOrder,
# however, StrictPartialOrder is subclass of POWL node, so it can be used as a node in another PO.

# We must add edges between these nodes accordingly.

# Let's define step1 as PO with nodes={Component_Sourcing, assembly_parallel} order = {Component_Sourcing->assembly_parallel}
step1 = StrictPartialOrder(nodes=[Component_Sourcing, assembly_parallel])
step1.order.add_edge(Component_Sourcing, assembly_parallel)

# 2. Assembly -> firmware_ai_parallel
step2 = StrictPartialOrder(nodes=[assembly_parallel, firmware_ai_parallel])
step2.order.add_edge(assembly_parallel, firmware_ai_parallel)

# 3. Firmware & AI -> Stress Testing
step3 = StrictPartialOrder(nodes=[firmware_ai_parallel, Stress_Testing])
step3.order.add_edge(firmware_ai_parallel, Stress_Testing)

# 4. Stress Testing -> loop_opt (flight pattern optimization loop)
step4 = StrictPartialOrder(nodes=[Stress_Testing, loop_opt])
step4.order.add_edge(Stress_Testing, loop_opt)

# 5. loop_opt -> Quality Inspect and Compliance Check (parallel)
step5 = StrictPartialOrder(nodes=[loop_opt, quality_compliance_parallel])
step5.order.add_edge(loop_opt, quality_compliance_parallel)

# 6. Quality Inspect and Compliance Check -> Packaging and Delivery
step6 = StrictPartialOrder(nodes=[quality_compliance_parallel, packaging_delivery_po])
step6.order.add_edge(quality_compliance_parallel, packaging_delivery_po)

# Chain all steps into one final PO
root = StrictPartialOrder(nodes=[step1, step2, step3, step4, step5, step6])

# Add edges between steps accordingly
root.order.add_edge(step1, step2)
root.order.add_edge(step2, step3)
root.order.add_edge(step3, step4)
root.order.add_edge(step4, step5)
root.order.add_edge(step5, step6)