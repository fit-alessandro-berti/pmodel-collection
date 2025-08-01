# Generated from: edc25dac-0fd5-4f0e-93b6-1b68e8f438b9.json
# Description: This process outlines the establishment of an urban rooftop farm on a commercial building, involving unique steps such as structural load assessment, soil-less medium installation, microclimate analysis, and automated irrigation programming. It integrates multiple disciplines including architecture, agriculture, and environmental engineering to ensure sustainable food production in a limited urban space. The process also includes community engagement for local sourcing and education, regulatory compliance with city zoning laws, and the implementation of renewable energy systems to minimize environmental impact. Continuous monitoring and adaptive management ensure optimal crop yield while maintaining building integrity and tenant satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
LoadAssess       = Transition(label='Load Assess')
PermitReview     = Transition(label='Permit Review')
SiteSurvey       = Transition(label='Site Survey')
DesignLayout     = Transition(label='Design Layout')
SoilMix          = Transition(label='Soil Mix')
InstallBeds      = Transition(label='Install Beds')
IrrigationSet    = Transition(label='Irrigation Set')
SensorDeploy     = Transition(label='Sensor Deploy')
EnergySetup      = Transition(label='Energy Setup')
CropSelect       = Transition(label='Crop Select')
PlantSeeding     = Transition(label='Plant Seeding')
CommunityMeet    = Transition(label='Community Meet')
ComplianceCheck  = Transition(label='Compliance Check')
GrowthMonitor    = Transition(label='Growth Monitor')
ClimateTest      = Transition(label='Climate Test')
HarvestPlan      = Transition(label='Harvest Plan')
WasteRecycle     = Transition(label='Waste Recycle')

# Model the continuous monitoring loop:
#   do GrowthMonitor,
#   then either exit or do ClimateTest and repeat
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[GrowthMonitor, ClimateTest]
)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    LoadAssess,
    PermitReview,
    SiteSurvey,
    CommunityMeet,
    ComplianceCheck,
    DesignLayout,
    SoilMix,
    InstallBeds,
    SensorDeploy,
    IrrigationSet,
    EnergySetup,
    CropSelect,
    PlantSeeding,
    monitor_loop,
    HarvestPlan,
    WasteRecycle
])

# Add ordering constraints
o = root.order
o.add_edge(LoadAssess, SiteSurvey)
o.add_edge(LoadAssess, PermitReview)

o.add_edge(SiteSurvey, CommunityMeet)
o.add_edge(SiteSurvey, DesignLayout)
o.add_edge(CommunityMeet, DesignLayout)

o.add_edge(PermitReview, ComplianceCheck)
o.add_edge(ComplianceCheck, DesignLayout)

o.add_edge(DesignLayout, SoilMix)
o.add_edge(SoilMix, InstallBeds)

o.add_edge(InstallBeds, SensorDeploy)
o.add_edge(InstallBeds, IrrigationSet)
o.add_edge(InstallBeds, EnergySetup)

o.add_edge(DesignLayout, CropSelect)
o.add_edge(CropSelect, PlantSeeding)

# Feed into the monitoring loop
o.add_edge(PlantSeeding, monitor_loop)
o.add_edge(SensorDeploy, monitor_loop)
o.add_edge(IrrigationSet, monitor_loop)
o.add_edge(EnergySetup, monitor_loop)

o.add_edge(monitor_loop, HarvestPlan)
o.add_edge(HarvestPlan, WasteRecycle)