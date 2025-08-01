# Generated from: c2675bd4-bf9c-424a-b68e-17ced25d8f0a.json
# Description: This process outlines the establishment of a sustainable urban rooftop farm in a dense city environment. It involves site analysis, structural assessments, soil and water testing, regulatory compliance checks, installation of modular planters, irrigation system setup, selection of crop varieties suited for rooftop conditions, pest management strategies, community engagement, ongoing maintenance scheduling, harvest planning, and integration with local markets. The process ensures environmental sustainability, optimizes limited space usage, and fosters urban food security while adhering to safety and zoning regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SiteSurvey = Transition(label='Site Survey')
LoadTest = Transition(label='Load Test')
SoilSample = Transition(label='Soil Sample')
WaterCheck = Transition(label='Water Check')
PermitReview = Transition(label='Permit Review')
PlanterInstall = Transition(label='Planter Install')
IrrigationSetup = Transition(label='Irrigation Setup')
CropSelect = Transition(label='Crop Select')
PestControl = Transition(label='Pest Control')
CommunityMeet = Transition(label='Community Meet')
MaintenancePlan = Transition(label='Maintenance Plan')
HarvestPrep = Transition(label='Harvest Prep')
MarketLink = Transition(label='Market Link')
WasteManage = Transition(label='Waste Manage')
EnergyAudit = Transition(label='Energy Audit')

# Create partial orders for parallel activities that can run concurrently

# Site analysis and assessments
site_assessment = StrictPartialOrder(nodes=[SiteSurvey, LoadTest])
site_assessment.order.add_edge(SiteSurvey, LoadTest)  # Survey before Load Test

# Soil and water testing can run concurrently after load test
soil_water = StrictPartialOrder(nodes=[SoilSample, WaterCheck])
# No edges between SoilSample and WaterCheck => concurrent

# After assessments and tests, regulatory compliance check (Permit Review)
assessments_and_regulations = StrictPartialOrder(nodes=[site_assessment, soil_water, PermitReview])
assessments_and_regulations.order.add_edge(site_assessment, PermitReview)
assessments_and_regulations.order.add_edge(soil_water, PermitReview)

# Installation: Planters and irrigation system setup can run sequentially or parallel?
installation = StrictPartialOrder(nodes=[PlanterInstall, IrrigationSetup])
installation.order.add_edge(PlanterInstall, IrrigationSetup)  # Planter install before irrigation setup

# Crop selection before pest control
crop_and_pest = StrictPartialOrder(nodes=[CropSelect, PestControl])
crop_and_pest.order.add_edge(CropSelect, PestControl)

# Community meeting can be concurrent with pest control and after irrigation setup
community_and_pest = StrictPartialOrder(nodes=[CommunityMeet, PestControl])
# No order edges => concurrent

# Maintenance plan after pest control and community meeting
maintenance_scheduling = StrictPartialOrder(nodes=[community_and_pest, MaintenancePlan])
maintenance_scheduling.order.add_edge(community_and_pest, MaintenancePlan)

# Harvest prep after maintenance plan
harvest_phase = StrictPartialOrder(nodes=[MaintenancePlan, HarvestPrep])
harvest_phase.order.add_edge(MaintenancePlan, HarvestPrep)

# Market linking and waste management can be concurrent after harvest prep
market_waste = StrictPartialOrder(nodes=[MarketLink, WasteManage])
# No edge => concurrent

# Energy audit can be concurrent or independent, put parallel with markets + waste after harvest prep
final_tasks = StrictPartialOrder(nodes=[market_waste, EnergyAudit])
final_tasks.order.add_edge(market_waste, EnergyAudit)  # Consider to happen after market/waste starts

# Build whole workflow partial order
root = StrictPartialOrder(
    nodes=[assessments_and_regulations, installation, crop_and_pest, community_and_pest, maintenance_scheduling, harvest_phase, market_waste, EnergyAudit]
)

# Define order dependencies based on logical flow
# assessments_and_regulations before installation
root.order.add_edge(assessments_and_regulations, installation)
# installation before crop selection and pest control (crop_and_pest and community_and_pest are related)
root.order.add_edge(installation, crop_and_pest)
# pest control also related with community meeting so connect crop_and_pest to community_and_pest with PestControl shared: 
# Instead, to keep the model clean, consider community_and_pest as peers of crop_and_pest, start after installation
root.order.add_edge(installation, community_and_pest)
# crop_and_pest and community_and_pest must precede maintenance
root.order.add_edge(crop_and_pest, maintenance_scheduling)
root.order.add_edge(community_and_pest, maintenance_scheduling)
# maintenance before harvest
root.order.add_edge(maintenance_scheduling, harvest_phase)
# harvest before market and waste management (market_waste)
root.order.add_edge(harvest_phase, market_waste)
# energy audit concurrent or after market_waste start (already ordered in final_tasks)
root.order.add_edge(market_waste, EnergyAudit)