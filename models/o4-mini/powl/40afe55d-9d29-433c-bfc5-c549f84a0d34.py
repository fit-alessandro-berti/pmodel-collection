# Generated from: 40afe55d-9d29-433c-bfc5-c549f84a0d34.json
# Description: This process details the comprehensive cycle of managing an urban vertical farm that integrates hydroponics, AI-driven environmental controls, and community engagement programs. It begins with crop selection based on market trends and climate data, followed by nutrient solution formulation and system calibration. Continuous monitoring of plant health and automated pest detection occur throughout growth stages. Harvesting is synchronized with distribution logistics tailored to local markets. Post-harvest, biomass recycling and waste reduction initiatives are implemented. The process also includes data aggregation for yield optimization and community workshops to promote sustainable urban agriculture. Overall, it combines advanced technology with social responsibility to create a resilient food production ecosystem in dense urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
crop_select     = Transition(label='Crop Select')
trend_analyze   = Transition(label='Trend Analyze')
nutrient_mix    = Transition(label='Nutrient Mix')
system_calibrate= Transition(label='System Calibrate')
seed_germinate  = Transition(label='Seed Germinate')
env_monitor     = Transition(label='Env Monitor')
pest_detect     = Transition(label='Pest Detect')
growth_adjust   = Transition(label='Growth Adjust')
harvest_plan    = Transition(label='Harvest Plan')
crop_harvest    = Transition(label='Crop Harvest')
pack_logistics  = Transition(label='Pack Logistics')
market_distribute = Transition(label='Market Distribute')
biomass_recycle = Transition(label='Biomass Recycle')
waste_reduce    = Transition(label='Waste Reduce')
data_aggregate  = Transition(label='Data Aggregate')
yield_optimize  = Transition(label='Yield Optimize')
community_train = Transition(label='Community Train')
feedback_collect= Transition(label='Feedback Collect')

# Silent transition for loop exit
skip = SilentTransition()

# Build the main body as a strict partial order
body = StrictPartialOrder(nodes=[
    trend_analyze, crop_select,
    nutrient_mix, system_calibrate,
    seed_germinate,
    env_monitor, pest_detect, growth_adjust,
    harvest_plan, crop_harvest, pack_logistics, market_distribute,
    biomass_recycle, waste_reduce,
    data_aggregate, yield_optimize,
    community_train, feedback_collect
])

# Define the control-flow (partial order) edges
# 1. Crop selection based on trend analysis
body.order.add_edge(trend_analyze, crop_select)

# 2. Nutrient solution formulation and system calibration
body.order.add_edge(crop_select, nutrient_mix)
body.order.add_edge(nutrient_mix, system_calibrate)

# 3. Seed germination
body.order.add_edge(system_calibrate, seed_germinate)

# 4. Continuous monitoring & pest detection & growth adjustments
body.order.add_edge(seed_germinate, env_monitor)
body.order.add_edge(seed_germinate, pest_detect)
body.order.add_edge(seed_germinate, growth_adjust)

# They all feed into harvest planning
body.order.add_edge(env_monitor, harvest_plan)
body.order.add_edge(pest_detect, harvest_plan)
body.order.add_edge(growth_adjust, harvest_plan)

# 5. Harvest & distribution
body.order.add_edge(harvest_plan, crop_harvest)
body.order.add_edge(crop_harvest, pack_logistics)
body.order.add_edge(pack_logistics, market_distribute)

# 6. Post-harvest recycling & waste reduction
body.order.add_edge(market_distribute, biomass_recycle)
body.order.add_edge(market_distribute, waste_reduce)

# 7. Data aggregation & yield optimization
body.order.add_edge(biomass_recycle, data_aggregate)
body.order.add_edge(waste_reduce, data_aggregate)
body.order.add_edge(data_aggregate, yield_optimize)

# 8. Community engagement & feedback
body.order.add_edge(yield_optimize, community_train)
body.order.add_edge(community_train, feedback_collect)

# Wrap the entire cycle in a loop (repeat or exit)
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[body, skip]
)