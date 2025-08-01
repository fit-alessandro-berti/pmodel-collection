# Generated from: 36598120-a4a9-4fbc-90e5-28b3ed3c788e.json
# Description: This process outlines the complex steps involved in launching a vertical farming operation in an urban environment. It includes site selection considering zoning laws and sunlight access, modular infrastructure setup with hydroponic systems, climate control calibration, nutrient solution formulation, crop selection based on local demand, real-time environmental monitoring integration, pest management using bio-controls, workforce training on specialized equipment, marketing strategy focused on sustainability, distribution channel partnerships with local grocers, compliance with health and safety regulations, continuous yield optimization through data analytics, customer feedback loops for product improvement, and finally, scalability planning for future expansion into multiple urban sites.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Zoning_Check = Transition(label='Zoning Check')
Infrastructure_Setup = Transition(label='Infrastructure Setup')
System_Calibration = Transition(label='System Calibration')
Nutrient_Mix = Transition(label='Nutrient Mix')
Crop_Selection = Transition(label='Crop Selection')
Enviro_Monitoring = Transition(label='Enviro Monitoring')
Pest_Control = Transition(label='Pest Control')
Staff_Training = Transition(label='Staff Training')
Marketing_Plan = Transition(label='Marketing Plan')
Distributor_Link = Transition(label='Distributor Link')
Regulation_Audit = Transition(label='Regulation Audit')
Yield_Analysis = Transition(label='Yield Analysis')
Feedback_Review = Transition(label='Feedback Review')
Expansion_Plan = Transition(label='Expansion Plan')

# Partial order nodes including some partial concurrency:
# Based on description:
# 1) Site Survey and Zoning Check precede Infrastructure Setup
# 2) Infrastructure Setup precedes System Calibration
# 3) Nutrient Mix and Crop Selection depend on System Calibration (can be concurrent)
# 4) Enviro Monitoring, Pest Control, Staff Training can be concurrent after Nutrient Mix & Crop Selection
# 5) Marketing Plan and Distributor Link parallel but both after Enviro Monitoring, Pest Control, Staff Training
# 6) Regulation Audit after Distributor Link and Marketing Plan
# 7) Yield Analysis after Regulation Audit
# 8) Feedback Review follows Yield Analysis
# 9) Expansion Plan after Feedback Review

# Build first partial order PO1: Site Survey --> Zoning Check --> Infrastructure Setup --> System Calibration
# But description implies Site Survey and Zoning Check are concurrent and both lead Infrastructure Setup, safer to model them concurrent with Infrastructure_Setup after both.

# To simplify:
# Site Survey and Zoning Check concurrent
# Both to Infrastructure Setup
# Infrastructure Setup --> System Calibration
# System Calibration --> Nutrient Mix and Crop Selection (concurrent)
# Nutrient Mix and Crop Selection --> Enviro Monitoring, Pest Control, Staff Training (all concurrent)
# Enviro Monitoring, Pest Control, Staff Training --> Marketing Plan and Distributor Link (concurrent)
# Marketing Plan, Distributor Link --> Regulation Audit
# Regulation Audit --> Yield Analysis --> Feedback Review --> Expansion Plan

nodes = [
    Site_Survey, Zoning_Check,
    Infrastructure_Setup,
    System_Calibration,
    Nutrient_Mix, Crop_Selection,
    Enviro_Monitoring, Pest_Control, Staff_Training,
    Marketing_Plan, Distributor_Link,
    Regulation_Audit,
    Yield_Analysis,
    Feedback_Review,
    Expansion_Plan
]

root = StrictPartialOrder(nodes=nodes)
order = root.order

# Site Survey and Zoning Check before Infrastructure Setup
order.add_edge(Site_Survey, Infrastructure_Setup)
order.add_edge(Zoning_Check, Infrastructure_Setup)

# Infrastructure Setup before System Calibration
order.add_edge(Infrastructure_Setup, System_Calibration)

# System Calibration before Nutrient Mix and Crop Selection
order.add_edge(System_Calibration, Nutrient_Mix)
order.add_edge(System_Calibration, Crop_Selection)

# Nutrient Mix and Crop Selection before Enviro Monitoring, Pest Control, Staff Training
order.add_edge(Nutrient_Mix, Enviro_Monitoring)
order.add_edge(Nutrient_Mix, Pest_Control)
order.add_edge(Nutrient_Mix, Staff_Training)
order.add_edge(Crop_Selection, Enviro_Monitoring)
order.add_edge(Crop_Selection, Pest_Control)
order.add_edge(Crop_Selection, Staff_Training)

# Enviro Monitoring, Pest Control, Staff Training before Marketing Plan and Distributor Link
order.add_edge(Enviro_Monitoring, Marketing_Plan)
order.add_edge(Pest_Control, Marketing_Plan)
order.add_edge(Staff_Training, Marketing_Plan)
order.add_edge(Enviro_Monitoring, Distributor_Link)
order.add_edge(Pest_Control, Distributor_Link)
order.add_edge(Staff_Training, Distributor_Link)

# Marketing Plan and Distributor Link before Regulation Audit
order.add_edge(Marketing_Plan, Regulation_Audit)
order.add_edge(Distributor_Link, Regulation_Audit)

# Regulation Audit before Yield Analysis
order.add_edge(Regulation_Audit, Yield_Analysis)

# Yield Analysis before Feedback Review
order.add_edge(Yield_Analysis, Feedback_Review)

# Feedback Review before Expansion Plan
order.add_edge(Feedback_Review, Expansion_Plan)