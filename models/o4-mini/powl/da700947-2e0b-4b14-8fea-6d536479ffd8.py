# Generated from: da700947-2e0b-4b14-8fea-6d536479ffd8.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a repurposed industrial building. It encompasses site evaluation, environmental control system design, modular planting setup, nutrient delivery automation, pest monitoring with AI integration, energy optimization through renewable sources, and yield forecasting using data analytics. The process also includes community engagement programs, regulatory compliance checks, staff training on specialized equipment, and continuous improvement loops based on sensor feedback. This atypical yet realistic sequence enables sustainable, high-density crop production in urban environments, reducing transportation emissions and supporting local food systems.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
SiteSurvey       = Transition(label='Site Survey')
StructuralAudit  = Transition(label='Structural Audit')
ClimateDesign    = Transition(label='Climate Design')
LightingSetup    = Transition(label='Lighting Setup')
IrrigationPlan   = Transition(label='Irrigation Plan')
NutrientMix      = Transition(label='Nutrient Mix')
SensorInstall    = Transition(label='Sensor Install')
AICalibration    = Transition(label='AI Calibration')
PestScan         = Transition(label='Pest Scan')
EnergyAudit      = Transition(label='Energy Audit')
RenewableSync    = Transition(label='Renewable Sync')
StaffBriefing    = Transition(label='Staff Briefing')
ComplianceCheck  = Transition(label='Compliance Check')
CommunityMeet    = Transition(label='Community Meet')
# These three belong inside the improvement loop
DataModeling     = Transition(label='Data Modeling')
YieldReview      = Transition(label='Yield Review')
FeedbackLoop     = Transition(label='Feedback Loop')

# Build the loop subprocess: A = DataModeling->YieldReview; B = FeedbackLoop
loop_body = StrictPartialOrder(
    nodes=[DataModeling, YieldReview]
)
loop_body.order.add_edge(DataModeling, YieldReview)
# The LOOP operator: first run loop_body, then either exit or run FeedbackLoop and repeat
improvement_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[loop_body, FeedbackLoop]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey, StructuralAudit,
    ClimateDesign, LightingSetup, IrrigationPlan, NutrientMix,
    SensorInstall, AICalibration, PestScan,
    EnergyAudit, RenewableSync,
    StaffBriefing, ComplianceCheck, CommunityMeet,
    improvement_loop
])

# Sequential site setup
root.order.add_edge(SiteSurvey,      StructuralAudit)
root.order.add_edge(StructuralAudit, ClimateDesign)
root.order.add_edge(ClimateDesign,   LightingSetup)
root.order.add_edge(LightingSetup,   IrrigationPlan)
root.order.add_edge(IrrigationPlan,  NutrientMix)

# After nutrient mix, launch parallel branches + reviews/training/compliance/community
for nxt in [SensorInstall, EnergyAudit, StaffBriefing, ComplianceCheck, CommunityMeet]:
    root.order.add_edge(NutrientMix, nxt)

# Sensor → AI → Pest → join
root.order.add_edge(SensorInstall, AICalibration)
root.order.add_edge(AICalibration, PestScan)
root.order.add_edge(PestScan,      improvement_loop)

# Energy → Renewable → join
root.order.add_edge(EnergyAudit,   RenewableSync)
root.order.add_edge(RenewableSync, improvement_loop)

# Training, compliance, community all join into the improvement loop
root.order.add_edge(StaffBriefing,   improvement_loop)
root.order.add_edge(ComplianceCheck, improvement_loop)
root.order.add_edge(CommunityMeet,   improvement_loop)

# The root POWL model is now in 'root'