# Generated from: 11676e90-cb77-4ecf-9c0d-bacd872209dc.json
# Description: This process involves establishing a multi-layered vertical farming system within an urban environment to maximize crop yield using limited space. It includes site analysis, modular structure assembly, hydroponic system installation, climate control calibration, nutrient solution formulation, automated lighting scheduling, pest monitoring with AI sensors, periodic crop health assessment, waste recycling integration, data collection for growth optimization, employee training on new technology, and continuous system maintenance to ensure sustainable production and minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Structure_Build = Transition(label='Structure Build')
Install_Hydroponics = Transition(label='Install Hydroponics')
Calibrate_Climate = Transition(label='Calibrate Climate')
Prepare_Nutrients = Transition(label='Prepare Nutrients')
Set_Lighting = Transition(label='Set Lighting')
Deploy_Sensors = Transition(label='Deploy Sensors')
Monitor_Pests = Transition(label='Monitor Pests')
Assess_Crops = Transition(label='Assess Crops')
Recycle_Waste = Transition(label='Recycle Waste')
Collect_Data = Transition(label='Collect Data')
Train_Staff = Transition(label='Train Staff')
Maintenance_Check = Transition(label='Maintenance Check')
Optimize_Growth = Transition(label='Optimize Growth')

# Model partial order reflecting the process flow and concurrency
# Order:
# Site Survey --> Design Layout --> Structure Build --> Install Hydroponics --> Calibrate Climate
#    --> Prepare Nutrients --> Set Lighting --> Deploy Sensors
# After Deploy Sensors: 
# Monitor Pests and Assess Crops can be concurrent
# Recycle Waste and Collect Data can be concurrent and follow Monitor Pests and Assess Crops
# Train Staff occurs concurrently but after Design Layout (assumption)
# Maintenance Check and Optimize Growth form a loop (maintenance and optimization cycle)
#
# Construct the loop for Maintenance_Check and Optimize_Growth:
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[Maintenance_Check, Optimize_Growth])

# Construct partial order nodes list
nodes = [
    Site_Survey, Design_Layout, Train_Staff, Structure_Build, Install_Hydroponics,
    Calibrate_Climate, Prepare_Nutrients, Set_Lighting, Deploy_Sensors,
    Monitor_Pests, Assess_Crops, Recycle_Waste, Collect_Data, maintenance_loop
]

root = StrictPartialOrder(nodes=nodes)

# Define order edges

root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Structure_Build)
root.order.add_edge(Design_Layout, Train_Staff)
root.order.add_edge(Structure_Build, Install_Hydroponics)
root.order.add_edge(Install_Hydroponics, Calibrate_Climate)
root.order.add_edge(Calibrate_Climate, Prepare_Nutrients)
root.order.add_edge(Prepare_Nutrients, Set_Lighting)
root.order.add_edge(Set_Lighting, Deploy_Sensors)

root.order.add_edge(Deploy_Sensors, Monitor_Pests)
root.order.add_edge(Deploy_Sensors, Assess_Crops)
root.order.add_edge(Monitor_Pests, Recycle_Waste)
root.order.add_edge(Assess_Crops, Collect_Data)

# Maintenance loop runs after Recycle_Waste and Collect_Data (assuming collected/processed data triggers maintenance)
root.order.add_edge(Recycle_Waste, maintenance_loop)
root.order.add_edge(Collect_Data, maintenance_loop)