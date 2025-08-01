# Generated from: bdaf4abd-760f-48e9-a3e5-801887f14b92.json
# Description: This process outlines the complex setup and operational launch of an urban vertical farming system designed to optimize crop yield in limited city spaces. It involves site assessment, modular unit assembly, climate control calibration, nutrient solution preparation, and automated monitoring system integration. Continuous data analysis guides iterative environmental adjustments while integrating renewable energy sources to enhance sustainability. Stakeholder coordination ensures compliance with local regulations and market readiness, culminating in a full-scale harvest and distribution plan tailored for urban consumers. The process balances technological innovation with ecological impact and economic viability to establish a pioneering agricultural model within metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions with the exact provided names
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
PermitAcquire = Transition(label='Permit Acquire')
UnitAssembly = Transition(label='Unit Assembly')
ClimateSetup = Transition(label='Climate Setup')
NutrientMix = Transition(label='Nutrient Mix')
IrrigationInstall = Transition(label='Irrigation Install')
SensorDeploy = Transition(label='Sensor Deploy')
EnergyConnect = Transition(label='Energy Connect')
SystemTest = Transition(label='System Test')
DataMonitor = Transition(label='Data Monitor')
AdjustParameters = Transition(label='Adjust Parameters')
StaffTrain = Transition(label='Staff Train')
QualityCheck = Transition(label='Quality Check')
HarvestPlan = Transition(label='Harvest Plan')
MarketLaunch = Transition(label='Market Launch')

# Model the initial setup: site survey, design layout, permit acquisition (sequential)
initial_setup = StrictPartialOrder(nodes=[SiteSurvey, DesignLayout, PermitAcquire])
initial_setup.order.add_edge(SiteSurvey, DesignLayout)
initial_setup.order.add_edge(DesignLayout, PermitAcquire)

# Model the assembly and setup of units and climate (sequential)
assembly_setup = StrictPartialOrder(nodes=[UnitAssembly, ClimateSetup])
assembly_setup.order.add_edge(UnitAssembly, ClimateSetup)

# Nutrient mix and irrigation install can be concurrent with sensor deploy
nutrient_irrigation = StrictPartialOrder(nodes=[NutrientMix, IrrigationInstall])
# No order edges means these two are concurrent

sensor_energy = StrictPartialOrder(nodes=[SensorDeploy, EnergyConnect])
# Sensor deployment and energy connection can be done concurrently with nutrient and irrigation

# Combine nutrient_irrigation and sensor_energy in parallel (no order linking)
nutrient_sensor_parallel = StrictPartialOrder(
    nodes=[nutrient_irrigation, sensor_energy])

# System test after these setups
system_test_po = StrictPartialOrder(nodes=[nutrient_sensor_parallel, SystemTest])
system_test_po.order.add_edge(nutrient_sensor_parallel, SystemTest)

# Data monitoring and adjusting parameters make a loop: monitor data then decide to adjust or exit loop
monitor_adjust_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[DataMonitor, AdjustParameters]
)

# Staff training and quality check happen after system test and loop finishes
training_quality = StrictPartialOrder(nodes=[StaffTrain, QualityCheck])
# These two can be concurrent (no order edges)

post_test = StrictPartialOrder(
    nodes=[monitor_adjust_loop, training_quality])
post_test.order.add_edge(monitor_adjust_loop, training_quality)

# Harvest plan after post test activities
harvest_plan_po = StrictPartialOrder(nodes=[post_test, HarvestPlan])
harvest_plan_po.order.add_edge(post_test, HarvestPlan)

# Final market launch after harvest planning
final_phase = StrictPartialOrder(nodes=[harvest_plan_po, MarketLaunch])
final_phase.order.add_edge(harvest_plan_po, MarketLaunch)

# Now combine all phases in sequence:
# initial_setup -> assembly_setup -> nutrient_sensor_parallel (merged in system_test_po) -> system_test_po/orders connection
# Let's clarify order steps:

# initial_setup -> assembly_setup
setup_phase = StrictPartialOrder(nodes=[initial_setup, assembly_setup])
setup_phase.order.add_edge(initial_setup, assembly_setup)

# assembly_setup -> nutrient_sensor_parallel
setup_to_nutrient_sensor = StrictPartialOrder(
    nodes=[setup_phase, nutrient_sensor_parallel])
setup_to_nutrient_sensor.order.add_edge(setup_phase, nutrient_sensor_parallel)

# nutrient_sensor_parallel -> system_test
nutrient_to_test = StrictPartialOrder(
    nodes=[setup_to_nutrient_sensor, SystemTest])
nutrient_to_test.order.add_edge(setup_to_nutrient_sensor, SystemTest)

# system_test -> monitor_adjust_loop
test_to_loop = StrictPartialOrder(nodes=[nutrient_to_test, monitor_adjust_loop])
test_to_loop.order.add_edge(nutrient_to_test, monitor_adjust_loop)

# loop -> training_quality
loop_to_training = StrictPartialOrder(nodes=[test_to_loop, training_quality])
loop_to_training.order.add_edge(test_to_loop, training_quality)

# training_quality -> harvest_plan
training_to_harvest = StrictPartialOrder(nodes=[loop_to_training, HarvestPlan])
training_to_harvest.order.add_edge(loop_to_training, HarvestPlan)

# harvest_plan -> market_launch
harvest_to_launch = StrictPartialOrder(nodes=[training_to_harvest, MarketLaunch])
harvest_to_launch.order.add_edge(training_to_harvest, MarketLaunch)

# Simplify by assigning final root to harvest_to_launch
root = harvest_to_launch