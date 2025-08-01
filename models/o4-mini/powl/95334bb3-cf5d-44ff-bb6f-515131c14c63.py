# Generated from: 95334bb3-cf5d-44ff-bb6f-515131c14c63.json
# Description: This process outlines the complex steps involved in establishing a vertical farming system within an urban environment. It includes site analysis, modular infrastructure design, climatic control integration, nutrient cycle optimization, automated planting schedules, and energy-efficient lighting configurations. Additionally, it covers stakeholder coordination, regulatory compliance validation, waste recycling mechanisms, and data analytics for yield prediction, aiming to create a sustainable, high-yield urban agriculture solution that minimizes resource use and maximizes output within confined city spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
design_modules   = Transition(label='Design Modules')
stakeholder_meet = Transition(label='Stakeholder Meet')
permit_check     = Transition(label='Permit Check')
climate_setup    = Transition(label='Climate Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
plant_scheduling = Transition(label='Plant Scheduling')
light_config     = Transition(label='Light Config')
energy_audit     = Transition(label='Energy Audit')
waste_setup      = Transition(label='Waste Setup')
data_capture     = Transition(label='Data Capture')
yield_model      = Transition(label='Yield Model')
harvest_plan     = Transition(label='Harvest Plan')
maintenance_log  = Transition(label='Maintenance Log')
system_testing   = Transition(label='System Testing')
feedback_loop    = Transition(label='Feedback Loop')

# Loop: after testing, optionally do feedback and retest
loop = OperatorPOWL(operator=Operator.LOOP, children=[system_testing, feedback_loop])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_modules,
    stakeholder_meet, permit_check,
    climate_setup, nutrient_mix,
    plant_scheduling, light_config,
    energy_audit, waste_setup,
    data_capture, yield_model,
    harvest_plan, maintenance_log,
    loop
])

# Define control-flow dependencies
root.order.add_edge(site_survey, design_modules)
root.order.add_edge(design_modules, stakeholder_meet)
root.order.add_edge(design_modules, permit_check)
root.order.add_edge(stakeholder_meet, climate_setup)
root.order.add_edge(permit_check, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, plant_scheduling)
root.order.add_edge(nutrient_mix, light_config)
root.order.add_edge(plant_scheduling, energy_audit)
root.order.add_edge(light_config, energy_audit)
root.order.add_edge(energy_audit, waste_setup)
root.order.add_edge(waste_setup, data_capture)
root.order.add_edge(data_capture, yield_model)
root.order.add_edge(yield_model, harvest_plan)
root.order.add_edge(harvest_plan, maintenance_log)
root.order.add_edge(maintenance_log, loop)