# Generated from: 36a7803e-5cce-43a7-a81d-a5050b5230c2.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site assessment, modular rack installation, hydroponic system configuration, environmental control calibration, crop selection based on urban climate, seedling propagation, nutrient solution formulation, automated monitoring integration, pest management planning, energy optimization, harvesting scheduling, post-harvest processing, packaging design, distribution logistics coordination, and sustainability compliance verification to ensure efficient production of fresh produce in a city environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_assess   = Transition(label='Site Assess')
rack_install  = Transition(label='Rack Install')
hydro_setup   = Transition(label='Hydro Setup')
env_control   = Transition(label='Env Control')
crop_select   = Transition(label='Crop Select')
seedling_prep = Transition(label='Seedling Prep')
nutrient_mix  = Transition(label='Nutrient Mix')
automation_set= Transition(label='Automation Set')
pest_plan     = Transition(label='Pest Plan')
energy_audit  = Transition(label='Energy Audit')
harvest_plan  = Transition(label='Harvest Plan')
post_harvest  = Transition(label='Post Harvest')
pack_design   = Transition(label='Pack Design')
logistics_map = Transition(label='Logistics Map')
sustain_verify= Transition(label='Sustain Verify')

# Build a sequential partial order for the process
nodes = [
    site_assess, rack_install, hydro_setup, env_control, crop_select,
    seedling_prep, nutrient_mix, automation_set, pest_plan, energy_audit,
    harvest_plan, post_harvest, pack_design, logistics_map, sustain_verify
]
root = StrictPartialOrder(nodes=nodes)

# Add ordering edges to represent the workflow sequence
for src, tgt in zip(nodes, nodes[1:]):
    root.order.add_edge(src, tgt)