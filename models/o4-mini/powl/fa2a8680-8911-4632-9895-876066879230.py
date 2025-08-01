# Generated from: fa2a8680-8911-4632-9895-876066879230.json
# Description: This process outlines the end-to-end workflow for deploying a custom drone fleet tailored to environmental monitoring in remote areas. It involves initial client consultation to gather unique requirements, followed by modular drone design and component sourcing from specialized suppliers. Prototype assembly and rigorous field testing ensure operational reliability under extreme conditions. After validation, software integration for real-time data analytics and autonomous navigation is conducted. The fleet undergoes pilot training and regulatory compliance verification before final deployment. Post-deployment includes continuous remote monitoring, maintenance scheduling, and iterative performance optimization through AI-driven feedback mechanisms, ensuring the drones adapt to evolving environmental challenges effectively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
client_meet      = Transition(label='Client Meet')
requirement_gath = Transition(label='Requirement Gather')
module_design    = Transition(label='Module Design')
supplier_vet     = Transition(label='Supplier Vetting')
component_ord    = Transition(label='Component Order')
prototype_build  = Transition(label='Prototype Build')
field_testing    = Transition(label='Field Testing')
test_analysis    = Transition(label='Test Analysis')
software_setup   = Transition(label='Software Setup')
data_integrate   = Transition(label='Data Integration')
pilot_train      = Transition(label='Pilot Train')
compliance_check = Transition(label='Compliance Check')
fleet_deploy     = Transition(label='Fleet Deploy')
remote_monitor   = Transition(label='Remote Monitor')
maintenance_plan = Transition(label='Maintenance Plan')
performance_tune = Transition(label='Performance Tune')

# Post-deployment loop: monitor then (maintenance + performance) then repeat or exit
post_tasks = StrictPartialOrder(nodes=[maintenance_plan, performance_tune])
# no edges => maintenance_plan and performance_tune run concurrently
post_deploy_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[remote_monitor, post_tasks]
)

# Pre-deployment parallel tasks before deployment
pre_deploy_parallel = StrictPartialOrder(nodes=[pilot_train, compliance_check])
# no edges => pilot_train and compliance_check run concurrently

# Build the root partial order
root = StrictPartialOrder(
    nodes=[
        client_meet, requirement_gath,
        module_design, supplier_vet,
        component_ord, prototype_build,
        field_testing, test_analysis,
        software_setup, data_integrate,
        pre_deploy_parallel, fleet_deploy,
        post_deploy_loop
    ]
)

# Sequence edges
root.order.add_edge(client_meet,      requirement_gath)
root.order.add_edge(requirement_gath, module_design)
root.order.add_edge(module_design,    supplier_vet)
root.order.add_edge(supplier_vet,     component_ord)
root.order.add_edge(component_ord,    prototype_build)
root.order.add_edge(prototype_build,  field_testing)
root.order.add_edge(field_testing,    test_analysis)
root.order.add_edge(test_analysis,    software_setup)
root.order.add_edge(software_setup,   data_integrate)

# Connect data_integrate to the parallel pilot_train/compliance_check
root.order.add_edge(data_integrate, pre_deploy_parallel)
# After both parallel tasks, deploy the fleet
root.order.add_edge(pre_deploy_parallel, fleet_deploy)

# After deployment, start the monitoring loop
root.order.add_edge(fleet_deploy, post_deploy_loop)