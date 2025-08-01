# Generated from: 5061a7d1-c4c0-4e8a-821a-3ef59dc5a38d.json
# Description: This complex business process involves designing and launching a tailored drone delivery solution for specialized clients. It begins with client needs analysis, followed by regulatory compliance checks and custom drone configuration. The process includes route optimization, payload testing, and integration with client logistics systems. Continuous monitoring and adaptive feedback loops ensure delivery efficiency and safety. Post-deployment support and iterative upgrades maintain operational excellence and client satisfaction over time, making the process both innovative and highly specialized.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
client_brief      = Transition(label='Client Brief')
needs_analysis    = Transition(label='Needs Analysis')
regulatory_check  = Transition(label='Regulatory Check')
drone_design      = Transition(label='Drone Design')
component_sourcing= Transition(label='Component Sourcing')
assembly_test     = Transition(label='Assembly Test')
payload_setup     = Transition(label='Payload Setup')
route_mapping     = Transition(label='Route Mapping')
flight_simulation = Transition(label='Flight Simulation')
logistics_sync    = Transition(label='Logistics Sync')
safety_audit      = Transition(label='Safety Audit')
pilot_training    = Transition(label='Pilot Training')
deployment_launch = Transition(label='Deployment Launch')
performance_review= Transition(label='Performance Review')
feedback_loop     = Transition(label='Feedback Loop')
maintenance_plan  = Transition(label='Maintenance Plan')
upgrade_cycle     = Transition(label='Upgrade Cycle')

# Define the post-deployment loop body: Feedback Loop -> Maintenance Plan -> Upgrade Cycle
post_deploy_body = StrictPartialOrder(nodes=[feedback_loop, maintenance_plan, upgrade_cycle])
post_deploy_body.order.add_edge(feedback_loop, maintenance_plan)
post_deploy_body.order.add_edge(maintenance_plan, upgrade_cycle)

# Define the loop: do Performance Review, then choose to exit or execute the body and repeat
post_deploy_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[performance_review, post_deploy_body]
)

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[
    client_brief,
    needs_analysis,
    regulatory_check,
    drone_design,
    component_sourcing,
    assembly_test,
    payload_setup,
    route_mapping,
    flight_simulation,
    logistics_sync,
    safety_audit,
    pilot_training,
    deployment_launch,
    post_deploy_loop
])

# Add the control‐flow ordering
root.order.add_edge(client_brief,       needs_analysis)
root.order.add_edge(needs_analysis,     regulatory_check)
root.order.add_edge(regulatory_check,   drone_design)
root.order.add_edge(drone_design,       component_sourcing)
root.order.add_edge(component_sourcing, assembly_test)
root.order.add_edge(assembly_test,      payload_setup)
root.order.add_edge(payload_setup,      route_mapping)
root.order.add_edge(route_mapping,      flight_simulation)
root.order.add_edge(flight_simulation,  logistics_sync)
root.order.add_edge(logistics_sync,     safety_audit)
root.order.add_edge(safety_audit,       pilot_training)
root.order.add_edge(pilot_training,     deployment_launch)
root.order.add_edge(deployment_launch,  post_deploy_loop)