# Generated from: c2779bf3-4a1d-4109-8cf5-5b601bab77f0.json
# Description: This process involves the comprehensive planning, design, and implementation of an urban vertical farming system within limited city spaces. It includes site analysis, modular infrastructure development, environmental controls installation, crop selection based on local demand, continuous monitoring of growth conditions, integration with smart irrigation systems, and logistics for distribution. Unique challenges such as energy optimization, urban zoning regulations, and waste recycling are addressed to ensure sustainable production. The process concludes with system calibration and stakeholder training for operational efficiency in an atypical urban agricultural environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities as labeled transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permit_acquire = Transition(label='Permit Acquire')
module_fabricate = Transition(label='Module Fabricate')
install_lighting = Transition(label='Install Lighting')
setup_sensors = Transition(label='Setup Sensors')
select_crops = Transition(label='Select Crops')
seed_planting = Transition(label='Seed Planting')
irrigation_setup = Transition(label='Irrigation Setup')
configure_controls = Transition(label='Configure Controls')
nutrient_mix = Transition(label='Nutrient Mix')
growth_monitor = Transition(label='Growth Monitor')
waste_manage = Transition(label='Waste Manage')
energy_audit = Transition(label='Energy Audit')
staff_training = Transition(label='Staff Training')
harvest_plan = Transition(label='Harvest Plan')
dispatch_prep = Transition(label='Dispatch Prep')

# Planning phase: site survey, design layout, permit acquire (sequential)
planning = StrictPartialOrder(nodes=[site_survey, design_layout, permit_acquire])
planning.order.add_edge(site_survey, design_layout)
planning.order.add_edge(design_layout, permit_acquire)

# Modular infrastructure development: module fabricate, install lighting, setup sensors (sequential)
modular_infra = StrictPartialOrder(nodes=[module_fabricate, install_lighting, setup_sensors])
modular_infra.order.add_edge(module_fabricate, install_lighting)
modular_infra.order.add_edge(install_lighting, setup_sensors)

# Crop preparation: select crops, seed planting (sequential)
crop_prep = StrictPartialOrder(nodes=[select_crops, seed_planting])
crop_prep.order.add_edge(select_crops, seed_planting)

# Controls setup: irrigation setup, configure controls, nutrient mix (sequential)
controls_setup = StrictPartialOrder(nodes=[irrigation_setup, configure_controls, nutrient_mix])
controls_setup.order.add_edge(irrigation_setup, configure_controls)
controls_setup.order.add_edge(configure_controls, nutrient_mix)

# Monitoring phase: growth monitor (may loop with adjustments)
growth_monitoring = growth_monitor

# Environmental and sustainability considerations (energy audit, waste manage) can be concurrent after setup
environmental = StrictPartialOrder(nodes=[energy_audit, waste_manage])

# Staff training and harvest/distribution planning concurrent but after monitoring 
training_and_final = StrictPartialOrder(nodes=[staff_training, harvest_plan, dispatch_prep])
training_and_final.order.add_edge(harvest_plan, dispatch_prep)  # harvest plan before dispatch prep

# Combine modular infrastructure and crop prep and controls setup in parallel (no order between them)
setup_parallel = StrictPartialOrder(nodes=[modular_infra, crop_prep, controls_setup])

# Add ordering: planning -> setup_parallel
root = StrictPartialOrder(nodes=[planning, setup_parallel, environmental, growth_monitoring, training_and_final])

# planning before setup_parallel
root.order.add_edge(planning, setup_parallel)
# setup_parallel before environmental and growth_monitoring
root.order.add_edge(setup_parallel, environmental)
root.order.add_edge(setup_parallel, growth_monitoring)
# environmental and growth_monitoring before training_and_final
root.order.add_edge(environmental, training_and_final)
root.order.add_edge(growth_monitoring, training_and_final)