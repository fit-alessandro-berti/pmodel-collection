# Generated from: 69891078-d455-4d86-ba27-16b943beb8cd.json
# Description: This process governs the adaptive urban farming cycle in a smart city environment, integrating real-time environmental data, community feedback, and resource optimization. It begins with soil analysis and proceeds through dynamic seed selection based on seasonal and pollution data. Automated irrigation is adjusted according to microclimate sensors, while drone-assisted pollination enhances yield. Community engagement is maintained through periodic workshops and feedback loops, influencing crop rotation and pest management strategies. Harvesting is coordinated with local markets via blockchain to ensure traceability. Post-harvest processing includes nutrient recycling and waste repurposing, closing the sustainability loop and preparing for the next adaptive cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
soil_test = Transition(label='Soil Test')
seed_select = Transition(label='Seed Select')
data_sync = Transition(label='Data Sync')
irrigation_set = Transition(label='Irrigation Set')
drone_pollinate = Transition(label='Drone Pollinate')
pest_monitor = Transition(label='Pest Monitor')
growth_track = Transition(label='Growth Track')
workshop_host = Transition(label='Workshop Host')
feedback_collect = Transition(label='Feedback Collect')
crop_rotate = Transition(label='Crop Rotate')
harvest_plan = Transition(label='Harvest Plan')
market_sync = Transition(label='Market Sync')
trace_verify = Transition(label='Trace Verify')
nutrient_recycle = Transition(label='Nutrient Recycle')
waste_process = Transition(label='Waste Process')
cycle_review = Transition(label='Cycle Review')

# Loop for Community Engagement & Feedback
# LOOP(workshop_host, XOR(feedback_collect, crop_rotate))
community_loop = OperatorPOWL(operator=Operator.LOOP,
                             children=[
                                 workshop_host,
                                 OperatorPOWL(operator=Operator.XOR,
                                              children=[feedback_collect, crop_rotate])
                             ])

# Loop for Resource optimization loop:
# LOOP(growth_track, pest_monitor)
growth_pest_loop = OperatorPOWL(operator=Operator.LOOP,
                                children=[growth_track, pest_monitor])

# Partial Order for Harvesting activities (sequential)
harvesting = StrictPartialOrder(nodes=[harvest_plan, market_sync, trace_verify])
harvesting.order.add_edge(harvest_plan, market_sync)
harvesting.order.add_edge(market_sync, trace_verify)

# Partial Order for Post-Harvest processing (sequential)
post_harvest = StrictPartialOrder(nodes=[nutrient_recycle, waste_process])
post_harvest.order.add_edge(nutrient_recycle, waste_process)

# Final sustainability cycle review after post-harvest
# Prepare final partial order connecting the main flow

# Build main flow as partial order:
# Soil Test --> Seed Select --> Data Sync --> Irrigation Set --> Drone Pollinate
# Then community_loop and growth_pest_loop run concurrently before harvesting
# So adding edges:
# drone_pollinate --> community_loop
# drone_pollinate --> growth_pest_loop
# community_loop and growth_pest_loop concurrent, both precede harvesting
# harvesting precedes post_harvest
# post_harvest precedes cycle_review

root = StrictPartialOrder(
    nodes=[
        soil_test,
        seed_select,
        data_sync,
        irrigation_set,
        drone_pollinate,
        community_loop,
        growth_pest_loop,
        harvesting,
        post_harvest,
        cycle_review
    ]
)

# Sequential main chain prior to concurrent loops
root.order.add_edge(soil_test, seed_select)
root.order.add_edge(seed_select, data_sync)
root.order.add_edge(data_sync, irrigation_set)
root.order.add_edge(irrigation_set, drone_pollinate)

# drone_pollinate precedes both loops
root.order.add_edge(drone_pollinate, community_loop)
root.order.add_edge(drone_pollinate, growth_pest_loop)

# loops precede harvesting
root.order.add_edge(community_loop, harvesting)
root.order.add_edge(growth_pest_loop, harvesting)

# harvesting precedes post_harvest
root.order.add_edge(harvesting, post_harvest)

# post_harvest precedes cycle_review (closing loop)
root.order.add_edge(post_harvest, cycle_review)