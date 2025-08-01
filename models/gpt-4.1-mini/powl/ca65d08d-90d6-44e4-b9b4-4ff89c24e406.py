# Generated from: ca65d08d-90d6-44e4-b9b4-4ff89c24e406.json
# Description: This process outlines the establishment of an urban vertical farming facility designed to optimize limited city space for sustainable food production. It involves site selection within dense urban areas, modular system design, environmental control setup, crop selection based on microclimate data, automated nutrient delivery, and integration of IoT sensors for real-time monitoring. The process also includes staff training on vertical farming techniques, waste recycling protocols, and establishing supply chain links with local markets. The goal is to create a resilient, scalable, and eco-friendly food production system that leverages technology and urban infrastructure to reduce food miles and improve fresh produce availability in metropolitan regions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
System_Build = Transition(label='System Build')
Install_Sensors = Transition(label='Install Sensors')
Select_Crops = Transition(label='Select Crops')
Setup_Lighting = Transition(label='Setup Lighting')
Configure_Climate = Transition(label='Configure Climate')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automate_Watering = Transition(label='Automate Watering')
Test_Systems = Transition(label='Test Systems')
Train_Staff = Transition(label='Train Staff')
Waste_Plan = Transition(label='Waste Plan')
Market_Link = Transition(label='Market Link')
Data_Monitor = Transition(label='Data Monitor')
Optimize_Yield = Transition(label='Optimize Yield')

# Subprocess: Environmental Control Setup = Setup Lighting --> Configure Climate
Environmental_Control = StrictPartialOrder(nodes=[Setup_Lighting, Configure_Climate])
Environmental_Control.order.add_edge(Setup_Lighting, Configure_Climate)

# Subprocess: Automation Setup = Nutrient Mix --> Automate Watering
Automation_Setup = StrictPartialOrder(nodes=[Nutrient_Mix, Automate_Watering])
Automation_Setup.order.add_edge(Nutrient_Mix, Automate_Watering)

# Subprocess: Monitoring Loop = LOOP (Data Monitor, Optimize Yield)
Monitoring_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Data_Monitor, Optimize_Yield])

# Subprocess: Crop Management Setup = Select Crops --> (Environmental Control + Automation Setup + Test Systems)
# Environmental Control, Automation Setup, Test Systems run concurrently after Select Crops

Crop_Management_Nodes = [Select_Crops, Environmental_Control, Automation_Setup, Test_Systems]
Crop_Management = StrictPartialOrder(nodes=Crop_Management_Nodes)
Crop_Management.order.add_edge(Select_Crops, Environmental_Control)
Crop_Management.order.add_edge(Select_Crops, Automation_Setup)
Crop_Management.order.add_edge(Select_Crops, Test_Systems)

# Subprocess: Integration = Install Sensors --> (Crop Management + Monitoring Loop) run concurrently
Integration_Nodes = [Install_Sensors, Crop_Management, Monitoring_Loop]
Integration = StrictPartialOrder(nodes=Integration_Nodes)
Integration.order.add_edge(Install_Sensors, Crop_Management)
Integration.order.add_edge(Install_Sensors, Monitoring_Loop)

# Subprocess: Final Setup = Train Staff --> Waste Plan --> Market Link
Final_Setup = StrictPartialOrder(nodes=[Train_Staff, Waste_Plan, Market_Link])
Final_Setup.order.add_edge(Train_Staff, Waste_Plan)
Final_Setup.order.add_edge(Waste_Plan, Market_Link)

# Build Overall Process

# Core Construction = Site Survey --> Design Layout --> System Build --> Integration --> Final Setup
Core_Construction_Nodes = [Site_Survey, Design_Layout, System_Build, Integration, Final_Setup]
Core_Construction = StrictPartialOrder(nodes=Core_Construction_Nodes)
Core_Construction.order.add_edge(Site_Survey, Design_Layout)
Core_Construction.order.add_edge(Design_Layout, System_Build)
Core_Construction.order.add_edge(System_Build, Integration)
Core_Construction.order.add_edge(Integration, Final_Setup)

root = Core_Construction