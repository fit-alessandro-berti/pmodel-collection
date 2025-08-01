# Generated from: bdf51ff8-1ecd-43d9-9343-7e09f5ec28ea.json
# Description: This process details the intricate cycle of managing an urban vertical farm that integrates automated hydroponics, AI-driven crop monitoring, waste recycling, and energy optimization. It involves seed selection based on market trends, nutrient solution adjustments, real-time environmental sensing, pest management using bio-controls, harvesting coordination with logistics, and post-harvest quality inspection. Additionally, the process incorporates data analytics to forecast yields and optimize resource consumption while maintaining sustainability standards and compliance with urban agricultural regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mixing = Transition(label='Nutrient Mixing')
System_Sterilize = Transition(label='System Sterilize')
Planting_Setup = Transition(label='Planting Setup')
Environment_Check = Transition(label='Environment Check')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Light_Adjust = Transition(label='Light Adjust')
Water_Recirculate = Transition(label='Water Recirculate')
Harvest_Schedule = Transition(label='Harvest Schedule')
Crop_Harvest = Transition(label='Crop Harvest')
Quality_Inspect = Transition(label='Quality Inspect')
Waste_Process = Transition(label='Waste Process')
Data_Analyze = Transition(label='Data Analyze')
Yield_Forecast = Transition(label='Yield Forecast')
Energy_Optimize = Transition(label='Energy Optimize')
Logistics_Plan = Transition(label='Logistics Plan')

# Build loop body: after some activities, decide to continue monitoring (loop) or exit

# Loop body partial order:
# - Growth Monitor is pivotal, it decides after monitoring whether to end or continue with adjustments and re-monitor.
# - After Growth Monitor: either exit or do Pest Control, Light Adjust, Water Recirculate, Environment Check then grow again.

# Partial order inside loop body after Growth Monitor:
# Pest_Control, Light_Adjust, Water_Recirculate and Environment_Check are concurrent after Growth_Monitor
loop_adjustments_nodes = [Pest_Control, Light_Adjust, Water_Recirculate, Environment_Check]
loop_adjustments = StrictPartialOrder(nodes=loop_adjustments_nodes)
# No edges, fully concurrent

# The loop body is Growth Monitor followed by these adjustments concurrently, then looping back
loop_body_po = StrictPartialOrder(
    nodes=[Growth_Monitor, loop_adjustments]
)
loop_body_po.order.add_edge(Growth_Monitor, loop_adjustments)

# Loop node: * (Growth_Monitor then adjustments)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, loop_adjustments])

# Initial setup partial order before loop:
# Seed_Selection --> Nutrient_Mixing --> System_Sterilize --> Planting_Setup --> loop
init_setup = StrictPartialOrder(
    nodes=[Seed_Selection, Nutrient_Mixing, System_Sterilize, Planting_Setup, loop]
)
init_setup.order.add_edge(Seed_Selection, Nutrient_Mixing)
init_setup.order.add_edge(Nutrient_Mixing, System_Sterilize)
init_setup.order.add_edge(System_Sterilize, Planting_Setup)
init_setup.order.add_edge(Planting_Setup, loop)

# After loop ends: Harvest_Schedule --> Crop_Harvest --> Quality_Inspect
harvest_po = StrictPartialOrder(
    nodes=[Harvest_Schedule, Crop_Harvest, Quality_Inspect]
)
harvest_po.order.add_edge(Harvest_Schedule, Crop_Harvest)
harvest_po.order.add_edge(Crop_Harvest, Quality_Inspect)

# Parallel activities after harvest: Waste_Process, Data_Analyze, Yield_Forecast, Energy_Optimize, Logistics_Plan
post_harvest_parallel = StrictPartialOrder(
    nodes=[Waste_Process, Data_Analyze, Yield_Forecast, Energy_Optimize, Logistics_Plan]
)
# No edges, all concurrent

# Compose final model with three sequential stages:
# init_setup --> harvest_po --> post_harvest_parallel
stage_2_3 = StrictPartialOrder(
    nodes=[harvest_po, post_harvest_parallel]
)
stage_2_3.order.add_edge(harvest_po, post_harvest_parallel)

root = StrictPartialOrder(
    nodes=[init_setup, stage_2_3]
)
root.order.add_edge(init_setup, stage_2_3)