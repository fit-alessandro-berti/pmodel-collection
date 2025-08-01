# Generated from: ae04f80e-0f7a-45fc-9a41-e3a2be008733.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming system within a repurposed warehouse. It includes site analysis, environmental control installation, seed selection, and nutrient calibration to optimize crop yields. The process further involves integrating automated harvesting robots, data-driven growth monitoring, and waste recycling protocols to ensure sustainability. Stakeholder coordination, regulatory compliance checks, and market launch strategies are also incorporated to guarantee a successful and scalable urban agriculture enterprise.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SiteSurvey = Transition(label='Site Survey')
LayoutDesign = Transition(label='Layout Design')
EnvironmentalSetup = Transition(label='Environmental Setup')
SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
LightingInstall = Transition(label='Lighting Install')
IrrigationSetup = Transition(label='Irrigation Setup')
SensorCalibration = Transition(label='Sensor Calibration')
GrowthMonitoring = Transition(label='Growth Monitoring')
AutomatedHarvest = Transition(label='Automated Harvest')
WasteRecycling = Transition(label='Waste Recycling')
DataAnalysis = Transition(label='Data Analysis')
ComplianceCheck = Transition(label='Compliance Check')
StakeholderMeet = Transition(label='Stakeholder Meet')
MarketLaunch = Transition(label='Market Launch')

# Partial order for site and environmental preparation in sequence:
# Site Survey --> Layout Design --> Environmental Setup
preparation = StrictPartialOrder(nodes=[SiteSurvey, LayoutDesign, EnvironmentalSetup])
preparation.order.add_edge(SiteSurvey, LayoutDesign)
preparation.order.add_edge(LayoutDesign, EnvironmentalSetup)

# Partial order for seed and nutrient setup (can be concurrent with lighting and irrigation setup)
seed_nutrient = StrictPartialOrder(nodes=[SeedSelection, NutrientMix])
seed_nutrient.order.add_edge(SeedSelection, NutrientMix)

lighting_irrigation = StrictPartialOrder(nodes=[LightingInstall, IrrigationSetup])
lighting_irrigation.order.add_edge(LightingInstall, IrrigationSetup)

# Sensor calibration after lighting and irrigation
sensor_calib = StrictPartialOrder(nodes=[SensorCalibration])
# Will link later

# Growth monitoring after sensor calibration
growth_monitoring = StrictPartialOrder(nodes=[GrowthMonitoring])

# Automated harvest concurrent with waste recycling
auto_harvest_recycle = StrictPartialOrder(nodes=[AutomatedHarvest, WasteRecycling])

# Data analysis after growth monitoring and automated harvest & waste recycling
data_analysis = StrictPartialOrder(nodes=[DataAnalysis])

# Compliance check and stakeholder meet can be done concurrently after data analysis
compliance_stakeholder = StrictPartialOrder(nodes=[ComplianceCheck, StakeholderMeet])

# Market launch after compliance check and stakeholder meet
market_launch = StrictPartialOrder(nodes=[MarketLaunch])

# Build the big partial order with dependencies:

# Root nodes:
# preparation must complete first
# seed_nutrient, lighting_irrigation can start after preparation
root_nodes = [
    preparation,
    seed_nutrient,
    lighting_irrigation,
    sensor_calib,
    growth_monitoring,
    auto_harvest_recycle,
    data_analysis,
    compliance_stakeholder,
    market_launch,
]

root = StrictPartialOrder(nodes=root_nodes)

# Add order edges:

# preparation --> seed_nutrient
root.order.add_edge(preparation, seed_nutrient)
# preparation --> lighting_irrigation
root.order.add_edge(preparation, lighting_irrigation)

# seed_nutrient and lighting_irrigation --> sensor_calib
root.order.add_edge(seed_nutrient, sensor_calib)
root.order.add_edge(lighting_irrigation, sensor_calib)

# sensor_calib --> growth_monitoring
root.order.add_edge(sensor_calib, growth_monitoring)

# growth_monitoring --> data_analysis
root.order.add_edge(growth_monitoring, data_analysis)

# auto_harvest_recycle after growth_monitoring (to represent monitoring informs harvesting and recycling)
root.order.add_edge(growth_monitoring, auto_harvest_recycle)

# auto_harvest_recycle --> data_analysis
root.order.add_edge(auto_harvest_recycle, data_analysis)

# data_analysis --> compliance_stakeholder
root.order.add_edge(data_analysis, compliance_stakeholder)

# compliance_stakeholder --> market_launch
root.order.add_edge(compliance_stakeholder, market_launch)