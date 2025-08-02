# Generated from: 8721b712-621a-4c4b-a7d5-5069d0fdba35.json
# Description: This process involves coordinating a network of urban residents to collaboratively cultivate and maintain micro-farms on underutilized city spaces. It starts with site identification and community onboarding, followed by soil testing and crop selection based on local climate data. Participants schedule planting and watering shifts through a digital platform, while periodic workshops ensure knowledge sharing on sustainable techniques. Harvesting is coordinated to optimize distribution via local markets and food banks. The process integrates real-time sensor data for automated irrigation and pest control alerts, fostering a resilient, community-driven urban agriculture ecosystem that enhances food security and social cohesion in densely populated areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_scan = Transition(label='Site Scan')
community_join = Transition(label='Community Join')

soil_check = Transition(label='Soil Check')
crop_plan = Transition(label='Crop Plan')

schedule_setup = Transition(label='Schedule Setup')
water_shift = Transition(label='Water Shift')

workshop_hold = Transition(label='Workshop Hold')

sensor_install = Transition(label='Sensor Install')
irrigation_alert = Transition(label='Irrigation Alert')
pest_monitor = Transition(label='Pest Monitor')

harvest_plan = Transition(label='Harvest Plan')
market_link = Transition(label='Market Link')
food_bank = Transition(label='Food Bank')

data_sync = Transition(label='Data Sync')
feedback_collect = Transition(label='Feedback Collect')

# 1) Initial partial order: Site Scan --> Community Join
init = StrictPartialOrder(nodes=[site_scan, community_join])
init.order.add_edge(site_scan, community_join)

# 2) Soil Check and Crop Plan in partial order (soil_check then crop_plan)
soil_crop = StrictPartialOrder(nodes=[soil_check, crop_plan])
soil_crop.order.add_edge(soil_check, crop_plan)

# Sequence: init --> soil_crop
front_section = StrictPartialOrder(nodes=[init, soil_crop])
front_section.order.add_edge(init, soil_crop)

# 3) Scheduling and Water Shift concurrent: Schedule Setup and Water Shift
# But schedule_setup must happen before water_shift (people schedule shifts first)
sched_water = StrictPartialOrder(nodes=[schedule_setup, water_shift])
sched_water.order.add_edge(schedule_setup, water_shift)

# 4) Workshops concurrent with scheduling/watering
# So combine sched_water and workshop_hold concurrently (no order)
sched_workshop = StrictPartialOrder(nodes=[sched_water, workshop_hold])

# 5) Sensor Install leads to Irrigation Alert and Pest Monitor concurrent
sensor_section = StrictPartialOrder(nodes=[sensor_install, irrigation_alert, pest_monitor])
sensor_section.order.add_edge(sensor_install, irrigation_alert)
sensor_section.order.add_edge(sensor_install, pest_monitor)

# 6) Harvest Plan followed by Market Link and Food Bank concurrent
# Market Link and Food Bank concurrent after Harvest Plan
harvest_section = StrictPartialOrder(nodes=[harvest_plan, market_link, food_bank])
harvest_section.order.add_edge(harvest_plan, market_link)
harvest_section.order.add_edge(harvest_plan, food_bank)

# 7) Data Sync and Feedback Collect concurrent after harvest_section and sensor_section
post_harvest = StrictPartialOrder(nodes=[data_sync, feedback_collect])

# Combine harvest_section and sensor_section concurrently
harvest_sensor = StrictPartialOrder(nodes=[harvest_section, sensor_section])

# Combine post harvest data sync and feedback collect with harvest_sensor concurrently
post_harvest_all = StrictPartialOrder(nodes=[harvest_sensor, post_harvest])

# Now build the full process:
# front_section --> sched_workshop --> post_harvest_all

temp1 = StrictPartialOrder(nodes=[front_section, sched_workshop])
temp1.order.add_edge(front_section, sched_workshop)

root = StrictPartialOrder(nodes=[temp1, post_harvest_all])
root.order.add_edge(temp1, post_harvest_all)