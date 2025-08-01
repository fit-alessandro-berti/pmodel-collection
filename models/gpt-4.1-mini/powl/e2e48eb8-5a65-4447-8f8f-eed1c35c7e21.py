# Generated from: e2e48eb8-5a65-4447-8f8f-eed1c35c7e21.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm in a densely populated city. It includes site analysis, structural assessment, microclimate evaluation, soil preparation with hydroponic integration, seed selection tailored to urban conditions, installation of automated irrigation and nutrient delivery systems, pest monitoring using AI-driven sensors, community engagement for resource sharing, regulatory compliance checks, and the establishment of a local distribution network for produce. The process ensures optimization of limited space, maximizes yield through technology, and fosters urban food security by integrating environmental, technical, and social considerations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
SiteSurvey = Transition(label='Site Survey')
StructuralCheck = Transition(label='Structural Check')
ClimateStudy = Transition(label='Climate Study')

SoilPrep = Transition(label='Soil Prep')
SeedSelection = Transition(label='Seed Selection')

IrrigationSetup = Transition(label='Irrigation Setup')
NutrientMix = Transition(label='Nutrient Mix')

SensorInstall = Transition(label='Sensor Install')
PestMonitor = Transition(label='Pest Monitor')
DataAnalysis = Transition(label='Data Analysis')

RegulationReview = Transition(label='Regulation Review')
CommunityMeet = Transition(label='Community Meet')

HarvestPlan = Transition(label='Harvest Plan')
PackagingDesign = Transition(label='Packaging Design')
DistributionMap = Transition(label='Distribution Map')

FeedbackLoop = Transition(label='Feedback Loop')
MaintenanceSchedule = Transition(label='Maintenance Schedule')

# Start with PO for initial analysis: Site Survey --> Structural Check and Climate Study can run concurrently after Structural Check
initial_po = StrictPartialOrder(nodes=[SiteSurvey, StructuralCheck, ClimateStudy])
initial_po.order.add_edge(SiteSurvey, StructuralCheck)
initial_po.order.add_edge(StructuralCheck, ClimateStudy)

# Soil preparation and seed selection sequential
soil_seed_po = StrictPartialOrder(nodes=[SoilPrep, SeedSelection])
soil_seed_po.order.add_edge(SoilPrep, SeedSelection)

# Irrigation and nutrient mix are parallel (hydroponic integration)
irrig_nutrient_po = StrictPartialOrder(nodes=[IrrigationSetup, NutrientMix])

# Pest monitoring branch:
# Sensor install -> Pest monitor -> Data analysis
pest_po = StrictPartialOrder(nodes=[SensorInstall, PestMonitor, DataAnalysis])
pest_po.order.add_edge(SensorInstall, PestMonitor)
pest_po.order.add_edge(PestMonitor, DataAnalysis)

# Community meet and regulation review in parallel
comm_reg_po = StrictPartialOrder(nodes=[CommunityMeet, RegulationReview])

# Harvest plan -> packaging design -> distribution map sequential
harvest_po = StrictPartialOrder(nodes=[HarvestPlan, PackagingDesign, DistributionMap])
harvest_po.order.add_edge(HarvestPlan, PackagingDesign)
harvest_po.order.add_edge(PackagingDesign, DistributionMap)

# Feedback loop and maintenance schedule form a LOOP:
# loop(children=[Activity to do, activity to repeat])
# Here, FeedbackLoop followed by MaintenanceSchedule can be repeated after distribution
loop = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackLoop, MaintenanceSchedule])

# Now combine all major parts into a big PO:
# Initial analysis --> soil and seed --> irrigation & nutrient (parallel) and pest monitoring (start pest after irrigation & nutrient done)
# pest monitoring runs after irrigation & nutrient, community & regulation parallel after pest monitoring
# then harvest plan -> packaging -> distribution -> loop

# Combine irrigation_nutrient and pest monitoring in sequence (pest after irrigation & nutrient)
irrig_nutrient_pest_po = StrictPartialOrder(nodes=[irrig_nutrient_po, pest_po])
irrig_nutrient_pest_po.order.add_edge(irrig_nutrient_po, pest_po)

# Combine community & regulation in parallel
# Already defined as comm_reg_po

# Combine harvest followed by loop (feedback)
harvest_loop_po = StrictPartialOrder(nodes=[harvest_po, loop])
harvest_loop_po.order.add_edge(harvest_po, loop)

# Now all big nodes: initial_po -> soil_seed_po -> irrig_nutrient_pest_po -> comm_reg_po -> harvest_loop_po

root = StrictPartialOrder(nodes=[initial_po, soil_seed_po, irrig_nutrient_pest_po, comm_reg_po, harvest_loop_po])
root.order.add_edge(initial_po, soil_seed_po)
root.order.add_edge(soil_seed_po, irrig_nutrient_pest_po)
root.order.add_edge(irrig_nutrient_pest_po, comm_reg_po)
root.order.add_edge(comm_reg_po, harvest_loop_po)