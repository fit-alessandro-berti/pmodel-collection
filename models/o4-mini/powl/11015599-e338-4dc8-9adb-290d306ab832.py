# Generated from: 11015599-e338-4dc8-9adb-290d306ab832.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site assessment, environmental impact analysis, modular system design, hydroponic and aeroponic integration, climate control calibration, nutrient cycle optimization, automation system installation, workforce training, regulatory compliance checks, pilot crop testing, data-driven yield forecasting, waste recycling implementation, community engagement strategy, and scaling plans. The goal is to create a sustainable, high-efficiency farming operation that maximizes limited urban space while minimizing environmental footprint and ensuring regulatory adherence.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
SiteSurvey      = Transition(label='Site Survey')
ImpactStudy     = Transition(label='Impact Study')
SystemDesign    = Transition(label='System Design')
HydroponicsSetup= Transition(label='Hydroponics Setup')
AeroponicsSetup = Transition(label='Aeroponics Setup')
ClimateSetup    = Transition(label='Climate Setup')
NutrientMix     = Transition(label='Nutrient Mix')
AutomationInstall= Transition(label='Automation Install')
StaffTraining   = Transition(label='Staff Training')
RegulationCheck = Transition(label='Regulation Check')
PilotCrops      = Transition(label='Pilot Crops')
YieldForecast   = Transition(label='Yield Forecast')
WasteCycle      = Transition(label='Waste Cycle')
CommunityPlan   = Transition(label='Community Plan')
ScaleStrategy   = Transition(label='Scale Strategy')

# Build the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey, ImpactStudy, SystemDesign,
    HydroponicsSetup, AeroponicsSetup,
    ClimateSetup, NutrientMix, AutomationInstall,
    StaffTraining, RegulationCheck,
    PilotCrops, YieldForecast, WasteCycle,
    CommunityPlan, ScaleStrategy
])

# Define ordering (dependencies)
root.order.add_edge(SiteSurvey,      ImpactStudy)
root.order.add_edge(ImpactStudy,     SystemDesign)

root.order.add_edge(SystemDesign,    HydroponicsSetup)
root.order.add_edge(SystemDesign,    AeroponicsSetup)

root.order.add_edge(HydroponicsSetup, ClimateSetup)
root.order.add_edge(AeroponicsSetup,  ClimateSetup)

root.order.add_edge(ClimateSetup,    NutrientMix)
root.order.add_edge(ClimateSetup,    AutomationInstall)
root.order.add_edge(NutrientMix,     AutomationInstall)

root.order.add_edge(AutomationInstall, StaffTraining)
root.order.add_edge(AutomationInstall, RegulationCheck)

root.order.add_edge(StaffTraining,   PilotCrops)
root.order.add_edge(RegulationCheck, PilotCrops)

root.order.add_edge(PilotCrops,      YieldForecast)
root.order.add_edge(PilotCrops,      WasteCycle)
root.order.add_edge(PilotCrops,      CommunityPlan)

root.order.add_edge(YieldForecast,   ScaleStrategy)
root.order.add_edge(WasteCycle,      ScaleStrategy)
root.order.add_edge(CommunityPlan,   ScaleStrategy)