# Generated from: 45dbb670-ca49-4ca7-a2df-7713534cc64d.json
# Description: This process outlines the comprehensive lifecycle management of an urban vertical farm that integrates advanced hydroponics, AI-driven climate control, and automated harvesting systems. Starting from seed selection based on market demand forecasts, the process includes nutrient mix optimization, multi-layered crop monitoring via IoT sensors, pest anomaly detection through machine learning, and dynamic light spectrum adjustments. It further encompasses automated pruning, yield prediction analytics, and adaptive packaging aligned with sustainability standards. The process concludes with real-time distribution logistics coordination and post-harvest nutrient recycling, ensuring minimal waste and maximized resource efficiency in dense city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SeedSelect = Transition(label='Seed Select')
DemandForecast = Transition(label='Demand Forecast')
NutrientMix = Transition(label='Nutrient Mix')
ClimateAdjust = Transition(label='Climate Adjust')
SensorMonitor = Transition(label='Sensor Monitor')
PestDetect = Transition(label='Pest Detect')
LightControl = Transition(label='Light Control')
PrunePlants = Transition(label='Prune Plants')
YieldPredict = Transition(label='Yield Predict')
HarvestAuto = Transition(label='Harvest Auto')
PackageAlign = Transition(label='Package Align')
WasteRecycle = Transition(label='Waste Recycle')
LogisticsPlan = Transition(label='Logistics Plan')
QualityAudit = Transition(label='Quality Audit')
DataSync = Transition(label='Data Sync')

# Create partial orders based on described sequences

# Seed selection follows demand forecast
po_seed = StrictPartialOrder(nodes=[SeedSelect, DemandForecast])
po_seed.order.add_edge(DemandForecast, SeedSelect)

# Nutrient mix optimization happens after seed select
po_nutrient = StrictPartialOrder(nodes=[NutrientMix])
# Later connected

# Multi-layered crop monitoring (SensorMonitor), PestDetect, LightControl run concurrently after NutrientMix
monitoring = StrictPartialOrder(nodes=[SensorMonitor, PestDetect, LightControl])
# no order edges = concurrent

# ClimateAdjust executed after PestDetect and SensorMonitor and before PrunePlants
# But description ties climate adjust to AI-driven climate control - presumably after NutrientMix, can be concurrent with monitor activities or follow them
# We'll add ClimateAdjust after NutrientMix, concurrent with monitoring activities

# PrunePlants after monitoring and climate adjust
po_after_monitor = StrictPartialOrder(nodes=[ClimateAdjust, PrunePlants])
# ClimateAdjust and PrunePlants order: ClimateAdjust --> PrunePlants

po_monitor_climate = StrictPartialOrder(
    nodes=[SensorMonitor, PestDetect, LightControl, ClimateAdjust])
# monitoring concurrent plus climate adjust after NutrientMix, pruning after climate adjust

# We'll synchronize Monitoring and ClimateAdjust as concurrent except ClimateAdjust before PrunePlants:
# So we connect NutrientMix to SensorMonitor, PestDetect, LightControl, ClimateAdjust (all concurrent),
# and then order ClimateAdjust --> PrunePlants

# YieldPredict after PrunePlants
# HarvestAuto after YieldPredict
# PackageAlign after HarvestAuto

# LogisticsPlan and WasteRecycle climax the process after PackageAlign
# QualityAudit and DataSync run concurrently near the end, after LogisticsPlan, WasteRecycle

# Compose partial orders along this flow

# Basic linear orders from above
po_linear1 = StrictPartialOrder(
    nodes=[NutrientMix, SensorMonitor, PestDetect, LightControl, ClimateAdjust])
po_linear1.order.add_edge(NutrientMix, SensorMonitor)
po_linear1.order.add_edge(NutrientMix, PestDetect)
po_linear1.order.add_edge(NutrientMix, LightControl)
po_linear1.order.add_edge(NutrientMix, ClimateAdjust)

# PrunePlants after ClimateAdjust
po_prune = StrictPartialOrder(nodes=[ClimateAdjust, PrunePlants])
po_prune.order.add_edge(ClimateAdjust, PrunePlants)

