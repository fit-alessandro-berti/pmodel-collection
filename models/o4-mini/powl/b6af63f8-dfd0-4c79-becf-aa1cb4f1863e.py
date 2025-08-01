# Generated from: b6af63f8-dfd0-4c79-becf-aa1cb4f1863e.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farm that integrates advanced hydroponic systems, AI-driven climate controls, and automated harvesting robots. Starting from seed selection optimized for urban microclimates, it progresses through nutrient blending, growth monitoring via IoT sensors, and pest management using biocontrol agents. The process also includes energy recycling from waste biomass, real-time yield prediction algorithms, and adaptive lighting schedules to maximize photosynthesis efficiency. Finally, harvested crops undergo quality scanning, packaging with smart labels for traceability, and urban distribution logistics optimized for minimal carbon footprint. This atypical but realistic process blends agriculture, technology, and sustainability into a continuous loop designed for dense metropolitan environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
seed_select     = Transition(label='Seed Select')
nutrient_mix    = Transition(label='Nutrient Mix')
planting_setup  = Transition(label='Planting Setup')
climate_adjust  = Transition(label='Climate Adjust')
iot_monitor     = Transition(label='IoT Monitor')
pest_control    = Transition(label='Pest Control')
growth_analyze  = Transition(label='Growth Analyze')
light_schedule  = Transition(label='Light Schedule')
yield_predict   = Transition(label='Yield Predict')
robot_harvest   = Transition(label='Robot Harvest')
quality_scan    = Transition(label='Quality Scan')
smart_label     = Transition(label='Smart Label')
pack_produce    = Transition(label='Pack Produce')
urban_dispatch  = Transition(label='Urban Dispatch')
waste_process   = Transition(label='Waste Process')
energy_capture  = Transition(label='Energy Capture')
water_recycle   = Transition(label='Water Recycle')

# Silent transition for loop continuation
skip = SilentTransition()

# Build the core cycle A as a strict partial order
A = StrictPartialOrder(nodes=[
    seed_select, nutrient_mix, planting_setup,
    climate_adjust, iot_monitor, pest_control, growth_analyze, light_schedule, yield_predict,
    robot_harvest, quality_scan, smart_label, pack_produce, urban_dispatch,
    waste_process, energy_capture, water_recycle
])

# Sequence for setup
A.order.add_edge(seed_select, nutrient_mix)
A.order.add_edge(nutrient_mix, planting_setup)

# From planting to parallel growth & monitoring tasks
for t in [climate_adjust, iot_monitor, pest_control, growth_analyze, light_schedule, yield_predict]:
    A.order.add_edge(planting_setup, t)

# After all growth/monitoring, proceed to harvest
for t in [climate_adjust, iot_monitor, pest_control, growth_analyze, light_schedule, yield_predict]:
    A.order.add_edge(t, robot_harvest)

# Harvest to packaging & dispatch
A.order.add_edge(robot_harvest, quality_scan)
A.order.add_edge(quality_scan, smart_label)
A.order.add_edge(smart_label, pack_produce)
A.order.add_edge(pack_produce, urban_dispatch)

# After distribution, handle waste & recycling
A.order.add_edge(urban_dispatch, waste_process)
A.order.add_edge(waste_process, energy_capture)
A.order.add_edge(energy_capture, water_recycle)

# Define the loop: perform A, then either exit or do skip + A again
root = OperatorPOWL(operator=Operator.LOOP, children=[A, skip])