# Generated from: cb0b361c-172a-4785-a11d-5afec4e4c726.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed warehouse. It involves site analysis, structural modifications, installation of hydroponic systems, climate control integration, and automation setup. The process also covers nutrient solution formulation, seed selection, growth monitoring, pest management, and harvesting protocols. Additionally, it includes packaging, distribution logistics, and sustainability reporting to ensure environmental compliance and economic viability in an urban agriculture context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
site_survey      = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
layout_design    = Transition(label='Layout Design')
system_install   = Transition(label='System Install')
climate_setup    = Transition(label='Climate Setup')
water_testing    = Transition(label='Water Testing')
nutrient_mix     = Transition(label='Nutrient Mix')
seed_selection   = Transition(label='Seed Selection')
planting_prep    = Transition(label='Planting Prep')
growth_monitor   = Transition(label='Growth Monitor')
pest_inspect     = Transition(label='Pest Inspect')
harvest_plan     = Transition(label='Harvest Plan')
packaging_prep   = Transition(label='Packaging Prep')
distribution     = Transition(label='Distribution')
sustainability   = Transition(label='Sustainability')

# Build a strictly ordered workflow
nodes = [
    site_survey,
    structural_audit,
    layout_design,
    system_install,
    climate_setup,
    water_testing,
    nutrient_mix,
    seed_selection,
    planting_prep,
    growth_monitor,
    pest_inspect,
    harvest_plan,
    packaging_prep,
    distribution,
    sustainability
]

root = StrictPartialOrder(nodes=nodes)

# Add the sequential dependencies
for src, tgt in zip(nodes, nodes[1:]):
    root.order.add_edge(src, tgt)