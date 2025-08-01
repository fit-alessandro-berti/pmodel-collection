# Generated from: 65cd00ff-08f7-4739-823f-cc40fa8e4833.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm designed to maximize crop yield in limited city spaces. It includes site analysis, modular infrastructure assembly, climate control calibration, nutrient solution preparation, automated planting, growth monitoring through IoT sensors, pest management with integrated biocontrol, adaptive lighting adjustment, harvesting automation, post-harvest processing, packaging, and distribution logistics. The process also involves continuous data analysis for yield optimization and sustainability reporting to comply with local regulations and environmental standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
ModuleSetup = Transition(label='Module Setup')
ClimateCalibrate = Transition(label='Climate Calibrate')
NutrientMix = Transition(label='Nutrient Mix')
PlantSeeding = Transition(label='Plant Seeding')
SensorInstall = Transition(label='Sensor Install')
GrowthMonitor = Transition(label='Growth Monitor')
PestControl = Transition(label='Pest Control')
LightAdjust = Transition(label='Light Adjust')
HarvestCrop = Transition(label='Harvest Crop')
ProcessSorting = Transition(label='Process Sorting')
PackGoods = Transition(label='Pack Goods')
LogisticsPlan = Transition(label='Logistics Plan')
DataAnalysis = Transition(label='Data Analysis')
SustainReport = Transition(label='Sustain Report')

# Build partial order according to the process description.
# Logical dependencies inferred:
# Site Survey --> Design Layout --> Module Setup --> Climate Calibrate
# Nutrient Mix parallel to Climate Calibrate but needed before Plant Seeding
# Plant Seeding after Module Setup, Climate Calibrate, Nutrient Mix
# Sensor Install after Plant Seeding
# Growth Monitor after Sensor Install
# Pest Control, Light Adjust concurrent after Growth Monitor
# Harvest Crop after Pest Control and Light Adjust
# Process Sorting after Harvest Crop
# Pack Goods after Process Sorting
# Logistics Plan after Pack Goods
# Data Analysis and Sustain Report concurrent after Logistics Plan (continuous data analysis and reporting)

# Define concurrent activities after Growth Monitor: Pest Control and Light Adjust
# We can model concurrency by just including them both as nodes without order edges between them

nodes = [
    SiteSurvey,
    DesignLayout,
    ModuleSetup,
    ClimateCalibrate,
    NutrientMix,
    PlantSeeding,
    SensorInstall,
    GrowthMonitor,
    PestControl,
    LightAdjust,
    HarvestCrop,
    ProcessSorting,
    PackGoods,
    LogisticsPlan,
    DataAnalysis,
    SustainReport
]

root = StrictPartialOrder(nodes=nodes)

# Add edges reflecting ordering/dependencies
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, ModuleSetup)
root.order.add_edge(ModuleSetup, ClimateCalibrate)
root.order.add_edge(ModuleSetup, NutrientMix)

root.order.add_edge(ClimateCalibrate, PlantSeeding)
root.order.add_edge(NutrientMix, PlantSeeding)

root.order.add_edge(PlantSeeding, SensorInstall)
root.order.add_edge(SensorInstall, GrowthMonitor)

root.order.add_edge(GrowthMonitor, PestControl)
root.order.add_edge(GrowthMonitor, LightAdjust)

root.order.add_edge(PestControl, HarvestCrop)
root.order.add_edge(LightAdjust, HarvestCrop)

root.order.add_edge(HarvestCrop, ProcessSorting)
root.order.add_edge(ProcessSorting, PackGoods)
root.order.add_edge(PackGoods, LogisticsPlan)

root.order.add_edge(LogisticsPlan, DataAnalysis)
root.order.add_edge(LogisticsPlan, SustainReport)