# Generated from: 026c5224-a2fd-4c90-9cc5-d5f37a71b9b6.json
# Description: This process outlines the steps involved in establishing an urban vertical farm within a metropolitan environment. It begins with site analysis and zoning approval, followed by modular infrastructure assembly, hydroponic system integration, and automation setup. Subsequent phases include seed selection, nutrient calibration, climate control optimization, pest monitoring, and growth tracking. The process concludes with harvest scheduling, quality assessment, packaging design, and distribution network establishment, ensuring a sustainable and efficient urban farming operation that minimizes environmental impact while maximizing crop yield in limited spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_analysis = Transition(label='Site Analysis')
zoning_approval = Transition(label='Zoning Approval')
modular_assembly = Transition(label='Modular Assembly')
hydroponic_setup = Transition(label='Hydroponic Setup')
automation_install = Transition(label='Automation Install')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
climate_control = Transition(label='Climate Control')
pest_monitoring = Transition(label='Pest Monitoring')
growth_tracking = Transition(label='Growth Tracking')
harvest_schedule = Transition(label='Harvest Schedule')
quality_check = Transition(label='Quality Check')
packaging_design = Transition(label='Packaging Design')
distribution_setup = Transition(label='Distribution Setup')
waste_recycling = Transition(label='Waste Recycling')

# Model the process as a partial order with the logical ordering:
# Site Analysis --> Zoning Approval --> Modular Assembly --> Hydroponic Setup --> Automation Install
# Seed Selection --> Nutrient Mix --> Climate Control --> Pest Monitoring --> Growth Tracking
# Harvest Schedule --> Quality Check --> Packaging Design --> Distribution Setup
# Waste Recycling can be done concurrently after Packaging Design and Distribution Setup

# To keep the structure clear:
# Group phases:
# Phase 1: Site Analysis, Zoning Approval
# Phase 2: Modular Assembly, Hydroponic Setup, Automation Install
# Phase 3: Seed Selection, Nutrient Mix, Climate Control, Pest Monitoring, Growth Tracking
# Phase 4: Harvest Schedule, Quality Check, Packaging Design, Distribution Setup
# Waste Recycling (last, concurrent after Packaging Design and Distribution Setup)

nodes = [
    site_analysis, zoning_approval,
    modular_assembly, hydroponic_setup, automation_install,
    seed_selection, nutrient_mix, climate_control, pest_monitoring, growth_tracking,
    harvest_schedule, quality_check, packaging_design, distribution_setup,
    waste_recycling
]

root = StrictPartialOrder(nodes=nodes)

# Phase 1 order
root.order.add_edge(site_analysis, zoning_approval)

# Phase 2 order
root.order.add_edge(zoning_approval, modular_assembly)
root.order.add_edge(modular_assembly, hydroponic_setup)
root.order.add_edge(hydroponic_setup, automation_install)

# Phase 3 order
root.order.add_edge(automation_install, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_control)
root.order.add_edge(climate_control, pest_monitoring)
root.order.add_edge(pest_monitoring, growth_tracking)

# Phase 4 order
root.order.add_edge(growth_tracking, harvest_schedule)
root.order.add_edge(harvest_schedule, quality_check)
root.order.add_edge(quality_check, packaging_design)
root.order.add_edge(packaging_design, distribution_setup)

# Waste recycling concurrent after packaging_design and distribution_setup
# So add edges from both to waste_recycling, meaning waste_recycling can start after both are done
root.order.add_edge(packaging_design, waste_recycling)
root.order.add_edge(distribution_setup, waste_recycling)