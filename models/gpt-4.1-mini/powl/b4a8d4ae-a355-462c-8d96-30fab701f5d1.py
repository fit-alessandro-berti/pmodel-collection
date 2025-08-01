# Generated from: b4a8d4ae-a355-462c-8d96-30fab701f5d1.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming system within a metropolitan environment. It involves site analysis, modular infrastructure design, installation of hydroponic systems, integration of IoT sensors for environmental control, selection of crop varieties optimized for vertical growth, nutrient solution formulation, automated planting, continuous monitoring of plant health using AI-driven analytics, pest management with eco-friendly agents, energy management via renewable sources, waste recycling integration, harvest scheduling, packaging customization, and distribution logistics tailored for local markets. Each phase ensures sustainability, scalability, and high yield within constrained urban spaces, balancing technology with ecological considerations to create a cutting-edge food production ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
module_build = Transition(label='Module Build')
hydroponic_install = Transition(label='Hydroponic Install')
sensor_setup = Transition(label='Sensor Setup')
crop_select = Transition(label='Crop Select')
nutrient_mix = Transition(label='Nutrient Mix')
planting_auto = Transition(label='Planting Auto')
health_monitor = Transition(label='Health Monitor')
pest_control = Transition(label='Pest Control')
energy_manage = Transition(label='Energy Manage')
waste_process = Transition(label='Waste Process')
harvest_plan = Transition(label='Harvest Plan')
packaging_dev = Transition(label='Packaging Dev')
local_dispatch = Transition(label='Local Dispatch')

# Construct the partial order as described in the process

root = StrictPartialOrder(nodes=[
    site_survey, design_layout, module_build, hydroponic_install,
    sensor_setup, crop_select, nutrient_mix, planting_auto,
    health_monitor, pest_control, energy_manage, waste_process,
    harvest_plan, packaging_dev, local_dispatch
])

# Add edges between activities following the described sequence and causalities:
# The steps have a natural order with some concurrency allowed:
# 1. Site Survey --> Design Layout
root.order.add_edge(site_survey, design_layout)

# 2. Design Layout --> Module Build (depends on design)
root.order.add_edge(design_layout, module_build)

# 3. Module Build --> Hydroponic Install (must build before install)
root.order.add_edge(module_build, hydroponic_install)

# 4. Hydroponic Install --> Sensor Setup (install system before setting sensors)
root.order.add_edge(hydroponic_install, sensor_setup)

# 5. Crop Select and Nutrient Mix can be done after design layout concurrently
root.order.add_edge(design_layout, crop_select)
root.order.add_edge(design_layout, nutrient_mix)

# 6. Planting Auto depends on Hydroponic Install, Crop Select, Nutrient Mix
root.order.add_edge(hydroponic_install, planting_auto)
root.order.add_edge(crop_select, planting_auto)
root.order.add_edge(nutrient_mix, planting_auto)

# 7. Health Monitor can run concurrently after Planting Auto (continuous monitoring)
root.order.add_edge(planting_auto, health_monitor)

# 8. Pest Control can run concurrently after Planting Auto as well
root.order.add_edge(planting_auto, pest_control)

# 9. Energy Manage and Waste Process run concurrently after Module Build (infrastructure ready)
root.order.add_edge(module_build, energy_manage)
root.order.add_edge(module_build, waste_process)

# 10. Harvest Plan after Planting Auto and Pest Control (need plants grown and managed)
root.order.add_edge(planting_auto, harvest_plan)
root.order.add_edge(pest_control, harvest_plan)

# 11. Packaging Dev after Harvest Plan (design packaging for harvest)
root.order.add_edge(harvest_plan, packaging_dev)

# 12. Local Dispatch after Packaging Dev and Energy Manage & Waste Process (final logistics)
root.order.add_edge(packaging_dev, local_dispatch)
root.order.add_edge(energy_manage, local_dispatch)
root.order.add_edge(waste_process, local_dispatch)