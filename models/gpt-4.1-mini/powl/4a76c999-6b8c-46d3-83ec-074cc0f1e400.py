# Generated from: 4a76c999-6b8c-46d3-83ec-074cc0f1e400.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farm integrating advanced hydroponics, AI-driven climate control, and automated harvesting. Beginning with seed selection optimized for urban conditions, it proceeds through nutrient calibration, environmental monitoring, pest bio-control deployment, and energy-efficient lighting adjustments. The flow includes real-time data analytics to predict growth phases and yield, adaptive resource allocation to minimize waste, and robotic harvesting that ensures produce quality. Post-harvest, the cycle incorporates packaging customization based on market demand, waste recycling into biofertilizers, and distribution scheduling aligned with consumer freshness windows. The process is designed to maximize productivity in constrained urban spaces while maintaining sustainability and reducing carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
Sensor_Calibration = Transition(label='Sensor Calibration')
Pest_Control = Transition(label='Pest Control')
Lighting_Adjust = Transition(label='Lighting Adjust')
Growth_Tracking = Transition(label='Growth Tracking')
Data_Analysis = Transition(label='Data Analysis')
Resource_Shift = Transition(label='Resource Shift')
Robotic_Harvest = Transition(label='Robotic Harvest')
Quality_Check = Transition(label='Quality Check')
Packaging_Sort = Transition(label='Packaging Sort')
Waste_Cycle = Transition(label='Waste Cycle')
Delivery_Plan = Transition(label='Delivery Plan')
Market_Sync = Transition(label='Market Sync')

# Construct the initial flow:
# Seed Selection -> Nutrient Mix -> Climate Setup -> Sensor Calibration
# Then Pest Control and Lighting Adjust are concurrent after Sensor Calibration
initial_PO = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Mix, Climate_Setup, Sensor_Calibration, Pest_Control, Lighting_Adjust])
initial_PO.order.add_edge(Seed_Selection, Nutrient_Mix)
initial_PO.order.add_edge(Nutrient_Mix, Climate_Setup)
initial_PO.order.add_edge(Climate_Setup, Sensor_Calibration)
initial_PO.order.add_edge(Sensor_Calibration, Pest_Control)
initial_PO.order.add_edge(Sensor_Calibration, Lighting_Adjust)

# After Pest Control and Lighting Adjust complete (concurrent), 
# Growth Tracking starts
post_pest_lighting_PO = StrictPartialOrder(nodes=[Pest_Control, Lighting_Adjust, Growth_Tracking])
post_pest_lighting_PO.order.add_edge(Pest_Control, Growth_Tracking)
post_pest_lighting_PO.order.add_edge(Lighting_Adjust, Growth_Tracking)

# After Growth Tracking -> Data Analysis -> Resource Shift (sequential)
growth_to_resource_PO = StrictPartialOrder(nodes=[Growth_Tracking, Data_Analysis, Resource_Shift])
growth_to_resource_PO.order.add_edge(Growth_Tracking, Data_Analysis)
growth_to_resource_PO.order.add_edge(Data_Analysis, Resource_Shift)

# After Resource Shift -> Robotic Harvest -> Quality Check (sequential)
harvest_PO = StrictPartialOrder(nodes=[Resource_Shift, Robotic_Harvest, Quality_Check])
harvest_PO.order.add_edge(Resource_Shift, Robotic_Harvest)
harvest_PO.order.add_edge(Robotic_Harvest, Quality_Check)

# After Quality Check, 3 concurrent activities:
# Packaging Sort, Waste Cycle, Delivery Plan
post_quality_PO = StrictPartialOrder(nodes=[Quality_Check, Packaging_Sort, Waste_Cycle, Delivery_Plan])
post_quality_PO.order.add_edge(Quality_Check, Packaging_Sort)
post_quality_PO.order.add_edge(Quality_Check, Waste_Cycle)
post_quality_PO.order.add_edge(Quality_Check, Delivery_Plan)

# Market Sync follows Delivery Plan
market_sync_PO = StrictPartialOrder(nodes=[Delivery_Plan, Market_Sync])
market_sync_PO.order.add_edge(Delivery_Plan, Market_Sync)

# Combine post_quality_PO and market_sync_PO to enforce Delivery Plan before Market Sync
# To do that, create a PO with all nodes of post_quality_PO + Market_Sync and proper edges
final_PO = StrictPartialOrder(nodes=[
    Quality_Check, Packaging_Sort, Waste_Cycle, Delivery_Plan, Market_Sync
])
final_PO.order.add_edge(Quality_Check, Packaging_Sort)
final_PO.order.add_edge(Quality_Check, Waste_Cycle)
final_PO.order.add_edge(Quality_Check, Delivery_Plan)
final_PO.order.add_edge(Delivery_Plan, Market_Sync)

# Now combine all stages stepwise as a partial order reflecting the flow of the whole process:
# initial_PO -> post_pest_lighting_PO -> growth_to_resource_PO -> harvest_PO -> final_PO

# This can be encoded by embedding the partial orders as nodes in a master PO and linking them accordingly

# However, pm4py POWL expects nodes to be Transition, OperatorPOWL, or StrictPartialOrder
# So we can create nested StrictPartialOrder for concurrent parts, assemble sequence via order edges

# Create top-level POs for each stage grouping nodes accordingly

# Stage 1: from Seed Selection to concurrent Pest Control and Lighting Adjust
stage1 = initial_PO

# Stage 2: Pest Control and Lighting Adjust concurrency completed by Growth Tracking
stage2 = post_pest_lighting_PO

# Stage 3: Growth Tracking, Data Analysis, Resource Shift (sequential)
stage3 = growth_to_resource_PO

# Stage 4: Resource Shift, Robotic Harvest, Quality Check (sequential)
stage4 = harvest_PO

# Stage 5: After Quality Check: concurrent Packaging Sort, Waste Cycle, Delivery Plan + Market Sync after Delivery Plan
stage5 = final_PO

# Now compose a top-level StrictPartialOrder connecting these stages sequentially
# To do this, define nodes as the stages themselves (they are StrictPartialOrder instances)
top_level_nodes = [stage1, stage2, stage3, stage4, stage5]

root = StrictPartialOrder(nodes=top_level_nodes)
root.order.add_edge(stage1, stage2)
root.order.add_edge(stage2, stage3)
root.order.add_edge(stage3, stage4)
root.order.add_edge(stage4, stage5)