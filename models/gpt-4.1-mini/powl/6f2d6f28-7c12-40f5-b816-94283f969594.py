# Generated from: 6f2d6f28-7c12-40f5-b816-94283f969594.json
# Description: This process details the comprehensive operational cycle of an urban vertical farm specializing in microgreens and exotic herbs. It includes site preparation with modular hydroponic systems, nutrient solution formulation, seed sourcing from rare cultivars, and continuous environmental monitoring using AI sensors. The process also covers adaptive lighting schedules, pest bio-control deployment, automated harvesting, quality grading, packaging with sustainable materials, and logistics coordination for same-day delivery to local restaurants. Additionally, customer feedback loops are integrated to refine crop varieties and improve yield predictions, ensuring a resilient and innovative urban agriculture model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Prep = Transition(label='Site Prep')
System_Setup = Transition(label='System Setup')
Seed_Sourcing = Transition(label='Seed Sourcing')
Nutrient_Mix = Transition(label='Nutrient Mix')
AI_Monitoring = Transition(label='AI Monitoring')
Light_Adjust = Transition(label='Light Adjust')
Pest_Control = Transition(label='Pest Control')
Growth_Tracking = Transition(label='Growth Tracking')
Harvesting = Transition(label='Harvesting')
Quality_Check = Transition(label='Quality Check')
Packing = Transition(label='Packing')
Labeling = Transition(label='Labeling')
Order_Dispatch = Transition(label='Order Dispatch')
Feedback_Loop = Transition(label='Feedback Loop')
Yield_Analysis = Transition(label='Yield Analysis')
Variety_Update = Transition(label='Variety Update')

# Compose initial preparation partial order: Site Prep then System Setup
prep = StrictPartialOrder(nodes=[Site_Prep, System_Setup])
prep.order.add_edge(Site_Prep, System_Setup)

# Nutrient solution formulation and seed sourcing can be done concurrently after setup
nutrient_seed = StrictPartialOrder(nodes=[Nutrient_Mix, Seed_Sourcing])
# no order edges implies concurrency

# Environmental monitoring via AI sensors runs concurrently with adaptive lighting schedules and pest control
env_monitor = StrictPartialOrder(nodes=[AI_Monitoring, Light_Adjust, Pest_Control])
# no order edges implies concurrency

# Growth tracking continues during growth phase, concurrent with environmental monitoring
growth_phase = StrictPartialOrder(nodes=[Growth_Tracking])
# disconnected single node, effectively alone

# Harvest-related activities strict order:
# Harvesting -> Quality Check -> Packing -> Labeling -> Order Dispatch
harvest_path = StrictPartialOrder(nodes=[Harvesting, Quality_Check, Packing, Labeling, Order_Dispatch])
harvest_path.order.add_edge(Harvesting, Quality_Check)
harvest_path.order.add_edge(Quality_Check, Packing)
harvest_path.order.add_edge(Packing, Labeling)
harvest_path.order.add_edge(Labeling, Order_Dispatch)

# Feedback loop as a loop structure:
# Loop body: Feedback Loop conditional + Yield Analysis + Variety Update
feedback_body = StrictPartialOrder(nodes=[Feedback_Loop, Yield_Analysis, Variety_Update])
feedback_body.order.add_edge(Feedback_Loop, Yield_Analysis)
feedback_body.order.add_edge(Yield_Analysis, Variety_Update)

# The loop executes feedback_body repeatedly until exit
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_body, Variety_Update])
# Note: to model repeated refinement cycle: execute feedback_body,
# then optionally repeat after Variety_Update

# Combine growth phase with env monitoring concurrently (Growth_Tracking concurrent with env_monitor)
growth_and_env = StrictPartialOrder(
    nodes=[Growth_Tracking, AI_Monitoring, Light_Adjust, Pest_Control]
)
# no edges to allow concurrency

# Put all together in a full partial order:
# Preparation -> (Nutrient Mix || Seed Sourcing) -> env_monitor & growth_and_env -> harvest_path -> feedback_loop
# We'll organize the order edges accordingly.

# First build parallel nutrient_seed after prep
prep_nutrient_seed = StrictPartialOrder(nodes=[prep, nutrient_seed])
prep_nutrient_seed.order.add_edge(prep, nutrient_seed)

# But prep and nutrient_seed are themselves partial orders, need to flatten nodes for a single order.
# We'll expand nodes for the root partial order:

all_nodes = [
    Site_Prep, System_Setup,
    Nutrient_Mix, Seed_Sourcing,
    AI_Monitoring, Light_Adjust, Pest_Control, Growth_Tracking,
    Harvesting, Quality_Check, Packing, Labeling, Order_Dispatch,
    feedback_loop
]

root = StrictPartialOrder(nodes=all_nodes)

# Add edges for preparation phase
root.order.add_edge(Site_Prep, System_Setup)

# Setup must precede Nutrient Mix and Seed Sourcing
root.order.add_edge(System_Setup, Nutrient_Mix)
root.order.add_edge(System_Setup, Seed_Sourcing)

# Nutrient Mix and Seed Sourcing must finish before AI Monitoring, Light Adjust, Pest Control, Growth Tracking start
root.order.add_edge(Nutrient_Mix, AI_Monitoring)
root.order.add_edge(Seed_Sourcing, AI_Monitoring)
root.order.add_edge(Nutrient_Mix, Light_Adjust)
root.order.add_edge(Seed_Sourcing, Light_Adjust)
root.order.add_edge(Nutrient_Mix, Pest_Control)
root.order.add_edge(Seed_Sourcing, Pest_Control)
root.order.add_edge(Nutrient_Mix, Growth_Tracking)
root.order.add_edge(Seed_Sourcing, Growth_Tracking)

# Harvesting sequence edges
root.order.add_edge(Growth_Tracking, Harvesting)
root.order.add_edge(Harvesting, Quality_Check)
root.order.add_edge(Quality_Check, Packing)
root.order.add_edge(Packing, Labeling)
root.order.add_edge(Labeling, Order_Dispatch)

# Order Dispatch precedes feedback loop
root.order.add_edge(Order_Dispatch, feedback_loop)

# feedback_loop already defined as operator, so it's treated as a node

# The model is complete