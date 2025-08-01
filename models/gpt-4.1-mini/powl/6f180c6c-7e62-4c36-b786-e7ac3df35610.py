# Generated from: 6f180c6c-7e62-4c36-b786-e7ac3df35610.json
# Description: This process outlines the complex steps involved in establishing an urban rooftop farm on a commercial building. It includes initial site assessment considering structural integrity and sunlight exposure, securing permits from local authorities, sourcing sustainable soil and seeds, installing efficient irrigation systems, and integrating automated climate controls. Additionally, it involves community engagement for education and volunteer programs, ongoing pest management with eco-friendly methods, crop rotation planning to maintain soil health, and establishing partnerships with local markets for produce distribution. Finally, the process covers regular yield monitoring, data collection for optimization, and scaling strategies for expansion to additional rooftops in urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SiteAssess = Transition(label='Site Assess')
PermitAcquire = Transition(label='Permit Acquire')
SoilSource = Transition(label='Soil Source')
SeedSelect = Transition(label='Seed Select')
IrrigationInstall = Transition(label='Irrigation Install')
ClimateSetup = Transition(label='Climate Setup')
VolunteerRecruit = Transition(label='Volunteer Recruit')
CommunityMeet = Transition(label='Community Meet')
PestControl = Transition(label='Pest Control')
CropRotate = Transition(label='Crop Rotate')
MarketPartner = Transition(label='Market Partner')
YieldMonitor = Transition(label='Yield Monitor')
DataCollect = Transition(label='Data Collect')
OptimizePlan = Transition(label='Optimize Plan')
ScaleExpand = Transition(label='Scale Expand')

# Group the initial assessment steps in partial order (Site Assess then Permit Acquire)
init_assessment = StrictPartialOrder(nodes=[SiteAssess, PermitAcquire])
init_assessment.order.add_edge(SiteAssess, PermitAcquire)

# Soil and seed sourcing can be concurrent
soil_seed = StrictPartialOrder(nodes=[SoilSource, SeedSelect])
# no edges => concurrent

# Irrigation Install and Climate Setup can be parallel (both needed before next phase)
installations = StrictPartialOrder(nodes=[IrrigationInstall, ClimateSetup])
# no edges => concurrent

# Community engagement phase: recruit volunteers then community meeting
community_engagement = StrictPartialOrder(nodes=[VolunteerRecruit, CommunityMeet])
community_engagement.order.add_edge(VolunteerRecruit, CommunityMeet)

# Pest control and crop rotation are ongoing / repeated tasks — model as loop
# Loop body: PestControl then CropRotate
loop_body = StrictPartialOrder(nodes=[PestControl, CropRotate])
loop_body.order.add_edge(PestControl, CropRotate)

pest_crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, SilentTransition()]) 
# Note: per definition LOOP(A,B): execute A, then either exit or B then A again.
# Using SilentTransition as second child means optional looping after A

# Market partner setup after pest/crop loop
# Model pest_crop_loop then MarketPartner
market_phase = StrictPartialOrder(nodes=[pest_crop_loop, MarketPartner])
market_phase.order.add_edge(pest_crop_loop, MarketPartner)

# Monitoring phase: yield monitor -> data collect -> optimize plan (sequence)
monitoring = StrictPartialOrder(nodes=[YieldMonitor, DataCollect, OptimizePlan])
monitoring.order.add_edge(YieldMonitor, DataCollect)
monitoring.order.add_edge(DataCollect, OptimizePlan)

# Final scaling phase occurs after monitoring
final_phase = StrictPartialOrder(nodes=[monitoring, ScaleExpand])
final_phase.order.add_edge(monitoring, ScaleExpand)

# Combine all main phases in order:
# init_assessment -> soil_seed -> installations -> community_engagement -> market_phase -> final_phase
root = StrictPartialOrder(
    nodes=[init_assessment, soil_seed, installations, community_engagement, market_phase, final_phase]
)
root.order.add_edge(init_assessment, soil_seed)
root.order.add_edge(soil_seed, installations)
root.order.add_edge(installations, community_engagement)
root.order.add_edge(community_engagement, market_phase)
root.order.add_edge(market_phase, final_phase)