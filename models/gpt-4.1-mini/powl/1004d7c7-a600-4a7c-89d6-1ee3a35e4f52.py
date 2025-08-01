# Generated from: 1004d7c7-a600-4a7c-89d6-1ee3a35e4f52.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a repurposed commercial building. It includes assessing structural integrity, designing modular growing units, integrating IoT sensors for climate control, selecting crop varieties optimized for vertical growth, installing hydroponic systems, and implementing automated nutrient delivery. The process further involves regulatory compliance checks, staff training on specialized farming techniques, continuous environmental monitoring, and establishing supply chain logistics for fresh produce distribution to local markets. Emphasis is placed on sustainability and energy efficiency throughout the setup.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
StructuralCheck = Transition(label='Structural Check')
DesignLayout = Transition(label='Design Layout')
CropSelection = Transition(label='Crop Selection')
SensorSetup = Transition(label='Sensor Setup')
HydroponicsInstall = Transition(label='Hydroponics Install')
NutrientMix = Transition(label='Nutrient Mix')
ClimateControl = Transition(label='Climate Control')
ComplianceReview = Transition(label='Compliance Review')
StaffTraining = Transition(label='Staff Training')
SystemTesting = Transition(label='System Testing')
DataIntegration = Transition(label='Data Integration')
HarvestPlanning = Transition(label='Harvest Planning')
PackagingSetup = Transition(label='Packaging Setup')
LogisticsSetup = Transition(label='Logistics Setup')
MarketLaunch = Transition(label='Market Launch')

# Step 1: Site Survey then Structural Check
step1 = StrictPartialOrder(nodes=[SiteSurvey, StructuralCheck])
step1.order.add_edge(SiteSurvey, StructuralCheck)

# Step 2: Design Layout, Crop Selection, Sensor Setup (concurrent after Structural Check)
step2 = StrictPartialOrder(nodes=[DesignLayout, CropSelection, SensorSetup])
# No order edges among them - fully concurrent

# Step 3: Hydroponics Install and Nutrient Mix and Climate Control (after step 2)
step3 = StrictPartialOrder(nodes=[HydroponicsInstall, NutrientMix, ClimateControl])
# No order edges, concurrent

# Step 4: Compliance Review (after step 3)
step4 = StrictPartialOrder(nodes=[ComplianceReview])

# Step 5: Staff Training and System Testing (concurrent after Compliance Review)
step5 = StrictPartialOrder(nodes=[StaffTraining, SystemTesting])
# No order edges, concurrent

# Step 6: Data Integration (after Staff Training and System Testing)
step6 = StrictPartialOrder(nodes=[DataIntegration])
# DataIntegration after step5 nodes

# Step 7: Harvest Planning, Packaging Setup, Logistics Setup (concurrent after Data Integration)
step7 = StrictPartialOrder(nodes=[HarvestPlanning, PackagingSetup, LogisticsSetup])
# No order edges, concurrent

# Step 8: Market Launch (after step7)
step8 = StrictPartialOrder(nodes=[MarketLaunch])

# Compose the overall model by connecting the steps in order
root = StrictPartialOrder(
    nodes=[
        step1,
        step2,
        step3,
        step4,
        step5,
        step6,
        step7,
        step8
    ]
)

# Define order edges between steps
# step1 --> step2
root.order.add_edge(step1, step2)
# step2 --> step3
root.order.add_edge(step2, step3)
# step3 --> step4
root.order.add_edge(step3, step4)
# step4 --> step5
root.order.add_edge(step4, step5)
# step5 --> step6
root.order.add_edge(step5, step6)
# step6 --> step7
root.order.add_edge(step6, step7)
# step7 --> step8
root.order.add_edge(step7, step8)