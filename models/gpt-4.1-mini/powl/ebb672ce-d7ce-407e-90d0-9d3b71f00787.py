# Generated from: ebb672ce-d7ce-407e-90d0-9d3b71f00787.json
# Description: This process details the establishment of a vertical farming facility within an urban environment, integrating sustainable practices and advanced technology to optimize crop yield in limited spaces. It involves site analysis, modular construction, sensor calibration, hydroponic system installation, nutrient cycling, energy optimization, pest management, and data-driven growth monitoring. The process requires coordination between architects, agronomists, engineers, and supply chain teams to ensure efficient production, minimal environmental impact, and scalability. Continuous feedback loops enable adaptive system improvements and resource allocation adjustments to meet dynamic urban demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
modular_build = Transition(label='Modular Build')
install_pumps = Transition(label='Install Pumps')
setup_sensors = Transition(label='Setup Sensors')
calibrate_lights = Transition(label='Calibrate Lights')
nutrient_mix = Transition(label='Nutrient Mix')
plant_seeding = Transition(label='Plant Seeding')
water_cycling = Transition(label='Water Cycling')
energy_audit = Transition(label='Energy Audit')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
data_analysis = Transition(label='Data Analysis')
yield_forecast = Transition(label='Yield Forecast')
supply_order = Transition(label='Supply Order')
waste_recycle = Transition(label='Waste Recycle')
system_upgrade = Transition(label='System Upgrade')

# Define a loop for continuous feedback and adaptive improvements:
# Loop body: Growth Monitor -> Data Analysis -> Yield Forecast -> Supply Order -> Waste Recycle -> System Upgrade
feedback_body = StrictPartialOrder(nodes=[
    growth_monitor, data_analysis, yield_forecast,
    supply_order, waste_recycle, system_upgrade
])
feedback_body.order.add_edge(growth_monitor, data_analysis)
feedback_body.order.add_edge(data_analysis, yield_forecast)
feedback_body.order.add_edge(yield_forecast, supply_order)
feedback_body.order.add_edge(supply_order, waste_recycle)
feedback_body.order.add_edge(waste_recycle, system_upgrade)

feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    feedback_body,  # A: body executed once per loop iteration
    SilentTransition()  # B: silent transition to optionally repeat the loop
])

# Core construction and installation partial order:
construction = StrictPartialOrder(nodes=[
    site_survey, design_layout, modular_build,
    install_pumps, setup_sensors, calibrate_lights,
    nutrient_mix, plant_seeding
])
construction.order.add_edge(site_survey, design_layout)
construction.order.add_edge(design_layout, modular_build)
construction.order.add_edge(modular_build, install_pumps)
construction.order.add_edge(install_pumps, setup_sensors)
construction.order.add_edge(setup_sensors, calibrate_lights)
construction.order.add_edge(calibrate_lights, nutrient_mix)
construction.order.add_edge(nutrient_mix, plant_seeding)

# Operational partial order that can run mostly concurrently after planting:
operations = StrictPartialOrder(nodes=[
    water_cycling, energy_audit, pest_control
])
# Let's say water cycling is required before pest control, and energy audit before pest control to reflect dependencies:
operations.order.add_edge(water_cycling, pest_control)
operations.order.add_edge(energy_audit, pest_control)

# Overall process partial order:
# First construction, then operations and feedback loop run concurrently, but feedback depends on operations
root = StrictPartialOrder(nodes=[construction, operations, feedback_loop])
root.order.add_edge(construction, operations)
root.order.add_edge(operations, feedback_loop)