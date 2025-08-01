# Generated from: 06a6d451-55d9-4153-88f0-f5d6c5231aa4.json
# Description: This process outlines the detailed steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site analysis, environmental impact assessment, modular system design, nutrient cycling setup, climate control calibration, and integration of IoT monitoring. Additionally, it covers workforce training, crop scheduling, pest management protocols, and supply chain coordination for distribution. The process ensures sustainable practices, energy efficiency, and maximized yield through innovative technology and precise resource management, accommodating urban space constraints while promoting local food production and reduced carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions with exact labels
site_survey = Transition(label='Site Survey')
impact_study = Transition(label='Impact Study')
system_design = Transition(label='System Design')
module_build = Transition(label='Module Build')
nutrient_prep = Transition(label='Nutrient Prep')
climate_setup = Transition(label='Climate Setup')
sensor_install = Transition(label='Sensor Install')
data_sync = Transition(label='Data Sync')
crop_planning = Transition(label='Crop Planning')
worker_train = Transition(label='Worker Train')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
water_cycle = Transition(label='Water Cycle')
harvest_plan = Transition(label='Harvest Plan')
distribution = Transition(label='Distribution')

# Build the POWL model according to the described process structure
# The process logically groups activities into phases
#
# Phase 1: Site Survey --> Impact Study (environmental impact)
# Phase 2: System Design with Module Build and Nutrient Prep,
#          and Climate Setup with Sensor Install and Data Sync
# Phase 3: Workforce training concurrently with Crop Planning and Pest Control
# Phase 4: Energy Audit and Water Cycle (sustainable practices)
# Phase 5: Harvest Plan followed by Distribution
#
# Some of these phases can run concurrently with appropriate partial orders.
# We combine phases in partial orders, with ordering to represent dependencies:

# Phase 1 order
phase1 = StrictPartialOrder(nodes=[site_survey, impact_study])
phase1.order.add_edge(site_survey, impact_study)

# Phase 2 partial order:
# System Design --> Module Build and Nutrient Prep (concurrent)
# Climate Setup --> Sensor Install --> Data Sync
# Assume system design precedes climate setup

module_build_nutrient = StrictPartialOrder(nodes=[module_build, nutrient_prep])
# module_build and nutrient_prep concurrent, no edges

sensor_chain = StrictPartialOrder(nodes=[sensor_install, data_sync])
sensor_chain.order.add_edge(sensor_install, data_sync)

climate_setup_group = StrictPartialOrder(nodes=[climate_setup, sensor_chain])
climate_setup_group.order.add_edge(climate_setup, sensor_chain)

phase2 = StrictPartialOrder(nodes=[system_design, module_build_nutrient, climate_setup_group])
phase2.order.add_edge(system_design, module_build_nutrient)
phase2.order.add_edge(system_design, climate_setup_group)
phase2.order.add_edge(module_build_nutrient, climate_setup_group)  # climate_setup after module_build and nutrient_prep

# Phase 3 - Workforce training, Crop Planning and Pest Control
worker_crop_pest = StrictPartialOrder(nodes=[worker_train, crop_planning, pest_control])
# All can be concurrent, no order edges

# Phase 4 - Energy Audit and Water Cycle (concurrent)
energy_water = StrictPartialOrder(nodes=[energy_audit, water_cycle])
# concurrent

# Phase 5 - Harvest Plan --> Distribution
harvest_dist = StrictPartialOrder(nodes=[harvest_plan, distribution])
harvest_dist.order.add_edge(harvest_plan, distribution)

# Put together phases with global ordering:
# phase1 --> phase2 --> phase3 --> phase4 --> phase5

root = StrictPartialOrder(
    nodes=[phase1, phase2, worker_crop_pest, energy_water, harvest_dist]
)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, worker_crop_pest)
root.order.add_edge(worker_crop_pest, energy_water)
root.order.add_edge(energy_water, harvest_dist)