# Generated from: 34ecacb5-56de-4a06-8f05-bbd7c9b4ec81.json
# Description: This process details the end-to-end assembly and deployment of custom drones tailored for specialized environmental monitoring. It begins with client consultation to specify unique sensor and flight requirements, followed by component sourcing from niche suppliers. The assembly phase involves precision integration of avionics, sensors, and bespoke software modules. Rigorous multi-stage testing ensures operational reliability under diverse environmental conditions. Subsequent calibration aligns sensor outputs with client specifications. Finally, the process concludes with drone packaging, pilot training sessions, and remote deployment planning, ensuring seamless field operation and data acquisition for research or industrial applications.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Client_Consult = Transition(label='Client Consult')
Specs_Finalize = Transition(label='Specs Finalize')
Component_Sourcing = Transition(label='Component Sourcing')

# Assembly steps - partial order (Frame Assembly, Avionics Install, Sensor Mounting, Software Upload) run concurrently after Component Sourcing
Frame_Assembly = Transition(label='Frame Assembly')
Avionics_Install = Transition(label='Avionics Install')
Sensor_Mounting = Transition(label='Sensor Mounting')
Software_Upload = Transition(label='Software Upload')

# Testing phases - sequential: Initial Testing -> Environmental Test -> Data Validation
Initial_Testing = Transition(label='Initial Testing')
Environmental_Test = Transition(label='Environmental Test')
Data_Validation = Transition(label='Data Validation')

# Calibration after testing
Flight_Calibration = Transition(label='Flight Calibration')

# Final phases packaging prep, pilot training, and deployment planning - partial order concurrent steps after calibration
Packaging_Prep = Transition(label='Packaging Prep')
Pilot_Training = Transition(label='Pilot Training')
Deployment_Plan = Transition(label='Deployment Plan')

# Final support phase after the above three complete
Field_Support = Transition(label='Field Support')

# Build partial orders step by step:

# Assembly concurrent activities (Frame Assembly, Avionics Install, Sensor Mounting, Software Upload)
assembly_nodes = [Frame_Assembly, Avionics_Install, Sensor_Mounting, Software_Upload]
assembly_po = StrictPartialOrder(nodes=assembly_nodes)
# No edges => concurrent

# Testing sequential: Initial Testing -> Environmental Test -> Data Validation
testing_nodes = [Initial_Testing, Environmental_Test, Data_Validation]
testing_po = StrictPartialOrder(nodes=testing_nodes)
testing_po.order.add_edge(Initial_Testing, Environmental_Test)
testing_po.order.add_edge(Environmental_Test, Data_Validation)

# Final concurrent: Packaging Prep, Pilot Training, Deployment Plan
final_nodes = [Packaging_Prep, Pilot_Training, Deployment_Plan]
final_po = StrictPartialOrder(nodes=final_nodes)
# concurrent, no edges

# Build the overall partial order with all phases:
# Start: Client Consult --> Specs Finalize --> Component Sourcing --> assembly_po --> testing_po --> Flight Calibration --> final_po --> Field Support

all_nodes = [
    Client_Consult,
    Specs_Finalize,
    Component_Sourcing,
    assembly_po,
    testing_po,
    Flight_Calibration,
    final_po,
    Field_Support,
]

root = StrictPartialOrder(nodes=all_nodes)

root.order.add_edge(Client_Consult, Specs_Finalize)
root.order.add_edge(Specs_Finalize, Component_Sourcing)
root.order.add_edge(Component_Sourcing, assembly_po)
root.order.add_edge(assembly_po, testing_po)
root.order.add_edge(testing_po, Flight_Calibration)
root.order.add_edge(Flight_Calibration, final_po)
root.order.add_edge(final_po, Field_Support)