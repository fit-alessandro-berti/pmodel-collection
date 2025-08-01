# Generated from: 40b2e441-0b67-4a24-9e17-2d521d0867e9.json
# Description: This process outlines the end-to-end establishment of an urban vertical farm in a densely populated city environment. It involves site analysis, modular structure design, hydroponic system installation, climate control calibration, crop selection, seedling propagation, nutrient solution preparation, automated monitoring setup, pest management integration, waste recycling, harvest scheduling, quality assessment, packaging design, distribution logistics, and community engagement to ensure sustainable urban agriculture with optimized yield, minimal environmental impact, and strong local support.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_analysis   = Transition(label='Site Analysis')
structure_design= Transition(label='Structure Design')
system_install  = Transition(label='System Install')
climate_setup   = Transition(label='Climate Setup')
crop_select     = Transition(label='Crop Select')
seedling_grow   = Transition(label='Seedling Grow')
nutrient_mix    = Transition(label='Nutrient Mix')
sensor_deploy   = Transition(label='Sensor Deploy')
pest_control    = Transition(label='Pest Control')
waste_process   = Transition(label='Waste Process')
harvest_plan    = Transition(label='Harvest Plan')
quality_check   = Transition(label='Quality Check')
packaging_dev   = Transition(label='Packaging Dev')
logistics_plan  = Transition(label='Logistics Plan')
community_meet  = Transition(label='Community Meet')

# Create a partial‐order of all activities in sequence
root = StrictPartialOrder(nodes=[
    site_analysis,
    structure_design,
    system_install,
    climate_setup,
    crop_select,
    seedling_grow,
    nutrient_mix,
    sensor_deploy,
    pest_control,
    waste_process,
    harvest_plan,
    quality_check,
    packaging_dev,
    logistics_plan,
    community_meet
])

# Add the ordering edges (strict sequence)
root.order.add_edge(site_analysis,   structure_design)
root.order.add_edge(structure_design,system_install)
root.order.add_edge(system_install,  climate_setup)
root.order.add_edge(climate_setup,   crop_select)
root.order.add_edge(crop_select,     seedling_grow)
root.order.add_edge(seedling_grow,   nutrient_mix)
root.order.add_edge(nutrient_mix,    sensor_deploy)
root.order.add_edge(sensor_deploy,   pest_control)
root.order.add_edge(pest_control,    waste_process)
root.order.add_edge(waste_process,   harvest_plan)
root.order.add_edge(harvest_plan,    quality_check)
root.order.add_edge(quality_check,   packaging_dev)
root.order.add_edge(packaging_dev,   logistics_plan)
root.order.add_edge(logistics_plan,  community_meet)