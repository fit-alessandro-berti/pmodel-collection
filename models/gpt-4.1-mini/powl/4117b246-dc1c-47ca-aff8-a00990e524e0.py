# Generated from: 4117b246-dc1c-47ca-aff8-a00990e524e0.json
# Description: This process details the establishment of a fully automated urban vertical farm within a repurposed industrial building. It involves site assessment, environmental control calibration, hydroponic system installation, integrated pest management, and AI-driven crop monitoring. The process ensures sustainable energy use, water recycling, and optimized yield through data analytics and continuous improvement cycles. Stakeholders include agronomists, engineers, supply chain managers, and local regulators, coordinating to transform urban spaces into high-efficiency food production hubs while minimizing ecological impact and maximizing social benefits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
InstallFrames = Transition(label='Install Frames')
SetupHydroponics = Transition(label='Setup Hydroponics')
CalibrateSensors = Transition(label='Calibrate Sensors')
SeedPlanting = Transition(label='Seed Planting')
NutrientMix = Transition(label='Nutrient Mix')
PestInspection = Transition(label='Pest Inspection')
DataIntegration = Transition(label='Data Integration')
ClimateControl = Transition(label='Climate Control')
EnergyAudit = Transition(label='Energy Audit')
WaterRecycling = Transition(label='Water Recycling')
GrowthMonitoring = Transition(label='Growth Monitoring')
YieldForecast = Transition(label='Yield Forecast')
HarvestPrep = Transition(label='Harvest Prep')
Packaging = Transition(label='Packaging')
Distribution = Transition(label='Distribution')
RegulatoryCheck = Transition(label='Regulatory Check')
FeedbackLoop = Transition(label='Feedback Loop')

# Define the loop body A and continue B for the continuous improvement cycle represented by Feedback Loop
# Loop: execute FeedbackLoop then choose to exit or continue cycle again (simulate continuous improvement)
loop = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackLoop, SilentTransition()])  # loop B is silent, will re-execute A if chosen

# Construct the main partial order of activities
# We organize the workflow in stages logically derived from description

# Stage 1: Initial assessment and design
stage1_nodes = [SiteSurvey, DesignLayout, InstallFrames, SetupHydroponics, CalibrateSensors]

stage1 = StrictPartialOrder(nodes=stage1_nodes)
# Site Survey -> Design Layout
stage1.order.add_edge(SiteSurvey, DesignLayout)
# Design Layout -> Install Frames and Setup Hydroponics
stage1.order.add_edge(DesignLayout, InstallFrames)
stage1.order.add_edge(DesignLayout, SetupHydroponics)
# Install Frames and Setup Hydroponics concurrent, then Calibrate Sensors after both
stage1.order.add_edge(InstallFrames, CalibrateSensors)
stage1.order.add_edge(SetupHydroponics, CalibrateSensors)

# Stage 2: Planting and maintenance
stage2_nodes = [SeedPlanting, NutrientMix, PestInspection]
stage2 = StrictPartialOrder(nodes=stage2_nodes)
# Seed Planting -> Nutrient Mix and Pest Inspection concurrent
stage2.order.add_edge(SeedPlanting, NutrientMix)
stage2.order.add_edge(SeedPlanting, PestInspection)

# Stage 3: Integration and environment control
stage3_nodes = [DataIntegration, ClimateControl]
stage3 = StrictPartialOrder(nodes=stage3_nodes)
# Data Integration and Climate Control concurrent (no order edges)

# Stage 4: Sustainability checks
stage4_nodes = [EnergyAudit, WaterRecycling]
stage4 = StrictPartialOrder(nodes=stage4_nodes)
# Energy Audit and Water Recycling concurrent

# Stage 5: Monitoring and forecasting
stage5_nodes = [GrowthMonitoring, YieldForecast]
stage5 = StrictPartialOrder(nodes=stage5_nodes)
# Growth Monitoring -> Yield Forecast
stage5.order.add_edge(GrowthMonitoring, YieldForecast)

# Stage 6: Harvest and distribution
stage6_nodes = [HarvestPrep, Packaging, Distribution]
stage6 = StrictPartialOrder(nodes=stage6_nodes)
# Harvest Prep -> Packaging -> Distribution
stage6.order.add_edge(HarvestPrep, Packaging)
stage6.order.add_edge(Packaging, Distribution)

# Stage 7: Regulatory and feedback loop
# Regulatory Check concurrent with Distribution
regulatory_and_loop = StrictPartialOrder(nodes=[RegulatoryCheck, loop])
# No order edges, can run concurrently

# Combine all stages with appropriate ordering

root = StrictPartialOrder(nodes=[
    stage1, stage2, stage3, stage4, stage5, stage6, regulatory_and_loop
])

# Connect stages with orders:

# Stage 1 completes before Stage 2 starts (Calibrate Sensors before Seed Planting)
root.order.add_edge(stage1, stage2)

# Stage 2 completes before Stage 3 (Pest Inspection or Nutrient Mix before Data Integration)
# Choose Pest Inspection as predecessor
root.order.add_edge(stage2, stage3)

# Stage 3 and Stage 4 run concurrently but Stage 3 before Stage 5
root.order.add_edge(stage3, stage5)

# Stage 4 concurrent with Stage 3 and Stage 5, no direct order needed

# Stage 5 before Stage 6 (Yield Forecast before Harvest Prep)
root.order.add_edge(stage5, stage6)

# Stage 6 before Regulatory Check and Feedback Loop (Distribution before regulatory/loop)
root.order.add_edge(stage6, regulatory_and_loop)