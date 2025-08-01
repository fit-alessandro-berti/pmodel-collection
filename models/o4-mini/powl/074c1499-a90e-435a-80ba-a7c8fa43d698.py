# Generated from: 074c1499-a90e-435a-80ba-a7c8fa43d698.json
# Description: This process outlines the establishment of a vertical farming operation within an urban environment, integrating advanced hydroponic systems, AI-driven climate control, and local supply chain logistics. It begins with site analysis and ends with ongoing yield optimization, incorporating activities such as nutrient cycling, pest monitoring without pesticides, and community engagement for sustainable food distribution. The process involves cross-disciplinary collaboration among agronomists, engineers, data scientists, and local authorities to ensure compliance and efficiency. It emphasizes resource recycling, energy management, and adaptive crop planning based on real-time data and market demand forecasts, creating a highly responsive urban agriculture model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
PermitsObtain = Transition(label='Permits Obtain')
SystemInstall = Transition(label='System Install')
SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
PlantingSetup = Transition(label='Planting Setup')
ClimateControl = Transition(label='Climate Control')
PestMonitor = Transition(label='Pest Monitor')
DataIntegration = Transition(label='Data Integration')
GrowthTracking = Transition(label='Growth Tracking')
HarvestPlan = Transition(label='Harvest Plan')
YieldAnalysis = Transition(label='Yield Analysis')
WasteRecycle = Transition(label='Waste Recycle')
MarketLiaison = Transition(label='Market Liaison')
CommunityEngage = Transition(label='Community Engage')

# Initial setup phase: Site Survey -> Design Layout -> Permits Obtain -> System Install
initial = StrictPartialOrder(nodes=[SiteSurvey, DesignLayout, PermitsObtain, SystemInstall])
initial.order.add_edge(SiteSurvey, DesignLayout)
initial.order.add_edge(DesignLayout, PermitsObtain)
initial.order.add_edge(PermitsObtain, SystemInstall)

# Core growing cycle body
body = StrictPartialOrder(nodes=[
    SeedSelection,
    NutrientMix,
    PlantingSetup,
    ClimateControl,
    PestMonitor,
    DataIntegration,
    GrowthTracking,
    HarvestPlan,
    YieldAnalysis,
    WasteRecycle
])
body.order.add_edge(SeedSelection, NutrientMix)
body.order.add_edge(NutrientMix, PlantingSetup)
body.order.add_edge(PlantingSetup, ClimateControl)
body.order.add_edge(PlantingSetup, PestMonitor)
body.order.add_edge(PlantingSetup, DataIntegration)
body.order.add_edge(PlantingSetup, GrowthTracking)
body.order.add_edge(ClimateControl, HarvestPlan)
body.order.add_edge(PestMonitor, HarvestPlan)
body.order.add_edge(DataIntegration, HarvestPlan)
body.order.add_edge(GrowthTracking, HarvestPlan)
body.order.add_edge(HarvestPlan, YieldAnalysis)
body.order.add_edge(YieldAnalysis, WasteRecycle)

# Feedback phase for adaptive planning: Market Liaison -> Community Engage
feedback = StrictPartialOrder(nodes=[MarketLiaison, CommunityEngage])
feedback.order.add_edge(MarketLiaison, CommunityEngage)

# Loop over the core cycle with feedback
loop_proc = OperatorPOWL(operator=Operator.LOOP, children=[body, feedback])

# Root model: initial setup followed by the looping cycle
root = StrictPartialOrder(nodes=[initial, loop_proc])
root.order.add_edge(initial, loop_proc)