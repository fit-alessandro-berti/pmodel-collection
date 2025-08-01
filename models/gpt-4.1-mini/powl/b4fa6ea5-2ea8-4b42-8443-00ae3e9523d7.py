# Generated from: b4fa6ea5-2ea8-4b42-8443-00ae3e9523d7.json
# Description: This process outlines the intricate steps required to establish an urban vertical farming system within a constrained city environment. It involves site evaluation, modular structure design, hydroponic system integration, nutrient cycling optimization, environmental control calibration, automation setup, crop selection tailored to urban microclimates, waste recycling, energy management with renewable sources, ongoing system diagnostics, pest management with biological controls, yield forecasting, community engagement for local distribution, and finally, scaling strategies for expansion. Each activity ensures efficient resource utilization and maximizes crop output within limited urban spaces while minimizing environmental impact and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
install_hydroponics = Transition(label='Install Hydroponics')
optimize_nutrients = Transition(label='Optimize Nutrients')
calibrate_sensors = Transition(label='Calibrate Sensors')
setup_automation = Transition(label='Setup Automation')
select_crops = Transition(label='Select Crops')
recycle_waste = Transition(label='Recycle Waste')
manage_energy = Transition(label='Manage Energy')
run_diagnostics = Transition(label='Run Diagnostics')
control_pests = Transition(label='Control Pests')
forecast_yield = Transition(label='Forecast Yield')
engage_community = Transition(label='Engage Community')
distribute_produce = Transition(label='Distribute Produce')
plan_expansion = Transition(label='Plan Expansion')

# Compose partial order according to described dependencies:
# The process is mostly sequential but some activities happen concurrently:
# Based on the description:
# 1. 'Site Survey' -> 'Design Modules' -> 'Install Hydroponics'
# 2. After installation, 'Optimize Nutrients', 'Calibrate Sensors', 'Setup Automation' happen concurrently
# 3. After these three finish, 'Select Crops', 'Recycle Waste', and 'Manage Energy' can proceed concurrently
# 4. Then 'Run Diagnostics' happens
# 5. Followed by 'Control Pests' and 'Forecast Yield' concurrently
# 6. 'Engage Community' and 'Distribute Produce' are concurrent after that
# 7. Finally 'Plan Expansion'

nodes = [
    site_survey,
    design_modules,
    install_hydroponics,
    optimize_nutrients,
    calibrate_sensors,
    setup_automation,
    select_crops,
    recycle_waste,
    manage_energy,
    run_diagnostics,
    control_pests,
    forecast_yield,
    engage_community,
    distribute_produce,
    plan_expansion
]

root = StrictPartialOrder(nodes=nodes)

# Sequential dependencies
root.order.add_edge(site_survey, design_modules)
root.order.add_edge(design_modules, install_hydroponics)

# After install_hydroponics, three concurrent nodes
root.order.add_edge(install_hydroponics, optimize_nutrients)
root.order.add_edge(install_hydroponics, calibrate_sensors)
root.order.add_edge(install_hydroponics, setup_automation)

# After these three complete, three more concurrent
root.order.add_edge(optimize_nutrients, select_crops)
root.order.add_edge(calibrate_sensors, select_crops)
root.order.add_edge(setup_automation, select_crops)

root.order.add_edge(optimize_nutrients, recycle_waste)
root.order.add_edge(calibrate_sensors, recycle_waste)
root.order.add_edge(setup_automation, recycle_waste)

root.order.add_edge(optimize_nutrients, manage_energy)
root.order.add_edge(calibrate_sensors, manage_energy)
root.order.add_edge(setup_automation, manage_energy)

# After these three (select_crops, recycle_waste, manage_energy) complete -> run_diagnostics
root.order.add_edge(select_crops, run_diagnostics)
root.order.add_edge(recycle_waste, run_diagnostics)
root.order.add_edge(manage_energy, run_diagnostics)

# After run_diagnostics, two concurrent nodes
root.order.add_edge(run_diagnostics, control_pests)
root.order.add_edge(run_diagnostics, forecast_yield)

# After these two, two concurrent nodes
root.order.add_edge(control_pests, engage_community)
root.order.add_edge(forecast_yield, engage_community)

root.order.add_edge(control_pests, distribute_produce)
root.order.add_edge(forecast_yield, distribute_produce)

# After engage_community and distribute_produce, plan_expansion
root.order.add_edge(engage_community, plan_expansion)
root.order.add_edge(distribute_produce, plan_expansion)