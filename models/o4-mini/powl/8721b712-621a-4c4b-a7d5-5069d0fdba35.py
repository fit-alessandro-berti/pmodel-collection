# Generated from: 8721b712-621a-4c4b-a7d5-5069d0fdba35.json
# Description: This process involves coordinating a network of urban residents to collaboratively cultivate and maintain micro-farms on underutilized city spaces. It starts with site identification and community onboarding, followed by soil testing and crop selection based on local climate data. Participants schedule planting and watering shifts through a digital platform, while periodic workshops ensure knowledge sharing on sustainable techniques. Harvesting is coordinated to optimize distribution via local markets and food banks. The process integrates real-time sensor data for automated irrigation and pest control alerts, fostering a resilient, community-driven urban agriculture ecosystem that enhances food security and social cohesion in densely populated areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_scan       = Transition(label='Site Scan')
community_join  = Transition(label='Community Join')
soil_check      = Transition(label='Soil Check')
crop_plan       = Transition(label='Crop Plan')
schedule_setup  = Transition(label='Schedule Setup')
water_shift     = Transition(label='Water Shift')
workshop_hold   = Transition(label='Workshop Hold')
sensor_install  = Transition(label='Sensor Install')
irrigation_alert= Transition(label='Irrigation Alert')
pest_monitor    = Transition(label='Pest Monitor')
harvest_plan    = Transition(label='Harvest Plan')
market_link     = Transition(label='Market Link')
food_bank       = Transition(label='Food Bank')
data_sync       = Transition(label='Data Sync')
feedback_collect= Transition(label='Feedback Collect')

# Choice between two alert types
alert_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[irrigation_alert, pest_monitor]
)

# Loop for sensor data synchronization and alerting
sensor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_sync, alert_choice]
)

# Periodic workshop with feedback
workshop_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[workshop_hold, feedback_collect]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_scan,
    community_join,
    soil_check,
    crop_plan,
    schedule_setup,
    water_shift,
    sensor_install,
    sensor_loop,
    workshop_loop,
    harvest_plan,
    market_link,
    food_bank
])

# Define the control-flow dependencies
root.order.add_edge(site_scan,      community_join)
root.order.add_edge(community_join, soil_check)
root.order.add_edge(soil_check,     crop_plan)

# After planning: schedule & watering
root.order.add_edge(crop_plan,      schedule_setup)
root.order.add_edge(schedule_setup, water_shift)

# After planning: sensor install and workshop start
root.order.add_edge(crop_plan,      sensor_install)
root.order.add_edge(sensor_install, sensor_loop)

root.order.add_edge(crop_plan,      workshop_loop)

# Harvesting depends on completion of schedule/water, sensor-loop, and workshops
root.order.add_edge(water_shift,    harvest_plan)
root.order.add_edge(sensor_loop,    harvest_plan)
root.order.add_edge(workshop_loop,  harvest_plan)

# Distribution after harvest
root.order.add_edge(harvest_plan,   market_link)
root.order.add_edge(harvest_plan,   food_bank)