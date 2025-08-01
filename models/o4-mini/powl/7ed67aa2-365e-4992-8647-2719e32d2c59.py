# Generated from: 7ed67aa2-365e-4992-8647-2719e32d2c59.json
# Description: This process details the complex steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site evaluation, structural modification, environmental system installation, crop selection, automated irrigation setup, data analytics integration, pest management protocols, nutrient cycling optimization, energy consumption monitoring, and community engagement programs. The process ensures sustainable urban agriculture by combining advanced technology with local ecosystem considerations, aiming to maximize yield in limited space while minimizing environmental impact and fostering social responsibility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
SiteSurvey = Transition(label='Site Survey')
StructuralAudit = Transition(label='Structural Audit')
PermitFiling = Transition(label='Permit Filing')
DesignLayout = Transition(label='Design Layout')
InstallRacks = Transition(label='Install Racks')
SetupLighting = Transition(label='Setup Lighting')
ConfigureHVAC = Transition(label='Configure HVAC')
IrrigationInstall = Transition(label='Irrigation Install')
SensorIntegration = Transition(label='Sensor Integration')
SelectCrops = Transition(label='Select Crops')
PlantSeeding = Transition(label='Plant Seeding')
DataCalibration = Transition(label='Data Calibration')
PestControl = Transition(label='Pest Control')
NutrientMix = Transition(label='Nutrient Mix')
WasteRecycling = Transition(label='Waste Recycling')
EnergyTracking = Transition(label='Energy Tracking')
HarvestPlanning = Transition(label='Harvest Planning')
CommunityOutreach = Transition(label='Community Outreach')

# Build partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey, StructuralAudit, PermitFiling, DesignLayout,
    InstallRacks, SetupLighting, ConfigureHVAC, IrrigationInstall,
    SensorIntegration, SelectCrops, PlantSeeding, DataCalibration,
    PestControl, NutrientMix, WasteRecycling, EnergyTracking,
    HarvestPlanning, CommunityOutreach
])

# Preliminary sequence
root.order.add_edge(SiteSurvey, StructuralAudit)
root.order.add_edge(StructuralAudit, PermitFiling)
root.order.add_edge(PermitFiling, DesignLayout)

# After design: installations and crop selection
for nxt in [InstallRacks, SetupLighting, ConfigureHVAC, IrrigationInstall, SensorIntegration, SelectCrops]:
    root.order.add_edge(DesignLayout, nxt)

# Sensor data calibration
root.order.add_edge(SensorIntegration, DataCalibration)

# Seeding after installations and crop selection
for pred in [InstallRacks, SetupLighting, ConfigureHVAC, IrrigationInstall, SelectCrops]:
    root.order.add_edge(pred, PlantSeeding)

# Data analytics informs downstream controls and monitoring
root.order.add_edge(DataCalibration, PestControl)
root.order.add_edge(DataCalibration, NutrientMix)
root.order.add_edge(DataCalibration, EnergyTracking)

# Post-seeding processes
root.order.add_edge(PlantSeeding, PestControl)
root.order.add_edge(PlantSeeding, NutrientMix)
root.order.add_edge(NutrientMix, WasteRecycling)

# Energy tracking begins after HVAC is in place
root.order.add_edge(ConfigureHVAC, EnergyTracking)

# Harvest planning and community outreach at end
root.order.add_edge(PestControl, HarvestPlanning)
root.order.add_edge(NutrientMix, HarvestPlanning)
root.order.add_edge(HarvestPlanning, CommunityOutreach)