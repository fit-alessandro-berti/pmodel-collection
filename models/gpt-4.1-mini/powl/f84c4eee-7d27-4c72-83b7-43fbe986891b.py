# Generated from: f84c4eee-7d27-4c72-83b7-43fbe986891b.json
# Description: This process involves the end-to-end assembly and calibration of highly customized drones tailored to specific client requirements. It begins with component sourcing, followed by frame assembly, electronics integration, and software loading. Quality assurance includes multiple test flights under varied conditions. Specialized calibration ensures optimal sensor accuracy and flight stability. Final packaging is designed to accommodate delicate parts and personalized documentation, while post-delivery support schedules remote diagnostics and firmware updates to maintain peak performance throughout the drone’s lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Component_Sourcing = Transition(label='Component Sourcing')
Frame_Assembly = Transition(label='Frame Assembly')
Sensor_Mounting = Transition(label='Sensor Mounting')
Wiring_Harness = Transition(label='Wiring Harness')
Circuit_Testing = Transition(label='Circuit Testing')
Firmware_Loading = Transition(label='Firmware Loading')
Initial_Calibration = Transition(label='Initial Calibration')
Software_Integration = Transition(label='Software Integration')
Flight_Testing = Transition(label='Flight Testing')
Data_Logging = Transition(label='Data Logging')
Performance_Tuning = Transition(label='Performance Tuning')
Packaging_Prep = Transition(label='Packaging Prep')
Custom_Labeling = Transition(label='Custom Labeling')
Documentation_Print = Transition(label='Documentation Print')
Quality_Review = Transition(label='Quality Review')
Client_Training = Transition(label='Client Training')
Remote_Monitoring = Transition(label='Remote Monitoring')
Firmware_Update = Transition(label='Firmware Update')

# First partial order: the assembly and integration phase
assembly_nodes = [
    Component_Sourcing,
    Frame_Assembly,
    Sensor_Mounting,
    Wiring_Harness,
    Circuit_Testing,
    Firmware_Loading,
    Initial_Calibration,
    Software_Integration
]
assembly = StrictPartialOrder(nodes=assembly_nodes)
assembly.order.add_edge(Component_Sourcing, Frame_Assembly)
assembly.order.add_edge(Frame_Assembly, Sensor_Mounting)
assembly.order.add_edge(Sensor_Mounting, Wiring_Harness)
assembly.order.add_edge(Wiring_Harness, Circuit_Testing)
assembly.order.add_edge(Circuit_Testing, Firmware_Loading)
assembly.order.add_edge(Firmware_Loading, Initial_Calibration)
assembly.order.add_edge(Initial_Calibration, Software_Integration)

# Second partial order: Quality Assurance phase (test flights & data logging & tuning)
qa_nodes = [Flight_Testing, Data_Logging, Performance_Tuning]
qa = StrictPartialOrder(nodes=qa_nodes)
# The three activities run partially concurrently but Flight_Testing precedes Data_Logging and Performance_Tuning
qa.order.add_edge(Flight_Testing, Data_Logging)
qa.order.add_edge(Flight_Testing, Performance_Tuning)
# Data_Logging and Performance_Tuning concurrent (no order between them)

# Third partial order: Final Packaging phase
packaging_nodes = [Packaging_Prep, Custom_Labeling, Documentation_Print]
packaging = StrictPartialOrder(nodes=packaging_nodes)
packaging.order.add_edge(Packaging_Prep, Custom_Labeling)
packaging.order.add_edge(Packaging_Prep, Documentation_Print)
# Custom_Labeling and Documentation_Print concurrent (no edge between them)

# Fourth partial order: Post-delivery support phase
support_nodes = [Client_Training, Remote_Monitoring, Firmware_Update]
support = StrictPartialOrder(nodes=support_nodes)
support.order.add_edge(Client_Training, Remote_Monitoring)
support.order.add_edge(Remote_Monitoring, Firmware_Update)

# Combine the phases into the full process partial order
root = StrictPartialOrder(
    nodes=[assembly, qa, Quality_Review, packaging, support]
)

# Define order between phases:
root.order.add_edge(assembly, Quality_Review)    # After assembly, quality review
root.order.add_edge(Quality_Review, qa)          # Quality review precedes QA test flights etc.
root.order.add_edge(qa, packaging)                # QA before packaging
root.order.add_edge(packaging, support)           # Packaging before support