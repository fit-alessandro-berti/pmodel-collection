# Generated from: 8ccfaa81-8c42-49eb-a56c-9a61f5eb74c1.json
# Description: This process outlines the steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It includes site assessment, modular system design, environmental control calibration, crop selection based on local demand, nutrient solution formulation, automation integration, pest monitoring, employee training, and continuous yield optimization. The process ensures sustainable resource use, minimal waste, and maximized production efficiency in a confined urban environment, adapting to fluctuating market needs and regulatory requirements while maintaining high product quality and safety standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
SystemBuild = Transition(label='System Build')
ClimateSetup = Transition(label='Climate Setup')
CropSelect = Transition(label='Crop Select')
NutrientMix = Transition(label='Nutrient Mix')
InstallSensors = Transition(label='Install Sensors')
AutomateControls = Transition(label='Automate Controls')
PestMonitor = Transition(label='Pest Monitor')
StaffTrain = Transition(label='Staff Train')
HarvestPlan = Transition(label='Harvest Plan')
DataAnalyze = Transition(label='Data Analyze')
WasteManage = Transition(label='Waste Manage')
MarketAlign = Transition(label='Market Align')
YieldOptimize = Transition(label='Yield Optimize')

# Model partial orders according to logical steps and concurrency inferred from description:
# 1) Site Survey -> Design Layout -> System Build -> Climate Setup
# 2) Crop Select and Nutrient Mix depend on Design Layout, can run in parallel
# 3) Install Sensors and Automate Controls depend on System Build (parallel)
# 4) Pest Monitor and Staff Train can run after Automate Controls (parallel)
# 5) Harvest Plan after Crop Select and Staff Train
# 6) Data Analyze after Harvest Plan (continuous yield monitoring)
# 7) Waste Manage and Market Align can run concurrently with Data Analyze
# 8) Yield Optimize depends on Data Analyze and Waste Manage, Market Align (concurrent prerequisites)

# Define groups to help ordering
# Partial Order nodes
po_nodes = [
    SiteSurvey, DesignLayout, SystemBuild, ClimateSetup,
    CropSelect, NutrientMix,
    InstallSensors, AutomateControls,
    PestMonitor, StaffTrain,
    HarvestPlan, DataAnalyze,
    WasteManage, MarketAlign,
    YieldOptimize
]

root = StrictPartialOrder(nodes=po_nodes)

# Define order edges
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, SystemBuild)
root.order.add_edge(SystemBuild, ClimateSetup)

# CropSelect and NutrientMix depend on DesignLayout
root.order.add_edge(DesignLayout, CropSelect)
root.order.add_edge(DesignLayout, NutrientMix)

# InstallSensors and AutomateControls depend on SystemBuild
root.order.add_edge(SystemBuild, InstallSensors)
root.order.add_edge(SystemBuild, AutomateControls)

# PestMonitor and StaffTrain after AutomateControls
root.order.add_edge(AutomateControls, PestMonitor)
root.order.add_edge(AutomateControls, StaffTrain)

# HarvestPlan depends on CropSelect and StaffTrain
root.order.add_edge(CropSelect, HarvestPlan)
root.order.add_edge(StaffTrain, HarvestPlan)

# DataAnalyze after HarvestPlan
root.order.add_edge(HarvestPlan, DataAnalyze)

# WasteManage and MarketAlign parallel and after HarvestPlan (implicit)
root.order.add_edge(HarvestPlan, WasteManage)
root.order.add_edge(HarvestPlan, MarketAlign)

# YieldOptimize depends on DataAnalyze, WasteManage, MarketAlign
root.order.add_edge(DataAnalyze, YieldOptimize)
root.order.add_edge(WasteManage, YieldOptimize)
root.order.add_edge(MarketAlign, YieldOptimize)