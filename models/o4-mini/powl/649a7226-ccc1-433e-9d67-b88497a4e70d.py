# Generated from: 649a7226-ccc1-433e-9d67-b88497a4e70d.json
# Description: This process describes the end-to-end supply chain management for an urban vertical farming operation that integrates automated hydroponics, AI-driven crop monitoring, and dynamic distribution logistics. It begins with seed sourcing and nutrient formulation, proceeds through automated germination and growth phases, incorporates environmental adjustments via IoT sensors, and culminates in harvest scheduling. Post-harvest activities include quality scanning, packaging customization based on consumer demand analytics, and last-mile delivery coordination using electric cargo bikes and smart lockers. The process emphasizes minimizing waste through real-time data feedback loops, adaptive inventory management, and proactive customer engagement to optimize freshness and sustainability in an atypical urban agriculture context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_sourcing    = Transition(label='Seed Sourcing')
nutrient_mix     = Transition(label='Nutrient Mix')
germination_start= Transition(label='Germination Start')
growth_monitor   = Transition(label='Growth Monitor')
climate_adjust   = Transition(label='Climate Adjust')
pest_detect      = Transition(label='Pest Detect')
water_recycle    = Transition(label='Water Recycle')
harvest_plan     = Transition(label='Harvest Plan')
quality_scan     = Transition(label='Quality Scan')
custom_pack      = Transition(label='Custom Pack')
inventory_sync   = Transition(label='Inventory Sync')
demand_forecast  = Transition(label='Demand Forecast')
dispatch_prep    = Transition(label='Dispatch Prep')
last_mile        = Transition(label='Last Mile')
customer_notify  = Transition(label='Customer Notify')
feedback_loop    = Transition(label='Feedback Loop')

# Define the environment-adjustment phase as a concurrent PO
env_adjust_po = StrictPartialOrder(nodes=[climate_adjust, pest_detect, water_recycle])
# No order edges => fully concurrent adjustments

# Define the growth-monitoring loop: monitor, then either exit or do adjustments and repeat
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, env_adjust_po]
)

# Build the main linear sequence as a strict partial order
main_seq = StrictPartialOrder(nodes=[
    seed_sourcing,
    nutrient_mix,
    germination_start,
    growth_loop,
    harvest_plan,
    quality_scan,
    demand_forecast,
    custom_pack,
    inventory_sync,
    dispatch_prep,
    last_mile,
    customer_notify
])

# Add the basic sequential dependencies
main_seq.order.add_edge(seed_sourcing, nutrient_mix)
main_seq.order.add_edge(nutrient_mix, germination_start)
main_seq.order.add_edge(germination_start, growth_loop)
main_seq.order.add_edge(growth_loop, harvest_plan)
main_seq.order.add_edge(harvest_plan, quality_scan)
main_seq.order.add_edge(quality_scan, demand_forecast)

# After demand forecast, packaging and inventory sync can proceed in parallel
main_seq.order.add_edge(demand_forecast, custom_pack)
main_seq.order.add_edge(demand_forecast, inventory_sync)

# Both packaging and inventory sync must complete before dispatch prep
main_seq.order.add_edge(custom_pack, dispatch_prep)
main_seq.order.add_edge(inventory_sync, dispatch_prep)
main_seq.order.add_edge(dispatch_prep, last_mile)
main_seq.order.add_edge(last_mile, customer_notify)

# Wrap the whole end-to-end flow in a feedback-loop at the highest level
# Execute main_seq; then choose to exit or do feedback_loop and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_seq, feedback_loop]
)