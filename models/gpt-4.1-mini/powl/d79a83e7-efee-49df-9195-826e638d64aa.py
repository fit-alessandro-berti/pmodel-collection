# Generated from: d79a83e7-efee-49df-9195-826e638d64aa.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming operation within a metropolitan environment. It covers site selection, environmental assessment, regulatory compliance, modular infrastructure setup, crop selection based on local demand, integration of IoT sensors for real-time monitoring, nutrient circulation system design, automated lighting calibration, staff training on sustainable practices, implementation of pest control protocols without pesticides, marketing strategy development targeting local consumers, logistics planning for fresh produce distribution, continuous yield optimization through data analytics, and establishing community engagement programs to promote urban agriculture awareness and education.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Survey = Transition(label='Site Survey')
Env_Assessment = Transition(label='Env Assessment')
Reg_Compliance = Transition(label='Reg Compliance')
Modular_Setup = Transition(label='Modular Setup')
Crop_Selection = Transition(label='Crop Selection')
IoT_Integration = Transition(label='IoT Integration')
Nutrient_Flow = Transition(label='Nutrient Flow')
Light_Calibration = Transition(label='Light Calibration')
Staff_Training = Transition(label='Staff Training')
Pest_Control = Transition(label='Pest Control')
Market_Strategy = Transition(label='Market Strategy')
Logistics_Plan = Transition(label='Logistics Plan')
Yield_Analysis = Transition(label='Yield Analysis')
Data_Review = Transition(label='Data Review')
Community_Engage = Transition(label='Community Engage')

# Build the sequential partial order according to the described process flow
nodes = [
    Site_Survey,
    Env_Assessment,
    Reg_Compliance,
    Modular_Setup,
    Crop_Selection,
    IoT_Integration,
    Nutrient_Flow,
    Light_Calibration,
    Staff_Training,
    Pest_Control,
    Market_Strategy,
    Logistics_Plan,
    Yield_Analysis,
    Data_Review,
    Community_Engage
]

root = StrictPartialOrder(nodes=nodes)
order = root.order

order.add_edge(Site_Survey, Env_Assessment)
order.add_edge(Env_Assessment, Reg_Compliance)
order.add_edge(Reg_Compliance, Modular_Setup)
order.add_edge(Modular_Setup, Crop_Selection)
order.add_edge(Crop_Selection, IoT_Integration)
order.add_edge(IoT_Integration, Nutrient_Flow)
order.add_edge(Nutrient_Flow, Light_Calibration)
order.add_edge(Light_Calibration, Staff_Training)
order.add_edge(Staff_Training, Pest_Control)
order.add_edge(Pest_Control, Market_Strategy)
order.add_edge(Market_Strategy, Logistics_Plan)
order.add_edge(Logistics_Plan, Yield_Analysis)
order.add_edge(Yield_Analysis, Data_Review)
order.add_edge(Data_Review, Community_Engage)