# Generated from: 49d62836-fb25-4270-a3a9-611365acf3da.json
# Description: This process outlines the establishment of an urban vertical farming system designed to maximize crop yield in limited city spaces by integrating hydroponics, AI-driven climate control, and automated harvesting. It begins with site scouting and structural assessment, followed by modular system design tailored to specific crops. Installation includes environmental sensors, water recycling units, and LED lighting arrays. After setup, the system undergoes calibration and AI model training to optimize growth conditions. Routine maintenance and yield analysis ensure continuous improvement. The process also incorporates community engagement for education and local distribution logistics to minimize food miles, creating a sustainable urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Scouting = Transition(label='Site Scouting')
Structure_Check = Transition(label='Structure Check')
Modular_Design = Transition(label='Modular Design')
System_Install = Transition(label='System Install')
Sensor_Setup = Transition(label='Sensor Setup')
Water_Recycling = Transition(label='Water Recycling')
LED_Wiring = Transition(label='LED Wiring')
AI_Calibration = Transition(label='AI Calibration')
Model_Training = Transition(label='Model Training')
Crop_Planting = Transition(label='Crop Planting')
Climate_Control = Transition(label='Climate Control')
Harvest_Automate = Transition(label='Harvest Automate')
Yield_Analysis = Transition(label='Yield Analysis')
Maintenance = Transition(label='Maintenance')
Community_Engage = Transition(label='Community Engage')
Logistics_Plan = Transition(label='Logistics Plan')

# Installation partial order: Sensor_Setup, Water_Recycling, LED_Wiring concurrent under System_Install
install_PO = StrictPartialOrder(nodes=[Sensor_Setup, Water_Recycling, LED_Wiring])

# Calibration steps: AI_Calibration --> Model_Training
calib_PO = StrictPartialOrder(nodes=[AI_Calibration, Model_Training])
calib_PO.order.add_edge(AI_Calibration, Model_Training)

# Crop management partial order: Crop_Planting --> Climate_Control --> Harvest_Automate
crop_PO = StrictPartialOrder(nodes=[Crop_Planting, Climate_Control, Harvest_Automate])
crop_PO.order.add_edge(Crop_Planting, Climate_Control)
crop_PO.order.add_edge(Climate_Control, Harvest_Automate)

# Maintenance and Yield Analysis concurrent (no order)
maint_yield_PO = StrictPartialOrder(nodes=[Maintenance, Yield_Analysis])

# Community and Logistics concurrent
community_logistics_PO = StrictPartialOrder(nodes=[Community_Engage, Logistics_Plan])

# System installation includes install_PO ordered after Modular_Design and System_Install
install_inner_PO = StrictPartialOrder(nodes=[System_Install, install_PO])
install_inner_PO.order.add_edge(System_Install, install_PO)  # Link System_Install --> install_PO as a node

# But pm4py POWL does not support adding StrictPartialOrder as node directly,
# so we treat install_PO's nodes as subnodes of installation phase.
# Instead, build installation PO with nodes: System_Install plus its sub-activities concurrently after it:
installation_nodes = [System_Install, Sensor_Setup, Water_Recycling, LED_Wiring]
installation_PO = StrictPartialOrder(nodes=installation_nodes)
installation_PO.order.add_edge(System_Install, Sensor_Setup)
installation_PO.order.add_edge(System_Install, Water_Recycling)
installation_PO.order.add_edge(System_Install, LED_Wiring)

# The initial steps partial order: Site_Scouting --> Structure_Check --> Modular_Design
initial_PO = StrictPartialOrder(nodes=[Site_Scouting, Structure_Check, Modular_Design])
initial_PO.order.add_edge(Site_Scouting, Structure_Check)
initial_PO.order.add_edge(Structure_Check, Modular_Design)

# Chain all main phases:
# initial_PO --> installation_PO --> calib_PO --> crop_PO 
# Then maintenance + yield analysis concurrent after crop_PO
# Then community + logistics concurrent after that
# We create a PO including all these nodes and edges corresponding:

all_nodes = [
    Site_Scouting, Structure_Check, Modular_Design,
    System_Install, Sensor_Setup, Water_Recycling, LED_Wiring,
    AI_Calibration, Model_Training,
    Crop_Planting, Climate_Control, Harvest_Automate,
    Maintenance, Yield_Analysis,
    Community_Engage, Logistics_Plan
]

root = StrictPartialOrder(nodes=all_nodes)

# initial_PO edges
root.order.add_edge(Site_Scouting, Structure_Check)
root.order.add_edge(Structure_Check, Modular_Design)

# installation_PO edges
root.order.add_edge(Modular_Design, System_Install)
root.order.add_edge(System_Install, Sensor_Setup)
root.order.add_edge(System_Install, Water_Recycling)
root.order.add_edge(System_Install, LED_Wiring)

# calibration edges
root.order.add_edge(LED_Wiring, AI_Calibration)
root.order.add_edge(AI_Calibration, Model_Training)

# crop management edges
root.order.add_edge(Model_Training, Crop_Planting)
root.order.add_edge(Crop_Planting, Climate_Control)
root.order.add_edge(Climate_Control, Harvest_Automate)

# maintenance and yield analysis concurrent after crop_PO: both after Harvest_Automate
root.order.add_edge(Harvest_Automate, Maintenance)
root.order.add_edge(Harvest_Automate, Yield_Analysis)

# community engagement and logistics concurrent after maintenance and yield analysis
# Both depend on Maintenance and Yield_Analysis
root.order.add_edge(Maintenance, Community_Engage)
root.order.add_edge(Yield_Analysis, Community_Engage)
root.order.add_edge(Maintenance, Logistics_Plan)
root.order.add_edge(Yield_Analysis, Logistics_Plan)