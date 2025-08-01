# Generated from: 527e357b-8769-4cdf-8ecb-a7b53bc323a0.json
# Description: This process involves the bespoke assembly of custom drones tailored to unique client specifications. It begins with requirement gathering and component sourcing, followed by precise frame construction. The next steps include sensor calibration, software integration, and quality assurance testing. Specialized activities such as aerodynamic tuning, battery optimization, and secure communication setup ensure superior performance. Final stages involve pilot training, deployment planning, and ongoing maintenance scheduling. The process requires interdisciplinary coordination between engineering, software development, and customer support teams to deliver fully functional, customized drone solutions efficiently and reliably.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Client_Brief = Transition(label='Client Brief')
Part_Sourcing = Transition(label='Part Sourcing')
Frame_Build = Transition(label='Frame Build')
Sensor_Setup = Transition(label='Sensor Setup')
Software_Load = Transition(label='Software Load')
Calibration_Test = Transition(label='Calibration Test')
Aerodynamic_Tune = Transition(label='Aerodynamic Tune')
Battery_Check = Transition(label='Battery Check')
Comm_Setup = Transition(label='Comm Setup')
Flight_Trial = Transition(label='Flight Trial')
Quality_Audit = Transition(label='Quality Audit')
Pilot_Train = Transition(label='Pilot Train')
Deploy_Plan = Transition(label='Deploy Plan')
Maintenance_Log = Transition(label='Maintenance Log')
Feedback_Review = Transition(label='Feedback Review')

# Define partial orders for specialized and final stages that are concurrent activities
# Specialized tuning: Aerodynamic Tune, Battery Check, and Comm Setup are likely concurrent after Calibration Test
specialized = StrictPartialOrder(nodes=[Aerodynamic_Tune, Battery_Check, Comm_Setup])

# Final stages Pilot Train, Deploy Plan, Maintenance Log happen sequentially (pilot train -> deploy plan -> maintenance)
final_stages = StrictPartialOrder(nodes=[Pilot_Train, Deploy_Plan, Maintenance_Log])
final_stages.order.add_edge(Pilot_Train, Deploy_Plan)
final_stages.order.add_edge(Deploy_Plan, Maintenance_Log)

# The feedback review likely follows maintenance log to close the loop of ongoing improvement
feedback = Feedback_Review

# Build the main sequence and parallelism step by step:

# Initial sequence: Client Brief -> Part Sourcing -> Frame Build
initial_seq = StrictPartialOrder(
    nodes=[Client_Brief, Part_Sourcing, Frame_Build])
initial_seq.order.add_edge(Client_Brief, Part_Sourcing)
initial_seq.order.add_edge(Part_Sourcing, Frame_Build)

# Then Sensor Setup -> Software Load -> Calibration Test
mid_seq = StrictPartialOrder(
    nodes=[Sensor_Setup, Software_Load, Calibration_Test])
mid_seq.order.add_edge(Sensor_Setup, Software_Load)
mid_seq.order.add_edge(Software_Load, Calibration_Test)

# calibration test must precede the specialized tuning activities
# connect mid_seq -> specialized
# Also Flight Trial and Quality Audit happen after specialized tuning
# Flight Trial and Quality Audit can happen sequentially or in parallel?
# The description suggests quality assurance testing is before specialized tuning, but 
# "Calibration Test" + "Quality Assurance testing" are in description. 
# "Calibration Test" and "Quality Audit" are different steps:
# "Calibration Test" before specialized tuning
# "Quality Audit" after Flight Trial (Flight Trial then Quality Audit)
flight_and_quality = StrictPartialOrder(nodes=[Flight_Trial, Quality_Audit])
flight_and_quality.order.add_edge(Flight_Trial, Quality_Audit)

# Maintenance Log precedes Feedback Review
maintenance_and_feedback = StrictPartialOrder(nodes=[Maintenance_Log, Feedback_Review])
maintenance_and_feedback.order.add_edge(Maintenance_Log, Feedback_Review)

# Compose the whole process: 
# initial_seq -> mid_seq -> specialized -> flight_and_quality -> final_stages -> maintenance_and_feedback

root = StrictPartialOrder(nodes=[
    initial_seq,
    mid_seq,
    specialized,
    flight_and_quality,
    final_stages,
    maintenance_and_feedback
])

# Add edges to impose order between these subprocesses
root.order.add_edge(initial_seq, mid_seq)
root.order.add_edge(mid_seq, specialized)
root.order.add_edge(specialized, flight_and_quality)
root.order.add_edge(flight_and_quality, final_stages)
root.order.add_edge(final_stages, maintenance_and_feedback)