# Generated from: 82341c76-b317-4a72-bcca-9de1b2895ade.json
# Description: This process manages the end-to-end supply chain for urban farming operations, integrating multiple stakeholders such as vertical farms, local suppliers, and distribution hubs. It starts with seed sourcing from specialized vendors, includes hydroponic nutrient formulation, real-time environmental monitoring, and automated crop harvesting using AI-powered robotics. The process also involves quality checks tailored for microgreen varieties, dynamic inventory adjustment based on environmental feedback, and last-mile delivery using electric cargo bikes to minimize carbon footprint. Additionally, it incorporates waste recycling by converting organic residues into biofertilizers, ensuring sustainability. The process requires coordination between software platforms for farm management, logistics, and customer relationship management to maintain a seamless flow from seed to consumer in densely populated urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
seed = Transition(label="Seed Sourcing")
nutrient = Transition(label="Nutrient Mix")
env = Transition(label="Env Monitoring")
crop = Transition(label="Crop Seeding")
growth = Transition(label="Growth Tracking")
pest = Transition(label="Pest Scanning")
harvest = Transition(label="Automated Harvest")
quality = Transition(label="Quality Check")
waste_sort = Transition(label="Waste Sorting")
bio_prep = Transition(label="Biofertilizer Prep")
inventory = Transition(label="Inventory Update")
order_alloc = Transition(label="Order Allocation")
route_plan = Transition(label="Route Planning")
bike_dispatch = Transition(label="Bike Dispatch")
feedback = Transition(label="Customer Feedback")
data_sync = Transition(label="Data Sync")

# Loop for continuous growth tracking and pest scanning
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth, pest]
)

# Waste‐handling subprocess (exclusive branch)
# If quality fails, do waste sorting and biofertilizer prep; otherwise skip
skip = SilentTransition()
waste_proc = StrictPartialOrder(nodes=[waste_sort, bio_prep])
waste_proc.order.add_edge(waste_sort, bio_prep)

quality_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[skip, waste_proc]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    seed,
    nutrient,
    crop,
    env,
    growth_loop,
    harvest,
    quality,
    quality_choice,
    inventory,
    order_alloc,
    route_plan,
    bike_dispatch,
    feedback,
    data_sync
])

# Add the control‐flow dependencies
root.order.add_edge(seed, nutrient)
root.order.add_edge(nutrient, crop)
# After seeding, start environmental monitoring in parallel with the growth loop
root.order.add_edge(crop, env)
root.order.add_edge(crop, growth_loop)
# After growth/pest loop, proceed to harvest and quality check
root.order.add_edge(growth_loop, harvest)
root.order.add_edge(harvest, quality)
# After quality, choose waste handling or skip, then update inventory
root.order.add_edge(quality, quality_choice)
root.order.add_edge(quality_choice, inventory)
# Delivery sub‐process
root.order.add_edge(inventory, order_alloc)
root.order.add_edge(order_alloc, route_plan)
root.order.add_edge(route_plan, bike_dispatch)
root.order.add_edge(bike_dispatch, feedback)

# 'data_sync' is left unconstrained to represent ongoing background synchronization