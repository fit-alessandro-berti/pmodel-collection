# Generated from: 3fbaa29e-7ef5-4694-b0f1-4df73c362f8a.json
# Description: This process outlines a complex, adaptive urban farming cycle designed to optimize crop yield in limited city spaces by integrating real-time environmental data, community feedback, and resource constraints. It involves iterative soil conditioning, microclimate analysis, automated nutrient dosing, and crop rotation scheduling. The process also incorporates waste recycling from urban sources, pest control using biological agents, and continuous monitoring of plant health through IoT sensors. Community engagement through crowdsourced data and educational workshops further refines the system, ensuring sustainability and responsiveness to changing urban conditions. The process concludes with yield assessment and redistribution planning to local markets and food banks, closing the loop on urban food production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SoilTesting = Transition(label='Soil Testing')
MicroclimateScan = Transition(label='Microclimate Scan')
NutrientDosing = Transition(label='Nutrient Dosing')
SeedSelection = Transition(label='Seed Selection')
PlantingSetup = Transition(label='Planting Setup')
WasteRecycling = Transition(label='Waste Recycling')
PestControl = Transition(label='Pest Control')
SensorMonitoring = Transition(label='Sensor Monitoring')
WaterScheduling = Transition(label='Water Scheduling')
GrowthAnalysis = Transition(label='Growth Analysis')
CommunityInput = Transition(label='Community Input')
WorkshopHosting = Transition(label='Workshop Hosting')
CropRotation = Transition(label='Crop Rotation')
YieldAssessment = Transition(label='Yield Assessment')
MarketPlanning = Transition(label='Market Planning')
Redistribution = Transition(label='Redistribution')

# Loop body: iterative soil conditioning, microclimate scan, nutrient dosing
soilLoop = StrictPartialOrder(nodes=[SoilTesting, MicroclimateScan, NutrientDosing])
soilLoop.order.add_edge(SoilTesting, MicroclimateScan)
soilLoop.order.add_edge(MicroclimateScan, NutrientDosing)

# Loop loop (B) node: Waste Recycling, Pest Control, Sensor Monitoring, Water Scheduling, Growth Analysis, Community activities
communityActivities = StrictPartialOrder(nodes=[CommunityInput, WorkshopHosting])
communityActivities.order.add_edge(CommunityInput, WorkshopHosting)

monitoringAndControl = StrictPartialOrder(nodes=[WasteRecycling, PestControl, SensorMonitoring, WaterScheduling, GrowthAnalysis])
monitoringAndControl.order.add_edge(WasteRecycling, PestControl)
monitoringAndControl.order.add_edge(PestControl, SensorMonitoring)
monitoringAndControl.order.add_edge(SensorMonitoring, WaterScheduling)
monitoringAndControl.order.add_edge(WaterScheduling, GrowthAnalysis)

# Combine monitoring and community in partial order (concurrent)
monitoringCommunity = StrictPartialOrder(
    nodes=[monitoringAndControl, communityActivities]
)
# No order edges added, so concurrent

# Loop: after soilLoop (A), either exit or do monitoringCommunity (B) then repeat soilLoop (A)
loop = OperatorPOWL(operator=Operator.LOOP, children=[soilLoop, monitoringCommunity])

# Planting setup branch after loop: seed selection -> planting setup
planting = StrictPartialOrder(nodes=[SeedSelection, PlantingSetup])
planting.order.add_edge(SeedSelection, PlantingSetup)

# Crop Rotation can be concurrent with planting setup (crop rotation scheduling)
plantingAndRotation = StrictPartialOrder(nodes=[planting, CropRotation])
# No edges between planting and CropRotation, so concurrent

# Final phase: Yield Assessment -> (Market Planning XOR Redistribution)
marketXor = OperatorPOWL(operator=Operator.XOR, children=[MarketPlanning, Redistribution])
finalPhase = StrictPartialOrder(nodes=[YieldAssessment, marketXor])
finalPhase.order.add_edge(YieldAssessment, marketXor)

# Assemble full process partial order:
root = StrictPartialOrder(
    nodes=[loop, plantingAndRotation, finalPhase]
)
# Add edges to ensure order:
# loop -> plantingAndRotation
root.order.add_edge(loop, plantingAndRotation)
# plantingAndRotation -> finalPhase
root.order.add_edge(plantingAndRotation, finalPhase)