# Generated from: e7db1b32-e87f-4cb5-831a-5b41249adcdc.json
# Description: This process outlines the complex operational cycle of an urban vertical farming facility that integrates IoT sensors, automated nutrient delivery, and AI-driven crop monitoring to optimize yield and resource efficiency. It begins with seed selection based on AI growth predictions, followed by automated planting in vertical trays. Environmental conditions like humidity, temperature, and light are continuously monitored and adjusted via smart controls. Nutrient solutions are precisely dosed through hydroponic systems, while robotic arms conduct pruning and harvesting to maintain plant health. Data collected is analyzed in real-time for predictive maintenance and yield forecasting. The process also involves waste recycling through composting organic residues and repurposing water. Finally, harvested produce is packaged using biodegradable materials and dispatched through an integrated logistics platform focused on reducing carbon footprint. This atypical process merges agriculture, technology, and sustainability in an urban setting to revolutionize food production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Seed_Selection = Transition(label='Seed Selection')
AI_Prediction = Transition(label='AI Prediction')
Automated_Planting = Transition(label='Automated Planting')
Sensor_Calibration = Transition(label='Sensor Calibration')
Environment_Adjust = Transition(label='Environment Adjust')
Nutrient_Dosing = Transition(label='Nutrient Dosing')
Hydroponic_Flow = Transition(label='Hydroponic Flow')
Robotic_Pruning = Transition(label='Robotic Pruning')
Health_Monitor = Transition(label='Health Monitor')
Harvesting_Ops = Transition(label='Harvesting Ops')
Data_Analysis = Transition(label='Data Analysis')
Predictive_Check = Transition(label='Predictive Check')
Waste_Composting = Transition(label='Waste Composting')
Water_Recycling = Transition(label='Water Recycling')
Eco_Packaging = Transition(label='Eco Packaging')
Carbon_Tracking = Transition(label='Carbon Tracking')
Logistics_Dispatch = Transition(label='Logistics Dispatch')

# Start with Seed Selection followed by AI Prediction and then Automated Planting
start_PO = StrictPartialOrder(nodes=[Seed_Selection, AI_Prediction, Automated_Planting])
start_PO.order.add_edge(Seed_Selection, AI_Prediction)
start_PO.order.add_edge(AI_Prediction, Automated_Planting)

# Monitoring and adjustments: Sensor Calibration --> Environment Adjust
monitoring_PO = StrictPartialOrder(nodes=[Sensor_Calibration, Environment_Adjust])
monitoring_PO.order.add_edge(Sensor_Calibration, Environment_Adjust)

# Nutrient dosing and hydroponic flow happen sequentially
nutrient_PO = StrictPartialOrder(nodes=[Nutrient_Dosing, Hydroponic_Flow])
nutrient_PO.order.add_edge(Nutrient_Dosing, Hydroponic_Flow)

# Robotic pruning and health monitoring can be concurrent but must both finish before harvesting
pruning_monitor_PO = StrictPartialOrder(nodes=[Robotic_Pruning, Health_Monitor])
# concurrent - no edges

# Harvesting follows pruning and health monitoring
harvesting_PO = StrictPartialOrder(nodes=[Harvesting_Ops])
# We will link pruning_monitor_PO to harvesting_PO later

# Data analysis and predictive checks form a loop: after data analysis, loop choice of exit or predictive check then data analysis again
data_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Data_Analysis, Predictive_Check]
)

# Waste Composting and Water Recycling happen concurrently after harvesting and can happen anytime before packaging
waste_water_PO = StrictPartialOrder(nodes=[Waste_Composting, Water_Recycling])
# concurrent - no edges

# Packaging and then Carbon Tracking then Dispatch in sequence
packaging_PO = StrictPartialOrder(nodes=[Eco_Packaging, Carbon_Tracking, Logistics_Dispatch])
packaging_PO.order.add_edge(Eco_Packaging, Carbon_Tracking)
packaging_PO.order.add_edge(Carbon_Tracking, Logistics_Dispatch)

# Now combine phases with dependencies:

# Phase 1: start_PO --> monitoring_PO
phase1_PO = StrictPartialOrder(nodes=[start_PO, monitoring_PO])
phase1_PO.order.add_edge(start_PO, monitoring_PO)

# Phase 2: monitoring_PO --> nutrient_PO
phase2_PO = StrictPartialOrder(nodes=[phase1_PO, nutrient_PO])
phase2_PO.order.add_edge(phase1_PO, nutrient_PO)

# Phase 3: nutrient_PO --> pruning_monitor_PO
phase3_PO = StrictPartialOrder(nodes=[phase2_PO, pruning_monitor_PO])
phase3_PO.order.add_edge(phase2_PO, pruning_monitor_PO)

# Phase 4: pruning_monitor_PO --> harvesting_PO
phase4_PO = StrictPartialOrder(nodes=[phase3_PO, harvesting_PO])
phase4_PO.order.add_edge(phase3_PO, harvesting_PO)

# Phase 5: harvesting_PO --> data_loop and waste_water_PO (both concurrent after harvesting)
phase5_PO = StrictPartialOrder(
    nodes=[phase4_PO, data_loop, waste_water_PO]
)
phase5_PO.order.add_edge(phase4_PO, data_loop)
phase5_PO.order.add_edge(phase4_PO, waste_water_PO)

# Final phase: data_loop and waste_water_PO --> packaging_PO
final_PO = StrictPartialOrder(
    nodes=[phase5_PO, packaging_PO]
)
final_PO.order.add_edge(phase5_PO, packaging_PO)

# The final root model
root = final_PO