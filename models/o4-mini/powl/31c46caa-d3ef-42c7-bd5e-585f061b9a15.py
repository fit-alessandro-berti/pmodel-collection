# Generated from: 31c46caa-d3ef-42c7-bd5e-585f061b9a15.json
# Description: This process outlines the intricate steps involved in establishing a scalable urban vertical farming operation within a repurposed industrial building. It includes site evaluation, environmental control design, multi-tier crop selection, and integrated pest management strategies. The workflow further covers automation system installation, nutrient delivery calibration, energy optimization, data analytics deployment, and community engagement initiatives to ensure sustainable food production in dense metropolitan areas. Each activity focuses on balancing technological innovation with ecological considerations and regulatory compliance to create a self-sustaining urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions for each activity
site_survey      = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
layout_design    = Transition(label='Layout Design')
climate_setup    = Transition(label='Climate Setup')
lighting_install = Transition(label='Lighting Install')
irrigation_plan  = Transition(label='Irrigation Plan')
crop_selection   = Transition(label='Crop Selection')
regulation_check = Transition(label='Regulation Check')
seed_sowing      = Transition(label='Seed Sowing')
pest_control     = Transition(label='Pest Control')
nutrient_mix     = Transition(label='Nutrient Mix')
automation_cfg   = Transition(label='Automation Config')
energy_audit     = Transition(label='Energy Audit')
data_integration = Transition(label='Data Integration')
harvest_schedule = Transition(label='Harvest Schedule')
waste_recycling  = Transition(label='Waste Recycling')
community_out    = Transition(label='Community Outreach')

# Build the partial order model
root = StrictPartialOrder(nodes=[
    site_survey, structural_audit, layout_design,
    climate_setup, lighting_install, irrigation_plan,
    crop_selection, regulation_check, seed_sowing,
    pest_control, nutrient_mix, automation_cfg,
    energy_audit, data_integration, harvest_schedule,
    waste_recycling, community_out
])

# Site evaluation
root.order.add_edge(site_survey, layout_design)
root.order.add_edge(structural_audit, layout_design)

# Environmental control design after layout
for env in [climate_setup, lighting_install, irrigation_plan]:
    root.order.add_edge(layout_design, env)

# Crop selection after environmental setup
for env in [climate_setup, lighting_install, irrigation_plan]:
    root.order.add_edge(env, crop_selection)

# Regulatory check before sowing
root.order.add_edge(crop_selection, regulation_check)
root.order.add_edge(regulation_check, seed_sowing)

# Planting and management sequence
root.order.add_edge(seed_sowing, pest_control)
root.order.add_edge(pest_control, nutrient_mix)

# Systems installation and calibration
root.order.add_edge(nutrient_mix, automation_cfg)
root.order.add_edge(automation_cfg, energy_audit)
root.order.add_edge(energy_audit, data_integration)

# Harvest, recycling, and outreach
root.order.add_edge(data_integration, harvest_schedule)
root.order.add_edge(harvest_schedule, waste_recycling)
root.order.add_edge(waste_recycling, community_out)