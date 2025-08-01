# Generated from: bdf51ff8-1ecd-43d9-9343-7e09f5ec28ea.json
# Description: This process details the intricate cycle of managing an urban vertical farm that integrates automated hydroponics, AI-driven crop monitoring, waste recycling, and energy optimization. It involves seed selection based on market trends, nutrient solution adjustments, real-time environmental sensing, pest management using bio-controls, harvesting coordination with logistics, and post-harvest quality inspection. Additionally, the process incorporates data analytics to forecast yields and optimize resource consumption while maintaining sustainability standards and compliance with urban agricultural regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection     = Transition(label="Seed Selection")
nutrient_mixing    = Transition(label="Nutrient Mixing")
system_sterilize   = Transition(label="System Sterilize")
planting_setup     = Transition(label="Planting Setup")
environment_check  = Transition(label="Environment Check")
growth_monitor     = Transition(label="Growth Monitor")
pest_control       = Transition(label="Pest Control")
light_adjust       = Transition(label="Light Adjust")
water_recirculate  = Transition(label="Water Recirculate")
harvest_schedule   = Transition(label="Harvest Schedule")
crop_harvest       = Transition(label="Crop Harvest")
quality_inspect    = Transition(label="Quality Inspect")
waste_process      = Transition(label="Waste Process")
data_analyze       = Transition(label="Data Analyze")
yield_forecast     = Transition(label="Yield Forecast")
energy_optimize    = Transition(label="Energy Optimize")
logistics_plan     = Transition(label="Logistics Plan")

# silent transition for optional/potential skips
skip = SilentTransition()

# 1) Planting preparation partial order
planting_po = StrictPartialOrder(
    nodes=[seed_selection, nutrient_mixing, system_sterilize, planting_setup]
)
planting_po.order.add_edge(seed_selection,   nutrient_mixing)
planting_po.order.add_edge(seed_selection,   system_sterilize)
planting_po.order.add_edge(nutrient_mixing,  planting_setup)
planting_po.order.add_edge(system_sterilize, planting_setup)

# 2) Growth cycle partial order with optional pest control
pest_xor = OperatorPOWL(
    operator=Operator.XOR,
    children=[pest_control, skip]
)
growth_cycle = StrictPartialOrder(
    nodes=[environment_check, growth_monitor, light_adjust, water_recirculate, pest_xor]
)
growth_cycle.order.add_edge(environment_check, growth_monitor)
growth_cycle.order.add_edge(growth_monitor,    light_adjust)
growth_cycle.order.add_edge(growth_monitor,    water_recirculate)
growth_cycle.order.add_edge(light_adjust,      pest_xor)
growth_cycle.order.add_edge(water_recirculate, pest_xor)

# loop: repeat the growth cycle until exit
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_cycle, growth_cycle]
)

# 3) Harvesting coordination partial order
harvest_po = StrictPartialOrder(
    nodes=[harvest_schedule, crop_harvest, quality_inspect, waste_process]
)
harvest_po.order.add_edge(harvest_schedule, crop_harvest)
harvest_po.order.add_edge(crop_harvest,     quality_inspect)
harvest_po.order.add_edge(crop_harvest,     waste_process)

# 4) Analytics & optimization partial order
analytics_po = StrictPartialOrder(
    nodes=[data_analyze, yield_forecast, energy_optimize, logistics_plan]
)
analytics_po.order.add_edge(data_analyze,    yield_forecast)
analytics_po.order.add_edge(yield_forecast,  energy_optimize)
analytics_po.order.add_edge(energy_optimize, logistics_plan)

# 5) Root partial order: sequencing the main phases
root = StrictPartialOrder(
    nodes=[planting_po, growth_loop, harvest_po, analytics_po]
)
root.order.add_edge(planting_po, growth_loop)
root.order.add_edge(growth_loop,  harvest_po)
root.order.add_edge(harvest_po,   analytics_po)