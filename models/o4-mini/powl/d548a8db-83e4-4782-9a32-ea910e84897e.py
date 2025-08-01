# Generated from: d548a8db-83e4-4782-9a32-ea910e84897e.json
# Description: This process outlines the operational cycle of an urban vertical farm integrating automated hydroponics, AI-driven crop monitoring, and community-supported distribution. Beginning with seed selection and nutrient calibration, the farm conducts continuous environmental adjustments to optimize growth. Automated harvesting robots coordinate with quality control sensors to ensure produce meets strict urban agricultural standards. Waste recycling and energy reuse loops minimize environmental impact. Finally, a dynamic delivery system synchronizes with local demand patterns to distribute fresh crops efficiently while engaging community members through participatory farming events and educational workshops.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities as POWL Transitions
SeedSelection   = Transition(label='Seed Selection')
NutrientSetup   = Transition(label='Nutrient Setup')
GrowthMonitoring = Transition(label='Growth Monitoring')
ClimateAdjust   = Transition(label='Climate Adjust')
PestControl     = Transition(label='Pest Control')
WaterRecirculate = Transition(label='Water Recirculate')
LightCalibration = Transition(label='Light Calibration')
RoboticHarvest  = Transition(label='Robotic Harvest')
QualityInspect  = Transition(label='Quality Inspect')
WasteProcess    = Transition(label='Waste Process')
EnergyReuse     = Transition(label='Energy Reuse')
InventoryUpdate = Transition(label='Inventory Update')
DemandForecast  = Transition(label='Demand Forecast')
OrderDispatch   = Transition(label='Order Dispatch')
CommunityEvent  = Transition(label='Community Event')
FeedbackCollect = Transition(label='Feedback Collect')
DataAnalyze     = Transition(label='Data Analyze')

# Silent transition for loops
skip = SilentTransition()

# 1) Growth cycle loop: repeat GrowthMonitoring then parallel environmental adjustments
envAdjust = StrictPartialOrder(
    nodes=[ClimateAdjust, PestControl, WaterRecirculate, LightCalibration]
)
growthLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[GrowthMonitoring, envAdjust]
)

# 2) Waste and energy loops (concurrent loops after quality inspect)
wasteLoop = OperatorPOWL(operator=Operator.LOOP, children=[WasteProcess, skip])
energyLoop = OperatorPOWL(operator=Operator.LOOP, children=[EnergyReuse, skip])

# Build the overall process as a single partial order
root = StrictPartialOrder(nodes=[
    # Initial setup
    SeedSelection, NutrientSetup,
    # Growth loop
    growthLoop,
    # Harvest & QC
    RoboticHarvest, QualityInspect,
    # Environmental-impact loops
    wasteLoop, energyLoop,
    # Distribution branch
    InventoryUpdate, DemandForecast, OrderDispatch,
    # Community engagement branch
    CommunityEvent, FeedbackCollect, DataAnalyze
])

# Define the control-flow (partial order) edges
# Initial sequence: SeedSelection -> NutrientSetup -> growthLoop
root.order.add_edge(SeedSelection, NutrientSetup)
root.order.add_edge(NutrientSetup, growthLoop)

# After growth cycle, harvest & inspect
root.order.add_edge(growthLoop, RoboticHarvest)
root.order.add_edge(RoboticHarvest, QualityInspect)

# After QA, start the waste & energy loops in parallel
root.order.add_edge(QualityInspect, wasteLoop)
root.order.add_edge(QualityInspect, energyLoop)

# After both loops, start distribution and community branches
# We add edges from both loops to the start of each branch
root.order.add_edge(wasteLoop, InventoryUpdate)
root.order.add_edge(energyLoop, InventoryUpdate)

root.order.add_edge(wasteLoop, CommunityEvent)
root.order.add_edge(energyLoop, CommunityEvent)

# Distribution sequence
root.order.add_edge(InventoryUpdate, DemandForecast)
root.order.add_edge(DemandForecast, OrderDispatch)

# Community engagement sequence
root.order.add_edge(CommunityEvent, FeedbackCollect)
root.order.add_edge(FeedbackCollect, DataAnalyze)