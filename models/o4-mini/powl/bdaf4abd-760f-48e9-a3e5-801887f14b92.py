# Generated from: bdaf4abd-760f-48e9-a3e5-801887f14b92.json
# Description: This process outlines the complex setup and operational launch of an urban vertical farming system designed to optimize crop yield in limited city spaces. It involves site assessment, modular unit assembly, climate control calibration, nutrient solution preparation, and automated monitoring system integration. Continuous data analysis guides iterative environmental adjustments while integrating renewable energy sources to enhance sustainability. Stakeholder coordination ensures compliance with local regulations and market readiness, culminating in a full-scale harvest and distribution plan tailored for urban consumers. The process balances technological innovation with ecological impact and economic viability to establish a pioneering agricultural model within metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey       = Transition(label='Site Survey')
design_layout     = Transition(label='Design Layout')
permit_acquire    = Transition(label='Permit Acquire')
unit_assembly     = Transition(label='Unit Assembly')
climate_setup     = Transition(label='Climate Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
irrigation_install= Transition(label='Irrigation Install')
sensor_deploy     = Transition(label='Sensor Deploy')
energy_connect    = Transition(label='Energy Connect')
system_test       = Transition(label='System Test')
data_monitor      = Transition(label='Data Monitor')
adjust_parameters = Transition(label='Adjust Parameters')
staff_train       = Transition(label='Staff Train')
quality_check     = Transition(label='Quality Check')
harvest_plan      = Transition(label='Harvest Plan')
market_launch     = Transition(label='Market Launch')

# Loop for continuous monitoring and adjustment
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, adjust_parameters])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, permit_acquire,
    unit_assembly, climate_setup, nutrient_mix,
    irrigation_install, sensor_deploy, energy_connect,
    system_test, monitor_loop,
    staff_train, quality_check, harvest_plan, market_launch
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, permit_acquire)

root.order.add_edge(permit_acquire, unit_assembly)

# Parallel setup tasks after assembly
for task in [climate_setup, nutrient_mix, irrigation_install, sensor_deploy, energy_connect]:
    root.order.add_edge(unit_assembly, task)
    root.order.add_edge(task, system_test)

# Testing before entering monitoring loop
root.order.add_edge(system_test, monitor_loop)

# After monitoring/adjustment loop, move to training and rollout
root.order.add_edge(monitor_loop, staff_train)
root.order.add_edge(staff_train, quality_check)
root.order.add_edge(quality_check, harvest_plan)
root.order.add_edge(harvest_plan, market_launch)