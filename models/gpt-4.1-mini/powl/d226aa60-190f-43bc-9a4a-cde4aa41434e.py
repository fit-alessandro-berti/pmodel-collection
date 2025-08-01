# Generated from: d226aa60-190f-43bc-9a4a-cde4aa41434e.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farming system integrating hydroponics and AI-driven environmental controls. It begins with seed selection based on market trends, followed by nutrient mix calibration customized for each crop type. Automated planting ensures precision seed placement, while sensors continuously monitor microclimate variables such as humidity, temperature, and light intensity. Data is analyzed in real-time to adjust water flow and nutrient delivery, optimizing growth rates. Periodic manual inspections validate sensor data and detect pest incursions early. Harvest scheduling leverages predictive analytics to align with demand fluctuations, minimizing waste. Post-harvest, produce undergoes rapid cooling and quality grading before packaging in eco-friendly materials. The process concludes with logistics coordination for same-day urban delivery, feedback collection from retailers, and system maintenance to prepare for the next planting cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Seed_Select = Transition(label='Seed Select')
Trend_Analyze = Transition(label='Trend Analyze')
Nutrient_Mix = Transition(label='Nutrient Mix')
Auto_Plant = Transition(label='Auto Plant')
Sensor_Check = Transition(label='Sensor Check')
Data_Analyze = Transition(label='Data Analyze')
Water_Adjust = Transition(label='Water Adjust')
Light_Control = Transition(label='Light Control')
Humidity_Monitor = Transition(label='Humidity Monitor')
Pest_Inspect = Transition(label='Pest Inspect')
Growth_Forecast = Transition(label='Growth Forecast')
Harvest_Plan = Transition(label='Harvest Plan')
Rapid_Cool = Transition(label='Rapid Cool')
Quality_Grade = Transition(label='Quality Grade')
Eco_Package = Transition(label='Eco Package')
Logistics_Prep = Transition(label='Logistics Prep')
Feedback_Collect = Transition(label='Feedback Collect')
System_Maintain = Transition(label='System Maintain')

# Build sensor monitoring partial order (Sensor_Check → Data_Analyze → adjustments in parallel)
# Sensor_Check -> Data_Analyze -> concurrent (Water_Adjust, Light_Control, Humidity_Monitor)
sensor_adjustments = StrictPartialOrder(nodes=[Water_Adjust, Light_Control, Humidity_Monitor])
# No order between Water_Adjust, Light_Control, Humidity_Monitor → they run concurrent

sensor_data_flow = StrictPartialOrder(
    nodes=[Sensor_Check, Data_Analyze, sensor_adjustments]
)
sensor_data_flow.order.add_edge(Sensor_Check, Data_Analyze)
sensor_data_flow.order.add_edge(Data_Analyze, sensor_adjustments)

# Build subworkflow for periodic manual inspection after sensor monitoring
inspection = Pest_Inspect  # single activity

# Build harvest planning subworkflow after inspection
harvest_plan = Growth_Forecast
harvest_plan_po = StrictPartialOrder(nodes=[Growth_Forecast, Harvest_Plan])
harvest_plan_po.order.add_edge(Growth_Forecast, Harvest_Plan)

# Build post-harvest packaging partial order: Rapid Cool → Quality Grade → Eco Package (sequential)
post_harvest_po = StrictPartialOrder(
    nodes=[Rapid_Cool, Quality_Grade, Eco_Package]
)
post_harvest_po.order.add_edge(Rapid_Cool, Quality_Grade)
post_harvest_po.order.add_edge(Quality_Grade, Eco_Package)

# Build final logistics and feedback partial order
logistics_feedback_maintain = StrictPartialOrder(
    nodes=[Logistics_Prep, Feedback_Collect, System_Maintain]
)
# No order between these three, concurrent

# Assemble the core flow:

# Initial seed selection & trend analysis, then nutrient mix & auto planting
init_po = StrictPartialOrder(
    nodes=[Seed_Select, Trend_Analyze, Nutrient_Mix, Auto_Plant]
)
init_po.order.add_edge(Seed_Select, Trend_Analyze)    # Seed Select -> Trend Analyze
init_po.order.add_edge(Trend_Analyze, Nutrient_Mix)   # Trend Analyze -> Nutrient Mix
init_po.order.add_edge(Nutrient_Mix, Auto_Plant)      # Nutrient Mix -> Auto Plant

# After planting, sensor monitoring + manual inspection parallelism:
# We interpret that sensor monitoring runs continuously,
# manual inspection is periodic after sensor monitoring.

# Merge sensor_data_flow and inspection with order Sensor_Check → Pest_Inspect
sensor_inspect_po = StrictPartialOrder(
    nodes=[sensor_data_flow, inspection]
)
sensor_inspect_po.order.add_edge(sensor_data_flow, Pest_Inspect)

# Then harvest planning
harvest_planning_po = harvest_plan_po

# Then post-harvest packaging
packaging_po = post_harvest_po

# After packaging, logistics and feedback concurrent with system maintenance
final_po = logistics_feedback_maintain

# Chain full process flow:
# init_po -> sensor_inspect_po -> harvest_planning_po -> packaging_po -> final_po

root = StrictPartialOrder(
    nodes=[init_po, sensor_inspect_po, harvest_planning_po, packaging_po, final_po]
)
root.order.add_edge(init_po, sensor_inspect_po)
root.order.add_edge(sensor_inspect_po, harvest_planning_po)
root.order.add_edge(harvest_planning_po, packaging_po)
root.order.add_edge(packaging_po, final_po)