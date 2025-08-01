# Generated from: 69891078-d455-4d86-ba27-16b943beb8cd.json
# Description: This process governs the adaptive urban farming cycle in a smart city environment, integrating real-time environmental data, community feedback, and resource optimization. It begins with soil analysis and proceeds through dynamic seed selection based on seasonal and pollution data. Automated irrigation is adjusted according to microclimate sensors, while drone-assisted pollination enhances yield. Community engagement is maintained through periodic workshops and feedback loops, influencing crop rotation and pest management strategies. Harvesting is coordinated with local markets via blockchain to ensure traceability. Post-harvest processing includes nutrient recycling and waste repurposing, closing the sustainability loop and preparing for the next adaptive cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
soil            = Transition(label='Soil Test')
data_sync       = Transition(label='Data Sync')
seed_select     = Transition(label='Seed Select')
irrigation_set  = Transition(label='Irrigation Set')
drone_pollinate = Transition(label='Drone Pollinate')
growth_track    = Transition(label='Growth Track')
harvest_plan    = Transition(label='Harvest Plan')
market_sync     = Transition(label='Market Sync')
trace_verify    = Transition(label='Trace Verify')
nutrient_recycle= Transition(label='Nutrient Recycle')
waste_process   = Transition(label='Waste Process')
cycle_review    = Transition(label='Cycle Review')

# Define the loop‐body transitions for community engagement
workshop_host    = Transition(label='Workshop Host')
feedback_collect = Transition(label='Feedback Collect')
crop_rotate      = Transition(label='Crop Rotate')
pest_monitor     = Transition(label='Pest Monitor')

# Build the LOOP construct:
#   A = (Workshop Host -> Feedback Collect)
A_loop = StrictPartialOrder(nodes=[workshop_host, feedback_collect])
A_loop.order.add_edge(workshop_host, feedback_collect)
#   B = (Crop Rotate -> Pest Monitor)
B_loop = StrictPartialOrder(nodes=[crop_rotate, pest_monitor])
B_loop.order.add_edge(crop_rotate, pest_monitor)
# LOOP(A, B)
community_loop = OperatorPOWL(operator=Operator.LOOP, children=[A_loop, B_loop])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    soil,
    data_sync,
    seed_select,
    irrigation_set,
    drone_pollinate,
    growth_track,
    community_loop,
    harvest_plan,
    market_sync,
    trace_verify,
    nutrient_recycle,
    waste_process,
    cycle_review
])

# Sequence: Soil Test -> Data Sync -> Seed Select -> Irrigation Set
root.order.add_edge(soil, data_sync)
root.order.add_edge(data_sync, seed_select)
root.order.add_edge(seed_select, irrigation_set)

# After irrigation, three threads run concurrently:
#   Drone Pollinate, Growth Track, Community Engagement Loop
root.order.add_edge(irrigation_set, drone_pollinate)
root.order.add_edge(irrigation_set, growth_track)
root.order.add_edge(irrigation_set, community_loop)

# Harvest planning waits for all three to complete
root.order.add_edge(drone_pollinate, harvest_plan)
root.order.add_edge(growth_track,   harvest_plan)
root.order.add_edge(community_loop,  harvest_plan)

# Harvest Plan -> Market Sync -> Trace Verify
root.order.add_edge(harvest_plan,  market_sync)
root.order.add_edge(market_sync,  trace_verify)

# Post‐harvest processing in parallel: Nutrient Recycle & Waste Process
root.order.add_edge(trace_verify,    nutrient_recycle)
root.order.add_edge(trace_verify,    waste_process)

# Both recycling and waste processing must finish before cycle review
root.order.add_edge(nutrient_recycle, cycle_review)
root.order.add_edge(waste_process,    cycle_review)