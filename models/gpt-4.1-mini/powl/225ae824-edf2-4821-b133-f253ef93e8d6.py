# Generated from: 225ae824-edf2-4821-b133-f253ef93e8d6.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming system within a metropolitan environment. It includes site assessment, environmental analysis, infrastructure integration, technology deployment, crop selection, nutrient management, automation setup, yield monitoring, and sustainable waste handling. The process ensures efficient space utilization, maximizes crop output, minimizes energy consumption through IoT-enabled devices, and integrates renewable energy sources. Additionally, it incorporates community engagement and compliance with urban agricultural regulations, aiming to create a resilient, scalable, and eco-friendly food production model tailored for densely populated cities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition objects
Site_Survey = Transition(label='Site Survey')
Climate_Study = Transition(label='Climate Study')
Design_Layout = Transition(label='Design Layout')
Secure_Permits = Transition(label='Secure Permits')
Install_Frames = Transition(label='Install Frames')
Set_Irrigation = Transition(label='Set Irrigation')
Deploy_Sensors = Transition(label='Deploy Sensors')
Select_Crops = Transition(label='Select Crops')
Mix_Nutrients = Transition(label='Mix Nutrients')
Configure_AI = Transition(label='Configure AI')
Start_Seeding = Transition(label='Start Seeding')
Monitor_Growth = Transition(label='Monitor Growth')
Adjust_Lighting = Transition(label='Adjust Lighting')
Harvest_Batches = Transition(label='Harvest Batches')
Process_Waste = Transition(label='Process Waste')
Engage_Community = Transition(label='Engage Community')
Report_Metrics = Transition(label='Report Metrics')

# One plausible ordering respecting dependencies and concurrency:

# Partial order nodes: all activities grouped by logical groupings

# Step 1: Site Survey and Climate Study can be concurrent
# Step 2: Design Layout (after both 1's)
# Step 3: Secure Permits (after Design Layout)
# Step 4: Install Frames, Set Irrigation, Deploy Sensors (concurrent after Permits)
# Step 5: Select Crops and Mix Nutrients (concurrent after frames/irrigation/sensors)
# Step 6: Configure AI (after crop selection and nutrients)
# Step 7: Start Seeding (after configure AI)
# Step 8: Monitor Growth and Adjust Lighting (concurrent, after Start Seeding)
# Step 9: Harvest Batches and Process Waste (concurrent, after monitor and adjust)
# Step 10: Engage Community and Report Metrics (concurrent, after harvest and waste)

nodes = [
    Site_Survey, Climate_Study,
    Design_Layout,
    Secure_Permits,
    Install_Frames, Set_Irrigation, Deploy_Sensors,
    Select_Crops, Mix_Nutrients,
    Configure_AI,
    Start_Seeding,
    Monitor_Growth, Adjust_Lighting,
    Harvest_Batches, Process_Waste,
    Engage_Community, Report_Metrics
]

root = StrictPartialOrder(nodes=nodes)

# Step 1: Site Survey and Climate Study can start concurrently: no edges needed.

# Step 2: Design Layout after both Site Survey and Climate Study
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Climate_Study, Design_Layout)

# Step 3: Secure Permits after Design Layout
root.order.add_edge(Design_Layout, Secure_Permits)

# Step 4: Install Frames, Set Irrigation, Deploy Sensors after Secure Permits
root.order.add_edge(Secure_Permits, Install_Frames)
root.order.add_edge(Secure_Permits, Set_Irrigation)
root.order.add_edge(Secure_Permits, Deploy_Sensors)

# Step 5: Select Crops and Mix Nutrients after installation steps (all three must complete)
root.order.add_edge(Install_Frames, Select_Crops)
root.order.add_edge(Set_Irrigation, Select_Crops)
root.order.add_edge(Deploy_Sensors, Select_Crops)

root.order.add_edge(Install_Frames, Mix_Nutrients)
root.order.add_edge(Set_Irrigation, Mix_Nutrients)
root.order.add_edge(Deploy_Sensors, Mix_Nutrients)

# Step 6: Configure AI after Select Crops and Mix Nutrients
root.order.add_edge(Select_Crops, Configure_AI)
root.order.add_edge(Mix_Nutrients, Configure_AI)

# Step 7: Start Seeding after Configure AI
root.order.add_edge(Configure_AI, Start_Seeding)

# Step 8: Monitor Growth and Adjust Lighting after Start Seeding (concurrent)
root.order.add_edge(Start_Seeding, Monitor_Growth)
root.order.add_edge(Start_Seeding, Adjust_Lighting)

# Step 9: Harvest Batches and Process Waste after monitor and adjust (both must complete)
root.order.add_edge(Monitor_Growth, Harvest_Batches)
root.order.add_edge(Adjust_Lighting, Harvest_Batches)
root.order.add_edge(Monitor_Growth, Process_Waste)
root.order.add_edge(Adjust_Lighting, Process_Waste)

# Step 10: Engage Community and Report Metrics after harvest and waste (both must complete)
root.order.add_edge(Harvest_Batches, Engage_Community)
root.order.add_edge(Process_Waste, Engage_Community)
root.order.add_edge(Harvest_Batches, Report_Metrics)
root.order.add_edge(Process_Waste, Report_Metrics)