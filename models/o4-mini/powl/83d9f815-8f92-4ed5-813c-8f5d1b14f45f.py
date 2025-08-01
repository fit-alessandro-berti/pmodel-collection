# Generated from: 83d9f815-8f92-4ed5-813c-8f5d1b14f45f.json
# Description: This process details the complex operational cycle of an urban vertical farm that integrates hydroponic systems, renewable energy management, and AI-driven crop optimization. The farm begins with seed preparation and nutrient formulation, followed by automated planting and environmental calibration. Continuous monitoring adjusts lighting, humidity, and nutrient delivery in real-time. Harvesting is staggered based on crop maturity, with post-harvest processing including cleaning, sorting, and packaging. Waste materials are recycled or composted to maintain sustainability. The entire system is supported by predictive maintenance of equipment and data analytics for yield forecasting, ensuring efficient resource use and minimal environmental impact within a constrained urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
seed_prep       = Transition(label='Seed Prep')
nutrient_mix    = Transition(label='Nutrient Mix')
automated_plant = Transition(label='Automated Plant')
env_calib       = Transition(label='Env Calibration')
light_adjust    = Transition(label='Light Adjust')
humidity_ctrl   = Transition(label='Humidity Control')
nutrient_feed   = Transition(label='Nutrient Feed')
growth_mon      = Transition(label='Growth Monitor')
pest_scan       = Transition(label='Pest Scan')
harvest_stage   = Transition(label='Harvest Stage')
crop_sort       = Transition(label='Crop Sort')
pack_produce    = Transition(label='Pack Produce')
waste_recycle   = Transition(label='Waste Recycle')
equip_maint     = Transition(label='Equip Maintain')
yield_forecast  = Transition(label='Yield Forecast')

# Silent transition for the loop exit
skip = SilentTransition()

# Group of monitoring activities (can be concurrent)
monitoring_group = StrictPartialOrder(
    nodes=[light_adjust, humidity_ctrl, nutrient_feed, growth_mon, pest_scan]
)
# Loop over monitoring until system decides to exit
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitoring_group, skip]
)

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        seed_prep,
        nutrient_mix,
        automated_plant,
        env_calib,
        monitoring_loop,
        harvest_stage,
        crop_sort,
        pack_produce,
        waste_recycle,
        equip_maint,
        yield_forecast
    ]
)

# Define control-flow dependencies
o = root.order
o.add_edge(seed_prep,       nutrient_mix)
o.add_edge(nutrient_mix,    automated_plant)
o.add_edge(automated_plant, env_calib)

# After calibration, start monitoring loop and also allow parallel maintenance & forecasting
o.add_edge(env_calib,        monitoring_loop)
o.add_edge(env_calib,        equip_maint)
o.add_edge(env_calib,        yield_forecast)

# After monitoring, proceed to harvesting & post-processing
o.add_edge(monitoring_loop,  harvest_stage)
o.add_edge(harvest_stage,    crop_sort)
o.add_edge(crop_sort,        pack_produce)
o.add_edge(pack_produce,     waste_recycle)