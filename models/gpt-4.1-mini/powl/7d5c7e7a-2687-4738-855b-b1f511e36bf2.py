# Generated from: 7d5c7e7a-2687-4738-855b-b1f511e36bf2.json
# Description: This process outlines the complex setup and operational phases involved in establishing an urban rooftop farm on a commercial building. It includes initial site evaluation, structural integrity assessment, soil and nutrient preparation, microclimate analysis, plant selection based on local conditions, installation of modular growing units, irrigation system integration, pest management planning, community engagement for educational workshops, harvesting scheduling, crop rotation planning, waste composting system implementation, and continuous monitoring using IoT sensors to optimize yield and resource usage. The process requires coordination across multiple disciplines including engineering, agriculture, environmental science, and community relations to ensure a sustainable and productive rooftop farming ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
soil_prep = Transition(label='Soil Prep')
climate_check = Transition(label='Climate Check')
plant_select = Transition(label='Plant Select')
module_setup = Transition(label='Module Setup')
irrigation_fit = Transition(label='Irrigation Fit')
pest_control = Transition(label='Pest Control')
workshop_plan = Transition(label='Workshop Plan')
harvest_plan = Transition(label='Harvest Plan')
crop_rotate = Transition(label='Crop Rotate')
waste_manage = Transition(label='Waste Manage')
sensor_install = Transition(label='Sensor Install')
data_monitor = Transition(label='Data Monitor')
yield_optimize = Transition(label='Yield Optimize')

# Phase 1: Initial site evaluation and assessments (Site Survey -> Load Test)
initial_phase = StrictPartialOrder(nodes=[site_survey, load_test])
initial_phase.order.add_edge(site_survey, load_test)

# Phase 2: Preparation steps (Soil Prep & Climate Check in parallel, then Plant Select)
prep_phase = StrictPartialOrder(nodes=[soil_prep, climate_check, plant_select])
prep_phase.order.add_edge(soil_prep, plant_select)
prep_phase.order.add_edge(climate_check, plant_select)

# Phase 3: Installation steps: Module Setup -> Irrigation Fit -> Pest Control
installation_phase = StrictPartialOrder(nodes=[module_setup, irrigation_fit, pest_control])
installation_phase.order.add_edge(module_setup, irrigation_fit)
installation_phase.order.add_edge(irrigation_fit, pest_control)

# Phase 4: Community and operational planning (Workshop Plan concurrent with Harvest Plan and Crop Rotate)
community_ops = StrictPartialOrder(
    nodes=[workshop_plan, harvest_plan, crop_rotate]
)
# No order edges: all concurrent

# Phase 5: Waste management and sensor installation (Waste Manage -> Sensor Install)
waste_sensor = StrictPartialOrder(nodes=[waste_manage, sensor_install])
waste_sensor.order.add_edge(waste_manage, sensor_install)

# Phase 6: Monitoring and optimization: Data Monitor -> Yield Optimize (loop)
# continuous monitoring loop: Data Monitor then choose to loop or Yield Optimize then exit
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, yield_optimize])

# Compose phases in overall partial order with logical flows:
# Initial phase -> Prep phase -> Installation phase
# Installation phase -> (community_ops AND waste_sensor AND monitor_loop) concurrent
root = StrictPartialOrder(nodes=[
    initial_phase,
    prep_phase,
    installation_phase,
    community_ops,
    waste_sensor,
    monitor_loop
])

# initial -> prep
root.order.add_edge(initial_phase, prep_phase)
# prep -> installation
root.order.add_edge(prep_phase, installation_phase)
# installation -> community_ops
root.order.add_edge(installation_phase, community_ops)
# installation -> waste_sensor
root.order.add_edge(installation_phase, waste_sensor)
# installation -> monitor_loop
root.order.add_edge(installation_phase, monitor_loop)