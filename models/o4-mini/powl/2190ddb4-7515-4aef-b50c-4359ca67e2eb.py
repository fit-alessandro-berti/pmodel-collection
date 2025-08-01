# Generated from: 2190ddb4-7515-4aef-b50c-4359ca67e2eb.json
# Description: This process outlines the complex cycle of managing an urban vertical farm, integrating advanced hydroponics and AI-driven environmental controls. It involves seed selection, nutrient blending, automated planting, continuous monitoring of microclimates, pest detection through computer vision, adaptive lighting adjustments, precision harvesting, and waste recycling. The process ensures optimal crop yield while minimizing water and energy consumption. Additionally, it includes data analytics to forecast demand and adjust production schedules dynamically, combined with logistics coordination for just-in-time delivery to local markets. This atypical business process leverages technology and sustainability principles to revolutionize urban agriculture in confined spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection      = Transition(label='Seed Selection')
nutrient_blend      = Transition(label='Nutrient Blend')
automated_planting  = Transition(label='Automated Planting')
microclimate_scan   = Transition(label='Microclimate Scan')
pest_detection      = Transition(label='Pest Detection')
light_adjustment    = Transition(label='Light Adjustment')
growth_monitoring   = Transition(label='Growth Monitoring')
water_recycling      = Transition(label='Water Recycling')
harvest_planning    = Transition(label='Harvest Planning')
precision_harvest   = Transition(label='Precision Harvest')
waste_processing    = Transition(label='Waste Processing')
yield_forecast      = Transition(label='Yield Forecast')
demand_analysis     = Transition(label='Demand Analysis')
schedule_update     = Transition(label='Schedule Update')
logistics_sync      = Transition(label='Logistics Sync')
market_delivery     = Transition(label='Market Delivery')

# Build the monitoring cycle as a partial order: Scan -> Detect -> Adjust -> Monitor
monitoring_cycle = StrictPartialOrder(nodes=[
    microclimate_scan,
    pest_detection,
    light_adjustment,
    growth_monitoring
])
monitoring_cycle.order.add_edge(microclimate_scan, pest_detection)
monitoring_cycle.order.add_edge(pest_detection, light_adjustment)
monitoring_cycle.order.add_edge(light_adjustment, growth_monitoring)

# Wrap the monitoring cycle in a loop to represent continuous monitoring
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitoring_cycle, monitoring_cycle]
)

# Build the top‐level process as a strict partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    nutrient_blend,
    automated_planting,
    monitoring_loop,
    water_recycling,
    harvest_planning,
    precision_harvest,
    waste_processing,
    yield_forecast,
    demand_analysis,
    schedule_update,
    logistics_sync,
    market_delivery
])

# Define the control‐flow dependencies
root.order.add_edge(seed_selection,     nutrient_blend)
root.order.add_edge(nutrient_blend,     automated_planting)
root.order.add_edge(automated_planting, monitoring_loop)
root.order.add_edge(monitoring_loop,    water_recycling)
root.order.add_edge(water_recycling,    harvest_planning)
root.order.add_edge(harvest_planning,   precision_harvest)
root.order.add_edge(precision_harvest,  waste_processing)

# After waste processing, run analytics in parallel, then update schedule
root.order.add_edge(waste_processing,  yield_forecast)
root.order.add_edge(waste_processing,  demand_analysis)
root.order.add_edge(yield_forecast,    schedule_update)
root.order.add_edge(demand_analysis,   schedule_update)

# Final logistics and delivery
root.order.add_edge(schedule_update,   logistics_sync)
root.order.add_edge(logistics_sync,    market_delivery)