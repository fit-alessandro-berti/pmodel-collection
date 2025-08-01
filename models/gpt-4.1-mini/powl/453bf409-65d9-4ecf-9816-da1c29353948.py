# Generated from: 453bf409-65d9-4ecf-9816-da1c29353948.json
# Description: This process involves the end-to-end assembly and testing of custom-made drones tailored to unique client specifications. It begins with detailed requirement analysis, followed by component sourcing from multiple specialized suppliers. Each drone frame is assembled manually to ensure precision. Firmware is then developed and uploaded to the flight controller. The drone undergoes multi-stage calibration, including sensor alignment and motor balancing. After initial bench testing, a simulated flight test is conducted in a controlled environment. Post-testing, data analytics are applied to evaluate performance metrics. If the drone passes quality standards, it is packaged with personalized documentation and shipped using a custom logistics solution. Throughout, frequent client updates and iterative feedback integration ensure the final product meets exact expectations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Requirement_Review = Transition(label='Requirement Review')
Supplier_Selection = Transition(label='Supplier Selection')
Component_Sourcing = Transition(label='Component Sourcing')
Frame_Assembly = Transition(label='Frame Assembly')
Firmware_Upload = Transition(label='Firmware Upload')
Sensor_Calibration = Transition(label='Sensor Calibration')
Motor_Balancing = Transition(label='Motor Balancing')
Bench_Testing = Transition(label='Bench Testing')
Flight_Simulation = Transition(label='Flight Simulation')
Data_Analysis = Transition(label='Data Analysis')
Quality_Audit = Transition(label='Quality Audit')
Client_Feedback = Transition(label='Client Feedback')
Documentation_Prep = Transition(label='Documentation Prep')
Custom_Packaging = Transition(label='Custom Packaging')
Logistics_Planning = Transition(label='Logistics Planning')
Shipment_Dispatch = Transition(label='Shipment Dispatch')

# Create loop for iterative feedback integration:
# loop body A = activities after Quality Audit until Client Feedback
# body B = Client Feedback

# The iterative feedback occurs throughout finalization after initial quality audit:
# Interpretation:
# - Execute Quality Audit
# - Then a loop of (Client Feedback) followed by the final packaging and shipment steps,
#   repeating until client is satisfied (loop exit)

# Finalization after Quality Audit:
finalization_after_audit = StrictPartialOrder(
    nodes=[Documentation_Prep, Custom_Packaging, Logistics_Planning, Shipment_Dispatch]
)
finalization_after_audit.order.add_edge(Documentation_Prep, Custom_Packaging)
finalization_after_audit.order.add_edge(Custom_Packaging, Logistics_Planning)
finalization_after_audit.order.add_edge(Logistics_Planning, Shipment_Dispatch)

# Loop: execute finalization_after_audit (A), then choice to exit or Client_Feedback (B)
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    finalization_after_audit,
    Client_Feedback
])

# Calibration partial order: Sensor Calibration and Motor Balancing concurrent
calibration = StrictPartialOrder(
    nodes=[Sensor_Calibration, Motor_Balancing]
)
# no edges: concurrent

# After firmware upload, calibration happens
# Then bench testing, then flight simulation, then data analysis, then quality audit
testing_sequence = StrictPartialOrder(
    nodes=[Bench_Testing, Flight_Simulation, Data_Analysis, Quality_Audit, loop]
)
testing_sequence.order.add_edge(Bench_Testing, Flight_Simulation)
testing_sequence.order.add_edge(Flight_Simulation, Data_Analysis)
testing_sequence.order.add_edge(Data_Analysis, Quality_Audit)
testing_sequence.order.add_edge(Quality_Audit, loop)

# Assembly workflow
assembly_sequence = StrictPartialOrder(
    nodes=[Frame_Assembly, Firmware_Upload, calibration]
)
assembly_sequence.order.add_edge(Frame_Assembly, Firmware_Upload)
assembly_sequence.order.add_edge(Firmware_Upload, calibration)

# Procurement workflow sequential
procurement_sequence = StrictPartialOrder(
    nodes=[Supplier_Selection, Component_Sourcing]
)
procurement_sequence.order.add_edge(Supplier_Selection, Component_Sourcing)

# Initial phase order: requirement review, then procurement, then assembly, then testing sequence
initial_sequence = StrictPartialOrder(
    nodes=[Requirement_Review, procurement_sequence, assembly_sequence, testing_sequence]
)
initial_sequence.order.add_edge(Requirement_Review, procurement_sequence)
initial_sequence.order.add_edge(procurement_sequence, assembly_sequence)
initial_sequence.order.add_edge(assembly_sequence, testing_sequence)

# root model is the whole sequence
root = initial_sequence