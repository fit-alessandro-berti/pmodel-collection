# Generated from: b2e25c2a-7584-4ceb-a58a-8ecc92a0c589.json
# Description: This process outlines the complex setup of an urban vertical farming system designed to optimize limited city space for high-yield crop production. It involves site analysis, modular structure assembly, environmental control calibration, nutrient solution preparation, and integration of IoT monitoring devices. Specialized activities include biosecurity protocol implementation to prevent contamination, adaptive lighting adjustment based on crop growth stages, and waste recycling for sustainability. The process concludes with trial harvests and data analysis to refine system parameters for commercial scalability and continuous improvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities
site_survey       = Transition(label='Site Survey')
design_layout     = Transition(label='Design Layout')
structure_assemble= Transition(label='Structure Assemble')
lighting_setup    = Transition(label='Lighting Setup')
climate_control   = Transition(label='Climate Control')
nutrient_mix      = Transition(label='Nutrient Mix')
sensor_install    = Transition(label='Sensor Install')
biosecurity_check = Transition(label='Biosecurity Check')
irrigation_test   = Transition(label='Irrigation Test')
seed_planting     = Transition(label='Seed Planting')
growth_monitor    = Transition(label='Growth Monitor')
# separate instance for adaptive lighting adjustment in the loop
lighting_adjust   = Transition(label='Lighting Setup')
waste_recycling   = Transition(label='Waste Recycling')
data_logging      = Transition(label='Data Logging')
trial_harvest     = Transition(label='Trial Harvest')
system_tuning     = Transition(label='System Tuning')
safety_audit      = Transition(label='Safety Audit')

# Loop for growth monitoring and adaptive lighting adjustment
#   * (Growth Monitor, Lighting Setup)
loop_growth = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, lighting_adjust])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    structure_assemble,
    lighting_setup,
    climate_control,
    nutrient_mix,
    sensor_install,
    biosecurity_check,
    irrigation_test,
    seed_planting,
    loop_growth,
    waste_recycling,
    trial_harvest,
    data_logging,
    system_tuning,
    safety_audit
])

# Add ordering constraints
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, structure_assemble)
# after structure, lighting & climate can proceed concurrently
root.order.add_edge(structure_assemble, lighting_setup)
root.order.add_edge(structure_assemble, climate_control)
# both must finish before nutrient mix
root.order.add_edge(lighting_setup, nutrient_mix)
root.order.add_edge(climate_control, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_install)
root.order.add_edge(sensor_install, biosecurity_check)
root.order.add_edge(biosecurity_check, irrigation_test)
root.order.add_edge(irrigation_test, seed_planting)
# seed planting leads into the growth-monitoring loop
root.order.add_edge(seed_planting, loop_growth)
# after loop exit, finish-up steps
root.order.add_edge(loop_growth, waste_recycling)
root.order.add_edge(waste_recycling, trial_harvest)
root.order.add_edge(trial_harvest, data_logging)
root.order.add_edge(data_logging, system_tuning)
root.order.add_edge(system_tuning, safety_audit)