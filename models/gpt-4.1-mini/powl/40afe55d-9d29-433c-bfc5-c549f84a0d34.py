# Generated from: 40afe55d-9d29-433c-bfc5-c549f84a0d34.json
# Description: This process details the comprehensive cycle of managing an urban vertical farm that integrates hydroponics, AI-driven environmental controls, and community engagement programs. It begins with crop selection based on market trends and climate data, followed by nutrient solution formulation and system calibration. Continuous monitoring of plant health and automated pest detection occur throughout growth stages. Harvesting is synchronized with distribution logistics tailored to local markets. Post-harvest, biomass recycling and waste reduction initiatives are implemented. The process also includes data aggregation for yield optimization and community workshops to promote sustainable urban agriculture. Overall, it combines advanced technology with social responsibility to create a resilient food production ecosystem in dense urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Crop_Select = Transition(label='Crop Select')
Trend_Analyze = Transition(label='Trend Analyze')
Nutrient_Mix = Transition(label='Nutrient Mix')
System_Calibrate = Transition(label='System Calibrate')
Seed_Germinate = Transition(label='Seed Germinate')
Env_Monitor = Transition(label='Env Monitor')
Pest_Detect = Transition(label='Pest Detect')
Growth_Adjust = Transition(label='Growth Adjust')
Harvest_Plan = Transition(label='Harvest Plan')
Crop_Harvest = Transition(label='Crop Harvest')
Pack_Logistics = Transition(label='Pack Logistics')
Market_Distribute = Transition(label='Market Distribute')
Biomass_Recycle = Transition(label='Biomass Recycle')
Waste_Reduce = Transition(label='Waste Reduce')
Data_Aggregate = Transition(label='Data Aggregate')
Yield_Optimize = Transition(label='Yield Optimize')
Community_Train = Transition(label='Community Train')
Feedback_Collect = Transition(label='Feedback Collect')

# The process structure:
# Crop Select -> Trend Analyze -> Nutrient Mix -> System Calibrate -> Seed Germinate
# Then Growth phases with Env Monitor, Pest Detect, Growth Adjust concurrent and looping until harvest planned
# Harvest Plan -> Crop Harvest -> Pack Logistics -> Market Distribute
# After Harvest: Biomass Recycle -> Waste Reduce
# Parallel: Data Aggregate -> Yield Optimize (optimization data flow)
# Community Train -> Feedback Collect (community engagement cycle)

# Loop for growth monitoring and adjustment:
# Loop body B: concurrent Env Monitor, Pest Detect, Growth Adjust
growth_monitoring = StrictPartialOrder(nodes=[Env_Monitor, Pest_Detect, Growth_Adjust])

# For concurrency no edges between Env Monitor, Pest Detect, Growth Adjust in growth_monitoring

# The growth loop: after Seed Germinate, loop between:
# A = Harvest Plan (we execute growth cycles until we decide to plan harvest)
# B = growth monitoring phase (monitor and adjust growth)
# However, loop semantics is * (A, B): execute A, then choose to exit or execute B then A again
# This does not match harvest planning being after loops, so reverse roles:
# * (growth_monitoring, Harvest Plan) means:
# execute growth_monitoring, then choose to exit or execute Harvest Plan then growth_monitoring again
# This fits better since after monitoring cycles, we can plan harvest.

# So loop is * (growth_monitoring, Harvest Plan)

growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, Harvest_Plan])

# After harvest plan, plan harvest and subsequent distribution logistics happen sequentially:
post_harvest = StrictPartialOrder(nodes=[Crop_Harvest, Pack_Logistics, Market_Distribute])
post_harvest.order.add_edge(Crop_Harvest, Pack_Logistics)
post_harvest.order.add_edge(Pack_Logistics, Market_Distribute)

# After distribution: biomass recycle and waste reduce in sequence
recycle_waste = StrictPartialOrder(nodes=[Biomass_Recycle, Waste_Reduce])
recycle_waste.order.add_edge(Biomass_Recycle, Waste_Reduce)

# Data aggregation and yield optimization sequential
data_opt = StrictPartialOrder(nodes=[Data_Aggregate, Yield_Optimize])
data_opt.order.add_edge(Data_Aggregate, Yield_Optimize)

# Community training and feedback also sequential
community_cycle = StrictPartialOrder(nodes=[Community_Train, Feedback_Collect])
community_cycle.order.add_edge(Community_Train, Feedback_Collect)

# The main process partial order:
# Initial sequence: Crop Select -> Trend Analyze -> Nutrient Mix -> System Calibrate -> Seed Germinate
init_seq = StrictPartialOrder(nodes=[Crop_Select, Trend_Analyze, Nutrient_Mix, System_Calibrate, Seed_Germinate])
init_seq.order.add_edge(Crop_Select, Trend_Analyze)
init_seq.order.add_edge(Trend_Analyze, Nutrient_Mix)
init_seq.order.add_edge(Nutrient_Mix, System_Calibrate)
init_seq.order.add_edge(System_Calibrate, Seed_Germinate)

# After Seed Germinate, growth loop starts
# After growth loop finishes (we exit the loop on Harvest Plan branch):
# then post harvest sequence
# data_opt and community_cycle are concurrent with recycle_waste and post_harvest but start only after growth loop finished

# We combine the post_harvest, recycle_waste, data_opt, community_cycle in concurrency with orderings:
# post_harvest -> recycle_waste (done)
# data_opt and community_cycle concurrent with recycle_waste/post_harvest

# We make a StrictPartialOrder with nodes = [init_seq, growth_loop, post_harvest, recycle_waste, data_opt, community_cycle]
# Add edges:
# init_seq -> growth_loop
# growth_loop -> post_harvest
# post_harvest -> recycle_waste
# and data_opt, community_cycle are concurrent with post_harvest and recycle_waste but start after growth_loop

root = StrictPartialOrder(
    nodes=[init_seq, growth_loop, post_harvest, recycle_waste, data_opt, community_cycle]
)

# Add edges defining the partial order between these sub-processes
root.order.add_edge(init_seq, growth_loop)
root.order.add_edge(growth_loop, post_harvest)
root.order.add_edge(post_harvest, recycle_waste)
root.order.add_edge(growth_loop, data_opt)
root.order.add_edge(growth_loop, community_cycle)

# No edges between data_opt and community_cycle or with recycle_waste to keep concurrency
