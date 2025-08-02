# Generated from: 7625c203-e639-411c-913f-b538f72bc756.json
# Description: This process involves the comprehensive management of an urban vertical farm, integrating hydroponic cultivation, environmental controls, resource recycling, and community engagement. The cycle begins with seed selection and preparation, followed by nutrient solution formulation and automated planting. Continuous monitoring adjusts lighting and humidity to optimize growth. Harvesting is coordinated with quality assessment and packaging. Waste biomass is processed into compost or bioenergy, closing the sustainability loop. Concurrently, data analytics drive yield optimization while educational workshops engage local communities. The process concludes with distribution logistics tailored for urban markets and feedback integration for continuous improvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
SeedPrep = Transition(label='Seed Prep')
NutrientMix = Transition(label='Nutrient Mix')
AutomatedPlant = Transition(label='Automated Plant')
EnvMonitor = Transition(label='Env Monitor')
LightAdjust = Transition(label='Light Adjust')
HumidityControl = Transition(label='Humidity Control')
GrowthCheck = Transition(label='Growth Check')
HarvestPlan = Transition(label='Harvest Plan')
QualityTest = Transition(label='Quality Test')
WasteProcess = Transition(label='Waste Process')
CompostCreate = Transition(label='Compost Create')
DataAnalyze = Transition(label='Data Analyze')
WorkshopHost = Transition(label='Workshop Host')
MarketPack = Transition(label='Market Pack')
DistributeGoods = Transition(label='Distribute Goods')

# Build the main workflow according to the description

# 1. Seed selection and preparation, then nutrient mix, then automated planting
prep_PO = StrictPartialOrder(nodes=[SeedPrep, NutrientMix, AutomatedPlant])
prep_PO.order.add_edge(SeedPrep, NutrientMix)
prep_PO.order.add_edge(NutrientMix, AutomatedPlant)

# 2. Continuous monitoring adjusts lighting and humidity to optimize growth
# EnvMonitor leads to concurrent LightAdjust and HumidityControl (both concurrent)
monitor_PO = StrictPartialOrder(nodes=[EnvMonitor, LightAdjust, HumidityControl])
monitor_PO.order.add_edge(EnvMonitor, LightAdjust)
monitor_PO.order.add_edge(EnvMonitor, HumidityControl)

# 3. Growth check after environmental adjustments
growth_PO = StrictPartialOrder(nodes=[monitor_PO, GrowthCheck])
growth_PO.order.add_edge(monitor_PO, GrowthCheck)

# 4. Harvesting coordinated with quality test and packaging
harvest_PO = StrictPartialOrder(nodes=[HarvestPlan, QualityTest, MarketPack])
harvest_PO.order.add_edge(HarvestPlan, QualityTest)
harvest_PO.order.add_edge(QualityTest, MarketPack)

# 5. Waste biomass processed into compost or bioenergy (represented by CompostCreate)
# We map WasteProcess leading to CompostCreate (bioenergy path abstracted by CompostCreate)
waste_PO = StrictPartialOrder(nodes=[WasteProcess, CompostCreate])
waste_PO.order.add_edge(WasteProcess, CompostCreate)

# 6. Concurrently, data analytics and educational workshops (concurrent)
concurrent_PO = StrictPartialOrder(nodes=[DataAnalyze, WorkshopHost])
# no order edges: fully concurrent

# 7. Final distribution and feedback integration (consider MarketPack leads to DistributeGoods)
final_PO = StrictPartialOrder(nodes=[MarketPack, DistributeGoods])
final_PO.order.add_edge(MarketPack, DistributeGoods)

# Assemble partial orders in sequence and concurrency

# Combine monitoring and growth check into one PO
monitor_growth_PO = growth_PO  # already combined above

# Combine harvest and waste processing concurrently
harvest_waste_PO = StrictPartialOrder(nodes=[harvest_PO, waste_PO])
# concurrent: no order edges between harvest_PO and waste_PO

# Combine harvest_waste_PO and concurrent analytics/workshops concurrently
post_growth_PO = StrictPartialOrder(nodes=[harvest_waste_PO, concurrent_PO])
# concurrent: no order edges between harvest_waste_PO and concurrent_PO

# Combine post_growth_PO with final distribution sequentially: packaging -> distribute
post_growth_final_PO = StrictPartialOrder(nodes=[post_growth_PO, final_PO])
post_growth_final_PO.order.add_edge(post_growth_PO, final_PO)

# Full process sequence:
# prep_PO --> monitor_growth_PO --> post_growth_final_PO

full_PO = StrictPartialOrder(nodes=[prep_PO, monitor_growth_PO, post_growth_final_PO])
full_PO.order.add_edge(prep_PO, monitor_growth_PO)
full_PO.order.add_edge(monitor_growth_PO, post_growth_final_PO)

root = full_PO