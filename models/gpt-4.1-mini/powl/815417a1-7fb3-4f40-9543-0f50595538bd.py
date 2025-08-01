# Generated from: 815417a1-7fb3-4f40-9543-0f50595538bd.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a constrained city environment. It includes site evaluation considering sunlight and zoning laws, modular structure design, hydroponic system integration, nutrient solution formulation, automated climate control setup, plant species selection for optimal yield, continuous monitoring and data analytics for growth optimization, pest and disease management using integrated pest management techniques, workforce training on specialized equipment, community engagement for sustainable support, logistics planning for harvest distribution, and iterative feedback loops to refine operational efficiency and sustainability in a rapidly changing urban ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
site_survey = Transition(label='Site Survey')
zoning_review = Transition(label='Zoning Review')
modular_design = Transition(label='Modular Design')
hydroponic_setup = Transition(label='Hydroponic Setup')
nutrient_mix = Transition(label='Nutrient Mix')
climate_control = Transition(label='Climate Control')
species_select = Transition(label='Species Select')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
worker_training = Transition(label='Worker Training')
community_meet = Transition(label='Community Meet')
harvest_plan = Transition(label='Harvest Plan')
data_analyze = Transition(label='Data Analyze')
logistics_map = Transition(label='Logistics Map')
feedback_loop = Transition(label='Feedback Loop')

# Initial phase: Site Survey and Zoning Review can be done concurrently (PO with no order)
init_phase = StrictPartialOrder(nodes=[site_survey, zoning_review])

# Design and setup phase with partial order representing dependencies
design_setup = StrictPartialOrder(nodes=[modular_design, hydroponic_setup, nutrient_mix, climate_control])
design_setup.order.add_edge(modular_design, hydroponic_setup)    # design before hydroponic setup
design_setup.order.add_edge(modular_design, nutrient_mix)        # design before nutrient mix
design_setup.order.add_edge(modular_design, climate_control)     # design before climate control

# Species selection after design and setup phase (strictly after)
species_selection = species_select

# Monitoring and control activities can be partially ordered
monitoring = StrictPartialOrder(nodes=[growth_monitor, pest_control, data_analyze])
# No explicit order (concurrent monitoring activities)

# Loop phase: iterative feedback for refinement
# Loop executes: Feedback Loop then monitoring & control activities, then worker training & community meeting
# After this, loop chooses to either exit or repeat

monitor_and_control = StrictPartialOrder(
    nodes=[growth_monitor, pest_control, data_analyze]
)
# No edges - concurrent

worker_training_node = worker_training
community_meet_node = community_meet

# Combine worker training and community meeting as concurrent
training_community = StrictPartialOrder(nodes=[worker_training_node, community_meet_node])

# After monitoring, do training/community meeting and plan harvest/logistics concurrently
harvest_logistics = StrictPartialOrder(nodes=[harvest_plan, logistics_map])
# No order edges - concurrent

# Combine training_community and harvest_logistics as concurrent
post_monitoring = StrictPartialOrder(nodes=[training_community, harvest_logistics])

# Since training_community and harvest_logistics are StrictPartialOrders, 'nodes' contain POWL models, 
# So flatten nodes for proper POWL model:
post_monitoring = StrictPartialOrder(nodes=[worker_training_node, community_meet_node, harvest_plan, logistics_map])
# No order edges, all concurrent

# Loop body B = sequence: feedback_loop -> monitoring -> post_monitoring
# Since POWL PO only supports partial order, create partial order combining these activities with order edges
loop_body_B = StrictPartialOrder(
    nodes=[feedback_loop, growth_monitor, pest_control, data_analyze,
           worker_training_node, community_meet_node, harvest_plan, logistics_map]
)
# feedback_loop before monitoring activities
loop_body_B.order.add_edge(feedback_loop, growth_monitor)
loop_body_B.order.add_edge(feedback_loop, pest_control)
loop_body_B.order.add_edge(feedback_loop, data_analyze)
# monitoring before post_monitoring activities
for mon_node in [growth_monitor, pest_control, data_analyze]:
    for post_node in [worker_training_node, community_meet_node, harvest_plan, logistics_map]:
        loop_body_B.order.add_edge(mon_node, post_node)

# Define the loop: * (species_select, loop_body_B)
loop = OperatorPOWL(operator=Operator.LOOP, children=[species_selection, loop_body_B])

# Full process order:
# (init_phase) -> (design_setup) -> loop
# Create a PO combining these three nodes and define edges accordingly
root = StrictPartialOrder(nodes=[init_phase, design_setup, loop])
root.order.add_edge(init_phase, design_setup)
root.order.add_edge(design_setup, loop)