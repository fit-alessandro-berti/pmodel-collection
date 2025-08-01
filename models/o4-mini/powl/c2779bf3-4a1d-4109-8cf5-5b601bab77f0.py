# Generated from: c2779bf3-4a1d-4109-8cf5-5b601bab77f0.json
# Description: This process involves the comprehensive planning, design, and implementation of an urban vertical farming system within limited city spaces. It includes site analysis, modular infrastructure development, environmental controls installation, crop selection based on local demand, continuous monitoring of growth conditions, integration with smart irrigation systems, and logistics for distribution. Unique challenges such as energy optimization, urban zoning regulations, and waste recycling are addressed to ensure sustainable production. The process concludes with system calibration and stakeholder training for operational efficiency in an atypical urban agricultural environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey    = Transition(label='Site Survey')
design_layout  = Transition(label='Design Layout')
permit_acquire = Transition(label='Permit Acquire')
module_fab     = Transition(label='Module Fabricate')
install_light  = Transition(label='Install Lighting')
setup_sensors  = Transition(label='Setup Sensors')
irrigation     = Transition(label='Irrigation Setup')
configure_ctrl = Transition(label='Configure Controls')
select_crops   = Transition(label='Select Crops')
seed_planting  = Transition(label='Seed Planting')
nutrient_mix   = Transition(label='Nutrient Mix')
growth_mon     = Transition(label='Growth Monitor')
waste_manage   = Transition(label='Waste Manage')
energy_audit   = Transition(label='Energy Audit')
harvest_plan   = Transition(label='Harvest Plan')
dispatch_prep  = Transition(label='Dispatch Prep')
staff_training = Transition(label='Staff Training')

# Define loop body for ongoing post‐planting tasks (nutrient mix, waste management, energy audits)
loop_body = StrictPartialOrder(nodes=[nutrient_mix, waste_manage, energy_audit])
# build loop: growth monitor is the A part, loop_body is the B part
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_mon, loop_body])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    permit_acquire,
    module_fab,
    install_light,
    setup_sensors,
    irrigation,
    configure_ctrl,
    select_crops,
    seed_planting,
    monitor_loop,
    harvest_plan,
    dispatch_prep,
    staff_training
])

# Add sequencing edges
o = root.order
o.add_edge(site_survey, design_layout)
o.add_edge(design_layout, permit_acquire)
o.add_edge(permit_acquire, module_fab)
o.add_edge(module_fab, install_light)
o.add_edge(install_light, setup_sensors)
o.add_edge(setup_sensors, irrigation)
o.add_edge(irrigation, configure_ctrl)
o.add_edge(configure_ctrl, select_crops)
o.add_edge(select_crops, seed_planting)
o.add_edge(seed_planting, monitor_loop)
o.add_edge(monitor_loop, harvest_plan)
o.add_edge(harvest_plan, dispatch_prep)
o.add_edge(dispatch_prep, staff_training)