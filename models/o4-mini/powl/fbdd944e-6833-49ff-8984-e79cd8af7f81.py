# Generated from: fbdd944e-6833-49ff-8984-e79cd8af7f81.json
# Description: This process manages the leasing of a fleet of autonomous drones to clients for various industrial applications such as surveying, delivery, and inspection. It involves client onboarding, drone customization, route programming, regulatory compliance checks, real-time monitoring setup, insurance verification, maintenance scheduling, and periodic performance reporting. The process also includes dynamic pricing adjustments based on drone usage data, incident management, and contract renewal negotiations, ensuring seamless operation and client satisfaction across multiple geographic regions with varying legal requirements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
client_onboard     = Transition(label='Client Onboard')
needs_assess       = Transition(label='Needs Assess')
drone_config       = Transition(label='Drone Config')
route_program      = Transition(label='Route Program')
compliance_check   = Transition(label='Compliance Check')
insurance_verify   = Transition(label='Insurance Verify')
lease_contract     = Transition(label='Lease Contract')
fleet_deploy       = Transition(label='Fleet Deploy')
monitor_setup      = Transition(label='Monitor Setup')
usage_track        = Transition(label='Usage Track')
performance_report = Transition(label='Performance Report')
price_adjust       = Transition(label='Price Adjust')
billing_process    = Transition(label='Billing Process')
incident_manage    = Transition(label='Incident Manage')
maintenance_plan   = Transition(label='Maintenance Plan')
contract_renew     = Transition(label='Contract Renew')
feedback_collect   = Transition(label='Feedback Collect')

# Define the cyclic monitoring & maintenance loop
cycle = StrictPartialOrder(
    nodes=[
        usage_track,
        performance_report,
        price_adjust,
        billing_process,
        incident_manage,
        maintenance_plan
    ]
)
# sequential flow within each cycle
cycle.order.add_edge(usage_track, performance_report)
cycle.order.add_edge(performance_report, price_adjust)
cycle.order.add_edge(price_adjust, billing_process)
# incident management and maintenance can occur concurrently with the billing/usage/report sequence
# (we leave them unconnected to represent concurrency)

# define the loop operator: do 'cycle', then either exit (skip) or repeat
skip = SilentTransition()
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycle, skip]
)

# assemble the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        client_onboard,
        needs_assess,
        drone_config,
        route_program,
        compliance_check,
        insurance_verify,
        lease_contract,
        fleet_deploy,
        monitor_setup,
        monitor_loop,
        contract_renew,
        feedback_collect
    ]
)

# add the main sequential dependencies
root.order.add_edge(client_onboard,     needs_assess)
root.order.add_edge(needs_assess,       drone_config)
root.order.add_edge(drone_config,       route_program)
root.order.add_edge(route_program,      compliance_check)
root.order.add_edge(compliance_check,   insurance_verify)
root.order.add_edge(insurance_verify,   lease_contract)
root.order.add_edge(lease_contract,     fleet_deploy)
root.order.add_edge(fleet_deploy,       monitor_setup)
root.order.add_edge(monitor_setup,      monitor_loop)
root.order.add_edge(monitor_loop,       contract_renew)
root.order.add_edge(contract_renew,     feedback_collect)