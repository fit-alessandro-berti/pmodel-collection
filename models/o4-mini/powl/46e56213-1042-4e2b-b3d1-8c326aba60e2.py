# Generated from: 46e56213-1042-4e2b-b3d1-8c326aba60e2.json
# Description: This process outlines the complex and atypical steps involved in establishing a sustainable urban rooftop farm. It begins with site analysis to assess structural integrity and sunlight exposure, followed by securing permits and community engagement to ensure regulatory compliance and local support. Next, soil testing and hydroponic system design are tailored to urban constraints. Procurement involves sourcing lightweight, eco-friendly materials and heirloom seeds. Installation includes modular bed assembly, irrigation setup, and sensor integration for climate control. Subsequent activities focus on planting, pest management using organic methods, and continuous monitoring via IoT devices. Harvesting is scheduled in phases to optimize yield, followed by distribution through local markets and restaurants. The process concludes with seasonal evaluation and planning for crop rotation to maintain soil health and sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define the activities
site_analysis     = Transition(label='Site Analysis')
permit_filing     = Transition(label='Permit Filing')
community_meet    = Transition(label='Community Meet')
soil_testing      = Transition(label='Soil Testing')
system_design     = Transition(label='System Design')
material_sourcing = Transition(label='Material Sourcing')
seed_selection    = Transition(label='Seed Selection')
bed_assembly      = Transition(label='Bed Assembly')
irrigation_setup  = Transition(label='Irrigation Setup')
sensor_install    = Transition(label='Sensor Install')
planting_phase    = Transition(label='Planting Phase')
pest_control      = Transition(label='Pest Control')
climate_monitor   = Transition(label='Climate Monitor')
harvesting_plan   = Transition(label='Harvesting Plan')
yield_distribution= Transition(label='Yield Distribution')
season_review     = Transition(label='Season Review')
crop_rotation     = Transition(label='Crop Rotation')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    site_analysis, permit_filing, community_meet,
    soil_testing, system_design,
    material_sourcing, seed_selection,
    bed_assembly, irrigation_setup, sensor_install,
    planting_phase, pest_control, climate_monitor,
    harvesting_plan, yield_distribution,
    season_review, crop_rotation
])

# Sequence: Site Analysis → Permit Filing → Community Meet
root.order.add_edge(site_analysis, permit_filing)
root.order.add_edge(permit_filing, community_meet)

# After community meet: Soil Testing and System Design in parallel
root.order.add_edge(community_meet, soil_testing)
root.order.add_edge(community_meet, system_design)

# Procurement (Material Sourcing & Seed Selection) after both Soil Testing and System Design
for pred in (soil_testing, system_design):
    root.order.add_edge(pred, material_sourcing)
    root.order.add_edge(pred, seed_selection)

# Installation (Bed Assembly, Irrigation Setup, Sensor Install) after both procurement tasks
for proc in (material_sourcing, seed_selection):
    root.order.add_edge(proc, bed_assembly)
    root.order.add_edge(proc, irrigation_setup)
    root.order.add_edge(proc, sensor_install)

# Planting Phase after installation completes
for inst in (bed_assembly, irrigation_setup, sensor_install):
    root.order.add_edge(inst, planting_phase)

# Pest Control & Climate Monitoring in parallel after planting
root.order.add_edge(planting_phase, pest_control)
root.order.add_edge(planting_phase, climate_monitor)

# Harvesting Plan after both Pest Control and Climate Monitoring
root.order.add_edge(pest_control, harvesting_plan)
root.order.add_edge(climate_monitor, harvesting_plan)

# Then Yield Distribution → Season Review → Crop Rotation
root.order.add_edge(harvesting_plan, yield_distribution)
root.order.add_edge(yield_distribution, season_review)
root.order.add_edge(season_review, crop_rotation)