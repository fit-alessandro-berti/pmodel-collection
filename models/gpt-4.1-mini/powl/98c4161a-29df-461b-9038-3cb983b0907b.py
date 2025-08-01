# Generated from: 98c4161a-29df-461b-9038-3cb983b0907b.json
# Description: This process describes the onboarding and setup of an urban vertical farming operation within a repurposed commercial building. It involves multi-disciplinary coordination including site analysis, environmental control calibration, crop selection tailored to micro-climates, integration of IoT sensors for real-time monitoring, and staff training on automated nutrient delivery systems. The process also covers regulatory compliance checks, sustainability assessments, and market launch strategy to ensure the farm meets local food demand efficiently while minimizing resource consumption and environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
SiteSurvey = Transition(label='Site Survey')
StructuralAudit = Transition(label='Structural Audit')
ClimateMapping = Transition(label='Climate Mapping')
CropSelection = Transition(label='Crop Selection')
SensorInstall = Transition(label='Sensor Install')
SystemCalibrate = Transition(label='System Calibrate')
NutrientSetup = Transition(label='Nutrient Setup')
WaterTesting = Transition(label='Water Testing')
StaffTraining = Transition(label='Staff Training')
ComplianceCheck = Transition(label='Compliance Check')
EnergyAudit = Transition(label='Energy Audit')
WastePlan = Transition(label='Waste Plan')
DataIntegration = Transition(label='Data Integration')
MarketResearch = Transition(label='Market Research')
LaunchPlanning = Transition(label='Launch Planning')

# Phase 1: Site Prep and Analysis - Site Survey --> Structural Audit --> Climate Mapping
phase1 = StrictPartialOrder(nodes=[SiteSurvey, StructuralAudit, ClimateMapping])
phase1.order.add_edge(SiteSurvey, StructuralAudit)
phase1.order.add_edge(StructuralAudit, ClimateMapping)

# Phase 2: Crop and System Setup - Crop Selection, Sensor Install, System Calibrate, Nutrient Setup, Water Testing in partial order:
# Crop Selection before Sensor Install and Nutrient Setup;
# Sensor Install before System Calibrate;
# Nutrient Setup before Water Testing
phase2 = StrictPartialOrder(nodes=[CropSelection, SensorInstall, SystemCalibrate, NutrientSetup, WaterTesting])
phase2.order.add_edge(CropSelection, SensorInstall)
phase2.order.add_edge(SensorInstall, SystemCalibrate)
phase2.order.add_edge(CropSelection, NutrientSetup)
phase2.order.add_edge(NutrientSetup, WaterTesting)

# Phase 3: Training and Compliance with possible concurrency between Staff Training and ComplianceCheck followed by Energy Audit and Waste Plan
training_compliance = StrictPartialOrder(nodes=[StaffTraining, ComplianceCheck])
# no edges: concurrent

energy_waste = StrictPartialOrder(nodes=[EnergyAudit, WastePlan])
energy_waste.order.add_edge(EnergyAudit, WastePlan)

phase3 = StrictPartialOrder(nodes=[training_compliance, energy_waste])
phase3.order.add_edge(training_compliance, energy_waste)

# Phase 4: Data Integration (after phase2 and phase3)
# So DataIntegration depends on phase2 and phase3
phase4 = DataIntegration

# Phase 5: Market Research then Launch Planning
phase5 = StrictPartialOrder(nodes=[MarketResearch, LaunchPlanning])
phase5.order.add_edge(MarketResearch, LaunchPlanning)

# Order between phases:
# phase1 --> phase2 & phase3 (concurrent)
# phase2 and phase3 --> phase4
# phase4 --> phase5

# Combine phase2 and phase3 as concurrent nodes
phase2_3 = StrictPartialOrder(nodes=[phase2, phase3])

# Build root partial order
root = StrictPartialOrder(nodes=[phase1, phase2_3, phase4, phase5])
root.order.add_edge(phase1, phase2_3)
root.order.add_edge(phase2_3, phase4)
root.order.add_edge(phase4, phase5)