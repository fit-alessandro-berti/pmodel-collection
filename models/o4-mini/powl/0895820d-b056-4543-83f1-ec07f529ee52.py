# Generated from: 0895820d-b056-4543-83f1-ec07f529ee52.json
# Description: This process outlines the end-to-end operational workflow for managing an urban vertical farm that integrates IoT sensors, automated hydroponic systems, and AI-driven crop optimization. Starting from environmental monitoring, nutrient mixing, and seed planting, the workflow continues through growth tracking, pest detection, and adaptive lighting adjustments. Harvest scheduling is dynamically optimized based on market demand forecasts, followed by automated packaging and distribution coordination with local vendors. The process also includes waste recycling, energy consumption analysis, and continuous improvement cycles driven by data insights to maximize yield and minimize resource use in constrained urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activity transitions
sensorSync     = Transition(label="Sensor Sync")
nutrientMix    = Transition(label="Nutrient Mix")
seedPlant      = Transition(label="Seed Plant")
climateAdjust  = Transition(label="Climate Adjust")
growthTrack    = Transition(label="Growth Track")
pestScan       = Transition(label="Pest Scan")
lightModulate  = Transition(label="Light Modulate")
marketForecast = Transition(label="Market Forecast")
harvestPlan    = Transition(label="Harvest Plan")
packagePrep    = Transition(label="Package Prep")
vendorNotify   = Transition(label="Vendor Notify")
wasteSort      = Transition(label="Waste Sort")
energyAudit    = Transition(label="Energy Audit")
dataAnalyze    = Transition(label="Data Analyze")
yieldOptimize  = Transition(label="Yield Optimize")

# Silent transition for loop bodies
skip = SilentTransition()

# Define one growth-monitoring cycle: climate adjust -> growth track -> pest scan -> light modulate
env_cycle = StrictPartialOrder(
    nodes=[climateAdjust, growthTrack, pestScan, lightModulate]
)
env_cycle.order.add_edge(climateAdjust, growthTrack)
env_cycle.order.add_edge(growthTrack, pestScan)
env_cycle.order.add_edge(pestScan, lightModulate)

# Loop over the growth cycle until exit
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[env_cycle, skip]
)

# Define one continuous improvement cycle: data analyze -> yield optimize
cont_cycle = StrictPartialOrder(
    nodes=[dataAnalyze, yieldOptimize]
)
cont_cycle.order.add_edge(dataAnalyze, yieldOptimize)

# Loop over the improvement cycle until exit
cont_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cont_cycle, skip]
)

# Build the root partial order for the end-to-end process
root = StrictPartialOrder(
    nodes=[
        sensorSync, nutrientMix, seedPlant,
        growth_loop,
        marketForecast, harvestPlan,
        packagePrep, vendorNotify,
        wasteSort, energyAudit,
        cont_loop
    ]
)

# Define the sequencing constraints
root.order.add_edge(sensorSync,     nutrientMix)
root.order.add_edge(nutrientMix,    seedPlant)
root.order.add_edge(seedPlant,      growth_loop)
root.order.add_edge(growth_loop,    marketForecast)
root.order.add_edge(marketForecast, harvestPlan)
root.order.add_edge(harvestPlan,    packagePrep)
root.order.add_edge(packagePrep,    vendorNotify)
root.order.add_edge(vendorNotify,   wasteSort)
root.order.add_edge(vendorNotify,   energyAudit)
root.order.add_edge(vendorNotify,   cont_loop)