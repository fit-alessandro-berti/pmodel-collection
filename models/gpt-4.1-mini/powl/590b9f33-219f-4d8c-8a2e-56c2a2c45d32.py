# Generated from: 590b9f33-219f-4d8c-8a2e-56c2a2c45d32.json
# Description: This process outlines the integration of vertical farming systems within urban infrastructure to optimize space usage, enhance food production, and reduce environmental impact. It involves site analysis, modular system design, automated nutrient delivery, energy optimization, and continuous monitoring. The process includes collaboration with local authorities for permits, community engagement for awareness, and adaptive maintenance strategies to ensure sustainability. Data from IoT sensors is analyzed to adjust environmental controls dynamically, while logistics management handles distribution to local markets. The approach supports circular economy principles by recycling water and organic waste, integrating renewable energy sources, and fostering urban biodiversity through green corridors. The goal is to create resilient, efficient, and scalable urban agriculture solutions tailored to diverse city landscapes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SiteSurvey = Transition(label='Site Survey')
PermitReview = Transition(label='Permit Review')
DesignLayout = Transition(label='Design Layout')
ModularBuild = Transition(label='Modular Build')
SensorInstall = Transition(label='Sensor Install')
NutrientMix = Transition(label='Nutrient Mix')
WaterCycle = Transition(label='Water Cycle')
EnergyAudit = Transition(label='Energy Audit')
IoTSetup = Transition(label='IoT Setup')
DataAnalyze = Transition(label='Data Analyze')
EnvControl = Transition(label='Env Control')
WasteRecycle = Transition(label='Waste Recycle')
CommunityMeet = Transition(label='Community Meet')
MarketLink = Transition(label='Market Link')
SystemMaintain = Transition(label='System Maintain')
BiodiversityPlan = Transition(label='Biodiversity Plan')
RenewableSync = Transition(label='Renewable Sync')

# Collaboration parallel choices after Site Survey
# After SiteSurvey: PermitReview and CommunityMeet can be concurrent (no order)
# Both must complete before DesignLayout

collaboration = StrictPartialOrder(nodes=[PermitReview, CommunityMeet])

# Core design and build partial order
design_build = StrictPartialOrder(nodes=[DesignLayout, ModularBuild])
design_build.order.add_edge(DesignLayout, ModularBuild)

# Sensor install and nutrient mix run in parallel after modular build
# SensorInstall precedes IoTSetup, NutrientMix precedes WaterCycle (recycling)
sensor_path = StrictPartialOrder(nodes=[SensorInstall, IoTSetup])
sensor_path.order.add_edge(SensorInstall, IoTSetup)

nutrient_path = StrictPartialOrder(nodes=[NutrientMix, WaterCycle])
nutrient_path.order.add_edge(NutrientMix, WaterCycle)

# Energy Audit and Renewable Sync run in parallel, then Energy Audit leads to Renewable Sync for integration
energy_path = StrictPartialOrder(nodes=[EnergyAudit, RenewableSync])
energy_path.order.add_edge(EnergyAudit, RenewableSync)

# Data analysis loop: DataAnalyze -> EnvControl repeated until exit (loop)
data_env_loop = OperatorPOWL(operator=Operator.LOOP, children=[DataAnalyze, EnvControl])

# Waste Recycle and BiodiversityPlan can be concurrent, no order
sustainability = StrictPartialOrder(nodes=[WasteRecycle, BiodiversityPlan])

# MarketLink and SystemMaintain can proceed after IoTSetup and EnvControl (monitoring & logistics)
# Require both IoTSetup and EnvControl before MarketLink and SystemMaintain

monitoring = StrictPartialOrder(nodes=[MarketLink, SystemMaintain])

# Build the main partial order:

# Step1: after SiteSurvey, collaboration (PermitReview, CommunityMeet) concurrently
# Both before DesignLayout
# DesignLayout before ModularBuild
# ModularBuild before Sensor and Nutrient paths (run in parallel)
# Sensor path before IoTSetup
# Nutrient path before WaterCycle
# After IoTSetup and EnvControl (loop), MarketLink and SystemMaintain
# EnergyAudit before RenewableSync (in parallel with Sensor/Nutrient)
# Sustainability nodes (WasteRecycle, BiodiversityPlan) concurrent with EnergyAudit path (can start after ModularBuild as well)

root = StrictPartialOrder(
    nodes=[
        SiteSurvey,
        collaboration,
        DesignLayout,
        ModularBuild,
        sensor_path,
        nutrient_path,
        energy_path,
        data_env_loop,
        sustainability,
        monitoring
    ]
)

# Add order edges to reflect the described flows:

# SiteSurvey before collaboration (PermitReview, CommunityMeet)
root.order.add_edge(SiteSurvey, collaboration)
# collaboration before DesignLayout
root.order.add_edge(collaboration, DesignLayout)
# DesignLayout before ModularBuild
root.order.add_edge(DesignLayout, ModularBuild)
# ModularBuild before SensorInstall and NutrientMix (sensor_path and nutrient_path nodes)
root.order.add_edge(ModularBuild, sensor_path)
root.order.add_edge(ModularBuild, nutrient_path)
# ModularBuild before energy_path and sustainability (can begin concurrently)
root.order.add_edge(ModularBuild, energy_path)
root.order.add_edge(ModularBuild, sustainability)
# IoTSetup (sensor_path's end) and EnvControl (in loop) before monitoring (MarketLink, SystemMaintain)
# We need to add edge from sensor_path nodes leaf to monitoring
root.order.add_edge(sensor_path, monitoring)  # sensor_path ends with IoTSetup
# EnvControl is in a loop, data_env_loop emits loop whose first child is DataAnalyze, second EnvControl
# The loop outputs a node that conceptually finishes after EnvControl finally exits
# For simplicity, assume data_env_loop ends with EnvControl 
root.order.add_edge(data_env_loop, monitoring)
# EnergyAudit before RenewableSync (inside energy_path already linked)
# Add edge between energy_path and data_env_loop: energy_path likely before or concurrent with loop
# Considering order: energy_path before data_env_loop (DataAnalyze and EnvControl depend on energy optimization)
root.order.add_edge(energy_path, data_env_loop)

# Finally, ensure that data_env_loop is reachable after energy path and sensor_path (which is after modular build)

# The sustainability nodes can be concurrent, no order needed between them and others beyond ModularBuild

# Sanity check: monitoring waits for IoTSetup (sensor_path) and EnvControl (data_env_loop)

# The model reflects concurrency, loops, and choices as per the main description.
