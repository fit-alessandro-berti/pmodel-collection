# Generated from: 8f449b8f-9c6c-4995-b1ba-4ef5755709b3.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site assessment, environmental control system design, hydroponic installation, crop cycle planning, nutrient solution optimization, and integration of IoT monitoring devices. Additional activities cover pest management strategies, staff training on automated systems, marketing of fresh produce to local businesses, and ongoing data analysis for yield improvement. The process ensures sustainable urban agriculture by maximizing space efficiency, reducing water usage, and promoting local food production in an atypical but realistic business model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Assess = Transition(label='Site Assess')
Design_HVAC = Transition(label='Design HVAC')
Install_Hydroponics = Transition(label='Install Hydroponics')
Setup_Lighting = Transition(label='Setup Lighting')
Plan_Crops = Transition(label='Plan Crops')
Mix_Nutrients = Transition(label='Mix Nutrients')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Deploy_IoT = Transition(label='Deploy IoT')
Train_Staff = Transition(label='Train Staff')
Start_Cultivation = Transition(label='Start Cultivation')
Pest_Control = Transition(label='Pest Control')
Harvest_Crops = Transition(label='Harvest Crops')
Quality_Check = Transition(label='Quality Check')
Package_Goods = Transition(label='Package Goods')
Distribute_Produce = Transition(label='Distribute Produce')
Analyze_Data = Transition(label='Analyze Data')

# Build the POWL model as a StrictPartialOrder with order dependencies

# Core process: site to design to installation & setup (concurrent)
initial_setup = StrictPartialOrder(nodes=[Site_Assess, Design_HVAC, Install_Hydroponics, Setup_Lighting])
initial_setup.order.add_edge(Site_Assess, Design_HVAC)
initial_setup.order.add_edge(Design_HVAC, Install_Hydroponics)
initial_setup.order.add_edge(Design_HVAC, Setup_Lighting)
# hydroponics and lighting can be concurrent after Design HVAC
# No order between Install Hydroponics and Setup Lighting

# Crop planning & nutrient calibration after initial setup is done: Plan Crops, Mix Nutrients
crop_nutrient = StrictPartialOrder(nodes=[Plan_Crops, Mix_Nutrients])
# Both rely on completion of initial setup
# We'll connect initial_setup to crop_nutrient in the final PO

# Sensor calibration and IoT deployment after setup
calibrate_deploy = StrictPartialOrder(nodes=[Calibrate_Sensors, Deploy_IoT])
calibrate_deploy.order.add_edge(Calibrate_Sensors, Deploy_IoT)

# Staff training after sensor calibration and IoT deployment
train = Train_Staff

# Start cultivation depends on crop plan, nutrient mix, IoT deployment, and training
start_cultivation = Start_Cultivation

# Pest control (can be concurrent once cultivation started)
# Harvest (after pest control)
# Quality check, packaging, distribution (sequential)
post_cultivation_PO = StrictPartialOrder(nodes=[Pest_Control, Harvest_Crops, Quality_Check, Package_Goods, Distribute_Produce])
post_cultivation_PO.order.add_edge(Pest_Control, Harvest_Crops)
post_cultivation_PO.order.add_edge(Harvest_Crops, Quality_Check)
post_cultivation_PO.order.add_edge(Quality_Check, Package_Goods)
post_cultivation_PO.order.add_edge(Package_Goods, Distribute_Produce)

# Analyze Data can be concurrent with all post harvest steps or follow distribution
# We'll put it as concurrent with the final stage (like ongoing data analysis)
final_nodes = [post_cultivation_PO, Analyze_Data]

# Compose the full PO
# All nodes:
nodes = [initial_setup, crop_nutrient, calibrate_deploy, train, start_cultivation] + final_nodes

root = StrictPartialOrder(nodes=nodes)

# Add cross edges to enforce order dependency

# initial_setup --> crop_nutrient and calibrate_deploy
root.order.add_edge(initial_setup, crop_nutrient)
root.order.add_edge(initial_setup, calibrate_deploy)

# calibrate_deploy --> train
root.order.add_edge(calibrate_deploy, train)

# crop_nutrient --> start_cultivation
root.order.add_edge(crop_nutrient, start_cultivation)

# train --> start_cultivation
root.order.add_edge(train, start_cultivation)

# start_cultivation --> post_cultivation_PO
root.order.add_edge(start_cultivation, post_cultivation_PO)

# post_cultivation_PO and Analyze_Data run concurrently (no order), both final
# so no edge between them

# Return the final root