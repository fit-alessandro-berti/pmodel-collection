# Generated from: b1cc8992-b9b1-4bc2-898c-56a6661d11a4.json
# Description: This process involves establishing an urban vertical farm in a dense metropolitan area, integrating sustainable agriculture with advanced technology. It includes site analysis, modular system design, climate control calibration, nutrient cycling optimization, and IoT sensor deployment. The process ensures efficient use of limited space by stacking growing layers, automating plant care, and minimizing resource consumption. It also incorporates community engagement, compliance with urban regulations, and a phased production rollout to guarantee consistent crop yield and quality throughout varying seasonal conditions in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey = Transition(label='Site Survey')
RegulationCheck = Transition(label='Regulation Check')
SystemDesign = Transition(label='System Design')
ModularBuild = Transition(label='Modular Build')
ClimateSetup = Transition(label='Climate Setup')
SensorInstall = Transition(label='Sensor Install')
NutrientMix = Transition(label='Nutrient Mix')
WaterCycle = Transition(label='Water Cycle')
LightCalibration = Transition(label='Light Calibration')
PlantSelection = Transition(label='Plant Selection')
AutomationSetup = Transition(label='Automation Setup')
DataIntegration = Transition(label='Data Integration')
TrialGrowth = Transition(label='Trial Growth')
QualityTest = Transition(label='Quality Test')
CommunityOutreach = Transition(label='Community Outreach')
YieldAnalysis = Transition(label='Yield Analysis')
MaintenancePlan = Transition(label='Maintenance Plan')

# Define modular build sub-process as partial order due to concurrency:
# NutrientMix, WaterCycle, LightCalibration can happen concurrently after ModularBuild
modularPO = StrictPartialOrder(
    nodes=[ModularBuild, NutrientMix, WaterCycle, LightCalibration]
)
modularPO.order.add_edge(ModularBuild, NutrientMix)
modularPO.order.add_edge(ModularBuild, WaterCycle)
modularPO.order.add_edge(ModularBuild, LightCalibration)

# Climate and sensor setup follow system design in partial order
climate_sensor_PO = StrictPartialOrder(
    nodes=[SystemDesign, ClimateSetup, SensorInstall]
)
climate_sensor_PO.order.add_edge(SystemDesign, ClimateSetup)
climate_sensor_PO.order.add_edge(SystemDesign, SensorInstall)

# Automation setup depends on PlantSelection
auto_PO = StrictPartialOrder(
    nodes=[PlantSelection, AutomationSetup, DataIntegration]
)
auto_PO.order.add_edge(PlantSelection, AutomationSetup)
auto_PO.order.add_edge(PlantSelection, DataIntegration)
auto_PO.order.add_edge(AutomationSetup, DataIntegration)

# Trial growth loop: TrialGrowth and QualityTest loop until satisfactory
trial_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[TrialGrowth, QualityTest]
)

# Phased production rollout partial order:
# TrialGrowth loop before YieldAnalysis then MaintenancePlan
production_PO = StrictPartialOrder(
    nodes=[trial_loop, YieldAnalysis, MaintenancePlan]
)
production_PO.order.add_edge(trial_loop, YieldAnalysis)
production_PO.order.add_edge(YieldAnalysis, MaintenancePlan)

# CommunityEngagement is concurrent with production rollout (YieldAnalysis, MaintenancePlan)
community_outreach_PO = StrictPartialOrder(
    nodes=[CommunityOutreach]
)

# Top-level partial order combining everything
root = StrictPartialOrder(
    nodes=[
        SiteSurvey,
        RegulationCheck,
        SystemDesign,
        modularPO,
        climate_sensor_PO,
        PlantSelection,
        auto_PO,
        production_PO,
        community_outreach_PO,
    ]
)

# Order constraints
root.order.add_edge(SiteSurvey, RegulationCheck)
root.order.add_edge(RegulationCheck, SystemDesign)
root.order.add_edge(SystemDesign, modularPO)
root.order.add_edge(SystemDesign, climate_sensor_PO)
root.order.add_edge(modularPO, PlantSelection)
root.order.add_edge(climate_sensor_PO, PlantSelection)
root.order.add_edge(PlantSelection, auto_PO)
root.order.add_edge(auto_PO, production_PO)
# Community outreach concurrent with production rollout (i.e. no edges)

# That completes the model