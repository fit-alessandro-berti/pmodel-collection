# Generated from: 32c1ae6d-f396-487c-89ca-3117e9cbd46e.json
# Description: This process outlines the comprehensive management cycle of an urban vertical farm that integrates IoT monitoring, automated nutrient delivery, and sustainable energy usage. It begins with environmental sensing to assess light, humidity, and temperature, followed by adaptive lighting adjustments. Water recycling and nutrient mixing are precisely controlled to optimize plant growth. Pollination is facilitated through robotic drones, while growth progress is tracked via computer vision systems. Harvest scheduling aligns with demand forecasting, and post-harvest processing includes packaging and quality assurance. Waste materials are composted onsite, and energy consumption is continuously optimized through smart grid integration, ensuring minimal environmental impact and maximum yield in a constrained urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
env_sensing = Transition(label='Env Sensing')
light_adjust = Transition(label='Light Adjust')
humidity_check = Transition(label='Humidity Check')
temp_control = Transition(label='Temp Control')
nutrient_mix = Transition(label='Nutrient Mix')
water_recycle = Transition(label='Water Recycle')
drone_pollinate = Transition(label='Drone Pollinate')
growth_scan = Transition(label='Growth Scan')
pest_detect = Transition(label='Pest Detect')
harvest_plan = Transition(label='Harvest Plan')
demand_forecast = Transition(label='Demand Forecast')
quality_check = Transition(label='Quality Check')
pack_produce = Transition(label='Pack Produce')
waste_compost = Transition(label='Waste Compost')
energy_optimize = Transition(label='Energy Optimize')
data_archive = Transition(label='Data Archive')

# Partial order for environmental sensing and adaptation (parallel checks after sensing)
env_partial = StrictPartialOrder(
    nodes=[env_sensing, light_adjust, humidity_check, temp_control]
)
env_partial.order.add_edge(env_sensing, light_adjust)
env_partial.order.add_edge(env_sensing, humidity_check)
env_partial.order.add_edge(env_sensing, temp_control)

# Partial order for nutrient and water handling (parallel)
nutrient_water = StrictPartialOrder(
    nodes=[nutrient_mix, water_recycle]
)

# Partial order for pollination and growth monitoring with pest detection parallel
grow_monitor = StrictPartialOrder(
    nodes=[drone_pollinate, growth_scan, pest_detect]
)

# Harvest planning aligns with demand forecasting (both prior to harvest plan)
harvest_partial = StrictPartialOrder(
    nodes=[demand_forecast, harvest_plan]
)
harvest_partial.order.add_edge(demand_forecast, harvest_plan)

# Post-harvest processing sequential: quality check -> pack produce
post_harvest = StrictPartialOrder(
    nodes=[quality_check, pack_produce]
)
post_harvest.order.add_edge(quality_check, pack_produce)

# Waste compost and energy optimize can be concurrent but happen after packing
waste_energy = StrictPartialOrder(
    nodes=[waste_compost, energy_optimize]
)

# Final data archiving happens after all main activities done
# We'll combine all the main parts into one big partial order

# Create root partial order containing all above nodes and the final node data_archive
root = StrictPartialOrder(
    nodes=[
        env_partial,          # environmental sensing and adaptation
        nutrient_water,       # nutrient mixing & water recycling
        grow_monitor,         # pollination, growth scan, pest detect
        harvest_partial,      # demand forecast and harvest plan
        post_harvest,         # quality check and packing
        waste_energy,         # waste compost and energy optimize
        data_archive          # final archiving activity
    ]
)

# Define ordering dependency among these partial orders and data archive

# env_partial precedes nutrient_water and grow_monitor
root.order.add_edge(env_partial, nutrient_water)
root.order.add_edge(env_partial, grow_monitor)

# nutrient_water and grow_monitor precede harvest planning
root.order.add_edge(nutrient_water, harvest_partial)
root.order.add_edge(grow_monitor, harvest_partial)

# harvest_partial precedes post_harvest
root.order.add_edge(harvest_partial, post_harvest)

# post_harvest precedes waste_energy
root.order.add_edge(post_harvest, waste_energy)

# waste_energy precedes data_archive
root.order.add_edge(waste_energy, data_archive)