# Generated from: 6b8f9844-69a7-42e1-9177-36c5fad0b615.json
# Description: This process outlines the establishment of an urban vertical farming system that integrates hydroponics, IoT monitoring, and renewable energy sources to maximize crop yield in limited city spaces. It involves site evaluation, modular system design, nutrient solution preparation, environmental control calibration, and ongoing crop health analysis to ensure sustainable and efficient food production within urban environments. The process also includes waste recycling, energy optimization, and community engagement to promote local food security and reduce carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Design_Module = Transition(label='Design Module')
Install_Frames = Transition(label='Install Frames')
Setup_Hydroponics = Transition(label='Setup Hydroponics')
Prepare_Nutrients = Transition(label='Prepare Nutrients')
Configure_Sensors = Transition(label='Configure Sensors')
Calibrate_Climate = Transition(label='Calibrate Climate')
Plant_Seeding = Transition(label='Plant Seeding')
Monitor_Growth = Transition(label='Monitor Growth')
Adjust_Lighting = Transition(label='Adjust Lighting')
Recycle_Waste = Transition(label='Recycle Waste')
Analyze_Data = Transition(label='Analyze Data')
Optimize_Energy = Transition(label='Optimize Energy')
Harvest_Crops = Transition(label='Harvest Crops')
Community_Outreach = Transition(label='Community Outreach')
Maintenance_Check = Transition(label='Maintenance Check')
Report_Metrics = Transition(label='Report Metrics')

# Define loops and choices according to the description:

# Loop for ongoing crop health analysis & adjustments:
# * (Monitor Growth, Adjust Lighting) - repeated monitoring and adjusting lighting
monitor_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[Monitor_Growth, Adjust_Lighting])

# Maintenance loop: * (Maintenance Check, Repair/Adjust) 
# Since Repair/Adjust not explicitly defined, represent as a silent transition
repair_adjust = SilentTransition()
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[Maintenance_Check, repair_adjust])

# Choice for recycling waste and energy optimization which support sustainability
sustainability_choice = OperatorPOWL(operator=Operator.XOR, children=[Recycle_Waste, Optimize_Energy])

# Partial order structure representing the main flow:
# 1. Site Survey
# 2. Design Module
# 3. Install Frames
# 4. Setup Hydroponics and Prepare Nutrients run concurrently
# 5. Configure Sensors and Calibrate Climate run concurrently
# 6. Plant Seeding
# 7. Loop of Monitor Growth and Adjust Lighting (monitor_adjust_loop)
# 8. Sustainability choices (Recycle Waste or Optimize Energy)
# 9. Harvest Crops
# 10. Community Outreach
# 11. Maintenance loop (maintenance_loop)
# 12. Analyze Data and Report Metrics run concurrently

nodes = [
    Site_Survey,
    Design_Module,
    Install_Frames,
    Setup_Hydroponics,
    Prepare_Nutrients,
    Configure_Sensors,
    Calibrate_Climate,
    Plant_Seeding,
    monitor_adjust_loop,
    sustainability_choice,
    Harvest_Crops,
    Community_Outreach,
    maintenance_loop,
    Analyze_Data,
    Report_Metrics
]

root = StrictPartialOrder(nodes=nodes)

# Add ordering edges reflecting the main control flow ordering and concurrency

# Linear sequence Site Survey --> Design Module --> Install Frames
root.order.add_edge(Site_Survey, Design_Module)
root.order.add_edge(Design_Module, Install_Frames)

# Setup Hydroponics and Prepare Nutrients in parallel after Install Frames
root.order.add_edge(Install_Frames, Setup_Hydroponics)
root.order.add_edge(Install_Frames, Prepare_Nutrients)

# Configure Sensors and Calibrate Climate in parallel after Setup Hydroponics and Prepare Nutrients both done
root.order.add_edge(Setup_Hydroponics, Configure_Sensors)
root.order.add_edge(Prepare_Nutrients, Configure_Sensors)
root.order.add_edge(Setup_Hydroponics, Calibrate_Climate)
root.order.add_edge(Prepare_Nutrients, Calibrate_Climate)

# Plant Seeding after both Configure Sensors and Calibrate Climate
root.order.add_edge(Configure_Sensors, Plant_Seeding)
root.order.add_edge(Calibrate_Climate, Plant_Seeding)

# Loop of Monitor Growth and Adjust Lighting after Plant Seeding
root.order.add_edge(Plant_Seeding, monitor_adjust_loop)

# Sustainability choice after monitor_adjust_loop
root.order.add_edge(monitor_adjust_loop, sustainability_choice)

# Harvest Crops after sustainability_choice
root.order.add_edge(sustainability_choice, Harvest_Crops)

# Community Outreach after Harvest Crops
root.order.add_edge(Harvest_Crops, Community_Outreach)

# Maintenance loop after Community Outreach
root.order.add_edge(Community_Outreach, maintenance_loop)

# Analyze Data and Report Metrics run concurrently after maintenance loop
root.order.add_edge(maintenance_loop, Analyze_Data)
root.order.add_edge(maintenance_loop, Report_Metrics)

# No direct order between Analyze Data and Report Metrics - concurrent

# root is the resulting POWL model