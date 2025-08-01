# Generated from: 1ae07da9-387d-4c30-960b-5e7b7fc6e611.json
# Description: This process outlines the setup and operational preparation for an urban drone delivery system integrating regulatory compliance, route optimization, drone calibration, and customer engagement. It involves coordinating with local authorities, performing environmental impact assessments, configuring autonomous flight parameters, and establishing emergency protocols. The process ensures seamless delivery of packages in densely populated areas while maintaining safety and efficiency through continuous monitoring and adaptive scheduling. It also includes community awareness campaigns and feedback loops to refine service quality and address urban logistic challenges in real time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
reg_check        = Transition(label="Regulatory Check")
route_survey     = Transition(label="Route Survey")
env_audit        = Transition(label="Environmental Audit")
drone_cal        = Transition(label="Drone Calibration")
battery_charging = Transition(label="Battery Charging")
payload_securing = Transition(label="Payload Securing")
autonomy_config  = Transition(label="Autonomy Config")
flight_sim       = Transition(label="Flight Simulation")
signal_testing   = Transition(label="Signal Testing")
emergency_setup  = Transition(label="Emergency Setup")
test_flight      = Transition(label="Test Flight")
community_brief  = Transition(label="Community Brief")
customer_notify  = Transition(label="Customer Notify")
feedback_review  = Transition(label="Feedback Review")
maintenance_plan = Transition(label="Maintenance Plan")

# For the adaptive monitoring & scheduling loop
data_logging   = Transition(label="Data Logging")
schedule_sync  = Transition(label="Schedule Sync")
monitor_loop   = OperatorPOWL(operator=Operator.LOOP, children=[data_logging, schedule_sync])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    reg_check,
    route_survey,
    env_audit,
    drone_cal,
    battery_charging,
    payload_securing,
    autonomy_config,
    flight_sim,
    signal_testing,
    emergency_setup,
    test_flight,
    community_brief,
    customer_notify,
    feedback_review,
    maintenance_plan,
    monitor_loop
])

# Add the control-flow dependencies
o = root.order
o.add_edge(reg_check,     env_audit)
o.add_edge(reg_check,     route_survey)
o.add_edge(env_audit,     autonomy_config)
o.add_edge(route_survey,  drone_cal)
o.add_edge(drone_cal,     battery_charging)
o.add_edge(battery_charging, payload_securing)
o.add_edge(autonomy_config,  flight_sim)
o.add_edge(payload_securing, flight_sim)
o.add_edge(flight_sim,       signal_testing)
o.add_edge(signal_testing,   test_flight)
o.add_edge(drone_cal,        emergency_setup)
o.add_edge(emergency_setup,  test_flight)
o.add_edge(test_flight,      monitor_loop)
o.add_edge(monitor_loop,     customer_notify)
o.add_edge(reg_check,        community_brief)
o.add_edge(route_survey,     community_brief)
o.add_edge(customer_notify,  feedback_review)
o.add_edge(feedback_review,  maintenance_plan)