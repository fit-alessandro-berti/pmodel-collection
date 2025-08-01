# Generated from: dc74f954-b514-49a9-88fa-4de75b5ce33b.json
# Description: This process outlines the complex establishment of an urban vertical farming facility designed to optimize limited city space for high-yield crop production. It involves site analysis, modular infrastructure assembly, environmental system calibration, automated nutrient delivery, integrated pest management, and data-driven crop monitoring. The process demands coordination between agronomists, engineers, and IT specialists to ensure sustainable operations while maximizing output and minimizing resource consumption within a controlled urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
site_survey       = Transition(label='Site Survey')
design_layout     = Transition(label='Design Layout')
permit_filing     = Transition(label='Permit Filing')
module_build      = Transition(label='Module Build')
system_install    = Transition(label='System Install')
climate_setup     = Transition(label='Climate Setup')
lighting_configure = Transition(label='Lighting Configure')
irrigation_setup  = Transition(label='Irrigation Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
pest_check        = Transition(label='Pest Check')
sensor_calibrate  = Transition(label='Sensor Calibrate')
data_integration  = Transition(label='Data Integration')
crop_planting     = Transition(label='Crop Planting')
growth_monitor    = Transition(label='Growth Monitor')
yield_analyze     = Transition(label='Yield Analyze')
waste_manage      = Transition(label='Waste Manage')
energy_audit      = Transition(label='Energy Audit')

# Loop for nutrient mixing and pest checking (mix -> (exit | check -> mix)*)
mix_check_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[nutrient_mix, pest_check]
)

# Build the root partial order with the loop as a single node
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    permit_filing,
    module_build,
    system_install,
    climate_setup,
    lighting_configure,
    irrigation_setup,
    mix_check_loop,
    sensor_calibrate,
    data_integration,
    crop_planting,
    growth_monitor,
    yield_analyze,
    waste_manage,
    energy_audit
])

# Define the control-flow/order relations
root.order.add_edge(site_survey,       design_layout)
root.order.add_edge(design_layout,     permit_filing)
root.order.add_edge(permit_filing,     module_build)
root.order.add_edge(module_build,      system_install)
root.order.add_edge(system_install,    climate_setup)
root.order.add_edge(climate_setup,     lighting_configure)
root.order.add_edge(climate_setup,     irrigation_setup)
# Both environment setups must finish before nutrient/pest loop starts
root.order.add_edge(lighting_configure, mix_check_loop)
root.order.add_edge(irrigation_setup,   mix_check_loop)
# After the mix/check loop, proceed to sensor calibration and beyond
root.order.add_edge(mix_check_loop,     sensor_calibrate)
root.order.add_edge(sensor_calibrate,   data_integration)
root.order.add_edge(data_integration,   crop_planting)
root.order.add_edge(crop_planting,      growth_monitor)
root.order.add_edge(growth_monitor,     yield_analyze)
# Final cleanup/audit tasks in parallel after yield analysis
root.order.add_edge(yield_analyze,      waste_manage)
root.order.add_edge(yield_analyze,      energy_audit)