# Generated from: 1f75a14b-3cf2-42f6-880c-3223d5ca77b6.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm within a repurposed industrial building. It involves site assessment, modular system design, advanced hydroponic installation, climate control calibration, automated nutrient delivery setup, energy optimization, crop planning, integrated pest management, and digital monitoring system integration. Additionally, it incorporates workforce training, regulatory compliance checks, pilot harvesting, data analysis, continuous improvement loops, and community engagement initiatives to ensure sustainability, productivity, and scalability in an unconventional agricultural environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Assess = Transition(label='Site Assess')
Design_Modules = Transition(label='Design Modules')
Install_Hydroponics = Transition(label='Install Hydroponics')
Calibrate_Climate = Transition(label='Calibrate Climate')
Setup_Nutrients = Transition(label='Setup Nutrients')
Optimize_Energy = Transition(label='Optimize Energy')
Plan_Crops = Transition(label='Plan Crops')
Manage_Pests = Transition(label='Manage Pests')
Integrate_Sensors = Transition(label='Integrate Sensors')
Train_Staff = Transition(label='Train Staff')
Compliance_Check = Transition(label='Compliance Check')
Pilot_Harvest = Transition(label='Pilot Harvest')
Analyze_Data = Transition(label='Analyze Data')
Improve_Process = Transition(label='Improve Process')
Engage_Community = Transition(label='Engage Community')

# Define the core sequential order of activities until pilot harvest
po1 = StrictPartialOrder(nodes=[
    Site_Assess, Design_Modules, Install_Hydroponics, Calibrate_Climate,
    Setup_Nutrients, Optimize_Energy, Plan_Crops, Manage_Pests, Integrate_Sensors,
    Train_Staff, Compliance_Check, Pilot_Harvest
])
po1.order.add_edge(Site_Assess, Design_Modules)
po1.order.add_edge(Design_Modules, Install_Hydroponics)
po1.order.add_edge(Install_Hydroponics, Calibrate_Climate)
po1.order.add_edge(Calibrate_Climate, Setup_Nutrients)
po1.order.add_edge(Setup_Nutrients, Optimize_Energy)
po1.order.add_edge(Optimize_Energy, Plan_Crops)
po1.order.add_edge(Plan_Crops, Manage_Pests)
po1.order.add_edge(Manage_Pests, Integrate_Sensors)
po1.order.add_edge(Integrate_Sensors, Train_Staff)
po1.order.add_edge(Train_Staff, Compliance_Check)
po1.order.add_edge(Compliance_Check, Pilot_Harvest)

# Loop for analysis and continuous improvement
# loop = *(Analyze_Data, Improve_Process)
loop_analysis = OperatorPOWL(operator=Operator.LOOP, children=[Analyze_Data, Improve_Process])

# After Pilot Harvest, do loop_analysis and then Engage Community concurrently
po2 = StrictPartialOrder(nodes=[loop_analysis, Engage_Community])
po2.order.add_edge(loop_analysis, Engage_Community)

# Connect Pilot Harvest to po2
root = StrictPartialOrder(nodes=[po1, po2])
root.order.add_edge(po1, po2)