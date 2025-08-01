# Generated from: 0895820d-b056-4543-83f1-ec07f529ee52.json
# Description: This process outlines the end-to-end operational workflow for managing an urban vertical farm that integrates IoT sensors, automated hydroponic systems, and AI-driven crop optimization. Starting from environmental monitoring, nutrient mixing, and seed planting, the workflow continues through growth tracking, pest detection, and adaptive lighting adjustments. Harvest scheduling is dynamically optimized based on market demand forecasts, followed by automated packaging and distribution coordination with local vendors. The process also includes waste recycling, energy consumption analysis, and continuous improvement cycles driven by data insights to maximize yield and minimize resource use in constrained urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SensorSync = Transition(label='Sensor Sync')
NutrientMix = Transition(label='Nutrient Mix')
SeedPlant = Transition(label='Seed Plant')

ClimateAdjust = Transition(label='Climate Adjust')
GrowthTrack = Transition(label='Growth Track')
PestScan = Transition(label='Pest Scan')
LightModulate = Transition(label='Light Modulate')

HarvestPlan = Transition(label='Harvest Plan')
MarketForecast = Transition(label='Market Forecast')

PackagePrep = Transition(label='Package Prep')
VendorNotify = Transition(label='Vendor Notify')

WasteSort = Transition(label='Waste Sort')
EnergyAudit = Transition(label='Energy Audit')

DataAnalyze = Transition(label='Data Analyze')
YieldOptimize = Transition(label='Yield Optimize')

# Initial parallel: Sensor Sync, Nutrient Mix, Seed Plant concurrent (partial order no edges)
initial = StrictPartialOrder(nodes=[SensorSync, NutrientMix, SeedPlant])

# Monitor phase partial order: ClimateAdjust -> GrowthTrack -> PestScan -> LightModulate
monitor = StrictPartialOrder(nodes=[ClimateAdjust, GrowthTrack, PestScan, LightModulate])
monitor.order.add_edge(ClimateAdjust, GrowthTrack)
monitor.order.add_edge(GrowthTrack, PestScan)
monitor.order.add_edge(PestScan, LightModulate)

# Harvest planning loop:
# Loop over (MarketForecast then HarvestPlan), conditionally repeat or exit
harvest_loop_body = StrictPartialOrder(nodes=[MarketForecast, HarvestPlan])
harvest_loop_body.order.add_edge(MarketForecast, HarvestPlan)
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_loop_body, SilentTransition()])

# Packaging and vendor notify in parallel (concurrent)
packaging_vendor = StrictPartialOrder(nodes=[PackagePrep, VendorNotify])

# Waste and energy analysis partial order, WasteSort -> EnergyAudit
waste_energy = StrictPartialOrder(nodes=[WasteSort, EnergyAudit])
waste_energy.order.add_edge(WasteSort, EnergyAudit)

# Continuous improvement loop: DataAnalyze then YieldOptimize, looped
improvement_body = StrictPartialOrder(nodes=[DataAnalyze, YieldOptimize])
improvement_body.order.add_edge(DataAnalyze, YieldOptimize)
improvement_loop = OperatorPOWL(operator=Operator.LOOP, children=[improvement_body, SilentTransition()])

# Now assemble full workflow partial order:
# initial -> monitor -> harvest_loop -> packaging_vendor
# and waste_energy and improvement_loop run concurrent with packaging_vendor but after harvest_loop
root = StrictPartialOrder(nodes=[initial, monitor, harvest_loop, packaging_vendor, waste_energy, improvement_loop])

root.order.add_edge(initial, monitor)
root.order.add_edge(monitor, harvest_loop)
root.order.add_edge(harvest_loop, packaging_vendor)
root.order.add_edge(harvest_loop, waste_energy)
root.order.add_edge(harvest_loop, improvement_loop)

# packaging_vendor, waste_energy, improvement_loop are concurrent (no edges among them)
