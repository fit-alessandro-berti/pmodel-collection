# Generated from: 63122b04-d411-41c3-87fb-ab2cf7941f36.json
# Description: This process outlines the comprehensive cycle of urban vertical farming, integrating advanced technologies and sustainability principles. It begins with site analysis and climate mapping to optimize microclimate conditions. Seed selection follows, emphasizing heirloom and genetically optimized varieties. Automated planting is performed using robotics, ensuring precision and efficiency. Nutrient monitoring leverages IoT sensors to maintain optimal hydroponic solutions. Pollination is artificially induced via drone deployment in enclosed environments. Growth tracking uses AI-powered imaging for real-time health assessment. Pest control employs biocontrol agents introduced through targeted release systems. Harvest scheduling adapts dynamically based on crop maturity data. Post-harvest handling includes automated sorting and quality grading using machine vision. Packaging is eco-friendly with biodegradable materials custom-fit by automated machinery. Distribution logistics use blockchain for traceability and smart contracts to ensure timely delivery. Waste recycling repurposes organic residues into biofertilizers. Energy management optimizes renewable inputs and storage. Finally, data analysis feeds back into process improvements, closing the cycle for sustainable urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Analysis = Transition(label='Site Analysis')
Climate_Mapping = Transition(label='Climate Mapping')
Seed_Selection = Transition(label='Seed Selection')
Automated_Planting = Transition(label='Automated Planting')
Nutrient_Monitoring = Transition(label='Nutrient Monitoring')
Pollination_Drone = Transition(label='Pollination Drone')
Growth_Tracking = Transition(label='Growth Tracking')
Pest_Control = Transition(label='Pest Control')
Harvest_Scheduling = Transition(label='Harvest Scheduling')
Post_Harvest = Transition(label='Post-Harvest')
Quality_Grading = Transition(label='Quality Grading')
Eco_Packaging = Transition(label='Eco Packaging')
Distribution_Track = Transition(label='Distribution Track')
Waste_Recycling = Transition(label='Waste Recycling')
Energy_Management = Transition(label='Energy Management')
Data_Analysis = Transition(label='Data Analysis')

# Define the partial order for the process
# Order reflects the sequence described in the narrative:
# Site Analysis and Climate Mapping first (concurrent)
# then Seed Selection
# then Automated Planting
# then Nutrient Monitoring
# then Pollination Drone
# then Growth Tracking
# then Pest Control
# then Harvest Scheduling
# then Post-Harvest and Quality Grading concurrent
# then Eco Packaging
# then Distribution Track
# then Waste Recycling and Energy Management concurrent
# then Data Analysis

nodes = [
    Site_Analysis,
    Climate_Mapping,
    Seed_Selection,
    Automated_Planting,
    Nutrient_Monitoring,
    Pollination_Drone,
    Growth_Tracking,
    Pest_Control,
    Harvest_Scheduling,
    Post_Harvest,
    Quality_Grading,
    Eco_Packaging,
    Distribution_Track,
    Waste_Recycling,
    Energy_Management,
    Data_Analysis
]

root = StrictPartialOrder(nodes=nodes)

# Site Analysis and Climate Mapping concurrent start: no edge between them

# Both leading to Seed Selection
root.order.add_edge(Site_Analysis, Seed_Selection)
root.order.add_edge(Climate_Mapping, Seed_Selection)

# Continuing the chain with single dependencies
root.order.add_edge(Seed_Selection, Automated_Planting)
root.order.add_edge(Automated_Planting, Nutrient_Monitoring)
root.order.add_edge(Nutrient_Monitoring, Pollination_Drone)
root.order.add_edge(Pollination_Drone, Growth_Tracking)
root.order.add_edge(Growth_Tracking, Pest_Control)
root.order.add_edge(Pest_Control, Harvest_Scheduling)

# Post-Harvest and Quality Grading concurrent after Harvest Scheduling
root.order.add_edge(Harvest_Scheduling, Post_Harvest)
root.order.add_edge(Harvest_Scheduling, Quality_Grading)

# Post-Harvest and Quality Grading both leading to Eco Packaging (means Eco Packaging waits for both)
root.order.add_edge(Post_Harvest, Eco_Packaging)
root.order.add_edge(Quality_Grading, Eco_Packaging)

root.order.add_edge(Eco_Packaging, Distribution_Track)

# Waste Recycling and Energy Management concurrent after Distribution Track
root.order.add_edge(Distribution_Track, Waste_Recycling)
root.order.add_edge(Distribution_Track, Energy_Management)

# Both must finish before Data Analysis
root.order.add_edge(Waste_Recycling, Data_Analysis)
root.order.add_edge(Energy_Management, Data_Analysis)