# Generated from: 7d728a9f-3ed8-456e-a8ad-094306a54950.json
# Description: This process outlines the complex setup of an urban vertical farm integrating hydroponic systems, renewable energy sources, and IoT-based environmental controls. It involves selecting optimal building spaces, designing multi-layer crop layouts, installing climate and nutrient monitoring sensors, automating irrigation schedules, and integrating blockchain for supply chain transparency. The process ensures sustainable food production in dense city environments by balancing energy efficiency, crop yield optimization, and waste reduction through smart analytics and adaptive resource management strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
space_design     = Transition(label='Space Design')
structural_check = Transition(label='Structural Check')
system_layout    = Transition(label='System Layout')
sensor_install   = Transition(label='Sensor Install')
irrigation_setup = Transition(label='Irrigation Setup')
lighting_config  = Transition(label='Lighting Config')
climate_control  = Transition(label='Climate Control')
nutrient_mix     = Transition(label='Nutrient Mix')
energy_connect   = Transition(label='Energy Connect')
data_sync        = Transition(label='Data Sync')
automation_test  = Transition(label='Automation Test')
crop_seeding     = Transition(label='Crop Seeding')
growth_monitor   = Transition(label='Growth Monitor')
harvest_plan     = Transition(label='Harvest Plan')
waste_handle     = Transition(label='Waste Handle')
supply_audit     = Transition(label='Supply Audit')

# Silent transition for loop continuation
skip = SilentTransition()

# Loop: repeat growth monitoring until exit
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, skip])

# Build the root partial order with all nodes
root = StrictPartialOrder(nodes=[
    site_survey, space_design, structural_check, system_layout,
    sensor_install, irrigation_setup, lighting_config, climate_control,
    nutrient_mix, energy_connect, data_sync, automation_test,
    crop_seeding, growth_loop, harvest_plan, waste_handle, supply_audit
])

# Linear setup: survey → design → structural check → layout
root.order.add_edge(site_survey, space_design)
root.order.add_edge(space_design, structural_check)
root.order.add_edge(structural_check, system_layout)

# Parallel installation/configuration after layout
for cfg in [sensor_install, irrigation_setup, lighting_config, climate_control]:
    root.order.add_edge(system_layout, cfg)

# After all config tasks complete, prepare nutrient mix & energy
for cfg in [sensor_install, irrigation_setup, lighting_config, climate_control]:
    root.order.add_edge(cfg, nutrient_mix)
    root.order.add_edge(cfg, energy_connect)

# Data syncing depends on both nutrient mix & energy connect
root.order.add_edge(nutrient_mix, data_sync)
root.order.add_edge(energy_connect, data_sync)

# Automation test follows data sync
root.order.add_edge(data_sync, automation_test)

# Crop seeding follows automation test
root.order.add_edge(automation_test, crop_seeding)

# Enter growth-monitoring loop after seeding
root.order.add_edge(crop_seeding, growth_loop)

# After exiting loop, harvest planning
root.order.add_edge(growth_loop, harvest_plan)

# Waste handling can start after harvest
root.order.add_edge(harvest_plan, waste_handle)

# Supply audit depends on both harvest plan and waste handling
root.order.add_edge(harvest_plan, supply_audit)
root.order.add_edge(waste_handle, supply_audit)