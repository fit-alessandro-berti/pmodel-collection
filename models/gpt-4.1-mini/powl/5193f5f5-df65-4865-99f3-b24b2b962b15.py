# Generated from: 5193f5f5-df65-4865-99f3-b24b2b962b15.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm in a metropolitan environment. It involves site assessment, modular design planning, installation of hydroponic and aeroponic systems, integration of IoT sensors for environmental monitoring, seed selection based on microclimate data, nutrient solution formulation, automation programming, staff training on crop management, pest control using biocontrol agents, energy optimization through renewable sources, waste recycling protocols, harvest scheduling, packaging logistics, and continuous yield analysis to maximize production efficiency while minimizing environmental impact and ensuring sustainable urban agriculture practices.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Plan = Transition(label='Design Plan')
Module_Setup = Transition(label='Module Setup')
System_Install = Transition(label='System Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automation_Code = Transition(label='Automation Code')
Staff_Train = Transition(label='Staff Train')
Pest_Control = Transition(label='Pest Control')
Energy_Audit = Transition(label='Energy Audit')
Waste_Sort = Transition(label='Waste Sort')
Harvest_Plan = Transition(label='Harvest Plan')
Pack_Prep = Transition(label='Pack Prep')
Yield_Review = Transition(label='Yield Review')

# Model the process as a strict partial order:
# The natural order inferred from the description:
# Site Survey --> Design Plan --> Module Setup --> System Install --> Sensor Deploy
# Sensor Deploy --> Seed Select --> Nutrient Mix --> Automation Code
# Automation Code --> Staff Train --> Pest Control
# Pest Control --> Energy Audit --> Waste Sort
# Waste Sort --> Harvest Plan --> Pack Prep --> Yield Review

nodes = [
    Site_Survey, Design_Plan, Module_Setup, System_Install, Sensor_Deploy,
    Seed_Select, Nutrient_Mix, Automation_Code, Staff_Train, Pest_Control,
    Energy_Audit, Waste_Sort, Harvest_Plan, Pack_Prep, Yield_Review
]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(Site_Survey, Design_Plan)
root.order.add_edge(Design_Plan, Module_Setup)
root.order.add_edge(Module_Setup, System_Install)
root.order.add_edge(System_Install, Sensor_Deploy)
root.order.add_edge(Sensor_Deploy, Seed_Select)
root.order.add_edge(Seed_Select, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Automation_Code)
root.order.add_edge(Automation_Code, Staff_Train)
root.order.add_edge(Staff_Train, Pest_Control)
root.order.add_edge(Pest_Control, Energy_Audit)
root.order.add_edge(Energy_Audit, Waste_Sort)
root.order.add_edge(Waste_Sort, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Pack_Prep)
root.order.add_edge(Pack_Prep, Yield_Review)