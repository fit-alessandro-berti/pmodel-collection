# Generated from: 3fbaa29e-7ef5-4694-b0f1-4df73c362f8a.json
# Description: This process outlines a complex, adaptive urban farming cycle designed to optimize crop yield in limited city spaces by integrating real-time environmental data, community feedback, and resource constraints. It involves iterative soil conditioning, microclimate analysis, automated nutrient dosing, and crop rotation scheduling. The process also incorporates waste recycling from urban sources, pest control using biological agents, and continuous monitoring of plant health through IoT sensors. Community engagement through crowdsourced data and educational workshops further refines the system, ensuring sustainability and responsiveness to changing urban conditions. The process concludes with yield assessment and redistribution planning to local markets and food banks, closing the loop on urban food production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
soil_testing      = Transition(label='Soil Testing')
microclimate_scan = Transition(label='Microclimate Scan')
nutrient_dosing   = Transition(label='Nutrient Dosing')
seed_selection    = Transition(label='Seed Selection')
planting_setup    = Transition(label='Planting Setup')
waste_recycling   = Transition(label='Waste Recycling')
pest_control      = Transition(label='Pest Control')
sensor_monitoring = Transition(label='Sensor Monitoring')
water_scheduling  = Transition(label='Water Scheduling')
growth_analysis   = Transition(label='Growth Analysis')
community_input   = Transition(label='Community Input')
workshop_hosting  = Transition(label='Workshop Hosting')
crop_rotation     = Transition(label='Crop Rotation')
yield_assessment  = Transition(label='Yield Assessment')
market_planning   = Transition(label='Market Planning')
redistribution    = Transition(label='Redistribution')

# A_loop = the monitoring & analysis steps done each iteration
A_loop = StrictPartialOrder(nodes=[sensor_monitoring, water_scheduling, growth_analysis])
A_loop.order.add_edge(sensor_monitoring, water_scheduling)
A_loop.order.add_edge(water_scheduling, growth_analysis)

# B_loop = the adaptive actions in the loop body
# Community engagement is an exclusive choice between direct input or a workshop
xor_community = OperatorPOWL(operator=Operator.XOR, children=[community_input, workshop_hosting])

B_loop = StrictPartialOrder(nodes=[pest_control, waste_recycling, xor_community, crop_rotation])
B_loop.order.add_edge(pest_control, waste_recycling)
B_loop.order.add_edge(waste_recycling, xor_community)
B_loop.order.add_edge(xor_community, crop_rotation)

# The main loop: do A_loop, then either exit or do B_loop and then repeat
main_loop = OperatorPOWL(operator=Operator.LOOP, children=[A_loop, B_loop])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    soil_testing,
    microclimate_scan,
    nutrient_dosing,
    seed_selection,
    planting_setup,
    main_loop,
    yield_assessment,
    market_planning,
    redistribution
])

# Sequence the nodes
root.order.add_edge(soil_testing,      microclimate_scan)
root.order.add_edge(microclimate_scan, nutrient_dosing)
root.order.add_edge(nutrient_dosing,   seed_selection)
root.order.add_edge(seed_selection,    planting_setup)
root.order.add_edge(planting_setup,    main_loop)

# After exiting the loop, final assessment and distribution
root.order.add_edge(main_loop,     yield_assessment)
root.order.add_edge(yield_assessment, market_planning)
root.order.add_edge(market_planning,  redistribution)