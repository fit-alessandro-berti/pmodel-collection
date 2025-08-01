# Generated from: 42de4269-da18-4ed4-91b4-770bbc470b42.json
# Description: This process outlines the complex and multifaceted approach to establishing a vertical farming operation in an urban environment. It involves site selection based on sunlight and infrastructure availability, modular farm design to maximize space efficiency, integration of IoT sensors for real-time monitoring, automated nutrient delivery systems, climate control calibration, regulatory compliance checks including zoning and agricultural permits, staff training on hydroponic systems, implementation of AI-driven crop health analysis, waste recycling protocols, marketing strategy development targeting local consumers, and continuous performance optimization through data analytics. This atypical business process combines agriculture, technology, urban planning, and sustainability to create a scalable and efficient urban farm that meets the demand for fresh produce within city limits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey   = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
SensorInstall= Transition(label='Sensor Install')
NutrientMix  = Transition(label='Nutrient Mix')
ClimateTune  = Transition(label='Climate Tune')
PermitReview = Transition(label='Permit Review')
StaffOnboard = Transition(label='Staff Onboard')
AITraining   = Transition(label='AI Training')
CropMonitor  = Transition(label='Crop Monitor')
WasteSetup   = Transition(label='Waste Setup')
MarketPlan   = Transition(label='Market Plan')
DataReview   = Transition(label='Data Review')
HarvestPlan  = Transition(label='Harvest Plan')
SupplyChain  = Transition(label='Supply Chain')
FeedbackLoop = Transition(label='Feedback Loop')

# Loop: after DataReview optionally perform FeedbackLoop then DataReview again
loop = OperatorPOWL(operator=Operator.LOOP, children=[DataReview, FeedbackLoop])

# Build partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey, DesignLayout, SensorInstall, NutrientMix, ClimateTune,
    PermitReview, StaffOnboard, AITraining, CropMonitor, WasteSetup,
    MarketPlan, HarvestPlan, SupplyChain, loop
])

# Define ordering relations
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(SiteSurvey, PermitReview)

root.order.add_edge(DesignLayout, SensorInstall)
root.order.add_edge(DesignLayout, NutrientMix)
root.order.add_edge(DesignLayout, ClimateTune)
root.order.add_edge(DesignLayout, WasteSetup)
root.order.add_edge(DesignLayout, MarketPlan)

root.order.add_edge(PermitReview, StaffOnboard)
root.order.add_edge(PermitReview, MarketPlan)

root.order.add_edge(StaffOnboard, AITraining)
root.order.add_edge(AITraining, CropMonitor)
root.order.add_edge(SensorInstall, CropMonitor)

root.order.add_edge(NutrientMix, HarvestPlan)
root.order.add_edge(ClimateTune, HarvestPlan)
root.order.add_edge(CropMonitor, HarvestPlan)

root.order.add_edge(HarvestPlan, SupplyChain)
root.order.add_edge(SupplyChain, loop)  # enter the performance optimization loop