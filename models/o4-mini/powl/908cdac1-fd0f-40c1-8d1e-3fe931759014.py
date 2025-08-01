# Generated from: 908cdac1-fd0f-40c1-8d1e-3fe931759014.json
# Description: This process outlines the complex operational cycle of an urban vertical farm integrating automated hydroponic systems, environmental controls, and supply chain logistics. It begins with seed selection and germination, followed by nutrient monitoring and adaptive lighting adjustments to optimize plant growth. Continuous pest detection and bio-control deployment maintain crop health without chemicals. Concurrently, data from IoT sensors is analyzed for predictive maintenance of farm equipment. Harvesting is synchronized with packaging and cold chain preparation to ensure freshness. The process concludes with real-time demand forecasting and direct-to-consumer distribution, closing the loop with customer feedback integration for iterative improvements in crop varieties and operational efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection    = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
nutrient_check    = Transition(label='Nutrient Check')
light_adjust      = Transition(label='Light Adjust')
pest_scan         = Transition(label='Pest Scan')
bio_control_deploy= Transition(label='Bio-Control Deploy')
sensor_data       = Transition(label='Sensor Data')
equipment_check   = Transition(label='Equipment Check')
growth_analysis   = Transition(label='Growth Analysis')
harvest_plan      = Transition(label='Harvest Plan')
crop_picking      = Transition(label='Crop Picking')
package_prep      = Transition(label='Package Prep')
cold_chain        = Transition(label='Cold Chain')
demand_forecast   = Transition(label='Demand Forecast')
order_dispatch    = Transition(label='Order Dispatch')
feedback_review   = Transition(label='Feedback Review')

# A silent transition for loop exits
skip = SilentTransition()

# 1) Growth cycle body: Nutrient Check -> Light Adjust -> Pest Scan -> Bio-Control Deploy
growth_body = StrictPartialOrder(nodes=[
    nutrient_check,
    light_adjust,
    pest_scan,
    bio_control_deploy
])
growth_body.order.add_edge(nutrient_check, light_adjust)
growth_body.order.add_edge(light_adjust, pest_scan)
growth_body.order.add_edge(pest_scan, bio_control_deploy)

# 2) Loop around the growth cycle: repeat growth_body until exit
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_body, skip]
)

# 3) Sensor-data-driven maintenance flow: Sensor Data -> Equipment Check -> Growth Analysis
sensor_flow = StrictPartialOrder(nodes=[
    sensor_data,
    equipment_check,
    growth_analysis
])
sensor_flow.order.add_edge(sensor_data, equipment_check)
sensor_flow.order.add_edge(equipment_check, growth_analysis)

# 4) Harvesting sequence: Harvest Plan -> Crop Picking -> Package Prep -> Cold Chain
harvest_seq = StrictPartialOrder(nodes=[
    harvest_plan,
    crop_picking,
    package_prep,
    cold_chain
])
harvest_seq.order.add_edge(harvest_plan, crop_picking)
harvest_seq.order.add_edge(crop_picking, package_prep)
harvest_seq.order.add_edge(package_prep, cold_chain)

# 5) Demand -> Dispatch
demand_seq = StrictPartialOrder(nodes=[
    demand_forecast,
    order_dispatch
])
demand_seq.order.add_edge(demand_forecast, order_dispatch)

# 6) Main cycle: sequence and concurrency
#    Seed Selection -> Germination Start -> {growth_loop, sensor_flow} in parallel -> harvest_seq -> demand_seq
cycle = StrictPartialOrder(nodes=[
    seed_selection,
    germination_start,
    growth_loop,
    sensor_flow,
    harvest_seq,
    demand_forecast,
    order_dispatch
])
cycle.order.add_edge(seed_selection, germination_start)
cycle.order.add_edge(germination_start, growth_loop)
cycle.order.add_edge(germination_start, sensor_flow)
cycle.order.add_edge(growth_loop, harvest_seq)
cycle.order.add_edge(sensor_flow, harvest_seq)
cycle.order.add_edge(harvest_seq, demand_forecast)
cycle.order.add_edge(demand_forecast, order_dispatch)

# 7) Wrap the entire cycle in a loop that optionally performs feedback review before repeating
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycle, feedback_review]
)