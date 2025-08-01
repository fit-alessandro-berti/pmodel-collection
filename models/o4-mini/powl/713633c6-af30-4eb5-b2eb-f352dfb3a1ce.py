# Generated from: 713633c6-af30-4eb5-b2eb-f352dfb3a1ce.json
# Description: This process involves leasing customized drones to corporate clients for specific operational needs such as agricultural monitoring, infrastructure inspection, or event coverage. It includes client consultation to define requirements, drone customization with specialized sensors, regulatory compliance checks, fleet scheduling, pilot training, live mission support, data collection and analysis, maintenance scheduling, and feedback integration for continuous product improvement. The process ensures tailored drone solutions are delivered efficiently while managing complex logistics and regulatory environments to maximize client satisfaction and operational safety.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
client_consult    = Transition(label='Client Consult')
needs_assess      = Transition(label='Needs Assess')
drone_design      = Transition(label='Drone Design')
sensor_install    = Transition(label='Sensor Install')
compliance_check  = Transition(label='Compliance Check')
fleet_assign      = Transition(label='Fleet Assign')
pilot_train       = Transition(label='Pilot Train')
mission_plan      = Transition(label='Mission Plan')
live_support      = Transition(label='Live Support')
data_capture      = Transition(label='Data Capture')
data_analyze      = Transition(label='Data Analyze')
maintenance_set   = Transition(label='Maintenance Set')
feedback_collect  = Transition(label='Feedback Collect')
update_fleet      = Transition(label='Update Fleet')
billing_process   = Transition(label='Billing Process')
contract_close    = Transition(label='Contract Close')

# Define the mission body (sequence of activities during each mission)
mission_body = StrictPartialOrder(nodes=[
    live_support,
    data_capture,
    data_analyze,
    maintenance_set,
    feedback_collect
])
mission_body.order.add_edge(live_support,   data_capture)
mission_body.order.add_edge(data_capture,    data_analyze)
mission_body.order.add_edge(data_analyze,    maintenance_set)
mission_body.order.add_edge(maintenance_set, feedback_collect)

# Define a loop: execute 'Mission Plan' first, then either exit or perform the mission body and re-plan
mission_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[mission_plan, mission_body]
)

# Build the overall process partial order
root = StrictPartialOrder(nodes=[
    client_consult,
    needs_assess,
    drone_design,
    sensor_install,
    compliance_check,
    fleet_assign,
    pilot_train,
    mission_loop,
    update_fleet,
    billing_process,
    contract_close
])
root.order.add_edge(client_consult,   needs_assess)
root.order.add_edge(needs_assess,     drone_design)
root.order.add_edge(drone_design,     sensor_install)
root.order.add_edge(sensor_install,   compliance_check)
root.order.add_edge(compliance_check, fleet_assign)
root.order.add_edge(fleet_assign,     pilot_train)
root.order.add_edge(pilot_train,      mission_loop)
root.order.add_edge(mission_loop,     update_fleet)
root.order.add_edge(update_fleet,     billing_process)
root.order.add_edge(billing_process,  contract_close)