# Generated from: fd8f075a-8a0f-4f7d-9fab-1a33101fbbec.json
# Description: This process outlines the establishment of a vertical farming facility within an urban environment, integrating advanced hydroponic systems, renewable energy sources, and automated climate control to optimize crop yield year-round. It involves site analysis, structural adaptation for vertical stacking, nutrient solution formulation, sensor calibration for environmental monitoring, and integration of AI-driven growth prediction models. The workflow includes securing permits, community engagement for sustainability awareness, supplier coordination for seeds and equipment, staff training on novel cultivation techniques, and continuous data-driven optimization for resource efficiency and minimal waste. This atypical agricultural process combines technology, urban planning, and environmental stewardship to create a resilient food production system tailored to dense metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
SiteSurvey = Transition(label='Site Survey')
PermitFiling = Transition(label='Permit Filing')
StructurePrep = Transition(label='Structure Prep')
SystemInstall = Transition(label='System Install')
NutrientMix = Transition(label='Nutrient Mix')
SensorSetup = Transition(label='Sensor Setup')
AICalibration = Transition(label='AI Calibration')
SeedSourcing = Transition(label='Seed Sourcing')
StaffTraining = Transition(label='Staff Training')
EnergyConnect = Transition(label='Energy Connect')
WaterCycle = Transition(label='Water Cycle')
GrowthMonitor = Transition(label='Growth Monitor')
WasteAudit = Transition(label='Waste Audit')
CommunityMeet = Transition(label='Community Meet')
DataReview = Transition(label='Data Review')
YieldForecast = Transition(label='Yield Forecast')

# From description, the process roughly:
# 1) Site Survey and Permit Filing start the project (can be concurrent)
# 2) Then Structure Prep after Permit Filing
# 3) System Install after Structure Prep
# 4) Nutrient Mix and Sensor Setup after System Install (concurrent)
# 5) AI Calibration after Sensor Setup
# 6) Seed Sourcing and Staff Training in parallel after AI Calibration
# 7) Energy Connect (likely linked after System Install or Structure Prep) 
#    place after System Install, concurrent with Nutrient Mix & Sensor Setup
# 8) Community Meet can be concurrent with Seed Sourcing and Staff Training
# 9) Water Cycle and Growth Monitor after AI Calibration and Seed Sourcing (concurrent)
# 10) Data Review after Growth Monitor and Waste Audit
# 11) Waste Audit after Water Cycle
# 12) Yield Forecast after Data Review

# Build partial orders accordingly

# Step 1: Site Survey and Permit Filing concurrent
start_nodes = [SiteSurvey, PermitFiling]

# Step 2: Structure Prep after Permit Filing
# Site Survey is preparatory too, but no explicit dependencies except Permit Filing --> Structure Prep
# We'll add Structure Prep depending on Permit Filing only

# Step 3: System Install after Structure Prep
# Step 4: Nutrient Mix, Sensor Setup, Energy Connect after System Install (concurrent)
# Step 5: AI Calibration after Sensor Setup
# Step 6: Seed Sourcing, Staff Training after AI Calibration (concurrent)
# Step 7: Community Meet concurrent with Seed Sourcing & Staff Training
# Step 8: Water Cycle, Growth Monitor after AI Calibration and Seed Sourcing (concurrent)
# Step 9: Waste Audit after Water Cycle
# Step 10: Data Review after Growth Monitor and Waste Audit
# Step 11: Yield Forecast after Data Review

nodes = [
    SiteSurvey, PermitFiling, StructurePrep, SystemInstall, NutrientMix, SensorSetup,
    EnergyConnect, AICalibration, SeedSourcing, StaffTraining, CommunityMeet,
    WaterCycle, GrowthMonitor, WasteAudit, DataReview, YieldForecast
]

root = StrictPartialOrder(nodes=nodes)

# Order edges

# Permit Filing --> Structure Prep
root.order.add_edge(PermitFiling, StructurePrep)

# Site Survey and Permit Filing concurrent, no edge needed between them

# Structure Prep --> System Install
root.order.add_edge(StructurePrep, SystemInstall)

# System Install --> Nutrient Mix
root.order.add_edge(SystemInstall, NutrientMix)

# System Install --> Sensor Setup
root.order.add_edge(SystemInstall, SensorSetup)

# System Install --> Energy Connect
root.order.add_edge(SystemInstall, EnergyConnect)

# Sensor Setup --> AI Calibration
root.order.add_edge(SensorSetup, AICalibration)

# AI Calibration --> Seed Sourcing
root.order.add_edge(AICalibration, SeedSourcing)

# AI Calibration --> Staff Training
root.order.add_edge(AICalibration, StaffTraining)

# Community Meet concurrent with Seed Sourcing & Staff Training
# To model concurrency, no edges between them

# Seed Sourcing --> Water Cycle
root.order.add_edge(SeedSourcing, WaterCycle)

# AICalibration --> Growth Monitor
root.order.add_edge(AICalibration, GrowthMonitor)

# Water Cycle --> Waste Audit
root.order.add_edge(WaterCycle, WasteAudit)

# Growth Monitor --> Data Review
root.order.add_edge(GrowthMonitor, DataReview)

# Waste Audit --> Data Review
root.order.add_edge(WasteAudit, DataReview)

# Data Review --> Yield Forecast
root.order.add_edge(DataReview, YieldForecast)