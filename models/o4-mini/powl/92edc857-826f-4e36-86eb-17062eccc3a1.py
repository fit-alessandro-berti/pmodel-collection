# Generated from: 92edc857-826f-4e36-86eb-17062eccc3a1.json
# Description: This process outlines the complete operational cycle of an urban vertical farming system that integrates hydroponics, AI-driven environmental controls, and real-time market analytics. The cycle starts with seed selection based on predictive demand, moves through nutrient calibration and climate optimization, incorporates pest monitoring using drones, and involves staggered harvesting coordinated with automated packaging. Post-harvest, produce quality is assessed by computer vision systems, and inventory levels are updated in cloud-based supply chain software. Finally, waste materials are processed into biofertilizers, closing the loop in a sustainable urban agriculture ecosystem designed to maximize yield and minimize resource consumption within constrained city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_select      = Transition(label='Seed Select')
demand_forecast  = Transition(label='Demand Forecast')
nutrient_mix     = Transition(label='Nutrient Mix')
climate_adjust   = Transition(label='Climate Adjust')
plant_monitor    = Transition(label='Plant Monitor')
drone_inspect    = Transition(label='Drone Inspect')
pest_control     = Transition(label='Pest Control')
growth_track     = Transition(label='Growth Track')
harvest_plan     = Transition(label='Harvest Plan')
automate_pack    = Transition(label='Automate Pack')
quality_scan     = Transition(label='Quality Scan')
inventory_update = Transition(label='Inventory Update')
market_sync      = Transition(label='Market Sync')
waste_process    = Transition(label='Waste Process')
biofertilizer    = Transition(label='Biofertilizer')

# Concurrent monitoring sub‐process
monitoring = StrictPartialOrder(nodes=[
    plant_monitor, drone_inspect, pest_control, growth_track
])
# no edges => fully concurrent

# Harvest coordination sub‐process
harvest_seq = StrictPartialOrder(nodes=[harvest_plan, automate_pack])
harvest_seq.order.add_edge(harvest_plan, automate_pack)

# Post‐harvest quality & sync sub‐process
post_harvest = StrictPartialOrder(
    nodes=[quality_scan, inventory_update, market_sync]
)
post_harvest.order.add_edge(quality_scan, inventory_update)
post_harvest.order.add_edge(inventory_update, market_sync)

# Main "do" part of the loop: seed to market sync
do_part = StrictPartialOrder(nodes=[
    seed_select,
    demand_forecast,
    nutrient_mix,
    climate_adjust,
    monitoring,
    harvest_seq,
    post_harvest
])
do_part.order.add_edge(seed_select,      demand_forecast)
do_part.order.add_edge(demand_forecast,  nutrient_mix)
do_part.order.add_edge(nutrient_mix,     climate_adjust)
do_part.order.add_edge(climate_adjust,   monitoring)
do_part.order.add_edge(monitoring,       harvest_seq)
do_part.order.add_edge(harvest_seq,      post_harvest)

# "Redo" part of the loop: waste to biofertilizer
redo_part = StrictPartialOrder(nodes=[waste_process, biofertilizer])
redo_part.order.add_edge(waste_process, biofertilizer)

# Loop around the full cycle
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[do_part, redo_part]
)