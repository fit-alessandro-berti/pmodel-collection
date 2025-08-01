# Generated from: 45dbb670-ca49-4ca7-a2df-7713534cc64d.json
# Description: This process outlines the comprehensive lifecycle management of an urban vertical farm that integrates advanced hydroponics, AI-driven climate control, and automated harvesting systems. Starting from seed selection based on market demand forecasts, the process includes nutrient mix optimization, multi-layered crop monitoring via IoT sensors, pest anomaly detection through machine learning, and dynamic light spectrum adjustments. It further encompasses automated pruning, yield prediction analytics, and adaptive packaging aligned with sustainability standards. The process concludes with real-time distribution logistics coordination and post-harvest nutrient recycling, ensuring minimal waste and maximized resource efficiency in dense city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
demand_forecast = Transition(label='Demand Forecast')
seed_select      = Transition(label='Seed Select')
nutrient_mix     = Transition(label='Nutrient Mix')
climate_adjust   = Transition(label='Climate Adjust')
sensor_monitor   = Transition(label='Sensor Monitor')
pest_detect      = Transition(label='Pest Detect')
light_control    = Transition(label='Light Control')
prune_plants     = Transition(label='Prune Plants')
yield_predict    = Transition(label='Yield Predict')
harvest_auto     = Transition(label='Harvest Auto')
package_align    = Transition(label='Package Align')
quality_audit    = Transition(label='Quality Audit')
logistics_plan   = Transition(label='Logistics Plan')
waste_recycle    = Transition(label='Waste Recycle')
data_sync        = Transition(label='Data Sync')

# Build the partial order
root = StrictPartialOrder(nodes=[
    demand_forecast, seed_select, nutrient_mix, climate_adjust,
    sensor_monitor, pest_detect, light_control, prune_plants,
    yield_predict, harvest_auto, package_align, quality_audit,
    logistics_plan, waste_recycle, data_sync
])

root.order.add_edge(demand_forecast, seed_select)
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_adjust)
root.order.add_edge(climate_adjust, sensor_monitor)
root.order.add_edge(sensor_monitor, pest_detect)
root.order.add_edge(pest_detect, light_control)
root.order.add_edge(light_control, prune_plants)
root.order.add_edge(prune_plants, yield_predict)
root.order.add_edge(yield_predict, harvest_auto)
root.order.add_edge(harvest_auto, package_align)
root.order.add_edge(package_align, quality_audit)
# After quality audit, logistics planning and waste recycling proceed in parallel
root.order.add_edge(quality_audit, logistics_plan)
root.order.add_edge(quality_audit, waste_recycle)
# Both branches synchronize into data synchronization
root.order.add_edge(logistics_plan, data_sync)
root.order.add_edge(waste_recycle, data_sync)