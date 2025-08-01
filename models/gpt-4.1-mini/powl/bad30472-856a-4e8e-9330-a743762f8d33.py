# Generated from: bad30472-856a-4e8e-9330-a743762f8d33.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It includes site assessment, modular system design, nutrient cycling integration, climate control calibration, automated seeding, continuous environmental monitoring, pest bio-control application, energy consumption optimization, waste recycling protocols, data-driven yield forecasting, community engagement for local produce distribution, regulatory compliance verification, and adaptive scaling strategies to maximize sustainable food production in dense urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteAssess = Transition(label='Site Assess')
DesignModules = Transition(label='Design Modules')
InstallSystems = Transition(label='Install Systems')
CalibrateClimate = Transition(label='Calibrate Climate')
SeedAutomation = Transition(label='Seed Automation')
MonitorSensors = Transition(label='Monitor Sensors')
ApplyBiocontrols = Transition(label='Apply Biocontrols')
OptimizeEnergy = Transition(label='Optimize Energy')
RecycleWaste = Transition(label='Recycle Waste')
ForecastYield = Transition(label='Forecast Yield')
EngageCommunity = Transition(label='Engage Community')
VerifyCompliance = Transition(label='Verify Compliance')
ScaleOperations = Transition(label='Scale Operations')
TrainStaff = Transition(label='Train Staff')
ReportMetrics = Transition(label='Report Metrics')

# Define the main (strict) partial order reflecting a logical linear sequence with environment monitoring and control steps happen concurrent after automation:

# After Design and Install: Calibrate climate must happen before Seed Automation
# Seed Automation followed by concurrent Monitor Sensors and Apply Biocontrols
# After monitoring and biocontrol, then Optimize Energy and Recycle Waste concurrently
# Then Forecast Yield and Engage Community concurrently
# Then Verify Compliance 
# Then Scale Operations, Train Staff and Report Metrics sequentially

# Let's model the parts with concurrency by placing nodes without order relations between them.

root = StrictPartialOrder(nodes=[
    SiteAssess,
    DesignModules,
    InstallSystems,
    CalibrateClimate,
    SeedAutomation,
    MonitorSensors,
    ApplyBiocontrols,
    OptimizeEnergy,
    RecycleWaste,
    ForecastYield,
    EngageCommunity,
    VerifyCompliance,
    ScaleOperations,
    TrainStaff,
    ReportMetrics
])

# Add order edges according to described logical flow

root.order.add_edge(SiteAssess, DesignModules)
root.order.add_edge(DesignModules, InstallSystems)
root.order.add_edge(InstallSystems, CalibrateClimate)
root.order.add_edge(CalibrateClimate, SeedAutomation)
root.order.add_edge(SeedAutomation, MonitorSensors)
root.order.add_edge(SeedAutomation, ApplyBiocontrols)
# Monitor Sensors and Apply Biocontrols are concurrent, no order between them

root.order.add_edge(MonitorSensors, OptimizeEnergy)
root.order.add_edge(ApplyBiocontrols, OptimizeEnergy)

root.order.add_edge(MonitorSensors, RecycleWaste)
root.order.add_edge(ApplyBiocontrols, RecycleWaste)
# OptimizeEnergy and RecycleWaste concurrent, no order between them

root.order.add_edge(OptimizeEnergy, ForecastYield)
root.order.add_edge(RecycleWaste, ForecastYield)

root.order.add_edge(OptimizeEnergy, EngageCommunity)
root.order.add_edge(RecycleWaste, EngageCommunity)
# ForecastYield and EngageCommunity concurrent, no order between them

root.order.add_edge(ForecastYield, VerifyCompliance)
root.order.add_edge(EngageCommunity, VerifyCompliance)

root.order.add_edge(VerifyCompliance, ScaleOperations)
root.order.add_edge(ScaleOperations, TrainStaff)
root.order.add_edge(TrainStaff, ReportMetrics)