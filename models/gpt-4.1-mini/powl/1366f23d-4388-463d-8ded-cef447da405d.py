# Generated from: 1366f23d-4388-463d-8ded-cef447da405d.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm within a city environment. It involves site evaluation, modular system design, nutrient solution formulation, and integration of IoT sensors for real-time monitoring. The process further includes seed selection optimized for vertical growth, automated planting, climate control calibration, and pest management using bio-controls. Post-harvest handling features automated sorting and quality inspection, coupled with data analytics to improve yield cycles. Finally, the system incorporates waste recycling and energy optimization to ensure sustainability and scalability within limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
SiteSurvey = Transition(label='Site Survey')
SystemDesign = Transition(label='System Design')
SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
IoTSetup = Transition(label='IoT Setup')
PlantingAutomation = Transition(label='Planting Automation')
ClimateAdjust = Transition(label='Climate Adjust')
PestControl = Transition(label='Pest Control')
WaterRecycling = Transition(label='Water Recycling')
HarvestSort = Transition(label='Harvest Sort')
QualityInspect = Transition(label='Quality Inspect')
DataAnalysis = Transition(label='Data Analysis')
WasteManage = Transition(label='Waste Manage')
EnergyMonitor = Transition(label='Energy Monitor')
YieldReport = Transition(label='Yield Report')

# Site evaluation and design partial order
site_eval_design = StrictPartialOrder(nodes=[SiteSurvey, SystemDesign])
site_eval_design.order.add_edge(SiteSurvey, SystemDesign)

# Nutrient mix and IoT setup partial order
nutrient_iot = StrictPartialOrder(nodes=[NutrientMix, IoTSetup])
nutrient_iot.order.add_edge(NutrientMix, IoTSetup)

# Seed selection and planting automation partial order
seeding_planting = StrictPartialOrder(nodes=[SeedSelection, PlantingAutomation])
seeding_planting.order.add_edge(SeedSelection, PlantingAutomation)

# Climate adjust and pest control partial order
climate_pest = StrictPartialOrder(nodes=[ClimateAdjust, PestControl])
climate_pest.order.add_edge(ClimateAdjust, PestControl)

# Post harvest partial order: Harvest Sort -> Quality Inspect -> Data Analysis
post_harvest = StrictPartialOrder(nodes=[HarvestSort, QualityInspect, DataAnalysis])
post_harvest.order.add_edge(HarvestSort, QualityInspect)
post_harvest.order.add_edge(QualityInspect, DataAnalysis)

# Sustainability partial order: Water Recycling -> Waste Manage -> Energy Monitor -> Yield Report
sustainability = StrictPartialOrder(nodes=[WaterRecycling, WasteManage, EnergyMonitor, YieldReport])
sustainability.order.add_edge(WaterRecycling, WasteManage)
sustainability.order.add_edge(WasteManage, EnergyMonitor)
sustainability.order.add_edge(EnergyMonitor, YieldReport)

# Combine the core assemblies with partial concurrency
# First group: site_eval_design -> nutrient_iot
group1 = StrictPartialOrder(nodes=[site_eval_design, nutrient_iot])
group1.order.add_edge(site_eval_design, nutrient_iot)

# Second group: seeding_planting
# Third group: climate_pest

# These three groups (nutrient_iot, seeding_planting, climate_pest) can run concurrently
group2 = StrictPartialOrder(nodes=[nutrient_iot, seeding_planting, climate_pest])

# Combine first and second group partially ordered and third group concurrent with them after nutrient_iot
# Because nutrient_iot feeds seeding_planting and climate_pest logically can start concurrently after nutrient_iot

# Actually nutrient_iot is after site_eval_design, seeding_planting after nutrient_iot
group3 = StrictPartialOrder(nodes=[group1, seeding_planting, climate_pest])
group3.order.add_edge(group1, seeding_planting)
group3.order.add_edge(group1, climate_pest)

# Post harvest starts after Planting Automation, Climate Adjust, and Pest Control finish
postharvest_start = StrictPartialOrder(nodes=[seeding_planting, climate_pest, post_harvest])
postharvest_start.order.add_edge(seeding_planting, post_harvest)
postharvest_start.order.add_edge(climate_pest, post_harvest)

# Sustainability starts after Data Analysis finishes
sustain_starts = StrictPartialOrder(nodes=[post_harvest, sustainability])
sustain_starts.order.add_edge(post_harvest, sustainability)

# Finally, Site Survey + System Design -> Nutrient Mix + IoT Setup -> Seed Selection -> Planting + Climate/Pest ->
# Post Harvest -> Sustainability

root = StrictPartialOrder(
    nodes=[SiteSurvey, SystemDesign, NutrientMix, IoTSetup, SeedSelection, PlantingAutomation, ClimateAdjust, PestControl,
           HarvestSort, QualityInspect, DataAnalysis, WaterRecycling, WasteManage, EnergyMonitor, YieldReport]
)

# Add edges to define ordering per above reasoning:

# Site evaluation and design
root.order.add_edge(SiteSurvey, SystemDesign)
# System Design -> Nutrient Mix
root.order.add_edge(SystemDesign, NutrientMix)
# Nutrient Mix -> IoT Setup
root.order.add_edge(NutrientMix, IoTSetup)
# IoT Setup -> Seed Selection
root.order.add_edge(IoTSetup, SeedSelection)
# Seed Selection -> Planting Automation
root.order.add_edge(SeedSelection, PlantingAutomation)
# Planting Automation -> Climate Adjust
root.order.add_edge(PlantingAutomation, ClimateAdjust)
# Climate Adjust -> Pest Control
root.order.add_edge(ClimateAdjust, PestControl)
# Pest Control -> Harvest Sort
root.order.add_edge(PestControl, HarvestSort)
# Harvest Sort -> Quality Inspect
root.order.add_edge(HarvestSort, QualityInspect)
# Quality Inspect -> Data Analysis
root.order.add_edge(QualityInspect, DataAnalysis)
# Data Analysis -> Water Recycling
root.order.add_edge(DataAnalysis, WaterRecycling)
# Water Recycling -> Waste Manage
root.order.add_edge(WaterRecycling, WasteManage)
# Waste Manage -> Energy Monitor
root.order.add_edge(WasteManage, EnergyMonitor)
# Energy Monitor -> Yield Report
root.order.add_edge(EnergyMonitor, YieldReport)