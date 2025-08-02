# Generated from: 1f92bbd0-37c1-4e1c-96c4-ac48d011926a.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming operation within a constrained city environment. It includes initial site evaluation, modular system design, climate control calibration, nutrient optimization, and automated harvesting integration. The process further involves stakeholder engagement for local sourcing, regulatory compliance checks, energy consumption analysis, waste recycling protocols, and real-time growth monitoring through IoT sensors. Each activity ensures sustainability, scalability, and community impact while addressing unique urban agricultural challenges such as space limitations and environmental factors, making this a multifaceted and innovative business endeavor.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SiteSurvey = Transition(label='Site Survey')
DesignModules = Transition(label='Design Modules')
ClimateSetup = Transition(label='Climate Setup')
NutrientMix = Transition(label='Nutrient Mix')
SensorInstall = Transition(label='Sensor Install')
WaterCycle = Transition(label='Water Cycle')
LightingTune = Transition(label='Lighting Tune')
EnergyAudit = Transition(label='Energy Audit')
WastePlan = Transition(label='Waste Plan')
ComplianceCheck = Transition(label='Compliance Check')
StaffTraining = Transition(label='Staff Training')
GrowthMonitor = Transition(label='Growth Monitor')
HarvestSync = Transition(label='Harvest Sync')
DistributionMap = Transition(label='Distribution Map')
CommunityMeet = Transition(label='Community Meet')
DataAnalyze = Transition(label='Data Analyze')
ScalePlan = Transition(label='Scale Plan')

# Model the loop for growth-monitoring and adjustment phase:
# Loop( GrowthMonitor ; choice(exit or DataAnalyze and ScalePlan) )
growthAdjustmentLoop = OperatorPOWL(operator=Operator.LOOP, children=[
    GrowthMonitor,
    OperatorPOWL(operator=Operator.XOR, children=[ScalePlan, DataAnalyze])
])

# Partial order representing the main process structure:

# Initial steps sequence:
# SiteSurvey --> DesignModules --> ClimateSetup --> NutrientMix
# Then parallel climate-related setup and equipment installation:
# ClimateSetup --> (WaterCycle, LightingTune, SensorInstall) concurrent

# Stakeholder and regulation related steps in parallel branch:
# CommunityMeet --> ComplianceCheck --> StaffTraining

# Energy and waste branch sequence:
# EnergyAudit --> WastePlan

# Harvesting and distribution branch:
# HarvestSync --> DistributionMap

# Combining all branches with partial orders:
# NutrientMix --> all three branches in parallel:
# 1) WaterCycle & LightingTune & SensorInstall
# 2) CommunityMeet --> ComplianceCheck --> StaffTraining
# 3) EnergyAudit --> WastePlan
# 4) HarvestSync --> DistributionMap

# Then after those branches, trigger growthAdjustmentLoop

# Create partial orders and nodes

# Concurrent branch 1: WaterCycle, LightingTune, SensorInstall
climateBranches = [WaterCycle, LightingTune, SensorInstall]

# Stakeholder & Compliance branch linear chain:
stakeholderBranch = StrictPartialOrder(nodes=[CommunityMeet, ComplianceCheck, StaffTraining])
stakeholderBranch.order.add_edge(CommunityMeet, ComplianceCheck)
stakeholderBranch.order.add_edge(ComplianceCheck, StaffTraining)

# Energy & waste branch linear chain:
energyWasteBranch = StrictPartialOrder(nodes=[EnergyAudit, WastePlan])
energyWasteBranch.order.add_edge(EnergyAudit, WastePlan)

# Harvest & distribution linear chain:
harvestBranch = StrictPartialOrder(nodes=[HarvestSync, DistributionMap])
harvestBranch.order.add_edge(HarvestSync, DistributionMap)

# Now build the top-level partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    DesignModules,
    ClimateSetup,
    NutrientMix,
    *climateBranches,
    stakeholderBranch,
    energyWasteBranch,
    harvestBranch,
    growthAdjustmentLoop
])

# Add sequential order for the initial activities
root.order.add_edge(SiteSurvey, DesignModules)
root.order.add_edge(DesignModules, ClimateSetup)
root.order.add_edge(ClimateSetup, NutrientMix)

# NutrientMix triggers all branches concurrently:
for node in climateBranches:
    root.order.add_edge(NutrientMix, node)

# NutrientMix triggers stakeholderBranch, energyWasteBranch, harvestBranch
root.order.add_edge(NutrientMix, stakeholderBranch)
root.order.add_edge(NutrientMix, energyWasteBranch)
root.order.add_edge(NutrientMix, harvestBranch)

# All branches must finish before growthAdjustmentLoop
for node in climateBranches:
    root.order.add_edge(node, growthAdjustmentLoop)
root.order.add_edge(stakeholderBranch, growthAdjustmentLoop)
root.order.add_edge(energyWasteBranch, growthAdjustmentLoop)
root.order.add_edge(harvestBranch, growthAdjustmentLoop)