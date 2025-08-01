# Generated from: 7d5c7e7a-2687-4738-855b-b1f511e36bf2.json
# Description: This process outlines the complex setup and operational phases involved in establishing an urban rooftop farm on a commercial building. It includes initial site evaluation, structural integrity assessment, soil and nutrient preparation, microclimate analysis, plant selection based on local conditions, installation of modular growing units, irrigation system integration, pest management planning, community engagement for educational workshops, harvesting scheduling, crop rotation planning, waste composting system implementation, and continuous monitoring using IoT sensors to optimize yield and resource usage. The process requires coordination across multiple disciplines including engineering, agriculture, environmental science, and community relations to ensure a sustainable and productive rooftop farming ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey    = Transition(label='Site Survey')
load_test      = Transition(label='Load Test')
soil_prep      = Transition(label='Soil Prep')
climate_check  = Transition(label='Climate Check')
plant_select   = Transition(label='Plant Select')
module_setup   = Transition(label='Module Setup')
irrigation_fit = Transition(label='Irrigation Fit')
pest_control   = Transition(label='Pest Control')
workshop_plan  = Transition(label='Workshop Plan')
harvest_plan   = Transition(label='Harvest Plan')
crop_rotate    = Transition(label='Crop Rotate')
waste_manage   = Transition(label='Waste Manage')
sensor_install = Transition(label='Sensor Install')
data_monitor   = Transition(label='Data Monitor')
yield_optimize = Transition(label='Yield Optimize')

# Define loop for continuous monitoring & optimization
skip = SilentTransition()
monitor_body = StrictPartialOrder(nodes=[data_monitor, yield_optimize])
monitor_body.order.add_edge(data_monitor, yield_optimize)
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_body, skip])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_test, soil_prep, climate_check, plant_select,
    module_setup, irrigation_fit, pest_control, workshop_plan,
    harvest_plan, crop_rotate, waste_manage, sensor_install, monitor_loop
])

# Specify ordering relations
root.order.add_edge(site_survey, load_test)
root.order.add_edge(load_test, soil_prep)
root.order.add_edge(load_test, climate_check)

root.order.add_edge(climate_check, plant_select)
root.order.add_edge(soil_prep, module_setup)
root.order.add_edge(plant_select, module_setup)

root.order.add_edge(module_setup, irrigation_fit)
root.order.add_edge(module_setup, pest_control)

root.order.add_edge(plant_select, workshop_plan)

root.order.add_edge(pest_control, harvest_plan)
root.order.add_edge(workshop_plan, harvest_plan)
root.order.add_edge(harvest_plan, crop_rotate)
root.order.add_edge(crop_rotate, waste_manage)

root.order.add_edge(irrigation_fit, sensor_install)
root.order.add_edge(sensor_install, monitor_loop)