# Generated from: ebb672ce-d7ce-407e-90d0-9d3b71f00787.json
# Description: This process details the establishment of a vertical farming facility within an urban environment, integrating sustainable practices and advanced technology to optimize crop yield in limited spaces. It involves site analysis, modular construction, sensor calibration, hydroponic system installation, nutrient cycling, energy optimization, pest management, and data-driven growth monitoring. The process requires coordination between architects, agronomists, engineers, and supply chain teams to ensure efficient production, minimal environmental impact, and scalability. Continuous feedback loops enable adaptive system improvements and resource allocation adjustments to meet dynamic urban demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
modular_build   = Transition(label='Modular Build')
install_pumps   = Transition(label='Install Pumps')
setup_sensors   = Transition(label='Setup Sensors')
calibrate_lights= Transition(label='Calibrate Lights')
nutrient_mix    = Transition(label='Nutrient Mix')
plant_seeding   = Transition(label='Plant Seeding')
water_cycling   = Transition(label='Water Cycling')
energy_audit    = Transition(label='Energy Audit')
pest_control    = Transition(label='Pest Control')
growth_monitor  = Transition(label='Growth Monitor')
data_analysis   = Transition(label='Data Analysis')
yield_forecast  = Transition(label='Yield Forecast')
supply_order    = Transition(label='Supply Order')
waste_recycle   = Transition(label='Waste Recycle')
system_upgrade  = Transition(label='System Upgrade')

# Silent transition for optional branches
skip = SilentTransition()

# After each growth‐forecast step, choose one of: supply order, waste recycle, system upgrade, or skip
choice_actions = OperatorPOWL(
    operator=Operator.XOR,
    children=[supply_order, waste_recycle, system_upgrade, skip]
)

# Loop body: nutrient mix → water cycling → monitor → analysis → forecast → choice
loop_body = StrictPartialOrder(
    nodes=[nutrient_mix, water_cycling, growth_monitor, data_analysis, yield_forecast, choice_actions]
)
loop_body.order.add_edge(nutrient_mix,    water_cycling)
loop_body.order.add_edge(water_cycling,    growth_monitor)
loop_body.order.add_edge(growth_monitor,   data_analysis)
loop_body.order.add_edge(data_analysis,    yield_forecast)
loop_body.order.add_edge(yield_forecast,   choice_actions)

# Loop node: plant seeding first, then repeat the loop body until exit
loop_node = OperatorPOWL(
    operator=Operator.LOOP,
    children=[plant_seeding, loop_body]
)

# Root partial order: from site survey through construction, then concurrent ongoing operations
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_layout,
        modular_build,
        install_pumps,
        setup_sensors,
        calibrate_lights,
        loop_node,
        energy_audit,
        pest_control
    ]
)

# Define the main control‐flow edges
root.order.add_edge(site_survey,      design_layout)
root.order.add_edge(design_layout,    modular_build)
root.order.add_edge(modular_build,    install_pumps)
root.order.add_edge(install_pumps,    setup_sensors)
root.order.add_edge(setup_sensors,    calibrate_lights)
# After calibration, start the growth loop and audit/pest tasks in parallel
root.order.add_edge(calibrate_lights, loop_node)
root.order.add_edge(calibrate_lights, energy_audit)
root.order.add_edge(calibrate_lights, pest_control)