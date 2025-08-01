# Generated from: e210eac0-39ba-4b3c-bf5e-ef253a5bd431.json
# Description: This process outlines the intricate steps involved in establishing a fully operational urban vertical farm within a constrained city environment. It includes site analysis, environmental compliance, modular system design, nutrient cycling optimization, integration of renewable energy sources, automated climate control calibration, and continuous yield monitoring. The process also covers community engagement to ensure local support, waste management strategies to minimize footprint, data analytics for crop optimization, and iterative feedback loops for system improvements. This atypical yet highly sustainable business model requires cross-disciplinary coordination between agriculture, technology, and urban planning sectors, aiming to revolutionize food production in dense metropolitan areas while maintaining ecological balance and economic viability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
SiteSurvey = Transition(label='Site Survey')
RegulationCheck = Transition(label='Regulation Check')
ModularDesign = Transition(label='Modular Design')
MaterialSourcing = Transition(label='Material Sourcing')
EnergyIntegration = Transition(label='Energy Integration')
ClimateSetup = Transition(label='Climate Setup')
NutrientMix = Transition(label='Nutrient Mix')
SystemAssembly = Transition(label='System Assembly')
AutomationConfig = Transition(label='Automation Config')
CropSeeding = Transition(label='Crop Seeding')
GrowthMonitoring = Transition(label='Growth Monitoring')
WasteHandling = Transition(label='Waste Handling')
CommunityMeet = Transition(label='Community Meet')
DataAnalysis = Transition(label='Data Analysis')
FeedbackLoop = Transition(label='Feedback Loop')
YieldForecast = Transition(label='Yield Forecast')

# Loop: FeedbackLoop repeats after DataAnalysis
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[DataAnalysis, FeedbackLoop])

# Partial Order construction:
# Core design & build phase (some concurrency and ordering):
# SiteSurvey -> RegulationCheck
# RegulationCheck -> ModularDesign, MaterialSourcing (concurrent after)
# ModularDesign -> EnergyIntegration
# MaterialSourcing -> SystemAssembly
# EnergyIntegration -> ClimateSetup
# ClimateSetup -> AutomationConfig
# NutrientMix and SystemAssembly parallel before AutomationConfig
# So NutrientMix parallel with SystemAssembly, both before AutomationConfig

# CropSeeding after AutomationConfig
# GrowthMonitoring after CropSeeding
# WasteHandling and CommunityMeet concurrent with GrowthMonitoring (can happen in parallel)
# CommunityMeet before DataAnalysis
# YieldForecast concurrent with GrowthMonitoring and WasteHandling, synchronized before DataAnalysis
# DataAnalysis enters the loop with FeedbackLoop 
# Finally YieldForecast follows the loop (e.g. after feedback)

nodes = [
    SiteSurvey, RegulationCheck,
    ModularDesign, MaterialSourcing, EnergyIntegration,
    ClimateSetup, NutrientMix, SystemAssembly,
    AutomationConfig,
    CropSeeding, GrowthMonitoring, WasteHandling,
    CommunityMeet,
    feedback_loop,
    YieldForecast
]

root = StrictPartialOrder(nodes=nodes)

order = root.order
order.add_edge(SiteSurvey, RegulationCheck)
order.add_edge(RegulationCheck, ModularDesign)
order.add_edge(RegulationCheck, MaterialSourcing)

order.add_edge(ModularDesign, EnergyIntegration)
order.add_edge(EnergyIntegration, ClimateSetup)

# NutrientMix and SystemAssembly must finish before AutomationConfig
order.add_edge(MaterialSourcing, SystemAssembly)
order.add_edge(NutrientMix, AutomationConfig)
order.add_edge(SystemAssembly, AutomationConfig)
order.add_edge(ClimateSetup, AutomationConfig)

order.add_edge(AutomationConfig, CropSeeding)
order.add_edge(CropSeeding, GrowthMonitoring)

# WasteHandling and CommunityMeet concurrent with GrowthMonitoring (so connect from GrowthMonitoring)
order.add_edge(GrowthMonitoring, WasteHandling)
order.add_edge(GrowthMonitoring, CommunityMeet)

order.add_edge(WasteHandling, feedback_loop)
order.add_edge(CommunityMeet, feedback_loop)

# YieldForecast can start after GrowthMonitoring and WasteHandling (to forecast yield)
order.add_edge(GrowthMonitoring, YieldForecast)
order.add_edge(WasteHandling, YieldForecast)

# YieldForecast leads to feedback loop DataAnalysis start is inside the loop node,
# but since feedback_loop contains DataAnalysis first then FeedbackLoop, after loop exits we consider the end after YieldForecast
order.add_edge(YieldForecast, feedback_loop)  # Add edge for synchronization before looping

# DataAnalysis and FeedbackLoop handled inside loop node
# To keep consistency, keep edges from loop node to YieldForecast or vice versa - more correct:
# We assume YieldForecast after loop, so cycle is inside loop node and YieldForecast after

# For clarity, no edge from feedback_loop to YieldForecast, only YieldForecast to feedback_loop completes cycle inside loop

