# Generated from: 33d03a3d-34b4-466e-ac80-9231cb9f5671.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farming system integrating automated hydroponics, environmental control, and crop yield optimization. Beginning with seed selection adapted for vertical growth, it moves through nutrient solution calibration, climate modulation, and multi-layer planting schedules. Continuous sensor data analysis enables adaptive lighting and irrigation adjustments while pest monitoring employs AI-driven detection. Harvesting is staggered to maximize space utilization, followed by post-harvest sorting and packaging within onsite clean rooms. Waste biomass is processed into bio-compost, closing the sustainability loop. This atypical but realistic process blends agriculture, IoT technology, and urban sustainability initiatives to meet local food demand efficiently within constrained city spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
Layer_Planting = Transition(label='Layer Planting')
Sensor_Install = Transition(label='Sensor Install')
Data_Monitoring = Transition(label='Data Monitoring')
Lighting_Adjust = Transition(label='Lighting Adjust')
Irrigation_Tune = Transition(label='Irrigation Tune')
Pest_Detect = Transition(label='Pest Detect')
Harvest_Plan = Transition(label='Harvest Plan')
Crop_Harvest = Transition(label='Crop Harvest')
Sorting_Pack = Transition(label='Sorting Pack')
Waste_Collect = Transition(label='Waste Collect')
Bio_Compost = Transition(label='Bio-Compost')
Yield_Review = Transition(label='Yield Review')
System_Clean = Transition(label='System Clean')

skip = SilentTransition()

# Loop for adaptive adjustments from sensor data: 
# After Data Monitoring, loop optionally executes Lighting Adjust and Irrigation Tune repeatedly
# loop = *(A=Data_Monitoring, B=Lighting_Adjust + Irrigation_Tune in partial order)
# We model the B (body) as a partial order of concurrent Lighting Adjust and Irrigation Tune so both can happen in any order or concurrency.
adjustments = StrictPartialOrder(nodes=[Lighting_Adjust, Irrigation_Tune])  # concurrent adjustments
# no order edges needed; they are concurrent

# Create loop node: execute Data Monitoring once, then repeatedly choose exit or perform adjustments + Data Monitoring again
# i.e., * (Data_Monitoring, adjustments)
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[Data_Monitoring, adjustments])

# Pest monitoring occurs after sensor data and adjustments, then Harvest Plan
# Pest detection also triggers Harvest Plan

# Multi-layer planting is concurrent with sensor install, both after climate setup
# so partial order with Sensor Install and Layer Planting concurrent, both after Climate Setup

# Harvest plan leads to multiple staggers of crop harvest - modeled as loop with Crop Harvest

# Loop for staggered harvest: perform Crop Harvest repeatedly until done
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Harvest_Plan, Crop_Harvest])

# Post-harvest: Sorting and Packing then Waste Collection + Bio-Compost in parallel (partial order)

post_harvest_sort_pack = StrictPartialOrder(nodes=[Sorting_Pack, Waste_Collect, Bio_Compost])
# Sorting_Pack --> Waste_Collect and Sorting_Pack --> Bio_Compost
post_harvest_sort_pack.order.add_edge(Sorting_Pack, Waste_Collect)
post_harvest_sort_pack.order.add_edge(Sorting_Pack, Bio_Compost)
# Waste_Collect and Bio_Compost concurrent

# Yield review and system clean happen after post harvest
post_harvest = StrictPartialOrder(nodes=[post_harvest_sort_pack, Yield_Review, System_Clean])
# Need to flatten post_harvest_sort_pack nodes inside post_harvest partial order:
# Instead of nesting post_harvest_sort_pack as a node, we merge its nodes in post_harvest to keep one partial order

# So rebuild final partial order after harvest_loop as:
final_post_harvest_nodes = [Sorting_Pack, Waste_Collect, Bio_Compost, Yield_Review, System_Clean]
final_post_harvest = StrictPartialOrder(nodes=final_post_harvest_nodes)
final_post_harvest.order.add_edge(Sorting_Pack, Waste_Collect)
final_post_harvest.order.add_edge(Sorting_Pack, Bio_Compost)
final_post_harvest.order.add_edge(Waste_Collect, Yield_Review)
final_post_harvest.order.add_edge(Bio_Compost, Yield_Review)
final_post_harvest.order.add_edge(Yield_Review, System_Clean)

# Now, build the main partial order:

# Seed Selection --> Nutrient Mix --> Climate Setup --> (Sensor Install || Layer Planting) 
# Sensor Install and Layer Planting concurrent, both after Climate Setup
# Both lead to sensor_loop (monitoring and adjustments)
# sensor_loop --> Pest Detect --> harvest_loop --> final_post_harvest --> Yield_Review and System_Clean already included in final_post_harvest

# Note: Yield Review and System Clean are after final_post_harvest, already ordered

# We build the main PO nodes: Seed Selection, Nutrient Mix, Climate Setup,
# Sensor Install, Layer Planting,
# sensor_loop, Pest Detect, harvest_loop,
# and finally the final_post_harvest nodes (Sorting_Pack, Waste_Collect, Bio_Compost, Yield_Review, System_Clean)

main_nodes = [
    Seed_Selection, Nutrient_Mix, Climate_Setup,
    Sensor_Install, Layer_Planting,
    sensor_loop, Pest_Detect, harvest_loop,
    Sorting_Pack, Waste_Collect, Bio_Compost, Yield_Review, System_Clean
]

root = StrictPartialOrder(nodes=main_nodes)

# Add sequential edges:
root.order.add_edge(Seed_Selection, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Climate_Setup)

# Climate Setup precedes Sensor Install and Layer Planting (both concurrent)
root.order.add_edge(Climate_Setup, Sensor_Install)
root.order.add_edge(Climate_Setup, Layer_Planting)

# Sensor Install and Layer Planting both precede sensor_loop (converge)
root.order.add_edge(Sensor_Install, sensor_loop)
root.order.add_edge(Layer_Planting, sensor_loop)

# sensor_loop precedes Pest Detect
root.order.add_edge(sensor_loop, Pest_Detect)

# Pest Detect precedes harvest_loop
root.order.add_edge(Pest_Detect, harvest_loop)

# harvest_loop precedes Sorting_Pack (start of final post harvest)
root.order.add_edge(harvest_loop, Sorting_Pack)

# Sorting Pack precedes Waste_Collect and Bio_Compost (added inside final_post_harvest already)
# Waste_Collect and Bio_Compost precede Yield_Review
# Yield_Review precedes System_Clean

# These edges are already added inside final_post_harvest, which shares these nodes with root.
# To make order consistent in root, we must add them again to root.order:

root.order.add_edge(Sorting_Pack, Waste_Collect)
root.order.add_edge(Sorting_Pack, Bio_Compost)
root.order.add_edge(Waste_Collect, Yield_Review)
root.order.add_edge(Bio_Compost, Yield_Review)
root.order.add_edge(Yield_Review, System_Clean)