# YieldPredict after PrunePlants
po_yield = StrictPartialOrder(nodes=[PrunePlants, YieldPredict])
po_yield.order.add_edge(PrunePlants, YieldPredict)

# HarvestAuto after YieldPredict
po_harvest = StrictPartialOrder(nodes=[YieldPredict, HarvestAuto])
po_harvest.order.add_edge(YieldPredict, HarvestAuto)

# PackageAlign after HarvestAuto
po_package = StrictPartialOrder(nodes=[HarvestAuto, PackageAlign])
po_package.order.add_edge(HarvestAuto, PackageAlign)

# LogisticsPlan and WasteRecycle after PackageAlign (concurrent)
po_logistics_waste = StrictPartialOrder(nodes=[PackageAlign, LogisticsPlan, WasteRecycle])
po_logistics_waste.order.add_edge(PackageAlign, LogisticsPlan)
po_logistics_waste.order.add_edge(PackageAlign, WasteRecycle)

# QualityAudit and DataSync run concurrently after LogisticsPlan and WasteRecycle
po_quality_data = StrictPartialOrder(nodes=[LogisticsPlan, WasteRecycle, QualityAudit, DataSync])
po_quality_data.order.add_edge(LogisticsPlan, QualityAudit)
po_quality_data.order.add_edge(WasteRecycle, QualityAudit)
po_quality_data.order.add_edge(LogisticsPlan, DataSync)
po_quality_data.order.add_edge(WasteRecycle, DataSync)

# Now combine all partial orders according to flow:

# Step1: DemandForecast --> SeedSelect
# Step2: SeedSelect --> NutrientMix
# Step3: NutrientMix --> monitoring + climateAdjust
# Step4: ClimateAdjust --> PrunePlants
# Step5: PrunePlants --> YieldPredict --> HarvestAuto --> PackageAlign
# Step6: PackageAlign --> LogisticsPlan and WasteRecycle (concurrent)
# Step7: LogisticsPlan and WasteRecycle --> QualityAudit and DataSync (concurrent)

# To combine them, start from po_seed with DemandForecast->SeedSelect
root = StrictPartialOrder(
    nodes=[DemandForecast, SeedSelect, NutrientMix, SensorMonitor, PestDetect, LightControl,
           ClimateAdjust, PrunePlants, YieldPredict, HarvestAuto, PackageAlign,
           LogisticsPlan, WasteRecycle, QualityAudit, DataSync])

# Add edges from po_seed
root.order.add_edge(DemandForecast, SeedSelect)
# SeedSelect --> NutrientMix
root.order.add_edge(SeedSelect, NutrientMix)
# NutrientMix --> monitoring and climate adjust
root.order.add_edge(NutrientMix, SensorMonitor)
root.order.add_edge(NutrientMix, PestDetect)
root.order.add_edge(NutrientMix, LightControl)
root.order.add_edge(NutrientMix, ClimateAdjust)
# ClimateAdjust --> PrunePlants
root.order.add_edge(ClimateAdjust, PrunePlants)
# PrunePlants --> YieldPredict
root.order.add_edge(PrunePlants, YieldPredict)
# YieldPredict --> HarvestAuto
root.order.add_edge(YieldPredict, HarvestAuto)
# HarvestAuto --> PackageAlign
root.order.add_edge(HarvestAuto, PackageAlign)
# PackageAlign --> LogisticsPlan and WasteRecycle
root.order.add_edge(PackageAlign, LogisticsPlan)
root.order.add_edge(PackageAlign, WasteRecycle)
# LogisticsPlan and WasteRecycle --> QualityAudit and DataSync
root.order.add_edge(LogisticsPlan, QualityAudit)
root.order.add_edge(WasteRecycle, QualityAudit)
root.order.add_edge(LogisticsPlan, DataSync)
root.order.add_edge(WasteRecycle, DataSync)

# No other edges means SensorMonitor, PestDetect, LightControl concurrent with each other and with ClimateAdjust (except orders from NutrientMix).

# Final POWL model stored in variable root