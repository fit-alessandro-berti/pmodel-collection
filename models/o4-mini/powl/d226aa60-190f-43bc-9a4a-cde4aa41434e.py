# Generated from: d226aa60-190f-43bc-9a4a-cde4aa41434e.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farming system integrating hydroponics and AI-driven environmental controls. It begins with seed selection based on market trends, followed by nutrient mix calibration customized for each crop type. Automated planting ensures precision seed placement, while sensors continuously monitor microclimate variables such as humidity, temperature, and light intensity. Data is analyzed in real-time to adjust water flow and nutrient delivery, optimizing growth rates. Periodic manual inspections validate sensor data and detect pest incursions early. Harvest scheduling leverages predictive analytics to align with demand fluctuations, minimizing waste. Post-harvest, produce undergoes rapid cooling and quality grading before packaging in eco-friendly materials. The process concludes with logistics coordination for same-day urban delivery, feedback collection from retailers, and system maintenance to prepare for the next planting cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
trend_analyze    = Transition(label='Trend Analyze')
seed_select      = Transition(label='Seed Select')
nutrient_mix     = Transition(label='Nutrient Mix')
auto_plant       = Transition(label='Auto Plant')
sensor_check     = Transition(label='Sensor Check')
humidity_monitor = Transition(label='Humidity Monitor')
data_analyze     = Transition(label='Data Analyze')
water_adjust     = Transition(label='Water Adjust')
light_control    = Transition(label='Light Control')
pest_inspect     = Transition(label='Pest Inspect')
growth_forecast  = Transition(label='Growth Forecast')
harvest_plan     = Transition(label='Harvest Plan')
rapid_cool       = Transition(label='Rapid Cool')
quality_grade    = Transition(label='Quality Grade')
eco_package      = Transition(label='Eco Package')
logistics_prep   = Transition(label='Logistics Prep')
feedback_collect = Transition(label='Feedback Collect')
system_maintain  = Transition(label='System Maintain')

# Define a silent transition for the loop exit
skip = SilentTransition()

# Build the control loop: sensors -> analyze -> adjust actions
control_loop = StrictPartialOrder(nodes=[
    sensor_check,
    humidity_monitor,
    data_analyze,
    water_adjust,
    light_control
])
control_loop.order.add_edge(sensor_check, data_analyze)
control_loop.order.add_edge(humidity_monitor, data_analyze)
control_loop.order.add_edge(data_analyze, water_adjust)
control_loop.order.add_edge(data_analyze, light_control)

# Wrap the control loop in a LOOP operator to model continuous adjustments
loop_control = OperatorPOWL(
    operator=Operator.LOOP,
    children=[control_loop, skip]
)

# Build the top‐level partial order of the entire process
root = StrictPartialOrder(nodes=[
    trend_analyze,
    seed_select,
    nutrient_mix,
    auto_plant,
    loop_control,
    pest_inspect,
    growth_forecast,
    harvest_plan,
    rapid_cool,
    quality_grade,
    eco_package,
    logistics_prep,
    feedback_collect,
    system_maintain
])

# Define the sequential dependencies
root.order.add_edge(trend_analyze, seed_select)
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, auto_plant)
root.order.add_edge(auto_plant, loop_control)
root.order.add_edge(loop_control, pest_inspect)
root.order.add_edge(pest_inspect, growth_forecast)
root.order.add_edge(growth_forecast, harvest_plan)
root.order.add_edge(harvest_plan, rapid_cool)
root.order.add_edge(rapid_cool, quality_grade)
root.order.add_edge(quality_grade, eco_package)
root.order.add_edge(eco_package, logistics_prep)
root.order.add_edge(logistics_prep, feedback_collect)
root.order.add_edge(feedback_collect, system_maintain)