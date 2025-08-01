# Generated from: 400cc8be-6a9d-4688-995b-6dc5c5e90a4d.json
# Description: This process outlines the intricate steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It includes site assessment, modular system design, environmental control calibration, crop selection based on microclimates, nutrient cycling optimization, automated harvesting integration, waste repurposing, and community engagement to ensure sustainability and scalability in constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_build = Transition(label='System Build')
climate_setup = Transition(label='Climate Setup')
crop_select = Transition(label='Crop Select')
nutrient_mix = Transition(label='Nutrient Mix')
water_cycle = Transition(label='Water Cycle')
lighting_adjust = Transition(label='Lighting Adjust')
sensor_deploy = Transition(label='Sensor Deploy')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
waste_process = Transition(label='Waste Process')
data_analyze = Transition(label='Data Analyze')
community_meet = Transition(label='Community Meet')
scale_review = Transition(label='Scale Review')

# Build the partial order according to the process description structure:

# 1. Site Survey --> Design Layout --> System Build
# 2. After System Build: Environmental Control Calibration and Crop Selection based on microclimates

# Environmental Control Calibration includes:
# Climate Setup, Nutrient Mix, Water Cycle, Lighting Adjust, Sensor Deploy
# Assume these 5 are concurrent (no order between them) after System Build

# Crop Selection is after or concurrent with environmental control calibration?
# Description says "crop selection based on microclimates" - likely depends on climate setup, so
# Crop Select depends on Climate Setup

# Nutrient cycling optimization involves Nutrient Mix and Water Cycle (and maybe Lighting Adjust?)
# We'll assume Nutrient Mix and Water Cycle are done before Growth Monitor, and Lighting Adjust and Sensor Deploy separate but before Growth Monitor.

# Growth Monitor happens after environmental setup and crop select
# Pest Control presumably after growth monitor
# Harvest Plan after Pest Control
# Automated harvesting integration is not an activity listed separately, so Harvest Plan models it
# Waste repurposing = Waste Process after Harvest Plan
# Data Analyze after Waste Process
# Community Engage (Community Meet) possibly concurrent with or after Data Analyze
# Scale Review last

# So overall order (simplified):

# Site Survey --> Design Layout --> System Build -->
#   - Climate Setup
#   - Nutrient Mix
#   - Water Cycle
#   - Lighting Adjust
#   - Sensor Deploy
#
# Crop Select depends on Climate Setup
# Growth Monitor after Nutrient Mix, Water Cycle, Lighting Adjust, Sensor Deploy, and Crop Select
# Pest Control after Growth Monitor
# Harvest Plan after Pest Control
# Waste Process after Harvest Plan
# Data Analyze after Waste Process
# Community Meet after Data Analyze
# Scale Review after Community Meet

# Create partial order nodes list including all activities.
nodes = [
    site_survey,
    design_layout,
    system_build,
    climate_setup,
    nutrient_mix,
    water_cycle,
    lighting_adjust,
    sensor_deploy,
    crop_select,
    growth_monitor,
    pest_control,
    harvest_plan,
    waste_process,
    data_analyze,
    community_meet,
    scale_review
]

root = StrictPartialOrder(nodes=nodes)

# Add edges according to the dependencies:

# Site Survey --> Design Layout --> System Build
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_build)

# System Build --> {Climate Setup, Nutrient Mix, Water Cycle, Lighting Adjust, Sensor Deploy}
root.order.add_edge(system_build, climate_setup)
root.order.add_edge(system_build, nutrient_mix)
root.order.add_edge(system_build, water_cycle)
root.order.add_edge(system_build, lighting_adjust)
root.order.add_edge(system_build, sensor_deploy)

# Climate Setup --> Crop Select
root.order.add_edge(climate_setup, crop_select)

# Crop Select and all environmental activities before Growth Monitor
# So Growth Monitor depends on: nutrient_mix, water_cycle, lighting_adjust, sensor_deploy, crop_select
root.order.add_edge(nutrient_mix, growth_monitor)
root.order.add_edge(water_cycle, growth_monitor)
root.order.add_edge(lighting_adjust, growth_monitor)
root.order.add_edge(sensor_deploy, growth_monitor)
root.order.add_edge(crop_select, growth_monitor)

# Growth Monitor --> Pest Control --> Harvest Plan --> Waste Process --> Data Analyze --> Community Meet --> Scale Review
root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(pest_control, harvest_plan)
root.order.add_edge(harvest_plan, waste_process)
root.order.add_edge(waste_process, data_analyze)
root.order.add_edge(data_analyze, community_meet)
root.order.add_edge(community_meet, scale_review)