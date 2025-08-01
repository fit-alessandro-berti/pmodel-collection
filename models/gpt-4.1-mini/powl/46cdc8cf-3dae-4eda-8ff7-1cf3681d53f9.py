# Generated from: 46cdc8cf-3dae-4eda-8ff7-1cf3681d53f9.json
# Description: This process outlines the setup of an urban vertical farming system designed to optimize limited city space for sustainable agriculture. It involves site analysis, modular system design, nutrient cycling planning, and integration of IoT sensors for microclimate control. Activities include selecting plant species based on local demand and light requirements, establishing water recycling loops, and coordinating with local authorities for compliance. The process further encompasses staff training on automated maintenance, real-time monitoring of crop health, and iterative optimization of growth parameters to maximize yield while minimizing energy consumption and waste. The system also incorporates community engagement strategies to promote urban agriculture awareness and potential partnerships with local markets for direct produce sales.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
SiteSurvey = Transition(label='Site Survey')
DesignModules = Transition(label='Design Modules')
SelectCrops = Transition(label='Select Crops')
PlanNutrients = Transition(label='Plan Nutrients')
InstallSensors = Transition(label='Install Sensors')
SetupLighting = Transition(label='Setup Lighting')
BuildStructures = Transition(label='Build Structures')
IntegrateIoT = Transition(label='Integrate IoT')
WaterLoop = Transition(label='Water Loop')
TestSystems = Transition(label='Test Systems')
TrainStaff = Transition(label='Train Staff')
MonitorGrowth = Transition(label='Monitor Growth')
AdjustParameters = Transition(label='Adjust Parameters')
EngageCommunity = Transition(label='Engage Community')
MarketProduce = Transition(label='Market Produce')

# Nutrient cycling planned and water recycling loop form a loop:
# Plan Nutrients -> loop Water Loop and Plan Nutrients again or exit
nutrient_loop = OperatorPOWL(operator=Operator.LOOP, children=[PlanNutrients, WaterLoop])

# Select Crops depends on Site Survey and Design Modules
# Design Modules depends on Site Survey
po_design = StrictPartialOrder(nodes=[SiteSurvey, DesignModules, SelectCrops])
po_design.order.add_edge(SiteSurvey, DesignModules)
po_design.order.add_edge(SiteSurvey, SelectCrops)
po_design.order.add_edge(DesignModules, SelectCrops)

# Installation and integration activities can happen in partial order:
# Build Structures precedes Setup Lighting and Install Sensors in parallel
# Integrate IoT follows both Setup Lighting and Install Sensors
po_install = StrictPartialOrder(
    nodes=[BuildStructures, SetupLighting, InstallSensors, IntegrateIoT]
)
po_install.order.add_edge(BuildStructures, SetupLighting)
po_install.order.add_edge(BuildStructures, InstallSensors)
po_install.order.add_edge(SetupLighting, IntegrateIoT)
po_install.order.add_edge(InstallSensors, IntegrateIoT)

# Testing follows Install and integration
# Testing depends on Integrate IoT and Water Loop (nutrient loop)
# Wait to allow Water Loop within nutrient_loop to complete at least once before testing
testing_stage = StrictPartialOrder(nodes=[nutrient_loop, TestSystems, po_install])
# Note: nutrient_loop and po_install are both nodes here, so we can add edges between
testing_stage = StrictPartialOrder(nodes=[nutrient_loop, TestSystems, BuildStructures, SetupLighting, InstallSensors, IntegrateIoT])
testing_stage.order.add_edge(nutrient_loop, TestSystems)
testing_stage.order.add_edge(IntegrateIoT, TestSystems)
# BuildStructures etc. already included in po_install above but to avoid confusion, we'll just use po_install + nutrient_loop + TestSystems as separate nodes:
po_testing = StrictPartialOrder(nodes=[nutrient_loop, TestSystems, po_install])
po_testing.order.add_edge(nutrient_loop, TestSystems)
po_testing.order.add_edge(po_install, TestSystems)

# Staff training follows testing
# Monitoring and adjustment form a loop (* (Monitor Growth, Adjust Parameters))
monitor_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[MonitorGrowth, AdjustParameters])

# Staff training before monitoring loop
training_and_monitoring = StrictPartialOrder(nodes=[TrainStaff, monitor_adjust_loop])
training_and_monitoring.order.add_edge(TrainStaff, monitor_adjust_loop)

# Community engagement and market produce are concurrent after training and monitoring
community_and_market = StrictPartialOrder(nodes=[EngageCommunity, MarketProduce])

# Overall partial order
# 1. Design phase: po_design
# 2. Installation + nutrient loop + testing (po_install + nutrient_loop + TestSystems)
# 3. Training + monitoring loop
# 4. Community & market

# Create a top-level PO with nodes:
# po_design, po_testing, training_and_monitoring, community_and_market

root = StrictPartialOrder(
    nodes=[po_design, po_testing, training_and_monitoring, community_and_market]
)

# Establish control flow between phases
root.order.add_edge(po_design, po_testing)
root.order.add_edge(po_testing, training_and_monitoring)
root.order.add_edge(training_and_monitoring, community_and_market)