# Generated from: f093d7ef-a523-4370-8dd9-32ec08de122b.json
# Description: This process outlines the intricate steps involved in establishing a fully operational urban vertical farm, integrating hydroponic technology, renewable energy, and automated climate control systems. It encompasses site analysis, modular structure assembly, nutrient solution formulation, seed selection, environmental calibration, pest monitoring, and yield optimization. The process further includes data integration from IoT sensors, AI-driven growth prediction, and community engagement for sustainable local food production, ensuring efficiency and minimal ecological footprint within dense city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey    = Transition(label='Site Survey')
design_layout  = Transition(label='Design Layout')
module_build   = Transition(label='Module Build')
system_install = Transition(label='System Install')
water_prep     = Transition(label='Water Prep')
seed_selection = Transition(label='Seed Selection')
nutrient_mix   = Transition(label='Nutrient Mix')
climate_setup  = Transition(label='Climate Setup')
sensor_deploy  = Transition(label='Sensor Deploy')
pest_scan      = Transition(label='Pest Scan')
growth_monitor = Transition(label='Growth Monitor')
data_sync      = Transition(label='Data Sync')
energy_manage  = Transition(label='Energy Manage')
harvest_plan   = Transition(label='Harvest Plan')
community_link = Transition(label='Community Link')

# Initial setup partial order:
# Site Survey -> Design Layout -> Module Build -> System Install
# after System Install, five tasks can proceed concurrently:
initial_setup = StrictPartialOrder(
    nodes=[
        site_survey, design_layout, module_build, system_install,
        water_prep, seed_selection, nutrient_mix, climate_setup, sensor_deploy
    ]
)
initial_setup.order.add_edge(site_survey, design_layout)
initial_setup.order.add_edge(design_layout, module_build)
initial_setup.order.add_edge(module_build, system_install)
for act in [water_prep, seed_selection, nutrient_mix, climate_setup, sensor_deploy]:
    initial_setup.order.add_edge(system_install, act)

# Monitoring body of the loop: can repeat Pest Scan, Growth Monitor, Data Sync, Energy Manage
# We impose Growth Monitor -> Data Sync to reflect that data sync follows monitoring
monitoring_body = StrictPartialOrder(
    nodes=[pest_scan, growth_monitor, data_sync, energy_manage]
)
monitoring_body.order.add_edge(growth_monitor, data_sync)

# LOOP node: do the initial setup once; then repeatedly do the monitoring body
loop_node = OperatorPOWL(
    operator=Operator.LOOP,
    children=[initial_setup, monitoring_body]
)

# Final harvesting and community engagement in sequence after the loop exits
root = StrictPartialOrder(nodes=[loop_node, harvest_plan, community_link])
root.order.add_edge(loop_node, harvest_plan)
root.order.add_edge(harvest_plan, community_link)