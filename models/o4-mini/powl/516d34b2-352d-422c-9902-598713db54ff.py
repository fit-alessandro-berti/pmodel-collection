# Generated from: 516d34b2-352d-422c-9902-598713db54ff.json
# Description: This process outlines the deployment of a custom drone fleet for environmental monitoring in remote areas. It involves initial site analysis, drone customization to adapt to varying weather conditions, regulatory compliance checks with local authorities, pilot training on specialized equipment, iterative testing of flight patterns, real-time data integration with satellite feeds, maintenance scheduling based on predictive analytics, emergency response protocols setup, community engagement for awareness, and final deployment with continuous performance monitoring and adaptive mission updates. The process ensures optimized data collection while maintaining safety and regulatory standards in complex terrains.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_analysis       = Transition(label='Site Analysis')
drone_customization = Transition(label='Drone Customization')
regulatory_check    = Transition(label='Regulatory Check')
pilot_training      = Transition(label='Pilot Training')
flight_testing      = Transition(label='Flight Testing')
data_integration    = Transition(label='Data Integration')
maintenance_plan    = Transition(label='Maintenance Plan')
emergency_setup     = Transition(label='Emergency Setup')
community_outreach  = Transition(label='Community Outreach')
mission_planning    = Transition(label='Mission Planning')
performance_review  = Transition(label='Performance Review')
pattern_adjust      = Transition(label='Pattern Adjustment')
battery_swap        = Transition(label='Battery Swap')
signal_cal          = Transition(label='Signal Calibration')
report_generation   = Transition(label='Report Generation')

# Loop 1: iterative flight testing with adjustments
redo_adjustments = StrictPartialOrder(
    nodes=[pattern_adjust, battery_swap, signal_cal]
)
redo_adjustments.order.add_edge(pattern_adjust, battery_swap)
redo_adjustments.order.add_edge(battery_swap, signal_cal)

loop_flight = OperatorPOWL(
    operator=Operator.LOOP,
    children=[flight_testing, redo_adjustments]
)

# Loop 2: continuous performance review and mission planning
loop_mission = OperatorPOWL(
    operator=Operator.LOOP,
    children=[performance_review, mission_planning]
)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_analysis,
        drone_customization,
        regulatory_check,
        pilot_training,
        loop_flight,
        data_integration,
        maintenance_plan,
        emergency_setup,
        community_outreach,
        loop_mission,
        report_generation
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(site_analysis,       drone_customization)
root.order.add_edge(site_analysis,       regulatory_check)
root.order.add_edge(drone_customization, pilot_training)
root.order.add_edge(regulatory_check,    pilot_training)
root.order.add_edge(pilot_training,      loop_flight)
root.order.add_edge(loop_flight,         data_integration)
# After data integration, schedule maintenance, emergency setup, and outreach in parallel
root.order.add_edge(data_integration, maintenance_plan)
root.order.add_edge(data_integration, emergency_setup)
root.order.add_edge(data_integration, community_outreach)
# Once those three are done, start the performance‐review loop
root.order.add_edge(maintenance_plan,   loop_mission)
root.order.add_edge(emergency_setup,    loop_mission)
root.order.add_edge(community_outreach, loop_mission)
# After the mission loop, generate the final report
root.order.add_edge(loop_mission, report_generation)