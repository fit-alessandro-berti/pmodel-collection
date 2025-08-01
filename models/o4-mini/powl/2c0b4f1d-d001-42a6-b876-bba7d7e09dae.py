# Generated from: 2c0b4f1d-d001-42a6-b876-bba7d7e09dae.json
# Description: This process describes the establishment of an urban rooftop farm on a commercial building. It involves site evaluation, structural assessments, and securing permits to ensure safety compliance. After soil and environmental testing, a modular planting system is designed and installed. Specialized irrigation and renewable energy systems are integrated to maximize sustainability. Continuous monitoring with IoT sensors ensures optimal growth conditions. The process includes community engagement for educational workshops and local market distribution planning, creating a self-sustaining urban agriculture ecosystem that promotes green spaces and local food production in dense city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey  = Transition(label='Site Survey')
load_check   = Transition(label='Load Check')
permit_apply = Transition(label='Permit Apply')
soil_sample  = Transition(label='Soil Sample')
enviro_test  = Transition(label='Enviro Test')
system_design= Transition(label='System Design')
module_build = Transition(label='Module Build')
irrigation   = Transition(label='Irrigation Setup')
solar_install= Transition(label='Solar Install')
sensor_deploy= Transition(label='Sensor Deploy')
growth_mon   = Transition(label='Growth Monitor')
data_analyze = Transition(label='Data Analyze')
workshop_plan= Transition(label='Workshop Plan')
market_setup = Transition(label='Market Setup')
community_meet=Transition(label='Community Meet')
harvest_cycle= Transition(label='Harvest Cycle')
waste_manage = Transition(label='Waste Manage')

# Define the recurring harvest loop: do Harvest Cycle, then either exit or do Waste Manage and repeat
harvest_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[harvest_cycle, waste_manage]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_check, permit_apply,
    soil_sample, enviro_test,
    system_design, module_build,
    irrigation, solar_install,
    sensor_deploy, growth_mon, data_analyze,
    workshop_plan, market_setup, community_meet,
    harvest_loop
])

# Site evaluation and permits
root.order.add_edge(site_survey, load_check)
root.order.add_edge(load_check, permit_apply)

# Soil and environmental tests can run in parallel after permits
root.order.add_edge(permit_apply, soil_sample)
root.order.add_edge(permit_apply, enviro_test)

# Design follows both tests
root.order.add_edge(soil_sample, system_design)
root.order.add_edge(enviro_test, system_design)

# Build follows design
root.order.add_edge(system_design, module_build)

# Irrigation and solar installation in parallel after building modules
root.order.add_edge(module_build, irrigation)
root.order.add_edge(module_build, solar_install)

# Sensor deployment after both systems are in place
root.order.add_edge(irrigation, sensor_deploy)
root.order.add_edge(solar_install, sensor_deploy)

# Continuous monitoring steps
root.order.add_edge(sensor_deploy, growth_mon)
root.order.add_edge(growth_mon, data_analyze)

# Community engagement and market planning after analysis (can run in parallel)
root.order.add_edge(data_analyze, workshop_plan)
root.order.add_edge(data_analyze, market_setup)

# Community meeting after both planning steps
root.order.add_edge(workshop_plan, community_meet)
root.order.add_edge(market_setup, community_meet)

# Finally enter the harvest loop
root.order.add_edge(community_meet, harvest_loop)