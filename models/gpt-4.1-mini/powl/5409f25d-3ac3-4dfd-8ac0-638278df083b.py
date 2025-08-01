# Generated from: 5409f25d-3ac3-4dfd-8ac0-638278df083b.json
# Description: This process outlines the establishment of an urban rooftop farm involving site assessment, environmental analysis, and installation of modular hydroponic systems. Activities include coordination with local authorities, sourcing sustainable materials, implementing water recycling solutions, and integrating IoT sensors for climate control. The process also covers staff training on crop management, pest control without chemicals, and community engagement to promote local food production. Continuous monitoring and data analysis ensure optimal yield and resource efficiency in an atypical but increasingly vital urban agricultural practice.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
SiteSurvey = Transition(label='Site Survey')
PermitRequest = Transition(label='Permit Request')
MaterialSourcing = Transition(label='Material Sourcing')
SystemDesign = Transition(label='System Design')
SoilTesting = Transition(label='Soil Testing')
WaterSetup = Transition(label='Water Setup')
SensorInstall = Transition(label='Sensor Install')
ClimateSetup = Transition(label='Climate Setup')
PlantSelection = Transition(label='Plant Selection')
SeedPlanting = Transition(label='Seed Planting')
IrrigationConfig = Transition(label='Irrigation Config')
PestMonitoring = Transition(label='Pest Monitoring')
StaffTraining = Transition(label='Staff Training')
YieldTracking = Transition(label='Yield Tracking')
CommunityMeet = Transition(label='Community Meet')
DataAnalysis = Transition(label='Data Analysis')
WasteManage = Transition(label='Waste Manage')

# Build partial order (strict sequencing + concurrency)

# Phase 1: Site Survey --> Permit Request
phase1 = StrictPartialOrder(nodes=[SiteSurvey, PermitRequest])
phase1.order.add_edge(SiteSurvey, PermitRequest)

# Phase 2: Material Sourcing --> System Design (material sourcing before system design)
phase2 = StrictPartialOrder(nodes=[MaterialSourcing, SystemDesign])
phase2.order.add_edge(MaterialSourcing, SystemDesign)

# Phase 3: Soil Testing (can run concurrently with Phase 2)
# Combine Phase 2 and Soil Testing in partial order with concurrency between Soil Testing and phase2
phase2_and_soil = StrictPartialOrder(nodes=[MaterialSourcing, SystemDesign, SoilTesting])
phase2_and_soil.order.add_edge(MaterialSourcing, SystemDesign)
# SoilTesting has no edges to phases 2 nodes, so it is concurrent

# Phase 4: Water Setup --> Sensor Install --> Climate Setup (sequential)
phase4 = StrictPartialOrder(nodes=[WaterSetup, SensorInstall, ClimateSetup])
phase4.order.add_edge(WaterSetup, SensorInstall)
phase4.order.add_edge(SensorInstall, ClimateSetup)

# Phase 5: Plant Selection --> Seed Planting --> Irrigation Config (sequential)
phase5 = StrictPartialOrder(nodes=[PlantSelection, SeedPlanting, IrrigationConfig])
phase5.order.add_edge(PlantSelection, SeedPlanting)
phase5.order.add_edge(SeedPlanting, IrrigationConfig)

# Phase 6: Pest Monitoring and Staff Training are concurrent
phase6 = StrictPartialOrder(nodes=[PestMonitoring, StaffTraining])
# no edges, concurrent

# Phase 7: Yield Tracking --> Community Meet --> Data Analysis --> Waste Manage (sequential)
phase7 = StrictPartialOrder(nodes=[YieldTracking, CommunityMeet, DataAnalysis, WasteManage])
phase7.order.add_edge(YieldTracking, CommunityMeet)
phase7.order.add_edge(CommunityMeet, DataAnalysis)
phase7.order.add_edge(DataAnalysis, WasteManage)

# Combine phases according to logical order inferred:
# 1) Phase 1 (Site Survey --> Permit Request)
# 2) Phase 2_and_SoilTesting (Material Sourcing and Soil Testing)
# 3) Phase 4 (Water Setup etc.)
# 4) Phase 5 (Plant Selection etc.)
# 5) Phase 6 (Pest Monitoring and Staff Training)
# 6) Phase 7 (Yield Tracking etc.)

# Combine all nodes into a single partial order
nodes_all = [
    SiteSurvey, PermitRequest,
    MaterialSourcing, SystemDesign, SoilTesting,
    WaterSetup, SensorInstall, ClimateSetup,
    PlantSelection, SeedPlanting, IrrigationConfig,
    PestMonitoring, StaffTraining,
    YieldTracking, CommunityMeet, DataAnalysis, WasteManage
]

root = StrictPartialOrder(nodes=nodes_all)

# Add edges for Phase 1
root.order.add_edge(SiteSurvey, PermitRequest)

# Add edges for Phase 2 and Soil Testing (only MaterialSourcing->SystemDesign)
root.order.add_edge(MaterialSourcing, SystemDesign)
# SoilTesting concurrent, no edges

# Add edges for Phase 4
root.order.add_edge(WaterSetup, SensorInstall)
root.order.add_edge(SensorInstall, ClimateSetup)

# Add edges for Phase 5
root.order.add_edge(PlantSelection, SeedPlanting)
root.order.add_edge(SeedPlanting, IrrigationConfig)

# Phase 6 concurrent (no edges)

# Add edges for Phase 7
root.order.add_edge(YieldTracking, CommunityMeet)
root.order.add_edge(CommunityMeet, DataAnalysis)
root.order.add_edge(DataAnalysis, WasteManage)

# Add higher level ordering edges between phases:
# Phase1 --> Phase2_and_soil_testing: PermitRequest -> MaterialSourcing and SoilTesting
root.order.add_edge(PermitRequest, MaterialSourcing)
root.order.add_edge(PermitRequest, SoilTesting)

# Phase2_and_soil_testing --> Phase4: SystemDesign -> WaterSetup and SoilTesting -> WaterSetup (to be safe)
root.order.add_edge(SystemDesign, WaterSetup)
root.order.add_edge(SoilTesting, WaterSetup)

# Phase4 --> Phase5: ClimateSetup -> PlantSelection
root.order.add_edge(ClimateSetup, PlantSelection)

# Phase5 --> Phase6: IrrigationConfig -> PestMonitoring and StaffTraining
root.order.add_edge(IrrigationConfig, PestMonitoring)
root.order.add_edge(IrrigationConfig, StaffTraining)

# Phase6 --> Phase7: PestMonitoring and StaffTraining -> YieldTracking
# Both need to complete before YieldTracking, so add edges from both nodes
root.order.add_edge(PestMonitoring, YieldTracking)
root.order.add_edge(StaffTraining, YieldTracking)