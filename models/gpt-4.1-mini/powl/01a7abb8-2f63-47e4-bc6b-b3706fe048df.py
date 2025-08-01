# Generated from: 01a7abb8-2f63-47e4-bc6b-b3706fe048df.json
# Description: This process outlines the comprehensive steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It includes site assessment for structural integrity and sunlight access, modular system design for hydroponics and aeroponics integration, procurement of specialized equipment, installation of climate control and nutrient delivery systems, staff training on innovative cultivation techniques, implementation of IoT sensors for real-time monitoring, compliance with local agricultural regulations, iterative crop testing to optimize yield, marketing strategies for urban produce distribution, and continuous sustainability assessments to reduce energy and water consumption. The process demands coordination between architects, agronomists, engineers, and business strategists to ensure a profitable and eco-friendly farming solution in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SiteSurvey = Transition(label='Site Survey')
StructuralCheck = Transition(label='Structural Check')
LightMapping = Transition(label='Light Mapping')
SystemDesign = Transition(label='System Design')
EquipmentOrder = Transition(label='Equipment Order')
ClimateSetup = Transition(label='Climate Setup')
NutrientMix = Transition(label='Nutrient Mix')
SensorInstall = Transition(label='Sensor Install')
StaffTraining = Transition(label='Staff Training')
RegulationReview = Transition(label='Regulation Review')
CropTesting = Transition(label='Crop Testing')
YieldAnalysis = Transition(label='Yield Analysis')
MarketOutreach = Transition(label='Market Outreach')
EnergyAudit = Transition(label='Energy Audit')
WaterRecycling = Transition(label='Water Recycling')
DataMonitoring = Transition(label='Data Monitoring')
FeedbackLoop = Transition(label='Feedback Loop')

# Site assessment as partial order of Structural Check and Light Mapping after Site Survey
site_assessment = StrictPartialOrder(nodes=[SiteSurvey, StructuralCheck, LightMapping])
site_assessment.order.add_edge(SiteSurvey, StructuralCheck)
site_assessment.order.add_edge(SiteSurvey, LightMapping)

# Modular system design after site assessment
modular_design = StrictPartialOrder(nodes=[site_assessment, SystemDesign])
modular_design.order.add_edge(site_assessment, SystemDesign)

# Procurement and installation in parallel (Equipment Order and installation steps)
installation = StrictPartialOrder(nodes=[ClimateSetup, NutrientMix, SensorInstall])
# These three (ClimateSetup, NutrientMix, SensorInstall) can be concurrent

procurement_installation = StrictPartialOrder(nodes=[EquipmentOrder, installation])
procurement_installation.order.add_edge(EquipmentOrder, installation)

# Staff training and regulation review after procurement and installation
staff_reg_review = StrictPartialOrder(nodes=[StaffTraining, RegulationReview])
# StaffTraining and RegulationReview can be concurrent

post_procurement = StrictPartialOrder(nodes=[procurement_installation, staff_reg_review])
post_procurement.order.add_edge(procurement_installation, staff_reg_review)

# Crop testing and yield analysis, yield analysis after crop testing
crop_test_yield = StrictPartialOrder(nodes=[CropTesting, YieldAnalysis])
crop_test_yield.order.add_edge(CropTesting, YieldAnalysis)

# Market outreach after yield analysis
market = StrictPartialOrder(nodes=[YieldAnalysis, MarketOutreach])
market.order.add_edge(YieldAnalysis, MarketOutreach)

# Sustainability assessments in parallel: Energy Audit and Water Recycling
sustainability = StrictPartialOrder(nodes=[EnergyAudit, WaterRecycling])
# no order between energy and water audits - concurrent

# Data Monitoring and Feedback Loop modeled as a loop: monitor data then feedback
data_monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[DataMonitoring, FeedbackLoop]
)

# Compose sustainability and monitoring loops
sustain_monitor = StrictPartialOrder(nodes=[sustainability, data_monitor_loop])
# Sustainability assessments and the monitoring loop run concurrently (no order edges)

# Final overall process as partial order:
# site assessment -> modular system design -> procurement & installation -> post procurement ->
# crop test & yield -> market outreach -> sustainability & monitoring loop

root = StrictPartialOrder(
    nodes=[
        site_assessment,
        modular_design,
        procurement_installation,
        post_procurement,
        crop_test_yield,
        market,
        sustain_monitor,
    ]
)

root.order.add_edge(site_assessment, modular_design)
root.order.add_edge(modular_design, procurement_installation)
root.order.add_edge(procurement_installation, post_procurement)
root.order.add_edge(post_procurement, crop_test_yield)
root.order.add_edge(crop_test_yield, market)
root.order.add_edge(market, sustain_monitor)