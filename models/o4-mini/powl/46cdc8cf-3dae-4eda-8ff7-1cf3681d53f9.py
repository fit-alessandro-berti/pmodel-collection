# Generated from: 46cdc8cf-3dae-4eda-8ff7-1cf3681d53f9.json
# Description: This process outlines the setup of an urban vertical farming system designed to optimize limited city space for sustainable agriculture. It involves site analysis, modular system design, nutrient cycling planning, and integration of IoT sensors for microclimate control. Activities include selecting plant species based on local demand and light requirements, establishing water recycling loops, and coordinating with local authorities for compliance. The process further encompasses staff training on automated maintenance, real-time monitoring of crop health, and iterative optimization of growth parameters to maximize yield while minimizing energy consumption and waste. The system also incorporates community engagement strategies to promote urban agriculture awareness and potential partnerships with local markets for direct produce sales.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey   = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
select_crops  = Transition(label='Select Crops')
plan_nutrients = Transition(label='Plan Nutrients')
water_loop    = Transition(label='Water Loop')
build_structures = Transition(label='Build Structures')
setup_lighting = Transition(label='Setup Lighting')
install_sensors = Transition(label='Install Sensors')
integrate_iot = Transition(label='Integrate IoT')
test_systems  = Transition(label='Test Systems')
train_staff   = Transition(label='Train Staff')
monitor_growth = Transition(label='Monitor Growth')
adjust_params = Transition(label='Adjust Parameters')
engage_comm   = Transition(label='Engage Community')
market_produce = Transition(label='Market Produce')

# Loop for iterative monitoring and adjustment
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_growth, adjust_params]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_modules, select_crops, plan_nutrients,
    water_loop, build_structures, setup_lighting, install_sensors,
    integrate_iot, test_systems, train_staff, monitor_loop,
    engage_comm, market_produce
])

# Define the sequence and concurrency via partial‐order edges
root.order.add_edge(site_survey, design_modules)
root.order.add_edge(design_modules, select_crops)
root.order.add_edge(select_crops, plan_nutrients)
root.order.add_edge(plan_nutrients, water_loop)
root.order.add_edge(water_loop, build_structures)
root.order.add_edge(build_structures, setup_lighting)
root.order.add_edge(setup_lighting, install_sensors)
root.order.add_edge(install_sensors, integrate_iot)
root.order.add_edge(integrate_iot, test_systems)

# After testing, split into two concurrent branches:
# 1) Staff training and then the monitor‐adjust loop
# 2) Community engagement leading to market produce
root.order.add_edge(test_systems, train_staff)
root.order.add_edge(train_staff, monitor_loop)

root.order.add_edge(test_systems, engage_comm)
root.order.add_edge(engage_comm, market_produce)