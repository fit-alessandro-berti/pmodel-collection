# Generated from: 0b228e6d-ce47-4277-99d2-b29b0c68045c.json
# Description: This process outlines the complex, cyclical operations of an urban vertical farm that integrates renewable energy management, waste recycling, and community engagement. It starts with seed selection based on predictive analytics, moves through automated nutrient delivery and environmental adjustments using IoT sensors, incorporates waste-to-compost conversion onsite, and ends with dynamic crop harvesting schedules adjusted by market demand and weather forecasts. Additionally, it involves coordinating volunteer shifts, educational workshops, and direct-to-consumer distribution, ensuring sustainability both economically and environmentally in a densely populated urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection = Transition(label='Seed Selection')
soil_prep = Transition(label='Soil Prep')
nutrient_mix = Transition(label='Nutrient Mix')
planting_cycle = Transition(label='Planting Cycle')
sensor_check = Transition(label='Sensor Check')
env_adjust = Transition(label='Env Adjust')
waste_collect = Transition(label='Waste Collect')
compost_turn = Transition(label='Compost Turn')
energy_monitor = Transition(label='Energy Monitor')
water_reuse = Transition(label='Water Reuse')
volunteer_coord = Transition(label='Volunteer Coord')
workshop_plan = Transition(label='Workshop Plan')
market_forecast = Transition(label='Market Forecast')
harvest_schedule = Transition(label='Harvest Schedule')
delivery_pack = Transition(label='Delivery Pack')
customer_notify = Transition(label='Customer Notify')
feedback_gather = Transition(label='Feedback Gather')

# Define loops
sensor_env_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_check, env_adjust])
waste_compost_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_collect, compost_turn])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    soil_prep,
    nutrient_mix,
    planting_cycle,
    sensor_env_loop,
    waste_compost_loop,
    energy_monitor,
    water_reuse,
    market_forecast,
    harvest_schedule,
    delivery_pack,
    customer_notify,
    feedback_gather,
    volunteer_coord,
    workshop_plan
])

# Sequence edges for the main workflow
root.order.add_edge(seed_selection, soil_prep)
root.order.add_edge(soil_prep, nutrient_mix)
root.order.add_edge(nutrient_mix, planting_cycle)
root.order.add_edge(planting_cycle, sensor_env_loop)
root.order.add_edge(sensor_env_loop, waste_compost_loop)
root.order.add_edge(waste_compost_loop, energy_monitor)
root.order.add_edge(energy_monitor, water_reuse)
root.order.add_edge(water_reuse, market_forecast)
root.order.add_edge(market_forecast, harvest_schedule)
root.order.add_edge(harvest_schedule, delivery_pack)
root.order.add_edge(delivery_pack, customer_notify)
root.order.add_edge(customer_notify, feedback_gather)

# After packing, coordinate volunteers and plan workshops concurrently
root.order.add_edge(delivery_pack, volunteer_coord)
root.order.add_edge(delivery_pack, workshop_plan)