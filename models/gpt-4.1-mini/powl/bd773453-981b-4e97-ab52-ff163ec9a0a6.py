# Generated from: bd773453-981b-4e97-ab52-ff163ec9a0a6.json
# Description: This process outlines the complex and multifaceted steps involved in establishing a sustainable urban rooftop farm. It includes site assessment, structural analysis, soil preparation, microclimate evaluation, and installation of automated irrigation systems. The process also integrates community engagement, local regulatory compliance, crop selection based on seasonal data, and ongoing monitoring for pest control and yield optimization. Additionally, it incorporates waste recycling from the farm into compost, energy management through solar panels, and distribution logistics to local markets. The process ensures environmental sustainability while maximizing crop productivity in an unconventional urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
LoadTest = Transition(label='Load Test')
SoilPrep = Transition(label='Soil Prep')
MicroclimateMap = Transition(label='Microclimate Map')
IrrigationSetup = Transition(label='Irrigation Setup')

PermitCheck = Transition(label='Permit Check')
CropPlan = Transition(label='Crop Plan')
CommunityMeet = Transition(label='Community Meet')

CompostBuild = Transition(label='Compost Build')
WasteCycle = Transition(label='Waste Cycle')

PestMonitor = Transition(label='Pest Monitor')
YieldReview = Transition(label='Yield Review')
DataLogging = Transition(label='Data Logging')

SolarInstall = Transition(label='Solar Install')
EnergyAudit = Transition(label='Energy Audit')

MarketLink = Transition(label='Market Link')

# Subprocess: Site assessment and preparation
# Site Survey then Load Test then Soil Prep & Microclimate Map & Irrigation Setup in parallel
site_assessment_prep = StrictPartialOrder(
    nodes=[SiteSurvey, LoadTest, SoilPrep, MicroclimateMap, IrrigationSetup]
)
site_assessment_prep.order.add_edge(SiteSurvey, LoadTest)
site_assessment_prep.order.add_edge(LoadTest, SoilPrep)
site_assessment_prep.order.add_edge(LoadTest, MicroclimateMap)
site_assessment_prep.order.add_edge(LoadTest, IrrigationSetup)
# SoilPrep, MicroclimateMap, IrrigationSetup concurrent after LoadTest

# Subprocess: Community and regulatory
# Permit Check and Community Meet concurrent, both must complete before Crop Plan
comm_reg = StrictPartialOrder(
    nodes=[PermitCheck, CommunityMeet, CropPlan]
)
# Permit Check and Community Meet are concurrent (no edges)
comm_reg.order.add_edge(PermitCheck, CropPlan)
comm_reg.order.add_edge(CommunityMeet, CropPlan)

# Subprocess: Waste and compost loop (simulate ongoing compost and waste cycling)
# Waste Cycle leads to Compost Build, modeled as a loop: * (Compost Build, Waste Cycle)
waste_compost_loop = OperatorPOWL(operator=Operator.LOOP, children=[CompostBuild, WasteCycle])

# Subprocess: Monitoring loop
# Pest Monitor followed by Yield Review and Data Logging looped to Pest Monitor again
monitoring_loop_body = StrictPartialOrder(
    nodes=[YieldReview, DataLogging]
)
monitoring_loop_body.order.add_edge(YieldReview, DataLogging)
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[PestMonitor, monitoring_loop_body])

# Subprocess: Energy management
# Solar Install before Energy Audit
energy_mgmt = StrictPartialOrder(
    nodes=[SolarInstall, EnergyAudit]
)
energy_mgmt.order.add_edge(SolarInstall, EnergyAudit)

# Now combine all subprocesses before final Market Link (distribution logistics)
root = StrictPartialOrder(
    nodes=[
        site_assessment_prep,
        comm_reg,
        waste_compost_loop,
        monitoring_loop,
        energy_mgmt,
        MarketLink
    ]
)

# Add edges for partial order:
# site_assessment_prep and comm_reg must complete before market link
root.order.add_edge(site_assessment_prep, MarketLink)
root.order.add_edge(comm_reg, MarketLink)
root.order.add_edge(waste_compost_loop, MarketLink)
root.order.add_edge(monitoring_loop, MarketLink)
root.order.add_edge(energy_mgmt, MarketLink)