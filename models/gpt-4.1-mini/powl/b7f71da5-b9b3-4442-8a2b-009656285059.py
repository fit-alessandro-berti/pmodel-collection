# Generated from: b7f71da5-b9b3-4442-8a2b-009656285059.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farm within a repurposed industrial building. It involves site assessment, environmental analysis, infrastructure retrofitting, hydroponic system installation, crop selection, nutrient calibration, lighting optimization, climate control setup, labor training, and compliance verification. The process ensures sustainable food production in dense urban areas, integrating technology and agriculture to maximize yield while minimizing resource consumption and environmental impact. Continuous monitoring and adaptation phases guarantee long-term operational efficiency and product quality.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Risk_Audit = Transition(label='Risk Audit')
Design_Layout = Transition(label='Design Layout')
System_Retrofit = Transition(label='System Retrofit')
Install_Hydroponics = Transition(label='Install Hydroponics')
Select_Crops = Transition(label='Select Crops')
Calibrate_Nutrients = Transition(label='Calibrate Nutrients')
Setup_Lighting = Transition(label='Setup Lighting')
Control_Climate = Transition(label='Control Climate')
Train_Staff = Transition(label='Train Staff')
Quality_Test = Transition(label='Quality Test')
Compliance_Check = Transition(label='Compliance Check')
Launch_Pilot = Transition(label='Launch Pilot')
Monitor_Growth = Transition(label='Monitor Growth')
Adjust_Parameters = Transition(label='Adjust Parameters')
Harvest_Cycle = Transition(label='Harvest Cycle')

# Model the main linear workflow up to Launch Pilot
linear_nodes = [
    Site_Survey,
    Risk_Audit,
    Design_Layout,
    System_Retrofit,
    Install_Hydroponics,
    Select_Crops,
    Calibrate_Nutrients,
    Setup_Lighting,
    Control_Climate,
    Train_Staff,
    Quality_Test,
    Compliance_Check,
    Launch_Pilot
]

linear_po = StrictPartialOrder(nodes=linear_nodes)
# add the sequential order for linear nodes
for i in range(len(linear_nodes) - 1):
    linear_po.order.add_edge(linear_nodes[i], linear_nodes[i+1])

# Loop to represent continuous monitoring and adjustment cycle:
# LOOP(Monitor Growth, Adjust Parameters)
loop_monitor_adjust = OperatorPOWL(operator=Operator.LOOP, children=[Monitor_Growth, Adjust_Parameters])

# After Launch_Pilot, the loop cycle and Harvest_Cycle proceed concurrently.
# So we create a partial order with nodes: linear_po, loop_monitor_adjust, Harvest_Cycle

root = StrictPartialOrder(nodes=[linear_po, loop_monitor_adjust, Harvest_Cycle])
# Dependencies:
# linear_po --> loop_monitor_adjust and Harvest_Cycle (both start after Launch Pilot)
root.order.add_edge(linear_po, loop_monitor_adjust)
root.order.add_edge(linear_po, Harvest_Cycle)