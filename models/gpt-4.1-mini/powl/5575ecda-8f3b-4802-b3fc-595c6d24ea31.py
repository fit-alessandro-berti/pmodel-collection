# Generated from: 5575ecda-8f3b-4802-b3fc-595c6d24ea31.json
# Description: This process outlines the establishment of a fully operational urban vertical farm within a city environment. It involves site assessment, modular structure assembly, climate system integration, automated nutrient delivery setup, crop selection based on local demand, AI-driven growth monitoring, pest management using bio-controls, waste recycling, energy optimization, workforce training, compliance verification, marketing launch, and continuous process improvement to ensure sustainable high-yield production while minimizing environmental impact in an atypical urban agricultural setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Assess = Transition(label='Site Assess')
Design_Layout = Transition(label='Design Layout')
Module_Build = Transition(label='Module Build')
Install_Climate = Transition(label='Install Climate')
Setup_Nutrients = Transition(label='Setup Nutrients')
Select_Crops = Transition(label='Select Crops')
Deploy_Sensors = Transition(label='Deploy Sensors')
Calibrate_AI = Transition(label='Calibrate AI')
Bio_Pestcontrol = Transition(label='Bio Pestcontrol')
Recycle_Waste = Transition(label='Recycle Waste')
Optimize_Energy = Transition(label='Optimize Energy')
Train_Staff = Transition(label='Train Staff')
Verify_Compliance = Transition(label='Verify Compliance')
Launch_Marketing = Transition(label='Launch Marketing')
Process_Review = Transition(label='Process Review')

# Partial order model reflecting the process

# Logical ordering notes:
#       Site Assess --> Design Layout --> Module Build --> Install Climate --> Setup Nutrients
#       After Setup Nutrients:
#           Select Crops, Deploy Sensors, Bio Pestcontrol, Recycle Waste, Optimize Energy 
#           can run concurrently
#       After those concurrent activities, Train Staff happens
#       Then Verify Compliance
#       Then Launch Marketing
#       Then Process Review (continuous improvement) -- as last step

# Build the StrictPartialOrder with all nodes
root = StrictPartialOrder(
    nodes=[
        Site_Assess, 
        Design_Layout, 
        Module_Build, 
        Install_Climate, 
        Setup_Nutrients,
        Select_Crops, 
        Deploy_Sensors, 
        Bio_Pestcontrol, 
        Recycle_Waste, 
        Optimize_Energy,
        Train_Staff, 
        Verify_Compliance, 
        Launch_Marketing, 
        Process_Review,
        Calibrate_AI
    ]
)

# Add edges representing dependencies

root.order.add_edge(Site_Assess, Design_Layout)
root.order.add_edge(Design_Layout, Module_Build)
root.order.add_edge(Module_Build, Install_Climate)
root.order.add_edge(Install_Climate, Setup_Nutrients)

root.order.add_edge(Setup_Nutrients, Select_Crops)
root.order.add_edge(Setup_Nutrients, Deploy_Sensors)
root.order.add_edge(Setup_Nutrients, Bio_Pestcontrol)
root.order.add_edge(Setup_Nutrients, Recycle_Waste)
root.order.add_edge(Setup_Nutrients, Optimize_Energy)

# Calibrate AI depends on Deploy Sensors (Deploy Sensors --> Calibrate AI)
root.order.add_edge(Deploy_Sensors, Calibrate_AI)

# Train Staff depends on all of: Select Crops, Calibrate AI, Bio Pestcontrol, Recycle Waste, Optimize Energy
root.order.add_edge(Select_Crops, Train_Staff)
root.order.add_edge(Calibrate_AI, Train_Staff)
root.order.add_edge(Bio_Pestcontrol, Train_Staff)
root.order.add_edge(Recycle_Waste, Train_Staff)
root.order.add_edge(Optimize_Energy, Train_Staff)

# Then Verify Compliance after Train Staff
root.order.add_edge(Train_Staff, Verify_Compliance)

# Then Launch Marketing after Verify Compliance
root.order.add_edge(Verify_Compliance, Launch_Marketing)

# Then Process Review after Launch Marketing
root.order.add_edge(Launch_Marketing, Process_Review)