# Generated from: 649a7226-ccc1-433e-9d67-b88497a4e70d.json
# Description: This process describes the end-to-end supply chain management for an urban vertical farming operation that integrates automated hydroponics, AI-driven crop monitoring, and dynamic distribution logistics. It begins with seed sourcing and nutrient formulation, proceeds through automated germination and growth phases, incorporates environmental adjustments via IoT sensors, and culminates in harvest scheduling. Post-harvest activities include quality scanning, packaging customization based on consumer demand analytics, and last-mile delivery coordination using electric cargo bikes and smart lockers. The process emphasizes minimizing waste through real-time data feedback loops, adaptive inventory management, and proactive customer engagement to optimize freshness and sustainability in an atypical urban agriculture context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SeedSourcing = Transition(label='Seed Sourcing')
NutrientMix = Transition(label='Nutrient Mix')
GerminationStart = Transition(label='Germination Start')
GrowthMonitor = Transition(label='Growth Monitor')
ClimateAdjust = Transition(label='Climate Adjust')
PestDetect = Transition(label='Pest Detect')
WaterRecycle = Transition(label='Water Recycle')
HarvestPlan = Transition(label='Harvest Plan')
QualityScan = Transition(label='Quality Scan')
CustomPack = Transition(label='Custom Pack')
InventorySync = Transition(label='Inventory Sync')
DemandForecast = Transition(label='Demand Forecast')
DispatchPrep = Transition(label='Dispatch Prep')
LastMile = Transition(label='Last Mile')
CustomerNotify = Transition(label='Customer Notify')
FeedbackLoop = Transition(label='Feedback Loop')

# Seed Sourcing --> Nutrient Mix --> Germination Start
initial_phase = StrictPartialOrder(nodes=[SeedSourcing, NutrientMix, GerminationStart])
initial_phase.order.add_edge(SeedSourcing, NutrientMix)
initial_phase.order.add_edge(NutrientMix, GerminationStart)

# Growth phase includes Growth Monitor, Climate Adjust, Pest Detect, Water Recycle concurrently
growth_phase = StrictPartialOrder(nodes=[GrowthMonitor, ClimateAdjust, PestDetect, WaterRecycle])

# After the concurrent growth phase, plan the harvest
after_growth = StrictPartialOrder(nodes=[growth_phase, HarvestPlan])
after_growth.order.add_edge(growth_phase, HarvestPlan)

# Post-harvest activities Quality Scan and Custom Pack in sequence
post_harvest_packaging = StrictPartialOrder(nodes=[QualityScan, CustomPack])
post_harvest_packaging.order.add_edge(QualityScan, CustomPack)

# Inventory sync and demand forecast concurrently after packaging
inventory_and_demand = StrictPartialOrder(nodes=[InventorySync, DemandForecast])

# Dispatch prep after InventorySync and DemandForecast both finish
dispatch_prep_phase = StrictPartialOrder(nodes=[inventory_and_demand, DispatchPrep])
dispatch_prep_phase.order.add_edge(inventory_and_demand, DispatchPrep)

# Last Mile and Customer Notify concurrently after Dispatch Prep
delivery_phase = StrictPartialOrder(nodes=[LastMile, CustomerNotify])
# Link DispatchPrep --> last mile and customer notify
delivery_link = StrictPartialOrder(nodes=[dispatch_prep_phase, delivery_phase])
delivery_link.order.add_edge(dispatch_prep_phase, delivery_phase)

# Feedback Loop as a loop repeating monitoring phases and inventory/demand cycle
# Loop body A: Growth phase + after growth + post harvest packaging + inventory and demand + dispatch prep + delivery
loop_body = StrictPartialOrder(nodes=[
    growth_phase,
    after_growth,
    post_harvest_packaging,
    inventory_and_demand,
    dispatch_prep_phase,
    delivery_phase
])
# Define orderings inside loop_body to chain these parts
loop_body.order.add_edge(growth_phase, after_growth)
loop_body.order.add_edge(after_growth, post_harvest_packaging)
loop_body.order.add_edge(post_harvest_packaging, inventory_and_demand)
loop_body.order.add_edge(inventory_and_demand, dispatch_prep_phase)
loop_body.order.add_edge(dispatch_prep_phase, delivery_phase)

# Loop "B" is Feedback Loop activity
loop_B = FeedbackLoop

# Create loop node: * (loop_body, FeedbackLoop)
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_B])

# Initial phase + loop_node + HarvestPlan repeated is not accurate, so
# the overall process begins with initial_phase then loop over growth & downstream

root = StrictPartialOrder(nodes=[initial_phase, loop_node])
root.order.add_edge(initial_phase, loop_node)