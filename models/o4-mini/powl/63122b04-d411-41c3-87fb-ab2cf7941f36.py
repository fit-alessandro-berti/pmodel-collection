# Generated from: 63122b04-d411-41c3-87fb-ab2cf7941f36.json
# Description: This process outlines the comprehensive cycle of urban vertical farming, integrating advanced technologies and sustainability principles. It begins with site analysis and climate mapping to optimize microclimate conditions. Seed selection follows, emphasizing heirloom and genetically optimized varieties. Automated planting is performed using robotics, ensuring precision and efficiency. Nutrient monitoring leverages IoT sensors to maintain optimal hydroponic solutions. Pollination is artificially induced via drone deployment in enclosed environments. Growth tracking uses AI-powered imaging for real-time health assessment. Pest control employs biocontrol agents introduced through targeted release systems. Harvest scheduling adapts dynamically based on crop maturity data. Post-harvest handling includes automated sorting and quality grading using machine vision. Packaging is eco-friendly with biodegradable materials custom-fit by automated machinery. Distribution logistics use blockchain for traceability and smart contracts to ensure timely delivery. Waste recycling repurposes organic residues into biofertilizers. Energy management optimizes renewable inputs and storage. Finally, data analysis feeds back into process improvements, closing the cycle for sustainable urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activity nodes
site_analysis       = Transition(label='Site Analysis')
climate_mapping     = Transition(label='Climate Mapping')
seed_selection      = Transition(label='Seed Selection')
automated_planting  = Transition(label='Automated Planting')
nutrient_monitoring = Transition(label='Nutrient Monitoring')
pollination_drone   = Transition(label='Pollination Drone')
growth_tracking     = Transition(label='Growth Tracking')
pest_control        = Transition(label='Pest Control')
harvest_scheduling  = Transition(label='Harvest Scheduling')
post_harvest        = Transition(label='Post-Harvest')
quality_grading     = Transition(label='Quality Grading')
eco_packaging       = Transition(label='Eco Packaging')
distribution_track  = Transition(label='Distribution Track')
waste_recycling     = Transition(label='Waste Recycling')
energy_management   = Transition(label='Energy Management')
data_analysis       = Transition(label='Data Analysis')

# Build the partial order model
root = StrictPartialOrder(nodes=[
    site_analysis, climate_mapping, seed_selection,
    automated_planting, nutrient_monitoring, pollination_drone,
    growth_tracking, pest_control, harvest_scheduling,
    post_harvest, quality_grading, eco_packaging,
    distribution_track, waste_recycling, energy_management,
    data_analysis
])

# Specify the control‐flow dependencies
root.order.add_edge(site_analysis,       seed_selection)
root.order.add_edge(climate_mapping,     seed_selection)
root.order.add_edge(seed_selection,      automated_planting)
root.order.add_edge(automated_planting,  nutrient_monitoring)
root.order.add_edge(nutrient_monitoring, pollination_drone)
root.order.add_edge(pollination_drone,   growth_tracking)
root.order.add_edge(growth_tracking,     pest_control)
root.order.add_edge(pest_control,        harvest_scheduling)
root.order.add_edge(harvest_scheduling,  post_harvest)
root.order.add_edge(post_harvest,        quality_grading)
root.order.add_edge(quality_grading,     eco_packaging)
root.order.add_edge(eco_packaging,       distribution_track)
root.order.add_edge(distribution_track,  waste_recycling)
root.order.add_edge(waste_recycling,     energy_management)
root.order.add_edge(energy_management,   data_analysis)