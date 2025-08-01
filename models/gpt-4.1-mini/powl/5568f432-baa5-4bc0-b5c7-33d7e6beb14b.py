# Generated from: 5568f432-baa5-4bc0-b5c7-33d7e6beb14b.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming system within a repurposed industrial building. It includes site evaluation, environmental control integration, hydroponic system installation, and multi-tiered crop planning. The process requires coordination between architects, agricultural scientists, IoT specialists, and supply chain managers to ensure optimal crop yield, energy efficiency, and sustainability. Continuous monitoring, pest control, and harvest scheduling are critical activities, alongside waste recycling and community engagement initiatives to promote local food production and reduce carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
StructuralAudit = Transition(label='Structural Audit')
EnviroSetup = Transition(label='Enviro Setup')
HydroInstall = Transition(label='Hydro Install')
LightingConfig = Transition(label='Lighting Config')
SensorDeploy = Transition(label='Sensor Deploy')
CropSelection = Transition(label='Crop Selection')
SeedPlanting = Transition(label='Seed Planting')
WaterCycling = Transition(label='Water Cycling')
NutrientMix = Transition(label='Nutrient Mix')
PestMonitor = Transition(label='Pest Monitor')
YieldTracking = Transition(label='Yield Tracking')
WasteRecycle = Transition(label='Waste Recycle')
MarketLaunch = Transition(label='Market Launch')
CommunityMeet = Transition(label='Community Meet')
EnergyAudit = Transition(label='Energy Audit')
DataAnalysis = Transition(label='Data Analysis')

# Planning partial order: Crop planning activities are concurrent but follow initial installations
planning_nodes = [CropSelection, SeedPlanting, WaterCycling, NutrientMix]

planning = StrictPartialOrder(nodes=planning_nodes)
# CropSelection -> SeedPlanting (must select crops before planting seeds)
planning.order.add_edge(CropSelection, SeedPlanting)

# Installation partial order: Site survey -> design and audits -> Enviro + Hydro + Lighting + Sensors (some parallel)
installation_nodes = [
    SiteSurvey, DesignLayout, StructuralAudit,
    EnviroSetup, HydroInstall, LightingConfig, SensorDeploy
]
installation = StrictPartialOrder(nodes=installation_nodes)
installation.order.add_edge(SiteSurvey, DesignLayout)
installation.order.add_edge(SiteSurvey, StructuralAudit)
installation.order.add_edge(DesignLayout, EnviroSetup)
installation.order.add_edge(DesignLayout, HydroInstall)
installation.order.add_edge(StructuralAudit, EnviroSetup)
installation.order.add_edge(StructuralAudit, HydroInstall)
installation.order.add_edge(EnviroSetup, LightingConfig)
installation.order.add_edge(HydroInstall, LightingConfig)
installation.order.add_edge(LightingConfig, SensorDeploy)

# Monitoring loop: continuous PestMonitor and YieldTracking, with periodic DataAnalysis and EnergyAudit
# Loop: execute Monitoring base (PestMonitor + YieldTracking concurrent),
# then either exit or do (DataAnalysis -> EnergyAudit) then repeat monitoring
monitoring_base = StrictPartialOrder(nodes=[PestMonitor, YieldTracking])  # concurrent

monitoring_analysis = StrictPartialOrder(nodes=[DataAnalysis, EnergyAudit])
monitoring_analysis.order.add_edge(DataAnalysis, EnergyAudit)

monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitoring_base, monitoring_analysis]
)

# Final phases: WasteRecycle, MarketLaunch, CommunityMeet concurrent after monitoring_loop
final_nodes = [WasteRecycle, MarketLaunch, CommunityMeet]
final_phase = StrictPartialOrder(nodes=final_nodes)

# Build overall process partial order:
# installation -> planning -> monitoring_loop -> final_phase

root = StrictPartialOrder(
    nodes=[installation, planning, monitoring_loop, final_phase]
)

root.order.add_edge(installation, planning)
root.order.add_edge(planning, monitoring_loop)
root.order.add_edge(monitoring_loop, final_phase)