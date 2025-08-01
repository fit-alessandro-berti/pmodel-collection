# Generated from: 1d21af9b-7f4c-45fd-a2c4-0b40eeae3eaa.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming system within a dense metropolitan environment. It includes site evaluation for structural integrity, microclimate assessment, integration of automated hydroponic systems, real-time nutrient monitoring, energy optimization using renewable sources, vertical crop rotation planning, waste recycling loops, IoT sensor calibration, pest control through bioengineering, and community engagement for local food distribution. The process ensures sustainable food production while balancing technology, environment, and urban constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
SiteSurvey = Transition(label='Site Survey')
LoadTest = Transition(label='Load Test')
ClimateMap = Transition(label='Climate Map')
SystemDesign = Transition(label='System Design')
HydroSetup = Transition(label='Hydro Setup')
SensorInstall = Transition(label='Sensor Install')
NutrientMix = Transition(label='Nutrient Mix')
WaterCycle = Transition(label='Water Cycle')
EnergyAudit = Transition(label='Energy Audit')
CropPlanning = Transition(label='Crop Planning')
PestControl = Transition(label='Pest Control')
WasteLoop = Transition(label='Waste Loop')
DataSync = Transition(label='Data Sync')
YieldForecast = Transition(label='Yield Forecast')
CommunityLink = Transition(label='Community Link')

# WasteLoop is a loop: waste recycling loops - repeat WaterCycle then WasteLoop again, or exit
# So loop node with WaterCycle as first part, WasteLoop repeated, then exit loop
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[WaterCycle, WasteLoop])

# Sensor calibration and real-time nutrient monitoring and data sync
# Let's structure those as a partial order:
# NutrientMix --> DataSync
# SensorInstall concurrent with NutrientMix (can be done in parallel)
sensors_nutrients = StrictPartialOrder(nodes=[SensorInstall, NutrientMix, DataSync])
sensors_nutrients.order.add_edge(NutrientMix, DataSync)

# Energy optimization and Crop Planning
energy_crop = StrictPartialOrder(nodes=[EnergyAudit, CropPlanning])
energy_crop.order.add_edge(EnergyAudit, CropPlanning)

# Pest control and waste loop may be sequential: PestControl --> waste_loop
pest_and_waste = StrictPartialOrder(nodes=[PestControl, waste_loop])
pest_and_waste.order.add_edge(PestControl, waste_loop)

# Real-time nutrient monitoring and sensor calibration combined with pest control and waste loop,
# but these two blocks are sequential: sensors_nutrients --> pest_and_waste
nutrient_pest = StrictPartialOrder(nodes=[sensors_nutrients, pest_and_waste])
nutrient_pest.order.add_edge(sensors_nutrients, pest_and_waste)

# System Design includes Hydro Setup after SystemDesign
system_hydro = StrictPartialOrder(nodes=[SystemDesign, HydroSetup])
system_hydro.order.add_edge(SystemDesign, HydroSetup)

# Site evaluation is composed of SiteSurvey --> LoadTest --> ClimateMap
site_eval = StrictPartialOrder(nodes=[SiteSurvey, LoadTest, ClimateMap])
site_eval.order.add_edge(SiteSurvey, LoadTest)
site_eval.order.add_edge(LoadTest, ClimateMap)

# Then site_eval --> system_hydro --> nutrient_pest --> energy_crop
middle_seq = StrictPartialOrder(nodes=[site_eval, system_hydro, nutrient_pest, energy_crop])
middle_seq.order.add_edge(site_eval, system_hydro)
middle_seq.order.add_edge(system_hydro, nutrient_pest)
middle_seq.order.add_edge(nutrient_pest, energy_crop)

# YieldForecast and CommunityLink are last; YieldForecast --> CommunityLink
yield_community = StrictPartialOrder(nodes=[YieldForecast, CommunityLink])
yield_community.order.add_edge(YieldForecast, CommunityLink)

# energy_crop --> yield_community
final_seq = StrictPartialOrder(nodes=[middle_seq, yield_community])
final_seq.order.add_edge(middle_seq, yield_community)

root = final_seq