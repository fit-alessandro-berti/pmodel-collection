# Generated from: 92e6d216-ab86-4e8b-9787-4e6d0385f0e5.json
# Description: This process outlines the comprehensive workflow for managing an urban vertical farm, integrating advanced hydroponics and AI-driven environmental controls. Starting from seed selection and germination, it includes nutrient solution preparation, automated lighting adjustments, pest monitoring using drones, and real-time growth analytics. Harvesting is synchronized with market demand forecasts, followed by quality inspection, packaging, and distribution through smart logistics. Waste recycling and system maintenance are continuous to ensure sustainability and operational efficiency in a confined urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Selection = Transition(label='Seed Selection')
Germination_Start = Transition(label='Germination Start')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Adjust = Transition(label='Lighting Adjust')
Climate_Control = Transition(label='Climate Control')
Pest_Drone = Transition(label='Pest Drone')
Growth_Scan = Transition(label='Growth Scan')
Water_Cycle = Transition(label='Water Cycle')
Harvest_Sync = Transition(label='Harvest Sync')
Quality_Check = Transition(label='Quality Check')
Pack_Produce = Transition(label='Pack Produce')
Smart_Dispatch = Transition(label='Smart Dispatch')
Waste_Recycle = Transition(label='Waste Recycle')
System_Clean = Transition(label='System Clean')
Data_Analyze = Transition(label='Data Analyze')
Market_Forecast = Transition(label='Market Forecast')

# The main flow before harvesting:
# Seed Selection --> Germination Start --> Nutrient Mix --> Lighting Adjust & Climate Control (parallel) 
# --> Pest Drone --> Growth Scan --> Water Cycle --> Harvest Sync --> Market Forecast

# Lighting Adjust and Climate Control are concurrent (no ordering between them)

pre_harvest_nodes = [
    Seed_Selection,
    Germination_Start,
    Nutrient_Mix,
    Lighting_Adjust,
    Climate_Control,
    Pest_Drone,
    Growth_Scan,
    Water_Cycle,
    Harvest_Sync,
    Market_Forecast,
]

pre_harvest_po = StrictPartialOrder(nodes=pre_harvest_nodes)
pre_harvest_po.order.add_edge(Seed_Selection, Germination_Start)
pre_harvest_po.order.add_edge(Germination_Start, Nutrient_Mix)

# Nutrient Mix precedes both Lighting Adjust and Climate Control, which run concurrently
pre_harvest_po.order.add_edge(Nutrient_Mix, Lighting_Adjust)
pre_harvest_po.order.add_edge(Nutrient_Mix, Climate_Control)

# Lighting Adjust and Climate Control complete before Pest Drone
pre_harvest_po.order.add_edge(Lighting_Adjust, Pest_Drone)
pre_harvest_po.order.add_edge(Climate_Control, Pest_Drone)

pre_harvest_po.order.add_edge(Pest_Drone, Growth_Scan)
pre_harvest_po.order.add_edge(Growth_Scan, Water_Cycle)
pre_harvest_po.order.add_edge(Water_Cycle, Harvest_Sync)

# Harvest Sync and Market Forecast run in parallel, but Harvest Sync must precede further activities, and Market Forecast participates later
# But from description Harvest Sync synchronized with Market Forecast forecasts, implies that Market Forecast is after Harvest Sync (or concurrent)
# We put Harvest_Sync --> Market_Forecast

pre_harvest_po.order.add_edge(Harvest_Sync, Market_Forecast)

# After harvest & forecast: Quality Check --> Pack Produce --> Smart Dispatch
post_harvest_nodes = [Quality_Check, Pack_Produce, Smart_Dispatch]

post_harvest_po = StrictPartialOrder(nodes=post_harvest_nodes)
post_harvest_po.order.add_edge(Quality_Check, Pack_Produce)
post_harvest_po.order.add_edge(Pack_Produce, Smart_Dispatch)

# Waste Recycle and System Clean run continuously (loop)
# Model continuous Waste Recycle and System Clean as a loop:
# Loop body: execute (Waste Recycle and System Clean in parallel), then loop back, option to exit

# Waste Recycle and System Clean concurrent in loop body
maintenance_nodes = [Waste_Recycle, System_Clean]
maintenance_po = StrictPartialOrder(nodes=maintenance_nodes)
# no order edges between Waste Recycle and System Clean for concurrency

maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    maintenance_po,
    SilentTransition()  # silent transition as the "do nothing and exit" option in loop
])

# Data Analyze is real-time growth analytics, from description likely concurrent with many activities,
# but we put Data Analyze concurrent with the post_harvest process and the maintenance_loop

# Create a combined post harvest + market forecast + data analyze
post_harvest_plus = StrictPartialOrder(nodes=[post_harvest_po, Market_Forecast, Data_Analyze])

# But pm4py's StrictPartialOrder expects nodes list, not sub POWL.
# We must combine them all into a single PO with all nodes from post_harvest_po, Market_Forecast and Data_Analyze:
combined_post_nodes = [Quality_Check, Pack_Produce, Smart_Dispatch, Market_Forecast, Data_Analyze]
combined_post_po = StrictPartialOrder(nodes=combined_post_nodes)

# Add the ordering edges from post_harvest_po
combined_post_po.order.add_edge(Quality_Check, Pack_Produce)
combined_post_po.order.add_edge(Pack_Produce, Smart_Dispatch)

# Market_Forecast and Data_Analyze concurrent with others, so no additional edges.

# Final model: 
# pre_harvest_po --> combined_post_po and concurrent with maintenance_loop

# Combine pre_harvest, combined_post_po and maintenance_loop nodes
all_nodes = [pre_harvest_po, combined_post_po, maintenance_loop]

root = StrictPartialOrder(nodes=all_nodes)
root.order.add_edge(pre_harvest_po, combined_post_po)
# No order edge between maintenance_loop and others => concurrent with all
