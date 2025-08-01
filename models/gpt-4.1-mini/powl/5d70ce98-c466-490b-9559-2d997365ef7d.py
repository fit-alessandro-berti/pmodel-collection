# Generated from: 5d70ce98-c466-490b-9559-2d997365ef7d.json
# Description: This process details the comprehensive operational cycle of an urban vertical farm that integrates automated hydroponics, AI-driven climate control, and real-time crop health monitoring. It begins with seed selection based on market demand predictions, followed by nutrient solution preparation and precise planting. Growth phases are continuously optimized through sensor data analytics and robotic pruning. Concurrently, pest detection algorithms trigger targeted biological interventions. Harvesting is automated, with quality sorting and packaging adapting dynamically to supply chain requirements. Waste biomass is processed on-site for energy recovery, closing the sustainability loop. The process concludes with data-driven reporting to improve future yield forecasts and resource efficiency, ensuring a resilient urban agriculture model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
SeedSelect = Transition(label='Seed Select')
DemandForecast = Transition(label='Demand Forecast')
NutrientMix = Transition(label='Nutrient Mix')
PlantSetup = Transition(label='Plant Setup')
ClimateAdjust = Transition(label='Climate Adjust')
SensorMonitor = Transition(label='Sensor Monitor')
GrowthAnalyze = Transition(label='Growth Analyze')
RoboticPrune = Transition(label='Robotic Prune')
PestDetect = Transition(label='Pest Detect')
BioIntervention = Transition(label='Bio Intervention')
AutoHarvest = Transition(label='Auto Harvest')
QualitySort = Transition(label='Quality Sort')
DynamicPack = Transition(label='Dynamic Pack')
WasteProcess = Transition(label='Waste Process')
DataReport = Transition(label='Data Report')
YieldForecast = Transition(label='Yield Forecast')

# Growth phases are continuously optimized through sensor data analytics and robotic pruning:
# model this as a loop: execute SensorMonitor, then choose to exit or do GrowthAnalyze + RoboticPrune then loop again
growth_loop_body = StrictPartialOrder(nodes=[GrowthAnalyze, RoboticPrune])
growth_loop_body.order.add_edge(GrowthAnalyze, RoboticPrune)
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[SensorMonitor, growth_loop_body])

# Pest detection algorithms trigger targeted bio interventions:
# Choice node: when PestDetect happens, it may or may not trigger BioIntervention
pest_choice = OperatorPOWL(operator=Operator.XOR, children=[BioIntervention, SilentTransition()])

# The loop: after PestDetect, do choice (BioIntervention or skip)
pest_handling = StrictPartialOrder(nodes=[PestDetect, pest_choice])
pest_handling.order.add_edge(PestDetect, pest_choice)

# Harvesting includes Auto Harvest, Quality Sort, Dynamic Pack in sequence
harvest_po = StrictPartialOrder(nodes=[AutoHarvest, QualitySort, DynamicPack])
harvest_po.order.add_edge(AutoHarvest, QualitySort)
harvest_po.order.add_edge(QualitySort, DynamicPack)

# Waste biomass Process happens after harvest (to close loop)
# Data reporting and yield forecasting conclude the process
conclusion_po = StrictPartialOrder(nodes=[DataReport, YieldForecast])
conclusion_po.order.add_edge(DataReport, YieldForecast)

# Nutrient Mix and Plant Setup come after DemandForecast and SeedSelect
initial_po = StrictPartialOrder(nodes=[SeedSelect, DemandForecast, NutrientMix, PlantSetup])
# SeedSelect and DemandForecast are concurrent; both precede NutrientMix and PlantSetup in sequence
# We'll assume NutrientMix then PlantSetup for logical order
initial_po.order.add_edge(SeedSelect, NutrientMix)
initial_po.order.add_edge(DemandForecast, NutrientMix)
initial_po.order.add_edge(NutrientMix, PlantSetup)

# ClimateAdjust occurs after PlantSetup and before growth_loop
climate_and_growth = StrictPartialOrder(nodes=[ClimateAdjust, growth_loop])
climate_and_growth.order.add_edge(ClimateAdjust, growth_loop)

# After growth loop and pest handling (which are concurrent), do harvest
post_growth = StrictPartialOrder(nodes=[growth_loop, pest_handling])
# growth_loop and pest_handling concurrent (no order edges)

# Create next phase PO with harvest coming after both growth and pest handling
harvest_phase = StrictPartialOrder(nodes=[post_growth, harvest_po])
harvest_phase.order.add_edge(post_growth, harvest_po)

# Waste process after harvest
waste_phase = StrictPartialOrder(nodes=[harvest_po, WasteProcess])
waste_phase.order.add_edge(harvest_po, WasteProcess)

# Conclusion after waste process
final_phase = StrictPartialOrder(nodes=[WasteProcess, conclusion_po])
final_phase.order.add_edge(WasteProcess, conclusion_po)

# Combine all phases into root
root = StrictPartialOrder(nodes=[initial_po, ClimateAdjust, growth_loop, pest_handling, harvest_po, WasteProcess, conclusion_po])
# Add orders to properly link phases:

# initial_po to ClimateAdjust and growth_loop
root.order.add_edge(initial_po, ClimateAdjust)
root.order.add_edge(ClimateAdjust, growth_loop)

# growth_loop and pest_handling concurrent: no order edge

# growth_loop and pest_handling both predecessors of harvest_po
root.order.add_edge(growth_loop, harvest_po)
root.order.add_edge(pest_handling, harvest_po)

# harvest_po before WasteProcess
root.order.add_edge(harvest_po, WasteProcess)

# WasteProcess before conclusion_po
root.order.add_edge(WasteProcess, conclusion_po)