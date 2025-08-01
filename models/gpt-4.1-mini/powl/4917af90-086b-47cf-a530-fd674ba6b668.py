# Generated from: 4917af90-086b-47cf-a530-fd674ba6b668.json
# Description: This process outlines the complex assembly and calibration of custom drones tailored for specialized industrial applications. Starting from component sourcing through iterative firmware tuning, the workflow includes precision mechanical integration, sensor alignment, and multi-environment testing. Each drone undergoes adaptive software calibration based on mission-specific parameters, followed by compliance verification with aviation regulations. The process concludes with detailed quality reporting and client-specific customization before final packaging and delivery, ensuring high reliability and performance in diverse operational conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
Component_Sourcing = Transition(label='Component Sourcing')
Frame_Assembly = Transition(label='Frame Assembly')
Motor_Installation = Transition(label='Motor Installation')
Wiring_Setup = Transition(label='Wiring Setup')
Sensor_Mounting = Transition(label='Sensor Mounting')
Firmware_Upload = Transition(label='Firmware Upload')
Calibration_Stage = Transition(label='Calibration Stage')
Software_Tuning = Transition(label='Software Tuning')
Env_Testing = Transition(label='Env Testing')
Flight_Simulation = Transition(label='Flight Simulation')
Compliance_Check = Transition(label='Compliance Check')
Performance_Audit = Transition(label='Performance Audit')
Client_Customization = Transition(label='Client Customization')
Quality_Reporting = Transition(label='Quality Reporting')
Final_Packaging = Transition(label='Final Packaging')
Delivery_Scheduling = Transition(label='Delivery Scheduling')

# Loop modeling iterative firmware tuning:
# Loop body: Calibration_Stage followed by Software_Tuning
# Loop redo part: Software_Tuning then Calibration_Stage again (until exit)
loop_firmware_tuning = OperatorPOWL(operator=Operator.LOOP, children=[Calibration_Stage, Software_Tuning])

# Partial order for initial assembly steps:
# Component Sourcing -> Frame Assembly -> Motor Installation -> Wiring Setup -> Sensor Mounting -> Firmware Upload
initial_assembly = StrictPartialOrder(nodes=[
    Component_Sourcing,
    Frame_Assembly,
    Motor_Installation,
    Wiring_Setup,
    Sensor_Mounting,
    Firmware_Upload
])
initial_assembly.order.add_edge(Component_Sourcing, Frame_Assembly)
initial_assembly.order.add_edge(Frame_Assembly, Motor_Installation)
initial_assembly.order.add_edge(Motor_Installation, Wiring_Setup)
initial_assembly.order.add_edge(Wiring_Setup, Sensor_Mounting)
initial_assembly.order.add_edge(Sensor_Mounting, Firmware_Upload)

# Partial order for testing and calibration phase:
# Firmware Upload -> calibration loop -> Env Testing and Flight Simulation concurrent
testing_and_calibration = StrictPartialOrder(nodes=[Firmware_Upload, loop_firmware_tuning, Env_Testing, Flight_Simulation])
testing_and_calibration.order.add_edge(Firmware_Upload, loop_firmware_tuning)
testing_and_calibration.order.add_edge(loop_firmware_tuning, Env_Testing)
testing_and_calibration.order.add_edge(loop_firmware_tuning, Flight_Simulation)
# Env Testing and Flight Simulation concurrent (no order between them)

# Compliance check after testing & calibration
compliance_and_audit = StrictPartialOrder(nodes=[Compliance_Check, Performance_Audit])
compliance_and_audit.order.add_edge(Compliance_Check, Performance_Audit)

# Adaptive software calibration to compliance check:
# After Flight Simulation and Env Testing finish, Compliance Check happens
# We connect compliance_and_audit partial order after testing_and_calibration
# Since testing_and_calibration contains loop_firmware_tuning and Env_Testing and Flight_Simulation,
# we add edges from these to Compliance_Check for partial ordering
# Will do outside partial order by adding a root order later.

# Final customization and reporting concurrent:
customization_and_reporting = StrictPartialOrder(nodes=[Client_Customization, Quality_Reporting])
# No order between Client Customization and Quality Reporting (concurrent)

# Final packaging followed by delivery scheduling
final_packaging_and_delivery = StrictPartialOrder(nodes=[Final_Packaging, Delivery_Scheduling])
final_packaging_and_delivery.order.add_edge(Final_Packaging, Delivery_Scheduling)

# Now assemble all phases in a big partial order root

# Gather all top-level nodes for root
nodes_root = [
    initial_assembly,
    testing_and_calibration,
    compliance_and_audit,
    customization_and_reporting,
    final_packaging_and_delivery
]

root = StrictPartialOrder(nodes=nodes_root)

# Link phases:
# initial_assembly -> testing_and_calibration (Firmware Upload to Firmware Upload node inside testing_and_calibration)
# But Firmware_Upload is shared, here it appears as node in initial_assembly and testing_and_calibration,
# this is a model reuse - to keep consistent, we will only link initial_assembly to testing_and_calibration by
# initial_assembly completes (Firmware_Upload) to calibration loop start (loop_firmware_tuning)

root.order.add_edge(initial_assembly, testing_and_calibration)

# Add explicit edges inside testing_and_calibration already
# We now link testing_and_calibration to compliance_and_audit
root.order.add_edge(testing_and_calibration, compliance_and_audit)

# Link compliance_and_audit to customization_and_reporting and final_packaging_and_delivery
root.order.add_edge(compliance_and_audit, customization_and_reporting)
root.order.add_edge(customization_and_reporting, final_packaging_and_delivery)

# The structure models the overall drone assembly and calibration process:
# Component sourcing through assembly -> firmware upload and iterative tuning (loop) -> testing (Env Testing, Flight Simulation concurrent)
# -> Compliance and audit -> customization and quality reporting concurrent -> final packaging and delivery
