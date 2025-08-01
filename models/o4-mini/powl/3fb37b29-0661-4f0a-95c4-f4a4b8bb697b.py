# Generated from: 3fb37b29-0661-4f0a-95c4-f4a4b8bb697b.json
# Description: This process outlines the establishment of a vertical farming facility within an urban environment, integrating advanced hydroponics, climate control, and automated harvesting technologies. It involves site selection based on urban density and sunlight patterns, structural modifications to optimize vertical space, installation of nutrient delivery systems, calibration of LED grow lights tailored to plant species, implementation of IoT sensors for continuous monitoring, recruitment and training of specialized agronomists, and development of a supply chain for rapid distribution. The process also includes compliance with urban agricultural regulations and community engagement to promote sustainable practices. Continuous data analysis and system optimization ensure high yield and energy efficiency, making this atypical business operation a model for future urban agriculture initiatives.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
light_mapping   = Transition(label='Light Mapping')
structure_design= Transition(label='Structure Design')
permits_acquire = Transition(label='Permits Acquire')
system_install  = Transition(label='System Install')
nutrient_setup  = Transition(label='Nutrient Setup')
light_calibrate = Transition(label='Light Calibrate')
sensor_deploy   = Transition(label='Sensor Deploy')
staff_hire      = Transition(label='Staff Hire')
training_plan   = Transition(label='Training Plan')
crop_select     = Transition(label='Crop Select')
planting_stage  = Transition(label='Planting Stage')
growth_monitor  = Transition(label='Growth Monitor')
harvest_automate= Transition(label='Harvest Automate')
quality_check   = Transition(label='Quality Check')
market_launch   = Transition(label='Market Launch')
data_review     = Transition(label='Data Review')
energy_audit    = Transition(label='Energy Audit')

# Loop for continuous monitoring and optimization
# Body A = growth_monitor
# Body B = concurrent data_review & energy_audit
monitor_optimize = StrictPartialOrder(nodes=[data_review, energy_audit])
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, monitor_optimize])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey, light_mapping,
    structure_design, permits_acquire,
    system_install, nutrient_setup, light_calibrate, sensor_deploy,
    staff_hire, training_plan,
    crop_select, planting_stage,
    monitor_loop,
    harvest_automate, quality_check, market_launch
])

# Define control-flow edges
# 1. Site survey -> light mapping -> structure design -> permits
root.order.add_edge(site_survey, light_mapping)
root.order.add_edge(light_mapping, structure_design)
root.order.add_edge(structure_design, permits_acquire)

# 2. Permits -> system install -> (nutrient, light calibrate, sensor) in parallel
root.order.add_edge(permits_acquire, system_install)
root.order.add_edge(system_install, nutrient_setup)
root.order.add_edge(system_install, light_calibrate)
root.order.add_edge(system_install, sensor_deploy)

# 3. After all setup tasks, hire and train staff
root.order.add_edge(nutrient_setup, staff_hire)
root.order.add_edge(light_calibrate, staff_hire)
root.order.add_edge(sensor_deploy, staff_hire)
root.order.add_edge(staff_hire, training_plan)

# 4. Moving to planting and growth
root.order.add_edge(training_plan, crop_select)
root.order.add_edge(crop_select, planting_stage)

# 5. Start the monitoring/optimization loop, then harvesting
root.order.add_edge(planting_stage, monitor_loop)
root.order.add_edge(monitor_loop, harvest_automate)

# 6. Quality check and market launch
root.order.add_edge(harvest_automate, quality_check)
root.order.add_edge(quality_check, market_launch)