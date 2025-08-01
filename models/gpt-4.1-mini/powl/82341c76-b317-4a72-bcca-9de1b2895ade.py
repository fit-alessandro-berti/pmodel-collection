# Generated from: 82341c76-b317-4a72-bcca-9de1b2895ade.json
# Description: This process manages the end-to-end supply chain for urban farming operations, integrating multiple stakeholders such as vertical farms, local suppliers, and distribution hubs. It starts with seed sourcing from specialized vendors, includes hydroponic nutrient formulation, real-time environmental monitoring, and automated crop harvesting using AI-powered robotics. The process also involves quality checks tailored for microgreen varieties, dynamic inventory adjustment based on environmental feedback, and last-mile delivery using electric cargo bikes to minimize carbon footprint. Additionally, it incorporates waste recycling by converting organic residues into biofertilizers, ensuring sustainability. The process requires coordination between software platforms for farm management, logistics, and customer relationship management to maintain a seamless flow from seed to consumer in densely populated urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Sourcing = Transition(label='Seed Sourcing')
Nutrient_Mix = Transition(label='Nutrient Mix')
Env_Monitoring = Transition(label='Env Monitoring')
Crop_Seeding = Transition(label='Crop Seeding')
Growth_Tracking = Transition(label='Growth Tracking')
Pest_Scanning = Transition(label='Pest Scanning')
Automated_Harvest = Transition(label='Automated Harvest')
Quality_Check = Transition(label='Quality Check')
Waste_Sorting = Transition(label='Waste Sorting')
Biofertilizer_Prep = Transition(label='Biofertilizer Prep')
Inventory_Update = Transition(label='Inventory Update')
Order_Allocation = Transition(label='Order Allocation')
Route_Planning = Transition(label='Route Planning')
Bike_Dispatch = Transition(label='Bike Dispatch')
Customer_Feedback = Transition(label='Customer Feedback')
Data_Sync = Transition(label='Data Sync')

# Create partial orders for concurrent/ordered steps

# 1) Initial supply and preparation phase:
# Seed Sourcing --> Nutrient Mix --> Env Monitoring
initial_supply = StrictPartialOrder(nodes=[Seed_Sourcing, Nutrient_Mix, Env_Monitoring])
initial_supply.order.add_edge(Seed_Sourcing, Nutrient_Mix)
initial_supply.order.add_edge(Nutrient_Mix, Env_Monitoring)

# 2) Planting and growth monitoring phase
# Crop Seeding AND Growth Tracking (concurrent activities)
# Pest Scanning depends on Growth Tracking
planting_growth = StrictPartialOrder(nodes=[Crop_Seeding, Growth_Tracking, Pest_Scanning])
planting_growth.order.add_edge(Growth_Tracking, Pest_Scanning)
# Crop Seeding can be concurrent with Growth Tracking (no order edges)

# 3) Harvest and quality check phase
# Automated Harvest --> Quality Check
harvest_quality = StrictPartialOrder(nodes=[Automated_Harvest, Quality_Check])
harvest_quality.order.add_edge(Automated_Harvest, Quality_Check)

# 4) Waste recycling phase:
# Waste Sorting --> Biofertilizer Prep (loop)
# Loop structure: do Waste Sorting, then optionally repeat Biofertilizer Prep and Waste Sorting
waste_sorting = Waste_Sorting
biofertilizer_prep = Biofertilizer_Prep
waste_recycling_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_sorting, biofertilizer_prep])

# 5) Inventory and distribution phase
# Inventory Update --> Order Allocation --> Route Planning --> Bike Dispatch
inventory_distribution = StrictPartialOrder(
    nodes=[Inventory_Update, Order_Allocation, Route_Planning, Bike_Dispatch]
)
inventory_distribution.order.add_edge(Inventory_Update, Order_Allocation)
inventory_distribution.order.add_edge(Order_Allocation, Route_Planning)
inventory_distribution.order.add_edge(Route_Planning, Bike_Dispatch)

# 6) Feedback and data synchronization phase
# Customer Feedback --> Data Sync
feedback_sync = StrictPartialOrder(nodes=[Customer_Feedback, Data_Sync])
feedback_sync.order.add_edge(Customer_Feedback, Data_Sync)

# The overall coordination:
# initial_supply --> planting_growth --> harvest_quality
# harvest_quality --> waste_recycling_loop AND inventory_distribution (concurrent)
# inventory_distribution --> feedback_sync

# Combine: waste_recycling_loop and inventory_distribution are concurrent after harvest_quality
post_harvest = StrictPartialOrder(
    nodes=[harvest_quality, waste_recycling_loop, inventory_distribution]
)
post_harvest.order.add_edge(harvest_quality, waste_recycling_loop)
post_harvest.order.add_edge(harvest_quality, inventory_distribution)

# Finally:
# initial_supply --> planting_growth --> post_harvest --> feedback_sync

step1_2 = StrictPartialOrder(nodes=[initial_supply, planting_growth])
step1_2.order.add_edge(initial_supply, planting_growth)

step1_3post = StrictPartialOrder(nodes=[step1_2, post_harvest])
step1_3post.order.add_edge(step1_2, post_harvest)

root = StrictPartialOrder(nodes=[step1_3post, feedback_sync])
root.order.add_edge(step1_3post, feedback_sync)