# Generated from: 897a9a5b-a555-4d30-8848-9e425f11d63a.json
# Description: This process describes the complex operational cycle of an urban vertical farming system integrating IoT sensors, AI-driven environmental controls, and automated nutrient delivery. It begins with seed selection based on seasonal data, followed by precision planting in modular trays. Continuous monitoring adjusts lighting, humidity, and temperature to optimize growth. Concurrently, water recycling and pest management systems operate autonomously. Harvesting is synchronized with market demand predictions using machine learning. Post-harvest, produce undergoes quality sorting and packaging in a sterile environment. Finally, logistics scheduling ensures timely distribution to urban retailers while maintaining freshness and minimizing waste through dynamic routing and inventory management. This atypical yet realistic process blends agriculture, technology, and supply chain coordination uniquely tailored for metropolitan settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
seed_select      = Transition(label='Seed Select')
tray_setup       = Transition(label='Tray Setup')
planting_start   = Transition(label='Planting Start')
sensor_deploy    = Transition(label='Sensor Deploy')
env_monitor      = Transition(label='Env Monitor')
light_adjust     = Transition(label='Light Adjust')
humidity_control = Transition(label='Humidity Control')
temp_regulate    = Transition(label='Temp Regulate')
nutrient_feed    = Transition(label='Nutrient Feed')
water_recycle    = Transition(label='Water Recycle')
pest_scan        = Transition(label='Pest Scan')
growth_analyze   = Transition(label='Growth Analyze')
harvest_sync     = Transition(label='Harvest Sync')
quality_sort     = Transition(label='Quality Sort')
package_produce  = Transition(label='Package Produce')
route_plan       = Transition(label='Route Plan')
inventory_update = Transition(label='Inventory Update')
delivery_track   = Transition(label='Delivery Track')

# Build the partial order with all nodes
root = StrictPartialOrder(nodes=[
    seed_select,
    tray_setup,
    planting_start,
    sensor_deploy,
    env_monitor,
    light_adjust,
    humidity_control,
    temp_regulate,
    nutrient_feed,
    water_recycle,
    pest_scan,
    growth_analyze,
    harvest_sync,
    quality_sort,
    package_produce,
    route_plan,
    inventory_update,
    delivery_track
])

# Sequence: Seed Select -> Tray Setup -> Planting Start -> Sensor Deploy
root.order.add_edge(seed_select, tray_setup)
root.order.add_edge(tray_setup, planting_start)
root.order.add_edge(planting_start, sensor_deploy)

# After Sensor Deploy, three branches start concurrently:
#  1) Env Monitor -> Light/Humidity/Temp -> Nutrient Feed
#  2) Water Recycle
#  3) Pest Scan
root.order.add_edge(sensor_deploy, env_monitor)
root.order.add_edge(sensor_deploy, water_recycle)
root.order.add_edge(sensor_deploy, pest_scan)

# Env monitor sub‐flow
root.order.add_edge(env_monitor, light_adjust)
root.order.add_edge(env_monitor, humidity_control)
root.order.add_edge(env_monitor, temp_regulate)

# Join adjustments into nutrient feed
root.order.add_edge(light_adjust, nutrient_feed)
root.order.add_edge(humidity_control, nutrient_feed)
root.order.add_edge(temp_regulate, nutrient_feed)

# After all three branches complete -> Growth Analyze
root.order.add_edge(nutrient_feed, growth_analyze)
root.order.add_edge(water_recycle, growth_analyze)
root.order.add_edge(pest_scan, growth_analyze)

# Continue sequence to Harvest, Sort, Package
root.order.add_edge(growth_analyze, harvest_sync)
root.order.add_edge(harvest_sync, quality_sort)
root.order.add_edge(quality_sort, package_produce)

# Packaging -> two parallel logistics activities
root.order.add_edge(package_produce, route_plan)
root.order.add_edge(package_produce, inventory_update)

# Both logistics join into final delivery tracking
root.order.add_edge(route_plan, delivery_track)
root.order.add_edge(inventory_update, delivery_track)