# Generated from: aa251f3d-392c-4376-881a-324ecde6a71e.json
# Description: This process outlines the highly specialized assembly of custom drones tailored for diverse industrial applications such as agriculture, surveillance, and delivery. It begins with design specification collection from clients followed by component sourcing that includes rare materials and specialized electronics. Subsequent activities involve precision machining, micro-soldering of circuit boards, and advanced sensor calibration under controlled environments. Quality assurance includes real-time flight simulation and adaptive software integration specific to each drone model. Final steps cover packaging with anti-static materials and customized documentation before shipping. This atypical process requires interdisciplinary coordination between engineering, procurement, and software teams to ensure every drone meets exacting client demands and regulatory standards, emphasizing flexibility and innovation in manufacturing.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Spec_Collection = Transition(label='Spec Collection')
Component_Sourcing = Transition(label='Component Sourcing')
Material_Inspection = Transition(label='Material Inspection')
Circuit_Assembly = Transition(label='Circuit Assembly')
Sensor_Calibration = Transition(label='Sensor Calibration')
Firmware_Upload = Transition(label='Firmware Upload')
Flight_Simulation = Transition(label='Flight Simulation')
Structural_Testing = Transition(label='Structural Testing')
Software_Integration = Transition(label='Software Integration')
Thermal_Imaging = Transition(label='Thermal Imaging')
Battery_Conditioning = Transition(label='Battery Conditioning')
Anti_Static_Pack = Transition(label='Anti-Static Pack')
Documentation_Prep = Transition(label='Documentation Prep')
Client_Approval = Transition(label='Client Approval')
Shipping_Dispatch = Transition(label='Shipping Dispatch')

# Build the process stepwise with partial orders and choices

# Step 1: Spec Collection --> Component Sourcing --> Material Inspection
step1 = StrictPartialOrder(nodes=[Spec_Collection, Component_Sourcing, Material_Inspection])
step1.order.add_edge(Spec_Collection, Component_Sourcing)
step1.order.add_edge(Component_Sourcing, Material_Inspection)

# Step 2: Precision machining and assembly (Circuit Assembly)
# Precede Sensor Calibration with possible concurrency of Circuit Assembly and Material Inspection
# but since Material Inspection is before Circuit Assembly we leave this linear

# Sensor Calibration includes advanced sensor calibration under controlled environments,
# Thermal Imaging and Battery Conditioning are specialized concurrent activities during calibration
calibration_parallel = StrictPartialOrder(
    nodes=[Sensor_Calibration, Thermal_Imaging, Battery_Conditioning]
)
# no order among these three => concurrent

# Circuit Assembly precedes calibration parallel activities
calibration_and_assembly = StrictPartialOrder(
    nodes=[Circuit_Assembly, calibration_parallel]
)
calibration_and_assembly.order.add_edge(Circuit_Assembly, calibration_parallel)

# Step 3: Firmware Upload after calibration and assembly
firmware_and_tests = StrictPartialOrder(
    nodes=[Firmware_Upload, Flight_Simulation, Structural_Testing]
)
firmware_and_tests.order.add_edge(Firmware_Upload, Flight_Simulation)
firmware_and_tests.order.add_edge(Firmware_Upload, Structural_Testing)

# Step 4: Software integration (adaptive) after flight simulation and structural testing
software_integration = StrictPartialOrder(
    nodes=[Software_Integration, firmware_and_tests]
)
software_integration.order.add_edge(firmware_and_tests, Software_Integration)

# Step 5: Packaging with Anti-Static Pack and Documentation Prep (concurrent)
final_packaging = StrictPartialOrder(
    nodes=[Anti_Static_Pack, Documentation_Prep]
)
# no order - concurrent

# Step 6: Client Approval must be done before Shipping Dispatch
final_approval = StrictPartialOrder(
    nodes=[Client_Approval, Shipping_Dispatch]
)
final_approval.order.add_edge(Client_Approval, Shipping_Dispatch)

# Combine final packaging to Client Approval and Shipping Dispatch sequence
pack_doc_to_approval = StrictPartialOrder(
    nodes=[final_packaging, final_approval]
)

pack_doc_to_approval.order.add_edge(final_packaging, final_approval)

# Now create the overall process combining all steps in correct order:
# Spec Collection -> Component Sourcing -> Material Inspection -> then Circuit Assembly and calibration
# (calibration_parallel is embedded in calibration_and_assembly)
# then firmware_and_tests
# then software_integration
# then packaging and documentation prep
# then client approval + shipping dispatch

# Start combining partial orders in sequence:

# 1 -> 2
step1_to_calib = StrictPartialOrder(
    nodes=[step1, calibration_and_assembly]
)
step1_to_calib.order.add_edge(step1, calibration_and_assembly)

# Append firmware_and_tests after calibration_and_assembly
calib_to_firmware = StrictPartialOrder(
    nodes=[step1_to_calib, firmware_and_tests]
)
calib_to_firmware.order.add_edge(step1_to_calib, firmware_and_tests)

# Append software_integration after firmware_and_tests
firmware_to_software = StrictPartialOrder(
    nodes=[calib_to_firmware, software_integration]
)
firmware_to_software.order.add_edge(calib_to_firmware, software_integration)

# Append packaging and documentation after software integration
software_to_packaging = StrictPartialOrder(
    nodes=[firmware_to_software, pack_doc_to_approval]
)
software_to_packaging.order.add_edge(firmware_to_software, pack_doc_to_approval)

root = software_to_packaging