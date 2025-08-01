# Generated from: 30d7c4ba-8a6c-46a0-83e5-8b7b6eb3f95d.json
# Description: This process details the comprehensive cycle of managing an urban vertical farm that integrates IoT sensors, AI-driven analytics, and automated hydroponic systems to optimize crop yield year-round. Starting from environmental setup and seed selection, the process includes nutrient mixing, growth monitoring, pest detection via drones, adaptive lighting control, and harvesting automation. Post-harvest activities encompass quality sorting, packaging using biodegradable materials, and distribution logistics tailored for city-based delivery. The process also incorporates sustainability checks, energy consumption audits, and community engagement initiatives to ensure ecological balance and social impact within the urban farming ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
setup_sensors = Transition(label='Setup Sensors')
select_seeds = Transition(label='Select Seeds')
mix_nutrients = Transition(label='Mix Nutrients')
plant_crops = Transition(label='Plant Crops')
monitor_growth = Transition(label='Monitor Growth')
detect_pests = Transition(label='Detect Pests')
adjust_lighting = Transition(label='Adjust Lighting')
control_climate = Transition(label='Control Climate')
automate_watering = Transition(label='Automate Watering')
harvest_crops = Transition(label='Harvest Crops')
sort_quality = Transition(label='Sort Quality')
package_goods = Transition(label='Package Goods')
plan_delivery = Transition(label='Plan Delivery')
audit_energy = Transition(label='Audit Energy')
engage_community = Transition(label='Engage Community')
recycle_waste = Transition(label='Recycle Waste')

# Silent transition for optional or loop exits
skip = SilentTransition()

# Build monitoring partial order for environmental and growth controls
# Detect Pests --> Adjust Lighting and Control Climate and Automate Watering can be concurrent after pests detected
detect_and_control = StrictPartialOrder(
    nodes=[detect_pests, adjust_lighting, control_climate, automate_watering]
)
detect_and_control.order.add_edge(detect_pests, adjust_lighting)
detect_and_control.order.add_edge(detect_pests, control_climate)
detect_and_control.order.add_edge(detect_pests, automate_watering)

# Loop for growth monitoring with possible pest detection and control cycle:
# Loop executing [Monitor Growth] then choice [Exit or (Detect Pests + Controls)]
# We model B in Loop as the pest detection and control PO
loop_growth_control = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, detect_and_control])

# Planting phase partial order: Mix Nutrients --> Plant Crops; both preceded by seed selection
planting = StrictPartialOrder(
    nodes=[select_seeds, mix_nutrients, plant_crops]
)
planting.order.add_edge(select_seeds, mix_nutrients)
planting.order.add_edge(mix_nutrients, plant_crops)

# Harvest partial order: Harvest Crops --> Sort Quality --> Package Goods --> Plan Delivery (linear)
harvest_sequence = StrictPartialOrder(
    nodes=[harvest_crops, sort_quality, package_goods, plan_delivery]
)
harvest_sequence.order.add_edge(harvest_crops, sort_quality)
harvest_sequence.order.add_edge(sort_quality, package_goods)
harvest_sequence.order.add_edge(package_goods, plan_delivery)

# Sustainability checks and community engagement partial order with Recycle Waste after audits and engagement
sustainability = StrictPartialOrder(
    nodes=[audit_energy, engage_community, recycle_waste]
)
sustainability.order.add_edge(audit_energy, recycle_waste)
sustainability.order.add_edge(engage_community, recycle_waste)

# Environmental setup partial order:
# Setup Sensors --> (Planting) --> (Loop of growth + pest control)
env_setup_and_planting = StrictPartialOrder(
    nodes=[setup_sensors, planting, loop_growth_control]
)
env_setup_and_planting.order.add_edge(setup_sensors, planting)
env_setup_and_planting.order.add_edge(planting, loop_growth_control)

# Combine the full process with environmental setup+growth, then harvesting, then sustainability
root = StrictPartialOrder(
    nodes=[env_setup_and_planting, harvest_sequence, sustainability]
)
root.order.add_edge(env_setup_and_planting, harvest_sequence)
root.order.add_edge(harvest_sequence, sustainability)