# Generated from: 159e5543-27e3-44c1-a4bd-2cce128d6838.json
# Description: This process details the establishment of an urban vertical farming facility, integrating advanced hydroponics and IoT-based environmental controls. It begins with site evaluation and structural assessment, followed by modular system design and nutrient solution formulation. After installation, sensors are calibrated for optimal growth conditions, and AI-driven monitoring is initiated. The process includes crop selection based on local demand and seasonal factors, pest management through organic methods, and continuous data analysis to improve yield. Finally, harvested produce undergoes quality inspection before packaging and distribution to local markets, ensuring freshness and sustainability throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for activities
Site_Assess = Transition(label='Site Assess')
Structure_Check = Transition(label='Structure Check')
System_Design = Transition(label='System Design')
Nutrient_Mix = Transition(label='Nutrient Mix')
Install_Modules = Transition(label='Install Modules')
Sensor_Setup = Transition(label='Sensor Setup')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Select_Crops = Transition(label='Select Crops')
Seed_Planting = Transition(label='Seed Planting')
Monitor_Growth = Transition(label='Monitor Growth')
Pest_Control = Transition(label='Pest Control')
Data_Analyze = Transition(label='Data Analyze')
Harvest_Crops = Transition(label='Harvest Crops')
Quality_Check = Transition(label='Quality Check')
Pack_Produce = Transition(label='Pack Produce')
Market_Delivery = Transition(label='Market Delivery')

# First PO: Site Assess --> Structure Check
po1 = StrictPartialOrder(nodes=[Site_Assess, Structure_Check])
po1.order.add_edge(Site_Assess, Structure_Check)

# Second PO: System Design --> Nutrient Mix
po2 = StrictPartialOrder(nodes=[System_Design, Nutrient_Mix])
po2.order.add_edge(System_Design, Nutrient_Mix)

# Partial order of po2 then Install Modules
po3 = StrictPartialOrder(nodes=[po2, Install_Modules])
po3.order.add_edge(po2, Install_Modules)

# Partial order: Sensor Setup --> Calibrate Sensors
po4 = StrictPartialOrder(nodes=[Sensor_Setup, Calibrate_Sensors])
po4.order.add_edge(Sensor_Setup, Calibrate_Sensors)

# Partial order: Select Crops --> Seed Planting
po5 = StrictPartialOrder(nodes=[Select_Crops, Seed_Planting])
po5.order.add_edge(Select_Crops, Seed_Planting)

# Partial order: Monitor Growth --> Pest Control --> Data Analyze
po6 = StrictPartialOrder(nodes=[Monitor_Growth, Pest_Control, Data_Analyze])
po6.order.add_edge(Monitor_Growth, Pest_Control)
po6.order.add_edge(Pest_Control, Data_Analyze)

# Partial order: Harvest Crops --> Quality Check --> Pack Produce --> Market Delivery
po7 = StrictPartialOrder(nodes=[Harvest_Crops, Quality_Check, Pack_Produce, Market_Delivery])
po7.order.add_edge(Harvest_Crops, Quality_Check)
po7.order.add_edge(Quality_Check, Pack_Produce)
po7.order.add_edge(Pack_Produce, Market_Delivery)

# Compose installation step (po3) and sensor calibration steps (po4)
po8 = StrictPartialOrder(nodes=[po3, po4])
po8.order.add_edge(po3, po4)

# Compose crop selection (po5) and monitoring (po6) in partial order
po9 = StrictPartialOrder(nodes=[po5, po6])
po9.order.add_edge(po5, po6)

# Compose po8 (install+sensor) and po9 (crops+monitor)
po10 = StrictPartialOrder(nodes=[po8, po9])
po10.order.add_edge(po8, po9)

# Compose po10 then harvest sequence (po7)
po11 = StrictPartialOrder(nodes=[po10, po7])
po11.order.add_edge(po10, po7)

# Compose overall initial steps: po1 (site assess/struct) then po11 (all subsequent)
root = StrictPartialOrder(nodes=[po1, po11])
root.order.add_edge(po1, po11)