# Generated from: fbd0a280-a097-4b20-bd85-a45e775b26c9.json
# Description: This process outlines the complex operational cycle of an urban vertical farming enterprise that integrates advanced hydroponics, AI-driven climate control, and community engagement. The workflow begins with seed selection and germination optimization, followed by nutrient formulation and precise water management. Real-time monitoring through IoT sensors enables adaptive lighting and airflow adjustments. Concurrently, crop health assessments using multispectral imaging guide pest control and disease prevention strategies without chemicals. Harvesting is carefully timed to maximize yield quality, after which produce undergoes immediate cold storage and packaging within the facility. Finally, logistics coordination ensures same-day delivery to local markets and subscription customers, while feedback loops from sales and customer input drive continuous process improvements and sustainability initiatives.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Selection = Transition(label='Seed Selection')
Germination_Setup = Transition(label='Germination Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Water_Control = Transition(label='Water Control')
Climate_Adjust = Transition(label='Climate Adjust')
Sensor_Monitor = Transition(label='Sensor Monitor')
Lighting_Tune = Transition(label='Lighting Tune')
Airflow_Manage = Transition(label='Airflow Manage')
Health_Scan = Transition(label='Health Scan')
Pest_Control = Transition(label='Pest Control')
Harvest_Timing = Transition(label='Harvest Timing')
Cold_Storage = Transition(label='Cold Storage')
Package_Prep = Transition(label='Package Prep')
Delivery_Plan = Transition(label='Delivery Plan')
Feedback_Loop = Transition(label='Feedback Loop')

# Concurrent lighting and airflow tuning, after sensor monitoring
lighting_airflow = StrictPartialOrder(nodes=[Lighting_Tune, Airflow_Manage])

# Pest control depends on health scan
# Health scan and pest control run concurrently with harvesting preparation (timing),
# but harvesting comes after pest control

# Create partial order for post-monitoring: Health scan -> Pest control -> Harvest Timing
post_monitoring = StrictPartialOrder(
    nodes=[Health_Scan, Pest_Control, Harvest_Timing]
)
post_monitoring.order.add_edge(Health_Scan, Pest_Control)
post_monitoring.order.add_edge(Pest_Control, Harvest_Timing)

# Cold storage and package prep are concurrent after harvest timing
storage_pack = StrictPartialOrder(nodes=[Cold_Storage, Package_Prep])

# Delivery plan and feedback loop concurrent after packaging
delivery_feedback = StrictPartialOrder(nodes=[Delivery_Plan, Feedback_Loop])

# Build sensor monitoring branch: Sensor monitor -> (Lighting + Airflow concurrent)
sensor_branch = StrictPartialOrder(nodes=[Sensor_Monitor, lighting_airflow])
sensor_branch.order.add_edge(Sensor_Monitor, lighting_airflow)

# Nutrient mix and water control run sequentially (formulation and precise control)
nutrient_water = StrictPartialOrder(nodes=[Nutrient_Mix, Water_Control])
nutrient_water.order.add_edge(Nutrient_Mix, Water_Control)

# Start: Seed selection -> Germination setup -> nutrient + water
start_seq = StrictPartialOrder(nodes=[Seed_Selection, Germination_Setup, nutrient_water])
start_seq.order.add_edge(Seed_Selection, Germination_Setup)
start_seq.order.add_edge(Germination_Setup, nutrient_water)

# Climate adjust depends on nutrient and water control
# After nutrient_water -> Climate Adjust
nw_climate = StrictPartialOrder(nodes=[nutrient_water, Climate_Adjust])
nw_climate.order.add_edge(nutrient_water, Climate_Adjust)

# After Climate Adjust comes Sensor monitoring branch
climate_sensor = StrictPartialOrder(nodes=[Climate_Adjust, sensor_branch])
climate_sensor.order.add_edge(Climate_Adjust, sensor_branch)

# Combine monitoring branch and post-monitoring chain
monitor_postmonitor = StrictPartialOrder(nodes=[climate_sensor, post_monitoring])
monitor_postmonitor.order.add_edge(climate_sensor, post_monitoring)

# After Harvest Timing comes storage and packaging
harvest_storagepack = StrictPartialOrder(nodes=[post_monitoring, storage_pack])
harvest_storagepack.order.add_edge(post_monitoring, storage_pack)

# After packaging comes delivery and feedback in parallel
pack_deliveryfeedback = StrictPartialOrder(nodes=[storage_pack, delivery_feedback])
pack_deliveryfeedback.order.add_edge(storage_pack, delivery_feedback)

# Final root partial order from start_seq up to delivery_feedback
root = StrictPartialOrder(
    nodes=[start_seq, climate_sensor, monitor_postmonitor, harvest_storagepack, pack_deliveryfeedback]
)

# add edges connecting the sequence properly:
# Start sequence to climate_sensor is already included because climate_sensor nodes include nutrient_water
# We'll connect start_seq to climate_sensor explicitly:
root.order.add_edge(start_seq, climate_sensor)

# connect climate_sensor to monitor_postmonitor
root.order.add_edge(climate_sensor, monitor_postmonitor)

# connect monitor_postmonitor to harvest_storagepack
root.order.add_edge(monitor_postmonitor, harvest_storagepack)

# connect harvest_storagepack to pack_deliveryfeedback
root.order.add_edge(harvest_storagepack, pack_deliveryfeedback)