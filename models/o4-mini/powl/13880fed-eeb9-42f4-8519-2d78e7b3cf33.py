# Generated from: 13880fed-eeb9-42f4-8519-2d78e7b3cf33.json
# Description: This process involves establishing a multi-tiered vertical farm within an urban environment, integrating advanced hydroponic systems, renewable energy sources, and AI-driven environmental controls. It requires site assessment, modular structure installation, nutrient solution formulation, crop selection tailored to microclimates, and continuous monitoring for optimal growth. Post-harvest activities include automated sorting, packaging, and distribution logistics coordinated with local markets. The process ensures sustainability by recycling water and organic waste while adapting dynamically to urban constraints and demand fluctuations, ultimately producing fresh produce with minimal carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
permit_acquire  = Transition(label='Permit Acquire')
structure_build = Transition(label='Structure Build')
system_install  = Transition(label='System Install')
nutrient_mix    = Transition(label='Nutrient Mix')
crop_select     = Transition(label='Crop Select')
seed_plant      = Transition(label='Seed Plant')
environment_tune= Transition(label='Environment Tune')
growth_monitor  = Transition(label='Growth Monitor')
pest_control    = Transition(label='Pest Control')
harvest_crop    = Transition(label='Harvest Crop')
sort_package    = Transition(label='Sort Package')
market_coord    = Transition(label='Market Coordinate')
waste_recycle   = Transition(label='Waste Recycle')
energy_manage   = Transition(label='Energy Manage')
data_analyze    = Transition(label='Data Analyze')

# Define the loop for the growth cycle: monitor -> optionally control pests -> repeat
growth_cycle = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, pest_control]
)

# Build the strict partial order for the overall process
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, permit_acquire,
    structure_build, system_install, nutrient_mix,
    crop_select, seed_plant, environment_tune,
    growth_cycle, harvest_crop, sort_package,
    market_coord, waste_recycle, energy_manage,
    data_analyze
])

# Linear setup steps
root.order.add_edge(site_survey,    design_layout)
root.order.add_edge(design_layout,  permit_acquire)
root.order.add_edge(permit_acquire, structure_build)
root.order.add_edge(structure_build,system_install)
root.order.add_edge(system_install, nutrient_mix)
root.order.add_edge(nutrient_mix,   crop_select)
root.order.add_edge(crop_select,    seed_plant)
root.order.add_edge(seed_plant,     environment_tune)

# Enter the growth-and-pest-control loop
root.order.add_edge(environment_tune, growth_cycle)

# After exiting the loop, harvest and package
root.order.add_edge(growth_cycle, harvest_crop)
root.order.add_edge(harvest_crop, sort_package)
root.order.add_edge(sort_package, market_coord)

# Sustainability and analytics run in parallel after harvest
root.order.add_edge(harvest_crop, waste_recycle)
root.order.add_edge(harvest_crop, energy_manage)
root.order.add_edge(harvest_crop, data_analyze)