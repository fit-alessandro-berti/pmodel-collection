# Generated from: 1497f4ec-5028-4ad4-8b4a-840386c83b6d.json
# Description: This process involves establishing a multi-tiered urban vertical farm within a repurposed warehouse. It includes site analysis, structural retrofitting, climate control installation, hydroponic system setup, seed selection, nutrient calibration, automated monitoring deployment, pest management integration, crop scheduling, continuous yield assessment, and community engagement initiatives. The objective is to maximize crop output within limited urban spaces while ensuring sustainability and minimal environmental impact through advanced automation and data-driven cultivation techniques.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
StructureRetrofit = Transition(label='Structure Retrofit')
HVACInstall = Transition(label='HVAC Install')
LightingSetup = Transition(label='Lighting Setup')
HydroponicsInit = Transition(label='Hydroponics Init')
SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
SensorDeploy = Transition(label='Sensor Deploy')
PestControl = Transition(label='Pest Control')
IrrigationPlan = Transition(label='Irrigation Plan')
CropScheduling = Transition(label='Crop Scheduling')
YieldMonitor = Transition(label='Yield Monitor')
DataAnalysis = Transition(label='Data Analysis')
WasteRecycle = Transition(label='Waste Recycle')
CommunityOutreach = Transition(label='Community Outreach')
EnergyAudit = Transition(label='Energy Audit')

# Phase 1: Setting up infrastructure
infra_PO = StrictPartialOrder(nodes=[SiteSurvey, StructureRetrofit, HVACInstall, LightingSetup, HydroponicsInit])
infra_PO.order.add_edge(SiteSurvey, StructureRetrofit)
infra_PO.order.add_edge(StructureRetrofit, HVACInstall)
infra_PO.order.add_edge(StructureRetrofit, LightingSetup)
infra_PO.order.add_edge(HVACInstall, HydroponicsInit)
infra_PO.order.add_edge(LightingSetup, HydroponicsInit)

# Phase 2: Preparations parallel: Seed + Nutrient + Sensor Deploy + Pest + Irrigation
prep_PO = StrictPartialOrder(nodes=[SeedSelection, NutrientMix, SensorDeploy, PestControl, IrrigationPlan])
# All concurrent (no order)

# Phase 3: Crop scheduling and yield monitoring loop
# Loop: execute CropScheduling, then choose to exit or do YieldMonitor + DataAnalysis + WasteRecycle + EnergyAudit then loop again

# Create the body of the loop (B)
body_PO = StrictPartialOrder(nodes=[YieldMonitor, DataAnalysis, WasteRecycle, EnergyAudit])
body_PO.order.add_edge(YieldMonitor, DataAnalysis)
body_PO.order.add_edge(DataAnalysis, WasteRecycle)
body_PO.order.add_edge(WasteRecycle, EnergyAudit)

loop = OperatorPOWL(operator=Operator.LOOP, children=[CropScheduling, body_PO])

# Phase 4: Community outreach after loop completes
root = StrictPartialOrder(nodes=[infra_PO, prep_PO, loop, CommunityOutreach])
# infra_PO precedes prep_PO
root.order.add_edge(infra_PO, prep_PO)
# prep_PO precedes loop
root.order.add_edge(prep_PO, loop)
# loop precedes CommunityOutreach
root.order.add_edge(loop, CommunityOutreach)