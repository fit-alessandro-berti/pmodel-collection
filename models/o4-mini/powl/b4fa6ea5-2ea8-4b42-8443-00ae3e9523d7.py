# Generated from: b4fa6ea5-2ea8-4b42-8443-00ae3e9523d7.json
# Description: This process outlines the intricate steps required to establish an urban vertical farming system within a constrained city environment. It involves site evaluation, modular structure design, hydroponic system integration, nutrient cycling optimization, environmental control calibration, automation setup, crop selection tailored to urban microclimates, waste recycling, energy management with renewable sources, ongoing system diagnostics, pest management with biological controls, yield forecasting, community engagement for local distribution, and finally, scaling strategies for expansion. Each activity ensures efficient resource utilization and maximizes crop output within limited urban spaces while minimizing environmental impact and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities as POWL transitions
site_survey        = Transition(label='Site Survey')
design_modules     = Transition(label='Design Modules')
install_hydroponics = Transition(label='Install Hydroponics')
optimize_nutrients = Transition(label='Optimize Nutrients')
calibrate_sensors  = Transition(label='Calibrate Sensors')
setup_automation   = Transition(label='Setup Automation')
select_crops       = Transition(label='Select Crops')
recycle_waste      = Transition(label='Recycle Waste')
manage_energy      = Transition(label='Manage Energy')
run_diagnostics    = Transition(label='Run Diagnostics')
control_pests      = Transition(label='Control Pests')
forecast_yield     = Transition(label='Forecast Yield')
engage_community   = Transition(label='Engage Community')
distribute_produce = Transition(label='Distribute Produce')
plan_expansion     = Transition(label='Plan Expansion')

# Build the initial setup as a partial order
initial = StrictPartialOrder(nodes=[
    site_survey, design_modules, install_hydroponics,
    optimize_nutrients, calibrate_sensors, setup_automation,
    select_crops, recycle_waste, manage_energy,
    run_diagnostics, control_pests, forecast_yield,
    engage_community, distribute_produce
])
initial.order.add_edge(site_survey,        design_modules)
initial.order.add_edge(design_modules,     install_hydroponics)
initial.order.add_edge(install_hydroponics, optimize_nutrients)
initial.order.add_edge(optimize_nutrients, calibrate_sensors)
initial.order.add_edge(calibrate_sensors,  setup_automation)
initial.order.add_edge(setup_automation,   select_crops)
# After selecting crops, recycle waste and manage energy can proceed in parallel
initial.order.add_edge(select_crops,       recycle_waste)
initial.order.add_edge(select_crops,       manage_energy)
# Both recycling and energy management must complete before diagnostics
initial.order.add_edge(recycle_waste,      run_diagnostics)
initial.order.add_edge(manage_energy,      run_diagnostics)
initial.order.add_edge(run_diagnostics,    control_pests)
initial.order.add_edge(control_pests,      forecast_yield)
initial.order.add_edge(forecast_yield,     engage_community)
initial.order.add_edge(engage_community,   distribute_produce)

# Wrap the entire setup in a loop to allow for expansion cycles
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[initial, plan_expansion]
)