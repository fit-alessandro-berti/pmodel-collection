# Generated from: 83d9f815-8f92-4ed5-813c-8f5d1b14f45f.json
# Description: This process details the complex operational cycle of an urban vertical farm that integrates hydroponic systems, renewable energy management, and AI-driven crop optimization. The farm begins with seed preparation and nutrient formulation, followed by automated planting and environmental calibration. Continuous monitoring adjusts lighting, humidity, and nutrient delivery in real-time. Harvesting is staggered based on crop maturity, with post-harvest processing including cleaning, sorting, and packaging. Waste materials are recycled or composted to maintain sustainability. The entire system is supported by predictive maintenance of equipment and data analytics for yield forecasting, ensuring efficient resource use and minimal environmental impact within a constrained urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define Activities
Seed_Prep = Transition(label='Seed Prep')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automated_Plant = Transition(label='Automated Plant')
Env_Calibration = Transition(label='Env Calibration')

Light_Adjust = Transition(label='Light Adjust')
Humidity_Control = Transition(label='Humidity Control')
Nutrient_Feed = Transition(label='Nutrient Feed')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Scan = Transition(label='Pest Scan')

Harvest_Stage = Transition(label='Harvest Stage')
Crop_Sort = Transition(label='Crop Sort')
Pack_Produce = Transition(label='Pack Produce')

Waste_Recycle = Transition(label='Waste Recycle')

Equip_Maintain = Transition(label='Equip Maintain')
Yield_Forecast = Transition(label='Yield Forecast')

# Phase 1: Seed Prep & Nutrient Mix then Automated Plant & Env Calibration (both sequential)
phase1 = StrictPartialOrder(nodes=[Seed_Prep, Nutrient_Mix, Automated_Plant, Env_Calibration])
phase1.order.add_edge(Seed_Prep, Nutrient_Mix)
phase1.order.add_edge(Nutrient_Mix, Automated_Plant)
phase1.order.add_edge(Automated_Plant, Env_Calibration)

# Phase 2: Continuous Monitoring with concurrent lighting, humidity, nutrient feed, growth monitor, and pest scan
monitoring_nodes = [Light_Adjust, Humidity_Control, Nutrient_Feed, Growth_Monitor, Pest_Scan]
phase2 = StrictPartialOrder(nodes=monitoring_nodes)
# No order edges - all concurrent as adjustments and monitoring run in parallel

# Phase 3: Harvesting staggered based on crop maturity (sequential: Harvest Stage then Crop Sort then Pack Produce)
phase3 = StrictPartialOrder(nodes=[Harvest_Stage, Crop_Sort, Pack_Produce])
phase3.order.add_edge(Harvest_Stage, Crop_Sort)
phase3.order.add_edge(Crop_Sort, Pack_Produce)

# Phase 4: Waste recycle (can be concurrent with Phase 3 and after packing)
# Phase 5: Support activities: Equip Maintain and Yield Forecast (concurrent with main flow)

# Combine Phases 3 and 4 into final processing partial order
processing_phase = StrictPartialOrder(nodes=[phase3, Waste_Recycle])
processing_phase.order.add_edge(phase3, Waste_Recycle)  # Waste recycle after packing

# Combine all phases in partial order:
root_nodes = [phase1, phase2, processing_phase, Equip_Maintain, Yield_Forecast]
root = StrictPartialOrder(nodes=root_nodes)

# Order edges defining process flow:
# phase1 before monitoring and harvesting
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase1, processing_phase)
# monitoring (phase2) concurrent with processing_phase but must start after phase1
# Equip maintain and yield forecast concurrent with main flow, so no edges to/from them

# The final 'root' POWL model is ready