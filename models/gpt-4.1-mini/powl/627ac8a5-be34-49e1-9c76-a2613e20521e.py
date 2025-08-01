# Generated from: 627ac8a5-be34-49e1-9c76-a2613e20521e.json
# Description: This process outlines the complex cycle of managing an urban vertical farm, integrating advanced hydroponics, AI-driven environmental control, and community engagement. It begins with seed sourcing and germination, followed by automated nutrient mixing and lighting adjustments. Continuous monitoring through sensors feeds data into an AI system that optimizes growth conditions dynamically. Periodic pest control using eco-friendly methods ensures plant health without chemicals. Harvesting is coordinated with packaging customized for urban delivery logistics. Additionally, the process includes waste recycling via composting and water reuse mechanisms. Community workshops and data sharing foster urban agricultural literacy and participation, closing the loop between production and consumption in a sustainable, tech-enabled ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SeedSourcing = Transition(label='Seed Sourcing')
GerminationStart = Transition(label='Germination Start')
NutrientMix = Transition(label='Nutrient Mix')
LightAdjust = Transition(label='Light Adjust')
SensorCheck = Transition(label='Sensor Check')
AIOptimization = Transition(label='AI Optimization')
PestControl = Transition(label='Pest Control')
GrowthScan = Transition(label='Growth Scan')
HarvestPlan = Transition(label='Harvest Plan')
CropPicking = Transition(label='Crop Picking')
PackAssemble = Transition(label='Pack Assemble')
DeliverySync = Transition(label='Delivery Sync')
WasteSort = Transition(label='Waste Sort')
WaterReuse = Transition(label='Water Reuse')
WorkshopHost = Transition(label='Workshop Host')
DataShare = Transition(label='Data Share')

# Hydroponics prep and initial growth phase partial order
prep_and_growth = StrictPartialOrder(nodes=[SeedSourcing, GerminationStart, NutrientMix, LightAdjust])
prep_and_growth.order.add_edge(SeedSourcing, GerminationStart)
prep_and_growth.order.add_edge(GerminationStart, NutrientMix)
prep_and_growth.order.add_edge(NutrientMix, LightAdjust)

# Monitoring cycle loop (SensorCheck -> AIOptimization -> GrowthScan)
monitor_cycle_body = StrictPartialOrder(nodes=[SensorCheck, AIOptimization])
monitor_cycle_body.order.add_edge(SensorCheck, AIOptimization)
monitor_cycle = OperatorPOWL(operator=Operator.LOOP, children=[SensorCheck, AIOptimization])

# Pest control can occur periodically, concurrent with monitoring and growth scan
# PestControl depends on GrowthScan, which follows AIOptimization (so place GrowthScan after AIOptimization)
growth_and_pest = StrictPartialOrder(nodes=[monitor_cycle, GrowthScan, PestControl])
growth_and_pest.order.add_edge(monitor_cycle, GrowthScan)
growth_and_pest.order.add_edge(GrowthScan, PestControl)

# Harvest and packaging partial order
harvest_packaging = StrictPartialOrder(nodes=[HarvestPlan, CropPicking, PackAssemble, DeliverySync])
harvest_packaging.order.add_edge(HarvestPlan, CropPicking)
harvest_packaging.order.add_edge(CropPicking, PackAssemble)
harvest_packaging.order.add_edge(PackAssemble, DeliverySync)

# Waste management partial order (WasteSort -> WaterReuse)
waste_mgmt = StrictPartialOrder(nodes=[WasteSort, WaterReuse])
waste_mgmt.order.add_edge(WasteSort, WaterReuse)

# Community activities partial order (WorkshopHost -> DataShare)
community = StrictPartialOrder(nodes=[WorkshopHost, DataShare])
community.order.add_edge(WorkshopHost, DataShare)

# Now build the root with all parts:
# 1) prep_and_growth leads to growth_and_pest
# 2) growth_and_pest leads to harvest_packaging
# 3) waste_mgmt and community run concurrently with harvest_packaging (and after growth_and_pest)
# So order is:
# prep_and_growth --> growth_and_pest --> harvest_packaging
# harvest_packaging --> (waste_mgmt and community) concurrent

root = StrictPartialOrder(
    nodes=[prep_and_growth, growth_and_pest, harvest_packaging, waste_mgmt, community]
)

root.order.add_edge(prep_and_growth, growth_and_pest)
root.order.add_edge(growth_and_pest, harvest_packaging)
root.order.add_edge(harvest_packaging, waste_mgmt)
root.order.add_edge(harvest_packaging, community)