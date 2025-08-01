# Generated from: 551ea399-b140-4310-81eb-64ae9e10994a.json
# Description: This process details the comprehensive cycle of urban vertical farming, integrating IoT-enabled environmental control and AI-driven crop management. Starting from seed selection tailored to microclimate data, it involves automated nutrient mixing, precise hydroponic irrigation, real-time pest detection via drone surveillance, adaptive lighting adjustment based on growth stages, and continual yield forecasting. The cycle concludes with post-harvest quality sorting, packaging optimized for urban logistics, and dynamic market demand analysis to adjust future planting schedules. This atypical process blends advanced technology with sustainable agriculture in constrained urban environments, ensuring maximum resource efficiency and crop output while minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
seed_select      = Transition(label='Seed Select')
climate_analyze  = Transition(label='Climate Analyze')
nutrient_mix     = Transition(label='Nutrient Mix')
irrigation_ctrl  = Transition(label='Irrigation Control')
drone_survey     = Transition(label='Drone Survey')
pest_detect      = Transition(label='Pest Detect')
light_adjust     = Transition(label='Light Adjust')
growth_monitor   = Transition(label='Growth Monitor')
yield_forecast   = Transition(label='Yield Forecast')
harvest_crop     = Transition(label='Harvest Crop')
quality_sort     = Transition(label='Quality Sort')
package_goods    = Transition(label='Package Goods')
logistics_plan   = Transition(label='Logistics Plan')
market_analyze   = Transition(label='Market Analyze')
schedule_update  = Transition(label='Schedule Update')

# Silent transition for loop redo
skip = SilentTransition()

# Build the body of the cycle as a strict partial order
body = StrictPartialOrder(nodes=[
    seed_select,
    climate_analyze,
    nutrient_mix,
    irrigation_ctrl,
    drone_survey,
    pest_detect,
    light_adjust,
    growth_monitor,
    yield_forecast,
    harvest_crop,
    quality_sort,
    package_goods,
    logistics_plan,
    market_analyze,
    schedule_update
])
# Sequential dependencies
body.order.add_edge(seed_select,     climate_analyze)
body.order.add_edge(climate_analyze, nutrient_mix)
body.order.add_edge(nutrient_mix,    irrigation_ctrl)
body.order.add_edge(irrigation_ctrl, drone_survey)
body.order.add_edge(drone_survey,    pest_detect)
body.order.add_edge(pest_detect,     light_adjust)
body.order.add_edge(light_adjust,    growth_monitor)
body.order.add_edge(growth_monitor,  yield_forecast)
body.order.add_edge(yield_forecast,  harvest_crop)
body.order.add_edge(harvest_crop,    quality_sort)
body.order.add_edge(quality_sort,    package_goods)
body.order.add_edge(package_goods,   logistics_plan)
body.order.add_edge(logistics_plan,  market_analyze)
body.order.add_edge(market_analyze,  schedule_update)

# Wrap the whole cycle in a LOOP: execute 'body' repeatedly until exit
root = OperatorPOWL(operator=Operator.LOOP, children=[body, skip])