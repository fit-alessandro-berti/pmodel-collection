# Generated from: 8770e290-bec0-4e0b-bc0a-8eaa5b352d04.json
# Description: This process outlines the establishment of a sustainable urban vertical farm in a multi-story building. It begins with site analysis and structural assessment, followed by environmental impact evaluation. Next, the process involves modular farming unit design, nutrient solution formulation, and automated climate control setup. Concurrently, seed selection and germination protocols are developed. The installation phase includes lighting system integration, hydroponic channel assembly, and sensor network deployment for real-time monitoring. Once operational, the process continues with data-driven growth optimization, pest management using biocontrol agents, and harvest scheduling. Finally, produce packaging and distribution logistics are coordinated with local markets to ensure freshness and minimal environmental footprint, closing the loop with waste recycling and energy efficiency audits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions for each activity
site_analysis    = Transition(label='Site Analysis')
structural_check = Transition(label='Structural Check')
impact_study     = Transition(label='Impact Study')
unit_design      = Transition(label='Unit Design')
nutrient_mix     = Transition(label='Nutrient Mix')
climate_setup    = Transition(label='Climate Setup')
seed_selection   = Transition(label='Seed Selection')
germination_prep = Transition(label='Germination Prep')
lighting_install = Transition(label='Lighting Install')
channel_assembly = Transition(label='Channel Assembly')
sensor_deploy    = Transition(label='Sensor Deploy')
growth_optimize  = Transition(label='Growth Optimize')
pest_control     = Transition(label='Pest Control')
harvest_plan     = Transition(label='Harvest Plan')
packaging        = Transition(label='Packaging')
distribution     = Transition(label='Distribution')
waste_audit      = Transition(label='Waste Audit')
energy_review    = Transition(label='Energy Review')

# Create the root partial‐order model
root = StrictPartialOrder(nodes=[
    site_analysis,
    structural_check,
    impact_study,
    unit_design,
    nutrient_mix,
    climate_setup,
    seed_selection,
    germination_prep,
    lighting_install,
    channel_assembly,
    sensor_deploy,
    growth_optimize,
    pest_control,
    harvest_plan,
    packaging,
    distribution,
    waste_audit,
    energy_review
])

# Define the control‐flow dependencies
root.order.add_edge(site_analysis, structural_check)
root.order.add_edge(structural_check, impact_study)

# From impact study two parallel branches
root.order.add_edge(impact_study, unit_design)
root.order.add_edge(impact_study, seed_selection)

# Branch 1: design → nutrient → climate
root.order.add_edge(unit_design, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_setup)

# Branch 2: seed selection → germination
root.order.add_edge(seed_selection, germination_prep)

# Synchronize before installation
root.order.add_edge(climate_setup, lighting_install)
root.order.add_edge(germination_prep, lighting_install)

# Installation sequence
root.order.add_edge(lighting_install, channel_assembly)
root.order.add_edge(channel_assembly, sensor_deploy)

# Post‐installation operations
root.order.add_edge(sensor_deploy, growth_optimize)
root.order.add_edge(growth_optimize, pest_control)
root.order.add_edge(pest_control, harvest_plan)

# Final packaging and closing loop
root.order.add_edge(harvest_plan, packaging)
root.order.add_edge(packaging, distribution)
root.order.add_edge(distribution, waste_audit)
root.order.add_edge(waste_audit, energy_review)