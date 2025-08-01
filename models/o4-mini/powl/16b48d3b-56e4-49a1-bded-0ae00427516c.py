# Generated from: 16b48d3b-56e4-49a1-bded-0ae00427516c.json
# Description: This process outlines the establishment of an urban vertical farming facility designed to maximize crop yield in limited city spaces using hydroponic and aeroponic systems. It integrates site analysis, modular infrastructure assembly, environmental control calibration, nutrient delivery optimization, and continuous monitoring. The workflow includes coordination with local authorities for permits, sourcing sustainable materials, implementing energy-efficient lighting, and setting up automated harvesting and packaging systems. The process also emphasizes adaptive crop rotation planning, employee training on advanced agricultural technologies, and integration of data analytics for yield prediction and resource management, ensuring a scalable and eco-friendly urban agriculture model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_survey     = Transition(label="Site Survey")
permit_request  = Transition(label="Permit Request")
material_source = Transition(label="Material Sourcing")
modular_build   = Transition(label="Modular Build")
system_wiring   = Transition(label="System Wiring")
enviro_setup    = Transition(label="Enviro Setup")
nutrient_mix    = Transition(label="Nutrient Mix")
lighting_install= Transition(label="Lighting Install")
sensor_deploy   = Transition(label="Sensor Deploy")
calibration_run = Transition(label="Calibration Run")
crop_seeding    = Transition(label="Crop Seeding")
irrigation_test = Transition(label="Irrigation Test")
growth_monitor  = Transition(label="Growth Monitor")
data_analysis   = Transition(label="Data Analysis")
harvest_prep    = Transition(label="Harvest Prep")
packaging_line  = Transition(label="Packaging Line")
waste_manage    = Transition(label="Waste Manage")
staff_training  = Transition(label="Staff Training")

# Continuous monitoring loop: monitor then analyze then repeat or exit
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, data_analysis]
)

# Assemble the partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_request, material_source, modular_build, system_wiring,
    enviro_setup, nutrient_mix, lighting_install, sensor_deploy, calibration_run,
    crop_seeding, irrigation_test, monitoring_loop,
    harvest_prep, packaging_line, waste_manage, staff_training
])

# Define the control-flow dependencies
o = root.order
o.add_edge(site_survey, permit_request)
o.add_edge(permit_request, material_source)
o.add_edge(material_source, modular_build)
o.add_edge(modular_build, system_wiring)
o.add_edge(system_wiring, enviro_setup)

# After setup, deploy sensors, mix nutrients, install lighting in parallel
o.add_edge(enviro_setup, sensor_deploy)
o.add_edge(enviro_setup, nutrient_mix)
o.add_edge(enviro_setup, lighting_install)

# Sensor deployment -> calibration
o.add_edge(sensor_deploy, calibration_run)
# Calibration allows crop seeding and staff training
o.add_edge(calibration_run, crop_seeding)
o.add_edge(calibration_run, staff_training)

# Seeding and mix feed into irrigation test
o.add_edge(crop_seeding, irrigation_test)
o.add_edge(nutrient_mix, irrigation_test)

# After irrigation test start continuous monitoring
o.add_edge(irrigation_test, monitoring_loop)

# After loop exit, proceed to harvest, packaging, waste management
o.add_edge(monitoring_loop, harvest_prep)
o.add_edge(harvest_prep, packaging_line)
o.add_edge(packaging_line, waste_manage)