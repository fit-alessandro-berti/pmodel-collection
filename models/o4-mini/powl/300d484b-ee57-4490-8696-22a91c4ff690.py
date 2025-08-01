# Generated from: 300d484b-ee57-4490-8696-22a91c4ff690.json
# Description: This process manages the end-to-end lifecycle of a custom drone fleet tailored for complex environmental monitoring missions. It begins with client consultation to define specific requirements, followed by modular drone design and prototype assembly. The process continues with iterative flight testing, data integration setup, and regulatory compliance validation. After deployment planning and operator training, the fleet undergoes continuous performance monitoring and adaptive maintenance scheduling. Data collected from missions is analyzed for insights, triggering firmware updates and hardware recalibrations. Post-mission reports are generated to refine future deployments and optimize operational efficiency, ensuring sustainable and scalable drone fleet management tailored to unique environmental challenges.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
client_consult      = Transition(label='Client Consult')
requirement_gather  = Transition(label='Requirement Gather')
modular_design      = Transition(label='Modular Design')
prototype_build     = Transition(label='Prototype Build')
flight_testing      = Transition(label='Flight Testing')
data_setup          = Transition(label='Data Setup')
compliance_check    = Transition(label='Compliance Check')
deployment_plan     = Transition(label='Deployment Plan')
operator_train      = Transition(label='Operator Train')
performance_monitor = Transition(label='Performance Monitor')
maintenance_schedule= Transition(label='Maintenance Schedule')
data_analysis       = Transition(label='Data Analysis')
firmware_update     = Transition(label='Firmware Update')
hardware_calibrate  = Transition(label='Hardware Calibrate')
report_generate     = Transition(label='Report Generate')

# Loop 1: iterative Flight Testing -> Data Setup -> Compliance Check
seq_loop1 = StrictPartialOrder(nodes=[flight_testing, data_setup, compliance_check])
seq_loop1.order.add_edge(flight_testing, data_setup)
seq_loop1.order.add_edge(data_setup, compliance_check)
skip1 = SilentTransition()
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[seq_loop1, skip1])

# Loop 2: continuous Performance Monitor -> Maintenance Schedule
seq_loop2 = StrictPartialOrder(nodes=[performance_monitor, maintenance_schedule])
seq_loop2.order.add_edge(performance_monitor, maintenance_schedule)
skip2 = SilentTransition()
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[seq_loop2, skip2])

# Construct the overall partial order
root = StrictPartialOrder(nodes=[
    client_consult,
    requirement_gather,
    modular_design,
    prototype_build,
    loop1,
    deployment_plan,
    operator_train,
    loop2,
    data_analysis,
    firmware_update,
    hardware_calibrate,
    report_generate
])

# Add the sequencing dependencies
root.order.add_edge(client_consult,       requirement_gather)
root.order.add_edge(requirement_gather,   modular_design)
root.order.add_edge(modular_design,       prototype_build)
root.order.add_edge(prototype_build,      loop1)
root.order.add_edge(loop1,                deployment_plan)
root.order.add_edge(deployment_plan,      operator_train)
root.order.add_edge(operator_train,       loop2)
root.order.add_edge(loop2,                data_analysis)
# After analysis, firmware update and hardware calibrate can run in parallel
root.order.add_edge(data_analysis,        firmware_update)
root.order.add_edge(data_analysis,        hardware_calibrate)
# Both updates must complete before report generation
root.order.add_edge(firmware_update,      report_generate)
root.order.add_edge(hardware_calibrate,   report_generate)