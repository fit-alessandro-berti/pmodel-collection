# Generated from: fbdd944e-6833-49ff-8984-e79cd8af7f81.json
# Description: This process manages the leasing of a fleet of autonomous drones to clients for various industrial applications such as surveying, delivery, and inspection. It involves client onboarding, drone customization, route programming, regulatory compliance checks, real-time monitoring setup, insurance verification, maintenance scheduling, and periodic performance reporting. The process also includes dynamic pricing adjustments based on drone usage data, incident management, and contract renewal negotiations, ensuring seamless operation and client satisfaction across multiple geographic regions with varying legal requirements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Client_Onboard = Transition(label='Client Onboard')
Needs_Assess = Transition(label='Needs Assess')
Drone_Config = Transition(label='Drone Config')
Route_Program = Transition(label='Route Program')
Compliance_Check = Transition(label='Compliance Check')
Insurance_Verify = Transition(label='Insurance Verify')
Lease_Contract = Transition(label='Lease Contract')
Fleet_Deploy = Transition(label='Fleet Deploy')
Monitor_Setup = Transition(label='Monitor Setup')
Usage_Track = Transition(label='Usage Track')
Maintenance_Plan = Transition(label='Maintenance Plan')
Incident_Manage = Transition(label='Incident Manage')
Billing_Process = Transition(label='Billing Process')
Performance_Report = Transition(label='Performance Report')
Contract_Renew = Transition(label='Contract Renew')
Price_Adjust = Transition(label='Price Adjust')
Feedback_Collect = Transition(label='Feedback Collect')

# Model dynamic pricing adjustment as a loop:
# Loop body B=Price_Adjust then A=Usage_Track, representing repeated usage tracking then price adjusting
dynamic_pricing_loop = OperatorPOWL(operator=Operator.LOOP, children=[Usage_Track, Price_Adjust])

# Incident management can happen anytime after deployment and usage tracking:
# Model the potential concurrent incident management and billing process happening after deployment
incident_billing_choice = OperatorPOWL(operator=Operator.XOR, children=[Incident_Manage, Billing_Process])

# Contract renewal and feedback collection are optional and can occur after billing and periodic reporting,
# model as choice between contract renewal and feedback collection
renew_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[Contract_Renew, Feedback_Collect])

# Performance reporting is periodic and occurs after maintenance and incident management
# So after Maintenance_Plan and incident/billing choice, Performance_Report is done
# Maintenance can occur repeatedly - model maintenance scheduling as a loop with maintenance plan and incident management:
maintenance_incident_loop = OperatorPOWL(operator=Operator.LOOP, children=[Maintenance_Plan, Incident_Manage])

# Client onboarding and needs assessment are sequential start activities
# Followed by drone configuration, route programming, and compliance and insurance checks (all sequential):
setup_order = StrictPartialOrder(nodes=[
    Client_Onboard, Needs_Assess, Drone_Config, Route_Program, Compliance_Check, Insurance_Verify
])
setup_order.order.add_edge(Client_Onboard, Needs_Assess)
setup_order.order.add_edge(Needs_Assess, Drone_Config)
setup_order.order.add_edge(Drone_Config, Route_Program)
setup_order.order.add_edge(Route_Program, Compliance_Check)
setup_order.order.add_edge(Compliance_Check, Insurance_Verify)

# After insurance verify, lease contract, fleet deploy, and monitor setup sequentially
post_insurance_order = StrictPartialOrder(nodes=[
    Lease_Contract, Fleet_Deploy, Monitor_Setup
])
post_insurance_order.order.add_edge(Lease_Contract, Fleet_Deploy)
post_insurance_order.order.add_edge(Fleet_Deploy, Monitor_Setup)

# Combine insurance verify to lease contract sequence
between_setup_and_post = StrictPartialOrder(nodes=[setup_order, post_insurance_order])
between_setup_and_post.order.add_edge(setup_order, post_insurance_order)

# After monitor setup:
# dynamic pricing loop, maintenance and incident loop, incident or billing choice (modeled concurrent),
# performance report, and then contract renewal or feedback choice

after_monitor_nodes = [
    dynamic_pricing_loop,
    maintenance_incident_loop,
    incident_billing_choice,
    Performance_Report,
    renew_feedback_choice
]

after_monitor = StrictPartialOrder(nodes=after_monitor_nodes)
# Order constraints:
# dynamic pricing loop, maintenance loop, and incident/billing can be concurrent, no edges enforced
# But all these must finish before Performance_Report
after_monitor.order.add_edge(dynamic_pricing_loop, Performance_Report)
after_monitor.order.add_edge(maintenance_incident_loop, Performance_Report)
after_monitor.order.add_edge(incident_billing_choice, Performance_Report)
# Performance_Report precedes renew_feedback_choice
after_monitor.order.add_edge(Performance_Report, renew_feedback_choice)

# Compose full model
root = StrictPartialOrder(nodes=[
    setup_order,
    post_insurance_order,
    after_monitor
])
# Link setup_order to post_insurance_order
root.order.add_edge(setup_order, post_insurance_order)
# Link post_insurance_order to after_monitor
root.order.add_edge(post_insurance_order, after_monitor)