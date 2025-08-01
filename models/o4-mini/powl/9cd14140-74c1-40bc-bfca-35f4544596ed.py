# Generated from: 9cd14140-74c1-40bc-bfca-35f4544596ed.json
# Description: This process describes the comprehensive operational cycle of an urban vertical farm integrating IoT sensors, AI-driven nutrient management, and automated harvesting. Starting from seed selection based on real-time climate data, the farm adjusts lighting, humidity, and irrigation through predictive analytics. Concurrently, waste organic matter is converted via bio-digesters to generate energy for internal use. Employees coordinate maintenance drones for pest control and monitor crop health via augmented reality interfaces. Finally, harvested produce undergoes automated quality sorting and packaging before real-time distribution scheduling to local markets, ensuring minimal waste and maximum freshness in a fully sustainable urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
seed_select    = Transition(label='Seed Select')
climate_scan   = Transition(label='Climate Scan')
sensor_sync    = Transition(label='Sensor Sync')
data_analyze   = Transition(label='Data Analyze')
light_adjust   = Transition(label='Light Adjust')
irrigation_set = Transition(label='Irrigation Set')
nutrient_mix   = Transition(label='Nutrient Mix')
waste_digest   = Transition(label='Waste Digest')
energy_store   = Transition(label='Energy Store')
drone_deploy   = Transition(label='Drone Deploy')
pest_control   = Transition(label='Pest Control')
crop_monitor   = Transition(label='Crop Monitor')
harvest_auto   = Transition(label='Harvest Auto')
quality_sort   = Transition(label='Quality Sort')
package_item   = Transition(label='Package Item')
dispatch_plan  = Transition(label='Dispatch Plan')
market_link    = Transition(label='Market Link')

# Build the partial order
root = StrictPartialOrder(nodes=[
    seed_select, climate_scan, sensor_sync, data_analyze,
    light_adjust, irrigation_set, nutrient_mix,
    waste_digest, energy_store,
    drone_deploy, pest_control, crop_monitor,
    harvest_auto, quality_sort, package_item,
    dispatch_plan, market_link
])

# Sequence: Seed Select -> Climate Scan -> Sensor Sync -> Data Analyze
root.order.add_edge(seed_select, climate_scan)
root.order.add_edge(climate_scan, sensor_sync)
root.order.add_edge(sensor_sync, data_analyze)

# After Data Analyze: concurrent adjustments
root.order.add_edge(data_analyze, light_adjust)
root.order.add_edge(data_analyze, irrigation_set)
root.order.add_edge(data_analyze, nutrient_mix)

# Concurrently after Climate Scan: waste conversion branch
root.order.add_edge(climate_scan, waste_digest)
root.order.add_edge(waste_digest, energy_store)

# Drone / pest-control branch
root.order.add_edge(data_analyze, drone_deploy)
root.order.add_edge(drone_deploy, pest_control)

# Crop monitoring branch
root.order.add_edge(sensor_sync, crop_monitor)

# Harvest can start only after adjustments, pest control, and monitoring
for predecessor in [light_adjust, irrigation_set, nutrient_mix, pest_control, crop_monitor]:
    root.order.add_edge(predecessor, harvest_auto)

# Final linear chain: Harvest -> Quality Sort -> Package -> Dispatch -> Market
root.order.add_edge(harvest_auto, quality_sort)
root.order.add_edge(quality_sort, package_item)
root.order.add_edge(package_item, dispatch_plan)
root.order.add_edge(dispatch_plan, market_link)