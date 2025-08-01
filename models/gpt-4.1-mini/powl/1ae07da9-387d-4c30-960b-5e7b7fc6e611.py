# Generated from: 1ae07da9-387d-4c30-960b-5e7b7fc6e611.json
# Description: This process outlines the setup and operational preparation for an urban drone delivery system integrating regulatory compliance, route optimization, drone calibration, and customer engagement. It involves coordinating with local authorities, performing environmental impact assessments, configuring autonomous flight parameters, and establishing emergency protocols. The process ensures seamless delivery of packages in densely populated areas while maintaining safety and efficiency through continuous monitoring and adaptive scheduling. It also includes community awareness campaigns and feedback loops to refine service quality and address urban logistic challenges in real time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
RegulatoryCheck = Transition(label='Regulatory Check')
RouteSurvey = Transition(label='Route Survey')
DroneCalibration = Transition(label='Drone Calibration')
PayloadSecuring = Transition(label='Payload Securing')
FlightSimulation = Transition(label='Flight Simulation')
EmergencySetup = Transition(label='Emergency Setup')
EnvironmentalAudit = Transition(label='Environmental Audit')
SignalTesting = Transition(label='Signal Testing')
CommunityBrief = Transition(label='Community Brief')
ScheduleSync = Transition(label='Schedule Sync')
BatteryCharging = Transition(label='Battery Charging')
AutonomyConfig = Transition(label='Autonomy Config')
TestFlight = Transition(label='Test Flight')
DataLogging = Transition(label='Data Logging')
CustomerNotify = Transition(label='Customer Notify')
FeedbackReview = Transition(label='Feedback Review')
MaintenancePlan = Transition(label='Maintenance Plan')

# Define subprocesses following the description:

# 1. Regulatory check and environmental audit + route survey and signal testing in partial order:
# RegulatoryCheck and EnvironmentalAudit may be concurrent but must precede RouteSurvey and SignalTesting.
reg_env_po = StrictPartialOrder(nodes=[RegulatoryCheck, EnvironmentalAudit, RouteSurvey, SignalTesting])
reg_env_po.order.add_edge(RegulatoryCheck, RouteSurvey)
reg_env_po.order.add_edge(EnvironmentalAudit, SignalTesting)

# 2. Drone preparation: calibration, payload securing, battery charging, autonomy config,
# flight simulation, test flight, data logging, and maintenance plan.
# We'll order calibration -> autonomy config -> payload securing, battery charging concurrent,
# then flight simulation, test flight, data logging in order, followed by maintenance plan.

drone_prep_po = StrictPartialOrder(nodes=[
    DroneCalibration, AutonomyConfig, PayloadSecuring, BatteryCharging,
    FlightSimulation, TestFlight, DataLogging, MaintenancePlan
])
# Calibration -> Autonomy Config
drone_prep_po.order.add_edge(DroneCalibration, AutonomyConfig)
# Autonomy Config -> Payload Securing
drone_prep_po.order.add_edge(AutonomyConfig, PayloadSecuring)
# Autonomy Config -> Battery Charging (Payload Securing and Battery Charging concurrent after Autonomy Config)
drone_prep_po.order.add_edge(AutonomyConfig, BatteryCharging)
# Payload Securing -> Flight Simulation
drone_prep_po.order.add_edge(PayloadSecuring, FlightSimulation)
# Battery Charging -> Flight Simulation
drone_prep_po.order.add_edge(BatteryCharging, FlightSimulation)
# Flight Simulation -> Test Flight
drone_prep_po.order.add_edge(FlightSimulation, TestFlight)
# Test Flight -> Data Logging
drone_prep_po.order.add_edge(TestFlight, DataLogging)
# Data Logging -> Maintenance Plan
drone_prep_po.order.add_edge(DataLogging, MaintenancePlan)

# 3. Emergency setup stands separately but must be done before or concurrently with operational steps
# We'll put it concurrent with the drone preparation.

# 4. Community engagement: Community Brief then Customer Notify
comm_engagement_po = StrictPartialOrder(nodes=[CommunityBrief, CustomerNotify])
comm_engagement_po.order.add_edge(CommunityBrief, CustomerNotify)

# 5. Schedule sync and Feedback review in a loop to reflect continuous monitoring and adaptive scheduling:
# Loop body: Schedule Sync then Feedback Review -> loop exit or repeat
loop_monitoring = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ScheduleSync, FeedbackReview]
)

# 6. Combine community engagement and monitoring loop by choice - sometimes notify directly, sometimes feedback loop
comm_and_feedback = OperatorPOWL(
    operator=Operator.XOR,
    children=[comm_engagement_po, loop_monitoring]
)

# 7. Top level partial order:
# reg_env_po -> EmergencySetup, drone_prep_po (both start after reg/env checks) concurrent with emergency setup
# After drone prep and emergency setup, community and feedback activities start

top_po_nodes = [reg_env_po, EmergencySetup, drone_prep_po, comm_and_feedback]

root = StrictPartialOrder(nodes=top_po_nodes)

# reg_env_po finishes before EmergencySetup and drone_prep_po start
root.order.add_edge(reg_env_po, EmergencySetup)
root.order.add_edge(reg_env_po, drone_prep_po)

# EmergencySetup and drone_prep_po complete before comm_and_feedback start
root.order.add_edge(EmergencySetup, comm_and_feedback)
root.order.add_edge(drone_prep_po, comm_and_feedback)