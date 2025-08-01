# Generated from: b9c06257-822e-4505-8c1e-f0c5f5c7adb0.json
# Description: This process outlines the steps required to design, assemble, and deploy a custom drone fleet tailored for environmental monitoring in remote areas. It involves initial requirement gathering, prototype design, component sourcing from multiple vendors, iterative testing under varied environmental conditions, software integration for autonomous operations, regulatory compliance checks, pilot training, and final deployment. Continuous feedback loops ensure adaptability and performance improvements, while data collection protocols are established to support long-term ecological studies and reporting obligations to environmental agencies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
requirement_gather   = Transition(label='Requirement Gather')
concept_design       = Transition(label='Concept Design')
vendor_select        = Transition(label='Vendor Select')
component_order      = Transition(label='Component Order')
prototype_build      = Transition(label='Prototype Build')
field_testing        = Transition(label='Field Testing')
performance_review   = Transition(label='Performance Review')
feedback_loop        = Transition(label='Feedback Loop')
software_install     = Transition(label='Software Install')
autonomy_setup       = Transition(label='Autonomy Setup')
compliance_check     = Transition(label='Compliance Check')
pilot_train          = Transition(label='Pilot Train')
data_protocol        = Transition(label='Data Protocol')
fleet_assemble       = Transition(label='Fleet Assemble')
deployment_plan      = Transition(label='Deployment Plan')
report_generate      = Transition(label='Report Generate')
maintenance_schedule = Transition(label='Maintenance Schedule')

# Build the iterative testing loop: do (Field Testing -> Performance Review), then optionally Feedback Loop, repeat
loop_body = StrictPartialOrder(nodes=[field_testing, performance_review])
loop_body.order.add_edge(field_testing, performance_review)
testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, feedback_loop])

# Assemble the full workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    requirement_gather,
    concept_design,
    vendor_select,
    component_order,
    prototype_build,
    testing_loop,
    software_install,
    autonomy_setup,
    compliance_check,
    pilot_train,
    data_protocol,
    fleet_assemble,
    deployment_plan,
    report_generate,
    maintenance_schedule
])

# Define the sequential dependencies
root.order.add_edge(requirement_gather,   concept_design)
root.order.add_edge(concept_design,       vendor_select)
root.order.add_edge(vendor_select,        component_order)
root.order.add_edge(component_order,      prototype_build)
root.order.add_edge(prototype_build,      testing_loop)
root.order.add_edge(testing_loop,         software_install)
root.order.add_edge(software_install,     autonomy_setup)
root.order.add_edge(autonomy_setup,       compliance_check)
root.order.add_edge(compliance_check,     pilot_train)
root.order.add_edge(pilot_train,          data_protocol)
root.order.add_edge(data_protocol,        fleet_assemble)
root.order.add_edge(fleet_assemble,       deployment_plan)
root.order.add_edge(deployment_plan,      report_generate)
root.order.add_edge(report_generate,      maintenance_schedule)