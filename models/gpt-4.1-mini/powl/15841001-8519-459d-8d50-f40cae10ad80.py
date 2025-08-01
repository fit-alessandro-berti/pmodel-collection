# Generated from: 15841001-8519-459d-8d50-f40cae10ad80.json
# Description: This process outlines the comprehensive cycle of managing an urban vertical farm, integrating advanced hydroponics, automated nutrient delivery, environmental monitoring, and crop harvesting. It begins with site preparation and seed selection, followed by controlled germination, nutrient solution calibration, and continuous growth monitoring using IoT sensors. Pest and disease management is conducted with biocontrol agents, while energy optimization ensures sustainable operations. Harvesting is synchronized with market demand forecasts, and post-harvest processing includes quality grading and packaging. The cycle completes with waste recycling and system maintenance to ensure perpetual productivity within constrained urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Prep = Transition(label='Site Prep')
Seed_Select = Transition(label='Seed Select')
Germination = Transition(label='Germination')
Nutrient_Mix = Transition(label='Nutrient Mix')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Disease_Check = Transition(label='Disease Check')
Energy_Audit = Transition(label='Energy Audit')
Water_Recycle = Transition(label='Water Recycle')
Climate_Adjust = Transition(label='Climate Adjust')
Harvest_Plan = Transition(label='Harvest Plan')
Crop_Picking = Transition(label='Crop Picking')
Quality_Grade = Transition(label='Quality Grade')
Package_Goods = Transition(label='Package Goods')
Waste_Process = Transition(label='Waste Process')
System_Maintain = Transition(label='System Maintain')

# Build pest/disease management partial order: concurrency of Pest Control and Disease Check
pest_disease = StrictPartialOrder(nodes=[Pest_Control, Disease_Check])

# Energy Optimization and Water Recycle and Climate Adjust happen concurrently after Pest/Disease
# Partial order of these three concurrent activities
env_monitoring = StrictPartialOrder(nodes=[Energy_Audit, Water_Recycle, Climate_Adjust])

# After these, Harvest Plan -> Crop Picking -> Quality Grade -> Package Goods in sequence
post_harvest = StrictPartialOrder(nodes=[Harvest_Plan, Crop_Picking, Quality_Grade, Package_Goods])
post_harvest.order.add_edge(Harvest_Plan, Crop_Picking)
post_harvest.order.add_edge(Crop_Picking, Quality_Grade)
post_harvest.order.add_edge(Quality_Grade, Package_Goods)

# After post harvest, Waste Process and System Maintain in sequence
waste_maintain = StrictPartialOrder(nodes=[Waste_Process, System_Maintain])
waste_maintain.order.add_edge(Waste_Process, System_Maintain)

# Growth monitoring happens continuously during growth process: for simplicity, model as sequential after nutrient mix and before pest/disease
# Overall growth monitoring after Nutrient Mix, before pest/disease and environment monitoring

# Define sequence of initial steps:
# Site Prep -> Seed Select -> Germination -> Nutrient Mix -> Growth Monitor
initial_sequence = StrictPartialOrder(nodes=[Site_Prep, Seed_Select, Germination, Nutrient_Mix, Growth_Monitor])
initial_sequence.order.add_edge(Site_Prep, Seed_Select)
initial_sequence.order.add_edge(Seed_Select, Germination)
initial_sequence.order.add_edge(Germination, Nutrient_Mix)
initial_sequence.order.add_edge(Nutrient_Mix, Growth_Monitor)

# Then Pest/Disease management (concurrent), then environment monitoring (concurrent),
# then harvesting (sequential) and waste/maintenance (sequential).
# Linking these parts in sequence

# Build partial order connecting the parts.

# Create final root partial order with all nodes
nodes = [
    Site_Prep, Seed_Select, Germination, Nutrient_Mix, Growth_Monitor,
    Pest_Control, Disease_Check,
    Energy_Audit, Water_Recycle, Climate_Adjust,
    Harvest_Plan, Crop_Picking, Quality_Grade, Package_Goods,
    Waste_Process, System_Maintain,
]

root = StrictPartialOrder(nodes=nodes)

# Initial sequence edges
root.order.add_edge(Site_Prep, Seed_Select)
root.order.add_edge(Seed_Select, Germination)
root.order.add_edge(Germination, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Growth_Monitor)

# From Growth Monitor to Pest and Disease (both concurrent)
root.order.add_edge(Growth_Monitor, Pest_Control)
root.order.add_edge(Growth_Monitor, Disease_Check)

# Pest and Disease to environment monitoring (concurrent)
root.order.add_edge(Pest_Control, Energy_Audit)
root.order.add_edge(Pest_Control, Water_Recycle)
root.order.add_edge(Pest_Control, Climate_Adjust)
root.order.add_edge(Disease_Check, Energy_Audit)
root.order.add_edge(Disease_Check, Water_Recycle)
root.order.add_edge(Disease_Check, Climate_Adjust)

# Environment monitoring to Harvest Plan (start of post harvest)
root.order.add_edge(Energy_Audit, Harvest_Plan)
root.order.add_edge(Water_Recycle, Harvest_Plan)
root.order.add_edge(Climate_Adjust, Harvest_Plan)

# Post harvest sequential edges
root.order.add_edge(Harvest_Plan, Crop_Picking)
root.order.add_edge(Crop_Picking, Quality_Grade)
root.order.add_edge(Quality_Grade, Package_Goods)

# Package Goods to Waste Process (start of final steps)
root.order.add_edge(Package_Goods, Waste_Process)

# Waste Process to System Maintain
root.order.add_edge(Waste_Process, System_Maintain)