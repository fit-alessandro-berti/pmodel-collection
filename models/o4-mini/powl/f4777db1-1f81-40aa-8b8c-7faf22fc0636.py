# Generated from: f4777db1-1f81-40aa-8b8c-7faf22fc0636.json
# Description: This process outlines the establishment of an urban rooftop farming operation on a commercial building. It includes site analysis, environmental impact assessment, structural integrity checks, soil and hydroponic system design, seed selection, installation of irrigation and lighting systems, implementation of pest control measures, and ongoing monitoring for crop health. The process also incorporates community engagement, compliance with local regulations, waste recycling strategies, and market launch preparations, ensuring a sustainable, productive, and community-supported urban agriculture initiative.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
SiteSurvey       = Transition(label='Site Survey')
ImpactStudy      = Transition(label='Impact Study')
StructureCheck   = Transition(label='Structure Check')
SoilTesting      = Transition(label='Soil Testing')
SystemDesign     = Transition(label='System Design')
SeedSelection    = Transition(label='Seed Selection')
IrrigationSetup  = Transition(label='Irrigation Setup')
LightingInstall  = Transition(label='Lighting Install')
PestControl      = Transition(label='Pest Control')
CommunityMeet    = Transition(label='Community Meet')
RegulationReview = Transition(label='Regulation Review')
WastePlan        = Transition(label='Waste Plan')
CropMonitor      = Transition(label='Crop Monitor')
HarvestPrep      = Transition(label='Harvest Prep')
MarketLaunch     = Transition(label='Market Launch')

# Loop: first monitor, then either exit or do pest control + monitor again
loop = OperatorPOWL(operator=Operator.LOOP, children=[CropMonitor, PestControl])

# Build the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    ImpactStudy,
    StructureCheck,
    SoilTesting,
    SystemDesign,
    SeedSelection,
    IrrigationSetup,
    LightingInstall,
    CommunityMeet,
    RegulationReview,
    WastePlan,
    loop,
    HarvestPrep,
    MarketLaunch
])

# Preliminary sequence
root.order.add_edge(SiteSurvey, StructureCheck)
root.order.add_edge(StructureCheck, SoilTesting)

# Parallel compliance & engagement all must finish before design
root.order.add_edge(ImpactStudy,      SystemDesign)
root.order.add_edge(RegulationReview, SystemDesign)
root.order.add_edge(CommunityMeet,    SystemDesign)
root.order.add_edge(WastePlan,        SystemDesign)

# Design & seed selection
root.order.add_edge(SoilTesting,  SystemDesign)
root.order.add_edge(SystemDesign, SeedSelection)

# Install irrigation & lighting after design/seed selection
root.order.add_edge(SeedSelection,   IrrigationSetup)
root.order.add_edge(SystemDesign,    LightingInstall)

# After installing infrastructure, enter the monitoring/pest‐control loop
root.order.add_edge(IrrigationSetup, loop)
root.order.add_edge(LightingInstall, loop)

# After loop exit, prepare harvest and then launch to market
root.order.add_edge(loop,       HarvestPrep)
root.order.add_edge(HarvestPrep, MarketLaunch)