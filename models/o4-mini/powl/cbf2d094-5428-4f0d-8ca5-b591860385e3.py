# Generated from: cbf2d094-5428-4f0d-8ca5-b591860385e3.json
# Description: This process outlines the comprehensive cycle of an urban vertical farming operation that integrates automated hydroponics with AI-driven crop monitoring to optimize yield in constrained city environments. Starting from seed selection and nutrient calibration, the process includes climate control adjustments, robotic planting, pest bio-control application, and continuous growth analytics. Harvesting is synchronized with demand forecasting to minimize waste, followed by post-harvest sterilization and packaging. Finally, logistics coordination ensures fresh delivery to local markets, while data feedback loops refine future crop cycles for sustainability and efficiency improvements in urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_select      = Transition(label='Seed Select')
nutrient_mix     = Transition(label='Nutrient Mix')
climate_adjust   = Transition(label='Climate Adjust')
planting_robotic = Transition(label='Planting Robotic')
pest_control     = Transition(label='Pest Control')
water_recycle    = Transition(label='Water Recycle')
light_optimize   = Transition(label='Light Optimize')
growth_monitor   = Transition(label='Growth Monitor')
growth_analyze   = Transition(label='Growth Analyze')
harvest_sync     = Transition(label='Harvest Sync')
demand_forecast  = Transition(label='Demand Forecast')
sterilize_crop   = Transition(label='Sterilize Crop')
package_fresh    = Transition(label='Package Fresh')
delivery_plan    = Transition(label='Delivery Plan')
data_feedback    = Transition(label='Data Feedback')

# Build the growth‐cycle loop: monitor → analyze, repeat until exit
sub_growth = StrictPartialOrder(nodes=[growth_monitor, growth_analyze])
sub_growth.order.add_edge(growth_monitor, growth_analyze)
skip = SilentTransition()  # exit branch of the loop
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[sub_growth, skip])

# Root partial order: all activities plus the loop node
root = StrictPartialOrder(nodes=[
    seed_select, nutrient_mix, climate_adjust, planting_robotic, pest_control,
    water_recycle, light_optimize, growth_loop,
    harvest_sync, demand_forecast,
    sterilize_crop, package_fresh, delivery_plan, data_feedback
])

# Linear setup: seed → nutrient → climate → planting → pest
root.order.add_edge(seed_select,      nutrient_mix)
root.order.add_edge(nutrient_mix,     climate_adjust)
root.order.add_edge(climate_adjust,   planting_robotic)
root.order.add_edge(planting_robotic, pest_control)

# After pest control, three branches run in parallel: water recycle, light optimize, growth loop
root.order.add_edge(pest_control, water_recycle)
root.order.add_edge(pest_control, light_optimize)
root.order.add_edge(pest_control, growth_loop)

# Harvest synchronization and demand forecast both depend on all three preceding branches
for predecessor in (water_recycle, light_optimize, growth_loop):
    root.order.add_edge(predecessor, harvest_sync)
    root.order.add_edge(predecessor, demand_forecast)

# Post‐harvest: sterilization awaits both harvest and forecast
root.order.add_edge(harvest_sync,    sterilize_crop)
root.order.add_edge(demand_forecast, sterilize_crop)

# Packaging → delivery → feedback
root.order.add_edge(sterilize_crop, package_fresh)
root.order.add_edge(package_fresh,  delivery_plan)
root.order.add_edge(delivery_plan,  data_feedback)