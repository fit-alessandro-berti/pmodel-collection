# Generated from: 55c0c56a-0802-4b3e-98c6-728edca09fde.json
# Description: This process involves establishing a vertical farm within an urban environment, integrating advanced hydroponics and IoT technologies to optimize crop yields in limited spaces. Activities include site evaluation, environmental analysis, modular system design, nutrient solution formulation, automated climate control setup, and crop cycle monitoring. The process requires coordination between architects, agronomists, engineers, and data analysts to ensure sustainable resource use, energy efficiency, and minimal environmental impact while maximizing productivity and profitability in a non-traditional farming context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey     = Transition(label='Site Survey')
soil_testing    = Transition(label='Soil Testing')
design_layout   = Transition(label='Design Layout')
system_procure  = Transition(label='System Procure')
install_modules = Transition(label='Install Modules')
setup_sensors   = Transition(label='Setup Sensors')
calibrate_climate = Transition(label='Calibrate Climate')
mix_nutrients   = Transition(label='Mix Nutrients')
plant_seeds     = Transition(label='Plant Seeds')
automate_water  = Transition(label='Automate Water')
monitor_growth  = Transition(label='Monitor Growth')
analyze_data    = Transition(label='Analyze Data')
adjust_conditions = Transition(label='Adjust Conditions')
harvest_crops   = Transition(label='Harvest Crops')
waste_disposal  = Transition(label='Waste Disposal')
market_produce  = Transition(label='Market Produce')

# Build the monitoring loop body (monitor -> analyze -> adjust)
monitor_body = StrictPartialOrder(nodes=[monitor_growth, analyze_data, adjust_conditions])
monitor_body.order.add_edge(monitor_growth, analyze_data)
monitor_body.order.add_edge(analyze_data, adjust_conditions)

# Build a second copy for the loop redo part
monitor_growth_r  = Transition(label='Monitor Growth')
analyze_data_r    = Transition(label='Analyze Data')
adjust_conditions_r = Transition(label='Adjust Conditions')
monitor_redo = StrictPartialOrder(nodes=[monitor_growth_r, analyze_data_r, adjust_conditions_r])
monitor_redo.order.add_edge(monitor_growth_r, analyze_data_r)
monitor_redo.order.add_edge(analyze_data_r, adjust_conditions_r)

# Define the loop: execute monitor_body, then 0 or more times (monitor_redo + monitor_body)
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_body, monitor_redo])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey, soil_testing, design_layout, system_procure,
    install_modules, setup_sensors, calibrate_climate, mix_nutrients,
    automate_water, plant_seeds, monitor_loop,
    harvest_crops, waste_disposal, market_produce
])

# Add the control-flow dependencies
root.order.add_edge(site_survey, soil_testing)
root.order.add_edge(soil_testing, design_layout)
root.order.add_edge(design_layout, system_procure)

root.order.add_edge(system_procure, install_modules)
root.order.add_edge(system_procure, mix_nutrients)

root.order.add_edge(install_modules, setup_sensors)
root.order.add_edge(setup_sensors, calibrate_climate)
root.order.add_edge(setup_sensors, automate_water)

root.order.add_edge(calibrate_climate, plant_seeds)
root.order.add_edge(mix_nutrients, plant_seeds)
root.order.add_edge(automate_water, plant_seeds)

root.order.add_edge(plant_seeds, monitor_loop)

root.order.add_edge(monitor_loop, harvest_crops)

root.order.add_edge(harvest_crops, waste_disposal)
root.order.add_edge(harvest_crops, market_produce)