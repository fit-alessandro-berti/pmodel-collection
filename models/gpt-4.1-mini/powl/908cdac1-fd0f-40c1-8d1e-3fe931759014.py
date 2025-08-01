# Generated from: 908cdac1-fd0f-40c1-8d1e-3fe931759014.json
# Description: This process outlines the complex operational cycle of an urban vertical farm integrating automated hydroponic systems, environmental controls, and supply chain logistics. It begins with seed selection and germination, followed by nutrient monitoring and adaptive lighting adjustments to optimize plant growth. Continuous pest detection and bio-control deployment maintain crop health without chemicals. Concurrently, data from IoT sensors is analyzed for predictive maintenance of farm equipment. Harvesting is synchronized with packaging and cold chain preparation to ensure freshness. The process concludes with real-time demand forecasting and direct-to-consumer distribution, closing the loop with customer feedback integration for iterative improvements in crop varieties and operational efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Seed_Selection = Transition(label='Seed Selection')
Germination_Start = Transition(label='Germination Start')
Nutrient_Check = Transition(label='Nutrient Check')
Light_Adjust = Transition(label='Light Adjust')
Pest_Scan = Transition(label='Pest Scan')
Bio_Control_Deploy = Transition(label='Bio-Control Deploy')
Sensor_Data = Transition(label='Sensor Data')
Equipment_Check = Transition(label='Equipment Check')
Growth_Analysis = Transition(label='Growth Analysis')
Harvest_Plan = Transition(label='Harvest Plan')
Crop_Picking = Transition(label='Crop Picking')
Package_Prep = Transition(label='Package Prep')
Cold_Chain = Transition(label='Cold Chain')
Demand_Forecast = Transition(label='Demand Forecast')
Order_Dispatch = Transition(label='Order Dispatch')
Feedback_Review = Transition(label='Feedback Review')

# Define pest detection and bio-control deployment as a partial order (concurrent, but Bio-Control Deploy depends on Pest Scan)
pest_control = StrictPartialOrder(nodes=[Pest_Scan, Bio_Control_Deploy])
pest_control.order.add_edge(Pest_Scan, Bio_Control_Deploy)

# Define sensor data analysis and equipment check and growth analysis as partial order (Growth Analysis depends on Sensor Data and Equipment Check,
# Sensor Data and Equipment Check independent/concurrent)
sensor_analysis = StrictPartialOrder(nodes=[Sensor_Data, Equipment_Check, Growth_Analysis])
sensor_analysis.order.add_edge(Sensor_Data, Growth_Analysis)
sensor_analysis.order.add_edge(Equipment_Check, Growth_Analysis)

# Define harvesting, packaging and cold chain as partial order (Harvest Plan, then concurrent Crop Picking and Package Prep, then Cold Chain)
harvest_preparation = StrictPartialOrder(
    nodes=[Harvest_Plan, Crop_Picking, Package_Prep, Cold_Chain])
harvest_preparation.order.add_edge(Harvest_Plan, Crop_Picking)
harvest_preparation.order.add_edge(Harvest_Plan, Package_Prep)
harvest_preparation.order.add_edge(Crop_Picking, Cold_Chain)
harvest_preparation.order.add_edge(Package_Prep, Cold_Chain)

# Define demand forecasting and order dispatch and feedback review:
# Demand Forecast -> Order Dispatch -> Feedback Review
demand_dispatch_feedback = StrictPartialOrder(
    nodes=[Demand_Forecast, Order_Dispatch, Feedback_Review])
demand_dispatch_feedback.order.add_edge(Demand_Forecast, Order_Dispatch)
demand_dispatch_feedback.order.add_edge(Order_Dispatch, Feedback_Review)

# Nutrient Check and Light Adjust run sequentially after Germination Start
growth_optimization = StrictPartialOrder(
    nodes=[Nutrient_Check, Light_Adjust])
growth_optimization.order.add_edge(Nutrient_Check, Light_Adjust)

# The overall growth phase after Germination Start is growth_optimization and pest_control running concurrently
growth_phase = StrictPartialOrder(
    nodes=[growth_optimization, pest_control])

# Add order edges: both Nutrient Check -> Light Adjust inside growth_optimization, no edges between growth_optimization and pest_control to allow partial order concurrency.

# Connect initial seed selection and germination start
start_phase = StrictPartialOrder(nodes=[Seed_Selection, Germination_Start])
start_phase.order.add_edge(Seed_Selection, Germination_Start)

# After Germination Start comes growth_phase (growth_optimization & pest_control)
# So Germination Start -> growth_phase
# But growth_phase is itself a strict partial order with nodes = [growth_optimization, pest_control]
# The nodes can contain other strict partial orders as nodes.

# After growth_phase, sensor_analysis runs
# Then harvesting preparation
# Then demand_dispatch_feedback

# Compose the process in partial orders stacking them in sequence:
# So we need a top-level PO from start_phase to growth_phase to sensor_analysis to harvest_preparation to demand_dispatch_feedback

# We'll create a top-level StrictPartialOrder with nodes:
# [start_phase, growth_phase, sensor_analysis, harvest_preparation, demand_dispatch_feedback]

root = StrictPartialOrder(
    nodes=[start_phase, growth_phase, sensor_analysis, harvest_preparation, demand_dispatch_feedback])

root.order.add_edge(start_phase, growth_phase)
root.order.add_edge(growth_phase, sensor_analysis)
root.order.add_edge(sensor_analysis, harvest_preparation)
root.order.add_edge(harvest_preparation, demand_dispatch_feedback)