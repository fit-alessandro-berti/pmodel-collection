# Generated from: 1c8d439e-57dd-4e1b-ae52-b26d090b1ed6.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm, integrating advanced hydroponics, IoT sensor networks, renewable energy sources, and automated harvesting systems. The process begins with site assessment and feasibility studies, followed by modular structure design tailored for limited urban spaces. Next, installation of climate control systems and nutrient delivery networks ensures optimal plant growth conditions. Integration of AI-driven monitoring and predictive maintenance reduces downtime and maximizes yield. Subsequent stages include staff training on system operations, trial planting phases to calibrate environmental parameters, and establishing logistics for produce distribution within city markets. This atypical yet realistic process requires coordination between architects, engineers, agronomists, and supply chain managers, highlighting the multidisciplinary nature of sustainable urban agriculture ventures.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Assess = Transition(label='Site Assess')
Design_Module = Transition(label='Design Module')
Install_Hydroponics = Transition(label='Install Hydroponics')
Setup_Sensors = Transition(label='Setup Sensors')
Configure_Climate = Transition(label='Configure Climate')
Install_Lighting = Transition(label='Install Lighting')
Connect_Energy = Transition(label='Connect Energy')
Program_AI = Transition(label='Program AI')
Test_Systems = Transition(label='Test Systems')
Train_Staff = Transition(label='Train Staff')
Trial_Planting = Transition(label='Trial Planting')
Monitor_Growth = Transition(label='Monitor Growth')
Adjust_Nutrients = Transition(label='Adjust Nutrients')
Schedule_Harvest = Transition(label='Schedule Harvest')
Plan_Logistics = Transition(label='Plan Logistics')
Distribute_Produce = Transition(label='Distribute Produce')

# Hydroponics & Climate Control partial order
hydro_climate = StrictPartialOrder(nodes=[
    Install_Hydroponics, Setup_Sensors, Configure_Climate, Install_Lighting, Connect_Energy
])
hydro_climate.order.add_edge(Install_Hydroponics, Setup_Sensors)
hydro_climate.order.add_edge(Install_Hydroponics, Configure_Climate)
hydro_climate.order.add_edge(Install_Hydroponics, Install_Lighting)
hydro_climate.order.add_edge(Install_Hydroponics, Connect_Energy)

# AI & Testing partial order
ai_test = StrictPartialOrder(nodes=[Program_AI, Test_Systems])
ai_test.order.add_edge(Program_AI, Test_Systems)

# Monitoring & Adjustments partial order (trial planting loop)
monitor_adj = StrictPartialOrder(nodes=[Monitor_Growth, Adjust_Nutrients])
monitor_adj.order.add_edge(Monitor_Growth, Adjust_Nutrients)

# Loop for trial planting, monitoring and adjustment (Trial_Planting -> (Monitor Growth -> Adjust Nutrients)* )
loop_monitor_adjust = OperatorPOWL(operator=Operator.LOOP, children=[Trial_Planting, monitor_adj])

# Logistics partial order
logistics = StrictPartialOrder(nodes=[Schedule_Harvest, Plan_Logistics, Distribute_Produce])
logistics.order.add_edge(Schedule_Harvest, Plan_Logistics)
logistics.order.add_edge(Plan_Logistics, Distribute_Produce)

# Assemble the main process as a StrictPartialOrder
root = StrictPartialOrder(nodes=[
    Site_Assess,
    Design_Module,
    hydro_climate,
    ai_test,
    Train_Staff,
    loop_monitor_adjust,
    logistics
])

# Define partial order dependencies:

# Site Assess --> Design Module
root.order.add_edge(Site_Assess, Design_Module)

# Design Module --> hydro_climate (installation of systems)
root.order.add_edge(Design_Module, hydro_climate)

# hydro_climate --> ai_test (integration of AI after installation)
root.order.add_edge(hydro_climate, ai_test)

# ai_test --> Train Staff
root.order.add_edge(ai_test, Train_Staff)

# Train Staff --> Loop for Trial Planting & Monitoring
root.order.add_edge(Train_Staff, loop_monitor_adjust)

# loop_monitor_adjust --> Schedule Harvest (logistics)
root.order.add_edge(loop_monitor_adjust, logistics)